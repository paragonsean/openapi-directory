from typing import List, Dict
from aiohttp import web

from openapi_server.models.admin_request import AdminRequest
from openapi_server.models.admin_response import AdminResponse
from openapi_server.models.balance_inquiry_request import BalanceInquiryRequest
from openapi_server.models.balance_inquiry_response import BalanceInquiryResponse
from openapi_server.models.card_acquisition_request import CardAcquisitionRequest
from openapi_server.models.card_acquisition_response import CardAcquisitionResponse
from openapi_server.models.card_reader_apdu_request import CardReaderAPDURequest
from openapi_server.models.card_reader_apdu_response import CardReaderAPDUResponse
from openapi_server.models.diagnosis_request import DiagnosisRequest
from openapi_server.models.diagnosis_response import DiagnosisResponse
from openapi_server.models.display_request import DisplayRequest
from openapi_server.models.display_response import DisplayResponse
from openapi_server.models.enable_service_request import EnableServiceRequest
from openapi_server.models.enable_service_response import EnableServiceResponse
from openapi_server.models.get_totals_request import GetTotalsRequest
from openapi_server.models.get_totals_response import GetTotalsResponse
from openapi_server.models.input_request import InputRequest
from openapi_server.models.input_response import InputResponse
from openapi_server.models.login_request import LoginRequest
from openapi_server.models.login_response import LoginResponse
from openapi_server.models.logout_request import LogoutRequest
from openapi_server.models.logout_response import LogoutResponse
from openapi_server.models.loyalty_request import LoyaltyRequest
from openapi_server.models.loyalty_response import LoyaltyResponse
from openapi_server.models.payment_request import PaymentRequest
from openapi_server.models.payment_response import PaymentResponse
from openapi_server.models.print_request import PrintRequest
from openapi_server.models.print_response import PrintResponse
from openapi_server.models.reconciliation_request import ReconciliationRequest
from openapi_server.models.reconciliation_response import ReconciliationResponse
from openapi_server.models.reversal_request import ReversalRequest
from openapi_server.models.reversal_response import ReversalResponse
from openapi_server.models.stored_value_request import StoredValueRequest
from openapi_server.models.stored_value_response import StoredValueResponse
from openapi_server.models.transaction_status_request import TransactionStatusRequest
from openapi_server.models.transaction_status_response import TransactionStatusResponse
from openapi_server import util


async def admin_post(request: web.Request, body=None) -> web.Response:
    """Admin Request

    Empty. Content of the Custom Admin Request message.

    :param body: 
    :type body: dict | bytes

    """
    body = AdminRequest.from_dict(body)
    return web.Response(status=200)


async def balanceinquiry_post(request: web.Request, body=None) -> web.Response:
    """BalanceInquiry Request

    It conveys Information related to the account for which a Balance Inquiry is requested. Content of the Balance Inquiry Request message.

    :param body: 
    :type body: dict | bytes

    """
    body = BalanceInquiryRequest.from_dict(body)
    return web.Response(status=200)


async def cardacquisition_post(request: web.Request, body=None) -> web.Response:
    """CardAcquisition Request

    It conveys Information related to the payment and loyalty cards to read and analyse. This message pair is usually followed by a message pair (e.g. payment or loyalty) which refers to this Card Acquisition message pair. Content of the Card Acquisition Request message.

    :param body: 
    :type body: dict | bytes

    """
    body = CardAcquisitionRequest.from_dict(body)
    return web.Response(status=200)


async def cardreaderapdu_post(request: web.Request, body=None) -> web.Response:
    """CardReaderAPDU Request

    It contains the APDU request to send to the chip of the card, and a possible invitation message to display on the CashierInterface or the CustomerInterface. Content of the Card Reader APDU Request message.

    :param body: 
    :type body: dict | bytes

    """
    body = CardReaderAPDURequest.from_dict(body)
    return web.Response(status=200)


async def diagnosis_post(request: web.Request, body=None) -> web.Response:
    """Diagnosis Request

    It conveys Information related to the target POI for which the diagnosis is requested. Content of the Diagnosis Request message.

    :param body: 
    :type body: dict | bytes

    """
    body = DiagnosisRequest.from_dict(body)
    return web.Response(status=200)


