from typing import List, Dict
from aiohttp import web

from openapi_server.models.provider_detail_response import ProviderDetailResponse
from openapi_server.models.provider_response import ProviderResponse
from openapi_server.models.providers_count_response import ProvidersCountResponse
from openapi_server.models.yodlee_error import YodleeError
from openapi_server import util


async def get_all_providers(request: web.Request, capability=None, datasetfilter=None, full_account_number_fields=None, institution_id=None, name=None, priority=None, provider_id=None, skip=None, top=None) -> web.Response:
    """Get Providers

    The get provider service is used to get all the providers that are enabled, search a provider service by name or routing number and get popular sites of a region. &lt;br&gt;Searching for a provider using a routing number is applicable only to the USA and Canada regions.&lt;br&gt;The valid values for priority are: &lt;br&gt;   1. cobrand: Returns providers enabled for the cobrand (Default priority)&lt;br&gt;   2. popular: Returns providers popular among users of the customer&lt;br&gt;&lt;br&gt;Only the datasets, attributes, and containers that are enabled for the customer will be returned in the response.&lt;br&gt;Input for the dataset$filter should adhere to the following expression:&lt;br&gt;&lt;dataset.name&gt;[&lt;attribute.name&gt;.container[&lt;container&gt; OR &lt;container&gt;] OR &lt;attribute.name&gt;.container[&lt;container&gt;]] &lt;br&gt;OR &lt;dataset.name&gt;[&lt;attribute.name&gt; OR &lt;attribute.name&gt;]&lt;br&gt;&lt;b&gt;dataset$filter value examples:&lt;/b&gt;&lt;br&gt;ACCT_PROFILE[FULL_ACCT_NUMBER.container[bank OR investment OR creditCard]]&lt;br&gt;ACCT_PROFILE[FULL_ACCT_NUMBER.container[bank]]&lt;br&gt;BASIC_AGG_DATA[ACCOUNT_DETAILS.container[bank OR investment] OR HOLDINGS.container[bank]] OR ACCT_PROFILE[FULL_ACCT_NUMBER.container[bank]]&lt;br&gt;BASIC_AGG_DATA&lt;br&gt;BASIC_AGG_DATA OR ACCT_PROFILE&lt;br&gt;BASIC_AGG_DATA [ ACCOUNT_DETAILS OR HOLDINGS ]&lt;br&gt;BASIC_AGG_DATA [ ACCOUNT_DETAILS] OR DOCUMENT &lt;br&gt;BASIC_AGG_DATA [ BASIC_ACCOUNT_INFO OR ACCOUNT_DETAILS ] &lt;br&gt;&lt;br&gt;The fullAcountNumberFields is specified to filter the providers that have paymentAccountNumber or unmaskedAccountNumber support in the FULL_ACCT_NUMBER dataset attribute.&lt;br&gt;&lt;b&gt;Examples for usage of fullAccountNumberFields &lt;/b&gt;&lt;br&gt;dataset$filter&#x3D;ACCT_PROFILE[ FULL_ACCT_NUMBER.container [ bank ]] &amp;amp; fullAccountNumberFields&#x3D;paymentAccountNumber&lt;br&gt;dataset$filter&#x3D;ACCT_PROFILE[ FULL_ACCT_NUMBER.container [ bank ]] &amp;amp; fullAccountNumberFields&#x3D;unmaskedAccountNumber&lt;br&gt;dataset$filter&#x3D;ACCT_PROFILE[ FULL_ACCT_NUMBER.container [ bank ]] &amp;amp; fullAccountNumberFields&#x3D;unmaskedAccountNumber,paymentAccountNumber&lt;br&gt;&lt;br&gt;The skip and top parameters are used for pagination. In the skip and top parameters, pass the number of records to be skipped and retrieved, respectively.&lt;br&gt;The response header provides the links to retrieve the next and previous set of transactions.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;ol&gt;&lt;li&gt;In a product flow involving user interaction, Yodlee recommends invoking this service with filters.&lt;li&gt;Without filters, the service may perform slowly as it takes a few minutes to return data in the response.&lt;li&gt;The AuthParameter appears in the response only in case of token-based aggregation sites.&lt;li&gt;The pagination feature only applies when the priority parameter is set as cobrand. If no values are provided in the skip and top parameters, the API will only return the first 500 records.&lt;li&gt;This service supports the localization feature and accepts locale as a header parameter.&lt;li&gt;The capability has been deprecated in query parameter and response.&lt;/li&gt;&lt;/ol&gt;

    :param capability: CHALLENGE_DEPOSIT_VERIFICATION - capability search is deprecated
    :type capability: str
    :param datasetfilter: Expression to filter the providers by dataset(s) or dataset attribute(s). The default value will be the dataset or dataset attributes configured as default for the customer.
    :type datasetfilter: str
    :param full_account_number_fields: Specify to filter the providers with values paymentAccountNumber,unmaskedAccountNumber.
    :type full_account_number_fields: str
    :param institution_id: Institution Id for Single site selection
    :type institution_id: int
    :param name: Name in minimum 1 character or routing number.
    :type name: str
    :param priority: Search priority
    :type priority: str
    :param provider_id: Max 5 Comma seperated Provider Ids
    :type provider_id: str
    :param skip: skip (Min 0) - This is not applicable along with &#39;name&#39; parameter.
    :type skip: int
    :param top: top (Max 500) - This is not applicable along with &#39;name&#39; parameter.
    :type top: int

    """
    return web.Response(status=200)


async def get_provider(request: web.Request, provider_id) -> web.Response:
    """Get Provider Details

    The get provider detail service is used to get detailed information including the login form for a provider.&lt;br&gt;The response is a provider object that includes information such as name of the provider, &lt;br&gt;provider&#39;s base URL, a list of containers supported by the provider, the login form details of the provider, etc.&lt;br&gt;Only enabled datasets, attributes and containers gets returned in the response.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;li&gt;This service supports the localization feature and accepts locale as a header parameter.&lt;li&gt;The capability has been deprecated in the response.

    :param provider_id: providerId
    :type provider_id: int

    """
    return web.Response(status=200)


async def get_providers_count(request: web.Request, capability=None, datasetfilter=None, full_account_number_fields=None, name=None, priority=None) -> web.Response:
    """Get Providers Count

    The count service provides the total number of providers that get returned in the GET /providers depending on the input parameters passed.&lt;br&gt;If you are implementing pagination for providers, call this endpoint before calling GET /providers to know the number of providers that are returned for the input parameters passed.&lt;br&gt;The functionality of the input parameters remains the same as that of the GET /providers endpoint&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;li&gt;The capability has been deprecated in the query parameter.&lt;/li&gt;

    :param capability: CHALLENGE_DEPOSIT_VERIFICATION - capability search is deprecated
    :type capability: str
    :param datasetfilter: Expression to filter the providers by dataset(s) or dataset attribute(s). The default value will be the dataset or dataset attributes configured as default for the customer.
    :type datasetfilter: str
    :param full_account_number_fields: Specify to filter the providers with values paymentAccountNumber,unmaskedAccountNumber.
    :type full_account_number_fields: str
    :param name: Name in minimum 1 character or routing number.
    :type name: str
    :param priority: Search priority
    :type priority: str

    """
    return web.Response(status=200)
