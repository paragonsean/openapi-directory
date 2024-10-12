# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.age_rating_declaration_response import AgeRatingDeclarationResponse
from openapi_server.models.app_store_review_detail_response import AppStoreReviewDetailResponse
from openapi_server.models.app_store_version_build_linkage_request import AppStoreVersionBuildLinkageRequest
from openapi_server.models.app_store_version_build_linkage_response import AppStoreVersionBuildLinkageResponse
from openapi_server.models.app_store_version_create_request import AppStoreVersionCreateRequest
from openapi_server.models.app_store_version_localizations_response import AppStoreVersionLocalizationsResponse
from openapi_server.models.app_store_version_phased_release_response import AppStoreVersionPhasedReleaseResponse
from openapi_server.models.app_store_version_response import AppStoreVersionResponse
from openapi_server.models.app_store_version_submission_response import AppStoreVersionSubmissionResponse
from openapi_server.models.app_store_version_update_request import AppStoreVersionUpdateRequest
from openapi_server.models.build_response import BuildResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.idfa_declaration_response import IdfaDeclarationResponse
from openapi_server.models.routing_app_coverage_response import RoutingAppCoverageResponse


pytestmark = pytest.mark.asyncio

async def test_app_store_versions_age_rating_declaration_get_to_one_related(client):
    """Test case for app_store_versions_age_rating_declaration_get_to_one_related

    
    """
    params = [('fields[ageRatingDeclarations]', ['fields_age_rating_declarations_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appStoreVersions/{id}/ageRatingDeclaration'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_versions_app_store_review_detail_get_to_one_related(client):
    """Test case for app_store_versions_app_store_review_detail_get_to_one_related

    
    """
    params = [('fields[appStoreReviewDetails]', ['fields_app_store_review_details_example']),
                    ('fields[appStoreVersions]', ['fields_app_store_versions_example']),
                    ('fields[appStoreReviewAttachments]', ['fields_app_store_review_attachments_example']),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appStoreVersions/{id}/appStoreReviewDetail'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_versions_app_store_version_localizations_get_to_many_related(client):
    """Test case for app_store_versions_app_store_version_localizations_get_to_many_related

    
    """
    params = [('fields[appStoreVersionLocalizations]', ['fields_app_store_version_localizations_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appStoreVersions/{id}/appStoreVersionLocalizations'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_versions_app_store_version_phased_release_get_to_one_related(client):
    """Test case for app_store_versions_app_store_version_phased_release_get_to_one_related

    
    """
    params = [('fields[appStoreVersionPhasedReleases]', ['fields_app_store_version_phased_releases_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appStoreVersions/{id}/appStoreVersionPhasedRelease'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_versions_app_store_version_submission_get_to_one_related(client):
    """Test case for app_store_versions_app_store_version_submission_get_to_one_related

    
    """
    params = [('fields[appStoreVersions]', ['fields_app_store_versions_example']),
                    ('fields[appStoreVersionSubmissions]', ['fields_app_store_version_submissions_example']),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appStoreVersions/{id}/appStoreVersionSubmission'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_versions_build_get_to_one_related(client):
    """Test case for app_store_versions_build_get_to_one_related

    
    """
    params = [('fields[builds]', ['fields_builds_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appStoreVersions/{id}/build'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_versions_build_get_to_one_relationship(client):
    """Test case for app_store_versions_build_get_to_one_relationship

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appStoreVersions/{id}/relationships/build'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_versions_build_update_to_one_relationship(client):
    """Test case for app_store_versions_build_update_to_one_relationship

    
    """
    body = {"data":{"id":"id","type":"builds"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/appStoreVersions/{id}/relationships/build'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_versions_create_instance(client):
    """Test case for app_store_versions_create_instance

    
    """
    body = {"data":{"relationships":{"app":{"data":{"id":"id","type":"apps"}},"build":{"data":{"id":"id","type":"builds"}}},"attributes":{"copyright":"copyright","earliestReleaseDate":"2000-01-23T04:56:07.000+00:00","usesIdfa":True,"versionString":"versionString","releaseType":"MANUAL","platform":"IOS"},"type":"appStoreVersions"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/appStoreVersions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_versions_delete_instance(client):
    """Test case for app_store_versions_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/appStoreVersions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_versions_get_instance(client):
    """Test case for app_store_versions_get_instance

    
    """
    params = [('fields[appStoreVersions]', ['fields_app_store_versions_example']),
                    ('include', ['include_example']),
                    ('fields[appStoreVersionLocalizations]', ['fields_app_store_version_localizations_example']),
                    ('fields[idfaDeclarations]', ['fields_idfa_declarations_example']),
                    ('fields[routingAppCoverages]', ['fields_routing_app_coverages_example']),
                    ('fields[appStoreVersionPhasedReleases]', ['fields_app_store_version_phased_releases_example']),
                    ('fields[ageRatingDeclarations]', ['fields_age_rating_declarations_example']),
                    ('fields[appStoreReviewDetails]', ['fields_app_store_review_details_example']),
                    ('fields[builds]', ['fields_builds_example']),
                    ('fields[appStoreVersionSubmissions]', ['fields_app_store_version_submissions_example']),
                    ('limit[appStoreVersionLocalizations]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appStoreVersions/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_versions_idfa_declaration_get_to_one_related(client):
    """Test case for app_store_versions_idfa_declaration_get_to_one_related

    
    """
    params = [('fields[idfaDeclarations]', ['fields_idfa_declarations_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appStoreVersions/{id}/idfaDeclaration'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_versions_routing_app_coverage_get_to_one_related(client):
    """Test case for app_store_versions_routing_app_coverage_get_to_one_related

    
    """
    params = [('fields[routingAppCoverages]', ['fields_routing_app_coverages_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appStoreVersions/{id}/routingAppCoverage'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_versions_update_instance(client):
    """Test case for app_store_versions_update_instance

    
    """
    body = {"data":{"relationships":{"build":{"data":{"id":"id","type":"builds"}}},"attributes":{"copyright":"copyright","downloadable":True,"earliestReleaseDate":"2000-01-23T04:56:07.000+00:00","usesIdfa":True,"versionString":"versionString","releaseType":"MANUAL"},"id":"id","type":"appStoreVersions"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/appStoreVersions/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

