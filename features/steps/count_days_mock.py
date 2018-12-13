from behave import given, when, then
import datetime

@given("today is {date}")
def what_is_now(context, date):
    context.now = datetime.datetime.strptime(date, "%Y-%m-%d")

@when("user says count days to the {date}")
def date_to_count(context, date):
    context.user_date = datetime.datetime.strptime(date, "%Y-%m-%d")


@then("VA tells {difference:d} days")
def calculation(context, difference):
    x = context.user_date - context.now
    assert x.days == difference




