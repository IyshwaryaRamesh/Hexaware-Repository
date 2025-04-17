class PropertyUtil:
    @staticmethod
    def load_properties(filepath):
        properties = {}
        with open(filepath, 'r') as file:
            for line in file:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=')
                    properties[key.strip()] = value.strip()
        return properties
