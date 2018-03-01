import json
import sys

def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as json_content: 
    	data = json.load(json_content)
    return data


def pretty_print_json(data):
    print(json.dumps(data,ensure_ascii=False, sort_keys=True, indent=4))

if __name__ == '__main__':
    pretty_print_json(load_data(sys.argv[1]))
