# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_holding_model import AccountHoldingModel
from openapi_server.models.account_holding_with_id_model import AccountHoldingWithIdModel
from openapi_server.models.account_holdings_model import AccountHoldingsModel
from openapi_server.models.account_holdings_without_id_model import AccountHoldingsWithoutIdModel
from openapi_server.models.account_model import AccountModel
from openapi_server.models.account_with_id_model import AccountWithIdModel
from openapi_server.models.accounts_model import AccountsModel
from openapi_server.models.savings_strategies_model import SavingsStrategiesModel
from openapi_server.models.savings_strategy_model import SavingsStrategyModel
from openapi_server.models.savings_strategy_with_id_model import SavingsStrategyWithIdModel


pytestmark = pytest.mark.asyncio

async def test_accounts_delete_account_by_id(client):
    """Test case for accounts_delete_account_by_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/Accounts/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_delete_account_holding_by_accountid_id(client):
    """Test case for accounts_delete_account_holding_by_accountid_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/Accounts/{account_id}/Holdings/{id}'.format(account_id=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_delete_savings_strategies_by_accountid(client):
    """Test case for accounts_delete_savings_strategies_by_accountid

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/Accounts/{account_id}/SavingsStrategies'.format(account_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_delete_savings_strategy_by_accountid_id(client):
    """Test case for accounts_delete_savings_strategy_by_accountid_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/Accounts/{account_id}/SavingsStrategies/{id}'.format(account_id=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_get_account_holding_by_accountid_id(client):
    """Test case for accounts_get_account_holding_by_accountid_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Accounts/{account_id}/Holdings/{id}'.format(account_id=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_get_account_holdings_by_accountid(client):
    """Test case for accounts_get_account_holdings_by_accountid

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Accounts/{account_id}/Holdings'.format(account_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_get_accounts_by_fact_finder_id_by_factfinderid_externalsourceid(client):
    """Test case for accounts_get_accounts_by_fact_finder_id_by_factfinderid_externalsourceid

    
    """
    params = [('factFinderId', 56),
                    ('externalSourceId', 'external_source_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_get_by_id(client):
    """Test case for accounts_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Accounts/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_get_savings_strategies_by_account_id_and_savings_strategy_id_by_accountid_id(client):
    """Test case for accounts_get_savings_strategies_by_account_id_and_savings_strategy_id_by_accountid_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Accounts/{account_id}/SavingsStrategies/{id}'.format(account_id=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_get_savings_strategies_by_account_id_by_accountid(client):
    """Test case for accounts_get_savings_strategies_by_account_id_by_accountid

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Accounts/{account_id}/SavingsStrategies'.format(account_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_accounts_post_account_holding_by_accountid_model(client):
    """Test case for accounts_post_account_holding_by_accountid_model

    
    """
    model = {"symbol":"symbol","cusip":"cusip","valuationDate":"2000-01-23T04:56:07.000+00:00","costBasis":0.8008281904610115,"description":"description","marketValue":6.027456183070403,"externalDestinationId":"externalDestinationId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/Accounts/{account_id}/Holdings'.format(account_id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_accounts_post_by_model(client):
    """Test case for accounts_post_by_model

    
    """
    model = {"owner":"Client","lastUpdated":"2000-01-23T04:56:07.000+00:00","externalSourceName":"externalSourceName","factFinderId":6,"accountType":0,"description":"description","marketValue":1.4658129805029452,"externalSourceId":"externalSourceId","ownerDependentId":5,"externalDestinationId":"externalDestinationId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/Accounts',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_accounts_post_savings_strategy_by_accountid_savingsstrategy(client):
    """Test case for accounts_post_savings_strategy_by_accountid_savingsstrategy

    
    """
    savings_strategy = {"employerSavingsAmount":0.8008281904610115,"frequencyId":6,"postTaxSavingsAmount":5.962133916683182,"preTaxSavingsAmount":5.637376656633329,"endDate":"2000-01-23T04:56:07.000+00:00","postTaxSavingsAmountType":"Dollar","mandatoryAmount":1.4658129805029452,"externalDestinationId":"externalDestinationId","preTaxSavingsAmountType":"Dollar","mandatoryAmountType":"Dollar","startDate":"2000-01-23T04:56:07.000+00:00","employerSavingsAmountType":"Dollar"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/Accounts/{account_id}/SavingsStrategies'.format(account_id=56),
        headers=headers,
        json=savings_strategy,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_accounts_put_by_accountid_id_holding(client):
    """Test case for accounts_put_by_accountid_id_holding

    
    """
    holding = {"symbol":"symbol","cusip":"cusip","valuationDate":"2000-01-23T04:56:07.000+00:00","costBasis":0.8008281904610115,"description":"description","marketValue":6.027456183070403,"externalDestinationId":"externalDestinationId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/Accounts/{account_id}/Holdings/{id}'.format(account_id=56, id=56),
        headers=headers,
        json=holding,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_accounts_put_by_id_model(client):
    """Test case for accounts_put_by_id_model

    
    """
    model = {"owner":"Client","lastUpdated":"2000-01-23T04:56:07.000+00:00","externalSourceName":"externalSourceName","factFinderId":6,"accountType":0,"description":"description","marketValue":1.4658129805029452,"externalSourceId":"externalSourceId","ownerDependentId":5,"externalDestinationId":"externalDestinationId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/Accounts/{id}'.format(id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_accounts_put_holdings_by_accountid_holdings(client):
    """Test case for accounts_put_holdings_by_accountid_holdings

    
    """
    holdings = {"holdings":[{"symbol":"symbol","cusip":"cusip","valuationDate":"2000-01-23T04:56:07.000+00:00","costBasis":0.8008281904610115,"description":"description","marketValue":6.027456183070403,"externalDestinationId":"externalDestinationId"},{"symbol":"symbol","cusip":"cusip","valuationDate":"2000-01-23T04:56:07.000+00:00","costBasis":0.8008281904610115,"description":"description","marketValue":6.027456183070403,"externalDestinationId":"externalDestinationId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/Accounts/{account_id}/Holdings'.format(account_id=56),
        headers=headers,
        json=holdings,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_accounts_put_savings_strategy_by_accountid_id_savingsstrategy(client):
    """Test case for accounts_put_savings_strategy_by_accountid_id_savingsstrategy

    
    """
    savings_strategy = {"employerSavingsAmount":0.8008281904610115,"frequencyId":6,"postTaxSavingsAmount":5.962133916683182,"preTaxSavingsAmount":5.637376656633329,"endDate":"2000-01-23T04:56:07.000+00:00","postTaxSavingsAmountType":"Dollar","mandatoryAmount":1.4658129805029452,"externalDestinationId":"externalDestinationId","preTaxSavingsAmountType":"Dollar","mandatoryAmountType":"Dollar","startDate":"2000-01-23T04:56:07.000+00:00","employerSavingsAmountType":"Dollar"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/Accounts/{account_id}/SavingsStrategies/{id}'.format(account_id=56, id=56),
        headers=headers,
        json=savings_strategy,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

