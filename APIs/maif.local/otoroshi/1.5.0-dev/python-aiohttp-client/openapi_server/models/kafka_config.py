# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class KafkaConfig(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, key_pass: str=None, key_store: str=None, servers: List[str]=None, topic: str=None, trustore: str=None):
        """KafkaConfig - a model defined in OpenAPI

        :param key_pass: The key_pass of this KafkaConfig.
        :param key_store: The key_store of this KafkaConfig.
        :param servers: The servers of this KafkaConfig.
        :param topic: The topic of this KafkaConfig.
        :param trustore: The trustore of this KafkaConfig.
        """
        self.openapi_types = {
            'key_pass': str,
            'key_store': str,
            'servers': List[str],
            'topic': str,
            'trustore': str
        }

        self.attribute_map = {
            'key_pass': 'keyPass',
            'key_store': 'keyStore',
            'servers': 'servers',
            'topic': 'topic',
            'trustore': 'trustore'
        }

        self._key_pass = key_pass
        self._key_store = key_store
        self._servers = servers
        self._topic = topic
        self._trustore = trustore

    @classmethod
    def from_dict(cls, dikt: dict) -> 'KafkaConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The KafkaConfig of this KafkaConfig.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def key_pass(self):
        """Gets the key_pass of this KafkaConfig.

        Optional keypass

        :return: The key_pass of this KafkaConfig.
        :rtype: str
        """
        return self._key_pass

    @key_pass.setter
    def key_pass(self, key_pass):
        """Sets the key_pass of this KafkaConfig.

        Optional keypass

        :param key_pass: The key_pass of this KafkaConfig.
        :type key_pass: str
        """

        self._key_pass = key_pass

    @property
    def key_store(self):
        """Gets the key_store of this KafkaConfig.

        Optional path to keystore

        :return: The key_store of this KafkaConfig.
        :rtype: str
        """
        return self._key_store

    @key_store.setter
    def key_store(self, key_store):
        """Sets the key_store of this KafkaConfig.

        Optional path to keystore

        :param key_store: The key_store of this KafkaConfig.
        :type key_store: str
        """

        self._key_store = key_store

    @property
    def servers(self):
        """Gets the servers of this KafkaConfig.

        URLs of the kafka servers

        :return: The servers of this KafkaConfig.
        :rtype: List[str]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this KafkaConfig.

        URLs of the kafka servers

        :param servers: The servers of this KafkaConfig.
        :type servers: List[str]
        """
        if servers is None:
            raise ValueError("Invalid value for `servers`, must not be `None`")

        self._servers = servers

    @property
    def topic(self):
        """Gets the topic of this KafkaConfig.

        Optional kafka topic (otoroshi-events by default)

        :return: The topic of this KafkaConfig.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this KafkaConfig.

        Optional kafka topic (otoroshi-events by default)

        :param topic: The topic of this KafkaConfig.
        :type topic: str
        """

        self._topic = topic

    @property
    def trustore(self):
        """Gets the trustore of this KafkaConfig.

        Optional path to trustore

        :return: The trustore of this KafkaConfig.
        :rtype: str
        """
        return self._trustore

    @trustore.setter
    def trustore(self, trustore):
        """Sets the trustore of this KafkaConfig.

        Optional path to trustore

        :param trustore: The trustore of this KafkaConfig.
        :type trustore: str
        """

        self._trustore = trustore
