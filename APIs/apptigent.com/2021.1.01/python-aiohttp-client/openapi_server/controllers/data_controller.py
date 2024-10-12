from typing import List, Dict
from aiohttp import web

from openapi_server.models.input_csv_conversion_json import InputCsvConversionJSON
from openapi_server.models.input_data_query import InputDataQuery
from openapi_server.models.input_json_conversion_csv import InputJsonConversionCSV
from openapi_server.models.input_json_conversion_html import InputJsonConversionHTML
from openapi_server.models.input_json_conversion_xml import InputJsonConversionXML
from openapi_server.models.input_xml_conversion_json import InputXmlConversionJSON
from openapi_server.models.output_string import OutputString
from openapi_server import util


async def csv_to_json(request: web.Request, csv_conversion_json=None) -> web.Response:
    """Data - CSV to JSON

    Convert a CSV string to a JSON array

    :param csv_conversion_json: 
    :type csv_conversion_json: dict | bytes

    """
    csv_conversion_json = InputCsvConversionJSON.from_dict(csv_conversion_json)
    return web.Response(status=200)


async def json_to_csv(request: web.Request, json_conversion_csv=None) -> web.Response:
    """Data - JSON to CSV

    Convert a JSON array to CSV string

    :param json_conversion_csv: 
    :type json_conversion_csv: dict | bytes

    """
    json_conversion_csv = InputJsonConversionCSV.from_dict(json_conversion_csv)
    return web.Response(status=200)


async def json_to_html(request: web.Request, json_conversion_html=None) -> web.Response:
    """Data - JSON to HTML Table

    Convert a JSON array to an HTML table

    :param json_conversion_html: 
    :type json_conversion_html: dict | bytes

    """
    json_conversion_html = InputJsonConversionHTML.from_dict(json_conversion_html)
    return web.Response(status=200)


async def json_to_xml(request: web.Request, json_conversion_xml=None) -> web.Response:
    """Data - JSON to XML

    Convert a JSON object to an XML string

    :param json_conversion_xml: 
    :type json_conversion_xml: dict | bytes

    """
    json_conversion_xml = InputJsonConversionXML.from_dict(json_conversion_xml)
    return web.Response(status=200)


async def query_json(request: web.Request, input_data_query=None) -> web.Response:
    """Data - Query JSON

    Query a JSON object using a JSONPath expression

    :param input_data_query: 
    :type input_data_query: dict | bytes

    """
    input_data_query = InputDataQuery.from_dict(input_data_query)
    return web.Response(status=200)


async def query_xml(request: web.Request, input_data_query=None) -> web.Response:
    """Data - Query XML

    Query an XML string using an XPath expression

    :param input_data_query: 
    :type input_data_query: dict | bytes

    """
    input_data_query = InputDataQuery.from_dict(input_data_query)
    return web.Response(status=200)


async def xml_to_json(request: web.Request, xml_conversion_json=None) -> web.Response:
    """Data - XML to JSON

    Convert an XML string to a JSON object

    :param xml_conversion_json: 
    :type xml_conversion_json: dict | bytes

    """
    xml_conversion_json = InputXmlConversionJSON.from_dict(xml_conversion_json)
    return web.Response(status=200)
