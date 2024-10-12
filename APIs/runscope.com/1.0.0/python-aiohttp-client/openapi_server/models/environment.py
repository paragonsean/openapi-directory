# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.agent import Agent
from openapi_server.models.integration import Integration
from openapi_server import util


class Environment(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, auth: str=None, client_certificate: str=None, emails: object=None, exported_at: int=None, headers: object=None, id: str=None, initial_script_hash: str=None, initial_variables: object=None, integrations: List[Integration]=None, name: str=None, parent_environment_id: str=None, preserve_cookies: bool=None, regions: List[str]=None, remote_agents: List[Agent]=None, retry_on_failure: bool=None, script: str=None, script_library: List[str]=None, stop_on_failure: bool=None, test_id: str=None, verify_ssl: bool=None, version: str=None, webhooks: str=None):
        """Environment - a model defined in OpenAPI

        :param auth: The auth of this Environment.
        :param client_certificate: The client_certificate of this Environment.
        :param emails: The emails of this Environment.
        :param exported_at: The exported_at of this Environment.
        :param headers: The headers of this Environment.
        :param id: The id of this Environment.
        :param initial_script_hash: The initial_script_hash of this Environment.
        :param initial_variables: The initial_variables of this Environment.
        :param integrations: The integrations of this Environment.
        :param name: The name of this Environment.
        :param parent_environment_id: The parent_environment_id of this Environment.
        :param preserve_cookies: The preserve_cookies of this Environment.
        :param regions: The regions of this Environment.
        :param remote_agents: The remote_agents of this Environment.
        :param retry_on_failure: The retry_on_failure of this Environment.
        :param script: The script of this Environment.
        :param script_library: The script_library of this Environment.
        :param stop_on_failure: The stop_on_failure of this Environment.
        :param test_id: The test_id of this Environment.
        :param verify_ssl: The verify_ssl of this Environment.
        :param version: The version of this Environment.
        :param webhooks: The webhooks of this Environment.
        """
        self.openapi_types = {
            'auth': str,
            'client_certificate': str,
            'emails': object,
            'exported_at': int,
            'headers': object,
            'id': str,
            'initial_script_hash': str,
            'initial_variables': object,
            'integrations': List[Integration],
            'name': str,
            'parent_environment_id': str,
            'preserve_cookies': bool,
            'regions': List[str],
            'remote_agents': List[Agent],
            'retry_on_failure': bool,
            'script': str,
            'script_library': List[str],
            'stop_on_failure': bool,
            'test_id': str,
            'verify_ssl': bool,
            'version': str,
            'webhooks': str
        }

        self.attribute_map = {
            'auth': 'auth',
            'client_certificate': 'client_certificate',
            'emails': 'emails',
            'exported_at': 'exported_at',
            'headers': 'headers',
            'id': 'id',
            'initial_script_hash': 'initial_script_hash',
            'initial_variables': 'initial_variables',
            'integrations': 'integrations',
            'name': 'name',
            'parent_environment_id': 'parent_environment_id',
            'preserve_cookies': 'preserve_cookies',
            'regions': 'regions',
            'remote_agents': 'remote_agents',
            'retry_on_failure': 'retry_on_failure',
            'script': 'script',
            'script_library': 'script_library',
            'stop_on_failure': 'stop_on_failure',
            'test_id': 'test_id',
            'verify_ssl': 'verify_ssl',
            'version': 'version',
            'webhooks': 'webhooks'
        }

        self._auth = auth
        self._client_certificate = client_certificate
        self._emails = emails
        self._exported_at = exported_at
        self._headers = headers
        self._id = id
        self._initial_script_hash = initial_script_hash
        self._initial_variables = initial_variables
        self._integrations = integrations
        self._name = name
        self._parent_environment_id = parent_environment_id
        self._preserve_cookies = preserve_cookies
        self._regions = regions
        self._remote_agents = remote_agents
        self._retry_on_failure = retry_on_failure
        self._script = script
        self._script_library = script_library
        self._stop_on_failure = stop_on_failure
        self._test_id = test_id
        self._verify_ssl = verify_ssl
        self._version = version
        self._webhooks = webhooks

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Environment':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Environment of this Environment.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def auth(self):
        """Gets the auth of this Environment.


        :return: The auth of this Environment.
        :rtype: str
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this Environment.


        :param auth: The auth of this Environment.
        :type auth: str
        """

        self._auth = auth

    @property
    def client_certificate(self):
        """Gets the client_certificate of this Environment.


        :return: The client_certificate of this Environment.
        :rtype: str
        """
        return self._client_certificate

    @client_certificate.setter
    def client_certificate(self, client_certificate):
        """Sets the client_certificate of this Environment.


        :param client_certificate: The client_certificate of this Environment.
        :type client_certificate: str
        """

        self._client_certificate = client_certificate

    @property
    def emails(self):
        """Gets the emails of this Environment.


        :return: The emails of this Environment.
        :rtype: object
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this Environment.


        :param emails: The emails of this Environment.
        :type emails: object
        """

        self._emails = emails

    @property
    def exported_at(self):
        """Gets the exported_at of this Environment.


        :return: The exported_at of this Environment.
        :rtype: int
        """
        return self._exported_at

    @exported_at.setter
    def exported_at(self, exported_at):
        """Sets the exported_at of this Environment.


        :param exported_at: The exported_at of this Environment.
        :type exported_at: int
        """

        self._exported_at = exported_at

    @property
    def headers(self):
        """Gets the headers of this Environment.


        :return: The headers of this Environment.
        :rtype: object
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this Environment.


        :param headers: The headers of this Environment.
        :type headers: object
        """

        self._headers = headers

    @property
    def id(self):
        """Gets the id of this Environment.

        The unique identifier for this environment.

        :return: The id of this Environment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Environment.

        The unique identifier for this environment.

        :param id: The id of this Environment.
        :type id: str
        """

        self._id = id

    @property
    def initial_script_hash(self):
        """Gets the initial_script_hash of this Environment.


        :return: The initial_script_hash of this Environment.
        :rtype: str
        """
        return self._initial_script_hash

    @initial_script_hash.setter
    def initial_script_hash(self, initial_script_hash):
        """Sets the initial_script_hash of this Environment.


        :param initial_script_hash: The initial_script_hash of this Environment.
        :type initial_script_hash: str
        """

        self._initial_script_hash = initial_script_hash

    @property
    def initial_variables(self):
        """Gets the initial_variables of this Environment.


        :return: The initial_variables of this Environment.
        :rtype: object
        """
        return self._initial_variables

    @initial_variables.setter
    def initial_variables(self, initial_variables):
        """Sets the initial_variables of this Environment.


        :param initial_variables: The initial_variables of this Environment.
        :type initial_variables: object
        """

        self._initial_variables = initial_variables

    @property
    def integrations(self):
        """Gets the integrations of this Environment.

        The list of integrations for this environment.

        :return: The integrations of this Environment.
        :rtype: List[Integration]
        """
        return self._integrations

    @integrations.setter
    def integrations(self, integrations):
        """Sets the integrations of this Environment.

        The list of integrations for this environment.

        :param integrations: The integrations of this Environment.
        :type integrations: List[Integration]
        """

        self._integrations = integrations

    @property
    def name(self):
        """Gets the name of this Environment.

        Name of this environment.

        :return: The name of this Environment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Environment.

        Name of this environment.

        :param name: The name of this Environment.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def parent_environment_id(self):
        """Gets the parent_environment_id of this Environment.


        :return: The parent_environment_id of this Environment.
        :rtype: str
        """
        return self._parent_environment_id

    @parent_environment_id.setter
    def parent_environment_id(self, parent_environment_id):
        """Sets the parent_environment_id of this Environment.


        :param parent_environment_id: The parent_environment_id of this Environment.
        :type parent_environment_id: str
        """

        self._parent_environment_id = parent_environment_id

    @property
    def preserve_cookies(self):
        """Gets the preserve_cookies of this Environment.


        :return: The preserve_cookies of this Environment.
        :rtype: bool
        """
        return self._preserve_cookies

    @preserve_cookies.setter
    def preserve_cookies(self, preserve_cookies):
        """Sets the preserve_cookies of this Environment.


        :param preserve_cookies: The preserve_cookies of this Environment.
        :type preserve_cookies: bool
        """

        self._preserve_cookies = preserve_cookies

    @property
    def regions(self):
        """Gets the regions of this Environment.

        An array of the region codes that this environment is using.

        :return: The regions of this Environment.
        :rtype: List[str]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this Environment.

        An array of the region codes that this environment is using.

        :param regions: The regions of this Environment.
        :type regions: List[str]
        """

        self._regions = regions

    @property
    def remote_agents(self):
        """Gets the remote_agents of this Environment.


        :return: The remote_agents of this Environment.
        :rtype: List[Agent]
        """
        return self._remote_agents

    @remote_agents.setter
    def remote_agents(self, remote_agents):
        """Sets the remote_agents of this Environment.


        :param remote_agents: The remote_agents of this Environment.
        :type remote_agents: List[Agent]
        """

        self._remote_agents = remote_agents

    @property
    def retry_on_failure(self):
        """Gets the retry_on_failure of this Environment.


        :return: The retry_on_failure of this Environment.
        :rtype: bool
        """
        return self._retry_on_failure

    @retry_on_failure.setter
    def retry_on_failure(self, retry_on_failure):
        """Sets the retry_on_failure of this Environment.


        :param retry_on_failure: The retry_on_failure of this Environment.
        :type retry_on_failure: bool
        """

        self._retry_on_failure = retry_on_failure

    @property
    def script(self):
        """Gets the script of this Environment.

        

        :return: The script of this Environment.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this Environment.

        

        :param script: The script of this Environment.
        :type script: str
        """

        self._script = script

    @property
    def script_library(self):
        """Gets the script_library of this Environment.

        The list of ids for scripts, part of the script libraries, being used for this environment.

        :return: The script_library of this Environment.
        :rtype: List[str]
        """
        return self._script_library

    @script_library.setter
    def script_library(self, script_library):
        """Sets the script_library of this Environment.

        The list of ids for scripts, part of the script libraries, being used for this environment.

        :param script_library: The script_library of this Environment.
        :type script_library: List[str]
        """

        self._script_library = script_library

    @property
    def stop_on_failure(self):
        """Gets the stop_on_failure of this Environment.

        Stop executing the test after the first failed step.

        :return: The stop_on_failure of this Environment.
        :rtype: bool
        """
        return self._stop_on_failure

    @stop_on_failure.setter
    def stop_on_failure(self, stop_on_failure):
        """Sets the stop_on_failure of this Environment.

        Stop executing the test after the first failed step.

        :param stop_on_failure: The stop_on_failure of this Environment.
        :type stop_on_failure: bool
        """

        self._stop_on_failure = stop_on_failure

    @property
    def test_id(self):
        """Gets the test_id of this Environment.

        The unique identifier for this test.

        :return: The test_id of this Environment.
        :rtype: str
        """
        return self._test_id

    @test_id.setter
    def test_id(self, test_id):
        """Sets the test_id of this Environment.

        The unique identifier for this test.

        :param test_id: The test_id of this Environment.
        :type test_id: str
        """

        self._test_id = test_id

    @property
    def verify_ssl(self):
        """Gets the verify_ssl of this Environment.

        Validate all SSL certificates on any HTTPS connections.

        :return: The verify_ssl of this Environment.
        :rtype: bool
        """
        return self._verify_ssl

    @verify_ssl.setter
    def verify_ssl(self, verify_ssl):
        """Sets the verify_ssl of this Environment.

        Validate all SSL certificates on any HTTPS connections.

        :param verify_ssl: The verify_ssl of this Environment.
        :type verify_ssl: bool
        """

        self._verify_ssl = verify_ssl

    @property
    def version(self):
        """Gets the version of this Environment.


        :return: The version of this Environment.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Environment.


        :param version: The version of this Environment.
        :type version: str
        """

        self._version = version

    @property
    def webhooks(self):
        """Gets the webhooks of this Environment.


        :return: The webhooks of this Environment.
        :rtype: str
        """
        return self._webhooks

    @webhooks.setter
    def webhooks(self, webhooks):
        """Sets the webhooks of this Environment.


        :param webhooks: The webhooks of this Environment.
        :type webhooks: str
        """

        self._webhooks = webhooks
