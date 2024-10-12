from typing import List, Dict
from aiohttp import web

from openapi_server.models.body_query_origin_status_v1_origin_status_post import BodyQueryOriginStatusV1OriginStatusPost
from openapi_server.models.body_update_configuration_origin_v1_origin_put import BodyUpdateConfigurationOriginV1OriginPut
from openapi_server.models.body_update_origin_status_v1_origin_status_put import BodyUpdateOriginStatusV1OriginStatusPut
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.origin_address_status_collection_output import OriginAddressStatusCollectionOutput
from openapi_server.models.origin_client_analysis_collection_output import OriginClientAnalysisCollectionOutput
from openapi_server.models.origin_collection_output import OriginCollectionOutput
from openapi_server.models.origin_cookie_id_status_collection_output import OriginCookieIdStatusCollectionOutput
from openapi_server.models.origin_output import OriginOutput
from openapi_server.models.origin_scripts_output import OriginScriptsOutput
from openapi_server.models.origin_status_details_collection_output import OriginStatusDetailsCollectionOutput
from openapi_server.models.origin_status_details_output import OriginStatusDetailsOutput
from openapi_server.models.origin_status_output import OriginStatusOutput
from openapi_server.models.origin_traffic_analysis_collection_output import OriginTrafficAnalysisCollectionOutput
from openapi_server import util


async def query_all_origin_information_v1_origin_all_get(request: web.Request, ) -> web.Response:
    """Get the information of the origins of the user in the region.

    ### What Obtain the attributes of all the origins of the user in the selected region. The purpose of this function is to display the information of configuration of the origins and also access to the live data of the origins.  The origin is a combination of protocol and domain (Ex: https://example.com) and the origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters No parameters are required.  ### Result The result is a list of JSON objects with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to the request to obtain all the origins of the user. - &#x60;&#x60;origins&#x60;&#x60;: A list of JSON objects with the following fields:     - &#x60;&#x60;self&#x60;&#x60;: the URI to the request to obtain the full details of an origin.     - &#x60;&#x60;origin&#x60;&#x60;: the protocol and the domain where the origin token is valid.     - &#x60;&#x60;status&#x60;&#x60;: the status of the origin token. The only allowed values are &#x60;&#x60;ENABLED&#x60;&#x60; and &#x60;&#x60;DISABLED&#x60;&#x60;.     - &#x60;&#x60;token&#x60;&#x60;: the URI to the request to obtain the token of the origin.     - &#x60;&#x60;data&#x60;&#x60;: a JSON object containing all the parameters of the origin as key-value pairs.     - &#x60;&#x60;logs&#x60;&#x60;: the URI to the request to obtain the log activity in the origin.     - &#x60;&#x60;addresses&#x60;&#x60;: the URI to the request to obtain the list of IP addresses active in the origin.     - &#x60;&#x60;cookies&#x60;&#x60;: the URI to the request to obtain the list of cookies active in the origin.     - &#x60;&#x60;created_at&#x60;&#x60;: the date and time when the origin token was created in UNIX timestamp in milliseconds.     - &#x60;&#x60;updated_at&#x60;&#x60;: the date and time when the origin token was last updated in UNIX timestamp in milliseconds.  ### Errors It will return the API Global errors described in the API description.


    """
    return web.Response(status=200)


