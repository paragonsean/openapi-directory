from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_domestic_summary_report_out import GetDomesticSummaryReportOut
from openapi_server.models.get_eu_vies_report_out import GetEuViesReportOut
from openapi_server import util


async def get_domestic_summary_report(request: web.Request, country_code, start_month, end_month, format=None, currency_code=None, fx_date_type=None) -> web.Response:
    """Calculate domestic summary

    

    :param country_code: ISO 2-letter country code which will be used for determining which country is domestic.
    :type country_code: str
    :param start_month: Period start month in yyyy-MM format.
    :type start_month: str
    :param end_month: Period end month in yyyy-MM format.
    :type end_month: str
    :param format: Output format. &#39;xml&#39; and &#39;csv&#39; values are accepted. Default format - json
    :type format: str
    :param currency_code: ISO 3-letter currency code, e.g. EUR or USD. Defaults to the one assigned to MOSS calculations for a given country code.
    :type currency_code: str
    :param fx_date_type: Which date should be used for FX.
    :type fx_date_type: str

    """
    return web.Response(status=200)


async def get_eu_vies_report(request: web.Request, end_month, start_month, eu_country_code, period_length=None, lff_sequence_number=None, transformation=None, currency_code=None, tax_id=None, fx_date_type=None, format=None) -> web.Response:
    """Calculate EU VIES report

    

    :param end_month: Period end month in yyyy-MM format.
    :type end_month: str
    :param start_month: Period start month in yyyy-MM format.
    :type start_month: str
    :param eu_country_code: ISO 2-letter country code which will be used for determining which country is domestic.
    :type eu_country_code: str
    :param period_length: Length of report period. &#39;month&#39;, &#39;quarter&#39; and &#39;year&#39; values are accepted. Required only if Large Filer Format is requested.
    :type period_length: str
    :param lff_sequence_number: Sequence number used to generate report in Large Filer Format. If not specified then &#39;0000000001&#39; will be used.
    :type lff_sequence_number: str
    :param transformation: Which transformation should be applied. Please note that transformation will be applied only for xml and csv formats.
    :type transformation: str
    :param currency_code: ISO 3-letter currency code, e.g. EUR or USD. Defaults to the one assigned to MOSS calculations for a given country code.
    :type currency_code: str
    :param tax_id: MOSS-assigned tax ID - if not provided, merchant&#39;s national tax number will be used.
    :type tax_id: str
    :param fx_date_type: Which date should be used for FX.
    :type fx_date_type: str
    :param format: Output format. &#39;xml&#39;, &#39;csv&#39; and &#39;lff&#39; (only for Ireland) values are accepted as well
    :type format: str

    """
    return web.Response(status=200)
