class FilterModule(object):
    def filters(self):
        return {
            'combine_properties': self.combine_properties,
        }

    def combine_properties(self, properties_dict):
        """Loops over properties dictionary and combines sub elements if enabled."""
        if not isinstance(properties_dict, dict):
            raise TypeError("combine_properties expects a dict, got %s" % type(properties_dict).__name__)

        final_dict = {}
        for prop in properties_dict:
            enabled = properties_dict[prop].get('enabled', False)
            if isinstance(enabled, str):
                enabled = enabled.lower() in ('true', 'yes', '1')
            if enabled:
                final_dict.update(properties_dict[prop].get('properties', {}))
        return final_dict
