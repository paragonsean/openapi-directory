from typing import List, Dict
from aiohttp import web

from openapi_server.models.model1_createanewtransaction_request import Model1CreateanewtransactionRequest
from openapi_server.models.model2_send_payments_public_request import Model2SendPaymentsPublicRequest
from openapi_server.models.model2_send_payments_with_saved_credit_card_request import Model2SendPaymentsWithSavedCreditCardRequest
from openapi_server.models.model4_doauthorization_request import Model4DoauthorizationRequest
from openapi_server.models.payment_details_response import PaymentDetailsResponse
from openapi_server.models.start_transaction_response import StartTransactionResponse
from openapi_server.models.transaction_details_response import TransactionDetailsResponse
from openapi_server.models.transaction_settlement_details import TransactionSettlementDetails
from openapi_server import util


async def call1_createanewtransaction(request: web.Request, x_provider_api_app_key, x_provider_api_app_token, accept, content_type, body) -> web.Response:
    """1. Starts a new transaction

    This request is the first step to create a new transaction.

    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = Model1CreateanewtransactionRequest.from_dict(body)
    return web.Response(status=200)


async def call2_send_payments_public(request: web.Request, order_id, x_provider_api_app_key, x_provider_api_app_token, accept, content_type, transaction_id, body) -> web.Response:
    """2.1 Send Payments Information Public

    The second step to create a new transaction. Here, you have the option to send the data in three diferent ways: doing a private request, a public request or a private request that uses a saved Credit Card. 

    :param order_id: 
    :type order_id: str
    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param transaction_id: 
    :type transaction_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [Model2SendPaymentsPublicRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def call2_send_payments_with_saved_credit_card(request: web.Request, x_provider_api_app_key, x_provider_api_app_token, accept, content_type, transaction_id, body) -> web.Response:
    """2.2 Send Payments With Saved Credit Card

    The second step to create a new transaction. Here, you have the option to send the data in three diferent ways: doing a private request, a public request or a private request that uses a saved Credit Card.

    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param transaction_id: 
    :type transaction_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [Model2SendPaymentsWithSavedCreditCardRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def call3_send_additional_data(request: web.Request, x_provider_api_app_key, x_provider_api_app_token, accept, content_type, transaction_id, body) -> web.Response:
    """3. Send Additional Data

    The third step to create a new transaction. It will send the additional related data to the transaction, like billig and shipping adress.

    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param transaction_id: Transaction identification.
    :type transaction_id: str
    :param body: 

    """
    return web.Response(status=200)


async def call4_doauthorization(request: web.Request, x_provider_api_app_key, x_provider_api_app_token, accept, content_type, transaction_id, body) -> web.Response:
    """Do authorization

    The fouth and last step to create a new transaction. It will authorized the new transction creation acorrdint to the data previously informed in the latests requests.

    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param transaction_id: 
    :type transaction_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Model4DoauthorizationRequest.from_dict(body)
    return web.Response(status=200)


async def payment_details(request: web.Request, x_provider_api_app_key, x_provider_api_app_token, content_type, accept, transaction_id, payment_id) -> web.Response:
    """Payment Details

    Returns associated information details for the specified payment id.

    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param transaction_id: 
    :type transaction_id: str
    :param payment_id: 
    :type payment_id: str

    """
    return web.Response(status=200)


async def transaction_details(request: web.Request, x_provider_api_app_key, x_provider_api_app_token, content_type, accept, transaction_id) -> web.Response:
    """Transaction Details

    Returns associated data for the specified transaction id, like value and status, for exemple.

    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param transaction_id: 
    :type transaction_id: str

    """
    return web.Response(status=200)


async def transaction_settlement_details(request: web.Request, x_provider_api_app_key, x_provider_api_app_token, content_type, accept, transaction_id) -> web.Response:
    """Transaction Settlement  Details

    Returns associated settlements data for the specified transaction id.

    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param transaction_id: 
    :type transaction_id: str

    """
    return web.Response(status=200)
