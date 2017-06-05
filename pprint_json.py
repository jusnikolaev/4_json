import json
import os
import argparse


def load_data(filepath):
    if not os.path.exists(filepath):
        return False
    with open(filepath, 'r', encoding='utf-8') as file:
        json_file = json.load(file)
        return json_file


def pretty_print_json(file_json):
    parsed_file = json.dumps(file_json, ensure_ascii=False, indent=4,
                             sort_keys=True)
    return parsed_file


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File path')
    parser.add_argument('--path', type=str)
    args = parser.parse_args()
    parsed_json = load_data(args.path)
    if parsed_json:
        parsed_json = pretty_print_json(parsed_json)
        print(parsed_json)
    else:
        print('No such directory')
