import base64
import yaml
import os


def file_encry_base64(data):
    try:
        dicts = str_match('base64,', data)
        for k, v in dicts.items():
            with open(v[1], 'rb') as f:
                content = f.read()
                encry_content = (base64.b64encode(content))
                if ';base64' in v[0]:
                    data[k] = v[0] + ',' + encry_content.decode()
                else:
                    data[k] = encry_content.decode()
    except Exception as e:
        print(e)


def str_match(match_str, data):
    result = {}
    for key, value in data.items():
        if match_str in value:
            value_list = value.split(',')
            result[key] = value_list
    return result


def file_binary(filepath):
    with open(filepath, 'rb') as fb:
        return [('file', fb.read())]


def read_yaml(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f.read())


if __name__ == '__main__':
    APIDIR = os.path.join(os.getcwd(), 'api')
    data = read_yaml(os.path.join(APIDIR, 'get_org_list_for_phone.yaml'))
    print(data)
