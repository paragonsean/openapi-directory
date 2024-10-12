# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ChallengeData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, additional_information: str=None, data: List[str]=None, image: str=None, image_link: str=None, otp_format: str=None, otp_max_length: int=None):
        """ChallengeData - a model defined in OpenAPI

        :param additional_information: The additional_information of this ChallengeData.
        :param data: The data of this ChallengeData.
        :param image: The image of this ChallengeData.
        :param image_link: The image_link of this ChallengeData.
        :param otp_format: The otp_format of this ChallengeData.
        :param otp_max_length: The otp_max_length of this ChallengeData.
        """
        self.openapi_types = {
            'additional_information': str,
            'data': List[str],
            'image': str,
            'image_link': str,
            'otp_format': str,
            'otp_max_length': int
        }

        self.attribute_map = {
            'additional_information': 'additionalInformation',
            'data': 'data',
            'image': 'image',
            'image_link': 'imageLink',
            'otp_format': 'otpFormat',
            'otp_max_length': 'otpMaxLength'
        }

        self._additional_information = additional_information
        self._data = data
        self._image = image
        self._image_link = image_link
        self._otp_format = otp_format
        self._otp_max_length = otp_max_length

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ChallengeData':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The challengeData of this ChallengeData.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def additional_information(self):
        """Gets the additional_information of this ChallengeData.

        Additional explanation for the PSU to explain e.g. fallback mechanism for the chosen SCA method. The TPP is obliged to show this to the PSU. 

        :return: The additional_information of this ChallengeData.
        :rtype: str
        """
        return self._additional_information

    @additional_information.setter
    def additional_information(self, additional_information):
        """Sets the additional_information of this ChallengeData.

        Additional explanation for the PSU to explain e.g. fallback mechanism for the chosen SCA method. The TPP is obliged to show this to the PSU. 

        :param additional_information: The additional_information of this ChallengeData.
        :type additional_information: str
        """

        self._additional_information = additional_information

    @property
    def data(self):
        """Gets the data of this ChallengeData.

        A collection of strings as challenge data.

        :return: The data of this ChallengeData.
        :rtype: List[str]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ChallengeData.

        A collection of strings as challenge data.

        :param data: The data of this ChallengeData.
        :type data: List[str]
        """

        self._data = data

    @property
    def image(self):
        """Gets the image of this ChallengeData.

        PNG data (max. 512 kilobyte) to be displayed to the PSU, Base64 encoding, cp. [RFC4648]. This attribute is used only, when PHOTO_OTP or CHIP_OTP is the selected SCA method. 

        :return: The image of this ChallengeData.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ChallengeData.

        PNG data (max. 512 kilobyte) to be displayed to the PSU, Base64 encoding, cp. [RFC4648]. This attribute is used only, when PHOTO_OTP or CHIP_OTP is the selected SCA method. 

        :param image: The image of this ChallengeData.
        :type image: str
        """

        self._image = image

    @property
    def image_link(self):
        """Gets the image_link of this ChallengeData.

        A link where the ASPSP will provides the challenge image for the TPP.

        :return: The image_link of this ChallengeData.
        :rtype: str
        """
        return self._image_link

    @image_link.setter
    def image_link(self, image_link):
        """Sets the image_link of this ChallengeData.

        A link where the ASPSP will provides the challenge image for the TPP.

        :param image_link: The image_link of this ChallengeData.
        :type image_link: str
        """

        self._image_link = image_link

    @property
    def otp_format(self):
        """Gets the otp_format of this ChallengeData.

        The format type of the OTP to be typed in. The admitted values are \"characters\" or \"integer\".

        :return: The otp_format of this ChallengeData.
        :rtype: str
        """
        return self._otp_format

    @otp_format.setter
    def otp_format(self, otp_format):
        """Sets the otp_format of this ChallengeData.

        The format type of the OTP to be typed in. The admitted values are \"characters\" or \"integer\".

        :param otp_format: The otp_format of this ChallengeData.
        :type otp_format: str
        """
        allowed_values = ["characters", "integer"]  # noqa: E501
        if otp_format not in allowed_values:
            raise ValueError(
                "Invalid value for `otp_format` ({0}), must be one of {1}"
                .format(otp_format, allowed_values)
            )

        self._otp_format = otp_format

    @property
    def otp_max_length(self):
        """Gets the otp_max_length of this ChallengeData.

        The maximal length for the OTP to be typed in by the PSU.

        :return: The otp_max_length of this ChallengeData.
        :rtype: int
        """
        return self._otp_max_length

    @otp_max_length.setter
    def otp_max_length(self, otp_max_length):
        """Sets the otp_max_length of this ChallengeData.

        The maximal length for the OTP to be typed in by the PSU.

        :param otp_max_length: The otp_max_length of this ChallengeData.
        :type otp_max_length: int
        """

        self._otp_max_length = otp_max_length
