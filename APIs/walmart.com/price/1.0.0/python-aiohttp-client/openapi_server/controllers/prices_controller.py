from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_strategy200_response import CreateStrategy200Response
from openapi_server.models.create_strategy_request import CreateStrategyRequest
from openapi_server.models.delete_strategy200_response import DeleteStrategy200Response
from openapi_server.models.get_repricer_feed200_response import GetRepricerFeed200Response
from openapi_server.models.get_repricer_feed_request import GetRepricerFeedRequest
from openapi_server.models.get_strategies200_response import GetStrategies200Response
from openapi_server.models.opt_cap_program_in_price200_response import OptCapProgramInPrice200Response
from openapi_server.models.opt_cap_program_in_price_request import OptCapProgramInPriceRequest
from openapi_server.models.price_bulk_uploads200_response import PriceBulkUploads200Response
from openapi_server.models.update_price200_response import UpdatePrice200Response
from openapi_server.models.update_price_request import UpdatePriceRequest
from openapi_server import util


async def create_strategy(request: web.Request, wm_sec_access_token, wm_qos_correlation_id, wm_svc_name, body, wm_consumer_channel_type=None) -> web.Response:
    """Create Repricer Strategy

    Creates a new strategy for the seller

    :param wm_sec_access_token: The access token retrieved in the Token API call
    :type wm_sec_access_token: str
    :param wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    :type wm_qos_correlation_id: str
    :param wm_svc_name: Walmart Service Name
    :type wm_svc_name: str
    :param body: The request body will have the strategy related information
    :type body: dict | bytes
    :param wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    :type wm_consumer_channel_type: str

    """
    body = CreateStrategyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_strategy(request: web.Request, wm_sec_access_token, wm_qos_correlation_id, wm_svc_name, strategy_collection_id, wm_consumer_channel_type=None) -> web.Response:
    """Delete Repricer Strategy

    Deletes the strategy

    :param wm_sec_access_token: The access token retrieved in the Token API call
    :type wm_sec_access_token: str
    :param wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    :type wm_qos_correlation_id: str
    :param wm_svc_name: Walmart Service Name
    :type wm_svc_name: str
    :param strategy_collection_id: Automatically added
    :type strategy_collection_id: str
    :param wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    :type wm_consumer_channel_type: str

    """
    return web.Response(status=200)


async def get_repricer_feed(request: web.Request, wm_sec_access_token, wm_qos_correlation_id, wm_svc_name, body, wm_consumer_channel_type=None) -> web.Response:
    """Assign/Unassign items to/from Repricer Strategy

    Add/Remove one or more items from a strategy

    :param wm_sec_access_token: The access token retrieved in the Token API call
    :type wm_sec_access_token: str
    :param wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    :type wm_qos_correlation_id: str
    :param wm_svc_name: Walmart Service Name
    :type wm_svc_name: str
    :param body: 
    :type body: dict | bytes
    :param wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    :type wm_consumer_channel_type: str

    """
    body = GetRepricerFeedRequest.from_dict(body)
    return web.Response(status=200)


async def get_strategies(request: web.Request, wm_sec_access_token, wm_qos_correlation_id, wm_svc_name, wm_consumer_channel_type=None) -> web.Response:
    """List of Repricer Strategies

    Get the list of strategies

    :param wm_sec_access_token: The access token retrieved in the Token API call
    :type wm_sec_access_token: str
    :param wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    :type wm_qos_correlation_id: str
    :param wm_svc_name: Walmart Service Name
    :type wm_svc_name: str
    :param wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    :type wm_consumer_channel_type: str

    """
    return web.Response(status=200)


