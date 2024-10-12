# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts_with_sub_entities_model import AccountsWithSubEntitiesModel
from openapi_server.models.defined_benefit_pensions_model import DefinedBenefitPensionsModel
from openapi_server.models.incomes_model import IncomesModel
from openapi_server.models.liabilities_model import LiabilitiesModel
from openapi_server.models.life_insurance_policies_with_sub_entities_model import LifeInsurancePoliciesWithSubEntitiesModel
from openapi_server.models.owners_model import OwnersModel
from openapi_server.models.relationship_types_model import RelationshipTypesModel


pytestmark = pytest.mark.asyncio

async def test_presentation_get_accounts_by_factfinderid_externalsourceid(client):
    """Test case for presentation_get_accounts_by_factfinderid_externalsourceid

    
    """
    params = [('factFinderId', 56),
                    ('externalSourceId', 'external_source_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Presentation/Accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_presentation_get_demographic_owners_by_factfinderid(client):
    """Test case for presentation_get_demographic_owners_by_factfinderid

    
    """
    params = [('factFinderId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Presentation/Demographics/Owners',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_presentation_get_demographic_relationships(client):
    """Test case for presentation_get_demographic_relationships

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Presentation/Demographics/Relationships',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_presentation_get_incomes_by_factfinderid(client):
    """Test case for presentation_get_incomes_by_factfinderid

    
    """
    params = [('factFinderId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Presentation/Incomes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_presentation_get_liabilities_by_factfinderid(client):
    """Test case for presentation_get_liabilities_by_factfinderid

    
    """
    params = [('factFinderId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Presentation/Liabilities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_presentation_get_life_insurance_policies_by_factfinderid(client):
    """Test case for presentation_get_life_insurance_policies_by_factfinderid

    
    """
    params = [('factFinderId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Presentation/LifeInsurancePolicies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_presentation_get_pensions_by_factfinderid(client):
    """Test case for presentation_get_pensions_by_factfinderid

    
    """
    params = [('factFinderId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Presentation/Pensions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

