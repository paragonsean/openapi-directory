# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class RpcRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str='neblio-apis', jsonrpc: str='1.0', method: str=None, params: List[str]=None):
        """RpcRequest - a model defined in OpenAPI

        :param id: The id of this RpcRequest.
        :param jsonrpc: The jsonrpc of this RpcRequest.
        :param method: The method of this RpcRequest.
        :param params: The params of this RpcRequest.
        """
        self.openapi_types = {
            'id': str,
            'jsonrpc': str,
            'method': str,
            'params': List[str]
        }

        self.attribute_map = {
            'id': 'id',
            'jsonrpc': 'jsonrpc',
            'method': 'method',
            'params': 'params'
        }

        self._id = id
        self._jsonrpc = jsonrpc
        self._method = method
        self._params = params

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RpcRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The rpcRequest of this RpcRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this RpcRequest.

        Identifier of RCP caller

        :return: The id of this RpcRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RpcRequest.

        Identifier of RCP caller

        :param id: The id of this RpcRequest.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def jsonrpc(self):
        """Gets the jsonrpc of this RpcRequest.

        JSON-RPC version

        :return: The jsonrpc of this RpcRequest.
        :rtype: str
        """
        return self._jsonrpc

    @jsonrpc.setter
    def jsonrpc(self, jsonrpc):
        """Sets the jsonrpc of this RpcRequest.

        JSON-RPC version

        :param jsonrpc: The jsonrpc of this RpcRequest.
        :type jsonrpc: str
        """
        if jsonrpc is None:
            raise ValueError("Invalid value for `jsonrpc`, must not be `None`")

        self._jsonrpc = jsonrpc

    @property
    def method(self):
        """Gets the method of this RpcRequest.

        Name of the Neblio RPC method to call

        :return: The method of this RpcRequest.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this RpcRequest.

        Name of the Neblio RPC method to call

        :param method: The method of this RpcRequest.
        :type method: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")

        self._method = method

    @property
    def params(self):
        """Gets the params of this RpcRequest.

        Array of string params that should be passed to the RPC method.

        :return: The params of this RpcRequest.
        :rtype: List[str]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this RpcRequest.

        Array of string params that should be passed to the RPC method.

        :param params: The params of this RpcRequest.
        :type params: List[str]
        """
        if params is None:
            raise ValueError("Invalid value for `params`, must not be `None`")

        self._params = params
