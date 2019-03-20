import json
import requests


def get_stream_content(url):
  r = requests.get(url, stream=True)

  for line in r.iter_lines():
    if line:
      decoded_line = line.decode('utf-8')
      print(json.loads(decoded_line))

if __name__ == '__main__':
  print "Hello World"
