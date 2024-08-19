from typing import List, Dict
from aiohttp import web

from openapi_server.models.chart_data200_response import ChartData200Response
from openapi_server.models.create_data_request import CreateDataRequest
from openapi_server.models.create_group_data_request import CreateGroupDataRequest
from openapi_server.models.create_webhook_feed_data_request import CreateWebhookFeedDataRequest
from openapi_server.models.data import Data
from openapi_server.models.data_response import DataResponse
from openapi_server import util


async def all_data(request: web.Request, username, feed_key, start_time=None, end_time=None, limit=None, include=None) -> web.Response:
    """Get all data for the given feed

    

    :param username: a valid username string
    :type username: str
    :param feed_key: a valid feed key
    :type feed_key: str
    :param start_time: Start time for filtering, returns records created after given time.
    :type start_time: str
    :param end_time: End time for filtering, returns records created before give time.
    :type end_time: str
    :param limit: Limit the number of records returned.
    :type limit: int
    :param include: List of Data record fields to include in response as comma separated list. Acceptable values are: &#x60;value&#x60;, &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60;, &#x60;id&#x60;, and &#x60;created_at&#x60;. 
    :type include: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def all_group_feed_data(request: web.Request, username, group_key, feed_key, start_time=None, end_time=None, limit=None) -> web.Response:
    """All data for current feed in a specific group

    

    :param username: a valid username string
    :type username: str
    :param group_key: 
    :type group_key: str
    :param feed_key: a valid feed key
    :type feed_key: str
    :param start_time: Start time for filtering data. Returns data created after given time.
    :type start_time: str
    :param end_time: End time for filtering data. Returns data created before give time.
    :type end_time: str
    :param limit: Limit the number of records returned.
    :type limit: int

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def batch_create_data(request: web.Request, username, feed_key, data) -> web.Response:
    """Create multiple new Data records

    

    :param username: a valid username string
    :type username: str
    :param feed_key: a valid feed key
    :type feed_key: str
    :param data: A collection of data records including &#x60;value&#x60; (required) and optionally including: &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60; (latitude, longitude, and elevation values), and &#x60;created_at&#x60; (a date/time string).
    :type data: list | bytes

    """
    data = [CreateDataRequest.from_dict(d) for d in data]
    return web.Response(status=200)


async def batch_create_group_feed_data(request: web.Request, username, group_key, feed_key, data) -> web.Response:
    """Create multiple new Data records in a feed belonging to a particular group

    

    :param username: a valid username string
    :type username: str
    :param group_key: 
    :type group_key: str
    :param feed_key: a valid feed key
    :type feed_key: str
    :param data: A collection of data records including &#x60;value&#x60; (required) and optionally including: &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60; (latitude, longitude, and elevation values), and &#x60;created_at&#x60; (a date/time string).
    :type data: list | bytes

    """
    data = [CreateDataRequest.from_dict(d) for d in data]
    return web.Response(status=200)


async def chart_data(request: web.Request, username, feed_key, start_time=None, end_time=None, resolution=None, hours=None) -> web.Response:
    """Chart data for current feed

    The Chart API is what we use on io.adafruit.com to populate charts over varying timespans with a consistent number of data points. The maximum number of points returned is 480. This API works by aggregating slices of time into a single value by averaging.  All time-based parameters are optional, if none are given it will default to 1 hour at the finest-grained resolution possible.

    :param username: a valid username string
    :type username: str
    :param feed_key: a valid feed key
    :type feed_key: str
    :param start_time: Start time for filtering, returns records created after given time.
    :type start_time: str
    :param end_time: End time for filtering, returns records created before give time.
    :type end_time: str
    :param resolution: A resolution size in minutes. By giving a resolution value you will get back grouped data points aggregated over resolution-sized intervals. NOTE: time span is preferred over resolution, so if you request a span of time that includes more than max limit points you may get a larger resolution than you requested. Valid resolutions are 1, 5, 10, 30, 60, and 120.
    :type resolution: int
    :param hours: The number of hours the chart should cover.
    :type hours: int

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def create_data(request: web.Request, username, feed_key, datum) -> web.Response:
    """Create new Data

    Create new data records on the given feed.  **NOTE:** when feed history is on, data &#x60;value&#x60; size is limited to 1KB, when feed history is turned off data value size is limited to 100KB.

    :param username: a valid username string
    :type username: str
    :param feed_key: a valid feed key
    :type feed_key: str
    :param datum: Data record including a &#x60;value&#x60; field (required) and optionally including: &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60; (latitude, longitude, and elevation values), and &#x60;created_at&#x60; (a date/time string).
    :type datum: dict | bytes

    """
    datum = CreateDataRequest.from_dict(datum)
    return web.Response(status=200)


async def create_group_data(request: web.Request, username, group_key, group_feed_data) -> web.Response:
    """Create new data for multiple feeds in a group

    

    :param username: a valid username string
    :type username: str
    :param group_key: 
    :type group_key: str
    :param group_feed_data: 
    :type group_feed_data: dict | bytes

    """
    group_feed_data = CreateGroupDataRequest.from_dict(group_feed_data)
    return web.Response(status=200)


async def create_group_feed_data(request: web.Request, username, group_key, feed_key, datum) -> web.Response:
    """Create new Data in a feed belonging to a particular group

    

    :param username: a valid username string
    :type username: str
    :param group_key: 
    :type group_key: str
    :param feed_key: a valid feed key
    :type feed_key: str
    :param datum: Data record including a &#x60;value&#x60; field (required) and optionally including: &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60; (latitude, longitude, and elevation values), and &#x60;created_at&#x60; (a date/time string).
    :type datum: dict | bytes

    """
    datum = CreateDataRequest.from_dict(datum)
    return web.Response(status=200)


async def create_raw_webhook_feed_data_0(request: web.Request, ) -> web.Response:
    """Send arbitrary data to a feed via webhook URL.

    The raw data webhook receiver accepts POST requests and stores the raw request body on your feed. This is useful when you don&#39;t have control of the webhook sender. If feed history is turned on, payloads will be truncated at 1024 bytes. If feed history is turned off, payloads will be truncated at 100KB.


    """
    return web.Response(status=200)


async def create_webhook_feed_data_0(request: web.Request, payload) -> web.Response:
    """Send data to a feed via webhook URL.

    

    :param payload: Webhook payload containing data &#x60;value&#x60; parameter.
    :type payload: dict | bytes

    """
    payload = CreateWebhookFeedDataRequest.from_dict(payload)
    return web.Response(status=200)


async def destroy_data(request: web.Request, username, feed_key, id) -> web.Response:
    """Delete existing Data

    

    :param username: a valid username string
    :type username: str
    :param feed_key: a valid feed key
    :type feed_key: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def first_data(request: web.Request, username, feed_key, include=None) -> web.Response:
    """First Data in Queue

    Get the oldest data point in the feed. This request sets the queue pointer to the beginning of the feed.

    :param username: a valid username string
    :type username: str
    :param feed_key: a valid feed key
    :type feed_key: str
    :param include: List of Data record fields to include in response as comma separated list. Acceptable values are: &#x60;value&#x60;, &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60;, &#x60;id&#x60;, and &#x60;created_at&#x60;. 
    :type include: str

    """
    return web.Response(status=200)


