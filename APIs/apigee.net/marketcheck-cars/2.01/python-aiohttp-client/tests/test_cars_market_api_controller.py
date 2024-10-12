# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.daily_stats import DailyStats
from openapi_server.models.error import Error
from openapi_server.models.fare_value import FareValue
from openapi_server.models.mds import Mds
from openapi_server.models.popular_cars import PopularCars
from openapi_server.models.price_prediction import PricePrediction
from openapi_server.models.sales import Sales


pytestmark = pytest.mark.asyncio

async def test_fare_value(client):
    """Test case for fare_value

    Predict fare value of car for UK based on YMMT & miles
    """
    params = [('api_key', 'api_key_example'),
                    ('vrm', 'vrm_example'),
                    ('year', 56),
                    ('make', 'make_example'),
                    ('model', 'model_example'),
                    ('variant', 'variant_example'),
                    ('miles', 56),
                    ('postal_code', 'postal_code_example'),
                    ('radius', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/predict/car/uk/fmv',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_daily_stats(client):
    """Test case for get_daily_stats

    Price, Miles and Days on Market stats
    """
    params = [('api_key', 'api_key_example'),
                    ('country', us),
                    ('car_type', used),
                    ('ymm', 'ymm_example'),
                    ('ymmt', 'ymmt_example'),
                    ('taxonomy_vin', 'taxonomy_vin_example'),
                    ('vin', 'vin_example'),
                    ('state', 'state_example'),
                    ('city_state', 'city_state_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/stats/car',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mds(client):
    """Test case for get_mds

    Market Days Supply
    """
    params = [('api_key', 'api_key_example'),
                    ('vin', 'vin_example'),
                    ('exact', False),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 56),
                    ('zip', 'zip_example'),
                    ('msa_code', 'msa_code_example'),
                    ('debug', False),
                    ('include_sold', False),
                    ('country', US),
                    ('state', 'state_example'),
                    ('city', 'city_example'),
                    ('ymmt', 'ymmt_example'),
                    ('car_type', 'car_type_example'),
                    ('lease_term', 'lease_term_example'),
                    ('lease_down_payment', 'lease_down_payment_example'),
                    ('lease_emp', 'lease_emp_example'),
                    ('finance_loan_term', 'finance_loan_term_example'),
                    ('finance_loan_apr', 'finance_loan_apr_example'),
                    ('finance_emp', 'finance_emp_example'),
                    ('finance_down_payment', 'finance_down_payment_example'),
                    ('finance_down_payment_per', 'finance_down_payment_per_example'),
                    ('carfax_1_owner', 'carfax_1_owner_example'),
                    ('carfax_clean_title', 'carfax_clean_title_example'),
                    ('year', 'year_example'),
                    ('make', 'make_example'),
                    ('model', 'model_example'),
                    ('trim', 'trim_example'),
                    ('dealer_id', 'dealer_id_example'),
                    ('source', 'source_example'),
                    ('body_type', 'body_type_example'),
                    ('body_subtype', 'body_subtype_example'),
                    ('vehicle_type', 'vehicle_type_example'),
                    ('cylinders', 'cylinders_example'),
                    ('transmission', 'transmission_example'),
                    ('doors', 'doors_example'),
                    ('drivetrain', 'drivetrain_example'),
                    ('exterior_color', 'exterior_color_example'),
                    ('interior_color', 'interior_color_example'),
                    ('base_exterior_color', 'base_exterior_color_example'),
                    ('base_interior_color', 'base_interior_color_example'),
                    ('engine', 'engine_example'),
                    ('engine_size', 'engine_size_example'),
                    ('engine_aspiration', 'engine_aspiration_example'),
                    ('engine_block', 'engine_block_example'),
                    ('highway_mpg_range', 'highway_mpg_range_example'),
                    ('city_mpg_range', 'city_mpg_range_example'),
                    ('miles_range', 'miles_range_example'),
                    ('price_range', 'price_range_example'),
                    ('msrp_range', 'msrp_range_example'),
                    ('dom_range', 'dom_range_example'),
                    ('dealership_group_name', 'dealership_group_name_example'),
                    ('dom_active_range', 'dom_active_range_example'),
                    ('dom_180_range', 'dom_180_range_example'),
                    ('fuel_type', 'fuel_type_example'),
                    ('dealer_type', 'dealer_type_example'),
                    ('engine_size_range', 'engine_size_range_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/mds/car',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_popular_cars(client):
    """Test case for get_popular_cars

    Get make model wise top 50 popular cars on national, state, city level
    """
    params = [('api_key', 'api_key_example'),
                    ('state', 'state_example'),
                    ('city_state', 'city_state_example'),
                    ('car_type', 'car_type_example'),
                    ('country', us)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/popular/cars',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sales_count(client):
    """Test case for get_sales_count

    Get sales count by make, model, year, trim or taxonomy vin
    """
    params = [('api_key', 'api_key_example'),
                    ('car_type', used),
                    ('make', 'make_example'),
                    ('mm', 'mm_example'),
                    ('ymm', 'ymm_example'),
                    ('ymmt', 'ymmt_example'),
                    ('taxonomy_vin', 'taxonomy_vin_example'),
                    ('state', 'state_example'),
                    ('city_state', 'city_state_example'),
                    ('vin', 'vin_example'),
                    ('country', us)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/sales/car',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_predict_car_price(client):
    """Test case for predict_car_price

    Predict car price based on it's specifications
    """
    params = [('api_key', 'api_key_example'),
                    ('vin', 'vin_example'),
                    ('car_type', 'car_type_example'),
                    ('year', 56),
                    ('make', 'make_example'),
                    ('model', 'model_example'),
                    ('trim', 'trim_example'),
                    ('is_certified', True),
                    ('carfax_1_owner', True),
                    ('carfax_clean_title', True),
                    ('base_exterior_color', 'base_exterior_color_example'),
                    ('base_interior_color', 'base_interior_color_example'),
                    ('transmission', 'transmission_example'),
                    ('drivetrain', 'drivetrain_example'),
                    ('engine_size', 3.4),
                    ('engine_block', 'engine_block_example'),
                    ('cylinders', 56),
                    ('doors', 56),
                    ('highway_mpg', 56),
                    ('city_mpg', 56),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('miles', 56),
                    ('zip', 'zip_example'),
                    ('country', us)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/predict/car/price',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_predict_uk_car_price(client):
    """Test case for predict_uk_car_price

    Predict car price for UK based on it's specifications
    """
    params = [('api_key', 'api_key_example'),
                    ('vrm', 'vrm_example'),
                    ('year', 56),
                    ('make', 'make_example'),
                    ('model', 'model_example'),
                    ('trim', 'trim_example'),
                    ('base_exterior_color', 'base_exterior_color_example'),
                    ('transmission', 'transmission_example'),
                    ('drivetrain', 'drivetrain_example'),
                    ('engine_size', 3.4),
                    ('cylinders', 56),
                    ('doors', 56),
                    ('fuel_type', 'fuel_type_example'),
                    ('highway_mpg', 3.4),
                    ('city_mpg', 3.4),
                    ('combined_mpg', 3.4),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('miles', 56),
                    ('zip', 'zip_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/predict/car/uk/price',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

