from behave import given
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

@given('an empty database')
def clear_card_broker_db(context):
    """
    truncate existing table data for clean run
    """
    # Clear card broker tables
    engine = create_engine(context.urls.card_broker_db)
    Session = scoped_session(sessionmaker(bind=engine))
    session = Session()
    session.execute('TRUNCATE TABLE gamestate')
    session.execute('TRUNCATE TABLE playerstate')
    session.commit()
    session.close()

    # Clear player service tables
    engine = create_engine(context.env_urls.player_service_db)
    Session = scoped_session(sessionmaker(bind=engine))
    session = Session()
    session.execute('TRUNCATE TABLE players')
    session.commit()
    session.close()

    # clear card service table
    engine = create_engine(context.env_urls.card_service_db)
    Session = scoped_session(sessionmaker(bind=engine))
    session = Session()
    session.execute('TRUNCATE TABLE cardlists')
    session.commit()
    session.close()
