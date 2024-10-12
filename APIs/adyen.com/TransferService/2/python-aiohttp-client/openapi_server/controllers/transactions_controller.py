from typing import List, Dict
from aiohttp import web

from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.transaction import Transaction
from openapi_server.models.transaction_search_response import TransactionSearchResponse
from openapi_server import util


async def get_transactions(request: web.Request, created_since, created_until, balance_platform=None, payment_instrument_id=None, account_holder_id=None, balance_account_id=None, cursor=None, limit=None) -> web.Response:
    """Get all transactions

    &gt;Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the latest version.  Returns all the transactions related to a balance account, account holder, or balance platform.  When making this request, you must include at least one of the following: - &#x60;balanceAccountId&#x60; - &#x60;accountHolderId&#x60; - &#x60;balancePlatform&#x60;.  This endpoint supports cursor-based pagination. The response returns the first page of results, and returns links to the next and previous pages when applicable. You can use the links to page through the results.  

    :param created_since: Only include transactions that have been created on or after this point in time. The value must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
    :type created_since: str
    :param created_until: Only include transactions that have been created on or before this point in time. The value must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
    :type created_until: str
    :param balance_platform: The unique identifier of the [balance platform](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balancePlatforms/{id}__queryParam_id).  Required if you don&#39;t provide a &#x60;balanceAccountId&#x60; or &#x60;accountHolderId&#x60;.
    :type balance_platform: str
    :param payment_instrument_id: The unique identifier of the [payment instrument](https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/_id_).  To use this parameter, you must also provide a &#x60;balanceAccountId&#x60;, &#x60;accountHolderId&#x60;, or &#x60;balancePlatform&#x60;.  The &#x60;paymentInstrumentId&#x60; must be related to the &#x60;balanceAccountId&#x60; or &#x60;accountHolderId&#x60; that you provide.
    :type payment_instrument_id: str
    :param account_holder_id: The unique identifier of the [account holder](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/accountHolders/{id}__queryParam_id).  Required if you don&#39;t provide a &#x60;balanceAccountId&#x60; or &#x60;balancePlatform&#x60;.  If you provide a &#x60;balanceAccountId&#x60;, the &#x60;accountHolderId&#x60; must be related to the &#x60;balanceAccountId&#x60;.
    :type account_holder_id: str
    :param balance_account_id: The unique identifier of the [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__queryParam_id).  Required if you don&#39;t provide an &#x60;accountHolderId&#x60; or &#x60;balancePlatform&#x60;.  If you provide an &#x60;accountHolderId&#x60;, the &#x60;balanceAccountId&#x60; must be related to the &#x60;accountHolderId&#x60;.
    :type balance_account_id: str
    :param cursor: The &#x60;cursor&#x60; returned in the links of the previous response.
    :type cursor: str
    :param limit: The number of items returned per page, maximum of 100 items. By default, the response returns 10 items per page.
    :type limit: int

    """
    created_since = util.deserialize_datetime(created_since)
    created_until = util.deserialize_datetime(created_until)
    return web.Response(status=200)


async def get_transactions_id(request: web.Request, id) -> web.Response:
    """Get a transaction

    &gt;Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the latest version.  Returns a transaction.

    :param id: The unique identifier of the transaction.
    :type id: str

    """
    return web.Response(status=200)
