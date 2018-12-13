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

  Scenario: VA notifies about tomorrow classes
    Given tomorrow we have classes
      And tomorrow is rainy
      And notification time is 9pm
     When it is 9pm
     Then assistant says that tomorrow we have classes
      And assistant advices to take umbrella

  Scenario: VA does not notify about tomorrow classes
    Given tomorrow we have classes
      And tomorrow is rainy
      And notification time is 10pm
     When it is 9pm
     Then assistant does nothing

  Scenario: VA does not notify about tomorrow classes
    Given tomorrow we have classes
      And tomorrow in saint-petersburg is Rainy
      And user is located in saint-petersburg
      And notification time is 9pm
     When it is 9pm
     Then assistant says that tomorrow we have classes
      And assistant advices to take umbrella



#  Scenario: User asks about schedule for tomorrow
#    Given tomorrow we have classes
#     When user asks about schedule
#     Then assistant provides schedule
