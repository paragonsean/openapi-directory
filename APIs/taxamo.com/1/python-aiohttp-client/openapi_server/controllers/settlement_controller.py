from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_detailed_refunds_out import GetDetailedRefundsOut
from openapi_server.models.get_refunds_out import GetRefundsOut
from openapi_server.models.get_settlement_out import GetSettlementOut
from openapi_server.models.get_settlement_summary_out import GetSettlementSummaryOut
from openapi_server import util


async def get_detailed_refunds(request: web.Request, format=None, country_codes=None, date_from=None, date_to=None, limit=None, offset=None) -> web.Response:
    """Detailed refunds

    

    :param format: Output format. &#39;json&#39; or &#39;csv&#39;. Default value is &#39;json&#39;
    :type format: str
    :param country_codes: Comma separated list of 2-letter country codes
    :type country_codes: str
    :param date_from: Take only refunds issued at or after the date. Format: yyyy-MM-dd
    :type date_from: str
    :param date_to: Take only refunds issued at or before the date. Format: yyyy-MM-dd
    :type date_to: str
    :param limit: Limit (no more than 1000, defaults to 100).
    :type limit: 
    :param offset: Offset. Defaults to 0
    :type offset: 

    """
    return web.Response(status=200)


async def get_refunds(request: web.Request, date_from, format=None, moss_country_code=None, tax_region=None) -> web.Response:
    """Fetch refunds

    

    :param date_from: Take only refunds issued at or after the date. Format: yyyy-MM-dd
    :type date_from: str
    :param format: Output format. &#39;csv&#39; value is accepted as well
    :type format: str
    :param moss_country_code: MOSS country code, used to determine currency. If ommited, merchant default setting is used.
    :type moss_country_code: str
    :param tax_region: Tax region key, defaults to EU for backwards compatibility.
    :type tax_region: str

    """
    return web.Response(status=200)


async def get_settlement(request: web.Request, quarter, moss_tax_id=None, currency_code=None, end_month=None, tax_id=None, refund_date_kind_override=None, start_month=None, moss_country_code=None, format=None, tax_country_code=None) -> web.Response:
    """Fetch settlement

    

    :param quarter: Quarter in yyyy-MM format. If start-date and end-date are provided, quarter is ignored and should be set to &#39;range&#39;.
    :type quarter: str
    :param moss_tax_id: MOSS-assigned tax ID - if not provided, merchant&#39;s national tax number will be used. Deprecated, please use tax-id.
    :type moss_tax_id: str
    :param currency_code: ISO 3-letter currency code, e.g. EUR or USD. If provided, all amounts will be coerced for this currency. Defaults to region&#39;s currency code.
    :type currency_code: str
    :param end_month: Period end month in yyyy-MM format. Either quarter or start-month and end-month have to be provided.
    :type end_month: str
    :param tax_id: MOSS-assigned tax ID - if not provided, merchant&#39;s national tax number will be used. Deprecated, please use tax-id.
    :type tax_id: str
    :param refund_date_kind_override: Set to &#39;order_date&#39; to show only refunds for the transactions in the selected reporting period. Set to &#39;refund_timestamp&#39; to show refunds that were created in the selected reporting period. Do not set to use the default region&#39;s setting.
    :type refund_date_kind_override: str
    :param start_month: Period start month in yyyy-MM format. Either quarter or start-month and end-month have to be provided.
    :type start_month: str
    :param moss_country_code: MOSS country code, used to determine currency/region. If ommited, merchant default setting is used. Deprecated: please use tax-country-code.
    :type moss_country_code: str
    :param format: Output format. &#39;csv&#39; value is accepted as well
    :type format: str
    :param tax_country_code: Tax entity country code, used to determine currency/region. 
    :type tax_country_code: str

    """
    return web.Response(status=200)


async def get_settlement_summary(request: web.Request, quarter, moss_country_code=None, tax_region=None, start_month=None, end_month=None) -> web.Response:
    """Fetch summary

    

    :param quarter: Quarter in yyyy-MM format. If start-date and end-date are provided, quarter is ignored and should be set to &#39;range&#39;.
    :type quarter: str
    :param moss_country_code: MOSS country code, used to determine currency. If ommited, merchant default setting is used.
    :type moss_country_code: str
    :param tax_region: Tax region key
    :type tax_region: str
    :param start_month: Period start month in yyyy-MM format. Either quarter or start-month and end-month have to be provided.
    :type start_month: str
    :param end_month: Period end month in yyyy-MM format. Either quarter or start-month and end-month have to be provided.
    :type end_month: str

    """
    return web.Response(status=200)
