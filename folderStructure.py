import os
from venv import create

folders = {
    'data': ['processed', 'raw'],
    'docs': list(),
    'models': list(),
    'notebooks': list(), 
    'src': ['data', 'models', 'scripts'],
    'visualization': list()
}

path_to_project = './styleTransfer'

if __name__ == '__main__':

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