# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_exception import ApiException
from openapi_server.models.api_response import ApiResponse
from openapi_server.models.article_dto import ArticleDTO
from openapi_server.models.default_response_dtoof_article_dto import DefaultResponseDTOOfArticleDTO
from openapi_server.models.default_response_dtoof_integer import DefaultResponseDTOOfInteger
from openapi_server.models.default_response_dtoof_list_of_article_search_dto import DefaultResponseDTOOfListOfArticleSearchDTO
from openapi_server.models.default_response_dtoof_status_dto import DefaultResponseDTOOfStatusDTO
from openapi_server.models.gym_article_details_dto import GymArticleDetailsDTO
from openapi_server.models.measure_unit_dto import MeasureUnitDTO


pytestmark = pytest.mark.asyncio

async def test_article_add_measure_unit(client):
    """Test case for article_add_measure_unit

    Add measure unit
    """
    body = {"name":"name","id":0,"type":"type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/Article/MeasureUnit',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_delete(client):
    """Test case for article_delete

    Delete article from the system             
    """
    params = [('ArticleId', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/Article',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_get(client):
    """Test case for article_get

    Get article details This will return all properties related to article entity             
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Article/{article_id}'.format(article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_get_addons(client):
    """Test case for article_get_addons

    
    """
    params = [('searchText', 'search_text_example'),
                    ('gymIds', '-1'),
                    ('type', 'all'),
                    ('limit', 100),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Article/GetAddons',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_get_measure_units(client):
    """Test case for article_get_measure_units

    Get mesure units
    """
    params = [('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Article/MeasureUnits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_get_revenue_accounts(client):
    """Test case for article_get_revenue_accounts

    Get Revenue Accounts 
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Article/RevenueAccounts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_gym_article_details(client):
    """Test case for article_gym_article_details

    Get Gym specific properties for article             
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Article/GymArticle/{article_id}/{gym_id}'.format(article_id=56, gym_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_post(client):
    """Test case for article_post

    Add new article             
    """
    body = {"modifiedUser":"modifiedUser","description":"description","discount":5.637376656633329,"isInventoryItem":True,"employeeDiscount":2.3021358869347655,"type":"type","reorderLevel":4.965218492984954,"number":7,"sellingPrice":9.965781217890562,"price":1.1730742509559433,"availableQty":5.962133916683182,"barcode":"barcode","availableGyms":[{"gymId":1,"gymName":"gymName","externalGymNumber":6,"location":"location"},{"gymId":1,"gymName":"gymName","externalGymNumber":6,"location":"location"}],"createdUser":"createdUser","gymArticles":[{"gymIdList":"gymIdList","modifiedUser":"modifiedUser","gymName":"gymName","articleId":9,"isInventoryItem":True,"isObsolete":True,"employeeDiscount":2.027123023002322,"reorderLevel":1.0246457001441578,"gymId":7,"isDefault":True,"sellingPrice":6.84685269835264,"availableQty":3.616076749251911,"id":1,"createdUser":"createdUser","revenueAccountId":1,"employeePrice":4.145608029883936},{"gymIdList":"gymIdList","modifiedUser":"modifiedUser","gymName":"gymName","articleId":9,"isInventoryItem":True,"isObsolete":True,"employeeDiscount":2.027123023002322,"reorderLevel":1.0246457001441578,"gymId":7,"isDefault":True,"sellingPrice":6.84685269835264,"availableQty":3.616076749251911,"id":1,"createdUser":"createdUser","revenueAccountId":1,"employeePrice":4.145608029883936}],"articleId":0,"vat":9.369310271410669,"measureUnit":"measureUnit","isObsolete":True,"tags":"tags","cronExpression":"cronExpression","createdDate":"2000-01-23T04:56:07.000+00:00","activeStatus":True,"vatApplicable":True,"isAddOn":True,"modifiedDate":"2000-01-23T04:56:07.000+00:00","name":"name","applyForAllGyms":True,"revenueAccountId":5,"employeePrice":7.061401241503109}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/Article',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_put(client):
    """Test case for article_put

    update existing article             
    """
    body = {"modifiedUser":"modifiedUser","description":"description","discount":5.637376656633329,"isInventoryItem":True,"employeeDiscount":2.3021358869347655,"type":"type","reorderLevel":4.965218492984954,"number":7,"sellingPrice":9.965781217890562,"price":1.1730742509559433,"availableQty":5.962133916683182,"barcode":"barcode","availableGyms":[{"gymId":1,"gymName":"gymName","externalGymNumber":6,"location":"location"},{"gymId":1,"gymName":"gymName","externalGymNumber":6,"location":"location"}],"createdUser":"createdUser","gymArticles":[{"gymIdList":"gymIdList","modifiedUser":"modifiedUser","gymName":"gymName","articleId":9,"isInventoryItem":True,"isObsolete":True,"employeeDiscount":2.027123023002322,"reorderLevel":1.0246457001441578,"gymId":7,"isDefault":True,"sellingPrice":6.84685269835264,"availableQty":3.616076749251911,"id":1,"createdUser":"createdUser","revenueAccountId":1,"employeePrice":4.145608029883936},{"gymIdList":"gymIdList","modifiedUser":"modifiedUser","gymName":"gymName","articleId":9,"isInventoryItem":True,"isObsolete":True,"employeeDiscount":2.027123023002322,"reorderLevel":1.0246457001441578,"gymId":7,"isDefault":True,"sellingPrice":6.84685269835264,"availableQty":3.616076749251911,"id":1,"createdUser":"createdUser","revenueAccountId":1,"employeePrice":4.145608029883936}],"articleId":0,"vat":9.369310271410669,"measureUnit":"measureUnit","isObsolete":True,"tags":"tags","cronExpression":"cronExpression","createdDate":"2000-01-23T04:56:07.000+00:00","activeStatus":True,"vatApplicable":True,"isAddOn":True,"modifiedDate":"2000-01-23T04:56:07.000+00:00","name":"name","applyForAllGyms":True,"revenueAccountId":5,"employeePrice":7.061401241503109}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/Article',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_search(client):
    """Test case for article_search

    Search articles It will only return basic information of article             
    """
    params = [('searchText', 'search_text_example'),
                    ('gymId', -1),
                    ('type', 'all'),
                    ('orderBy', '1'),
                    ('limit', 100),
                    ('offset', 0),
                    ('activeStatus', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Article/Search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_update_article_gym_details(client):
    """Test case for article_update_article_gym_details

    Add article details that associate with a Gym             
    """
    body = {"gymIdList":"gymIdList","modifiedUser":"modifiedUser","gymName":"gymName","articleId":9,"isInventoryItem":True,"isObsolete":True,"employeeDiscount":2.027123023002322,"reorderLevel":1.0246457001441578,"gymId":7,"isDefault":True,"sellingPrice":6.84685269835264,"availableQty":3.616076749251911,"id":1,"createdUser":"createdUser","revenueAccountId":1,"employeePrice":4.145608029883936}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/Article/ArticleGymDetails',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_update_status(client):
    """Test case for article_update_status

    Deactivate existing article 
    """
    params = [('ArticleId', 56),
                    ('status', 56),
                    ('userName', 'user_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/Article/UpdateStatus',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

