A script to convert odt files to pdf

## Usage

1. clone repo `clone git@github.com:HmzAli/odt-to-pdf-converter.git`
2. cd the project folder and run `pip install requirements.txt`
3. run `ODT_FILE=file.odt CONTEXT_FILE=context.json python main.py`

### ODT_FILE: Path to odt fle

### CONTEXT_FILE: Path to file containing variables info in json format

Context file content sample: 
```
{
  'name': 'Hmz',
  'address': 'abc'
}
