from typing import List, Dict
from aiohttp import web

from openapi_server.models.ardef_request import ArdefRequest
from openapi_server.models.ardef_response import ArdefResponse
from openapi_server.models.pg_api_bad_response import PGApiBadResponse
from openapi_server.models.pg_api_batch_close_request import PGApiBatchCloseRequest
from openapi_server.models.pg_api_batch_close_response import PGApiBatchCloseResponse
from openapi_server.models.pg_api_capture_request import PGApiCaptureRequest
from openapi_server.models.pg_api_capture_response import PGApiCaptureResponse
from openapi_server.models.pg_api_decline_response import PGApiDeclineResponse
from openapi_server.models.pg_api_email_receipt_request import PGApiEmailReceiptRequest
from openapi_server.models.pg_api_email_receipt_response import PGApiEmailReceiptResponse
from openapi_server.models.pg_api_expire_token_request import PGApiExpireTokenRequest
from openapi_server.models.pg_api_expire_token_response import PGApiExpireTokenResponse
from openapi_server.models.pg_api_internal_error_response import PGApiInternalErrorResponse
from openapi_server.models.pg_api_recharge_request import PGApiRechargeRequest
from openapi_server.models.pg_api_recharge_response import PGApiRechargeResponse
from openapi_server.models.pg_api_refund_request import PGApiRefundRequest
from openapi_server.models.pg_api_refund_response import PGApiRefundResponse
from openapi_server.models.pg_api_response import PGApiResponse
from openapi_server.models.pg_api_timeout_response import PGApiTimeoutResponse
from openapi_server.models.pg_api_tokenize_request import PGApiTokenizeRequest
from openapi_server.models.pg_api_tokenize_response import PGApiTokenizeResponse
from openapi_server.models.pg_api_transaction_request import PGApiTransactionRequest
from openapi_server.models.pg_api_transaction_response import PGApiTransactionResponse
from openapi_server.models.pg_api_unauth_response import PGApiUnauthResponse
from openapi_server.models.pg_api_verify_request import PGApiVerifyRequest
from openapi_server.models.pg_api_verify_response import PGApiVerifyResponse
from openapi_server.models.pg_api_void_request import PGApiVoidRequest
from openapi_server.models.pg_api_void_response import PGApiVoidResponse
from openapi_server import util


async def authorization(request: web.Request, body) -> web.Response:
    """Authorize Transaction

    Authorizes a credit card for capture at a later time. An authorized transaction will continue to be open until it expires or a capture message is received. Authorizations are automatically voided if they are not captured within 28 days, although most issuing banks will release the hold after 24 hours in retail environments or 7 days in card not present environments.

    :param body: Payment Gateway Authorization Request
    :type body: dict | bytes

    """
    body = PGApiTransactionRequest.from_dict(body)
    return web.Response(status=200)


async def batch_close(request: web.Request, body) -> web.Response:
    """Close Batch

    Closes a batch. Use this request when the timing of the batch close needs to be controlled rather than relying on the once-daily automatic batch close which is 9 PM Pacific by default, and can be changed in the Qualpay Manager administration settings.

    :param body: Payment Gateway Batch Close Request
    :type body: dict | bytes

    """
    body = PGApiBatchCloseRequest.from_dict(body)
    return web.Response(status=200)


async def capture(request: web.Request, pg_id_orig, body) -> web.Response:
    """Capture an Authorized Transaction

    Captures an authorized transaction for any amount up to the amount originally authorized. An authorized transaction can only be captured once.

    :param pg_id_orig: pgIdOrig
    :type pg_id_orig: str
    :param body: Payment Gateway Capture Request
    :type body: dict | bytes

    """
    body = PGApiCaptureRequest.from_dict(body)
    return web.Response(status=200)


async def credit(request: web.Request, body) -> web.Response:
    """Issue Credit to Cardholder

    Issues an unlinked credit. Credit requests require that the cardholder data is  provided in the request. Credits are only available during the first 30 days of account opening unless you contact Qualpay support to make other arrangements. The refund request should generally be used to return money to the cardholder, as it is a reversal of a previously captured transaction. A refund request is linked to the original transaction which is helpful for reconciliation purposes.

    :param body: Payment Gateway Credit Request
    :type body: dict | bytes

    """
    body = PGApiTransactionRequest.from_dict(body)
    return web.Response(status=200)


async def expire(request: web.Request, body) -> web.Response:
    """Expire Token

    Once expired, the token (card_id) is no longer valid for use in future transactions.

    :param body: Payment Gateway Expire Token Request
    :type body: dict | bytes

    """
    body = PGApiExpireTokenRequest.from_dict(body)
    return web.Response(status=200)


