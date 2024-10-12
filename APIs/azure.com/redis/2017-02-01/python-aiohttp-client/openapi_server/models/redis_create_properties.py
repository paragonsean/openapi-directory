# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.sku import Sku
import re
from openapi_server import util


class RedisCreateProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sku: Sku=None, enable_non_ssl_port: bool=None, redis_configuration: Dict[str, str]=None, shard_count: int=None, static_ip: str=None, subnet_id: str=None, tenant_settings: Dict[str, str]=None):
        """RedisCreateProperties - a model defined in OpenAPI

        :param sku: The sku of this RedisCreateProperties.
        :param enable_non_ssl_port: The enable_non_ssl_port of this RedisCreateProperties.
        :param redis_configuration: The redis_configuration of this RedisCreateProperties.
        :param shard_count: The shard_count of this RedisCreateProperties.
        :param static_ip: The static_ip of this RedisCreateProperties.
        :param subnet_id: The subnet_id of this RedisCreateProperties.
        :param tenant_settings: The tenant_settings of this RedisCreateProperties.
        """
        self.openapi_types = {
            'sku': Sku,
            'enable_non_ssl_port': bool,
            'redis_configuration': Dict[str, str],
            'shard_count': int,
            'static_ip': str,
            'subnet_id': str,
            'tenant_settings': Dict[str, str]
        }

        self.attribute_map = {
            'sku': 'sku',
            'enable_non_ssl_port': 'enableNonSslPort',
            'redis_configuration': 'redisConfiguration',
            'shard_count': 'shardCount',
            'static_ip': 'staticIP',
            'subnet_id': 'subnetId',
            'tenant_settings': 'tenantSettings'
        }

        self._sku = sku
        self._enable_non_ssl_port = enable_non_ssl_port
        self._redis_configuration = redis_configuration
        self._shard_count = shard_count
        self._static_ip = static_ip
        self._subnet_id = subnet_id
        self._tenant_settings = tenant_settings

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RedisCreateProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RedisCreateProperties of this RedisCreateProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sku(self):
        """Gets the sku of this RedisCreateProperties.


        :return: The sku of this RedisCreateProperties.
        :rtype: Sku
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this RedisCreateProperties.


        :param sku: The sku of this RedisCreateProperties.
        :type sku: Sku
        """
        if sku is None:
            raise ValueError("Invalid value for `sku`, must not be `None`")

        self._sku = sku

    @property
    def enable_non_ssl_port(self):
        """Gets the enable_non_ssl_port of this RedisCreateProperties.

        Specifies whether the non-ssl Redis server port (6379) is enabled.

        :return: The enable_non_ssl_port of this RedisCreateProperties.
        :rtype: bool
        """
        return self._enable_non_ssl_port

    @enable_non_ssl_port.setter
    def enable_non_ssl_port(self, enable_non_ssl_port):
        """Sets the enable_non_ssl_port of this RedisCreateProperties.

        Specifies whether the non-ssl Redis server port (6379) is enabled.

        :param enable_non_ssl_port: The enable_non_ssl_port of this RedisCreateProperties.
        :type enable_non_ssl_port: bool
        """

        self._enable_non_ssl_port = enable_non_ssl_port

    @property
    def redis_configuration(self):
        """Gets the redis_configuration of this RedisCreateProperties.

        All Redis Settings. Few possible keys: rdb-backup-enabled,rdb-storage-connection-string,rdb-backup-frequency,maxmemory-delta,maxmemory-policy,notify-keyspace-events,maxmemory-samples,slowlog-log-slower-than,slowlog-max-len,list-max-ziplist-entries,list-max-ziplist-value,hash-max-ziplist-entries,hash-max-ziplist-value,set-max-intset-entries,zset-max-ziplist-entries,zset-max-ziplist-value etc.

        :return: The redis_configuration of this RedisCreateProperties.
        :rtype: Dict[str, str]
        """
        return self._redis_configuration

    @redis_configuration.setter
    def redis_configuration(self, redis_configuration):
        """Sets the redis_configuration of this RedisCreateProperties.

        All Redis Settings. Few possible keys: rdb-backup-enabled,rdb-storage-connection-string,rdb-backup-frequency,maxmemory-delta,maxmemory-policy,notify-keyspace-events,maxmemory-samples,slowlog-log-slower-than,slowlog-max-len,list-max-ziplist-entries,list-max-ziplist-value,hash-max-ziplist-entries,hash-max-ziplist-value,set-max-intset-entries,zset-max-ziplist-entries,zset-max-ziplist-value etc.

        :param redis_configuration: The redis_configuration of this RedisCreateProperties.
        :type redis_configuration: Dict[str, str]
        """

        self._redis_configuration = redis_configuration

    @property
    def shard_count(self):
        """Gets the shard_count of this RedisCreateProperties.

        The number of shards to be created on a Premium Cluster Cache.

        :return: The shard_count of this RedisCreateProperties.
        :rtype: int
        """
        return self._shard_count

    @shard_count.setter
    def shard_count(self, shard_count):
        """Sets the shard_count of this RedisCreateProperties.

        The number of shards to be created on a Premium Cluster Cache.

        :param shard_count: The shard_count of this RedisCreateProperties.
        :type shard_count: int
        """

        self._shard_count = shard_count

    @property
    def static_ip(self):
        """Gets the static_ip of this RedisCreateProperties.

        Static IP address. Required when deploying a Redis cache inside an existing Azure Virtual Network.

        :return: The static_ip of this RedisCreateProperties.
        :rtype: str
        """
        return self._static_ip

    @static_ip.setter
    def static_ip(self, static_ip):
        """Sets the static_ip of this RedisCreateProperties.

        Static IP address. Required when deploying a Redis cache inside an existing Azure Virtual Network.

        :param static_ip: The static_ip of this RedisCreateProperties.
        :type static_ip: str
        """
        if static_ip is not None and not re.search(r'^\d+\.\d+\.\d+\.\d+$', static_ip):
            raise ValueError("Invalid value for `static_ip`, must be a follow pattern or equal to `/^\d+\.\d+\.\d+\.\d+$/`")

        self._static_ip = static_ip

    @property
    def subnet_id(self):
        """Gets the subnet_id of this RedisCreateProperties.

        The full resource ID of a subnet in a virtual network to deploy the Redis cache in. Example format: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/Microsoft.{Network|ClassicNetwork}/VirtualNetworks/vnet1/subnets/subnet1

        :return: The subnet_id of this RedisCreateProperties.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this RedisCreateProperties.

        The full resource ID of a subnet in a virtual network to deploy the Redis cache in. Example format: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/Microsoft.{Network|ClassicNetwork}/VirtualNetworks/vnet1/subnets/subnet1

        :param subnet_id: The subnet_id of this RedisCreateProperties.
        :type subnet_id: str
        """
        if subnet_id is not None and not re.search(r'^\/subscriptions\/[^\/]*\/resourceGroups\/[^\/]*\/providers\/Microsoft.(ClassicNetwork|Network)\/virtualNetworks\/[^\/]*\/subnets\/[^\/]*$', subnet_id):
            raise ValueError("Invalid value for `subnet_id`, must be a follow pattern or equal to `/^\/subscriptions\/[^\/]*\/resourceGroups\/[^\/]*\/providers\/Microsoft.(ClassicNetwork|Network)\/virtualNetworks\/[^\/]*\/subnets\/[^\/]*$/`")

        self._subnet_id = subnet_id

    @property
    def tenant_settings(self):
        """Gets the tenant_settings of this RedisCreateProperties.

        tenantSettings

        :return: The tenant_settings of this RedisCreateProperties.
        :rtype: Dict[str, str]
        """
        return self._tenant_settings

    @tenant_settings.setter
    def tenant_settings(self, tenant_settings):
        """Sets the tenant_settings of this RedisCreateProperties.

        tenantSettings

        :param tenant_settings: The tenant_settings of this RedisCreateProperties.
        :type tenant_settings: Dict[str, str]
        """

        self._tenant_settings = tenant_settings
