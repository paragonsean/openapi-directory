# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.call_broadcast_sounds import CallBroadcastSounds
from openapi_server.models.local_time_restriction import LocalTimeRestriction
from openapi_server.models.recipient import Recipient
from openapi_server.models.retry_config import RetryConfig
from openapi_server.models.schedule import Schedule
from openapi_server import util


class CallBroadcast(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, answering_machine_config: str=None, dialplan_xml: str=None, from_number: str=None, id: int=None, labels: list[str]=None, last_modified: int=None, local_time_restriction: LocalTimeRestriction=None, max_active: int=None, max_active_transfers: int=None, name: str=None, recipients: List[Recipient]=None, resume_next_day: bool=None, retry_config: RetryConfig=None, schedules: List[Schedule]=None, sounds: CallBroadcastSounds=None, status: str=None):
        """CallBroadcast - a model defined in OpenAPI

        :param answering_machine_config: The answering_machine_config of this CallBroadcast.
        :param dialplan_xml: The dialplan_xml of this CallBroadcast.
        :param from_number: The from_number of this CallBroadcast.
        :param id: The id of this CallBroadcast.
        :param labels: The labels of this CallBroadcast.
        :param last_modified: The last_modified of this CallBroadcast.
        :param local_time_restriction: The local_time_restriction of this CallBroadcast.
        :param max_active: The max_active of this CallBroadcast.
        :param max_active_transfers: The max_active_transfers of this CallBroadcast.
        :param name: The name of this CallBroadcast.
        :param recipients: The recipients of this CallBroadcast.
        :param resume_next_day: The resume_next_day of this CallBroadcast.
        :param retry_config: The retry_config of this CallBroadcast.
        :param schedules: The schedules of this CallBroadcast.
        :param sounds: The sounds of this CallBroadcast.
        :param status: The status of this CallBroadcast.
        """
        self.openapi_types = {
            'answering_machine_config': str,
            'dialplan_xml': str,
            'from_number': str,
            'id': int,
            'labels': list[str],
            'last_modified': int,
            'local_time_restriction': LocalTimeRestriction,
            'max_active': int,
            'max_active_transfers': int,
            'name': str,
            'recipients': List[Recipient],
            'resume_next_day': bool,
            'retry_config': RetryConfig,
            'schedules': List[Schedule],
            'sounds': CallBroadcastSounds,
            'status': str
        }

        self.attribute_map = {
            'answering_machine_config': 'answeringMachineConfig',
            'dialplan_xml': 'dialplanXml',
            'from_number': 'fromNumber',
            'id': 'id',
            'labels': 'labels',
            'last_modified': 'lastModified',
            'local_time_restriction': 'localTimeRestriction',
            'max_active': 'maxActive',
            'max_active_transfers': 'maxActiveTransfers',
            'name': 'name',
            'recipients': 'recipients',
            'resume_next_day': 'resumeNextDay',
            'retry_config': 'retryConfig',
            'schedules': 'schedules',
            'sounds': 'sounds',
            'status': 'status'
        }

        self._answering_machine_config = answering_machine_config
        self._dialplan_xml = dialplan_xml
        self._from_number = from_number
        self._id = id
        self._labels = labels
        self._last_modified = last_modified
        self._local_time_restriction = local_time_restriction
        self._max_active = max_active
        self._max_active_transfers = max_active_transfers
        self._name = name
        self._recipients = recipients
        self._resume_next_day = resume_next_day
        self._retry_config = retry_config
        self._schedules = schedules
        self._sounds = sounds
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CallBroadcast':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CallBroadcast of this CallBroadcast.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def answering_machine_config(self):
        """Gets the answering_machine_config of this CallBroadcast.

        Specifies which action should be taken if answering machine was detected, default value: AM_AND_LIVE. Available values: AM_ONLY - run AMD (Answering Machine Detection), hang up if LA (Live Answer); AM_AND_LIVE - run AMD, play separate live vs. machine sound; LIVE_WITH_AMD, run AMD, hang up if machine answers; LIVE_IMMEDIATE - no AMD, play live sound immediately

        :return: The answering_machine_config of this CallBroadcast.
        :rtype: str
        """
        return self._answering_machine_config

    @answering_machine_config.setter
    def answering_machine_config(self, answering_machine_config):
        """Sets the answering_machine_config of this CallBroadcast.

        Specifies which action should be taken if answering machine was detected, default value: AM_AND_LIVE. Available values: AM_ONLY - run AMD (Answering Machine Detection), hang up if LA (Live Answer); AM_AND_LIVE - run AMD, play separate live vs. machine sound; LIVE_WITH_AMD, run AMD, hang up if machine answers; LIVE_IMMEDIATE - no AMD, play live sound immediately

        :param answering_machine_config: The answering_machine_config of this CallBroadcast.
        :type answering_machine_config: str
        """
        allowed_values = ["AM_ONLY", "AM_AND_LIVE", "LIVE_WITH_AMD", "LIVE_IMMEDIATE"]  # noqa: E501
        if answering_machine_config not in allowed_values:
            raise ValueError(
                "Invalid value for `answering_machine_config` ({0}), must be one of {1}"
                .format(answering_machine_config, allowed_values)
            )

        self._answering_machine_config = answering_machine_config

    @property
    def dialplan_xml(self):
        """Gets the dialplan_xml of this CallBroadcast.

        IVR xml is a document which describes the dialplan to setup the IVR broadcast

        :return: The dialplan_xml of this CallBroadcast.
        :rtype: str
        """
        return self._dialplan_xml

    @dialplan_xml.setter
    def dialplan_xml(self, dialplan_xml):
        """Sets the dialplan_xml of this CallBroadcast.

        IVR xml is a document which describes the dialplan to setup the IVR broadcast

        :param dialplan_xml: The dialplan_xml of this CallBroadcast.
        :type dialplan_xml: str
        """

        self._dialplan_xml = dialplan_xml

    @property
    def from_number(self):
        """Gets the from_number of this CallBroadcast.

        Phone number in E.164 format (11-digit) or short code for text. Example: 12132000384, 67076

        :return: The from_number of this CallBroadcast.
        :rtype: str
        """
        return self._from_number

    @from_number.setter
    def from_number(self, from_number):
        """Sets the from_number of this CallBroadcast.

        Phone number in E.164 format (11-digit) or short code for text. Example: 12132000384, 67076

        :param from_number: The from_number of this CallBroadcast.
        :type from_number: str
        """

        self._from_number = from_number

    @property
    def id(self):
        """Gets the id of this CallBroadcast.

        A unique id of broadcast (readonly)

        :return: The id of this CallBroadcast.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CallBroadcast.

        A unique id of broadcast (readonly)

        :param id: The id of this CallBroadcast.
        :type id: int
        """

        self._id = id

    @property
    def labels(self):
        """Gets the labels of this CallBroadcast.

        Labels of a broadcast

        :return: The labels of this CallBroadcast.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this CallBroadcast.

        Labels of a broadcast

        :param labels: The labels of this CallBroadcast.
        :type labels: list[str]
        """

        self._labels = labels

    @property
    def last_modified(self):
        """Gets the last_modified of this CallBroadcast.

        The time when a given resource was updated, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT 

        :return: The last_modified of this CallBroadcast.
        :rtype: int
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this CallBroadcast.

        The time when a given resource was updated, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT 

        :param last_modified: The last_modified of this CallBroadcast.
        :type last_modified: int
        """

        self._last_modified = last_modified

    @property
    def local_time_restriction(self):
        """Gets the local_time_restriction of this CallBroadcast.


        :return: The local_time_restriction of this CallBroadcast.
        :rtype: LocalTimeRestriction
        """
        return self._local_time_restriction

    @local_time_restriction.setter
    def local_time_restriction(self, local_time_restriction):
        """Sets the local_time_restriction of this CallBroadcast.


        :param local_time_restriction: The local_time_restriction of this CallBroadcast.
        :type local_time_restriction: LocalTimeRestriction
        """

        self._local_time_restriction = local_time_restriction

    @property
    def max_active(self):
        """Gets the max_active of this CallBroadcast.

        Sets a maximum number of calls to be dialed by CallFire at once

        :return: The max_active of this CallBroadcast.
        :rtype: int
        """
        return self._max_active

    @max_active.setter
    def max_active(self, max_active):
        """Sets the max_active of this CallBroadcast.

        Sets a maximum number of calls to be dialed by CallFire at once

        :param max_active: The max_active of this CallBroadcast.
        :type max_active: int
        """

        self._max_active = max_active

    @property
    def max_active_transfers(self):
        """Gets the max_active_transfers of this CallBroadcast.

        A maximum number of active transfers

        :return: The max_active_transfers of this CallBroadcast.
        :rtype: int
        """
        return self._max_active_transfers

    @max_active_transfers.setter
    def max_active_transfers(self, max_active_transfers):
        """Sets the max_active_transfers of this CallBroadcast.

        A maximum number of active transfers

        :param max_active_transfers: The max_active_transfers of this CallBroadcast.
        :type max_active_transfers: int
        """

        self._max_active_transfers = max_active_transfers

    @property
    def name(self):
        """Gets the name of this CallBroadcast.

        A name of a broadcast

        :return: The name of this CallBroadcast.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CallBroadcast.

        A name of a broadcast

        :param name: The name of this CallBroadcast.
        :type name: str
        """

        self._name = name

    @property
    def recipients(self):
        """Gets the recipients of this CallBroadcast.

        Recipients of a call broadcast, can be either existing contacts or a new ones

        :return: The recipients of this CallBroadcast.
        :rtype: List[Recipient]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this CallBroadcast.

        Recipients of a call broadcast, can be either existing contacts or a new ones

        :param recipients: The recipients of this CallBroadcast.
        :type recipients: List[Recipient]
        """

        self._recipients = recipients

    @property
    def resume_next_day(self):
        """Gets the resume_next_day of this CallBroadcast.

        If true resumes the unfinished campaign to the next day

        :return: The resume_next_day of this CallBroadcast.
        :rtype: bool
        """
        return self._resume_next_day

    @resume_next_day.setter
    def resume_next_day(self, resume_next_day):
        """Sets the resume_next_day of this CallBroadcast.

        If true resumes the unfinished campaign to the next day

        :param resume_next_day: The resume_next_day of this CallBroadcast.
        :type resume_next_day: bool
        """

        self._resume_next_day = resume_next_day

    @property
    def retry_config(self):
        """Gets the retry_config of this CallBroadcast.


        :return: The retry_config of this CallBroadcast.
        :rtype: RetryConfig
        """
        return self._retry_config

    @retry_config.setter
    def retry_config(self, retry_config):
        """Sets the retry_config of this CallBroadcast.


        :param retry_config: The retry_config of this CallBroadcast.
        :type retry_config: RetryConfig
        """

        self._retry_config = retry_config

    @property
    def schedules(self):
        """Gets the schedules of this CallBroadcast.

        A list of schedule objects which specifies a range of time when broadcast should be started and stopped. Supports the scheduling per day of week

        :return: The schedules of this CallBroadcast.
        :rtype: List[Schedule]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """Sets the schedules of this CallBroadcast.

        A list of schedule objects which specifies a range of time when broadcast should be started and stopped. Supports the scheduling per day of week

        :param schedules: The schedules of this CallBroadcast.
        :type schedules: List[Schedule]
        """

        self._schedules = schedules

    @property
    def sounds(self):
        """Gets the sounds of this CallBroadcast.


        :return: The sounds of this CallBroadcast.
        :rtype: CallBroadcastSounds
        """
        return self._sounds

    @sounds.setter
    def sounds(self, sounds):
        """Sets the sounds of this CallBroadcast.


        :param sounds: The sounds of this CallBroadcast.
        :type sounds: CallBroadcastSounds
        """

        self._sounds = sounds

    @property
    def status(self):
        """Gets the status of this CallBroadcast.

        A status of a broadcast (read only). SETUP - campaign isn't configured yet; START_PENDING - waiting for contact batch population; RUNNING - campaign is running; STOPPED - campaign is stopped; FINISHED - campaign is finished; ARCHIVED - campaign was archived

        :return: The status of this CallBroadcast.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CallBroadcast.

        A status of a broadcast (read only). SETUP - campaign isn't configured yet; START_PENDING - waiting for contact batch population; RUNNING - campaign is running; STOPPED - campaign is stopped; FINISHED - campaign is finished; ARCHIVED - campaign was archived

        :param status: The status of this CallBroadcast.
        :type status: str
        """
        allowed_values = ["TEST", "SETUP", "START_PENDING", "RUNNING", "SCHEDULED", "STOPPED", "SUSPENDED", "FINISHED", "ARCHIVED", "VALIDATING_START", "VALIDATING_EMAIL", "BLOCKED_SUSPICIOUS", "DECLINED", "APPROVED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
