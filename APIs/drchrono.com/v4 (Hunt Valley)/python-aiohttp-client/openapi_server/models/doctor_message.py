# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.message_note import MessageNote
from openapi_server import util


class DoctorMessage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, archived: bool=None, attachment: str=None, doctor: int=None, id: int=None, message_notes: List[MessageNote]=None, owner: str=None, patient: int=None, read: bool=None, received_at: str=None, responsible_user: str=None, starred: bool=None, title: str=None, type: str=None, updated_at: str=None, workflow_step: str=None):
        """DoctorMessage - a model defined in OpenAPI

        :param archived: The archived of this DoctorMessage.
        :param attachment: The attachment of this DoctorMessage.
        :param doctor: The doctor of this DoctorMessage.
        :param id: The id of this DoctorMessage.
        :param message_notes: The message_notes of this DoctorMessage.
        :param owner: The owner of this DoctorMessage.
        :param patient: The patient of this DoctorMessage.
        :param read: The read of this DoctorMessage.
        :param received_at: The received_at of this DoctorMessage.
        :param responsible_user: The responsible_user of this DoctorMessage.
        :param starred: The starred of this DoctorMessage.
        :param title: The title of this DoctorMessage.
        :param type: The type of this DoctorMessage.
        :param updated_at: The updated_at of this DoctorMessage.
        :param workflow_step: The workflow_step of this DoctorMessage.
        """
        self.openapi_types = {
            'archived': bool,
            'attachment': str,
            'doctor': int,
            'id': int,
            'message_notes': List[MessageNote],
            'owner': str,
            'patient': int,
            'read': bool,
            'received_at': str,
            'responsible_user': str,
            'starred': bool,
            'title': str,
            'type': str,
            'updated_at': str,
            'workflow_step': str
        }

        self.attribute_map = {
            'archived': 'archived',
            'attachment': 'attachment',
            'doctor': 'doctor',
            'id': 'id',
            'message_notes': 'message_notes',
            'owner': 'owner',
            'patient': 'patient',
            'read': 'read',
            'received_at': 'received_at',
            'responsible_user': 'responsible_user',
            'starred': 'starred',
            'title': 'title',
            'type': 'type',
            'updated_at': 'updated_at',
            'workflow_step': 'workflow_step'
        }

        self._archived = archived
        self._attachment = attachment
        self._doctor = doctor
        self._id = id
        self._message_notes = message_notes
        self._owner = owner
        self._patient = patient
        self._read = read
        self._received_at = received_at
        self._responsible_user = responsible_user
        self._starred = starred
        self._title = title
        self._type = type
        self._updated_at = updated_at
        self._workflow_step = workflow_step

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DoctorMessage':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DoctorMessage of this DoctorMessage.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def archived(self):
        """Gets the archived of this DoctorMessage.

        If true, indicates that the message has been soft-deleted

        :return: The archived of this DoctorMessage.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this DoctorMessage.

        If true, indicates that the message has been soft-deleted

        :param archived: The archived of this DoctorMessage.
        :type archived: bool
        """

        self._archived = archived

    @property
    def attachment(self):
        """Gets the attachment of this DoctorMessage.

        Files are passed using `multipart/form-data` encoding, but returned as URLs.

        :return: The attachment of this DoctorMessage.
        :rtype: str
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        """Sets the attachment of this DoctorMessage.

        Files are passed using `multipart/form-data` encoding, but returned as URLs.

        :param attachment: The attachment of this DoctorMessage.
        :type attachment: str
        """

        self._attachment = attachment

    @property
    def doctor(self):
        """Gets the doctor of this DoctorMessage.

        

        :return: The doctor of this DoctorMessage.
        :rtype: int
        """
        return self._doctor

    @doctor.setter
    def doctor(self, doctor):
        """Sets the doctor of this DoctorMessage.

        

        :param doctor: The doctor of this DoctorMessage.
        :type doctor: int
        """
        if doctor is None:
            raise ValueError("Invalid value for `doctor`, must not be `None`")

        self._doctor = doctor

    @property
    def id(self):
        """Gets the id of this DoctorMessage.

        

        :return: The id of this DoctorMessage.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DoctorMessage.

        

        :param id: The id of this DoctorMessage.
        :type id: int
        """

        self._id = id

    @property
    def message_notes(self):
        """Gets the message_notes of this DoctorMessage.

        Array of notes attached to the message

        :return: The message_notes of this DoctorMessage.
        :rtype: List[MessageNote]
        """
        return self._message_notes

    @message_notes.setter
    def message_notes(self, message_notes):
        """Sets the message_notes of this DoctorMessage.

        Array of notes attached to the message

        :param message_notes: The message_notes of this DoctorMessage.
        :type message_notes: List[MessageNote]
        """

        self._message_notes = message_notes

    @property
    def owner(self):
        """Gets the owner of this DoctorMessage.

        ID of `/api/users` who owns the message, who may be the doctor themselves or one of their staff members

        :return: The owner of this DoctorMessage.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DoctorMessage.

        ID of `/api/users` who owns the message, who may be the doctor themselves or one of their staff members

        :param owner: The owner of this DoctorMessage.
        :type owner: str
        """

        self._owner = owner

    @property
    def patient(self):
        """Gets the patient of this DoctorMessage.

        ID of patient that the message concerns, if applicable

        :return: The patient of this DoctorMessage.
        :rtype: int
        """
        return self._patient

    @patient.setter
    def patient(self, patient):
        """Sets the patient of this DoctorMessage.

        ID of patient that the message concerns, if applicable

        :param patient: The patient of this DoctorMessage.
        :type patient: int
        """

        self._patient = patient

    @property
    def read(self):
        """Gets the read of this DoctorMessage.

        

        :return: The read of this DoctorMessage.
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this DoctorMessage.

        

        :param read: The read of this DoctorMessage.
        :type read: bool
        """

        self._read = read

    @property
    def received_at(self):
        """Gets the received_at of this DoctorMessage.

        

        :return: The received_at of this DoctorMessage.
        :rtype: str
        """
        return self._received_at

    @received_at.setter
    def received_at(self, received_at):
        """Sets the received_at of this DoctorMessage.

        

        :param received_at: The received_at of this DoctorMessage.
        :type received_at: str
        """

        self._received_at = received_at

    @property
    def responsible_user(self):
        """Gets the responsible_user of this DoctorMessage.

        ID of `/api/users` who has been assigned to process the message, who may be the doctor themselves or one of their staff members

        :return: The responsible_user of this DoctorMessage.
        :rtype: str
        """
        return self._responsible_user

    @responsible_user.setter
    def responsible_user(self, responsible_user):
        """Sets the responsible_user of this DoctorMessage.

        ID of `/api/users` who has been assigned to process the message, who may be the doctor themselves or one of their staff members

        :param responsible_user: The responsible_user of this DoctorMessage.
        :type responsible_user: str
        """

        self._responsible_user = responsible_user

    @property
    def starred(self):
        """Gets the starred of this DoctorMessage.

        

        :return: The starred of this DoctorMessage.
        :rtype: bool
        """
        return self._starred

    @starred.setter
    def starred(self, starred):
        """Sets the starred of this DoctorMessage.

        

        :param starred: The starred of this DoctorMessage.
        :type starred: bool
        """

        self._starred = starred

    @property
    def title(self):
        """Gets the title of this DoctorMessage.

        

        :return: The title of this DoctorMessage.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DoctorMessage.

        

        :param title: The title of this DoctorMessage.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def type(self):
        """Gets the type of this DoctorMessage.

         Value | Description ----- | ----------- `\"GP\"` | Generated PDF `\"GC\"` | Generated CSV `\"GZ\"` | Generated ZIP `\"IF\"` | Incoming Fax `\"OF\"` | Outgoing Fax `\"IL\"` | Incoming Labs `\"IR\"` | Inbound Referrals `\"OR\"` | Outbound Referrals `\"IE\"` | Incoming eRx `\"OA\"` | Online Appointments `\"PO\"` | Patient Onboarding `\"PI\"` | Patient Incoming Message `\"PM\"` | Patient Outgoing Message `\"OO\"` | Demo Meeting Message `\"OD\"` | Outbound Direct Message `\"ID\"` | Inbound Direct Message 

        :return: The type of this DoctorMessage.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DoctorMessage.

         Value | Description ----- | ----------- `\"GP\"` | Generated PDF `\"GC\"` | Generated CSV `\"GZ\"` | Generated ZIP `\"IF\"` | Incoming Fax `\"OF\"` | Outgoing Fax `\"IL\"` | Incoming Labs `\"IR\"` | Inbound Referrals `\"OR\"` | Outbound Referrals `\"IE\"` | Incoming eRx `\"OA\"` | Online Appointments `\"PO\"` | Patient Onboarding `\"PI\"` | Patient Incoming Message `\"PM\"` | Patient Outgoing Message `\"OO\"` | Demo Meeting Message `\"OD\"` | Outbound Direct Message `\"ID\"` | Inbound Direct Message 

        :param type: The type of this DoctorMessage.
        :type type: str
        """
        allowed_values = ["GP", "GC", "GT", "GZ", "IF", "OF", "IL", "IR", "OR", "IE", "OA", "PO", "PI", "PM", "OO", "OD", "ID", "DL", "CN"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this DoctorMessage.

        

        :return: The updated_at of this DoctorMessage.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DoctorMessage.

        

        :param updated_at: The updated_at of this DoctorMessage.
        :type updated_at: str
        """

        self._updated_at = updated_at

    @property
    def workflow_step(self):
        """Gets the workflow_step of this DoctorMessage.

        Used by doctors and their staff to keep track of what step of processing the message is in

        :return: The workflow_step of this DoctorMessage.
        :rtype: str
        """
        return self._workflow_step

    @workflow_step.setter
    def workflow_step(self, workflow_step):
        """Sets the workflow_step of this DoctorMessage.

        Used by doctors and their staff to keep track of what step of processing the message is in

        :param workflow_step: The workflow_step of this DoctorMessage.
        :type workflow_step: str
        """

        self._workflow_step = workflow_step
