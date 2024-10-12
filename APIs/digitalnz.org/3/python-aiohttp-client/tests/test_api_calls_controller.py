# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.record import Record
from openapi_server.models.records_format_get200_response import RecordsFormatGet200Response
from openapi_server.models.records_record_id_more_like_this_format_get200_response import RecordsRecordIdMoreLikeThisFormatGet200Response


pytestmark = pytest.mark.asyncio

async def test_records_format_get(client):
    """Test case for records_format_get

    Run queries against DigitalNZ metadata search service.
    """
    params = [('text', 'text_example'),
                    ('and[category][]', 'and_category_example'),
                    ('and[content_partner][]', 'and_content_partner_example'),
                    ('and[primary_collection][]', 'and_primary_collection_example'),
                    ('and[collection][]', 'and_collection_example'),
                    ('and[usage][]', 'and_usage_example'),
                    ('and[subject][]', 'and_subject_example'),
                    ('and[dc_type][]', 'and_dc_type_example'),
                    ('and[format][]', 'and_format_example'),
                    ('and[placename][]', 'and_placename_example'),
                    ('and[creator][]', 'and_creator_example'),
                    ('and[title][]', 'and_title_example'),
                    ('and[date]', 'and_date_example'),
                    ('and[year]', 'and_year_example'),
                    ('and[decade]', 'and_decade_example'),
                    ('and[century]', 'and_century_example'),
                    ('without[{filter_field}]', 'without_filter_field_example'),
                    ('and[or][{filter_field}][]', 'and_or_filter_field_example'),
                    ('and[is_commercial_use]', True),
                    ('and[has_large_thumbnail_url]', 'and_has_large_thumbnail_url_example'),
                    ('and[has_lat_lng]', True),
                    ('geo_bbox', 'geo_bbox_example'),
                    ('fields', 'fields_example'),
                    ('sort', 'sort_example'),
                    ('direction', asc),
                    ('page', 1),
                    ('per_page', 20),
                    ('facets', ['facets_example']),
                    ('facets_page', 56),
                    ('facets_per_page', 10),
                    ('exclude_filters_from_facets', False)]
    headers = { 
        'Accept': 'application/json',
        'authentication_token': 'authentication_token_example',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/records.{format}'.format(format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_records_record_id_format_get(client):
    """Test case for records_record_id_format_get

    View metadata associated with a single record.
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'authentication_token': 'authentication_token_example',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/records/{record_id_format}'.format(record_id=189089, format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_records_record_id_more_like_this_format_get(client):
    """Test case for records_record_id_more_like_this_format_get

    The \"More Like This\" call returns similar records to the specified ID. 
    """
    params = [('fields', 'fields_example'),
                    ('mlt_fields', 'mlt_fields_example'),
                    ('filtering', 'filtering_example')]
    headers = { 
        'Accept': 'application/json',
        'authentication_token': 'authentication_token_example',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/records/{record_id}/more_like_this.{format}'.format(record_id=35806021, format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