async def query_origin_address_status_information_v1_origin_addresses_get(request: web.Request, query, page=None, page_size=None) -> web.Response:
    """Get the address status of the origin of the user in the region.

    ### What  Obtain the status that trigger the change in the status of the origin of a specific IP address. The status will also describe the current state of the status and the information that triggered the change.  The origin is a combination of protocol and domain (Ex: https://example.com) and the origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters In the querystring of the request, add the origin of the user to the &#x60;query&#x60; parameter with the following format:1. Protocol: Can be &#x60;&#x60;http&#x60;&#x60; or &#x60;&#x60;https&#x60;&#x60;. 2. Domain: The domain of the origin.  Then, the origin must be urlencoded. Example: &#x60;&#x60;&#x60; https://example.com &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60; https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  The querystring must be like this: &#x60;&#x60;&#x60; ?query&#x3D;https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to the request to obtain the full details of the status of an origin. - &#x60;&#x60;addresses&#x60;&#x60;: a list of JSON objects with the following fields:     - &#x60;&#x60;address&#x60;&#x60;: the IP address of the origin.     - &#x60;&#x60;status&#x60;&#x60;: the status of IP address for the given origin.     - &#x60;&#x60;log_id&#x60;&#x60;: the ID of the log that triggered the change in the status of the origin.     - &#x60;&#x60;expiry&#x60;&#x60;: the date and time when the origin status will expire in UNIX timestamp in milliseconds.     - &#x60;&#x60;created_at&#x60;&#x60;: the date and time when the origin status was created in UNIX timestamp in milliseconds.     - &#x60;&#x60;updated_at&#x60;&#x60;: the date and time when the origin status was last updated in UNIX timestamp in milliseconds.  ### Errors - a &#x60;404 Not Found&#x60; error if the origin is not found. - a &#x60;400 Bad Request&#x60; error if the origin does not have the correct format.  It will return the API Global errors described in the API description.

    :param query: The origin site to query
    :type query: str
    :param page: The page to be returned
    :type page: int
    :param page_size: The number of items per page
    :type page_size: int

    """
    return web.Response(status=200)


async def query_origin_cookie_id_status_information_v1_origin_cookies_get(request: web.Request, query, page=None, page_size=None) -> web.Response:
    """Get the tracking cookie ID status of the origin of the user in the region.

    ### What  Obtain the status that trigger the change in the status of the origin of the cookie ID used to track the users. The status will also describe the current state of the status and the information that triggered the change.  The origin is a combination of protocol and domain (Ex: https://example.com) and the origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters In the querystring of the request, add the origin of the user to the &#x60;query&#x60; parameter with the following format:1. Protocol: Can be &#x60;&#x60;http&#x60;&#x60; or &#x60;&#x60;https&#x60;&#x60;. 2. Domain: The domain of the origin.  Then, the origin must be urlencoded. Example: &#x60;&#x60;&#x60; https://example.com &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60; https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  The querystring must be like this: &#x60;&#x60;&#x60; ?query&#x3D;https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to the request to obtain the full details of the status of an origin. - &#x60;&#x60;addresses&#x60;&#x60;: a list of JSON objects with the following fields:     - &#x60;&#x60;cookie_id&#x60;&#x60;: the ID of the tracking cookie for the origin.     - &#x60;&#x60;status&#x60;&#x60;: the status of tracking cookie ID for the given origin.     - &#x60;&#x60;log_id&#x60;&#x60;: the ID of the log that triggered the change in the status of the origin.     - &#x60;&#x60;expiry&#x60;&#x60;: the date and time when the origin status will expire in UNIX timestamp in milliseconds.     - &#x60;&#x60;created_at&#x60;&#x60;: the date and time when the origin status was created in UNIX timestamp in milliseconds.     - &#x60;&#x60;updated_at&#x60;&#x60;: the date and time when the origin status was last updated in UNIX timestamp in milliseconds.  ### Errors - a &#x60;404 Not Found&#x60; error if the origin is not found. - a &#x60;400 Bad Request&#x60; error if the origin does not have the correct format.  It will return the API Global errors described in the API description.

    :param query: The origin site to query
    :type query: str
    :param page: The page to be returned
    :type page: int
    :param page_size: The number of items per page
    :type page_size: int

    """
    return web.Response(status=200)


