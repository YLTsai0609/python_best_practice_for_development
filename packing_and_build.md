# PyProjects.toml

* PEP 518 – Specifying Minimum Build System Requirements for Python Projects
* PEP 621 – Storing project metadata in pyproject.toml

**ChatGPT:**

`pyproject.toml` 是一個用於 Python 項目配置的文件格式，主要目的是標準化項目配置文件的結構和內容，並提升工具的兼容性和可擴展性。它最早由 [PEP 518](https://www.python.org/dev/peps/pep-0518/) 提出的，後來 PEP 621 也對其進行了擴展和改進。

### `pyproject.toml` 的基本結構

`pyproject.toml` 文件是基於 TOML（Tom's Obvious, Minimal Language）格式的，通常包含以下幾個部分：

1. **[build-system]**：指定構建系統及其需求，例如包構建工具和版本。這是 PEP 518 定義的部分。
    
    ```toml
    [build-system]
    requires = ["setuptools>=42", "wheel"]
    build-backend = "setuptools.build_meta"
    ```
    
2. **[tool]**：用於配置各種工具的區域，例如 `pytest`、`black` 或 `mypy` 等。
    
    ```toml
    [tool.black]
    line-length = 88
    ```
    
3. **[project]**：PEP 621 提供的擴展，用於定義項目元數據，如包名、版本、依賴等。
    
    ```toml
    [project]
    name = "my_project"
    version = "0.1.0
    ```



**ChatGPT:**

PEP 518 和 PEP 621 都涉及 `pyproject.toml` 文件的使用和標準化，這些 PEP 定義了如何使用 `pyproject.toml` 來配置 Python 項目。以下是它們的介紹及與 `pyproject.toml` 的關係：

### PEP 518
* `build-system` by setuptools and wheels

**PEP 518**：這個提案標準化了 Python 項目的構建系統配置，並引入了 `pyproject.toml` 文件來指定構建系統和其要求。具體內容如下：

* **目的**：定義如何使用 `pyproject.toml` 來指定構建系統（例如 setuptools 或 flit）及其需求，這樣在構建 Python 包時，構建工具可以獲得所需的依賴和配置。
    
* **配置**：通過在 `pyproject.toml` 文件中添加 `[build-system]` 部分，指定需要的構建工具和版本。
    
    ```toml
    [build-system]
    requires = ["setuptools>=42", "wheel"]
    build-backend = "setuptools.build_meta"
    ```
    

### PEP 621

**PEP 621**：這個提案擴展了 `pyproject.toml` 的用法，添加了項目元數據的標準配置部分。具體內容如下：

* **目的**：提供一種標準化的方式來描述 Python 項目的元數據，如名稱、版本、作者、依賴等，取代傳統的 `setup.py` 和 `setup.cfg` 文件。
    
* **配置**：通過在 `pyproject.toml` 文件中添加 `[project]` 部分來指定項目元數據。
    
    ```toml
    [project]
    name = "my_project"
    version = "0.1.0"
    description = "A sample Python project"
    authors = [{name = "John Doe", email = "john.doe@example.com"}]
    dependencies = ["requests", "numpy"]
    ```
    

### 沒有 `pyproject.toml` 時的配置方式

在 `pyproject.toml` 被引入之前，Python 項目的配置通常使用以下文件：

* **`setup.py`**：這是 Python 包的傳統配置文件，用於指定包的元數據、安裝需求和構建邏輯。這個文件使用 Python 語法編寫，適用於 `setuptools`。
    
    ```python
    from setuptools import setup
    
    setup(
        name='my_project',
        version='0.1.0',
        description='A sample Python project',
        author='John Doe',
        author_email='john.doe@example.com',
        packages=['my_project'],
        install_requires=['requests', 'numpy'],
    )
    ```
    
* **`setup.cfg`**：這是一個配置文件，用於描述包的元數據和配置，通常與 `setup.py` 配合使用。它使用 `.ini` 格式編寫。
    
    ```ini
    [metadata]
    name = my_project
    version = 0.1.0
    description = A sample Python project
    author = John Doe
    author_email = john.doe@example.com
    
    [options]
    packages = find:
    install_requires =
        requests
        numpy
    ```
    

`pyproject.toml` 的引入旨在統一和簡化配置方式，使得不同的工具和構建系統能夠更好地協同工作，並使項目配置更加清晰和一致。
