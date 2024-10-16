# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SoapNoteLineItemFieldType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, allowed_values: List[str]=None, archived: bool=None, clinical_note_template: str=None, comment: str=None, data_type: str=None, id: int=None, name: str=None, required: bool=None):
        """SoapNoteLineItemFieldType - a model defined in OpenAPI

        :param allowed_values: The allowed_values of this SoapNoteLineItemFieldType.
        :param archived: The archived of this SoapNoteLineItemFieldType.
        :param clinical_note_template: The clinical_note_template of this SoapNoteLineItemFieldType.
        :param comment: The comment of this SoapNoteLineItemFieldType.
        :param data_type: The data_type of this SoapNoteLineItemFieldType.
        :param id: The id of this SoapNoteLineItemFieldType.
        :param name: The name of this SoapNoteLineItemFieldType.
        :param required: The required of this SoapNoteLineItemFieldType.
        """
        self.openapi_types = {
            'allowed_values': List[str],
            'archived': bool,
            'clinical_note_template': str,
            'comment': str,
            'data_type': str,
            'id': int,
            'name': str,
            'required': bool
        }

        self.attribute_map = {
            'allowed_values': 'allowed_values',
            'archived': 'archived',
            'clinical_note_template': 'clinical_note_template',
            'comment': 'comment',
            'data_type': 'data_type',
            'id': 'id',
            'name': 'name',
            'required': 'required'
        }

        self._allowed_values = allowed_values
        self._archived = archived
        self._clinical_note_template = clinical_note_template
        self._comment = comment
        self._data_type = data_type
        self._id = id
        self._name = name
        self._required = required

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SoapNoteLineItemFieldType':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SoapNoteLineItemFieldType of this SoapNoteLineItemFieldType.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def allowed_values(self):
        """Gets the allowed_values of this SoapNoteLineItemFieldType.

        Value options the field type relies on if applicable, otherwise it will be an empty array

        :return: The allowed_values of this SoapNoteLineItemFieldType.
        :rtype: List[str]
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """Sets the allowed_values of this SoapNoteLineItemFieldType.

        Value options the field type relies on if applicable, otherwise it will be an empty array

        :param allowed_values: The allowed_values of this SoapNoteLineItemFieldType.
        :type allowed_values: List[str]
        """

        self._allowed_values = allowed_values

    @property
    def archived(self):
        """Gets the archived of this SoapNoteLineItemFieldType.

        Indicates that the field has been soft-deleted by the doctor and will not be used in future notes

        :return: The archived of this SoapNoteLineItemFieldType.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this SoapNoteLineItemFieldType.

        Indicates that the field has been soft-deleted by the doctor and will not be used in future notes

        :param archived: The archived of this SoapNoteLineItemFieldType.
        :type archived: bool
        """

        self._archived = archived

    @property
    def clinical_note_template(self):
        """Gets the clinical_note_template of this SoapNoteLineItemFieldType.

        ID of the `/api/clinical_note_templates` object that the field belongs to

        :return: The clinical_note_template of this SoapNoteLineItemFieldType.
        :rtype: str
        """
        return self._clinical_note_template

    @clinical_note_template.setter
    def clinical_note_template(self, clinical_note_template):
        """Sets the clinical_note_template of this SoapNoteLineItemFieldType.

        ID of the `/api/clinical_note_templates` object that the field belongs to

        :param clinical_note_template: The clinical_note_template of this SoapNoteLineItemFieldType.
        :type clinical_note_template: str
        """

        self._clinical_note_template = clinical_note_template

    @property
    def comment(self):
        """Gets the comment of this SoapNoteLineItemFieldType.

        Comment

        :return: The comment of this SoapNoteLineItemFieldType.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this SoapNoteLineItemFieldType.

        Comment

        :param comment: The comment of this SoapNoteLineItemFieldType.
        :type comment: str
        """

        self._comment = comment

    @property
    def data_type(self):
        """Gets the data_type of this SoapNoteLineItemFieldType.

        One of `\"\"`, `\"Checkbox\"`, `\"NullCheckbox\"`, `\"String\"`, `\"TwoStrings\"`, `\"FreeDraw\"`, `\"Photo\"`, `\"Header\"`, `\"Subheader\"`

        :return: The data_type of this SoapNoteLineItemFieldType.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this SoapNoteLineItemFieldType.

        One of `\"\"`, `\"Checkbox\"`, `\"NullCheckbox\"`, `\"String\"`, `\"TwoStrings\"`, `\"FreeDraw\"`, `\"Photo\"`, `\"Header\"`, `\"Subheader\"`

        :param data_type: The data_type of this SoapNoteLineItemFieldType.
        :type data_type: str
        """

        self._data_type = data_type

    @property
    def id(self):
        """Gets the id of this SoapNoteLineItemFieldType.

        

        :return: The id of this SoapNoteLineItemFieldType.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SoapNoteLineItemFieldType.

        

        :param id: The id of this SoapNoteLineItemFieldType.
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SoapNoteLineItemFieldType.

        

        :return: The name of this SoapNoteLineItemFieldType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SoapNoteLineItemFieldType.

        

        :param name: The name of this SoapNoteLineItemFieldType.
        :type name: str
        """

        self._name = name

    @property
    def required(self):
        """Gets the required of this SoapNoteLineItemFieldType.

        Indicates that a note should not be locked unless a value is provided for this field

        :return: The required of this SoapNoteLineItemFieldType.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this SoapNoteLineItemFieldType.

        Indicates that a note should not be locked unless a value is provided for this field

        :param required: The required of this SoapNoteLineItemFieldType.
        :type required: bool
        """

        self._required = required
