from typing import List, Dict
from aiohttp import web

from openapi_server.models.balance import Balance
from openapi_server.models.prepare_transaction_request import PrepareTransactionRequest
from openapi_server.models.quittung_create_request import QuittungCreateRequest
from openapi_server.models.stromkonto_login200_response import StromkontoLogin200Response
from openapi_server.models.stromkonto_register_request import StromkontoRegisterRequest
from openapi_server import util


async def prepare_transaction(request: web.Request, body) -> web.Response:
    """Prepare Transaction

    Prepares and inques a transaction (transfer) between two accounts (Stromkonten). This might be used to send any balanced entity. Using this endpoint will only prepare the transaction and enques it for signing and countersigning. This is done from within the user UI using validation process. Note: This API method does not validate any transations. In other words authentication, authorization, validation and actual transfer of value is done using a smart contract during processing in the energy blockchain. 

    :param body: 
    :type body: dict | bytes

    """
    body = PrepareTransactionRequest.from_dict(body)
    return web.Response(status=200)


async def stromkonto_balances(request: web.Request, account=None) -> web.Response:
    """Balances

    Stromkonto represents a core component of the Corrently Ecosystem. It is a ledger for green energy related transactions and gets heavily used by the public Web-UI on www.stromkonto.net . Beside of some decoration and reformating operations all data is backed by the [Energychain blockchain](https://github.com/energychain/) to provide consensus of balances and transactions. Use this API Endppoint if you prefere not to work with low level Distributed Ledger Technology (Blockchain). 

    :param account: Ethereum style address referencing a valid account (AKA Stromkonto).
    :type account: str

    """
    return web.Response(status=200)


async def stromkonto_choices(request: web.Request, account=None) -> web.Response:
    """Selectable Choices for customer

    Signable choices (contract changes) for customer. 

    :param account: Ethereum style address referencing a valid account alias (never use Stromkonto directly!).
    :type account: str

    """
    return web.Response(status=200)


async def stromkonto_login(request: web.Request, body) -> web.Response:
    """Login (via Mail)

    Sends a mail to a given email address to login this user. This function makes life a bit easier in order to not having to deal with private key protection on the user side as a shared key is used to sign transactions onbehalf of a particular account.  However viewing consensus information (balances) are public and *might move* from account to account without prior notification. Best practice for third party uses is to always start a session with the login RESP call and only create a user in case the response indicates an &#x60;unregistered&#x60; status. 

    :param body: 
    :type body: dict | bytes

    """
    body = QuittungCreateRequest.from_dict(body)
    return web.Response(status=200)


async def stromkonto_register(request: web.Request, body) -> web.Response:
    """Register (new Stromkonto)

    Calling this method with an unregistered (new) email will create a new account (Stromkonto) with all balances having a value of &#x60;0&#x60; and no transaction history. In addition some basic properties like region and zipcode are set to allow further operation of account. 

    :param body: 
    :type body: dict | bytes

    """
    body = StromkontoRegisterRequest.from_dict(body)
    return web.Response(status=200)
