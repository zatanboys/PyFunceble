from PyFunceble.abstracts import Version
from PyFunceble.exceptions import WrongParameterType

from .base import ConverterBase


class InternalUrl(ConverterBase):
    """
    Converter of the internal URLs.

    .. note::
        The internal URLs are actually the URL that has nothing to
        do with what we are going to test.

        They are only relevant for the software itself.

    :param str data_to_convert: The data to convert
    """

    def __init__(self, data_to_convert):
        if not isinstance(data_to_convert, str):
            raise WrongParameterType(
                f"<data_to_convert> should be {str}, {type(data_to_convert)} given."
            )

        super().__init__(data_to_convert)

        self.converted_data = self.to_right_url()

    def to_right_url(self):
        """
        Process the conversion to the right URL.
        """

        if Version.is_local_dev():
            return self.data_to_convert.replace("master", "dev")
        return self.data_to_convert.replace("dev", "master")
