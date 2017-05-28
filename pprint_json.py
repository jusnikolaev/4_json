import json
import os
import argparse


def load_data(filepath):
    if not os.path.exists(filepath):
        print('No file in directory')
        exit()
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def pretty_print_json(file_json):
    parsed_file = json.dumps(file_json, ensure_ascii=False, indent=4,
                             sort_keys=True)
    return parsed_file


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File path')
    parser.add_argument('--path', type=str)
    args = parser.parse_args()
    parsed_json = load_data(args.path)
    parsed_json = pretty_print_json(parsed_json)
    print(parsed_json)
