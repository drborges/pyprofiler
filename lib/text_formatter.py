class TextFormatter:

  def type(self):
    return 'txt'

  def format(self, profiles):
    def format_time(datetime):
      return "%s:%s:%.4g" % (
        datetime.hour, datetime.minute, datetime.second + (datetime.microsecond / 1000000.0))

    return "\n".join(["%s took %s [started at: %s, finished at: %s]" % (
        profile_id,
        profile['elapsed'],
        format_time(profile['started']),
        format_time(profile['stopped'])
    ) for profile_id, profile in profiles.items()])