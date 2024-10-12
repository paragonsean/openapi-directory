from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_rate_plan_response import ListRatePlanResponse
from openapi_server.models.wireless_v1_rate_plan import WirelessV1RatePlan
from openapi_server import util


async def create_rate_plan(request: web.Request, data_enabled=None, data_limit=None, data_metering=None, friendly_name=None, international_roaming=None, international_roaming_data_limit=None, messaging_enabled=None, national_roaming_data_limit=None, national_roaming_enabled=None, unique_name=None, voice_enabled=None) -> web.Response:
    """create_rate_plan

    

    :param data_enabled: Whether SIMs can use GPRS/3G/4G/LTE data connectivity.
    :type data_enabled: bool
    :param data_limit: The total data usage (download and upload combined) in Megabytes that the Network allows during one month on the home network (T-Mobile USA). The metering period begins the day of activation and ends on the same day in the following month. Can be up to 2TB and the default value is &#x60;1000&#x60;.
    :type data_limit: int
    :param data_metering: The model used to meter data usage. Can be: &#x60;payg&#x60; and &#x60;quota-1&#x60;, &#x60;quota-10&#x60;, and &#x60;quota-50&#x60;. Learn more about the available [data metering models](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource#payg-vs-quota-data-plans).
    :type data_metering: str
    :param friendly_name: A descriptive string that you create to describe the resource. It does not have to be unique.
    :type friendly_name: str
    :param international_roaming: The list of services that SIMs capable of using GPRS/3G/4G/LTE data connectivity can use outside of the United States. Can contain: &#x60;data&#x60; and &#x60;messaging&#x60;.
    :type international_roaming: List[str]
    :param international_roaming_data_limit: The total data usage (download and upload combined) in Megabytes that the Network allows during one month when roaming outside the United States. Can be up to 2TB.
    :type international_roaming_data_limit: int
    :param messaging_enabled: Whether SIMs can make, send, and receive SMS using [Commands](https://www.twilio.com/docs/iot/wireless/api/command-resource).
    :type messaging_enabled: bool
    :param national_roaming_data_limit: The total data usage (download and upload combined) in Megabytes that the Network allows during one month on non-home networks in the United States. The metering period begins the day of activation and ends on the same day in the following month. Can be up to 2TB. See [national roaming](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource#national-roaming) for more info.
    :type national_roaming_data_limit: int
    :param national_roaming_enabled: Whether SIMs can roam on networks other than the home network (T-Mobile USA) in the United States. See [national roaming](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource#national-roaming).
    :type national_roaming_enabled: bool
    :param unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource.
    :type unique_name: str
    :param voice_enabled: Deprecated.
    :type voice_enabled: bool

    """
    return web.Response(status=200)


async def delete_rate_plan(request: web.Request, sid) -> web.Response:
    """delete_rate_plan

    

    :param sid: The SID of the RatePlan resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_rate_plan(request: web.Request, sid) -> web.Response:
    """fetch_rate_plan

    

    :param sid: The SID of the RatePlan resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_rate_plan(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_rate_plan

    

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_rate_plan(request: web.Request, sid, friendly_name=None, unique_name=None) -> web.Response:
    """update_rate_plan

    

    :param sid: The SID of the RatePlan resource to update.
    :type sid: str
    :param friendly_name: A descriptive string that you create to describe the resource. It does not have to be unique.
    :type friendly_name: str
    :param unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource.
    :type unique_name: str

    """
    return web.Response(status=200)
