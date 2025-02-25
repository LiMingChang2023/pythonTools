import os
from argparse import ArgumentParser
from venv import create

folders = {
    'data': ['processed', 'raw'],
    'docs': list(),
    'models': list(),
    'notebooks': list(), 
    'src': ['data', 'models', 'scripts'],
}

def parse_arguments():
    parser = ArgumentParser(description="Create project folder structure and venv")
    parser.add_argument('--path', type=str, default='./', 
                        help="Path to the project directory")
    return parser.parse_args()

if __name__ == '__main__':

    args = parse_arguments()
    path_to_project = args.path

    for folder in folders:
        path = os.path.join(path_to_project, folder)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f'"{folder: <20}" created')
        else:
            print(f'"{folder: <20}" existed')
        for sub_folder in folders[folder]:
            sub_path = os.path.join(path, sub_folder)
            if not os.path.exists(sub_path):
                os.makedirs(sub_path)
                print(f'   "{sub_folder: <10}" created')
            else:
                print(f'   "{sub_folder: <10}" existed')

    else:
        print('project folder construct complete')
    
    create(os.path.join(path_to_project, '.venv'))
