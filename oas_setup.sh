#!/bin/bash

#fetch card broker API Spec

curl https://raw.githubusercontent.com/mhhoban/dukedoms.card_broker_api/master/dukedoms_card_broker_api.yaml -O
mv dukedoms_card_broker_api.yaml card_broker/swagger/card_broker_api.yaml

curl https://raw.githubusercontent.com/mhhoban/dukedoms.card_service_api/master/dukedoms_card_service_api.yaml -O
mv dukedoms_card_service_api.yaml card_broker/swagger/card_service_api.yaml
