**ChatGPT:**

### 1. CLI Tools 優缺點總結及 Minimum Example

**1.1 Argparse**

* **優點**:
    
    * 標準庫自帶，無需額外安裝。
    * 非常靈活，支持複雜的參數解析。
* **缺點**:
    
    * 語法相對冗長，配置複雜的命令時代碼較多。
* **Minimum Example**:
    
    ```python
    import argparse
    
    def main():
        parser = argparse.ArgumentParser()
        parser.add_argument("name", help="Your name")
        args = parser.parse_args()
        print(f"Hello, {args.name}")
    
    if __name__ == "__main__":
        main()
    ```
    

**1.2 Click**

* **優點**:
    
    * 語法簡潔，易於擴展為複雜的 CLI 工具。
    * 提供自動幫助和文檔生成。
* **缺點**:
    
    * 需要安裝額外的庫。
* **Minimum Example**:
    
    ```python
    import click
    
    @click.command()
    @click.argument("name")
    def main(name):
        click.echo(f"Hello, {name}")
    
    if __name__ == '__main__':
        main()
    ```
    

**1.3 Fire**

* **優點**:
    
    * 可以快速將 Python 對象（函數、類）轉換為命令行工具。
    * 非常簡單直接，適合快速構建 CLI 工具。
* **缺點**:
    
    * 缺乏一些高級功能，如複雜的參數解析和自動生成文檔。
* **Minimum Example**:
    
    ```python
    import fire
    
    def main(name):
        print(f"Hello, {name}")
    
    if __name__ == "__main__":
        fire.Fire(main)
    ```
    

**1.4 Typer**

* **優點**:
    
    * 基於 Python 3.6+ 的 type hints，自動生成命令行參數。
    * 語法簡潔，適合現代 Python 開發，且支持完整的 Click 功能。
* **缺點**:
    
    * 依賴於 Click 庫，需要安裝額外的庫。
* **Minimum Example**:
    
    ```python
    import typer
    
    def main(name: str):
        print(f"Hello, {name}")
    
    if __name__ == '__main__':
        typer.run(main)
    ```
    

**1.5 Docopt**

* **優點**:
    
    * 語法直觀，透過 usage 語法定義接口，非常適合簡單的 CLI 工具。
* **缺點**:
    
    * 對於複雜的參數解析支持有限。
    * 需要額外的配置來將其打包為可執行命令。
* **Minimum Example**:
    
    ```python
    """Usage: script.py <name>"""
    
    from docopt import docopt
    
    def main():
        args = docopt(__doc__)
        print(f"Hello, {args['<name>']}")
    
    if __name__ == "__main__":
        main()
    ```
    

* * *

### 2. CLI Tools 使用 pyproject.toml 打包為 `cpml` 的 Binary File 的 Minimum Examples

#### 2.1 Argparse

**Pyproject.toml Example**:

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "cpml"
version = "0.1"
description = "A simple CLI tool using argparse"
dependencies = []

[project.scripts]
cpml = "cpml.cli:main"
```

**Reasoning**: Argparse 是 Python 標準庫的一部分，可以通過 `entry_points` 或 `scripts` 來生成 binary file。

* * *

#### 2.2 Click

**Pyproject.toml Example**:

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "cpml"
version = "0.1"
description = "A simple CLI tool using click"
dependencies = ["click"]

[project.scripts]
cpml = "cpml.cli:main"
```

**Reasoning**: Click 提供簡單的命令行參數解析和處理，可以通過 `entry_points` 生成可執行命令。

* * *

#### 2.3 Fire

**Pyproject.toml Example**:

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "cpml"
version = "0.1"
description = "A simple CLI tool using fire"
dependencies = ["fire"]

[project.scripts]
cpml = "cpml.cli:main"
```

**Reasoning**: Fire 可以通過 `entry_points` 將 Python 函數打包成可執行命令。

* * *

#### 2.4 Typer

**Pyproject.toml Example**:

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "cpml"
version = "0.1"
description = "A simple CLI tool using typer"
dependencies = ["typer"]

[project.scripts]
cpml = "cpml.cli:main"
```

**Reasoning**: Typer 基於 Click，完全支持通過 `entry_points` 打包成可執行命令。

* * *

#### 2.5 Docopt

**Pyproject.toml Example**:

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "cpml"
version = "0.1"
description = "A simple CLI tool using docopt"
dependencies = ["docopt"]

[project.scripts]
cpml = "cpml.cli:main"
```

**Reasoning**: Docopt 需要額外的配置來生成可執行的命令，但可以通過 `entry_points` 實現。

* * *

### 總結

* **Argparse**, **Click**, **Fire**, **Typer** 和 **Docopt** 都可以通過在 `pyproject.toml` 中配置 `entry_points` 或 `scripts` 打包為 binary file。
* 儘管 **Docopt** 的語法更直觀，但在處理複雜的 CLI 工具時可能不如其他工具靈活。


**Project Structure**:

```markdown
cpml/
├── cpml/
│   ├── __init__.py
│   ├── __main__.py
│   └── cli.py
└── pyproject.toml
```

其中，一旦 click, type 被 build up 起來，可以支援 binary file 的執行方式



### 2. Click

**Minimum Example:**

建立一個 Python package `cpml`:

```markdown
cpml/
├── __init__.py
├── __main__.py
└── cli.py
```

`cli.py`:

```python
import click

@click.command()
@click.argument("name")
def main(name):
    click.echo(f"Hello, {name}")

if __name__ == "__main__":
    main()
```

`__main__.py`:

```python
from .cli import main

main()
```

**執行方式:**

```bash
cpml John
```

**優點**: 語法簡潔，容易擴展。

**缺點**: 需要安裝 Click 庫。

* * *

### 3. Typer

**Minimum Example:**

建立一個 Python package `cpml`:

```markdown
cpml/
├── __init__.py
├── __main__.py
└── cli.py
```

`cli.py`:

```python
import typer

def main(name: str):
    print(f"Hello, {name}")

if __name__ == "__main__":
    typer.run(main)
```

`__main__.py`:

```python
from .cli import main

main()
```

**執行方式:**

```bash
cpml John
```

**優點**: 基於 type hints，自動生成命令行參數。

**缺點**: 需要安裝 Typer 和 Click 庫。

