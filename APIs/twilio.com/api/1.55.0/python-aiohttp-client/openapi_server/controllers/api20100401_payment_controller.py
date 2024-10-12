from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_call_payments import ApiV2010AccountCallPayments
from openapi_server.models.payments_enum_bank_account_type import PaymentsEnumBankAccountType
from openapi_server.models.payments_enum_capture import PaymentsEnumCapture
from openapi_server.models.payments_enum_payment_method import PaymentsEnumPaymentMethod
from openapi_server.models.payments_enum_status import PaymentsEnumStatus
from openapi_server.models.payments_enum_token_type import PaymentsEnumTokenType
from openapi_server import util


async def create_payments(request: web.Request, account_sid, call_sid, idempotency_key, status_callback, bank_account_type=None, charge_amount=None, currency=None, description=None, input=None, min_postal_code_length=None, parameter=None, payment_connector=None, payment_method=None, postal_code=None, security_code=None, timeout=None, token_type=None, valid_card_types=None) -> web.Response:
    """create_payments

    create an instance of payments. This will start a new payments session

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    :type account_sid: str
    :param call_sid: The SID of the call that will create the resource. Call leg associated with this sid is expected to provide payment information thru DTMF.
    :type call_sid: str
    :param idempotency_key: A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated.
    :type idempotency_key: str
    :param status_callback: Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [expected StatusCallback values](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback)
    :type status_callback: str
    :param bank_account_type: 
    :type bank_account_type: str
    :param charge_amount: A positive decimal value less than 1,000,000 to charge against the credit card or bank account. Default currency can be overwritten with &#x60;currency&#x60; field. Leave blank or set to 0 to tokenize.
    :type charge_amount: 
    :param currency: The currency of the &#x60;charge_amount&#x60;, formatted as [ISO 4127](http://www.iso.org/iso/home/standards/currency_codes.htm) format. The default value is &#x60;USD&#x60; and all values allowed from the Pay Connector are accepted.
    :type currency: str
    :param description: The description can be used to provide more details regarding the transaction. This information is submitted along with the payment details to the Payment Connector which are then posted on the transactions.
    :type description: str
    :param input: A list of inputs that should be accepted. Currently only &#x60;dtmf&#x60; is supported. All digits captured during a pay session are redacted from the logs.
    :type input: str
    :param min_postal_code_length: A positive integer that is used to validate the length of the &#x60;PostalCode&#x60; inputted by the user. User must enter this many digits.
    :type min_postal_code_length: int
    :param parameter: A single-level JSON object used to pass custom parameters to payment processors. (Required for ACH payments). The information that has to be included here depends on the &lt;Pay&gt; Connector. [Read more](https://www.twilio.com/console/voice/pay-connectors).
    :type parameter: dict | bytes
    :param payment_connector: This is the unique name corresponding to the Pay Connector installed in the Twilio Add-ons. Learn more about [&lt;Pay&gt; Connectors](https://www.twilio.com/console/voice/pay-connectors). The default value is &#x60;Default&#x60;.
    :type payment_connector: str
    :param payment_method: 
    :type payment_method: str
    :param postal_code: Indicates whether the credit card postal code (zip code) is a required piece of payment information that must be provided by the caller. The default is &#x60;true&#x60;.
    :type postal_code: bool
    :param security_code: Indicates whether the credit card security code is a required piece of payment information that must be provided by the caller. The default is &#x60;true&#x60;.
    :type security_code: bool
    :param timeout: The number of seconds that &lt;Pay&gt; should wait for the caller to press a digit between each subsequent digit, after the first one, before moving on to validate the digits captured. The default is &#x60;5&#x60;, maximum is &#x60;600&#x60;.
    :type timeout: int
    :param token_type: 
    :type token_type: str
    :param valid_card_types: Credit card types separated by space that Pay should accept. The default value is &#x60;visa mastercard amex&#x60;
    :type valid_card_types: str

    """
    parameter = object.from_dict(parameter)
    return web.Response(status=200)


async def update_payments(request: web.Request, account_sid, call_sid, sid, idempotency_key, status_callback, capture=None, status=None) -> web.Response:
    """update_payments

    update an instance of payments with different phases of payment flows.

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will update the resource.
    :type account_sid: str
    :param call_sid: The SID of the call that will update the resource. This should be the same call sid that was used to create payments resource.
    :type call_sid: str
    :param sid: The SID of Payments session that needs to be updated.
    :type sid: str
    :param idempotency_key: A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated.
    :type idempotency_key: str
    :param status_callback: Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [Update](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-update) and [Complete/Cancel](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-cancelcomplete) POST requests.
    :type status_callback: str
    :param capture: 
    :type capture: str
    :param status: 
    :type status: str

    """
    return web.Response(status=200)
