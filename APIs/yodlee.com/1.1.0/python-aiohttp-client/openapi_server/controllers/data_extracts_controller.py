from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_extracts_event_response import DataExtractsEventResponse
from openapi_server.models.data_extracts_user_data_response import DataExtractsUserDataResponse
from openapi_server.models.yodlee_error import YodleeError
from openapi_server import util


async def get_data_extracts_events(request: web.Request, event_name, from_date, to_date) -> web.Response:
    """Get Events

    The get extracts events service is used to learn about occurrences of data extract related events. This service currently supports only the DATA_UPDATES event.&lt;br&gt;Passing the event name as DATA_UPDATES provides information about users for whom data has been modified in the system for the specified time range. To learn more, please refer to the &lt;a href&#x3D;\&quot;https://developer.yodlee.com/docs/api/1.1/DataExtracts\&quot;&gt;dataExtracts&lt;/a&gt; page.&lt;br&gt;You can retrieve data in increments of no more than 60 minutes over the period of the last 7 days from today&#39;s date.&lt;br&gt;This service is only invoked with either admin access token or a cobrand session.&lt;br&gt;

    :param event_name: Event Name
    :type event_name: str
    :param from_date: From DateTime (YYYY-MM-DDThh:mm:ssZ)
    :type from_date: str
    :param to_date: To DateTime (YYYY-MM-DDThh:mm:ssZ)
    :type to_date: str

    """
    return web.Response(status=200)


async def get_data_extracts_user_data(request: web.Request, from_date, login_name, to_date) -> web.Response:
    """Get userData

    The get user data service is used to get a user&#39;s modified data for a particular period of time for accounts, transactions, holdings, and provider account information.&lt;br&gt;The time difference between fromDate and toDate fields cannot be more than 60 minutes.&lt;br&gt;By default, pagination is available for the transaction entity in this API. In the first response, the API will retrieve 500 transactions along with other data. The response header will provide a link to retrieve the next set of transactions.&lt;br&gt;In the response body of the first API response, totalTransactionsCount indicates the total number of transactions the API will retrieve for the user.&lt;br&gt;This service is only invoked with either admin access token or a cobrand session.&lt;br/&gt;Refer to &lt;a href&#x3D;\&quot;https://developer.yodlee.com/docs/api/1.1/DataExtracts\&quot;&gt;dataExtracts&lt;/a&gt; page for more information.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;li&gt;This service supports the localization feature and accepts locale as a header parameter.&lt;/li&gt;

    :param from_date: From DateTime (YYYY-MM-DDThh:mm:ssZ)
    :type from_date: str
    :param login_name: Login Name
    :type login_name: str
    :param to_date: To DateTime (YYYY-MM-DDThh:mm:ssZ)
    :type to_date: str

    """
    return web.Response(status=200)
