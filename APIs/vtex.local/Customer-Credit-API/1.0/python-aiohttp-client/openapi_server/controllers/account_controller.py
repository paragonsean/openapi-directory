from typing import List, Dict
from aiohttp import web

from openapi_server.models.addanaccount_holder_request1 import AddanaccountHolderRequest1
from openapi_server.models.changecreditlimitofan_account_request1 import ChangecreditlimitofanAccountRequest1
from openapi_server.models.changetoleranceofanaccount_request1 import ChangetoleranceofanaccountRequest1
from openapi_server.models.closean_account_request1 import CloseanAccountRequest1
from openapi_server.models.createa_pre_authorization_request1 import CreateaPreAuthorizationRequest1
from openapi_server.models.createa_pre_authorization_usingid_request import CreateaPreAuthorizationUsingidRequest
from openapi_server.models.createor_update_settlement_request1 import CreateorUpdateSettlementRequest1
from openapi_server.models.decreasebalanceofanaccount_request1 import DecreasebalanceofanaccountRequest1
from openapi_server.models.getaccount1 import Getaccount1
from openapi_server.models.openan_account_request1 import OpenanAccountRequest1
from openapi_server.models.openor_change_account_request1 import OpenorChangeAccountRequest1
from openapi_server.models.partialor_total_refunda_settlement_request1 import PartialorTotalRefundaSettlementRequest1
from openapi_server.models.searchaccounts1 import Searchaccounts1
from openapi_server.models.searchcheckingaccounts1 import Searchcheckingaccounts1
from openapi_server.models.statements1 import Statements1
from openapi_server.models.thisoperationcausesthecreationof_ninvoices_where_nisthenumberofinstallments_thefirstinvoicewillhaveaduedatewith30daysandthenextinvoiceswillhaveaduedate30daysawayfrompreviousinvoice import ThisoperationcausesthecreationofNinvoicesWhereNisthenumberofinstallmentsThefirstinvoicewillhaveaduedatewith30daysandthenextinvoiceswillhaveaduedate30daysawayfrompreviousinvoice
from openapi_server.models.updateemailanddescriptionofaaccount_request1 import UpdateemailanddescriptionofaaccountRequest1
from openapi_server import util


async def accountstatements(request: web.Request, content_type, accept, credit_account_id) -> web.Response:
    """Account statements

    Get the account statements.

    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param credit_account_id: 
    :type credit_account_id: str

    """
    return web.Response(status=200)


async def addanaccount_holder(request: web.Request, credit_account_id, accept, content_type, body) -> web.Response:
    """Add an account Holder

    

    :param credit_account_id: Credit account&#39;s identification
    :type credit_account_id: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddanaccountHolderRequest1.from_dict(body)
    return web.Response(status=200)


async def cancela_pre_authorization(request: web.Request, content_type, accept, credit_account_id, transaction_id) -> web.Response:
    """Cancel a Pre Authorization

    

    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param credit_account_id: Credit account&#39;s identification
    :type credit_account_id: str
    :param transaction_id: 
    :type transaction_id: str

    """
    return web.Response(status=200)


async def changecreditlimitofan_account(request: web.Request, credit_account_id, accept, content_type, body) -> web.Response:
    """Change credit limit of an Account

    Increase the credit limit of an account.

    :param credit_account_id: Credit account&#39;s identifier
    :type credit_account_id: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChangecreditlimitofanAccountRequest1.from_dict(body)
    return web.Response(status=200)


async def changetoleranceofanaccount(request: web.Request, credit_account_id, accept, content_type, body) -> web.Response:
    """Change tolerance of an account

    Increase the credit limit of a checking account.

    :param credit_account_id: Credit account&#39;s identification
    :type credit_account_id: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChangetoleranceofanaccountRequest1.from_dict(body)
    return web.Response(status=200)


async def closean_account(request: web.Request, credit_account_id, accept, content_type, body) -> web.Response:
    """Close an Account

    Closes an account.

    :param credit_account_id: Credit account&#39;s identifier
    :type credit_account_id: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = CloseanAccountRequest1.from_dict(body)
    return web.Response(status=200)


