from typing import List, Dict
from aiohttp import web

from openapi_server.models.lookups_v1_phone_number import LookupsV1PhoneNumber
from openapi_server import util


async def fetch_phone_number(request: web.Request, phone_number, country_code=None, type=None, add_ons=None, add_ons_data=None) -> web.Response:
    """fetch_phone_number

    

    :param phone_number: The phone number to lookup in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
    :type phone_number: str
    :param country_code: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the phone number to fetch. This is used to specify the country when the phone number is provided in a national format.
    :type country_code: str
    :param type: The type of information to return. Can be: &#x60;carrier&#x60; or &#x60;caller-name&#x60;. The default is null.  Carrier information costs $0.005 per phone number looked up.  Caller Name information is currently available only in the US and costs $0.01 per phone number looked up.  To retrieve both types on information, specify this parameter twice; once with &#x60;carrier&#x60; and once with &#x60;caller-name&#x60; as the value.
    :type type: List[str]
    :param add_ons: The &#x60;unique_name&#x60; of an Add-on you would like to invoke. Can be the &#x60;unique_name&#x60; of an Add-on that is installed on your account. You can specify multiple instances of this parameter to invoke multiple Add-ons. For more information about  Add-ons, see the [Add-ons documentation](https://www.twilio.com/docs/add-ons).
    :type add_ons: List[str]
    :param add_ons_data: Data specific to the add-on you would like to invoke. The content and format of this value depends on the add-on.
    :type add_ons_data: dict | bytes

    """
    add_ons_data = .from_dict(add_ons_data)
    return web.Response(status=200)
