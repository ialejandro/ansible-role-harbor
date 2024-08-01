class FilterModule(object):
    def filters(self):
        return {
            'combine_properties': self.combine_properties,
        }

    def combine_properties(self, properties_dict):
        # Loops over master properties dictionary and combines sub elements if enabled
        final_dict = {}
        for prop in properties_dict:
            if properties_dict[prop].get('enabled'):
                final_dict.update(properties_dict[prop].get('properties'))
        return final_dict