async def display_post(request: web.Request, body=None) -> web.Response:
    """Display Request

    It conveys the data to display and the way to process the display. It contains the complete content to display. It might contain an operation (the DisplayOutput element) per Display Device type. Content of the Display Request message.

    :param body: 
    :type body: dict | bytes

    """
    body = DisplayRequest.from_dict(body)
    return web.Response(status=200)


async def enableservice_post(request: web.Request, body=None) -> web.Response:
    """EnableService Request

    It conveys the services that will be enabled for the  POI Terminal without the request of the Sale System, and a possible invitation for the Customer to start the services. Content of the Enable Service Request message.

    :param body: 
    :type body: dict | bytes

    """
    body = EnableServiceRequest.from_dict(body)
    return web.Response(status=200)


async def gettotals_post(request: web.Request, body=None) -> web.Response:
    """GetTotals Request

    It conveys information from the Sale System related to the scope and the format of the totals to be computed by the POI System. Content of the Get Totals Request message.

    :param body: 
    :type body: dict | bytes

    """
    body = GetTotalsRequest.from_dict(body)
    return web.Response(status=200)


async def input_post(request: web.Request, body=None) -> web.Response:
    """Input Request

    It conveys data to display and the way to process the display, and contains the complete content to display. In addition to the display on the Input Device, it might contain an operation (the DisplayOutput element) per Display Device type. Content of the Input Request message.

    :param body: 
    :type body: dict | bytes

    """
    body = InputRequest.from_dict(body)
    return web.Response(status=200)


async def login_post(request: web.Request, body=None) -> web.Response:
    """Login Request

    It conveys Information related to the session (period between a Login and the following Logout) to process. Content of the Login Request message.

    :param body: 
    :type body: dict | bytes

    """
    body = LoginRequest.from_dict(body)
    return web.Response(status=200)


async def logout_post(request: web.Request, body=None) -> web.Response:
    """Logout Request

    Empty. Content of the Logout Request message.

    :param body: 
    :type body: dict | bytes

    """
    body = LogoutRequest.from_dict(body)
    return web.Response(status=200)


async def loyalty_post(request: web.Request, body=None) -> web.Response:
    """Loyalty Request

    It conveys Information related to the Loyalty transaction to process. Content of the Loyalty Request message.

    :param body: 
    :type body: dict | bytes

    """
    body = LoyaltyRequest.from_dict(body)
    return web.Response(status=200)


async def payment_post(request: web.Request, body=None) -> web.Response:
    """Payment Request

    Request sent to terminal to initiate payment.  It conveys Information related to the Payment transaction to process. Content of the Payment Request message.

    :param body: 
    :type body: dict | bytes

    """
    body = PaymentRequest.from_dict(body)
    return web.Response(status=200)


async def print_post(request: web.Request, body=None) -> web.Response:
    """Print Request

    It conveys the data to print and the way to process the print. It contains the complete content to print. Content of the Print Request message.

    :param body: 
    :type body: dict | bytes

    """
    body = PrintRequest.from_dict(body)
    return web.Response(status=200)


async def reconciliation_post(request: web.Request, body=None) -> web.Response:
    """Reconciliation Request

    It conveys Information related to the Reconciliation requested by the Sale System. Content of the Reconciliation Request message.

    :param body: 
    :type body: dict | bytes

    """
    body = ReconciliationRequest.from_dict(body)
    return web.Response(status=200)


async def reversal_post(request: web.Request, body=None) -> web.Response:
    """Reversal Request

    It conveys Information related to the reversal of a previous payment or a loyalty transaction. Content of the Reversal Request message.

    :param body: 
    :type body: dict | bytes

    """
    body = ReversalRequest.from_dict(body)
    return web.Response(status=200)


async def storedvalue_post(request: web.Request, body=None) -> web.Response:
    """StoredValue Request

    It conveys Information related to the Stored Value transaction to process. Content of the Stored Value Request message.

    :param body: 
    :type body: dict | bytes

    """
    body = StoredValueRequest.from_dict(body)
    return web.Response(status=200)


async def transactionstatus_post(request: web.Request, body=None) -> web.Response:
    """TransactionStatus Request

    It conveys Information requested for status of the last or current Payment, Loyalty or Reversal transaction. Content of the TransactionStatus Request message.

    :param body: 
    :type body: dict | bytes

    """
    body = TransactionStatusRequest.from_dict(body)
    return web.Response(status=200)
