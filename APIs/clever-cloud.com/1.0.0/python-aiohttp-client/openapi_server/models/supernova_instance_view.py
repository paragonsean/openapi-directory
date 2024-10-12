# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.supernova_instance_view_flavor import SupernovaInstanceViewFlavor
from openapi_server import util


class SupernovaInstanceView(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, app_id: str=None, app_port: float=None, commit_id: str=None, created_at: float=None, deploy_id: str=None, deploy_number: float=None, display_name: str=None, flavor: SupernovaInstanceViewFlavor=None, hv: str=None, image: str=None, instance_number: float=None, internal_ip: str=None, ip: str=None, owner_id: str=None, source: str=None, ssh_port: float=None, state: str=None, uuid: str=None, zabbix_port: float=None, zone: str=None):
        """SupernovaInstanceView - a model defined in OpenAPI

        :param app_id: The app_id of this SupernovaInstanceView.
        :param app_port: The app_port of this SupernovaInstanceView.
        :param commit_id: The commit_id of this SupernovaInstanceView.
        :param created_at: The created_at of this SupernovaInstanceView.
        :param deploy_id: The deploy_id of this SupernovaInstanceView.
        :param deploy_number: The deploy_number of this SupernovaInstanceView.
        :param display_name: The display_name of this SupernovaInstanceView.
        :param flavor: The flavor of this SupernovaInstanceView.
        :param hv: The hv of this SupernovaInstanceView.
        :param image: The image of this SupernovaInstanceView.
        :param instance_number: The instance_number of this SupernovaInstanceView.
        :param internal_ip: The internal_ip of this SupernovaInstanceView.
        :param ip: The ip of this SupernovaInstanceView.
        :param owner_id: The owner_id of this SupernovaInstanceView.
        :param source: The source of this SupernovaInstanceView.
        :param ssh_port: The ssh_port of this SupernovaInstanceView.
        :param state: The state of this SupernovaInstanceView.
        :param uuid: The uuid of this SupernovaInstanceView.
        :param zabbix_port: The zabbix_port of this SupernovaInstanceView.
        :param zone: The zone of this SupernovaInstanceView.
        """
        self.openapi_types = {
            'app_id': str,
            'app_port': float,
            'commit_id': str,
            'created_at': float,
            'deploy_id': str,
            'deploy_number': float,
            'display_name': str,
            'flavor': SupernovaInstanceViewFlavor,
            'hv': str,
            'image': str,
            'instance_number': float,
            'internal_ip': str,
            'ip': str,
            'owner_id': str,
            'source': str,
            'ssh_port': float,
            'state': str,
            'uuid': str,
            'zabbix_port': float,
            'zone': str
        }

        self.attribute_map = {
            'app_id': 'appId',
            'app_port': 'appPort',
            'commit_id': 'commitId',
            'created_at': 'createdAt',
            'deploy_id': 'deployId',
            'deploy_number': 'deployNumber',
            'display_name': 'displayName',
            'flavor': 'flavor',
            'hv': 'hv',
            'image': 'image',
            'instance_number': 'instanceNumber',
            'internal_ip': 'internalIP',
            'ip': 'ip',
            'owner_id': 'ownerId',
            'source': 'source',
            'ssh_port': 'sshPort',
            'state': 'state',
            'uuid': 'uuid',
            'zabbix_port': 'zabbixPort',
            'zone': 'zone'
        }

        self._app_id = app_id
        self._app_port = app_port
        self._commit_id = commit_id
        self._created_at = created_at
        self._deploy_id = deploy_id
        self._deploy_number = deploy_number
        self._display_name = display_name
        self._flavor = flavor
        self._hv = hv
        self._image = image
        self._instance_number = instance_number
        self._internal_ip = internal_ip
        self._ip = ip
        self._owner_id = owner_id
        self._source = source
        self._ssh_port = ssh_port
        self._state = state
        self._uuid = uuid
        self._zabbix_port = zabbix_port
        self._zone = zone

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SupernovaInstanceView':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SupernovaInstanceView of this SupernovaInstanceView.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_id(self):
        """Gets the app_id of this SupernovaInstanceView.

        Identifier of running app/add-on

        :return: The app_id of this SupernovaInstanceView.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this SupernovaInstanceView.

        Identifier of running app/add-on

        :param app_id: The app_id of this SupernovaInstanceView.
        :type app_id: str
        """

        self._app_id = app_id

    @property
    def app_port(self):
        """Gets the app_port of this SupernovaInstanceView.

        Port of the HV that's redirected to 8080 on VM

        :return: The app_port of this SupernovaInstanceView.
        :rtype: float
        """
        return self._app_port

    @app_port.setter
    def app_port(self, app_port):
        """Sets the app_port of this SupernovaInstanceView.

        Port of the HV that's redirected to 8080 on VM

        :param app_port: The app_port of this SupernovaInstanceView.
        :type app_port: float
        """
        if app_port is None:
            raise ValueError("Invalid value for `app_port`, must not be `None`")

        self._app_port = app_port

    @property
    def commit_id(self):
        """Gets the commit_id of this SupernovaInstanceView.


        :return: The commit_id of this SupernovaInstanceView.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this SupernovaInstanceView.


        :param commit_id: The commit_id of this SupernovaInstanceView.
        :type commit_id: str
        """

        self._commit_id = commit_id

    @property
    def created_at(self):
        """Gets the created_at of this SupernovaInstanceView.

        Integer unix timestamp

        :return: The created_at of this SupernovaInstanceView.
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SupernovaInstanceView.

        Integer unix timestamp

        :param created_at: The created_at of this SupernovaInstanceView.
        :type created_at: float
        """

        self._created_at = created_at

    @property
    def deploy_id(self):
        """Gets the deploy_id of this SupernovaInstanceView.


        :return: The deploy_id of this SupernovaInstanceView.
        :rtype: str
        """
        return self._deploy_id

    @deploy_id.setter
    def deploy_id(self, deploy_id):
        """Sets the deploy_id of this SupernovaInstanceView.


        :param deploy_id: The deploy_id of this SupernovaInstanceView.
        :type deploy_id: str
        """

        self._deploy_id = deploy_id

    @property
    def deploy_number(self):
        """Gets the deploy_number of this SupernovaInstanceView.


        :return: The deploy_number of this SupernovaInstanceView.
        :rtype: float
        """
        return self._deploy_number

    @deploy_number.setter
    def deploy_number(self, deploy_number):
        """Sets the deploy_number of this SupernovaInstanceView.


        :param deploy_number: The deploy_number of this SupernovaInstanceView.
        :type deploy_number: float
        """

        self._deploy_number = deploy_number

    @property
    def display_name(self):
        """Gets the display_name of this SupernovaInstanceView.

        Generated PokéName. This name is generated from the uuid.

        :return: The display_name of this SupernovaInstanceView.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this SupernovaInstanceView.

        Generated PokéName. This name is generated from the uuid.

        :param display_name: The display_name of this SupernovaInstanceView.
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def flavor(self):
        """Gets the flavor of this SupernovaInstanceView.


        :return: The flavor of this SupernovaInstanceView.
        :rtype: SupernovaInstanceViewFlavor
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this SupernovaInstanceView.


        :param flavor: The flavor of this SupernovaInstanceView.
        :type flavor: SupernovaInstanceViewFlavor
        """
        if flavor is None:
            raise ValueError("Invalid value for `flavor`, must not be `None`")

        self._flavor = flavor

    @property
    def hv(self):
        """Gets the hv of this SupernovaInstanceView.

        String name of hv.

        :return: The hv of this SupernovaInstanceView.
        :rtype: str
        """
        return self._hv

    @hv.setter
    def hv(self, hv):
        """Sets the hv of this SupernovaInstanceView.

        String name of hv.

        :param hv: The hv of this SupernovaInstanceView.
        :type hv: str
        """
        if hv is None:
            raise ValueError("Invalid value for `hv`, must not be `None`")

        self._hv = hv

    @property
    def image(self):
        """Gets the image of this SupernovaInstanceView.

        Base system image. E.g. java-20181030, node-20180912…

        :return: The image of this SupernovaInstanceView.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this SupernovaInstanceView.

        Base system image. E.g. java-20181030, node-20180912…

        :param image: The image of this SupernovaInstanceView.
        :type image: str
        """
        if image is None:
            raise ValueError("Invalid value for `image`, must not be `None`")

        self._image = image

    @property
    def instance_number(self):
        """Gets the instance_number of this SupernovaInstanceView.


        :return: The instance_number of this SupernovaInstanceView.
        :rtype: float
        """
        return self._instance_number

    @instance_number.setter
    def instance_number(self, instance_number):
        """Sets the instance_number of this SupernovaInstanceView.


        :param instance_number: The instance_number of this SupernovaInstanceView.
        :type instance_number: float
        """

        self._instance_number = instance_number

    @property
    def internal_ip(self):
        """Gets the internal_ip of this SupernovaInstanceView.


        :return: The internal_ip of this SupernovaInstanceView.
        :rtype: str
        """
        return self._internal_ip

    @internal_ip.setter
    def internal_ip(self, internal_ip):
        """Sets the internal_ip of this SupernovaInstanceView.


        :param internal_ip: The internal_ip of this SupernovaInstanceView.
        :type internal_ip: str
        """

        self._internal_ip = internal_ip

    @property
    def ip(self):
        """Gets the ip of this SupernovaInstanceView.

        Public IP of the HV

        :return: The ip of this SupernovaInstanceView.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this SupernovaInstanceView.

        Public IP of the HV

        :param ip: The ip of this SupernovaInstanceView.
        :type ip: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")

        self._ip = ip

    @property
    def owner_id(self):
        """Gets the owner_id of this SupernovaInstanceView.

        Identifier of the owner of the app/add-on running

        :return: The owner_id of this SupernovaInstanceView.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this SupernovaInstanceView.

        Identifier of the owner of the app/add-on running

        :param owner_id: The owner_id of this SupernovaInstanceView.
        :type owner_id: str
        """

        self._owner_id = owner_id

    @property
    def source(self):
        """Gets the source of this SupernovaInstanceView.

        Who/what started this instance? E.g. \"app\", \"cli\"

        :return: The source of this SupernovaInstanceView.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this SupernovaInstanceView.

        Who/what started this instance? E.g. \"app\", \"cli\"

        :param source: The source of this SupernovaInstanceView.
        :type source: str
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")

        self._source = source

    @property
    def ssh_port(self):
        """Gets the ssh_port of this SupernovaInstanceView.

        Port of the HV that's redirected to 22 on VM

        :return: The ssh_port of this SupernovaInstanceView.
        :rtype: float
        """
        return self._ssh_port

    @ssh_port.setter
    def ssh_port(self, ssh_port):
        """Sets the ssh_port of this SupernovaInstanceView.

        Port of the HV that's redirected to 22 on VM

        :param ssh_port: The ssh_port of this SupernovaInstanceView.
        :type ssh_port: float
        """

        self._ssh_port = ssh_port

    @property
    def state(self):
        """Gets the state of this SupernovaInstanceView.


        :return: The state of this SupernovaInstanceView.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SupernovaInstanceView.


        :param state: The state of this SupernovaInstanceView.
        :type state: str
        """

        self._state = state

    @property
    def uuid(self):
        """Gets the uuid of this SupernovaInstanceView.


        :return: The uuid of this SupernovaInstanceView.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this SupernovaInstanceView.


        :param uuid: The uuid of this SupernovaInstanceView.
        :type uuid: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")

        self._uuid = uuid

    @property
    def zabbix_port(self):
        """Gets the zabbix_port of this SupernovaInstanceView.

        Port of the HV that's redirected to 10050 on VM

        :return: The zabbix_port of this SupernovaInstanceView.
        :rtype: float
        """
        return self._zabbix_port

    @zabbix_port.setter
    def zabbix_port(self, zabbix_port):
        """Sets the zabbix_port of this SupernovaInstanceView.

        Port of the HV that's redirected to 10050 on VM

        :param zabbix_port: The zabbix_port of this SupernovaInstanceView.
        :type zabbix_port: float
        """
        if zabbix_port is None:
            raise ValueError("Invalid value for `zabbix_port`, must not be `None`")

        self._zabbix_port = zabbix_port

    @property
    def zone(self):
        """Gets the zone of this SupernovaInstanceView.


        :return: The zone of this SupernovaInstanceView.
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this SupernovaInstanceView.


        :param zone: The zone of this SupernovaInstanceView.
        :type zone: str
        """

        self._zone = zone
