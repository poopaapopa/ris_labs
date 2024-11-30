import os
from string import Template

class SQLProvider:
    def __init__(self, path):
        self._scripts = {}
        for file in os.listdir(path):
            if file.endswith('.sql'):
                self._scripts[file] = Template(open(f'{path}/{file}', 'r').read())

    def get(self, category, **params):
        if category not in self._scripts:
            raise ValueError(f'No such sql template {category}')
        return self._scripts[category].substitute(**params)