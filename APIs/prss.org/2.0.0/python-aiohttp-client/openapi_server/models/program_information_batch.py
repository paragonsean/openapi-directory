# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.program_information_batch_program import ProgramInformationBatchProgram
from openapi_server import util


class ProgramInformationBatch(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, created_date: str=None, finished_date: str=None, format: str=None, id: int=None, message: str=None, name: str=None, program: ProgramInformationBatchProgram=None, status: str=None, uri: str=None):
        """ProgramInformationBatch - a model defined in OpenAPI

        :param created_date: The created_date of this ProgramInformationBatch.
        :param finished_date: The finished_date of this ProgramInformationBatch.
        :param format: The format of this ProgramInformationBatch.
        :param id: The id of this ProgramInformationBatch.
        :param message: The message of this ProgramInformationBatch.
        :param name: The name of this ProgramInformationBatch.
        :param program: The program of this ProgramInformationBatch.
        :param status: The status of this ProgramInformationBatch.
        :param uri: The uri of this ProgramInformationBatch.
        """
        self.openapi_types = {
            'created_date': str,
            'finished_date': str,
            'format': str,
            'id': int,
            'message': str,
            'name': str,
            'program': ProgramInformationBatchProgram,
            'status': str,
            'uri': str
        }

        self.attribute_map = {
            'created_date': 'createdDate',
            'finished_date': 'finishedDate',
            'format': 'format',
            'id': 'id',
            'message': 'message',
            'name': 'name',
            'program': 'program',
            'status': 'status',
            'uri': 'uri'
        }

        self._created_date = created_date
        self._finished_date = finished_date
        self._format = format
        self._id = id
        self._message = message
        self._name = name
        self._program = program
        self._status = status
        self._uri = uri

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProgramInformationBatch':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProgramInformationBatch of this ProgramInformationBatch.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created_date(self):
        """Gets the created_date of this ProgramInformationBatch.

        The date and time the batch was created.

        :return: The created_date of this ProgramInformationBatch.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this ProgramInformationBatch.

        The date and time the batch was created.

        :param created_date: The created_date of this ProgramInformationBatch.
        :type created_date: str
        """
        if created_date is None:
            raise ValueError("Invalid value for `created_date`, must not be `None`")

        self._created_date = created_date

    @property
    def finished_date(self):
        """Gets the finished_date of this ProgramInformationBatch.

        The date and time the batch finished (either successful or failed).

        :return: The finished_date of this ProgramInformationBatch.
        :rtype: str
        """
        return self._finished_date

    @finished_date.setter
    def finished_date(self, finished_date):
        """Sets the finished_date of this ProgramInformationBatch.

        The date and time the batch finished (either successful or failed).

        :param finished_date: The finished_date of this ProgramInformationBatch.
        :type finished_date: str
        """

        self._finished_date = finished_date

    @property
    def format(self):
        """Gets the format of this ProgramInformationBatch.

        The format of the metadata file defining the create or update actions to be performed on one or more EPG programs.

        :return: The format of this ProgramInformationBatch.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ProgramInformationBatch.

        The format of the metadata file defining the create or update actions to be performed on one or more EPG programs.

        :param format: The format of this ProgramInformationBatch.
        :type format: str
        """
        allowed_values = ["radiodns"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def id(self):
        """Gets the id of this ProgramInformationBatch.

        The ID of the batch.

        :return: The id of this ProgramInformationBatch.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProgramInformationBatch.

        The ID of the batch.

        :param id: The id of this ProgramInformationBatch.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")
        if id is not None and id < 0:
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")

        self._id = id

    @property
    def message(self):
        """Gets the message of this ProgramInformationBatch.

        The human readable success or failure message.

        :return: The message of this ProgramInformationBatch.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ProgramInformationBatch.

        The human readable success or failure message.

        :param message: The message of this ProgramInformationBatch.
        :type message: str
        """

        self._message = message

    @property
    def name(self):
        """Gets the name of this ProgramInformationBatch.

        The optional name of the batch for human reference.

        :return: The name of this ProgramInformationBatch.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProgramInformationBatch.

        The optional name of the batch for human reference.

        :param name: The name of this ProgramInformationBatch.
        :type name: str
        """

        self._name = name

    @property
    def program(self):
        """Gets the program of this ProgramInformationBatch.


        :return: The program of this ProgramInformationBatch.
        :rtype: ProgramInformationBatchProgram
        """
        return self._program

    @program.setter
    def program(self, program):
        """Sets the program of this ProgramInformationBatch.


        :param program: The program of this ProgramInformationBatch.
        :type program: ProgramInformationBatchProgram
        """

        self._program = program

    @property
    def status(self):
        """Gets the status of this ProgramInformationBatch.

        The current processing status.

        :return: The status of this ProgramInformationBatch.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProgramInformationBatch.

        The current processing status.

        :param status: The status of this ProgramInformationBatch.
        :type status: str
        """
        allowed_values = ["queued", "processing", "failed", "successful"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def uri(self):
        """Gets the uri of this ProgramInformationBatch.

        The URI to the metadata file defining the batch creates/updates.

        :return: The uri of this ProgramInformationBatch.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ProgramInformationBatch.

        The URI to the metadata file defining the batch creates/updates.

        :param uri: The uri of this ProgramInformationBatch.
        :type uri: str
        """

        self._uri = uri
