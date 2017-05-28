import json
import argparse


def load_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print('No file in directory')
        exit()


def pretty_print_json(data):
    parsed_json = json.dumps(data, ensure_ascii=False, indent=4,
                             sort_keys=True)
    return parsed_json


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Filepath')
    parser.add_argument('--path', type=str)
    args = parser.parse_args()
    parsed_json = load_data(args.path)
    parsed_json = pretty_print_json(parsed_json)
    print(parsed_json)
