import json
import traceback


class CommonFunctions():

    def get_browser_mapping(scenario_name=None):
        try:
            if scenario_name is None:
                print('Scenario name :: ' + scenario_name + ' not defined in star.json, please re-check and confirm!')
            else:
                scenario_name = scenario_name.upper()
                browser_type = CommonFunctions().get_star_json('BROWSER_MAPPING', scenario_name)
                print('browser_type is ' + str(browser_type))
                return browser_type
        except:
            print(traceback.format_exc())
            print('Error while getting the browser mapping')

    def get_star_json(self, key_name, sub_key_name=None):
        try:
            print('inside json loads')
            data = json.loads(open('././star.json').read())
            if sub_key_name is None:
                key_name = key_name.upper()
                print('key_name :::' + key_name)
                print(data[key_name])
                return data[key_name]
            else:
                key_name = key_name.upper()
                sub_key_name = sub_key_name.upper()
                print('printing values now :: ' + data[key_name][sub_key_name])
                return data[key_name][sub_key_name]
        except:
            print(traceback.format_exc())
            print('Error reading data from star.json')
