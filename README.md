# mbox to eml

Convert email export format from `mbox` to `eml`. And some useful tools.

Tested on `python3.11` but should works fine on other versions of `python3`.

## Uasge:

➡️ **Convert** mbox to eml:

```bash
python3 mbox2eml.py -f spam.mbox -o output
```

👁️ **Read** eml file content in CLI:

```bash
python3 read_eml.py <input_eml_path>
```

🛠️ **Modify** a specified section of eml. (Modify this code as needed.)

```bash
python3 modify_eml.py <input_eml_path> <output_eml_path>
```
