from typing import List, Dict
from aiohttp import web

from openapi_server.models.calculate_simple_tax_out import CalculateSimpleTaxOut
from openapi_server.models.calculate_tax_in import CalculateTaxIn
from openapi_server.models.calculate_tax_location_out import CalculateTaxLocationOut
from openapi_server.models.calculate_tax_out import CalculateTaxOut
from openapi_server.models.validate_tax_number_out import ValidateTaxNumberOut
from openapi_server import util


async def calculate_simple_tax(request: web.Request, currency_code, product_type=None, invoice_address_city=None, buyer_credit_card_prefix=None, invoice_address_region=None, unit_price=None, quantity=None, buyer_tax_number=None, force_country_code=None, order_date=None, amount=None, billing_country_code=None, invoice_address_postal_code=None, total_amount=None, tax_deducted=None) -> web.Response:
    """Simple tax

    

    :param currency_code: Currency code for transaction - e.g. EUR.
    :type currency_code: str
    :param product_type: Product type, according to dictionary /dictionaries/product_types. 
    :type product_type: str
    :param invoice_address_city: Invoice address/postal_code
    :type invoice_address_city: str
    :param buyer_credit_card_prefix: First 6 digits of buyer&#39;s credit card prefix.
    :type buyer_credit_card_prefix: str
    :param invoice_address_region: Invoice address/region
    :type invoice_address_region: str
    :param unit_price: Unit price.
    :type unit_price: 
    :param quantity: Quantity Defaults to 1.
    :type quantity: 
    :param buyer_tax_number:  Buyer&#39;s tax number - EU VAT number for example. If using EU VAT number, it is possible to provide country code in it (e.g. IE1234567X) or simply use billing_country_code field for that. In the first case, if billing_country_code value was provided, it will be overwritten with country code value extracted from VAT number - but only if the VAT has been verified properly.
    :type buyer_tax_number: str
    :param force_country_code: Two-letter ISO country code, e.g. FR. Use it to force country code for tax calculation.
    :type force_country_code: str
    :param order_date: Order date in yyyy-MM-dd format, in merchant&#39;s timezone. If provided by the API caller, no timezone conversion is performed. Default value is current date and time. When using public token, the default value is used.
    :type order_date: str
    :param amount: Amount. Required if total amount or both unit price and quantity are not provided.
    :type amount: 
    :param billing_country_code: Billing two letter ISO country code.
    :type billing_country_code: str
    :param invoice_address_postal_code: Invoice address/postal_code
    :type invoice_address_postal_code: str
    :param total_amount: Total amount. Required if amount or both unit price and quantity are not provided.
    :type total_amount: 
    :param tax_deducted: If the transaction is in a country supported by Taxamo, but the tax is not calculated due to merchant settings or EU B2B transaction for example.
    :type tax_deducted: bool

    """
    return web.Response(status=200)


async def calculate_tax(request: web.Request, input) -> web.Response:
    """Calculate tax

    

    :param input: Input
    :type input: dict | bytes

    """
    input = CalculateTaxIn.from_dict(input)
    return web.Response(status=200)


async def calculate_tax_location(request: web.Request, billing_country_code=None, buyer_credit_card_prefix=None) -> web.Response:
    """Calculate location

    

    :param billing_country_code: Billing two letter ISO country code.
    :type billing_country_code: str
    :param buyer_credit_card_prefix: First 6 digits of buyer&#39;s credit card prefix.
    :type buyer_credit_card_prefix: str

    """
    return web.Response(status=200)


async def validate_tax_number(request: web.Request, tax_number, country_code=None) -> web.Response:
    """Validate VAT number

    

    :param tax_number: Tax number
    :type tax_number: str
    :param country_code: Two-letter ISO country code.
    :type country_code: str

    """
    return web.Response(status=200)
