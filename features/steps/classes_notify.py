from behave import given, when, then

@given("tomorrow we have classes")
def classes_tomorrow(context):
    context.is_classes_tomorrow = True

@given("notification time is {hour:d}pm")
def set_notification_time(context, hour):
    context.notification_time = hour

@when("it is notification time")
def notification_time(context):
    context.is_notification_time = True

@when("it is {hour:d}pm")
def time_is(context, hour):
    context.hour = hour

@then("assistant says that tomorrow we have classes")
def va_notifies_about_classes_tomorrow(context):
    va_notifies = False
    is_notification_time = False

    if context.hour == context.notification_time:
        is_notification_time = True

    if context.is_classes_tomorrow and is_notification_time:
        va_notifies = True
    assert va_notifies

@then("assistant does nothing")
def va_does_nothing(context):
    va_notifies = False
    is_notification_time = False

    if context.hour == context.notification_time:
        is_notification_time = True

    if context.is_classes_tomorrow and is_notification_time:
        va_notifies = True
    assert va_notifies is False
