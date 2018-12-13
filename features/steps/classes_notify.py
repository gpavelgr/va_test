from behave import given, when, then


@given("tomorrow we have classes")
def classes_tomorrow(context):
    context.is_classes_tomorrow = True

@given("notification time is {hour:d}pm")
def set_notification_time(context, hour):
    context.notification_time = hour

@given("tomorrow is rainy")
def tomorrow_is_rainy(context):
    context.tomorrow_weather = "Rainy"

@given("tomorrow in {location} is {weather}")
def tomorrow_weather_in_location(context, location, weather):
    if not context.weather_forecast:
        context.weather_forecast = {}
    context.weather_forecast[location] = weather



@given("user is located in {location}")
def user_is_located(context, location):
    pass



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
    context.va_notifies = va_notifies
    assert va_notifies

@then("assistant does nothing")
def va_does_nothing(context):
    va_notifies = False
    is_notification_time = False

    if context.hour == context.notification_time:
        is_notification_time = True

    if context.is_classes_tomorrow and is_notification_time:
        va_notifies = True
    context.va_notifies = va_notifies
    assert va_notifies is False


@then("assistant advices to take umbrella")
def va_take_umbrella(context):
    va_advices_to_take_umbrella = False

    from weather_mock import get_weather_for_tomorrow_mock as get_weather_for_tomorrow
    # from weather_mock import get_weather_for_tomorrow

    users_location = ""
    tomorrow_weather = ""

    # Get weather forecast
    forecast = get_weather_for_tomorrow("saint-petersburg")
    tomorrow_weather_forecast = forecast["text"]

    if context.va_notifies:
        if tomorrow_weather == tomorrow_weather_forecast:
            va_advices_to_take_umbrella = True
    assert va_advices_to_take_umbrella
