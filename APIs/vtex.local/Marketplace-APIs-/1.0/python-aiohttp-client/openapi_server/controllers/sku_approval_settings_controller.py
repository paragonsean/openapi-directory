from typing import List, Dict
from aiohttp import web

from openapi_server.models.getaccountconfig200_response import Getaccountconfig200Response
from openapi_server.models.getauto_approvevaluefromconfig200_response import GetautoApprovevaluefromconfig200Response
from openapi_server.models.putselleraccountconfig_request import PutselleraccountconfigRequest
from openapi_server.models.saveaccountconfig200_response import Saveaccountconfig200Response
from openapi_server.models.saveaccountconfig_request import SaveaccountconfigRequest
from openapi_server.models.saveautoapproveforaccount200_response import Saveautoapproveforaccount200Response
from openapi_server.models.saveautoapproveforaccount_request import SaveautoapproveforaccountRequest
from openapi_server.models.saveautoapproveforaccountseller_request import SaveautoapproveforaccountsellerRequest
from openapi_server import util


async def getaccountconfig(request: web.Request, account_name, accept, content_type) -> web.Response:
    """Get Account&#39;s Approval Settings

    This endpoint retrieves the current approval settings of a marketplace&#39;s Received SKUs module. Its response includes:   - &#x60;Score&#x60;: Matcher scores for approving and rejecting SKUs received from sellers.   - &#x60;Matchers&#x60;: All Matchers configured on the marketplace, and their respective details.   - &#x60;SpecificationsMapping&#x60;: Mapping of product and SKU specifications, per seller.   - &#x60;MatchFlux&#x60;: This field determines the type of approval configuration applied to SKUs received from a seller.   The possible values include:   -&#x60;default&#x60;, where the Matcher reviews the SKU, and approves it based on its score.   -&#x60;manual&#x60;, for manual approvals through the Received SKU UI, or Match API.   -&#x60;autoApprove&#x60;, for every SKU received from a given seller to be approved automatically, regardless of their Matcher Score.

    :param account_name: Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    :type account_name: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str

    """
    return web.Response(status=200)


async def getauto_approvevaluefromconfig(request: web.Request, seller_id, account_name, accept, content_type) -> web.Response:
    """Get autoApprove Status in Account Settings

    This endpoint can be used to check whether the autoapprove setting is active or not, for a specific seller.   If the response is &#x60;true&#x60;, the autoapprove setting is active. If the response is &#x60;false&#x60;, it is inactive.

    :param seller_id: A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    :type seller_id: str
    :param account_name: Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    :type account_name: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str

    """
    return web.Response(status=200)


async def getselleraccountconfig(request: web.Request, account_name, seller_id, accept, content_type) -> web.Response:
    """Get Seller&#39;s Approval Settings

    This endpoint retrieves the current Received SKUs approval settings applied to a specific seller. Its response includes:   - &#x60;sellerId&#x60;: A string that identifies the seller in the marketplace.   - &#x60;accountId&#x60;: Marketplace’s account ID.   - &#x60;accountName&#x60;: Marketplace’s account name.   - &#x60;mapping&#x60;: Mapping of SKU and product Specifications.   - &#x60;matchFlux&#x60;: This field determines the type of approval configuration applied to SKUs received  from a seller.   The possible values include:    -&#x60;default&#x60;, where the Matcher reviews the SKU, and approves it based on its score.   -&#x60;manual&#x60;, for manual approvals through the Received SKU UI and Match API.   -&#x60;autoApprove&#x60;, for every SKU received from a given seller to be approved automatically, regardless of the Matcher Score.

    :param account_name: Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    :type account_name: str
    :param seller_id: A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    :type seller_id: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str

    """
    return web.Response(status=200)


async def putselleraccountconfig(request: web.Request, account_name, seller_id, accept, content_type, body) -> web.Response:
    """Save Seller&#39;s Approval Settings

    Marketplaces use this endpoint to create or update approval settings to a specific seller, on the Received SKUs module.   The request includes all the details necessary to implement the chosen approval settings.

    :param account_name: Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    :type account_name: str
    :param seller_id: A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    :type seller_id: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutselleraccountconfigRequest.from_dict(body)
    return web.Response(status=200)


async def saveaccountconfig(request: web.Request, account_name, accept, content_type, body) -> web.Response:
    """Save Account&#39;s Approval Settings

    Marketplaces use this endpoint to create or update approval settings on their Received SKUs module.   The request includes all the details necessary to implement the chosen approval settings.

    :param account_name: Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    :type account_name: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = SaveaccountconfigRequest.from_dict(body)
    return web.Response(status=200)


async def saveautoapproveforaccount(request: web.Request, account_name, accept, content_type, body) -> web.Response:
    """Activate autoApprove in Marketplace&#39;s Account

    This endpoint enables the autoapprove rule to a marketplace&#39;s whole Received SKUs module. Once enabling the rule, received SKUs will be automatically approved on your store, regardless of the seller.    For the autoapprove rule to work as expected, the approval [Matcher score](https://help.vtex.com/en/tutorial/entendendo-a-pontuacao-do-vtex-matcher--tutorials_424) should be set up as 80 (default value), but you can configure a different number through the field &#x60;Score&#x60; in [Save Account&#39;s Approval Settings](https://developers.vtex.com/vtex-rest-api/reference/saveaccountconfig).

    :param account_name: Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    :type account_name: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = SaveautoapproveforaccountRequest.from_dict(body)
    return web.Response(status=200)


async def saveautoapproveforaccountseller(request: web.Request, account_name, seller_id, accept, content_type, body) -> web.Response:
    """Activate autoApprove Setting for a Seller

    This endpoint enables the auto approve setting to received SKUs from a specific seller. Be aware that once enabling the rule through this request, all received SKUs from that seller will be automatically approved on your store, regardless of the Matcher Score.

    :param account_name: Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    :type account_name: str
    :param seller_id: A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    :type seller_id: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = SaveautoapproveforaccountsellerRequest.from_dict(body)
    return web.Response(status=200)
