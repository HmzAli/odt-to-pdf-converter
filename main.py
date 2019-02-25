import os
import subprocess
import json

from pyopendoc import opendocument, writer
from tempfile import NamedTemporaryFile

ODT_FILE = os.getenv('ODT_FILE', '')
CONTEXT_FILE = os.getenv('CONTEXT_FILE', '')

if not ODT_FILE:
    raise Exception('No odt file specified. Specify with ODT_FILE environment variable')

if not CONTEXT_FILE:
    raise Exception('No context file specified. Specify with CONTEXT_FILE environment variable')

def get_context(filename):
    with open(filename, 'r') as f:
        context = json.loads(f.read())
    return context

def insert_data(file, context):
    for key, value in context.items():
        file.set_variable(key, value)
    return file

def convert_to_pdf(file):
    return new_file

def delete_file(filename):
    return

def main():
    context = get_context(CONTEXT_FILE)
    odt_file = writer.OpenWriterDocument(filepath=ODT_FILE)
    updated_odt_file = insert_data(odt_file, context)
    odt_bytes = updated_odt_file.save_to_bytes()
    updated_odt_file.close()

    temp_odt_file = NamedTemporaryFile(suffix='.odt', delete=True)
    temp_odt_file.write(odt_bytes)

    subprocess.call(['libreoffice', '--headless', '--convert-to', 'pdf', temp_odt_file.name, '--outdir', 'files'])
    temp_odt_file.close()

main()
