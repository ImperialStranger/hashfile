# hashfile

A python based tool get or verify integrity of a file.

# Usage

## Get hash of a file

Open your terminal emulator (example: Commmand Prompt, Powershell, Linux Terminal) then execute following command.
```bash
python hashfile.py get-hash --hash-func <hash function> --filepath <filename or it's path>
```

## Verify itegrity of a file
```bash
python hashfile.py verify --hash-func <hash function> --filepath <filename or it's path> --hash <Pass a hash to verify>
```

**NOTE:** For Windows users, If `hashfile.py` is compiled to `hashfile.exe` with python pyinstaller library, Python is no longer required. `hashfile` can be used instead of `python hashfile.py`
