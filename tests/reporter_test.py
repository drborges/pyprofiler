from sure import expect
from mock import Mock

from reporter import Reporter
from text_formatter import TextFormatter

def test_should_use_text_formatter_by_default():
  formatters = Reporter().formatters

  expect(formatters).to.have.length_of(1)
  expect(formatters[0]).to.be.a(TextFormatter)

def test_generate_should_be_chainable():
  reporter = Reporter()

  formatter = reporter.formatters[0]
  formatter.format = Mock(return_value="the formatted content")

  expect(reporter.generate('profiles')).to.equal(reporter)

def test_should_create_reports_in_current_dir_by_default():
  expect(Reporter().base_dir).to.equal('./')

def test_be_able_to_customize_reports_base_dir():
  expect(Reporter('/tmp').base_dir).to.equal('/tmp')

def test_should_generate_report():
  reporter = Reporter()
  formatter = reporter.formatters[0]
  formatter.format = Mock(return_value="the formatted content")

  reporter.generate('a profiles list')

  formatter.format.assert_called_once_with('a profiles list')
  with open('./report.txt', 'r') as f:
    expect(f.read()).to.equal("the formatted content")