async def query_origin_information_v1_origin_get(request: web.Request, query) -> web.Response:
    """Get the information of an origin of the user in the region.

    ### What Obtain the attributes of the origin of the user passed as argument in the selected region. The purpose of this function is to display the information of configuration of the origin and also access to the live data of the origin.  The origin is a combination of protocol and domain (Ex: https://example.com) and the origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters In the querystring of the request, add the origin of the user to the &#x60;query&#x60; parameter with the following format:1. Protocol: Can be &#x60;&#x60;http&#x60;&#x60; or &#x60;&#x60;https&#x60;&#x60;. 2. Domain: The domain of the origin.  Then, the origin must be urlencoded. Example: &#x60;&#x60;&#x60; https://example.com &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60; https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  The querystring must be like this: &#x60;&#x60;&#x60; ?query&#x3D;https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to the request to obtain the full details of an origin. - &#x60;&#x60;origin&#x60;&#x60;: the protocol and the domain where the origin token is valid. - &#x60;&#x60;status&#x60;&#x60;: the status of the origin token. The only allowed values are &#x60;&#x60;ENABLED&#x60;&#x60; and &#x60;&#x60;DISABLED&#x60;&#x60;. - &#x60;&#x60;token&#x60;&#x60;: the URI to the request to obtain the token of the origin. - &#x60;&#x60;data&#x60;&#x60;: a JSON object containing all the parameters of the origin as key-value pairs. - &#x60;&#x60;logs&#x60;&#x60;: the URI to the request to obtain the log activity in the origin. - &#x60;&#x60;addresses&#x60;&#x60;: the URI to the request to obtain the list of IP addresses active in the origin. - &#x60;&#x60;cookies&#x60;&#x60;: the URI to the request to obtain the list of cookies active in the origin. - &#x60;&#x60;created_at&#x60;&#x60;: the date and time when the origin token was created in UNIX timestamp in milliseconds. - &#x60;&#x60;updated_at&#x60;&#x60;: the date and time when the origin token was last updated in UNIX timestamp in milliseconds.  ### Errors - a &#x60;404 Not Found&#x60; error if the origin token is not found. - a &#x60;400 Bad Request&#x60; error if the origin does not have the correct format.  It will return the API Global errors described in the API description.

    :param query: The origin site to query
    :type query: str

    """
    return web.Response(status=200)


async def query_origin_scripts_v1_origin_scripts_get(request: web.Request, query) -> web.Response:
    """Get the code snippets of an origin of the user in the region.

    ### What Obtain the code snippets of the origin of the user passed as argument in the selected region. The purpose of this function is to help the user to integrate the javascript library in their website with a preconfigured script that contains the origin token.  ### Parameters In the querystring of the request, add the origin of the user to the &#x60;query&#x60; parameter with the following format:1. Protocol: Can be &#x60;&#x60;http&#x60;&#x60; or &#x60;&#x60;https&#x60;&#x60;. 2. Domain: The domain of the origin.  Then, the origin must be urlencoded. Example: &#x60;&#x60;&#x60; https://example.com &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60; https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  The querystring must be like this: &#x60;&#x60;&#x60; ?query&#x3D;https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to the request to obtain the full details of an origin. - &#x60;&#x60;detection&#x60;&#x60;: code snippet to integrate into the website described in the origin to detect malicious activity.  ### Errors - a &#x60;404 Not Found&#x60; error if the origin token is not found. - a &#x60;400 Bad Request&#x60; error if the origin does not have the correct format.  It will return the API Global errors described in the API description.

    :param query: The origin site to query
    :type query: str

    """
    return web.Response(status=200)


async def query_origin_status_detail_v1_origin_status_detail_status_id_get(request: web.Request, status_id) -> web.Response:
    """Get detail of a status available in the platform.

    ### What Obtain the description of a status available in the platform.  ### Parameters A &#x60;status_id&#x60; parameter in the path of the request: - &#x60;PASS&#x60; - &#x60;BLOCK&#x60; - &#x60;CHALLENGE&#x60; - &#x60;BYPASS&#x60; - &#x60;IGNORE&#x60;  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to the status detail. - &#x60;&#x60;description&#x60;&#x60;: a human readable description of the status. - &#x60;&#x60;cardinality&#x60;&#x60;: The number describing the cardinality of the status.  ### Errors - a &#x60;400 Bad Request&#x60; error if the origin status is not any of the available ones.  It will return the API Global errors described in the API description.

    :param status_id: The status id to query the details
    :type status_id: str

    """
    return web.Response(status=200)


async def query_origin_status_details_v1_origin_status_details_get(request: web.Request, ) -> web.Response:
    """Get the list of different status available in the platform.

    ### What Obtain the full list and description of the different status available in the platform.  ### Parameters No parameters needed.  ### Result The result is a JSON list with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to the request to obtain the list. - &#x60;&#x60;list&#x60;&#x60;: a JSON list with the following elements each one with the following fields:     - &#x60;&#x60;self&#x60;&#x60;: the URI to the status detail.     - &#x60;&#x60;description&#x60;&#x60;: a human readable description of the status.     - &#x60;&#x60;cardinality&#x60;&#x60;: The number describing the cardinality of the status.  ### Errors It will return the API Global errors described in the API description.


    """
    return web.Response(status=200)


