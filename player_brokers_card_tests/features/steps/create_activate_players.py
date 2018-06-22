from behave import given, then, when
from hamcrest import assert_that, equal_to

@given('a pending game')
def create_game(context):
    """
    creates a 'game' of a given number of players with the same game id
    """

    account_list = context.table.rows[0]['account ids'].split(',')
    game_id = int(context.table.rows[0]['game id'])

    for account_id in account_list:
        context.player_ids[account_id] = _create_player(
            game_id=game_id,
            account_id=account_id,
            client=context.clients.player_service
        )


@when('player service receives request to activate pending player')
def activate_pending_player(context):
    """
    send request to activate a pending player with a given turn phase
    """
    account_id = context.table.rows[0]['account id']

    player_id = context.player_ids[account_id]
    phase = context.table.rows[0]['phase']
    result, status = context.clients.player_service.gameOperations.activate_player(
        activatePlayerRequest = {
            'playerId': player_id,
            'startingPhase': phase
        }
    ).result()

    assert_that(status.status_code, equal_to(200))


def _create_player(game_id=None, account_id=None, client=None):
    """
    creates player based on game and account id
    """

    response = client.newPlayer.create_new_player(newPlayerRequest={
            'accountId': int(account_id),
            'gameId': int(game_id)
        }
    ).response()
    assert_that(response.incoming_response.status_code, equal_to(200))

    return response.result.player_id
