import tika
from tika import parser

tika.initVM()

parsed = parser.from_file('/path/to/file')
print(parsed["metadata"])
print(parsed["content"])