async def query_origin_status_v1_origin_status_post(request: web.Request, query, body=None) -> web.Response:
    """Get the current cookie ID and IP address status of the origin of user in the region.

    ### What  Obtain the current status of the origin for a given IP address and/or cookie ID. The values can be correlated, but they are not required to be. The status will also describe the following information: - &#x60;PASS&#x60;: The traffic should not be intercepted, but should be analyzed and a positive detection should trigger a change in the status. - &#x60;BLOCK&#x60;: The traffic must be intercepted and redirected to a blocking page. Only a timeout of the IP address or Cookie ID, a solved challenge or a manual status change can change the status. - &#x60;CHALLENGE&#x60;: The traffic must be intercepted and redirected to a page where the user must solve a challenge. If the challenge is succesfully solved the status will change to &#x60;PASS&#x60;. If the user fails to change the challenge a specific amount of times, the status can change to &#x60;BLOCK&#x60;. - &#x60;BYPASS&#x60;: The traffic should not be tapped even if it is suspected to be malicious, as long as the timeout has not expired. When the timeout is reached, it should revert to a previous state instead of going to &#x60;PASS&#x60;. - &#x60;IGNORE&#x60;: Whatever happens to the traffic of the user, it should not be tapped. Once the time expires, it should return to the state PASS.  The origin is a combination of protocol and domain (Ex: https://example.com) and the origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters In the querystring of the request, add the origin of the user to the &#x60;query&#x60; parameter with the following format:1. Protocol: Can be &#x60;&#x60;http&#x60;&#x60; or &#x60;&#x60;https&#x60;&#x60;. 2. Domain: The domain of the origin.  Then, the origin must be urlencoded. Example: &#x60;&#x60;&#x60; https://example.com &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60; https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  The querystring must be like this: &#x60;&#x60;&#x60; ?query&#x3D;https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  The body should have at least one of the following fields: - &#x60;address&#x60;: The IP address of the user to query. - &#x60;cookie_id&#x60;: The ID of the tracking cookie of the user to query.  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to the request to obtain the full details of the &#x60;cookie_id&#x60; and &#x60;address&#x60; status of an origin. - &#x60;&#x60;cookie_id&#x60;&#x60;: a JSON object with the following fields:     - &#x60;&#x60;cookie_id&#x60;&#x60;: the ID of the tracking cookie for the origin.     - &#x60;&#x60;status&#x60;&#x60;: the URI to the status detail of the cookie ID.     - &#x60;&#x60;log_id&#x60;&#x60;: (Optional) the ID of the log that triggered the change in the status of the origin.     - &#x60;&#x60;expiry&#x60;&#x60;: (Optional) the date and time when the origin status will expire in UNIX timestamp in milliseconds.     - &#x60;&#x60;created_at&#x60;&#x60;: (Optional) the date and time when the origin status was created in UNIX timestamp in milliseconds.     - &#x60;&#x60;updated_at&#x60;&#x60;: (Optional) the date and time when the origin status was last updated in UNIX timestamp in milliseconds. - &#x60;&#x60;address&#x60;&#x60;: a JSON object with the following fields:     - &#x60;&#x60;address&#x60;&#x60;: the address for the origin.     - &#x60;&#x60;status&#x60;&#x60;: the URI to the status detail of the cookie ID.     - &#x60;&#x60;log_id&#x60;&#x60;: (Optional) the ID of the log that triggered the change in the status of the origin.     - &#x60;&#x60;expiry&#x60;&#x60;: (Optional) the date and time when the origin status will expire in UNIX timestamp in milliseconds.     - &#x60;&#x60;created_at&#x60;&#x60;: (Optional) the date and time when the origin status was created in UNIX timestamp in milliseconds.     - &#x60;&#x60;updated_at&#x60;&#x60;: (Optional) the date and time when the origin status was last updated in UNIX timestamp in milliseconds.  ### Errors - a &#x60;404 Not Found&#x60; error if the origin is not found. - a &#x60;400 Bad Request&#x60; error if the origin does not have the correct format.  It will return the API Global errors described in the API description.

    :param query: The origin site to query
    :type query: str
    :param body: 
    :type body: dict | bytes

    """
    body = BodyQueryOriginStatusV1OriginStatusPost.from_dict(body)
    return web.Response(status=200)


