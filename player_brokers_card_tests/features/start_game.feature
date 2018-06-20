Feature: Game Flow
  Tests the basic flow of game mechanics between the player service, the card/action broker and
  the card service

  Background: Empty database
    Given an empty database

  @foo
  Scenario: Activate New Game
    Given a pending game:
      | game id | account ids |
      | 1337    | 11,13       |
    When player service receives request to activate pending player:
      | account id | phase     |
      | 11         | inactive  |
    And player service receives request to activate pending player:
      | account id | phase  |
      | 13         | action |
    When player service receives request for player status for account id "13"
    Then player service returns player status:
      | game id | game status | phase  |
      | 1337    | active      | action |
    When player service receives request for player status for account id "11"
    Then player service returns player status:
      | game id | game status | phase    |
      | 1337    | active      | inactive |

  @wip
  Scenario: Starting Game State
    Given an activated game:
      | game id | account ids |
      | 1337    | 11, 13      |
    When card broker receives request for game state for game id "1337"
    Then card broker returns expected game card state
    When player service receives request for card state for account id "11"
    Then player service returns player card state:
      | deck size | hand size | discard size |
      | 5         | 5         | 0            |
    When player service receives request for card state for account id "13"
    Then player service returns player card state:
      | deck size | hand size | discard size |
      | 5         | 5         | 0            |

  @wip
  Scenario: Player Buys Card
    Given an activated game:
      | game id | account ids |
      | 1337    | 11, 13      |
    And player in phase
      | account id | phase |
      | 11         | buy   |
    When player service receives buy request
      | account id | card |
      | 11         | 11   |
    Then player service returns player state with card "11" atop discard pile
