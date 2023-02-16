from geoips.interfaces.base import BaseInterface, BasePlugin


class ReadersInterface(BaseInterface):
    name = "readers"
    deprecated_family_attr = "reader_type"
    required_args = {"standard": ["fnames"]}
    required_kwargs = {
        "standard": ["metadata_only", "chans", "area_def", "self_register"]
    }


readers = ReadersInterface()
