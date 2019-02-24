import os

ODT_FILE = os.getenv('ODT_FILE', '')
CONTEXT_FILE = os.getenv('CONTEXT_FILE', '')

if not ODT_FILE:
    raise Exception('No odt file specified. Specify file with ODT_FILE environment variable')

if not CONTEXT_FILE:
    raise Exception('No context file specified. Specify file with CONTEXT_FILE environment variable')

def get_context(file):
    ''' Extract context data from json file and returns a dict'''
    return context

def create_odt_file(file):
    return

def insert_data(file, context):
    return file

def convert_to_pdf(file):
    return new_file

def delete_file(filename):
    return

def main():
    return

main()
