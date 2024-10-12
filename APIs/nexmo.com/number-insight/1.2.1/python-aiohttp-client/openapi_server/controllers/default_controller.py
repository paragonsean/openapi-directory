from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_number_insight_advanced200_response import GetNumberInsightAdvanced200Response
from openapi_server.models.get_number_insight_async200_response import GetNumberInsightAsync200Response
from openapi_server.models.get_number_insight_standard200_response import GetNumberInsightStandard200Response
from openapi_server.models.ni_response_async import NiResponseAsync
from openapi_server.models.ni_response_json_basic import NiResponseJsonBasic
from openapi_server.models.ni_response_xml_advanced import NiResponseXmlAdvanced
from openapi_server.models.ni_response_xml_basic import NiResponseXmlBasic
from openapi_server.models.ni_response_xml_standard import NiResponseXmlStandard
from openapi_server import util


async def get_number_insight_advanced(request: web.Request, format, number, real_time_data=None, country=None, cnam=None, ip=None) -> web.Response:
    """Advanced Number Insight (sync)

    Provides [advanced number insight](/number-insight/overview#basic-standard-and-advanced-apis) information about a number synchronously, in the same way that the basic and standard endpoints do.  Vonage recommends accessing the Advanced API **asynchronously** using the &#x60;/advanced/async&#x60; endpoint, to avoid timeouts.  Note that this endpoint also supports &#x60;POST&#x60; requests. 

    :param format: The format of the response
    :type format: str
    :param number: A single phone number that you need insight about in national or international format.
    :type number: str
    :param real_time_data: A boolean to choose whether to get real time data back in the response.
    :type real_time_data: bool
    :param country: If a number does not have a country code or is uncertain, set the two-character country code. This code must be in ISO 3166-1 alpha-2 format and in upper case. For example, GB or US. If you set country and number is already in [E.164](https://en.wikipedia.org/wiki/E.164) format, country must match the country code in number.
    :type country: str
    :param cnam: Indicates if the name of the person who owns the phone number should be looked up and returned in the response. Set to true to receive phone number owner name in the response. This features is available for US numbers only and incurs an additional charge.
    :type cnam: bool
    :param ip: This parameter is deprecated as we are no longer able to retrieve reliable IP data globally from carriers. 
    :type ip: str

    """
    return web.Response(status=200)


async def get_number_insight_async(request: web.Request, format, param_callback, number, country=None, cnam=None, ip=None) -> web.Response:
    """Advanced Number Insight (async)

    Provides [advanced number insight](/number-insight/overview#basic-standard-and-advanced-apis) number information **asynchronously** using the URL specified in the &#x60;callback&#x60; parameter.  recommends asynchronous use of the Number Insight Advanced API, to avoid timeouts.  Note that this endpoint also supports &#x60;POST&#x60; requests. 

    :param format: The format of the response
    :type format: str
    :param param_callback: The callback URL
    :type param_callback: str
    :param number: A single phone number that you need insight about in national or international format.
    :type number: str
    :param country: If a number does not have a country code or is uncertain, set the two-character country code. This code must be in ISO 3166-1 alpha-2 format and in upper case. For example, GB or US. If you set country and number is already in [E.164](https://en.wikipedia.org/wiki/E.164) format, country must match the country code in number.
    :type country: str
    :param cnam: Indicates if the name of the person who owns the phone number should be looked up and returned in the response. Set to true to receive phone number owner name in the response. This features is available for US numbers only and incurs an additional charge.
    :type cnam: bool
    :param ip: This parameter is deprecated as we are no longer able to retrieve reliable IP data globally from carriers. 
    :type ip: str

    """
    return web.Response(status=200)


async def get_number_insight_basic(request: web.Request, format, number, country=None) -> web.Response:
    """Basic Number Insight

    Provides [basic number insight](/number-insight/overview#basic-standard-and-advanced-apis) information about a number.  Note that this endpoint also supports &#x60;POST&#x60; requests. 

    :param format: The format of the response
    :type format: str
    :param number: A single phone number that you need insight about in national or international format.
    :type number: str
    :param country: If a number does not have a country code or is uncertain, set the two-character country code. This code must be in ISO 3166-1 alpha-2 format and in upper case. For example, GB or US. If you set country and number is already in [E.164](https://en.wikipedia.org/wiki/E.164) format, country must match the country code in number.
    :type country: str

    """
    return web.Response(status=200)


async def get_number_insight_standard(request: web.Request, format, number, country=None, cnam=None) -> web.Response:
    """Standard Number Insight

    Provides [standard number insight](/number-insight/overview#basic-standard-and-advanced-apis) information about a number.  Note that this endpoint also supports &#x60;POST&#x60; requests. 

    :param format: The format of the response
    :type format: str
    :param number: A single phone number that you need insight about in national or international format.
    :type number: str
    :param country: If a number does not have a country code or is uncertain, set the two-character country code. This code must be in ISO 3166-1 alpha-2 format and in upper case. For example, GB or US. If you set country and number is already in [E.164](https://en.wikipedia.org/wiki/E.164) format, country must match the country code in number.
    :type country: str
    :param cnam: Indicates if the name of the person who owns the phone number should be looked up and returned in the response. Set to true to receive phone number owner name in the response. This features is available for US numbers only and incurs an additional charge.
    :type cnam: bool

    """
    return web.Response(status=200)
