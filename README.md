# Go game by Gavril Marinov

- Created with python 3.10.7  
- Pygame library required  
- Supports single player only  
- Japanese rules only  
- Death stones removal are mandatory for territorial calculations  
- With authentic sounds from a real go board from shin kaya wood and real yunzi stones

## Requirements

1. Installing the requiered modules

   ```pip
   pip install -r requirements.txt
   ```

   (*) All required module are added to `requirements.txt`

2. `tox` is used for automating testing and the usage of different virtualenvs.
   - Installation:
  
    ```pip
    pip install tox
    ```

   - Usage:
     - Configuration is done in `tox.ini` file. Currently formatting is configured (using `black`).  
     - Formatting the code

        ```bash
        tox -e format
        ```

     - Linting the code

        ```bash
        tox -e lint
        ```
