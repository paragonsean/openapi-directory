from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_collection_output import ActivityCollectionOutput
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.token_output import TokenOutput
from openapi_server import util


async def query_token_activity_v1_token_activity_get(request: web.Request, page=None, page_size=None) -> web.Response:
    """Get the activity information of the token in the region.

    ### What Obtain the list of all the activity events of the current user in the selected region. The purpose of this function is to show what actions performed a user with the specific token.  ### Parameters The following pagination parameters are required as query string parameters: - &#x60;&#x60;page&#x60;&#x60;: (Optional) the page number to retrieve. The first page is 1. Default is 1. - &#x60;&#x60;page_size&#x60;&#x60;: (Optional) the number of items per page. Default is 20.  The token is obtained automatically from the &#x60;Bearer&#x60; in the header.  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to all activities of the token. - &#x60;&#x60;activities&#x60;&#x60;: a list of activities performed by the user with the token.     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual activity information.     - &#x60;&#x60;event&#x60;&#x60;: ID of the reference of the event type.     - &#x60;&#x60;description&#x60;&#x60;: Human readable description of the event.     - &#x60;&#x60;data&#x60;&#x60;: the payload of the event. It can be empty.     - &#x60;&#x60;source&#x60;&#x60;: A JSON object with the following fields:         - &#x60;&#x60;address&#x60;&#x60;: the IP address of the client.         - &#x60;&#x60;ua_string&#x60;&#x60;: the user agent string of the client.         - &#x60;&#x60;status_code&#x60;&#x60;: the HTTP status code of the response.         - &#x60;&#x60;uri&#x60;&#x60;: the URI of the request.         - &#x60;&#x60;body&#x60;&#x60;: the body of the request.         - &#x60;&#x60;method&#x60;&#x60;: the HTTP method of the request.     - &#x60;&#x60;created_at&#x60;&#x60;: the date and time when the token was created in UNIX timestamp in milliseconds.  ### Errors It will return the API Global errors described in the API description.

    :param page: The page to be returned
    :type page: int
    :param page_size: The number of items per page
    :type page_size: int

    """
    return web.Response(status=200)


async def query_token_info_v1_token_get(request: web.Request, ) -> web.Response:
    """Get the information of the user&#39;s token in the region.

    ### What Obtain the list of all the token attributes of the current user in the selected region. The purpose of this function is to show the current values of the user&#39;s quota.  ### Parameters No parameters are required. The token is obtained automatically from the &#x60;Bearer&#x60; in the header.  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual token information. - &#x60;&#x60;region_id&#x60;&#x60;: the name of the region where the token is valid. - &#x60;&#x60;last_month_bucket_init_value&#x60;&#x60;: the initial value of the monthly bucket. - &#x60;&#x60;last_month_bucket_value&#x60;&#x60;: the current value of consumed quota in the monthly bucket. - &#x60;&#x60;last_month_bucket_refresh&#x60;&#x60;: Unix timestamp in milliseconds of the next monthly bucket reset. - &#x60;&#x60;last_minute_bucket_init_value&#x60;&#x60;: the initial value of the per minute bucket. - &#x60;&#x60;last_minute_bucket_value&#x60;&#x60;: the current value of consumed quota in the per minute bucket. - &#x60;&#x60;last_minute_bucket_refresh&#x60;&#x60;: Unix timestamp in milliseconds of the next per minute bucket reset. - &#x60;&#x60;last_minute_bucket_refill_ratio&#x60;&#x60;: the number of tokens to add every second to the per minute bucket. - &#x60;&#x60;status&#x60;&#x60;: the status of the token. The only allowed value is &#x60;&#x60;ENABLED&#x60;&#x60;. - &#x60;&#x60;created_at&#x60;&#x60;: the date and time when the token was created in UNIX timestamp in milliseconds. - &#x60;&#x60;updated_at&#x60;&#x60;: the date and time when the token was last updated in UNIX timestamp in milliseconds.  ### Errors It will return the API Global errors described in the API description.


    """
    return web.Response(status=200)