async def opt_cap_program_in_price(request: web.Request, wm_sec_access_token, wm_qos_correlation_id, wm_svc_name, body, wm_consumer_channel_type=None) -> web.Response:
    """Set up CAP SKU All

    This API helps Sellers to completely opt-in or opt-out from CAP program.  If the subsidyEnrolled value &#x3D; \&quot;true\&quot;, the Seller enrolls in the CAP program. All eligible SKUs (current and future) are by default opt-in. Seller should use the SKU opt-in/opt-out API to opt-out individual items.  If the subsidyEnrolled value &#x3D; \&quot;false\&quot;, the Seller stops participating in the CAP program and all eligible SKUs (current and future) are opt-out of the CAP program.

    :param wm_sec_access_token: The access token retrieved in the Token API call
    :type wm_sec_access_token: str
    :param wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    :type wm_qos_correlation_id: str
    :param wm_svc_name: Walmart Service Name
    :type wm_svc_name: str
    :param body: Request fields
    :type body: dict | bytes
    :param wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    :type wm_consumer_channel_type: str

    """
    body = OptCapProgramInPriceRequest.from_dict(body)
    return web.Response(status=200)


async def price_bulk_uploads(request: web.Request, feed_type, wm_sec_access_token, wm_qos_correlation_id, wm_svc_name, file, wm_consumer_channel_type=None) -> web.Response:
    """Update bulk prices (Multiple)

    Updates prices in bulk.  In one Feed you can update up to 10,000 items in bulk. To ensure optimal Feed processing time, we recommend sending no more than 1000 items in one Feed and keeping the Feed sizes below 10 MB.  The price sequence guarantee is observed by the bulk price update functionality, subject to the following rules:  The timestamp used to determine precedence is passed in the request headers. All price updates in the feed are considered to have the same timestamp. The timestamp in the XML file is used only for auditing. You can send a single SKU multiple times in one Feed. If a SKU is repeated in a Feed, the price will be set for that SKU on Walmart.com, but there is no guarantee as to which SKU&#39;s price within that feed will be used. This API should be used in preference to the update a price. It should be called no sooner than 24 hours after a new item is set up and a wpid (Walmart Part ID) is available. Thereafter, the bulk price update has an service level agreement (SLA) of 15 minutes.  After the update is submitted, wait for at least five minutes before verifying whether the bulk price update was successful. Individual SKU price update success or failure is only available after the entire feed is processed.  If a SKU&#39;s price update fails (for example, multiple price updates were sent for the same SKU in a single feed), an error will be returned.

    :param feed_type: The feed Type
    :type feed_type: str
    :param wm_sec_access_token: The access token retrieved in the Token API call
    :type wm_sec_access_token: str
    :param wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    :type wm_qos_correlation_id: str
    :param wm_svc_name: Walmart Service Name
    :type wm_svc_name: str
    :param file: Feed file to upload
    :type file: str
    :param wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    :type wm_consumer_channel_type: str

    """
    return web.Response(status=200)


async def update_price(request: web.Request, wm_sec_access_token, wm_qos_correlation_id, wm_svc_name, body, wm_consumer_channel_type=None) -> web.Response:
    """Update a price

    Updates the regular price for a given item.

    :param wm_sec_access_token: The access token retrieved in the Token API call
    :type wm_sec_access_token: str
    :param wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    :type wm_qos_correlation_id: str
    :param wm_svc_name: Walmart Service Name
    :type wm_svc_name: str
    :param body: The request body consists of a Feed file attached to the request.
    :type body: dict | bytes
    :param wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    :type wm_consumer_channel_type: str

    """
    body = UpdatePriceRequest.from_dict(body)
    return web.Response(status=200)


async def update_strategy(request: web.Request, wm_sec_access_token, wm_qos_correlation_id, wm_svc_name, strategy_collection_id, body, wm_consumer_channel_type=None) -> web.Response:
    """Update Repricer Strategy

    Updates the existing strategy

    :param wm_sec_access_token: The access token retrieved in the Token API call
    :type wm_sec_access_token: str
    :param wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    :type wm_qos_correlation_id: str
    :param wm_svc_name: Walmart Service Name
    :type wm_svc_name: str
    :param strategy_collection_id: Automatically added
    :type strategy_collection_id: str
    :param body: The request body will have the strategy related information
    :type body: dict | bytes
    :param wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    :type wm_consumer_channel_type: str

    """
    body = CreateStrategyRequest.from_dict(body)
    return web.Response(status=200)
