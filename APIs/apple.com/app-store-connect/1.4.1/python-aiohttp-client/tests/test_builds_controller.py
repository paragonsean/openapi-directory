# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_encryption_declaration_response import AppEncryptionDeclarationResponse
from openapi_server.models.app_response import AppResponse
from openapi_server.models.app_store_version_response import AppStoreVersionResponse
from openapi_server.models.beta_app_review_submission_response import BetaAppReviewSubmissionResponse
from openapi_server.models.beta_build_localizations_response import BetaBuildLocalizationsResponse
from openapi_server.models.beta_testers_response import BetaTestersResponse
from openapi_server.models.build_app_encryption_declaration_linkage_request import BuildAppEncryptionDeclarationLinkageRequest
from openapi_server.models.build_app_encryption_declaration_linkage_response import BuildAppEncryptionDeclarationLinkageResponse
from openapi_server.models.build_beta_detail_response import BuildBetaDetailResponse
from openapi_server.models.build_beta_groups_linkages_request import BuildBetaGroupsLinkagesRequest
from openapi_server.models.build_icons_response import BuildIconsResponse
from openapi_server.models.build_individual_testers_linkages_request import BuildIndividualTestersLinkagesRequest
from openapi_server.models.build_individual_testers_linkages_response import BuildIndividualTestersLinkagesResponse
from openapi_server.models.build_response import BuildResponse
from openapi_server.models.build_update_request import BuildUpdateRequest
from openapi_server.models.builds_response import BuildsResponse
from openapi_server.models.diagnostic_signatures_response import DiagnosticSignaturesResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.perf_power_metrics_response import PerfPowerMetricsResponse
from openapi_server.models.prerelease_version_response import PrereleaseVersionResponse


pytestmark = pytest.mark.asyncio

