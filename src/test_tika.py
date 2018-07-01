import tika
from tika import parser

tika.initVM()

parsed = parser.from_file('data/raw/1990.docx')
print(parsed["metadata"])
print(parsed["content"])
