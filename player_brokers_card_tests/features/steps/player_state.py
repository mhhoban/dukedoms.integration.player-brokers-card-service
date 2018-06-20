from behave import given, then, when
from hamcrest import assert_that, equal_to

@when('player service receives request for player status for account id "{act_id}"')
def get_player_status(context, act_id):
    """
    queries player service for status of player for account_id
    """
    result, status = context.clients.player_service.playerInfo.get_player_info(
        playerId=int(context.player_ids[act_id])
    ).result()
    assert_that(status.status_code, equal_to(200))
    context.retrieved_player_status = result

@then('player service returns player status')
def assert_player_status(context):
    """
    asserts player status is that which is expected
    """
    assert_that(
        context.retrieved_player_status.game_status,
        equal_to(context.table.rows[0]['game status'])
    )
    assert_that(
        context.retrieved_player_status.turn_phase,
        equal_to(context.table.rows[0]['phase'])
    )
    assert_that(
        context.retrieved_player_status.game_id,
        equal_to(int(context.table.rows[0]['game id']))
    )
