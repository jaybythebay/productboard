import json
import os
import requests
import asana

PRODUCT_BOARD_API_KEY = os.getenv("PRODUCT_BOARD_JAY_WALL_TEST_INTEGRATION")
ASANA_PERSONAL_ACCESS_TOKEN = os.getenv("ASANA_PRODUCT_BOARD_TEST_2")

product_board_headers = {'Authorization': 'Bearer ' + PRODUCT_BOARD_API_KEY,
           'X-Version': '1',
           'Content-Type': 'application/json'}

client = asana.Client.access_token(ASANA_PERSONAL_ACCESS_TOKEN)
asana_headers = {'Accept': 'application/json',
                 'Content-Type': 'application/json',
                 'Authorization': 'Bearer ' + ASANA_PERSONAL_ACCESS_TOKEN}


def get_features_list():
    r = requests.get("https://api.productboard.com/features", headers=product_board_headers)
    print(r.text)

    features_dict = r.json()['data']
    print(type(features_dict))

    for feature in features_dict:
        print(feature)

    return list


def asana_test_authentication():
    # https://developers.asana.com/docs/python-hello-world
    print(ASANA_PERSONAL_ACCESS_TOKEN)
    client = asana.Client.access_token(ASANA_PERSONAL_ACCESS_TOKEN)
    client.options['client_name'] = "hello_world_python"
    # Get your user info
    me = client.users.me()

    # Print out your information
    print("Hello world! " + "My name is " + me['name'] + "!")

    return None


def asana_test_authentication_with_requests():
    print(ASANA_PERSONAL_ACCESS_TOKEN)
    r = requests.get("https://app.asana.com/api/1.0/projects/1202041241966322/tasks", headers=asana_headers)
    print(r.text)

    return None


def asana_get_tasks_list():
    result = client.tasks.get_tasks_for_project('1202041241966322', {'param': 'value', 'param': 'value'}, opt_pretty=True)

    print(result)
    # # print(list(result))
    for item in result:
        print(item)

    return None


def create_plugin_integration():
    print(asana_headers)
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
                            "authorization": json.dumps(asana_headers)
                          }
                        }
                      }
                    }

    # r = requests.post('https://api.productboard.com/plugin-integrations',
    #                   data=integration_settings, headers=product_board_headers)

    r = requests.post('https://api.productboard.com/plugin-integrations', data=json.dumps(integration_settings), headers=product_board_headers)
    print(r.text)

    return None


if __name__ == '__main__':
    create_plugin_integration()
    # get_features_list()
    # asana_get_tasks_list()
    # create_plugin_integration()
    # asana_test_authentication_with_requests()







    # https://testintegration.productboard.com/