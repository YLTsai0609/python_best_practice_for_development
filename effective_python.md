# Chapter 1 : Pythonic thinking

# Chapter 2 : Functions

## item 14 : 比起回傳None，不如使用例外情況(exceptions)

* i. 回傳None的Function容易產生不可預期的bug，因為None，zero，空字串在條件判斷式之下都會被認定是False
* ii. 使用例外情況而不使用None，可以透過try catch，把zero，空字串的條件判斷式分開來個別進行處理，並且在函數說明中，也能夠標明例外情況 

## Item 20: 使用None以及DocString來描述動態引數

1. Function中的預設引數只會在該模組(.py)被載入的時候執行一次，想要預設行為時建議使用None避免非預期外的行為
2. 例如 `when=datetime.now()` - 將會永遠得到一樣的時間，`error_default = {}` - 每次call函數時會得到"同一個"dict
3. 為了解決這種難以發現的bug，使用None，並在DocString中說明該引數要放的內容，就能避免這種奇怪的bug

## Item 21: 強制使用關鍵字引數讓程式碼更容易讀懂

1. 關鍵字引數可以讓可讀性更好
2. Python提供了`*`可放置在function argument中，意義為位置引數的結尾，後面的引數必為關鍵字引數，在function中如果有兩個以上的布林引數值，那麼你就應該使用它，避免以後看不懂自己的程式碼

# Chapter 3 : Classes and Ingeritance

## Item 25 : 使用super來初始化父類別 

1. python使用 method resolution order(MRO)來釐清據鑽石結構的繼承關係順序(使用super，並且可以呼叫`mro`方法)

2. 永遠使用super來初始化父類別，避免不預期的bug

# Chapter 4 : Metaclasses and Attributes

## Item 29 : 寫Python時避免使用Get和Set，必要時使用@property

1. 正常使用class時，不要使用Get和Set的設計
2. 使用`@property`來定義讀取物件屬性時的特殊行為，以及唯讀
3. 編寫`@property`時，遵從最小驚喜原則，避免神奇的bug產生
4. 確認你所編寫的`@property`方法是快速取得屬性，慢的，複雜的工作用一般屬性撰寫

## Item 30 : 考慮使用@property

1. 使用`@property`來增加class的新功能，能夠與原來物件屬性做區別
2. 在功能/需求未知的情況下可以使用`@property`，並依此設計更好的data model
3. 當`@property`使用情況過於繁重，應該考慮重構物件

# Chapter 5 : Concurrency and parallelism

# Chapter 6 : Built-in Modules

# Chapter 7 : Collaboration

# Chapter 8 : Production
