from typing import List, Dict
from aiohttp import web

from openapi_server.models.configuration_summary_list_response import ConfigurationSummaryListResponse
from openapi_server.models.configuration_update_summary_list_response import ConfigurationUpdateSummaryListResponse
from openapi_server import util


async def query_configuration_history_updates(request: web.Request, limit=None, offset=None, api_user=None, node_id=None, namespace=None, name=None, source=None, after_time=None, before_time=None) -> web.Response:
    """View a list of filtered configuration updates

    View a list of cluster configuration options that have updated within a specified time window.

    :param limit: Limit the number of matches returned.
    :type limit: int
    :param offset: Ignore these many matches in the beginning.
    :type offset: int
    :param api_user: The username of the account. Applies a filter to the configuration updates performed by the specified username.
    :type api_user: str
    :param node_id: The node ID. Applies a filter to the configuration updates for the specified node. When no node_id is specified, the filter shows both local and cluster-wide configurations. Specify &#39;cluster&#39; for filtering out cluster-wide configuration updates.
    :type node_id: str
    :param namespace: The configuration namespace. Applies a filter to the configuration updates for the specified namespace.
    :type namespace: str
    :param name: Name of the configuration. Applies a filter to the configuration updates for the specified configuration name.
    :type name: str
    :param source: Source for configuration updates. Applies a filter to the configuration updates for the specified source.
    :type source: str
    :param after_time: The earliest time configuration history is needed. Applies a filter that only shows configuration updates after the specified time.
    :type after_time: str
    :param before_time: The latest time configuration history is needed. Applies filter to display only configuration updates prior to the specified time. The default value is the current time.
    :type before_time: str

    """
    after_time = util.deserialize_datetime(after_time)
    before_time = util.deserialize_datetime(before_time)
    return web.Response(status=200)


async def retrieve_configuration_values(request: web.Request, namespace, on_date, limit=None, offset=None, node_id=None, name=None) -> web.Response:
    """View a list of configurations and their values on a given date

    View a list of configurations and their values on a given date.

    :param namespace: The configuration namespace. Applies a filter to the configuration updates for the specified namespace.
    :type namespace: str
    :param on_date: The timestamp for which to retrieve configuration values.
    :type on_date: str
    :param limit: Limit the number of matches returned.
    :type limit: int
    :param offset: Ignore these many matches in the beginning.
    :type offset: int
    :param node_id: The name of the node that require configuration values. Applies a filter specific to the name of node. When no node_id is specified, the filter shows both local and cluster-wide configurations.
    :type node_id: str
    :param name: The name of the configuration option. Applies a filter to the configuration updates for the specified option.
    :type name: str

    """
    on_date = util.deserialize_datetime(on_date)
    return web.Response(status=200)
