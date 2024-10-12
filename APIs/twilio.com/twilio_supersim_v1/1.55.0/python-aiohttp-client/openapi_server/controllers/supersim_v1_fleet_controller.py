from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_fleet_response import ListFleetResponse
from openapi_server.models.supersim_v1_fleet import SupersimV1Fleet
from openapi_server import util


async def create_fleet(request: web.Request, network_access_profile, data_enabled=None, data_limit=None, ip_commands_method=None, ip_commands_url=None, sms_commands_enabled=None, sms_commands_method=None, sms_commands_url=None, unique_name=None) -> web.Response:
    """create_fleet

    Create a Fleet

    :param network_access_profile: The SID or unique name of the Network Access Profile that will control which cellular networks the Fleet&#39;s SIMs can connect to.
    :type network_access_profile: str
    :param data_enabled: Defines whether SIMs in the Fleet are capable of using 2G/3G/4G/LTE/CAT-M data connectivity. Defaults to &#x60;true&#x60;.
    :type data_enabled: bool
    :param data_limit: The total data usage (download and upload combined) in Megabytes that each Super SIM assigned to the Fleet can consume during a billing period (normally one month). Value must be between 1MB (1) and 2TB (2,000,000). Defaults to 1GB (1,000).
    :type data_limit: int
    :param ip_commands_method: A string representing the HTTP method to use when making a request to &#x60;ip_commands_url&#x60;. Can be one of &#x60;POST&#x60; or &#x60;GET&#x60;. Defaults to &#x60;POST&#x60;.
    :type ip_commands_method: str
    :param ip_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an IP Command from your device to a special IP address. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
    :type ip_commands_url: str
    :param sms_commands_enabled: Defines whether SIMs in the Fleet are capable of sending and receiving machine-to-machine SMS via Commands. Defaults to &#x60;true&#x60;.
    :type sms_commands_enabled: bool
    :param sms_commands_method: A string representing the HTTP method to use when making a request to &#x60;sms_commands_url&#x60;. Can be one of &#x60;POST&#x60; or &#x60;GET&#x60;. Defaults to &#x60;POST&#x60;.
    :type sms_commands_method: str
    :param sms_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an SMS from your device to the SMS Commands number. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
    :type sms_commands_url: str
    :param unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource.
    :type unique_name: str

    """
    return web.Response(status=200)


async def fetch_fleet(request: web.Request, sid) -> web.Response:
    """fetch_fleet

    Fetch a Fleet instance from your account.

    :param sid: The SID of the Fleet resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_fleet(request: web.Request, network_access_profile=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_fleet

    Retrieve a list of Fleets from your account.

    :param network_access_profile: The SID or unique name of the Network Access Profile that controls which cellular networks the Fleet&#39;s SIMs can connect to.
    :type network_access_profile: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_fleet(request: web.Request, sid, data_limit=None, ip_commands_method=None, ip_commands_url=None, network_access_profile=None, sms_commands_method=None, sms_commands_url=None, unique_name=None) -> web.Response:
    """update_fleet

    Updates the given properties of a Super SIM Fleet instance from your account.

    :param sid: The SID of the Fleet resource to update.
    :type sid: str
    :param data_limit: The total data usage (download and upload combined) in Megabytes that each Super SIM assigned to the Fleet can consume during a billing period (normally one month). Value must be between 1MB (1) and 2TB (2,000,000). Defaults to 1GB (1,000).
    :type data_limit: int
    :param ip_commands_method: A string representing the HTTP method to use when making a request to &#x60;ip_commands_url&#x60;. Can be one of &#x60;POST&#x60; or &#x60;GET&#x60;. Defaults to &#x60;POST&#x60;.
    :type ip_commands_method: str
    :param ip_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an IP Command from your device to a special IP address. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
    :type ip_commands_url: str
    :param network_access_profile: The SID or unique name of the Network Access Profile that will control which cellular networks the Fleet&#39;s SIMs can connect to.
    :type network_access_profile: str
    :param sms_commands_method: A string representing the HTTP method to use when making a request to &#x60;sms_commands_url&#x60;. Can be one of &#x60;POST&#x60; or &#x60;GET&#x60;. Defaults to &#x60;POST&#x60;.
    :type sms_commands_method: str
    :param sms_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an SMS from your device to the SMS Commands number. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
    :type sms_commands_url: str
    :param unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource.
    :type unique_name: str

    """
    return web.Response(status=200)
