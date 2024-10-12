# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_message import ErrorMessage
from openapi_server.models.facet import Facet


pytestmark = pytest.mark.asyncio

async def test_facets_get(client):
    """Test case for facets_get

    Shop Facets
    """
    params = [('ageGroup', ['age_group_example']),
                    ('articleId', ['article_id_example']),
                    ('activationDate', ['activation_date_example']),
                    ('articleModelId', ['article_model_id_example']),
                    ('assortmentArea', ['assortment_area_example']),
                    ('brand', ['brand_example']),
                    ('brandfamily', ['brandfamily_example']),
                    ('category', ['category_example']),
                    ('color', ['color_example']),
                    ('den', ['den_example']),
                    ('filling', ['filling_example']),
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
                    ('fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='GET',
        path='/facets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

