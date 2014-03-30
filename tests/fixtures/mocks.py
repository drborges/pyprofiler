from mock import Mock

def mock_formatter():
  formatter = Mock()
  formatter.format = Mock(return_value="the formatted content")
  formatter.type = Mock(return_value='txt')
  return formatter