async def query_origin_traffic_analysis_v1_origin_traffic_analysis_get(request: web.Request, query, interval, from_timestamp, to_timestamp=None) -> web.Response:
    """Get the traffic analysis of the origin.

    ### What Obtain the traffic analysis of the origin in the specified time range and interval. Theanalysis will return the number of requests and the anomalies detected like:  - number of requests - overall score - malicious synthetic traffic (bad bot traffic) - IP in a denylist - IP in a datacenter - user uses a headless webdriver - Autonomous System (ASN) of the IP is risky - The location of the IP address and the ASN is different  The origin is a combination of protocol and domain (Ex: https://example.com) and the origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters In the querystring of the request, add the origin of the user to the &#x60;query&#x60; parameter with the following format:1. Protocol: Can be &#x60;&#x60;http&#x60;&#x60; or &#x60;&#x60;https&#x60;&#x60;. 2. Domain: The domain of the origin.  Then, the origin must be urlencoded. Example: &#x60;&#x60;&#x60; https://example.com &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60; https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  The querystring must be like this: &#x60;&#x60;&#x60; ?query&#x3D;https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  To restrict the analysis to a specific time range, add the following parameters to the querystring: - &#x60;&#x60;from_timestamp&#x60;&#x60;: the start date and time of the analysis in UNIX timestamp in milliseconds. - &#x60;&#x60;to_timestamp&#x60;&#x60;: (Optional) the end date and time of the analysis in UNIX timestamp in milliseconds. - &#x60;&#x60;interval&#x60;&#x60;: (Optional) the interval of the analysis in minutes. The default value is 60 minutes (HOURLY). Possible values are: &#x60;&#x60;HOURLY&#x60;&#x60;.  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to the request to obtain the traffic analysis for the origin. - &#x60;&#x60;from_timestamp&#x60;&#x60;: the start date and time of the analysis in UNIX timestamp in milliseconds. - &#x60;&#x60;to_timestamp&#x60;&#x60;: the end date and time of the analysis in UNIX timestamp in milliseconds. - &#x60;&#x60;interval&#x60;&#x60;: the interval of the analysis. Possible values are: &#x60;&#x60;HOURLY&#x60;&#x60;. - &#x60;&#x60;data&#x60;&#x60;: a JSON list with the following elements each one with the following fields:     - &#x60;&#x60;timestamp&#x60;&#x60;: the date and time of the analysis in UNIX timestamp in milliseconds.     - &#x60;&#x60;total&#x60;&#x60;: the total number of requests.     - &#x60;&#x60;score_high&#x60;&#x60;: the number of requests with a high score (bad traffic).     - &#x60;&#x60;bots&#x60;&#x60;: the number of requests from bad bots.     - &#x60;&#x60;denylists&#x60;&#x60;: the number of requests from IPs in a denylist.     - &#x60;&#x60;datacenters&#x60;&#x60;: the number of requests from IPs in a datacenter.     - &#x60;&#x60;webdrivers&#x60;&#x60;: the number of requests from IPs using a headless webdriver.     - &#x60;&#x60;asn_risky&#x60;&#x60;: the number of requests from IPs with a risky ASN.     - &#x60;&#x60;network_country_mismatches&#x60;&#x60;: the number of requests from IPs with a different location than the ASN.  ### Errors - a &#x60;404 Not Found&#x60; error if the origin token is not found. - a &#x60;400 Bad Request&#x60; error if the origin does not have the correct format.  It will return the API Global errors described in the API description.

    :param query: The origin site to query
    :type query: str
    :param interval: The data inteval to aggregate the result dataset
    :type interval: str
    :param from_timestamp: A UNIX timestamp in milliseconds to restrict the results of the query to entries logged after or equal to this value.
    :type from_timestamp: int
    :param to_timestamp: A UNIX timestamp in milliseconds to restrict the results of the query to entries logged before this value.
    :type to_timestamp: int

    """
    return web.Response(status=200)


