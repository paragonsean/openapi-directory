from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.latency_scorecard import LatencyScorecard
from openapi_server.models.timeseries import Timeseries
from openapi_server import util


async def reports_get_latency_scorecards(request: web.Request, subscription_id, api_version, resource_group_name, profile_name, experiment_name, aggregation_interval, end_date_time_utc=None, country=None) -> web.Response:
    """Gets a Latency Scorecard for a given Experiment

    

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: The Profile identifier associated with the Tenant and Partner
    :type profile_name: str
    :param experiment_name: The Experiment identifier associated with the Experiment
    :type experiment_name: str
    :param aggregation_interval: The aggregation interval of the Latency Scorecard
    :type aggregation_interval: str
    :param end_date_time_utc: The end DateTime of the Latency Scorecard in UTC
    :type end_date_time_utc: str
    :param country: The country associated with the Latency Scorecard. Values are country ISO codes as specified here- https://www.iso.org/iso-3166-country-codes.html
    :type country: str

    """
    return web.Response(status=200)


async def reports_get_timeseries(request: web.Request, subscription_id, api_version, resource_group_name, profile_name, experiment_name, start_date_time_utc, end_date_time_utc, aggregation_interval, timeseries_type, endpoint=None, country=None) -> web.Response:
    """Gets a Timeseries for a given Experiment

    

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: The Profile identifier associated with the Tenant and Partner
    :type profile_name: str
    :param experiment_name: The Experiment identifier associated with the Experiment
    :type experiment_name: str
    :param start_date_time_utc: The start DateTime of the Timeseries in UTC
    :type start_date_time_utc: str
    :param end_date_time_utc: The end DateTime of the Timeseries in UTC
    :type end_date_time_utc: str
    :param aggregation_interval: The aggregation interval of the Timeseries
    :type aggregation_interval: str
    :param timeseries_type: The type of Timeseries
    :type timeseries_type: str
    :param endpoint: The specific endpoint
    :type endpoint: str
    :param country: The country associated with the Timeseries. Values are country ISO codes as specified here- https://www.iso.org/iso-3166-country-codes.html
    :type country: str

    """
    start_date_time_utc = util.deserialize_datetime(start_date_time_utc)
    end_date_time_utc = util.deserialize_datetime(end_date_time_utc)
    return web.Response(status=200)
