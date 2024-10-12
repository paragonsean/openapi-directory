# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_accountstatements(client):
    """Test case for accountstatements

    Account statements
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/creditcontrol/accounts/{credit_account_id}/statements'.format(credit_account_id='insert identifier here'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_addanaccount_holder(client):
    """Test case for addanaccount_holder

    Add an account Holder
    """
    body = {"claims":{"email":"USER-EMAIL"}}
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/creditcontrol/accounts/{credit_account_id}/holders'.format(credit_account_id='insert identifier here'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancela_pre_authorization(client):
    """Test case for cancela_pre_authorization

    Cancel a Pre Authorization
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/creditcontrol/accounts/{credit_account_id}/transactions/{transaction_id}'.format(credit_account_id='insert identifier here', transaction_id='insert identifier here'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_changecreditlimitofan_account(client):
    """Test case for changecreditlimitofan_account

    Change credit limit of an Account
    """
    body = {"value":10000}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/creditcontrol/accounts/{credit_account_id}/creditlimit'.format(credit_account_id='insert identifier here'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_changetoleranceofanaccount(client):
    """Test case for changetoleranceofanaccount

    Change tolerance of an account
    """
    body = {"value":0.2}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/creditcontrol/accounts/{credit_account_id}/tolerance'.format(credit_account_id='insert identifier here'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_closean_account(client):
    """Test case for closean_account

    Close an Account
    """
    body = {"document":"number","documentType":"CPF ou CNPJ ou Other","email":"email"}
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/creditcontrol/accounts/{credit_account_id}'.format(credit_account_id='insert identifier here'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_createa_pre_authorization(client):
    """Test case for createa_pre_authorization

    Create a Pre Authorization
    """
    body = {"expirationDate":"date in ISO8601 (UTC) dateformat (optional default is 1(one) day)","installments":"integer (optional default is 1)","settle":false,"value":"decimal (required)"}
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/creditcontrol/accounts/{credit_account_id}/transaction'.format(credit_account_id='insert identifier here'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_createa_pre_authorization_usingid(client):
    """Test case for createa_pre_authorization_usingid

    Create a Pre Authorization (using id)
    """
    body = {"expirationDate":"date in ISO8601 (UTC) dateformat (optional default is 1(one) day)","installments":"integer (optional default is 1)","settle":False,"value":"decimal (required)"}
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/creditcontrol/accounts/{credit_account_id}/transactions/{transaction_id}'.format(credit_account_id='insert identifier here', transaction_id='insert identifier here'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_createor_update_settlement(client):
    """Test case for createor_update_settlement

    Create or Update Settlement
    """
    body = {"value":"decimal (required)"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/creditcontrol/accounts/{credit_account_id}/transactions/{transaction_id}/settlement'.format(credit_account_id='insert identifier here', transaction_id='insert identifier here'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_decreasebalanceofanaccount(client):
    """Test case for decreasebalanceofanaccount

    Decrease balance of an account
    """
    body = {"value":"-number"}
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/creditcontrol/accounts/{credit_account_id}/statements/{statement_id}'.format(credit_account_id='insert example here', statement_id='insert example here'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deleteanaccountholder(client):
    """Test case for deleteanaccountholder

    Delete an account holder
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/creditcontrol/accounts/{credit_account_id}/holders/{holder_id}'.format(credit_account_id='insert identifier here', holder_id='insert identifier here'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_openan_account(client):
    """Test case for openan_account

    Open an Account
    """
    body = {"creditLimit":"number","description":"description","document":"number","documentType":"CPF ou CNPJ ou Other","email":"email","tolerance":"1 is 100%"}
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/creditcontrol/accounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_openor_change_account(client):
    """Test case for openor_change_account

    Open or Change Account
    """
    body = {"creditLimit":"number","email":"email"}
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/creditcontrol/accounts/{account_id}'.format(account_id='insert identifier here'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_partialor_total_refunda_settlement(client):
    """Test case for partialor_total_refunda_settlement

    Partial or Total Refund a Settlement
    """
    body = {"value":"decimal (required)"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/creditcontrol/accounts/{credit_account_id}/transactions/{transaction_id}/refunds'.format(credit_account_id='insert identifier here', transaction_id='insert identifier here'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrievea_accountby_id(client):
    """Test case for retrievea_accountby_id

    Retrieve an Account by Id
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/creditcontrol/accounts/{credit_account_id}'.format(credit_account_id='insert identifier here'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_searchallaccounts(client):
    """Test case for searchallaccounts

    Search all accounts
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/creditcontrol/accounts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_updateemailanddescriptionofaaccount(client):
    """Test case for updateemailanddescriptionofaaccount

    Update email and description of a account
    """
    body = {"description":"string","email":"email"}
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/creditcontrol/accounts/{credit_account_id}'.format(credit_account_id='insert identifier here'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

