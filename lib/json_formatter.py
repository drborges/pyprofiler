import json

from datetime import datetime, timedelta

class JsonFormatter:
  def format(self, profiles):
    def format_time(datetime):
      microsecond_as_seconds = datetime.microsecond / 1000000.0
      return "%s:%s:%.4g" % (
        datetime.hour, datetime.minute, datetime.second + microsecond_as_seconds)

    def to_json(o):
      if hasattr(o, '__dict__'):
        return o.__dict__
      elif isinstance(o, datetime):
        return format_time(o)
      elif isinstance(o, timedelta):
        return str(o)

      raise UnexpectedValueError(o)

    return json.dumps(profiles, default=to_json, sort_keys=True)

class UnexpectedValueError(Exception):
  def __init__(self, field_value):
    self.field_value = field_value

  def __str__(self):
    return 'Unexpected field value : ' + self.field_value