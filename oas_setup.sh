#!/bin/bash

#fetch card broker API Spec

curl https://raw.githubusercontent.com/mhhoban/dukedoms.card_broker_api/master/dukedoms_card_broker_api.yaml -O
mv dukedoms_card_broker_api.yaml player_brokers_card_tests/swagger/card_broker_api.yaml

curl https://raw.githubusercontent.com/mhhoban/dukedoms.card_service_api/master/dukedoms_card_service_api.yaml -O
mv dukedoms_card_service_api.yaml player_brokers_card_tests/swagger/card_service_api.yaml

curl https://raw.githubusercontent.com/mhhoban/dukedoms.player_service_api/master/dukedoms_player_service_api.yaml -O
mv dukedoms_player_service_api.yaml player_brokers_card_tests/swagger/player_service_api.yaml

curl https://raw.githubusercontent.com/mhhoban/dukedoms.action_broker_api/master/dukedoms_action_broker_api.yaml -O
mv dukedoms_action_broker_api.yaml player_brokers_card_tests/swagger/action_broker_api.yaml
