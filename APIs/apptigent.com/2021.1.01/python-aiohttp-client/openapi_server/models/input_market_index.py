# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class InputMarketIndex(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, _date: str=None, symbol: str=None):
        """InputMarketIndex - a model defined in OpenAPI

        :param _date: The _date of this InputMarketIndex.
        :param symbol: The symbol of this InputMarketIndex.
        """
        self.openapi_types = {
            '_date': str,
            'symbol': str
        }

        self.attribute_map = {
            '_date': 'date',
            'symbol': 'symbol'
        }

        self.__date = _date
        self._symbol = symbol

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InputMarketIndex':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The inputMarketIndex of this InputMarketIndex.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _date(self):
        """Gets the _date of this InputMarketIndex.

        Date (yyyy-MM-dd, leave empty for last trading day)

        :return: The _date of this InputMarketIndex.
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this InputMarketIndex.

        Date (yyyy-MM-dd, leave empty for last trading day)

        :param _date: The _date of this InputMarketIndex.
        :type _date: str
        """

        self.__date = _date

    @property
    def symbol(self):
        """Gets the symbol of this InputMarketIndex.

        Market index

        :return: The symbol of this InputMarketIndex.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this InputMarketIndex.

        Market index

        :param symbol: The symbol of this InputMarketIndex.
        :type symbol: str
        """
        allowed_values = ["DJA.INDX (Dow Jones Composite Average)", "DJI.INDX (Dow Jones Industrial Average)", "DJT.INDX (Dow Jones Transportation)", "DJUS.INDX (Dow Jones US)", "DXY.INDX (US Dollar Index)", "GDOW.INDX (Global Dow USD)", "NY.INDX (NYSE US 100 Index)", "NYA.INDX (NYSE Composite)", "IXIC.INDX (NASDAQ Composite)", "NDX.INDX (NASDAQ 100)", "GSPC.INDX (S&P 500)", "ES.INDX (S&P 500 Futures)", "MID.INDX (S&P Midcap 400)", "GPTSE.INDX (S&P TSX Composite Index [Canada])", "FTSE.INDX (FTSE 100 Index [UK])", "CDAXX.INDX (DAX Composite Index [Germany])", "GDAXI.INDX (DAX Index [Germany])", "HSCE.INDX (Hang Seng China Enterprise (CEI))", "HSI.INDX (Hang Seng Index [Hong Kong])", "N100.INDX (EuroNext 100)", "N225.INDX (Nikkei 225 Index)", "RTSI.INDX (RTSI Index [Russia])", "SSEC.INDX (Shanghai Composite)", "SSMI.INDX (Swiss Market Index)"]  # noqa: E501
        if symbol not in allowed_values:
            raise ValueError(
                "Invalid value for `symbol` ({0}), must be one of {1}"
                .format(symbol, allowed_values)
            )

        self._symbol = symbol
