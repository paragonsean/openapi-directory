from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_usage import ApiUsage
from openapi_server.models.convert_price import ConvertPrice
from openapi_server.models.country_code_check import CountryCodeCheck
from openapi_server.models.create_invoice import CreateInvoice
from openapi_server.models.currency_conversion import CurrencyConversion
from openapi_server.models.ip_check import IPCheck
from openapi_server.models.invoice_data import InvoiceData
from openapi_server.models.retrieve_invoice import RetrieveInvoice
from openapi_server.models.update_invoice import UpdateInvoice
from openapi_server.models.update_invoice_array import UpdateInvoiceArray
from openapi_server.models.vat_rates import VatRates
from openapi_server import util


async def api_usage(request: web.Request, response_type=None) -> web.Response:
    """Check api requests remaining on current subscription plan

    

    :param response_type: The default response type is application/json if you would like to receive an XML response then set this to XML
    :type response_type: str

    """
    return web.Response(status=200)


async def convert_price(request: web.Request, code, price, response_type=None, country_rate=None, type=None) -> web.Response:
    """Convert a price to or from VAT price.

    

    :param code: The 2 digit country code
    :type code: str
    :param price: The price you want converting
    :type price: int
    :param response_type: The default response type is application/json if you would like to receive an XML response then set this to XML
    :type response_type: str
    :param country_rate: The VAT rate to get the price for. Default: standard
    :type country_rate: str
    :param type: Optional, if the price is including VAT set the type to &#39;incl&#39;. Otherwise the default is assumed as excluding VAT already, &#39;excl&#39;
    :type type: str

    """
    return web.Response(status=200)


async def country_code_check(request: web.Request, code, response_type=None) -> web.Response:
    """Retrieve a countries VAT rates by its 2 digit country code

    

    :param code: The 2 digit country code
    :type code: str
    :param response_type: The default response type is application/json if you would like to receive an XML response then set this to XML
    :type response_type: str

    """
    return web.Response(status=200)


async def create_invoice(request: web.Request, body, response_type=None) -> web.Response:
    """Create a VAT invoice

    

    :param body: Enter invoice data as JSON
    :type body: dict | bytes
    :param response_type: The default response type is application/json if you would like to receive an XML response then set this to XML
    :type response_type: str

    """
    body = InvoiceData.from_dict(body)
    return web.Response(status=200)


async def currency_conversion(request: web.Request, currency_from, currency_to, response_type=None, amount=None) -> web.Response:
    """Convert a currency

    

    :param currency_from: The currency code you are converting from
    :type currency_from: str
    :param currency_to: The currency code you are converting to
    :type currency_to: str
    :param response_type: The default response type is application/json if you would like to receive an XML response then set this to XML
    :type response_type: str
    :param amount: Optional, an amount you are wanting to convert. Leave blank to just get the current rate
    :type amount: int

    """
    return web.Response(status=200)


async def get_invoice(request: web.Request, id, response_type=None) -> web.Response:
    """Retrieve an invoice

    

    :param id: Enter the invoice id
    :type id: int
    :param response_type: The default response type is application/json if you would like to receive an XML response then set this to XML
    :type response_type: str

    """
    return web.Response(status=200)


async def invoice_delete(request: web.Request, id, response_type=None) -> web.Response:
    """Delete an invoice

    

    :param id: Enter an invoice id
    :type id: int
    :param response_type: The default response type is application/json if you would like to receive an XML response then set this to XML
    :type response_type: str

    """
    return web.Response(status=200)


async def invoice_update(request: web.Request, id, body, response_type=None) -> web.Response:
    """Update an existing invoice

    

    :param id: Enter an invoice id
    :type id: int
    :param body: Enter invoice data as JSON
    :type body: dict | bytes
    :param response_type: The default response type is application/json if you would like to receive an XML response then set this to XML
    :type response_type: str

    """
    body = UpdateInvoiceArray.from_dict(body)
    return web.Response(status=200)


async def ip_check(request: web.Request, address, response_type=None) -> web.Response:
    """Retrieve a countries VAT rates from an IP address

    

    :param address: The IP address to search against
    :type address: str
    :param response_type: The default response type is application/json if you would like to receive an XML response then set this to XML
    :type response_type: str

    """
    return web.Response(status=200)


async def vat_number_validate(request: web.Request, vatid, response_type=None) -> web.Response:
    """Validate a VAT number

    &lt;p&gt;We highly recommend if you are able, to check a VAT number on your end first to save wasted API lookups. It maybe that your customer has simply entered the wrong format. &lt;a href&#x3D;&#39;http://www.braemoor.co.uk/software/vat.shtml&#39; target&#x3D;&#39;_blank&#39;&gt;Heres a client side way to check the format using Javascript&lt;/a&gt;&lt;/p&gt;

    :param vatid: The VAT number to validate
    :type vatid: str
    :param response_type: The default response type is application/json if you would like to receive an XML response then set this to XML
    :type response_type: str

    """
    return web.Response(status=200)


async def vat_rates(request: web.Request, response_type=None) -> web.Response:
    """Retrieve all current EU VAT rates

    

    :param response_type: The default response type is application/json if you would like to receive an XML response then set this to XML
    :type response_type: str

    """
    return web.Response(status=200)