async def force(request: web.Request, body) -> web.Response:
    """Force Transaction Approval

    Forces an approval, used when an online authorization request received a &#39;declined&#39; reason code and you have received an authorization from a voice or automated response (ARU) system. The required fields are the same as a sale or authorization request, except that the expiration date (exp_date) is not required, and the 6-character authorization code (auth_code) is required.

    :param body: Payment Gateway Force Request
    :type body: dict | bytes

    """
    body = PGApiTransactionRequest.from_dict(body)
    return web.Response(status=200)


async def get_card_type_information(request: web.Request, body) -> web.Response:
    """Get Card type Information for Visa, Mastercard, and Discover

    Gets Card type information for Visa, Mastercard, and Discover. Useful if you prohibit or allow certain activity based on card type. For example, you may not want to allow a subscription to be created using a prepaid card.

    :param body: Card Type Request
    :type body: dict | bytes

    """
    body = ArdefRequest.from_dict(body)
    return web.Response(status=200)


async def recharge(request: web.Request, pg_id_orig, body) -> web.Response:
    """Recharge Previously Settled Transaction

    Creates a new sale transaction using the cardholder data from a previous successful transaction.

    :param pg_id_orig: pgIdOrig
    :type pg_id_orig: str
    :param body: Payment Gateway Recharge Request
    :type body: dict | bytes

    """
    body = PGApiRechargeRequest.from_dict(body)
    return web.Response(status=200)


async def refund(request: web.Request, pg_id_orig, body) -> web.Response:
    """Refund Previously Captured Transaction

    Returns money to the cardholder from a previously captured transaction. Multiple refunds are allowed per captured transaction, provided that the sum of all refunds does not exceed the original captured transaction amount. Authorizations that have not been captured are not eligible for a refund.

    :param pg_id_orig: pgIdOrig
    :type pg_id_orig: str
    :param body: Payment Gateway Refund Request
    :type body: dict | bytes

    """
    body = PGApiRefundRequest.from_dict(body)
    return web.Response(status=200)


async def sale(request: web.Request, body) -> web.Response:
    """Sale (Auth + Capture)

    Requests authorization, and, if approved, will immediately capture the transaction to be included in the next batch close. This transaction type is used in card-present environments, and also card-not-present environments where no physical goods are being shipped.

    :param body: Payment Gateway Sale Request
    :type body: dict | bytes

    """
    body = PGApiTransactionRequest.from_dict(body)
    return web.Response(status=200)


async def send_receipt(request: web.Request, pg_id, body) -> web.Response:
    """Send Transaction Receipt Email

    Sends the transaction receipt to multiple email addresses. Receipts can be sent only for successful transactions.

    :param pg_id: pgId
    :type pg_id: str
    :param body: Payment Gateway Email Receipt Request
    :type body: dict | bytes

    """
    body = PGApiEmailReceiptRequest.from_dict(body)
    return web.Response(status=200)


async def tokenize(request: web.Request, body) -> web.Response:
    """Tokenize Card

    Once stored, a unique card_id is returned for use in future transactions. Optionally, tokenization can be requested in an authorization, verify, force, credit, or sale request by sending the tokenize field set to true.

    :param body: Payment Gateway Tokenize Request
    :type body: dict | bytes

    """
    body = PGApiTokenizeRequest.from_dict(body)
    return web.Response(status=200)


async def verify(request: web.Request, body) -> web.Response:
    """Verify Card

    A verify request will return success if the cardholder information was verified by the issuer. If AVS or CVV data is included in the message, then the AVS or CVV result code will be returned in the response message. This is useful if you want to determine if you have been presented with a valid card, but are not ready to authorize the card.

    :param body: Payment Gateway Card Verify Request
    :type body: dict | bytes

    """
    body = PGApiVerifyRequest.from_dict(body)
    return web.Response(status=200)


async def void(request: web.Request, pg_id_orig, body) -> web.Response:
    """Void a Previously Authorized Transaction

    Authorizations can be voided at any time until Qualpay automatically voids them at 28 days. Captured transactions can be voided until the batch is closed. If your batch closes and you did not void the transaction in time, you may make a refund request.

    :param pg_id_orig: pgIdOrig
    :type pg_id_orig: str
    :param body: Payment Gateway Void Request
    :type body: dict | bytes

    """
    body = PGApiVoidRequest.from_dict(body)
    return web.Response(status=200)
