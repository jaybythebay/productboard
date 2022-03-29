import os
import requests

PRODUCT_BOARD_API_KEY = os.getenv("PRODUCT_BOARD_JAY_WALL_TEST_INTEGRATION")
headers = {'Authorization': 'Bearer ' + PRODUCT_BOARD_API_KEY, 'X-Version': '1'}


def get_features_list():
    r = requests.get("https://api.productboard.com/features", headers=headers)
    print(r.text)

    features_dict = r.json()['data']
    print(type(features_dict))

    for feature in features_dict:
        print(feature)

    return list

ASANA_CLIENT_SECRET = os.getenv("ASANA_TEST_INTEGRATION_CLIENT_SECRET")

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


if __name__ == '__main__':
    get_features_list()


# r = requests.post('https://api.productboard.com/plugin-integrations', data=integration_settings, headers=headers)
# print(r.text)




# https://testintegration.productboard.com/