async def createa_pre_authorization(request: web.Request, credit_account_id, accept, content_type, body) -> web.Response:
    """Create a Pre Authorization

    

    :param credit_account_id: Credit account&#39;s identification
    :type credit_account_id: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateaPreAuthorizationRequest1.from_dict(body)
    return web.Response(status=200)


async def createa_pre_authorization_usingid(request: web.Request, credit_account_id, transaction_id, accept, content_type, body) -> web.Response:
    """Create a Pre Authorization (using id)

    

    :param credit_account_id: Credit account&#39;s identification
    :type credit_account_id: str
    :param transaction_id: 
    :type transaction_id: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateaPreAuthorizationUsingidRequest.from_dict(body)
    return web.Response(status=200)


async def createor_update_settlement(request: web.Request, credit_account_id, transaction_id, accept, content_type, body) -> web.Response:
    """Create or Update Settlement

    Debit a value from checking account.

    :param credit_account_id: Credit account&#39;s identification
    :type credit_account_id: str
    :param transaction_id: 
    :type transaction_id: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateorUpdateSettlementRequest1.from_dict(body)
    return web.Response(status=200)


async def decreasebalanceofanaccount(request: web.Request, credit_account_id, statement_id, accept, content_type, body) -> web.Response:
    """Decrease balance of an account

    Create a debit value updating the account BALANCE.

    :param credit_account_id: Credit account&#39;s identification
    :type credit_account_id: str
    :param statement_id: 
    :type statement_id: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = DecreasebalanceofanaccountRequest1.from_dict(body)
    return web.Response(status=200)


async def deleteanaccountholder(request: web.Request, content_type, accept, credit_account_id, holder_id) -> web.Response:
    """Delete an account holder

    

    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param credit_account_id: Credit account&#39;s identification
    :type credit_account_id: str
    :param holder_id: 
    :type holder_id: str

    """
    return web.Response(status=200)


async def openan_account(request: web.Request, accept, content_type, body) -> web.Response:
    """Open an Account

    Open an account.

    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = OpenanAccountRequest1.from_dict(body)
    return web.Response(status=200)


async def openor_change_account(request: web.Request, account_id, accept, content_type, body=None) -> web.Response:
    """Open or Change Account

    Open or Change an account.

    :param account_id: It must be an alphanumeric value
    :type account_id: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = OpenorChangeAccountRequest1.from_dict(body)
    return web.Response(status=200)


async def partialor_total_refunda_settlement(request: web.Request, credit_account_id, transaction_id, accept, content_type, body) -> web.Response:
    """Partial or Total Refund a Settlement

    Refund a value from a already settled transaction.

    :param credit_account_id: Credit account&#39;s identification
    :type credit_account_id: str
    :param transaction_id: 
    :type transaction_id: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PartialorTotalRefundaSettlementRequest1.from_dict(body)
    return web.Response(status=200)


async def retrievea_accountby_id(request: web.Request, content_type, accept, credit_account_id) -> web.Response:
    """Retrieve an Account by Id

    Retrieve an account by id.

    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param credit_account_id: 
    :type credit_account_id: str

    """
    return web.Response(status=200)


async def searchallaccounts(request: web.Request, content_type, accept) -> web.Response:
    """Search all accounts

    

    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str

    """
    return web.Response(status=200)


async def updateemailanddescriptionofaaccount(request: web.Request, credit_account_id, accept, content_type, body) -> web.Response:
    """Update email and description of a account

    Update a checking account.

    :param credit_account_id: Credit account&#39;s identification
    :type credit_account_id: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateemailanddescriptionofaaccountRequest1.from_dict(body)
    return web.Response(status=200)
