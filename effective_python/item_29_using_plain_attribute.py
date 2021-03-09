# Item 29: Use plain attributes instead of get and set methods


# Programmers coming to Python from other languages may naturally try to
# implement explicit getter and setter methods in their classes.

# On the other hand, get and set exist in the other languages(Java, C#, ...)


class OldResistor(object):
    def __init__(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self, ohms):
        self._ohms = ohms

# getter, setter, such a boring stuff. When you code with this style
# the drawback comes when you are doing accumulation


r0 = OldResistor(50e3)
r0.set_ohms(r0.get_ohms() + 5e3)  # quite dirty and not elgant
print(r0.get_ohms())

# So use the plain attribute instead


class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


r1 = Resistor(50e3)
print('Before: %5r' % r1.ohms)
# These make operations like incrementing in place natural and clear.
r1.ohms = 10e3
print('After:  %5r' % r1.ohms)
r1.ohms += 5e3
print('Add 5e3: %5r' % r1.ohms)

# What if you want a special behavior when an attribute is set?
# Migrate the @property decorator as getter and corresponding setter


class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        """
        Due to the votage setting, 
        current will chagne

        Args:
            voltage ([int]): voltage
        """
        self._voltage = voltage
        self.current = self._voltage / self.ohms

# Now, assigning the voltage property will run the voltage setter method
# updaeing the current property of the object to mach


r2 = VoltageResistance(1e3)
print('Before: %5r amps' % r2.current)
r2.voltage = 10
print('After:  %5r amps' % r2.current)
r2.voltage += 20
print('After accumulation:  %5r amps' % r2.current)
print('After accumulation:  %5r voltage' % r2.voltage)

# Specifying a setter on property also let you perform type checking and validation


class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError("%f ohms must be > 0" % ohms)
        self._ohms = ohms

# Assigning and invalid resistance to the attribute will raise an exception


# r3 = BoundedResistance(0) # ValueError: 0.000000 ohms mush be > 0
# r3.ohms = 0 # ValueError: 0.000000 ohms mush be > 0
r2 = BoundedResistance(1e3)

# Why it happend?
# BoundedResistance.__init__ calls Resistor.__init__
# which assigns self.ohms = 0. That assignment cause the @ohms.setter
# method from BoundedResistance to be called, immediately running the validation code
# """before""" object construction has completed

# You can even use @property to make attributes from parent classes immutable.


class FixResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms

# well, the condition in setter cannot be solved, so it's immutable
# but in general case, you use @property only, then you make the attribute immutable


# @property is designed to describe the read-only stuff
# so don't put attribute-changable logic in the @property functions


class MysteriousResistor(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        self.voltage = self._ohms * self.current  # like this line
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms

# This leads to extremely bizarre behavior


r7 = MysteriousResistor(10)
r7.current = 0.01

print('Before:  %5r' % r7.voltage)  # 0
r7.ohms
print('After:   %5r' % r7.voltage)  # 0.1

# I just read the ohms, but my voltage changed!
# The best policy to only modify related object state in @property.setter

# Thnigs to remember
# 1. Define new class interfaces using simple public attributes, and avoid set and get methods
# 2. Use @property to define special behavior when attributes are accessed on your objects, if necessary.
# 3. Follow the rule of least suprise and void weird side effects in your @property methods
# 4. Ensure the @property methods are fast, do slow or complex work using mornal method
