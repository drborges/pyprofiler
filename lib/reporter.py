from os import path
from text_formatter import TextFormatter

class Reporter:

  def __init__(self, base_dir='./', default_formatter=TextFormatter()):
    self.base_dir = base_dir
    self.formatters = [default_formatter]

  def generate(self, profiles):
    for formatter in self.formatters:
      report_file_path = path.join(self.base_dir, 'report.' + formatter.type())
      with open(report_file_path, 'w') as f:
        f.write(formatter.format(profiles))

    return self