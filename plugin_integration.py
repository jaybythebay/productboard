import json
import os
import requests

PRODUCT_BOARD_API_KEY = os.getenv("PRODUCT_BOARD_JAY_WALL_TEST_INTEGRATION")
ASANA_CLIENT_SECRET = os.getenv("ASANA_TEST_INTEGRATION_CLIENT_SECRET")
headers = {'Authorization': 'Bearer ' + PRODUCT_BOARD_API_KEY,
           'X-Version': '1',
           'Content-Type': 'application/json'}

def get_features_list():
    r = requests.get("https://api.productboard.com/features", headers=headers)
    print(r.text)

    features_dict = r.json()['data']
    print(type(features_dict))

    for feature in features_dict:
        print(feature)

    return list

def create_plugin_integration():
    integration_settings = {
                      "data": {
                        "integrationStatus": "enabled",
                        "type": "com.asana.app",
                        "name": "Asana",
                        "initialState": {
                          "label": "Push"
                        },
                        "action": {
                          "url": "https://app.asana.com/api/1.0/tasks",
                          "version": 1,
                          "headers": {
                            "authorization": ASANA_CLIENT_SECRET
                          }
                        }
                      }
                    }

    r = requests.post('https://api.productboard.com/plugin-integrations', data=json.dumps(integration_settings), headers=headers)
    print(r.text)

    return None


if __name__ == '__main__':
    create_plugin_integration()
    # get_features_list()







# https://testintegration.productboard.com/