# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.associate_external_connection_result import AssociateExternalConnectionResult
from openapi_server.models.copy_package_versions_request import CopyPackageVersionsRequest
from openapi_server.models.copy_package_versions_result import CopyPackageVersionsResult
from openapi_server.models.create_domain_request import CreateDomainRequest
from openapi_server.models.create_domain_result import CreateDomainResult
from openapi_server.models.create_repository_request import CreateRepositoryRequest
from openapi_server.models.create_repository_result import CreateRepositoryResult
from openapi_server.models.delete_domain_permissions_policy_result import DeleteDomainPermissionsPolicyResult
from openapi_server.models.delete_domain_result import DeleteDomainResult
from openapi_server.models.delete_package_result import DeletePackageResult
from openapi_server.models.delete_package_versions_request import DeletePackageVersionsRequest
from openapi_server.models.delete_package_versions_result import DeletePackageVersionsResult
from openapi_server.models.delete_repository_permissions_policy_result import DeleteRepositoryPermissionsPolicyResult
from openapi_server.models.delete_repository_result import DeleteRepositoryResult
from openapi_server.models.describe_domain_result import DescribeDomainResult
from openapi_server.models.describe_package_result import DescribePackageResult
from openapi_server.models.describe_package_version_result import DescribePackageVersionResult
from openapi_server.models.describe_repository_result import DescribeRepositoryResult
from openapi_server.models.disassociate_external_connection_result import DisassociateExternalConnectionResult
from openapi_server.models.dispose_package_versions_request import DisposePackageVersionsRequest
from openapi_server.models.dispose_package_versions_result import DisposePackageVersionsResult
from openapi_server.models.get_authorization_token_result import GetAuthorizationTokenResult
from openapi_server.models.get_domain_permissions_policy_result import GetDomainPermissionsPolicyResult
from openapi_server.models.get_package_version_asset_result import GetPackageVersionAssetResult
from openapi_server.models.get_package_version_readme_result import GetPackageVersionReadmeResult
from openapi_server.models.get_repository_endpoint_result import GetRepositoryEndpointResult
from openapi_server.models.get_repository_permissions_policy_result import GetRepositoryPermissionsPolicyResult
from openapi_server.models.list_domains_request import ListDomainsRequest
from openapi_server.models.list_domains_result import ListDomainsResult
from openapi_server.models.list_package_version_assets_result import ListPackageVersionAssetsResult
from openapi_server.models.list_package_version_dependencies_result import ListPackageVersionDependenciesResult
from openapi_server.models.list_package_versions_result import ListPackageVersionsResult
from openapi_server.models.list_packages_result import ListPackagesResult
from openapi_server.models.list_repositories_in_domain_result import ListRepositoriesInDomainResult
from openapi_server.models.list_repositories_result import ListRepositoriesResult
from openapi_server.models.list_tags_for_resource_result import ListTagsForResourceResult
from openapi_server.models.publish_package_version_request import PublishPackageVersionRequest
from openapi_server.models.publish_package_version_result import PublishPackageVersionResult
from openapi_server.models.put_domain_permissions_policy_request import PutDomainPermissionsPolicyRequest
from openapi_server.models.put_domain_permissions_policy_result import PutDomainPermissionsPolicyResult
from openapi_server.models.put_package_origin_configuration_request import PutPackageOriginConfigurationRequest
from openapi_server.models.put_package_origin_configuration_result import PutPackageOriginConfigurationResult
from openapi_server.models.put_repository_permissions_policy_request import PutRepositoryPermissionsPolicyRequest
from openapi_server.models.put_repository_permissions_policy_result import PutRepositoryPermissionsPolicyResult
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_package_versions_status_request import UpdatePackageVersionsStatusRequest
from openapi_server.models.update_package_versions_status_result import UpdatePackageVersionsStatusResult
from openapi_server.models.update_repository_request import UpdateRepositoryRequest
from openapi_server.models.update_repository_result import UpdateRepositoryResult


pytestmark = pytest.mark.asyncio

