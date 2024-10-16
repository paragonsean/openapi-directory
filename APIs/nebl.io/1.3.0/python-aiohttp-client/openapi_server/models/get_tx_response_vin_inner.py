# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_transaction_info_response_vin_inner_script_sig import GetTransactionInfoResponseVinInnerScriptSig
from openapi_server import util


class GetTxResponseVinInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, n: float=None, script_sig: GetTransactionInfoResponseVinInnerScriptSig=None, sequence: float=None, txid: str=None, value: float=None, value_sat: float=None, vout: float=None):
        """GetTxResponseVinInner - a model defined in OpenAPI

        :param n: The n of this GetTxResponseVinInner.
        :param script_sig: The script_sig of this GetTxResponseVinInner.
        :param sequence: The sequence of this GetTxResponseVinInner.
        :param txid: The txid of this GetTxResponseVinInner.
        :param value: The value of this GetTxResponseVinInner.
        :param value_sat: The value_sat of this GetTxResponseVinInner.
        :param vout: The vout of this GetTxResponseVinInner.
        """
        self.openapi_types = {
            'n': float,
            'script_sig': GetTransactionInfoResponseVinInnerScriptSig,
            'sequence': float,
            'txid': str,
            'value': float,
            'value_sat': float,
            'vout': float
        }

        self.attribute_map = {
            'n': 'n',
            'script_sig': 'scriptSig',
            'sequence': 'sequence',
            'txid': 'txid',
            'value': 'value',
            'value_sat': 'valueSat',
            'vout': 'vout'
        }

        self._n = n
        self._script_sig = script_sig
        self._sequence = sequence
        self._txid = txid
        self._value = value
        self._value_sat = value_sat
        self._vout = vout

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetTxResponseVinInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getTxResponse_vin_inner of this GetTxResponseVinInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def n(self):
        """Gets the n of this GetTxResponseVinInner.

        input index

        :return: The n of this GetTxResponseVinInner.
        :rtype: float
        """
        return self._n

    @n.setter
    def n(self, n):
        """Sets the n of this GetTxResponseVinInner.

        input index

        :param n: The n of this GetTxResponseVinInner.
        :type n: float
        """

        self._n = n

    @property
    def script_sig(self):
        """Gets the script_sig of this GetTxResponseVinInner.


        :return: The script_sig of this GetTxResponseVinInner.
        :rtype: GetTransactionInfoResponseVinInnerScriptSig
        """
        return self._script_sig

    @script_sig.setter
    def script_sig(self, script_sig):
        """Sets the script_sig of this GetTxResponseVinInner.


        :param script_sig: The script_sig of this GetTxResponseVinInner.
        :type script_sig: GetTransactionInfoResponseVinInnerScriptSig
        """

        self._script_sig = script_sig

    @property
    def sequence(self):
        """Gets the sequence of this GetTxResponseVinInner.


        :return: The sequence of this GetTxResponseVinInner.
        :rtype: float
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this GetTxResponseVinInner.


        :param sequence: The sequence of this GetTxResponseVinInner.
        :type sequence: float
        """

        self._sequence = sequence

    @property
    def txid(self):
        """Gets the txid of this GetTxResponseVinInner.

        TXID of the input

        :return: The txid of this GetTxResponseVinInner.
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this GetTxResponseVinInner.

        TXID of the input

        :param txid: The txid of this GetTxResponseVinInner.
        :type txid: str
        """

        self._txid = txid

    @property
    def value(self):
        """Gets the value of this GetTxResponseVinInner.

        Value of input in NEBL

        :return: The value of this GetTxResponseVinInner.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GetTxResponseVinInner.

        Value of input in NEBL

        :param value: The value of this GetTxResponseVinInner.
        :type value: float
        """

        self._value = value

    @property
    def value_sat(self):
        """Gets the value_sat of this GetTxResponseVinInner.

        Value of input in NEBL satoshi

        :return: The value_sat of this GetTxResponseVinInner.
        :rtype: float
        """
        return self._value_sat

    @value_sat.setter
    def value_sat(self, value_sat):
        """Sets the value_sat of this GetTxResponseVinInner.

        Value of input in NEBL satoshi

        :param value_sat: The value_sat of this GetTxResponseVinInner.
        :type value_sat: float
        """

        self._value_sat = value_sat

    @property
    def vout(self):
        """Gets the vout of this GetTxResponseVinInner.

        output index

        :return: The vout of this GetTxResponseVinInner.
        :rtype: float
        """
        return self._vout

    @vout.setter
    def vout(self, vout):
        """Sets the vout of this GetTxResponseVinInner.

        output index

        :param vout: The vout of this GetTxResponseVinInner.
        :type vout: float
        """

        self._vout = vout
