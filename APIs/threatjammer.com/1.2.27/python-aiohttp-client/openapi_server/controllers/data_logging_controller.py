from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.ip_log_collection_output import IPLogCollectionOutput
from openapi_server.models.ip_log_output import IPLogOutput
from openapi_server import util


async def log_change_id_v1_log_ip_id_logchange_id_get(request: web.Request, logchange_id) -> web.Response:
    """Get a log event.

    ### What Obtain the full detail of a specific log change.  ### Parameters The endpoint accepts only the following parameters in the path: - &#x60;&#x60;logchange_id&#x60;&#x60;: (Mandatory) A unique integer of the change event log.  ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI of the API call - &#x60;&#x60;cidr&#x60;&#x60;: The CIDR affected by the change. - &#x60;&#x60;score&#x60;&#x60;: The score of the IP address when the event happened. It ranges from 0 to 99. - &#x60;&#x60;risk&#x60;&#x60;: The risk of the IP address when the event happened. The allowed values are: LOW, MEDIUM, HIGH. It&#39;s a human readable representation of the score. - &#x60;&#x60;dataset&#x60;&#x60;: The URI of the dataset where the change was logged. - &#x60;&#x60;source&#x60;&#x60;: The URI of the data source where the change was found. - &#x60;&#x60;lapse&#x60;&#x60;: The time elapsed between the event found and the moment the source was queried. The possible values are: 1H, 6H, 12H, 1D, 7D, 30D, 90D, 180D, 365D. - &#x60;&#x60;action&#x60;&#x60;: The action that was performed on the IP address. The allowed values are: ADD, DELETE. - &#x60;&#x60;timestamp&#x60;&#x60;: The UNIX timestamp in milliseconds when the change was logged.   ### Errors The endpoint will return the following errors: - a &#x60;404 Not Found&#x60; error if there is no event in the log with the &#x60;&#x60;logchange_ID&#x60;&#x60; given. - a &#x60;422 Unprocessable Entity&#x60; error if the &#x60;&#x60;logchange_ID&#x60;&#x60; is malformed.  It will also return the API Global errors described in the API description.

    :param logchange_id: 
    :type logchange_id: int

    """
    return web.Response(status=200)


async def logchanges_ip_v1_log_ip_ip_address_get(request: web.Request, ip_address, dataset=None, logged_after=None) -> web.Response:
    """Get the changes logged in the different datasets of an IP address.

    ### What Obtain a list of changes logged in the different datasets of the IP address given.  ### Parameters The endpoint accepts the following parameters in the path: - &#x60;&#x60;ip_address&#x60;&#x60;: (Mandatory) The public IPv4 or IPv6 addresses to be queried.  The endpoint accepts the following parameters in the query string: - &#x60;&#x60;dataset&#x60;&#x60;: (Optional) Name of the dataset to filter the query. If not given, then all datasets are queried. If given, then only the changes logged in the given dataset are returned. The list of datasets is obtained from the &#x60;&#x60;/v1/dataset/ip&#x60;&#x60; endpoint. - &#x60;&#x60;logged_after&#x60;&#x60;: (Optional) The UNIX timestamp in milliseconds of the earliest date to be included in the query. If not given, then the earliest date is the date of the first change logged in the dataset.   ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI of the API call - &#x60;&#x60;logs&#x60;&#x60;: The list of log changes. Each element of the list is a JSON object of a specific log change with the structure described in the endpoint &#x60;&#x60;/v1/log/ip/id/logchange_id&#x60;&#x60;. ### Errors The endpoint will return the following errors: - a &#x60;400 Bad Request&#x60; error if the IP address is not public. - a &#x60;400 Bad Request&#x60; error if the timestamp is in the future. - a &#x60;400 Bad Request&#x60; error if the dataset is not a string that can have numbers, upper and lower case letters, and underscores. - a &#x60;404 Not Found&#x60; error if the dataset was not found. - a &#x60;422 Unprocessable Entity&#x60; error if the IP address is malformed.  It will also return the API Global errors described in the API description.

    :param ip_address: The IPv4 or IPv6 address to asses the risk
    :type ip_address: str
    :param dataset: The name of the dataset to restrict the query
    :type dataset: str
    :param logged_after: A UNIX timestamp in milliseconds to restrict the results of the query to entries logged after this value.
    :type logged_after: int

    """
    return web.Response(status=200)