async def test_associate_external_connection(client):
    """Test case for associate_external_connection

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example'),
                    ('external-connection', 'external_connection_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/repository/external-connection#domain&repository&external-connection',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_copy_package_versions(client):
    """Test case for copy_package_versions

    
    """
    body = {"versions":"","versionRevisions":"","allowOverwrite":"","includeFromUpstream":""}
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('source-repository', 'source_repository_example'),
                    ('destination-repository', 'destination_repository_example'),
                    ('format', 'format_example'),
                    ('namespace', 'namespace_example'),
                    ('package', 'package_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/package/versions/copy#domain&source-repository&destination-repository&format&package',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_domain(client):
    """Test case for create_domain

    
    """
    body = {"encryptionKey":"","tags":""}
    params = [('domain', 'domain_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/domain#domain',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_repository(client):
    """Test case for create_repository

    
    """
    body = {"upstreams":"","description":"","tags":""}
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/repository#domain&repository',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_domain(client):
    """Test case for delete_domain

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/domain#domain',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_domain_permissions_policy(client):
    """Test case for delete_domain_permissions_policy

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('policy-revision', 'policy_revision_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/domain/permissions/policy#domain',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_package(client):
    """Test case for delete_package

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example'),
                    ('format', 'format_example'),
                    ('namespace', 'namespace_example'),
                    ('package', 'package_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/package#domain&repository&format&package',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_package_versions(client):
    """Test case for delete_package_versions

    
    """
    body = {"versions":"","expectedStatus":""}
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example'),
                    ('format', 'format_example'),
                    ('namespace', 'namespace_example'),
                    ('package', 'package_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/package/versions/delete#domain&repository&format&package',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_repository(client):
    """Test case for delete_repository

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/repository#domain&repository',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_repository_permissions_policy(client):
    """Test case for delete_repository_permissions_policy

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example'),
                    ('policy-revision', 'policy_revision_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/repository/permissions/policies#domain&repository',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_domain(client):
    """Test case for describe_domain

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/domain#domain',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_package(client):
    """Test case for describe_package

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example'),
                    ('format', 'format_example'),
                    ('namespace', 'namespace_example'),
                    ('package', 'package_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/package#domain&repository&format&package',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_package_version(client):
    """Test case for describe_package_version

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example'),
                    ('format', 'format_example'),
                    ('namespace', 'namespace_example'),
                    ('package', 'package_example'),
                    ('version', 'version_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/package/version#domain&repository&format&package&version',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_repository(client):
    """Test case for describe_repository

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/repository#domain&repository',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disassociate_external_connection(client):
    """Test case for disassociate_external_connection

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example'),
                    ('external-connection', 'external_connection_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/repository/external-connection#domain&repository&external-connection',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dispose_package_versions(client):
    """Test case for dispose_package_versions

    
    """
    body = {"versions":"","versionRevisions":"","expectedStatus":""}
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example'),
                    ('format', 'format_example'),
                    ('namespace', 'namespace_example'),
                    ('package', 'package_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/package/versions/dispose#domain&repository&format&package',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_authorization_token(client):
    """Test case for get_authorization_token

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('duration', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/authorization-token#domain',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_domain_permissions_policy(client):
    """Test case for get_domain_permissions_policy

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/domain/permissions/policy#domain',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_package_version_asset(client):
    """Test case for get_package_version_asset

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example'),
                    ('format', 'format_example'),
                    ('namespace', 'namespace_example'),
                    ('package', 'package_example'),
                    ('version', 'version_example'),
                    ('asset', 'asset_example'),
                    ('revision', 'revision_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/package/version/asset#domain&repository&format&package&version&asset',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_package_version_readme(client):
    """Test case for get_package_version_readme

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example'),
                    ('format', 'format_example'),
                    ('namespace', 'namespace_example'),
                    ('package', 'package_example'),
                    ('version', 'version_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/package/version/readme#domain&repository&format&package&version',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_repository_endpoint(client):
    """Test case for get_repository_endpoint

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/repository/endpoint#domain&repository&format',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_repository_permissions_policy(client):
    """Test case for get_repository_permissions_policy

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/repository/permissions/policy#domain&repository',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_domains(client):
    """Test case for list_domains

    
    """
    body = {"maxResults":"","nextToken":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/domains',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_package_version_assets(client):
    """Test case for list_package_version_assets

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example'),
                    ('format', 'format_example'),
                    ('namespace', 'namespace_example'),
                    ('package', 'package_example'),
                    ('version', 'version_example'),
                    ('max-results', 56),
                    ('next-token', 'next_token_example'),
                    ('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/package/version/assets#domain&repository&format&package&version',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_package_version_dependencies(client):
    """Test case for list_package_version_dependencies

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example'),
                    ('format', 'format_example'),
                    ('namespace', 'namespace_example'),
                    ('package', 'package_example'),
                    ('version', 'version_example'),
                    ('next-token', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/package/version/dependencies#domain&repository&format&package&version',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_package_versions(client):
    """Test case for list_package_versions

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example'),
                    ('format', 'format_example'),
                    ('namespace', 'namespace_example'),
                    ('package', 'package_example'),
                    ('status', 'status_example'),
                    ('sortBy', 'sort_by_example'),
                    ('max-results', 56),
                    ('next-token', 'next_token_example'),
                    ('originType', 'origin_type_example'),
                    ('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/package/versions#domain&repository&format&package',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_packages(client):
    """Test case for list_packages

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example'),
                    ('format', 'format_example'),
                    ('namespace', 'namespace_example'),
                    ('package-prefix', 'package_prefix_example'),
                    ('max-results', 56),
                    ('next-token', 'next_token_example'),
                    ('publish', 'publish_example'),
                    ('upstream', 'upstream_example'),
                    ('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/packages#domain&repository',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_repositories(client):
    """Test case for list_repositories

    
    """
    params = [('repository-prefix', 'repository_prefix_example'),
                    ('max-results', 56),
                    ('next-token', 'next_token_example'),
                    ('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/repositories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_repositories_in_domain(client):
    """Test case for list_repositories_in_domain

    
    """
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('administrator-account', 'administrator_account_example'),
                    ('repository-prefix', 'repository_prefix_example'),
                    ('max-results', 56),
                    ('next-token', 'next_token_example'),
                    ('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/domain/repositories#domain',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tags_for_resource(client):
    """Test case for list_tags_for_resource

    
    """
    params = [('resourceArn', 'resource_arn_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/tags#resourceArn',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_publish_package_version(client):
    """Test case for publish_package_version

    
    """
    body = {"assetContent":""}
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example'),
                    ('format', 'format_example'),
                    ('namespace', 'namespace_example'),
                    ('package', 'package_example'),
                    ('version', 'version_example'),
                    ('asset', 'asset_example'),
                    ('unfinished', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_content_sha257': 'x_amz_content_sha256_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/package/version/publish#domain&repository&format&package&version&asset&x-amz-content-sha256',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_domain_permissions_policy(client):
    """Test case for put_domain_permissions_policy

    
    """
    body = {"policyDocument":"","domain":"","domainOwner":"","policyRevision":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/domain/permissions/policy',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_package_origin_configuration(client):
    """Test case for put_package_origin_configuration

    
    """
    body = {"restrictions":{"upstream":"","publish":""}}
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example'),
                    ('format', 'format_example'),
                    ('namespace', 'namespace_example'),
                    ('package', 'package_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/package#domain&repository&format&package',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_repository_permissions_policy(client):
    """Test case for put_repository_permissions_policy

    
    """
    body = {"policyDocument":"","policyRevision":""}
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/repository/permissions/policy#domain&repository',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_resource(client):
    """Test case for tag_resource

    
    """
    body = {"tags":""}
    params = [('resourceArn', 'resource_arn_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/tag#resourceArn',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_untag_resource(client):
    """Test case for untag_resource

    
    """
    body = {"tagKeys":""}
    params = [('resourceArn', 'resource_arn_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/untag#resourceArn',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_package_versions_status(client):
    """Test case for update_package_versions_status

    
    """
    body = {"versions":"","versionRevisions":"","expectedStatus":"","targetStatus":""}
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example'),
                    ('format', 'format_example'),
                    ('namespace', 'namespace_example'),
                    ('package', 'package_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/package/versions/update_status#domain&repository&format&package',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_repository(client):
    """Test case for update_repository

    
    """
    body = {"upstreams":"","description":""}
    params = [('domain', 'domain_example'),
                    ('domain-owner', 'domain_owner_example'),
                    ('repository', 'repository_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/repository#domain&repository',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

