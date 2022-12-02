from geoips.interfaces.base_interface import BaseInterface, BaseInterfacePlugin


class FilenameFormattersInterface(BaseInterface):
    name = 'filename_formatters'
    entry_point_group = 'filename_formats'
    deprecated_family_attr = 'filename_type'

    def find_duplicates(self, *args, **kwargs):
        try:
            func = self.get_plugin_attr(name, 'find_duplicates')
        except AttributeError:
            raise AttributeError(f'Plugin {name} does not have a "find_duplicates" function.')

        duplicates = func()

    def remove_duplicates(self):
        duplicates = self.find_duplicates()


filename_formatters = FilenameFormattersInterface()


class FilenameFormattersInterfacePlugin(BaseInterfacePlugin):
    interface = filename_formatters
