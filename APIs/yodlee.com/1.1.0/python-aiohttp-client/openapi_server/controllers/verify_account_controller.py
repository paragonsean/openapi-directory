from typing import List, Dict
from aiohttp import web

from openapi_server.models.verify_account_request import VerifyAccountRequest
from openapi_server.models.verify_account_response import VerifyAccountResponse
from openapi_server.models.yodlee_error import YodleeError
from openapi_server import util


async def initiate_account_verification(request: web.Request, provider_account_id, body) -> web.Response:
    """Verify Accounts Using Transactions

    The verify account service is used to verify the account&#39;s ownership by  matching the transaction details with the accounts aggregated for the user.&lt;br&gt;&lt;ul&gt;&lt;li&gt;If a match is identified, the service returns details of all the accounts along with the matched transaction&#39;s details.&lt;li&gt;If no transaction match is found, an empty response will be returned.&lt;li&gt;A maximum of 5 transactionCriteria can be passed in a request.&lt;li&gt;The baseType, date, and amount parameters should mandatorily be passed.&lt;li&gt;The optional dateVariance parameter cannot be more than 7 days. For example, +7, -4, or +/-2.&lt;li&gt;Pass the container or accountId parameters for better performance.&lt;li&gt;This service supports the localization feature and accepts locale as a header parameter.&lt;/li&gt;&lt;/ul&gt;

    :param provider_account_id: providerAccountId
    :type provider_account_id: str
    :param body: verificationParam
    :type body: dict | bytes

    """
    body = VerifyAccountRequest.from_dict(body)
    return web.Response(status=200)
