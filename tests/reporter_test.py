from sure import expect
from mock import Mock, patch, mock_open
from fixtures.decorators import mock_dep
from fixtures.mocks import mock_formatter

from reporter import Reporter
from text_formatter import TextFormatter

def test_should_use_text_formatter_by_default():
  formatters = Reporter().formatters

  expect(formatters).to.have.length_of(1)
  expect(formatters[0]).to.be.a(TextFormatter)

@mock_dep(mock_fn=mock_formatter)
def test_generate_should_be_chainable(mocked_formatter):
  reporter = Reporter(default_formatter=mocked_formatter)

  with patch('__builtin__.open', mock_open(), create=True):
    expect(reporter.generate('profiles')).to.equal(reporter)

def test_should_create_reports_in_current_dir_by_default():
  expect(Reporter().base_dir).to.equal('./')

def test_be_able_to_customize_reports_base_dir():
  expect(Reporter('/tmp').base_dir).to.equal('/tmp')

@mock_dep(mock_fn=mock_formatter)
def test_should_generate_report(mocked_formatter):
  mocked_open = mock_open()

  with patch('__builtin__.open', mocked_open, create=True):
    Reporter(default_formatter=mocked_formatter).generate('a profiles list')

  mocked_formatter.format.assert_called_once_with('a profiles list')
  mocked_open.assert_called_once_with('./report.txt', 'w')
  mocked_open().write.assert_called_once_with('the formatted content')