async def test_builds_app_encryption_declaration_get_to_one_related(client):
    """Test case for builds_app_encryption_declaration_get_to_one_related

    
    """
    params = [('fields[appEncryptionDeclarations]', ['fields_app_encryption_declarations_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/builds/{id}/appEncryptionDeclaration'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_app_encryption_declaration_get_to_one_relationship(client):
    """Test case for builds_app_encryption_declaration_get_to_one_relationship

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/builds/{id}/relationships/appEncryptionDeclaration'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_app_encryption_declaration_update_to_one_relationship(client):
    """Test case for builds_app_encryption_declaration_update_to_one_relationship

    
    """
    body = {"data":{"id":"id","type":"appEncryptionDeclarations"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/builds/{id}/relationships/appEncryptionDeclaration'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_app_get_to_one_related(client):
    """Test case for builds_app_get_to_one_related

    
    """
    params = [('fields[apps]', ['fields_apps_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/builds/{id}/app'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_app_store_version_get_to_one_related(client):
    """Test case for builds_app_store_version_get_to_one_related

    
    """
    params = [('fields[appStoreVersions]', ['fields_app_store_versions_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/builds/{id}/appStoreVersion'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_beta_app_review_submission_get_to_one_related(client):
    """Test case for builds_beta_app_review_submission_get_to_one_related

    
    """
    params = [('fields[betaAppReviewSubmissions]', ['fields_beta_app_review_submissions_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/builds/{id}/betaAppReviewSubmission'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_beta_build_localizations_get_to_many_related(client):
    """Test case for builds_beta_build_localizations_get_to_many_related

    
    """
    params = [('fields[betaBuildLocalizations]', ['fields_beta_build_localizations_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/builds/{id}/betaBuildLocalizations'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_beta_groups_create_to_many_relationship(client):
    """Test case for builds_beta_groups_create_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"betaGroups"},{"id":"id","type":"betaGroups"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/builds/{id}/relationships/betaGroups'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_beta_groups_delete_to_many_relationship(client):
    """Test case for builds_beta_groups_delete_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"betaGroups"},{"id":"id","type":"betaGroups"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/builds/{id}/relationships/betaGroups'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_build_beta_detail_get_to_one_related(client):
    """Test case for builds_build_beta_detail_get_to_one_related

    
    """
    params = [('fields[buildBetaDetails]', ['fields_build_beta_details_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/builds/{id}/buildBetaDetail'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_diagnostic_signatures_get_to_many_related(client):
    """Test case for builds_diagnostic_signatures_get_to_many_related

    
    """
    params = [('filter[diagnosticType]', ['filter_diagnostic_type_example']),
                    ('fields[diagnosticSignatures]', ['fields_diagnostic_signatures_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/builds/{id}/diagnosticSignatures'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_get_collection(client):
    """Test case for builds_get_collection

    
    """
    params = [('filter[betaAppReviewSubmission.betaReviewState]', ['filter_beta_app_review_submission_beta_review_state_example']),
                    ('filter[expired]', ['filter_expired_example']),
                    ('filter[preReleaseVersion.platform]', ['filter_pre_release_version_platform_example']),
                    ('filter[preReleaseVersion.version]', ['filter_pre_release_version_version_example']),
                    ('filter[processingState]', ['filter_processing_state_example']),
                    ('filter[usesNonExemptEncryption]', ['filter_uses_non_exempt_encryption_example']),
                    ('filter[version]', ['filter_version_example']),
                    ('filter[app]', ['filter_app_example']),
                    ('filter[appStoreVersion]', ['filter_app_store_version_example']),
                    ('filter[betaGroups]', ['filter_beta_groups_example']),
                    ('filter[preReleaseVersion]', ['filter_pre_release_version_example']),
                    ('filter[id]', ['filter_id_example']),
                    ('sort', ['sort_example']),
                    ('fields[builds]', ['fields_builds_example']),
                    ('limit', 56),
                    ('include', ['include_example']),
                    ('fields[appEncryptionDeclarations]', ['fields_app_encryption_declarations_example']),
                    ('fields[betaAppReviewSubmissions]', ['fields_beta_app_review_submissions_example']),
                    ('fields[buildBetaDetails]', ['fields_build_beta_details_example']),
                    ('fields[buildIcons]', ['fields_build_icons_example']),
                    ('fields[perfPowerMetrics]', ['fields_perf_power_metrics_example']),
                    ('fields[preReleaseVersions]', ['fields_pre_release_versions_example']),
                    ('fields[appStoreVersions]', ['fields_app_store_versions_example']),
                    ('fields[diagnosticSignatures]', ['fields_diagnostic_signatures_example']),
                    ('fields[betaTesters]', ['fields_beta_testers_example']),
                    ('fields[betaBuildLocalizations]', ['fields_beta_build_localizations_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit[betaBuildLocalizations]', 56),
                    ('limit[icons]', 56),
                    ('limit[individualTesters]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/builds',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_get_instance(client):
    """Test case for builds_get_instance

    
    """
    params = [('fields[builds]', ['fields_builds_example']),
                    ('include', ['include_example']),
                    ('fields[appEncryptionDeclarations]', ['fields_app_encryption_declarations_example']),
                    ('fields[betaAppReviewSubmissions]', ['fields_beta_app_review_submissions_example']),
                    ('fields[buildBetaDetails]', ['fields_build_beta_details_example']),
                    ('fields[buildIcons]', ['fields_build_icons_example']),
                    ('fields[perfPowerMetrics]', ['fields_perf_power_metrics_example']),
                    ('fields[preReleaseVersions]', ['fields_pre_release_versions_example']),
                    ('fields[appStoreVersions]', ['fields_app_store_versions_example']),
                    ('fields[diagnosticSignatures]', ['fields_diagnostic_signatures_example']),
                    ('fields[betaTesters]', ['fields_beta_testers_example']),
                    ('fields[betaBuildLocalizations]', ['fields_beta_build_localizations_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit[betaBuildLocalizations]', 56),
                    ('limit[icons]', 56),
                    ('limit[individualTesters]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/builds/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_icons_get_to_many_related(client):
    """Test case for builds_icons_get_to_many_related

    
    """
    params = [('fields[buildIcons]', ['fields_build_icons_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/builds/{id}/icons'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_individual_testers_create_to_many_relationship(client):
    """Test case for builds_individual_testers_create_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"betaTesters"},{"id":"id","type":"betaTesters"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/builds/{id}/relationships/individualTesters'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_individual_testers_delete_to_many_relationship(client):
    """Test case for builds_individual_testers_delete_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"betaTesters"},{"id":"id","type":"betaTesters"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/builds/{id}/relationships/individualTesters'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_individual_testers_get_to_many_related(client):
    """Test case for builds_individual_testers_get_to_many_related

    
    """
    params = [('fields[betaTesters]', ['fields_beta_testers_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/builds/{id}/individualTesters'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_individual_testers_get_to_many_relationship(client):
    """Test case for builds_individual_testers_get_to_many_relationship

    
    """
    params = [('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/builds/{id}/relationships/individualTesters'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_perf_power_metrics_get_to_many_related(client):
    """Test case for builds_perf_power_metrics_get_to_many_related

    
    """
    params = [('filter[deviceType]', ['filter_device_type_example']),
                    ('filter[metricType]', ['filter_metric_type_example']),
                    ('filter[platform]', ['filter_platform_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/builds/{id}/perfPowerMetrics'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_pre_release_version_get_to_one_related(client):
    """Test case for builds_pre_release_version_get_to_one_related

    
    """
    params = [('fields[preReleaseVersions]', ['fields_pre_release_versions_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/builds/{id}/preReleaseVersion'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_update_instance(client):
    """Test case for builds_update_instance

    
    """
    body = {"data":{"relationships":{"appEncryptionDeclaration":{"data":{"id":"id","type":"appEncryptionDeclarations"}}},"attributes":{"expired":True,"usesNonExemptEncryption":True},"id":"id","type":"builds"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/builds/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

