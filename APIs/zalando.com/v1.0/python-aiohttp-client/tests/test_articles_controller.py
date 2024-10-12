# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.article import Article
from openapi_server.models.article_media import ArticleMedia
from openapi_server.models.article_review import ArticleReview
from openapi_server.models.article_reviews import ArticleReviews
from openapi_server.models.article_reviews_summaries import ArticleReviewsSummaries
from openapi_server.models.article_reviews_summary import ArticleReviewsSummary
from openapi_server.models.article_unit import ArticleUnit
from openapi_server.models.articles import Articles
from openapi_server.models.error_message import ErrorMessage


pytestmark = pytest.mark.asyncio

async def test_article_reviews_get(client):
    """Test case for article_reviews_get

    Get Article Reviews
    """
    params = [('articleId', ['article_id_example']),
                    ('articleModelId', ['article_model_id_example']),
                    ('minStarRating', 'min_star_rating_example'),
                    ('maxStarRating', 'max_star_rating_example'),
                    ('sort', newest),
                    ('page', 'page_example'),
                    ('pageSize', 'page_size_example'),
                    ('fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='GET',
        path='/article-reviews',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_reviews_review_id_get(client):
    """Test case for article_reviews_review_id_get

    Get Article Reviews by reviewId
    """
    params = [('fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='GET',
        path='/article-reviews/{review_id}'.format(review_id='review_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_reviews_summaries_article_model_id_get(client):
    """Test case for article_reviews_summaries_article_model_id_get

    Get Article Reviews Summaries by articleModelId
    """
    params = [('fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='GET',
        path='/article-reviews-summaries/{article_model_id}'.format(article_model_id='article_model_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_reviews_summaries_get(client):
    """Test case for article_reviews_summaries_get

    Get Article Reviews Summaries
    """
    params = [('articleModelId', ['article_model_id_example']),
                    ('page', 'page_example'),
                    ('pageSize', 'page_size_example'),
                    ('fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='GET',
        path='/article-reviews-summaries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_articles_article_id_get(client):
    """Test case for articles_article_id_get

    Get Article by articleId
    """
    params = [('fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='GET',
        path='/articles/{article_id}'.format(article_id='article_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_articles_article_id_media_get(client):
    """Test case for articles_article_id_media_get

    Get Article media by articleId
    """
    params = [('fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='GET',
        path='/articles/{article_id}/media'.format(article_id='article_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_articles_article_id_reviews_get(client):
    """Test case for articles_article_id_reviews_get

    Get Article reviews by articleId
    """
    params = [('minStarRating', 'min_star_rating_example'),
                    ('maxStarRating', 'max_star_rating_example'),
                    ('sort', newest),
                    ('page', 'page_example'),
                    ('pageSize', 'page_size_example'),
                    ('fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='GET',
        path='/articles/{article_id}/reviews'.format(article_id='article_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_articles_article_id_reviews_summary_get(client):
    """Test case for articles_article_id_reviews_summary_get

    Get Article reviews summary by articleId
    """
    params = [('fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='GET',
        path='/articles/{article_id}/reviews-summary'.format(article_id='article_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_articles_article_id_units_get(client):
    """Test case for articles_article_id_units_get

    Get Article units by articleId
    """
    params = [('fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='GET',
        path='/articles/{article_id}/units'.format(article_id='article_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_articles_article_id_units_unit_id_get(client):
    """Test case for articles_article_id_units_unit_id_get

    Get Article units by articleId snd unitId
    """
    params = [('fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='GET',
        path='/articles/{article_id}/units/{unit_id}'.format(article_id='article_id_example', unit_id='unit_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_articles_get(client):
    """Test case for articles_get

    Search for Articles
    """
    params = [('articleId', ['article_id_example']),
                    ('articleModelId', ['article_model_id_example']),
                    ('articleUnitId', ['article_unit_id_example']),
                    ('activationDate', ['activation_date_example']),
                    ('ageGroup', ['age_group_example']),
                    ('assortmentArea', ['assortment_area_example']),
                    ('brand', ['brand_example']),
                    ('brandfamily', ['brandfamily_example']),
                    ('category', ['category_example']),
                    ('color', ['color_example']),
                    ('den', ['den_example']),
                    ('filling', ['filling_example']),
                    ('fullText', 'full_text_example'),
                    ('gender', ['gender_example']),
                    ('heelForm', ['heel_form_example']),
                    ('heelHeight', ['heel_height_example']),
                    ('length', 'length_example'),
                    ('occasion', ['occasion_example']),
                    ('pattern', ['pattern_example']),
                    ('price', 'price_example'),
                    ('sale', ['sale_example']),
                    ('season', ['season_example']),
                    ('shaftHeight', ['shaft_height_example']),
                    ('shaftWidth', ['shaft_width_example']),
                    ('shirtCollar', ['shirt_collar_example']),
                    ('shoeFastener', ['shoe_fastener_example']),
                    ('shoeToecap', ['shoe_toecap_example']),
                    ('shopArea', ['shop_area_example']),
                    ('size', 'size_example'),
                    ('sports', ['sports_example']),
                    ('technology', ['technology_example']),
                    ('trouserRise', ['trouser_rise_example']),
                    ('upperMaterial', ['upper_material_example']),
                    ('volume', ['volume_example']),
                    ('page', 'page_example'),
                    ('pageSize', 'page_size_example'),
                    ('sort', 'sort_example'),
                    ('fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='GET',
        path='/articles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

