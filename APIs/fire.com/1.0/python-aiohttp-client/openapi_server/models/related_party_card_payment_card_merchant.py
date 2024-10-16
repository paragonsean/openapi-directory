# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class RelatedPartyCardPaymentCardMerchant(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, acquirer_id_de32: str=None, additional_amt_de54: str=None, additional_data_de124: str=None, additional_data_de48: str=None, auth_code_de38: str=None, authorised_by_gps: str=None, avs_result: str=None, bill_amt: int=None, bill_ccy: str=None, expiry_date: str=None, mcc_code: str=None, merch_id_de42: str=None, merch_name_de43: str=None, mt_id: str=None, pos_data_de22: str=None, pos_data_de61: str=None, pos_termnl_de41: str=None, proc_code: str=None, record_data_de120: str=None, resp_code_de39: str=None, ret_ref_no_de37: str=None, status_code: str=None, token: str=None, txn_amt4d: int=None, txn_ccy: str=None, txn_ctry: str=None, txn_desc: str=None, txn_stat_code: str=None, txn_type: str=None):
        """RelatedPartyCardPaymentCardMerchant - a model defined in OpenAPI

        :param acquirer_id_de32: The acquirer_id_de32 of this RelatedPartyCardPaymentCardMerchant.
        :param additional_amt_de54: The additional_amt_de54 of this RelatedPartyCardPaymentCardMerchant.
        :param additional_data_de124: The additional_data_de124 of this RelatedPartyCardPaymentCardMerchant.
        :param additional_data_de48: The additional_data_de48 of this RelatedPartyCardPaymentCardMerchant.
        :param auth_code_de38: The auth_code_de38 of this RelatedPartyCardPaymentCardMerchant.
        :param authorised_by_gps: The authorised_by_gps of this RelatedPartyCardPaymentCardMerchant.
        :param avs_result: The avs_result of this RelatedPartyCardPaymentCardMerchant.
        :param bill_amt: The bill_amt of this RelatedPartyCardPaymentCardMerchant.
        :param bill_ccy: The bill_ccy of this RelatedPartyCardPaymentCardMerchant.
        :param expiry_date: The expiry_date of this RelatedPartyCardPaymentCardMerchant.
        :param mcc_code: The mcc_code of this RelatedPartyCardPaymentCardMerchant.
        :param merch_id_de42: The merch_id_de42 of this RelatedPartyCardPaymentCardMerchant.
        :param merch_name_de43: The merch_name_de43 of this RelatedPartyCardPaymentCardMerchant.
        :param mt_id: The mt_id of this RelatedPartyCardPaymentCardMerchant.
        :param pos_data_de22: The pos_data_de22 of this RelatedPartyCardPaymentCardMerchant.
        :param pos_data_de61: The pos_data_de61 of this RelatedPartyCardPaymentCardMerchant.
        :param pos_termnl_de41: The pos_termnl_de41 of this RelatedPartyCardPaymentCardMerchant.
        :param proc_code: The proc_code of this RelatedPartyCardPaymentCardMerchant.
        :param record_data_de120: The record_data_de120 of this RelatedPartyCardPaymentCardMerchant.
        :param resp_code_de39: The resp_code_de39 of this RelatedPartyCardPaymentCardMerchant.
        :param ret_ref_no_de37: The ret_ref_no_de37 of this RelatedPartyCardPaymentCardMerchant.
        :param status_code: The status_code of this RelatedPartyCardPaymentCardMerchant.
        :param token: The token of this RelatedPartyCardPaymentCardMerchant.
        :param txn_amt4d: The txn_amt4d of this RelatedPartyCardPaymentCardMerchant.
        :param txn_ccy: The txn_ccy of this RelatedPartyCardPaymentCardMerchant.
        :param txn_ctry: The txn_ctry of this RelatedPartyCardPaymentCardMerchant.
        :param txn_desc: The txn_desc of this RelatedPartyCardPaymentCardMerchant.
        :param txn_stat_code: The txn_stat_code of this RelatedPartyCardPaymentCardMerchant.
        :param txn_type: The txn_type of this RelatedPartyCardPaymentCardMerchant.
        """
        self.openapi_types = {
            'acquirer_id_de32': str,
            'additional_amt_de54': str,
            'additional_data_de124': str,
            'additional_data_de48': str,
            'auth_code_de38': str,
            'authorised_by_gps': str,
            'avs_result': str,
            'bill_amt': int,
            'bill_ccy': str,
            'expiry_date': str,
            'mcc_code': str,
            'merch_id_de42': str,
            'merch_name_de43': str,
            'mt_id': str,
            'pos_data_de22': str,
            'pos_data_de61': str,
            'pos_termnl_de41': str,
            'proc_code': str,
            'record_data_de120': str,
            'resp_code_de39': str,
            'ret_ref_no_de37': str,
            'status_code': str,
            'token': str,
            'txn_amt4d': int,
            'txn_ccy': str,
            'txn_ctry': str,
            'txn_desc': str,
            'txn_stat_code': str,
            'txn_type': str
        }

        self.attribute_map = {
            'acquirer_id_de32': 'acquirerIdDe32',
            'additional_amt_de54': 'additionalAmtDe54',
            'additional_data_de124': 'additionalDataDe124',
            'additional_data_de48': 'additionalDataDe48',
            'auth_code_de38': 'authCodeDe38',
            'authorised_by_gps': 'authorisedByGps',
            'avs_result': 'avsResult',
            'bill_amt': 'billAmt',
            'bill_ccy': 'billCcy',
            'expiry_date': 'expiryDate',
            'mcc_code': 'mccCode',
            'merch_id_de42': 'merchIdDe42',
            'merch_name_de43': 'merchNameDe43',
            'mt_id': 'mtId',
            'pos_data_de22': 'posDataDe22',
            'pos_data_de61': 'posDataDe61',
            'pos_termnl_de41': 'posTermnlDe41',
            'proc_code': 'procCode',
            'record_data_de120': 'recordDataDe120',
            'resp_code_de39': 'respCodeDe39',
            'ret_ref_no_de37': 'retRefNoDe37',
            'status_code': 'statusCode',
            'token': 'token',
            'txn_amt4d': 'txnAmt4d',
            'txn_ccy': 'txnCcy',
            'txn_ctry': 'txnCtry',
            'txn_desc': 'txnDesc',
            'txn_stat_code': 'txnStatCode',
            'txn_type': 'txnType'
        }

        self._acquirer_id_de32 = acquirer_id_de32
        self._additional_amt_de54 = additional_amt_de54
        self._additional_data_de124 = additional_data_de124
        self._additional_data_de48 = additional_data_de48
        self._auth_code_de38 = auth_code_de38
        self._authorised_by_gps = authorised_by_gps
        self._avs_result = avs_result
        self._bill_amt = bill_amt
        self._bill_ccy = bill_ccy
        self._expiry_date = expiry_date
        self._mcc_code = mcc_code
        self._merch_id_de42 = merch_id_de42
        self._merch_name_de43 = merch_name_de43
        self._mt_id = mt_id
        self._pos_data_de22 = pos_data_de22
        self._pos_data_de61 = pos_data_de61
        self._pos_termnl_de41 = pos_termnl_de41
        self._proc_code = proc_code
        self._record_data_de120 = record_data_de120
        self._resp_code_de39 = resp_code_de39
        self._ret_ref_no_de37 = ret_ref_no_de37
        self._status_code = status_code
        self._token = token
        self._txn_amt4d = txn_amt4d
        self._txn_ccy = txn_ccy
        self._txn_ctry = txn_ctry
        self._txn_desc = txn_desc
        self._txn_stat_code = txn_stat_code
        self._txn_type = txn_type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RelatedPartyCardPaymentCardMerchant':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The relatedPartyCardPayment_cardMerchant of this RelatedPartyCardPaymentCardMerchant.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def acquirer_id_de32(self):
        """Gets the acquirer_id_de32 of this RelatedPartyCardPaymentCardMerchant.


        :return: The acquirer_id_de32 of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._acquirer_id_de32

    @acquirer_id_de32.setter
    def acquirer_id_de32(self, acquirer_id_de32):
        """Sets the acquirer_id_de32 of this RelatedPartyCardPaymentCardMerchant.


        :param acquirer_id_de32: The acquirer_id_de32 of this RelatedPartyCardPaymentCardMerchant.
        :type acquirer_id_de32: str
        """

        self._acquirer_id_de32 = acquirer_id_de32

    @property
    def additional_amt_de54(self):
        """Gets the additional_amt_de54 of this RelatedPartyCardPaymentCardMerchant.


        :return: The additional_amt_de54 of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._additional_amt_de54

    @additional_amt_de54.setter
    def additional_amt_de54(self, additional_amt_de54):
        """Sets the additional_amt_de54 of this RelatedPartyCardPaymentCardMerchant.


        :param additional_amt_de54: The additional_amt_de54 of this RelatedPartyCardPaymentCardMerchant.
        :type additional_amt_de54: str
        """

        self._additional_amt_de54 = additional_amt_de54

    @property
    def additional_data_de124(self):
        """Gets the additional_data_de124 of this RelatedPartyCardPaymentCardMerchant.


        :return: The additional_data_de124 of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._additional_data_de124

    @additional_data_de124.setter
    def additional_data_de124(self, additional_data_de124):
        """Sets the additional_data_de124 of this RelatedPartyCardPaymentCardMerchant.


        :param additional_data_de124: The additional_data_de124 of this RelatedPartyCardPaymentCardMerchant.
        :type additional_data_de124: str
        """

        self._additional_data_de124 = additional_data_de124

    @property
    def additional_data_de48(self):
        """Gets the additional_data_de48 of this RelatedPartyCardPaymentCardMerchant.


        :return: The additional_data_de48 of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._additional_data_de48

    @additional_data_de48.setter
    def additional_data_de48(self, additional_data_de48):
        """Sets the additional_data_de48 of this RelatedPartyCardPaymentCardMerchant.


        :param additional_data_de48: The additional_data_de48 of this RelatedPartyCardPaymentCardMerchant.
        :type additional_data_de48: str
        """

        self._additional_data_de48 = additional_data_de48

    @property
    def auth_code_de38(self):
        """Gets the auth_code_de38 of this RelatedPartyCardPaymentCardMerchant.


        :return: The auth_code_de38 of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._auth_code_de38

    @auth_code_de38.setter
    def auth_code_de38(self, auth_code_de38):
        """Sets the auth_code_de38 of this RelatedPartyCardPaymentCardMerchant.


        :param auth_code_de38: The auth_code_de38 of this RelatedPartyCardPaymentCardMerchant.
        :type auth_code_de38: str
        """

        self._auth_code_de38 = auth_code_de38

    @property
    def authorised_by_gps(self):
        """Gets the authorised_by_gps of this RelatedPartyCardPaymentCardMerchant.


        :return: The authorised_by_gps of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._authorised_by_gps

    @authorised_by_gps.setter
    def authorised_by_gps(self, authorised_by_gps):
        """Sets the authorised_by_gps of this RelatedPartyCardPaymentCardMerchant.


        :param authorised_by_gps: The authorised_by_gps of this RelatedPartyCardPaymentCardMerchant.
        :type authorised_by_gps: str
        """

        self._authorised_by_gps = authorised_by_gps

    @property
    def avs_result(self):
        """Gets the avs_result of this RelatedPartyCardPaymentCardMerchant.


        :return: The avs_result of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._avs_result

    @avs_result.setter
    def avs_result(self, avs_result):
        """Sets the avs_result of this RelatedPartyCardPaymentCardMerchant.


        :param avs_result: The avs_result of this RelatedPartyCardPaymentCardMerchant.
        :type avs_result: str
        """

        self._avs_result = avs_result

    @property
    def bill_amt(self):
        """Gets the bill_amt of this RelatedPartyCardPaymentCardMerchant.


        :return: The bill_amt of this RelatedPartyCardPaymentCardMerchant.
        :rtype: int
        """
        return self._bill_amt

    @bill_amt.setter
    def bill_amt(self, bill_amt):
        """Sets the bill_amt of this RelatedPartyCardPaymentCardMerchant.


        :param bill_amt: The bill_amt of this RelatedPartyCardPaymentCardMerchant.
        :type bill_amt: int
        """

        self._bill_amt = bill_amt

    @property
    def bill_ccy(self):
        """Gets the bill_ccy of this RelatedPartyCardPaymentCardMerchant.


        :return: The bill_ccy of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._bill_ccy

    @bill_ccy.setter
    def bill_ccy(self, bill_ccy):
        """Sets the bill_ccy of this RelatedPartyCardPaymentCardMerchant.


        :param bill_ccy: The bill_ccy of this RelatedPartyCardPaymentCardMerchant.
        :type bill_ccy: str
        """

        self._bill_ccy = bill_ccy

    @property
    def expiry_date(self):
        """Gets the expiry_date of this RelatedPartyCardPaymentCardMerchant.


        :return: The expiry_date of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this RelatedPartyCardPaymentCardMerchant.


        :param expiry_date: The expiry_date of this RelatedPartyCardPaymentCardMerchant.
        :type expiry_date: str
        """

        self._expiry_date = expiry_date

    @property
    def mcc_code(self):
        """Gets the mcc_code of this RelatedPartyCardPaymentCardMerchant.


        :return: The mcc_code of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, mcc_code):
        """Sets the mcc_code of this RelatedPartyCardPaymentCardMerchant.


        :param mcc_code: The mcc_code of this RelatedPartyCardPaymentCardMerchant.
        :type mcc_code: str
        """

        self._mcc_code = mcc_code

    @property
    def merch_id_de42(self):
        """Gets the merch_id_de42 of this RelatedPartyCardPaymentCardMerchant.


        :return: The merch_id_de42 of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._merch_id_de42

    @merch_id_de42.setter
    def merch_id_de42(self, merch_id_de42):
        """Sets the merch_id_de42 of this RelatedPartyCardPaymentCardMerchant.


        :param merch_id_de42: The merch_id_de42 of this RelatedPartyCardPaymentCardMerchant.
        :type merch_id_de42: str
        """

        self._merch_id_de42 = merch_id_de42

    @property
    def merch_name_de43(self):
        """Gets the merch_name_de43 of this RelatedPartyCardPaymentCardMerchant.


        :return: The merch_name_de43 of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._merch_name_de43

    @merch_name_de43.setter
    def merch_name_de43(self, merch_name_de43):
        """Sets the merch_name_de43 of this RelatedPartyCardPaymentCardMerchant.


        :param merch_name_de43: The merch_name_de43 of this RelatedPartyCardPaymentCardMerchant.
        :type merch_name_de43: str
        """

        self._merch_name_de43 = merch_name_de43

    @property
    def mt_id(self):
        """Gets the mt_id of this RelatedPartyCardPaymentCardMerchant.


        :return: The mt_id of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._mt_id

    @mt_id.setter
    def mt_id(self, mt_id):
        """Sets the mt_id of this RelatedPartyCardPaymentCardMerchant.


        :param mt_id: The mt_id of this RelatedPartyCardPaymentCardMerchant.
        :type mt_id: str
        """

        self._mt_id = mt_id

    @property
    def pos_data_de22(self):
        """Gets the pos_data_de22 of this RelatedPartyCardPaymentCardMerchant.


        :return: The pos_data_de22 of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._pos_data_de22

    @pos_data_de22.setter
    def pos_data_de22(self, pos_data_de22):
        """Sets the pos_data_de22 of this RelatedPartyCardPaymentCardMerchant.


        :param pos_data_de22: The pos_data_de22 of this RelatedPartyCardPaymentCardMerchant.
        :type pos_data_de22: str
        """

        self._pos_data_de22 = pos_data_de22

    @property
    def pos_data_de61(self):
        """Gets the pos_data_de61 of this RelatedPartyCardPaymentCardMerchant.


        :return: The pos_data_de61 of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._pos_data_de61

    @pos_data_de61.setter
    def pos_data_de61(self, pos_data_de61):
        """Sets the pos_data_de61 of this RelatedPartyCardPaymentCardMerchant.


        :param pos_data_de61: The pos_data_de61 of this RelatedPartyCardPaymentCardMerchant.
        :type pos_data_de61: str
        """

        self._pos_data_de61 = pos_data_de61

    @property
    def pos_termnl_de41(self):
        """Gets the pos_termnl_de41 of this RelatedPartyCardPaymentCardMerchant.


        :return: The pos_termnl_de41 of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._pos_termnl_de41

    @pos_termnl_de41.setter
    def pos_termnl_de41(self, pos_termnl_de41):
        """Sets the pos_termnl_de41 of this RelatedPartyCardPaymentCardMerchant.


        :param pos_termnl_de41: The pos_termnl_de41 of this RelatedPartyCardPaymentCardMerchant.
        :type pos_termnl_de41: str
        """

        self._pos_termnl_de41 = pos_termnl_de41

    @property
    def proc_code(self):
        """Gets the proc_code of this RelatedPartyCardPaymentCardMerchant.


        :return: The proc_code of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._proc_code

    @proc_code.setter
    def proc_code(self, proc_code):
        """Sets the proc_code of this RelatedPartyCardPaymentCardMerchant.


        :param proc_code: The proc_code of this RelatedPartyCardPaymentCardMerchant.
        :type proc_code: str
        """

        self._proc_code = proc_code

    @property
    def record_data_de120(self):
        """Gets the record_data_de120 of this RelatedPartyCardPaymentCardMerchant.


        :return: The record_data_de120 of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._record_data_de120

    @record_data_de120.setter
    def record_data_de120(self, record_data_de120):
        """Sets the record_data_de120 of this RelatedPartyCardPaymentCardMerchant.


        :param record_data_de120: The record_data_de120 of this RelatedPartyCardPaymentCardMerchant.
        :type record_data_de120: str
        """

        self._record_data_de120 = record_data_de120

    @property
    def resp_code_de39(self):
        """Gets the resp_code_de39 of this RelatedPartyCardPaymentCardMerchant.


        :return: The resp_code_de39 of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._resp_code_de39

    @resp_code_de39.setter
    def resp_code_de39(self, resp_code_de39):
        """Sets the resp_code_de39 of this RelatedPartyCardPaymentCardMerchant.


        :param resp_code_de39: The resp_code_de39 of this RelatedPartyCardPaymentCardMerchant.
        :type resp_code_de39: str
        """

        self._resp_code_de39 = resp_code_de39

    @property
    def ret_ref_no_de37(self):
        """Gets the ret_ref_no_de37 of this RelatedPartyCardPaymentCardMerchant.


        :return: The ret_ref_no_de37 of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._ret_ref_no_de37

    @ret_ref_no_de37.setter
    def ret_ref_no_de37(self, ret_ref_no_de37):
        """Sets the ret_ref_no_de37 of this RelatedPartyCardPaymentCardMerchant.


        :param ret_ref_no_de37: The ret_ref_no_de37 of this RelatedPartyCardPaymentCardMerchant.
        :type ret_ref_no_de37: str
        """

        self._ret_ref_no_de37 = ret_ref_no_de37

    @property
    def status_code(self):
        """Gets the status_code of this RelatedPartyCardPaymentCardMerchant.


        :return: The status_code of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this RelatedPartyCardPaymentCardMerchant.


        :param status_code: The status_code of this RelatedPartyCardPaymentCardMerchant.
        :type status_code: str
        """

        self._status_code = status_code

    @property
    def token(self):
        """Gets the token of this RelatedPartyCardPaymentCardMerchant.


        :return: The token of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this RelatedPartyCardPaymentCardMerchant.


        :param token: The token of this RelatedPartyCardPaymentCardMerchant.
        :type token: str
        """

        self._token = token

    @property
    def txn_amt4d(self):
        """Gets the txn_amt4d of this RelatedPartyCardPaymentCardMerchant.


        :return: The txn_amt4d of this RelatedPartyCardPaymentCardMerchant.
        :rtype: int
        """
        return self._txn_amt4d

    @txn_amt4d.setter
    def txn_amt4d(self, txn_amt4d):
        """Sets the txn_amt4d of this RelatedPartyCardPaymentCardMerchant.


        :param txn_amt4d: The txn_amt4d of this RelatedPartyCardPaymentCardMerchant.
        :type txn_amt4d: int
        """

        self._txn_amt4d = txn_amt4d

    @property
    def txn_ccy(self):
        """Gets the txn_ccy of this RelatedPartyCardPaymentCardMerchant.


        :return: The txn_ccy of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._txn_ccy

    @txn_ccy.setter
    def txn_ccy(self, txn_ccy):
        """Sets the txn_ccy of this RelatedPartyCardPaymentCardMerchant.


        :param txn_ccy: The txn_ccy of this RelatedPartyCardPaymentCardMerchant.
        :type txn_ccy: str
        """

        self._txn_ccy = txn_ccy

    @property
    def txn_ctry(self):
        """Gets the txn_ctry of this RelatedPartyCardPaymentCardMerchant.


        :return: The txn_ctry of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._txn_ctry

    @txn_ctry.setter
    def txn_ctry(self, txn_ctry):
        """Sets the txn_ctry of this RelatedPartyCardPaymentCardMerchant.


        :param txn_ctry: The txn_ctry of this RelatedPartyCardPaymentCardMerchant.
        :type txn_ctry: str
        """

        self._txn_ctry = txn_ctry

    @property
    def txn_desc(self):
        """Gets the txn_desc of this RelatedPartyCardPaymentCardMerchant.


        :return: The txn_desc of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._txn_desc

    @txn_desc.setter
    def txn_desc(self, txn_desc):
        """Sets the txn_desc of this RelatedPartyCardPaymentCardMerchant.


        :param txn_desc: The txn_desc of this RelatedPartyCardPaymentCardMerchant.
        :type txn_desc: str
        """

        self._txn_desc = txn_desc

    @property
    def txn_stat_code(self):
        """Gets the txn_stat_code of this RelatedPartyCardPaymentCardMerchant.


        :return: The txn_stat_code of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._txn_stat_code

    @txn_stat_code.setter
    def txn_stat_code(self, txn_stat_code):
        """Sets the txn_stat_code of this RelatedPartyCardPaymentCardMerchant.


        :param txn_stat_code: The txn_stat_code of this RelatedPartyCardPaymentCardMerchant.
        :type txn_stat_code: str
        """

        self._txn_stat_code = txn_stat_code

    @property
    def txn_type(self):
        """Gets the txn_type of this RelatedPartyCardPaymentCardMerchant.


        :return: The txn_type of this RelatedPartyCardPaymentCardMerchant.
        :rtype: str
        """
        return self._txn_type

    @txn_type.setter
    def txn_type(self, txn_type):
        """Sets the txn_type of this RelatedPartyCardPaymentCardMerchant.


        :param txn_type: The txn_type of this RelatedPartyCardPaymentCardMerchant.
        :type txn_type: str
        """

        self._txn_type = txn_type
