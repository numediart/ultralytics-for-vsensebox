[![Test Build](https://github.com/numediart/ultralytics-for-vsensebox/actions/workflows/test_build.yaml/badge.svg)](https://github.com/numediart/ultralytics-for-vsensebox/actions/workflows/test_build.yaml) [![PyPI](https://github.com/numediart/ultralytics-for-vsensebox/actions/workflows/publish.yaml/badge.svg)](https://github.com/numediart/ultralytics-for-vsensebox/actions/workflows/publish.yaml)

# Customized Ultralytics for VSenseBox

* Updated: **November 20, 2024**
* Synced with: v8.3.34 -> [[652e05e]](https://github.com/ultralytics/ultralytics/commit/652e05e833087652053346946827034a4a038025)
* All credit and info -> [[Original Ultralytics repo]](https://github.com/ultralytics/ultralytics)
* Customized for [`VSenseBox`](https://github.com/numediart/vsensebox):
    - Enable OpenCV multithreading
    - Remove restrictions on customized OpenCV
    - Disable dependency auto-install
    - Disable auto update

## Installation

* Install from [PyPI](https://pypi.org/project/vsensebox-ultralytics/):
    ```
    pip install vsensebox-ultralytics
    ``` 
* Or install from GitHub directly:
    ```
    pip install git+https://github.com/numediart/ultralytics-for-vsensebox.git
    ```
* Or build from source:

    <details><summary><ins>Click here to expand!</ins></summary>
    
    ```
    git clone https://github.com/numediart/ultralytics-for-vsensebox.git
    cd ultralytics-for-vsensebox
    python -m pip install --upgrade pip
    python -m pip install -U pip setuptools
    pip install wheel build
    python -m build --wheel --skip-dependency-check --no-isolatio
    cd dist
    ```
    
    </details>
