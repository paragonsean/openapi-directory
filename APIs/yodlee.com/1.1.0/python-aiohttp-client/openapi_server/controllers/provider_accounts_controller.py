from typing import List, Dict
from aiohttp import web

from openapi_server.models.provider_account_detail_response import ProviderAccountDetailResponse
from openapi_server.models.provider_account_preferences_request import ProviderAccountPreferencesRequest
from openapi_server.models.provider_account_request import ProviderAccountRequest
from openapi_server.models.provider_account_response import ProviderAccountResponse
from openapi_server.models.provider_account_user_profile_response import ProviderAccountUserProfileResponse
from openapi_server.models.updated_provider_account_response import UpdatedProviderAccountResponse
from openapi_server.models.yodlee_error import YodleeError
from openapi_server import util


async def delete_provider_account(request: web.Request, provider_account_id) -> web.Response:
    """Delete Provider Account

    The delete provider account service is used to delete a provider account from the Yodlee system. This service also deletes the accounts that are created in the Yodlee system for that provider account. &lt;br&gt;This service does not return a response. The HTTP response code is 204 (Success with no content).&lt;br&gt;

    :param provider_account_id: providerAccountId
    :type provider_account_id: int

    """
    return web.Response(status=200)


async def edit_credentials_or_refresh_provider_account(request: web.Request, provider_account_ids, body=None) -> web.Response:
    """Update Account

    The update account API is used to:&lt;br&gt; &lt;ul&gt;&lt;li&gt;Retrieve the latest information for accounts that belong to one providerAccount from the provider site. You must allow at least 15 min between requests.&lt;li&gt;Retrieve the latest information of all the eligible accounts that belong to the user.&lt;li&gt;Data to be retrieved from the provider site can be overridden using datasetName or dataset. If you do pass datasetName, all the datasets that are implicitly configured for the dataset will be retrieved. This action is allowed for single provider account refresh flows only.&lt;li&gt;Check the status of the providerAccount before invoking this API. Do not call this API to trigger any action on a providerAccount when an action is already in progress for the providerAccount.&lt;li&gt;If the customer has subscribed to the REFRESH event notification and invoked this API, relevant notifications will be sent to the customer.&lt;li&gt;A dataset may depend on another dataset for retrieval, so the response will include the requested and dependent datasets.&lt;li&gt;Check all the dataset additional statuses returned in the response because the provider account status is drawn from the dataset additional statuses.&lt;li&gt;Updating preferences using this API will trigger refreshes.&lt;li&gt; The content type has to be passed as application/json for the body parameter.&lt;/ul&gt;&lt;br&gt;-----------------------------------------------------------------------------------------------------------------------------------------&lt;br&gt;&lt;br&gt;&lt;b&gt;Update All Eligible Accounts - Notes:&lt;/b&gt;&lt;br&gt;&lt;ul&gt;&lt;li&gt;This API will trigger a refresh for all the eligible provider accounts(both OB and credential-based accounts).&lt;li&gt;This API will not refresh closed, inactive, or UAR accounts, or accounts with refreshes in-progress or recently refreshed non-OB accounts.&lt;li&gt;No parameters should be passed to this API to trigger this action.&lt;li&gt;Do not call this API often. Our recommendation is to call this only at the time the user logs in to your app because it can hamper other API calls performance.&lt;li&gt;The response only contains information for accounts that were refreshed. If no accounts are eligible for refresh, no response is returned.&lt;/ul&gt;

    :param provider_account_ids: comma separated providerAccountIds
    :type provider_account_ids: str
    :param body: loginForm or field entity
    :type body: dict | bytes

    """
    body = ProviderAccountRequest.from_dict(body)
    return web.Response(status=200)


async def get_all_provider_accounts(request: web.Request, include=None, provider_ids=None) -> web.Response:
    """Get Provider Accounts

    The get provider accounts service is used to return all the provider accounts added by the user. &lt;br&gt;This includes the failed and successfully added provider accounts.&lt;br&gt;

    :param include: include
    :type include: str
    :param provider_ids: Comma separated providerIds.
    :type provider_ids: str

    """
    return web.Response(status=200)


async def get_provider_account(request: web.Request, provider_account_id, include=None, request_id=None) -> web.Response:
    """Get Provider Account Details

    The get provider account details service is used to learn the status of adding accounts and updating accounts.&lt;br&gt;This service has to be called continuously to know the progress level of the triggered process. This service also provides the MFA information requested by the provider site.&lt;br&gt;When &lt;i&gt;include &#x3D; credentials&lt;/i&gt;, questions is passed as input, the service returns the credentials (non-password values) and questions stored in the Yodlee system for that provider account. &lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;li&gt;The password and answer fields are not returned in the response.&lt;/li&gt;

    :param provider_account_id: providerAccountId
    :type provider_account_id: int
    :param include: include credentials,questions
    :type include: str
    :param request_id: The unique identifier for the request that returns contextual data
    :type request_id: str

    """
    return web.Response(status=200)


async def get_provider_account_profiles(request: web.Request, provider_account_id=None) -> web.Response:
    """Get User Profile Details

    The get provider accounts profile service is used to return the user profile details that are associated to the provider account. &lt;br&gt;

    :param provider_account_id: Comma separated providerAccountIds.
    :type provider_account_id: str

    """
    return web.Response(status=200)


async def update_preferences(request: web.Request, provider_account_id, body) -> web.Response:
    """Update Preferences

    This endpoint is used to update preferences like data extracts and auto refreshes without triggering refresh for the providerAccount.&lt;br&gt;Setting isDataExtractsEnabled to false will not trigger data extracts notification and dataExtracts/events will not reflect any data change that is happening for the providerAccount.&lt;br&gt;Modified data will not be provided in the dataExtracts/userData endpoint.&lt;br&gt;Setting isAutoRefreshEnabled to false will not trigger auto refreshes for the provider account.&lt;br&gt;

    :param provider_account_id: providerAccountId
    :type provider_account_id: int
    :param body: preferences
    :type body: dict | bytes

    """
    body = ProviderAccountPreferencesRequest.from_dict(body)
    return web.Response(status=200)