async def get_data(request: web.Request, username, feed_key, id, include=None) -> web.Response:
    """Returns data based on feed key

    

    :param username: a valid username string
    :type username: str
    :param feed_key: a valid feed key
    :type feed_key: str
    :param id: 
    :type id: str
    :param include: List of Data record fields to include in response as comma separated list. Acceptable values are: &#x60;value&#x60;, &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60;, &#x60;id&#x60;, and &#x60;created_at&#x60;. 
    :type include: str

    """
    return web.Response(status=200)


async def last_data(request: web.Request, username, feed_key, include=None) -> web.Response:
    """Last Data in Queue

    Get the most recent data point in the feed. This request sets the queue pointer to the end of the feed.

    :param username: a valid username string
    :type username: str
    :param feed_key: a valid feed key
    :type feed_key: str
    :param include: List of Data record fields to include in response as comma separated list. Acceptable values are: &#x60;value&#x60;, &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60;, &#x60;id&#x60;, and &#x60;created_at&#x60;. 
    :type include: str

    """
    return web.Response(status=200)


async def next_data(request: web.Request, username, feed_key, include=None) -> web.Response:
    """Next Data in Queue

    Get the next newest data point in the feed. If queue processing hasn&#39;t been started, the first data point in the feed will be returned.

    :param username: a valid username string
    :type username: str
    :param feed_key: a valid feed key
    :type feed_key: str
    :param include: List of Data record fields to include in response as comma separated list. Acceptable values are: &#x60;value&#x60;, &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60;, &#x60;id&#x60;, and &#x60;created_at&#x60;. 
    :type include: str

    """
    return web.Response(status=200)


async def previous_data(request: web.Request, username, feed_key, include=None) -> web.Response:
    """Previous Data in Queue

    Get the previously processed data point in the feed. NOTE: this method doesn&#39;t move the processing queue pointer.

    :param username: a valid username string
    :type username: str
    :param feed_key: a valid feed key
    :type feed_key: str
    :param include: List of Data record fields to include in response as comma separated list. Acceptable values are: &#x60;value&#x60;, &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60;, &#x60;id&#x60;, and &#x60;created_at&#x60;. 
    :type include: str

    """
    return web.Response(status=200)


async def replace_data(request: web.Request, username, feed_key, id, datum) -> web.Response:
    """Replace existing Data

    

    :param username: a valid username string
    :type username: str
    :param feed_key: a valid feed key
    :type feed_key: str
    :param id: 
    :type id: str
    :param datum: Data record including a &#x60;value&#x60; field (required) and optionally including: &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60; (latitude, longitude, and elevation values), and &#x60;created_at&#x60; (a date/time string).
    :type datum: dict | bytes

    """
    datum = CreateDataRequest.from_dict(datum)
    return web.Response(status=200)


async def retain_data(request: web.Request, username, feed_key) -> web.Response:
    """Last Data in MQTT CSV format

    Get the most recent data point in the feed in an MQTT compatible CSV format: &#x60;value,lat,lon,ele&#x60;

    :param username: a valid username string
    :type username: str
    :param feed_key: a valid feed key
    :type feed_key: str

    """
    return web.Response(status=200)


async def update_data(request: web.Request, username, feed_key, id, datum) -> web.Response:
    """Update properties of existing Data

    

    :param username: a valid username string
    :type username: str
    :param feed_key: a valid feed key
    :type feed_key: str
    :param id: 
    :type id: str
    :param datum: Data record including a &#x60;value&#x60; field (required) and optionally including: &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60; (latitude, longitude, and elevation values), and &#x60;created_at&#x60; (a date/time string).
    :type datum: dict | bytes

    """
    datum = CreateDataRequest.from_dict(datum)
    return web.Response(status=200)
