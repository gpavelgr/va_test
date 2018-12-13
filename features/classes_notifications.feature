Feature: Classes start notification
  Voice assistant will notify user about 

  Scenario: VA notifies about tomorrow classes
    Given tomorrow we have classes
      And notification time is 9pm
     When it is 9pm
     Then assistant says that tomorrow we have classes

  Scenario: VA does not notify about tomorrow classes
    Given tomorrow we have classes
      And notification time is 10pm
     When it is 9pm
     Then assistant does nothing

#  Scenario: User asks about schedule for tomorrow
#    Given tomorrow we have classes
#     When user asks about schedule
#     Then assistant provides schedule