async def query_origin_traffic_client_v1_origin_client_analysis_get(request: web.Request, query, interval, from_timestamp, to_timestamp=None) -> web.Response:
    """Get the type of clients of the trafffic of the origin.

    ### What Obtain the type of clients of trhe traffic in the specified time range and interval. Thequery will return the number of requests and the different type of CLIENTs and CRAWLERs.  The origin is a combination of protocol and domain (Ex: https://example.com) and the origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters In the querystring of the request, add the origin of the user to the &#x60;query&#x60; parameter with the following format:1. Protocol: Can be &#x60;&#x60;http&#x60;&#x60; or &#x60;&#x60;https&#x60;&#x60;. 2. Domain: The domain of the origin.  Then, the origin must be urlencoded. Example: &#x60;&#x60;&#x60; https://example.com &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60; https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  The querystring must be like this: &#x60;&#x60;&#x60; ?query&#x3D;https%3A%2F%2Fexample.com &#x60;&#x60;&#x60;  To restrict the query to a specific time range, add the following parameters to the querystring: - &#x60;&#x60;from_timestamp&#x60;&#x60;: the start date and time of the analysis in UNIX timestamp in milliseconds. - &#x60;&#x60;to_timestamp&#x60;&#x60;: (Optional) the end date and time of the analysis in UNIX timestamp in milliseconds. - &#x60;&#x60;interval&#x60;&#x60;: (Optional) the interval of the analysis in minutes. The default value is 60 minutes (HOURLY). Possible values are: &#x60;&#x60;HOURLY&#x60;&#x60;.  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to the request to obtain the traffic client analysis for the origin. - &#x60;&#x60;from_timestamp&#x60;&#x60;: the start date and time of the analysis in UNIX timestamp in milliseconds. - &#x60;&#x60;to_timestamp&#x60;&#x60;: the end date and time of the analysis in UNIX timestamp in milliseconds. - &#x60;&#x60;interval&#x60;&#x60;: the interval of the analysis. Possible values are: &#x60;&#x60;HOURLY&#x60;&#x60;. - &#x60;&#x60;data&#x60;&#x60;: a JSON list with the following elements each one with the following fields:     - &#x60;&#x60;timestamp&#x60;&#x60;: the date and time of the analysis in UNIX timestamp in milliseconds.     - &#x60;&#x60;total&#x60;&#x60;: the total number of requests.     - &#x60;&#x60;client_*&#x60;&#x60;: the number of requests from a specific client. The possible clients are: &#x60;&#x60;browser&#x60;&#x60;, &#x60;&#x60;crawler&#x60;&#x60;, &#x60;&#x60;email&#x60;&#x60;, &#x60;&#x60;library&#x60;&#x60;, &#x60;&#x60;mobile_browser&#x60;&#x60;, &#x60;&#x60;multimedia_player&#x60;&#x60;, &#x60;&#x60;offline_browser&#x60;&#x60;, &#x60;&#x60;unrecognized&#x60;&#x60;, &#x60;&#x60;ua_anonymizer&#x60;&#x60;, &#x60;&#x60;validator&#x60;&#x60;, &#x60;&#x60;wap_browser&#x60;&#x60;.     - &#x60;&#x60;crawler_*&#x60;&#x60;: the number of requests from a specific crawler. The possible crawlers are:&#x60;&#x60;feed_fetcher&#x60;&#x60;, &#x60;&#x60;link_checker&#x60;&#x60;, &#x60;&#x60;marketing&#x60;&#x60;, &#x60;&#x60;screenshot_creator&#x60;&#x60;, &#x60;&#x60;search_engine_bot&#x60;&#x60;,&#x60;&#x60;site_monitor&#x60;&#x60;, &#x60;&#x60;speed_tester&#x60;&#x60;, &#x60;&#x60;tool&#x60;&#x60;, &#x60;&#x60;uncategorized&#x60;&#x60;, &#x60;&#x60;unrecognized&#x60;&#x60;, &#x60;&#x60;virus_scanner&#x60;&#x60;,&#x60;&#x60;vulnerability_scanner&#x60;&#x60;, &#x60;&#x60;web_scraper&#x60;&#x60;.  ### Errors - a &#x60;404 Not Found&#x60; error if the origin token is not found. - a &#x60;400 Bad Request&#x60; error if the origin does not have the correct format.  It will return the API Global errors described in the API description.

    :param query: The origin site to query
    :type query: str
    :param interval: The data inteval to aggregate the result dataset
    :type interval: str
    :param from_timestamp: A UNIX timestamp in milliseconds to restrict the results of the query to entries logged after or equal to this value.
    :type from_timestamp: int
    :param to_timestamp: A UNIX timestamp in milliseconds to restrict the results of the query to entries logged before this value.
    :type to_timestamp: int

    """
    return web.Response(status=200)


