from sure import expect
from mock import Mock, patch, mock_open

from reporter import Reporter
from text_formatter import TextFormatter

def mock_formatter():
  formatter = Mock()
  formatter.format = Mock(return_value="the formatted content")
  formatter.type = Mock(return_value='txt')
  return formatter

def test_should_use_text_formatter_by_default():
  formatters = Reporter().formatters

  expect(formatters).to.have.length_of(1)
  expect(formatters[0]).to.be.a(TextFormatter)

def test_generate_should_be_chainable():
  reporter = Reporter(default_formatter=mock_formatter())

  with patch('__builtin__.open', mock_open(), create=True):
    expect(reporter.generate('profiles')).to.equal(reporter)

def test_should_create_reports_in_current_dir_by_default():
  expect(Reporter().base_dir).to.equal('./')

def test_be_able_to_customize_reports_base_dir():
  expect(Reporter('/tmp').base_dir).to.equal('/tmp')

def test_should_generate_report():
  mocked_formatter = mock_formatter()
  mocked_open = mock_open()

  with patch('__builtin__.open', mocked_open, create=True):
    Reporter(default_formatter=mocked_formatter).generate('a profiles list')

  mocked_formatter.format.assert_called_once_with('a profiles list')
  mocked_open.assert_called_once_with('./report.txt', 'w')
  mocked_open().write.assert_called_once_with('the formatted content')
