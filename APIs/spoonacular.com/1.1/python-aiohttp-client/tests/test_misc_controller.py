# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.detect_food_in_text200_response import DetectFoodInText200Response
from openapi_server.models.get_a_random_food_joke200_response import GetARandomFoodJoke200Response
from openapi_server.models.get_conversation_suggests200_response import GetConversationSuggests200Response
from openapi_server.models.get_random_food_trivia200_response import GetRandomFoodTrivia200Response
from openapi_server.models.image_analysis_by_url200_response import ImageAnalysisByURL200Response
from openapi_server.models.image_classification_by_url200_response import ImageClassificationByURL200Response
from openapi_server.models.search_all_food200_response import SearchAllFood200Response
from openapi_server.models.search_custom_foods200_response import SearchCustomFoods200Response
from openapi_server.models.search_food_videos200_response import SearchFoodVideos200Response
from openapi_server.models.search_site_content200_response import SearchSiteContent200Response
from openapi_server.models.talk_to_chatbot200_response import TalkToChatbot200Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_detect_food_in_text(client):
    """Test case for detect_food_in_text

    Detect Food in Text
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'content_type': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/food/detect',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_a_random_food_joke(client):
    """Test case for get_a_random_food_joke

    Random Food Joke
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/jokes/random',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_conversation_suggests(client):
    """Test case for get_conversation_suggests

    Conversation Suggests
    """
    params = [('query', 'tell'),
                    ('number', 5)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/converse/suggest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_random_food_trivia(client):
    """Test case for get_random_food_trivia

    Random Food Trivia
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/trivia/random',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_image_analysis_by_url(client):
    """Test case for image_analysis_by_url

    Image Analysis by URL
    """
    params = [('imageUrl', 'https://spoonacular.com/recipeImages/635350-240x150.jpg')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/images/analyze',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_image_classification_by_url(client):
    """Test case for image_classification_by_url

    Image Classification by URL
    """
    params = [('imageUrl', 'https://spoonacular.com/recipeImages/635350-240x150.jpg')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/images/classify',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_all_food(client):
    """Test case for search_all_food

    Search All Food
    """
    params = [('query', 'apple'),
                    ('offset', 56),
                    ('number', 10)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_custom_foods(client):
    """Test case for search_custom_foods

    Search Custom Foods
    """
    params = [('query', 'burger'),
                    ('username', 'dsky'),
                    ('hash', '4b5v4398573406'),
                    ('offset', 56),
                    ('number', 10)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/customFoods/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_food_videos(client):
    """Test case for search_food_videos

    Search Food Videos
    """
    params = [('query', 'burger'),
                    ('type', 'main course'),
                    ('cuisine', 'italian'),
                    ('diet', 'vegetarian'),
                    ('includeIngredients', 'tomato,cheese'),
                    ('excludeIngredients', 'eggs'),
                    ('minLength', 0),
                    ('maxLength', 999),
                    ('offset', 56),
                    ('number', 10)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/videos/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_site_content(client):
    """Test case for search_site_content

    Search Site Content
    """
    params = [('query', 'past')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/site/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_talk_to_chatbot(client):
    """Test case for talk_to_chatbot

    Talk to Chatbot
    """
    params = [('text', 'donut recipes'),
                    ('contextId', '342938')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/converse',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

