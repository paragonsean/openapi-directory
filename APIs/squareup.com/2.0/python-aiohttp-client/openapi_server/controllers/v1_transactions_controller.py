from typing import List, Dict
from aiohttp import web

from openapi_server.models.v1_create_refund_request import V1CreateRefundRequest
from openapi_server.models.v1_order import V1Order
from openapi_server.models.v1_payment import V1Payment
from openapi_server.models.v1_refund import V1Refund
from openapi_server.models.v1_settlement import V1Settlement
from openapi_server.models.v1_update_order_request import V1UpdateOrderRequest
from openapi_server import util


async def create_refund(request: web.Request, location_id, body) -> web.Response:
    """CreateRefund

    Issues a refund for a previously processed payment. You must issue a refund within 60 days of the associated payment.  You cannot issue a partial refund for a split tender payment. You must instead issue a full or partial refund for a particular tender, by providing the applicable tender id to the V1CreateRefund endpoint. Issuing a full refund for a split tender payment refunds all tenders associated with the payment.  Issuing a refund for a card payment is not reversible. For development purposes, you can create fake cash payments in Square Point of Sale and refund them.

    :param location_id: The ID of the original payment&#39;s associated location.
    :type location_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = V1CreateRefundRequest.from_dict(body)
    return web.Response(status=200)


async def list_orders(request: web.Request, location_id, order=None, limit=None, batch_token=None) -> web.Response:
    """ListOrders

    Provides summary information for a merchant&#39;s online store orders.

    :param location_id: The ID of the location to list online store orders for.
    :type location_id: str
    :param order: The order in which payments are listed in the response.
    :type order: str
    :param limit: The maximum number of payments to return in a single response. This value cannot exceed 200.
    :type limit: int
    :param batch_token: A pagination cursor to retrieve the next set of results for your original query to the endpoint.
    :type batch_token: str

    """
    return web.Response(status=200)


async def list_payments(request: web.Request, location_id, order=None, begin_time=None, end_time=None, limit=None, batch_token=None, include_partial=None) -> web.Response:
    """ListPayments

    Provides summary information for all payments taken for a given Square account during a date range. Date ranges cannot exceed 1 year in length. See Date ranges for details of inclusive and exclusive dates.  *Note**: Details for payments processed with Square Point of Sale while in offline mode may not be transmitted to Square for up to 72 hours. Offline payments have a &#x60;created_at&#x60; value that reflects the time the payment was originally processed, not the time it was subsequently transmitted to Square. Consequently, the ListPayments endpoint might list an offline payment chronologically between online payments that were seen in a previous request.

    :param location_id: The ID of the location to list payments for. If you specify me, this endpoint returns payments aggregated from all of the business&#39;s locations.
    :type location_id: str
    :param order: The order in which payments are listed in the response.
    :type order: str
    :param begin_time: The beginning of the requested reporting period, in ISO 8601 format. If this value is before January 1, 2013 (2013-01-01T00:00:00Z), this endpoint returns an error. Default value: The current time minus one year.
    :type begin_time: str
    :param end_time: The end of the requested reporting period, in ISO 8601 format. If this value is more than one year greater than begin_time, this endpoint returns an error. Default value: The current time.
    :type end_time: str
    :param limit: The maximum number of payments to return in a single response. This value cannot exceed 200.
    :type limit: int
    :param batch_token: A pagination cursor to retrieve the next set of results for your original query to the endpoint.
    :type batch_token: str
    :param include_partial: Indicates whether or not to include partial payments in the response. Partial payments will have the tenders collected so far, but the itemizations will be empty until the payment is completed.
    :type include_partial: bool

    """
    return web.Response(status=200)


async def list_refunds(request: web.Request, location_id, order=None, begin_time=None, end_time=None, limit=None, batch_token=None) -> web.Response:
    """ListRefunds

    Provides the details for all refunds initiated by a merchant or any of the merchant&#39;s mobile staff during a date range. Date ranges cannot exceed one year in length.

    :param location_id: The ID of the location to list refunds for.
    :type location_id: str
    :param order: The order in which payments are listed in the response.
    :type order: str
    :param begin_time: The beginning of the requested reporting period, in ISO 8601 format. If this value is before January 1, 2013 (2013-01-01T00:00:00Z), this endpoint returns an error. Default value: The current time minus one year.
    :type begin_time: str
    :param end_time: The end of the requested reporting period, in ISO 8601 format. If this value is more than one year greater than begin_time, this endpoint returns an error. Default value: The current time.
    :type end_time: str
    :param limit: The approximate number of refunds to return in a single response. Default: 100. Max: 200. Response may contain more results than the prescribed limit when refunds are made simultaneously to multiple tenders in a payment or when refunds are generated in an exchange to account for the value of returned goods.
    :type limit: int
    :param batch_token: A pagination cursor to retrieve the next set of results for your original query to the endpoint.
    :type batch_token: str

    """
    return web.Response(status=200)


async def list_settlements(request: web.Request, location_id, order=None, begin_time=None, end_time=None, limit=None, status=None, batch_token=None) -> web.Response:
    """ListSettlements

    Provides summary information for all deposits and withdrawals initiated by Square to a linked bank account during a date range. Date ranges cannot exceed one year in length.  *Note**: the ListSettlements endpoint does not provide entry information.

    :param location_id: The ID of the location to list settlements for. If you specify me, this endpoint returns settlements aggregated from all of the business&#39;s locations.
    :type location_id: str
    :param order: The order in which settlements are listed in the response.
    :type order: str
    :param begin_time: The beginning of the requested reporting period, in ISO 8601 format. If this value is before January 1, 2013 (2013-01-01T00:00:00Z), this endpoint returns an error. Default value: The current time minus one year.
    :type begin_time: str
    :param end_time: The end of the requested reporting period, in ISO 8601 format. If this value is more than one year greater than begin_time, this endpoint returns an error. Default value: The current time.
    :type end_time: str
    :param limit: The maximum number of settlements to return in a single response. This value cannot exceed 200.
    :type limit: int
    :param status: Provide this parameter to retrieve only settlements with a particular status (SENT or FAILED).
    :type status: str
    :param batch_token: A pagination cursor to retrieve the next set of results for your original query to the endpoint.
    :type batch_token: str

    """
    return web.Response(status=200)


async def retrieve_order(request: web.Request, location_id, order_id) -> web.Response:
    """RetrieveOrder

    Provides comprehensive information for a single online store order, including the order&#39;s history.

    :param location_id: The ID of the order&#39;s associated location.
    :type location_id: str
    :param order_id: The order&#39;s Square-issued ID. You obtain this value from Order objects returned by the List Orders endpoint
    :type order_id: str

    """
    return web.Response(status=200)


async def retrieve_payment(request: web.Request, location_id, payment_id) -> web.Response:
    """RetrievePayment

    Provides comprehensive information for a single payment.

    :param location_id: The ID of the payment&#39;s associated location.
    :type location_id: str
    :param payment_id: The Square-issued payment ID. payment_id comes from Payment objects returned by the List Payments endpoint, Settlement objects returned by the List Settlements endpoint, or Refund objects returned by the List Refunds endpoint.
    :type payment_id: str

    """
    return web.Response(status=200)


async def retrieve_settlement(request: web.Request, location_id, settlement_id) -> web.Response:
    """RetrieveSettlement

    Provides comprehensive information for a single settlement.  The returned &#x60;Settlement&#x60; objects include an &#x60;entries&#x60; field that lists the transactions that contribute to the settlement total. Most settlement entries correspond to a payment payout, but settlement entries are also generated for less common events, like refunds, manual adjustments, or chargeback holds.  Square initiates its regular deposits as indicated in the [Deposit Options with Square](https://squareup.com/help/us/en/article/3807) help article. Details for a regular deposit are usually not available from Connect API endpoints before 10 p.m. PST the same day.  Square does not know when an initiated settlement **completes**, only whether it has failed. A completed settlement is typically reflected in a bank account within 3 business days, but in exceptional cases it may take longer.

    :param location_id: The ID of the settlements&#39;s associated location.
    :type location_id: str
    :param settlement_id: The settlement&#39;s Square-issued ID. You obtain this value from Settlement objects returned by the List Settlements endpoint.
    :type settlement_id: str

    """
    return web.Response(status=200)


async def update_order(request: web.Request, location_id, order_id, body) -> web.Response:
    """UpdateOrder

    Updates the details of an online store order. Every update you perform on an order corresponds to one of three actions:

    :param location_id: The ID of the order&#39;s associated location.
    :type location_id: str
    :param order_id: The order&#39;s Square-issued ID. You obtain this value from Order objects returned by the List Orders endpoint
    :type order_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = V1UpdateOrderRequest.from_dict(body)
    return web.Response(status=200)
