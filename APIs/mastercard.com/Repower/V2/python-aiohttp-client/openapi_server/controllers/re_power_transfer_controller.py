from typing import List, Dict
from aiohttp import web

from openapi_server.models.repower5_wrapper import Repower5Wrapper
from openapi_server.models.repowerrequest1_wrapper import Repowerrequest1Wrapper
from openapi_server import util


async def repower_post2(request: web.Request, repower_request=None) -> web.Response:
    """repower_post2

    Mastercard rePower empowers consumers to instantly add money to eligible Mastercard cards. Money is available immediately for expenditures anywhere Mastercard prepaid account is accepted. The ease with which cardholders can convert cash to prepaid card funds turns their reloadable prepaid cards into valuable and practical financial tools. Making the reload process simple and accessible provides merchants with an opportunity to increase cardholder traffic. Unlike other top-up services, merchants have the flexibility to set their own reload fees.  This resource streamlines development efforts to offer Mastercard rePower services, through quick and convenient web services with the following benefits: 1)Savings in development and operational costs associated with implementing a standard MIP connection.  2)Requires support for only a single acquiring interface.  3)Leverages existing processing messages and transaction codes  4)Mastercard provides a net settlement guarantee for each reload transaction  5)Supports EMV, PayPass &amp; MDES transactions.  This resource facilitates the ability for cardholders to reload their prepaid cards easily and securely.   

    :param repower_request: Contains the details of the repower request message.
    :type repower_request: dict | bytes

    """
    repower_request = Repowerrequest1Wrapper.from_dict(repower_request)
    return web.Response(status=200)
