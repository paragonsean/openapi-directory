# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_what_are_my_options_model import AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel
from openapi_server.models.advicent_navi_plan_rest_api_goals_models_goal_funding_list_model import AdvicentNaviPlanRestApiGoalsModelsGoalFundingListModel
from openapi_server.models.advicent_navi_plan_rest_api_goals_models_live_goal_base_model import AdvicentNaviPlanRestApiGoalsModelsLiveGoalBaseModel
from openapi_server.models.advicent_navi_plan_rest_api_net_worth_models_account_base_model import AdvicentNaviPlanRestApiNetWorthModelsAccountBaseModel
from openapi_server.models.advicent_navi_plan_rest_api_net_worth_models_liability_base_model import AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel
from openapi_server.models.advicent_navi_plan_rest_api_net_worth_models_lifestyle_asset_base_model import AdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetBaseModel
from openapi_server.models.advicent_navi_plan_rest_api_net_worth_models_real_estate_base_model import AdvicentNaviPlanRestApiNetWorthModelsRealEstateBaseModel
from openapi_server.models.advicent_navi_plan_rest_api_projections_models_needs_vs_abilities_projections_model import AdvicentNaviPlanRestApiProjectionsModelsNeedsVsAbilitiesProjectionsModel
from openapi_server.models.advicent_navi_plan_rest_api_projections_models_net_worth_projections_model import AdvicentNaviPlanRestApiProjectionsModelsNetWorthProjectionsModel


pytestmark = pytest.mark.asyncio

async def test_live_plan_get_accounts_by_clientid_planid(client):
    """Test case for live_plan_get_accounts_by_clientid_planid

    Retrieves accounts for a given plan
    """
    params = [('clientId', 'client_id_example'),
                    ('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/LivePlan/NetWorth/Accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_live_plan_get_goal_funding_list_by_clientid_planid(client):
    """Test case for live_plan_get_goal_funding_list_by_clientid_planid

    Retrieve a list of funding accounts
    """
    params = [('clientId', 'client_id_example'),
                    ('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/LivePlan/Goals/Funding',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_live_plan_get_goals_by_clientid_planid(client):
    """Test case for live_plan_get_goals_by_clientid_planid

    Retrieves all goals from the live plan
    """
    params = [('clientId', 'client_id_example'),
                    ('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/LivePlan/Goals',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_live_plan_get_liabilities_by_clientid_planid(client):
    """Test case for live_plan_get_liabilities_by_clientid_planid

    Retrieves liabilities for a given plan
    """
    params = [('clientId', 'client_id_example'),
                    ('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/LivePlan/NetWorth/Liabilities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_live_plan_get_lifestyle_assets_by_clientid_planid(client):
    """Test case for live_plan_get_lifestyle_assets_by_clientid_planid

    Retrieves lifestyle assets for a given plan
    """
    params = [('clientId', 'client_id_example'),
                    ('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/LivePlan/NetWorth/LifestyleAssets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_live_plan_get_projected_needs_vs_abilities_by_id_clientid_planid(client):
    """Test case for live_plan_get_projected_needs_vs_abilities_by_id_clientid_planid

    Retrieves needs vs abilities projections
    """
    params = [('clientId', 'client_id_example'),
                    ('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/LivePlan/Projections/{id}/NeedsVsAbilities'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_live_plan_get_projected_net_worth_by_clientid_planid(client):
    """Test case for live_plan_get_projected_net_worth_by_clientid_planid

    Retrieves net worth projections
    """
    params = [('clientId', 'client_id_example'),
                    ('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/LivePlan/Projections/NetWorth',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_live_plan_get_real_estate_assets_by_clientid_planid(client):
    """Test case for live_plan_get_real_estate_assets_by_clientid_planid

    Retrieves real estate accounts for a given plan
    """
    params = [('clientId', 'client_id_example'),
                    ('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/LivePlan/NetWorth/RealEstate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_live_plan_get_what_are_my_options_by_id_clientid_planid(client):
    """Test case for live_plan_get_what_are_my_options_by_id_clientid_planid

    Retrieve WAMO values for a given goal
    """
    params = [('clientId', 'client_id_example'),
                    ('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/LivePlan/Goals/{id}/WhatAreMyOptions'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

