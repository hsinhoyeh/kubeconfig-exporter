def load_file_to_base64(filepath: str) -> str:
    import base64
    with open(filepath, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def convert_datapath_to_datafield(configpath: str, output: str):
    # keyed by clusters
    clusters_list = [{
        'from': 'certificate-authority',
        'to': 'certificate-authority-data',
    }]

    # keyed by users
    users_list = [{
        'from': 'client-certificate',
        'to': 'client-certificate-data',
    }, {
        'from': 'client-key',
        'to': 'client-key-data',
    }]

    import yaml
    with open(configpath, 'r') as f:
        kubeconfig_json = yaml.load(f, Loader=yaml.FullLoader)


    if kubeconfig_json['clusters']:
        for obj in kubeconfig_json['clusters']:
            cluster = obj['cluster']
            for convertor in clusters_list:
                if convertor['from'] in cluster:
                    cluster[convertor['to']] = load_file_to_base64(cluster[convertor['from']])
                    del cluster[convertor['from']]

    if kubeconfig_json['users']:
        for obj in kubeconfig_json['users']:
            user = obj['user']
            for convertor in users_list:
                if convertor['from'] in user:
                    user[convertor['to']] = load_file_to_base64(user[convertor['from']])
                    del user[convertor['from']]
    if output == 'json':
        import json
        print(json.dumps(kubeconfig_json, indent=2))
    else:
        print(yaml.dump(kubeconfig_json))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--to-data', action='store_true', help='convert path file to static data field', dest="toData")
    parser.add_argument('-f', '--filename', default='/.kube/config', help='convert path file to static data field', dest="filename")
    parser.add_argument('-o', '--output', default='yaml',
            choices=['yaml','json'], help='output format (default: yaml)', dest="output")
    args = parser.parse_args()
    if args.toData:
        convert_datapath_to_datafield(args.filename, args.output)

