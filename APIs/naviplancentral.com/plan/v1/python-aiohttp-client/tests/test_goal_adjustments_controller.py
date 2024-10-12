# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_coverage_projections_result_model_advicent_domain_logic_goal_what_if_education_goal_adjustments import AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_coverage_projections_result_model_advicent_domain_logic_goal_what_if_major_purchase_goal_adjustments import AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_coverage_projections_result_model_advicent_domain_logic_goal_what_if_retirement_goal_adjustments import AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_education_goal_adjustments_model import AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_goal_adjustments_model_advicent_domain_logic_goal_what_if_education_goal_adjustments import AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_goal_adjustments_model_advicent_domain_logic_goal_what_if_major_purchase_goal_adjustments import AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_goal_adjustments_model_advicent_domain_logic_goal_what_if_retirement_goal_adjustments import AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_goal_success_rate_results_model import AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateResultsModel
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_major_purchase_goal_adjustments_model import AdvicentNaviPlanRestApiGoalAdjustmentsModelsMajorPurchaseGoalAdjustmentsModel
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_restrictions_result_model import AdvicentNaviPlanRestApiGoalAdjustmentsModelsRestrictionsResultModel
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_retirement_goal_adjustments_model import AdvicentNaviPlanRestApiGoalAdjustmentsModelsRetirementGoalAdjustmentsModel
from openapi_server.models.advicent_navi_plan_rest_api_goal_adjustments_models_what_are_my_options_model import AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel


pytestmark = pytest.mark.asyncio

async def test_goal_adjustments_get_education_by_id_clientid_planid(client):
    """Test case for goal_adjustments_get_education_by_id_clientid_planid

    Retrieve the adjustments
    """
    params = [('clientId', 'client_id_example'),
                    ('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/GoalAdjustments/Education/{id}/Adjustments'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_goal_adjustments_get_goal_adjustment_restrictions_by_clientid_planid(client):
    """Test case for goal_adjustments_get_goal_adjustment_restrictions_by_clientid_planid

    Returns a list of goal adjustment restrictions.
    """
    params = [('clientId', 'client_id_example'),
                    ('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/GoalAdjustments/Restrictions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_goal_adjustments_get_goal_success_rates_by_clientid_planid(client):
    """Test case for goal_adjustments_get_goal_success_rates_by_clientid_planid

    Returns a list of goals with their relevant success rates.
    """
    params = [('clientId', 'client_id_example'),
                    ('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/GoalAdjustments/GoalSuccessRates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_goal_adjustments_get_major_purchase_by_id_clientid_planid(client):
    """Test case for goal_adjustments_get_major_purchase_by_id_clientid_planid

    Retrieve the adjustments
    """
    params = [('clientId', 'client_id_example'),
                    ('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/GoalAdjustments/MajorPurchase/{id}/Adjustments'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_goal_adjustments_get_retirement_by_clientid_planid(client):
    """Test case for goal_adjustments_get_retirement_by_clientid_planid

    Retrieve the adjustments
    """
    params = [('clientId', 'client_id_example'),
                    ('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/GoalAdjustments/Retirement/Adjustments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_goal_adjustments_get_what_are_my_options_by_id_clientid_planid(client):
    """Test case for goal_adjustments_get_what_are_my_options_by_id_clientid_planid

    Returns WAMO values for current goal
    """
    params = [('clientId', 'client_id_example'),
                    ('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/GoalAdjustments/{id}/WhatAreMyOptions'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_goal_adjustments_post_education_by_id_goaladjustments_planid(client):
    """Test case for goal_adjustments_post_education_by_id_goaladjustments_planid

    Perform calculations
    """
    goal_adjustments = {"adjustedValues":{"duration":0.8008281904610115,"lumpSumDate":"2000-01-23T04:56:07.000+00:00","lumpSumContribution":1.4658129805029452,"monthlySavingsContribution":5.962133916683182,"expensesCovered":6.027456183070403}}
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/plan/api/GoalAdjustments/Education/{id}/Calculations'.format(id=56),
        headers=headers,
        json=goal_adjustments,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_goal_adjustments_post_major_purchase_by_id_goaladjustments_planid(client):
    """Test case for goal_adjustments_post_major_purchase_by_id_goaladjustments_planid

    Perform calculations
    """
    goal_adjustments = {"adjustedValues":{"lumpSumDate":"2000-01-23T04:56:07.000+00:00","lumpSumContribution":0.8008281904610115,"targetDate":"2000-01-23T04:56:07.000+00:00","monthlySavingsContribution":6.027456183070403,"totalNeed":1.4658129805029452}}
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/plan/api/GoalAdjustments/MajorPurchase/{id}/Calculations'.format(id=56),
        headers=headers,
        json=goal_adjustments,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_goal_adjustments_post_retirement_by_goaladjustments_planid(client):
    """Test case for goal_adjustments_post_retirement_by_goaladjustments_planid

    Perform calculations
    """
    goal_adjustments = {"adjustedValues":{"discretionaryExpenseCoverage":1.4658129805029452,"lumpSumDate":"2000-01-23T04:56:07.000+00:00","lumpSumContribution":5.637376656633329,"coClientRetirementAge":6.027456183070403,"monthlySavingsContribution":2.3021358869347655,"clientRetirementAge":0.8008281904610115,"fixedExpenseCoverage":5.962133916683182}}
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/plan/api/GoalAdjustments/Retirement/Calculations',
        headers=headers,
        json=goal_adjustments,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

