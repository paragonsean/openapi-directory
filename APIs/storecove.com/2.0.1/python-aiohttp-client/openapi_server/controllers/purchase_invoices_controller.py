from typing import List, Dict
from aiohttp import web

from openapi_server.models.purchase_invoice import PurchaseInvoice
from openapi_server.models.purchase_invoice_ubl import PurchaseInvoiceUbl
from openapi_server import util


async def get_invoice_json(request: web.Request, guid, pmv=None) -> web.Response:
    """Get Purchase invoice data as JSON

    Get a specific PurchaseInvoice, in JSON format.

    :param guid: The guid of the purchase invoice, from the webhook.
    :type guid: str
    :type guid: str
    :param pmv: The PaymentMeans version. The default (and deprecated) version 1.0 will give BankPaymentMean, DirectDebitPaymentMean, CardPaymentMean, NppPaymentMean, SeBankGiroPaymentMean, SePlusGiroPaymentMean, SgCardPaymentMean, SgGiroPaymentMean, SgPaynowPaymentMean.  Version 2.0 deprecates BankPaymentMean (now CreditTransferPaymentMean), CardPaymentMean (now CreditCardPaymentMean), NppPaymentMean (now AunzNppPayidPaymentMean), SeBankGiroPaymentMean (now SeBankgiroPaymentMean  -- note the lower &#39;g&#39; in &#39;bankgiro&#39;). It also adds OnlinePaymentServicePaymentMean, StandingAgreementPaymentMean, AunzNppPaytoPaymentMean, AunzBpayPaymentMean, AunzPostbillpayPaymentMean, AunzUriPaymentMean.
    :type pmv: str

    """
    return web.Response(status=200)


async def get_invoice_ubl(request: web.Request, guid, packaging, pmv=None) -> web.Response:
    """Get Purchase invoice data in a selectable format

    Get a specific PurchaseInvoice.

    :param guid: purchase invoice guid
    :type guid: str
    :type guid: str
    :param packaging: How to package the purchase invoice.
    :type packaging: str
    :param pmv: The PaymentMeans version. The default (and deprecated) version 1.0 will give BankPaymentMean, DirectDebitPaymentMean, CardPaymentMean, NppPaymentMean, SeBankGiroPaymentMean, SePlusGiroPaymentMean, SgCardPaymentMean, SgGiroPaymentMean, SgPaynowPaymentMean.  Version 2.0 deprecates BankPaymentMean (now CreditTransferPaymentMean), CardPaymentMean (now CreditCardPaymentMean), NppPaymentMean (now AunzNppPayidPaymentMean), SeBankGiroPaymentMean (now SeBankgiroPaymentMean  -- note the lower &#39;g&#39; in &#39;bankgiro&#39;). It also adds OnlinePaymentServicePaymentMean, StandingAgreementPaymentMean, AunzNppPaytoPaymentMean, AunzBpayPaymentMean, AunzPostbillpayPaymentMean, AunzUriPaymentMean.
    :type pmv: str

    """
    return web.Response(status=200)


async def get_invoice_ubl_versioned(request: web.Request, guid, packaging, package_version) -> web.Response:
    """Get Purchase invoice data as JSON with a Base64-encoded UBL string in the specified version

    Get a specific PurchaseInvoice in UBL format

    :param guid: purchase invoice guid
    :type guid: str
    :type guid: str
    :param packaging: How to package the purchase invoice.
    :type packaging: str
    :param package_version: The version of the package.
    :type package_version: str

    """
    return web.Response(status=200)