async def update_configuration_origin_v1_origin_put(request: web.Request, body) -> web.Response:
    """Update the configuration of an origin of the user in the region.

    ### What Modify the configuration metadata of the origin of the user in the selected region.  The origin is a combination of protocol and domain (Ex: https://example.com) and the origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters In the body of the request, add the &#x60;origin&#x60; of the user and the &#x60;config&#x60; parameter with the following format for the &#x60;origin&#x60;:1. Protocol: Can be &#x60;&#x60;http&#x60;&#x60; or &#x60;&#x60;https&#x60;&#x60;. 2. Domain: The domain of the origin.  The &#x60;config&#x60; parameter is a JSON object containing the configuration of the origin. It only accepts the existing parameters obtained from the &#x60;GET&#x60; request of the origin. If the parameter is not present in the &#x60;config&#x60; object, it will fail to store it. It&#39;s not necessary to send all the parameters, only the ones that need to be updated.  ### Result The result is the JSON object with all the new values of the origin configuration.  ### Errors - a &#x60;404 Not Found&#x60; error if the origin token is not found. - a &#x60;400 Bad Request&#x60; error if the origin does not have the correct format. - a &#x60;400 Bad Request&#x60; error if the &#x60;config&#x60; parameter is not a JSON object or unknown parameters are sent.  It will return the API Global errors described in the API description.

    :param body: 
    :type body: dict | bytes

    """
    body = BodyUpdateConfigurationOriginV1OriginPut.from_dict(body)
    return web.Response(status=200)


async def update_origin_status_v1_origin_status_put(request: web.Request, query, body=None) -> web.Response:
    """Update the status of a given origin event in the platform.

    ### What Update the status of a given origin event in the platform. The status can be one of the    following values: - &#x60;PASS&#x60;: The event is not considered as a threat. - &#x60;BLOCK&#x60;: The event is considered as a threat and the origin must be blocked. - &#x60;CHALLENGE&#x60;: The event is considered as a threat and the origin must be challenged. - &#x60;BYPASS&#x60;: The event is considered as a threat but the origin must be bypassed. - &#x60;IGNORE&#x60;: The event is considered as a threat but the origin must be ignored.  To apply the change, it&#39;s necessary to send a request to the API with the &#x60;log_id&#x60; of the    origin status event and the scope of the change. The scope can be one of the following values: - &#x60;address_and_cookie&#x60;: The change will be applied to the origin IP address and the cookie. - &#x60;address&#x60;: The change will be applied to the origin IP address. - &#x60;cookie&#x60;: The change will be applied to the cookie.  ### Parameters The request must send the following parameters in the body of the request: - &#x60;&#x60;log_id&#x60;&#x60;: the log id of the origin status event. - &#x60;&#x60;scope&#x60;&#x60;: the scope of the change. Possible values are: &#x60;&#x60;address_and_cookie&#x60;&#x60;, &#x60;&#x60;address&#x60;&#x60;, &#x60;&#x60;cookie&#x60;&#x60;. - &#x60;&#x60;status&#x60;&#x60;: the new status of the origin. Possible values are: &#x60;&#x60;pass&#x60;&#x60;, &#x60;&#x60;block&#x60;&#x60;, &#x60;&#x60;challenge&#x60;&#x60;, &#x60;&#x60;bypass&#x60;&#x60;, &#x60;&#x60;ignore&#x60;&#x60;.  And in the &#x60;query&#x60; query string parameter, add the origin website in the format &#x60;https://example.com&#x60;.  ### Result A 200 OK response without any content.  ### Errors It will return the API Global errors described in the API description. If the parameters are invalid, it will return a &#x60;400 Bad Request&#x60; error.

    :param query: The origin site to query
    :type query: str
    :param body: 
    :type body: dict | bytes

    """
    body = BodyUpdateOriginStatusV1OriginStatusPut.from_dict(body)
    return web.Response(status=200)
