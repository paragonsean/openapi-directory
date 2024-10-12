# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_association import GoogleCloudPrivatecatalogproducerV1beta1Association
from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_catalog import GoogleCloudPrivatecatalogproducerV1beta1Catalog
from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_copy_product_request import GoogleCloudPrivatecatalogproducerV1beta1CopyProductRequest
from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_create_association_request import GoogleCloudPrivatecatalogproducerV1beta1CreateAssociationRequest
from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_list_associations_response import GoogleCloudPrivatecatalogproducerV1beta1ListAssociationsResponse
from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_list_catalogs_response import GoogleCloudPrivatecatalogproducerV1beta1ListCatalogsResponse
from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_list_products_response import GoogleCloudPrivatecatalogproducerV1beta1ListProductsResponse
from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_list_versions_response import GoogleCloudPrivatecatalogproducerV1beta1ListVersionsResponse
from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_product import GoogleCloudPrivatecatalogproducerV1beta1Product
from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_upload_icon_request import GoogleCloudPrivatecatalogproducerV1beta1UploadIconRequest
from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_version import GoogleCloudPrivatecatalogproducerV1beta1Version
from openapi_server.models.google_iam_v1_policy import GoogleIamV1Policy
from openapi_server.models.google_iam_v1_set_iam_policy_request import GoogleIamV1SetIamPolicyRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_request import GoogleIamV1TestIamPermissionsRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_response import GoogleIamV1TestIamPermissionsResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalogproducer_catalogs_associations_create(client):
    """Test case for cloudprivatecatalogproducer_catalogs_associations_create

    
    """
    body = {"association":{"createTime":"createTime","resource":"resource","name":"name"}}
    params = [('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/associations'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalogproducer_catalogs_associations_list(client):
    """Test case for cloudprivatecatalogproducer_catalogs_associations_list

    
    """
    params = [('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/associations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalogproducer_catalogs_create(client):
    """Test case for cloudprivatecatalogproducer_catalogs_create

    
    """
    body = {"parent":"parent","createTime":"createTime","displayName":"displayName","name":"name","description":"description","updateTime":"updateTime"}
    params = [('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/catalogs',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalogproducer_catalogs_get_iam_policy(client):
    """Test case for cloudprivatecatalogproducer_catalogs_get_iam_policy

    
    """
    params = [('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example'),
                    ('options.requestedPolicyVersion', 56)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalogproducer_catalogs_list(client):
    """Test case for cloudprivatecatalogproducer_catalogs_list

    
    """
    params = [('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('parent', 'parent_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/catalogs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalogproducer_catalogs_products_copy(client):
    """Test case for cloudprivatecatalogproducer_catalogs_products_copy

    
    """
    body = {"destinationProductName":"destinationProductName"}
    params = [('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{namecop}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalogproducer_catalogs_products_create(client):
    """Test case for cloudprivatecatalogproducer_catalogs_products_create

    
    """
    body = {"displayMetadata":{"key":""},"createTime":"createTime","name":"name","updateTime":"updateTime","iconUri":"iconUri","assetType":"assetType"}
    params = [('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/products'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalogproducer_catalogs_products_icons_upload(client):
    """Test case for cloudprivatecatalogproducer_catalogs_products_icons_upload

    
    """
    body = {"icon":"icon"}
    params = [('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{product}/icons:upload'.format(product='product_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalogproducer_catalogs_products_list(client):
    """Test case for cloudprivatecatalogproducer_catalogs_products_list

    
    """
    params = [('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/products'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalogproducer_catalogs_products_versions_create(client):
    """Test case for cloudprivatecatalogproducer_catalogs_products_versions_create

    
    """
    body = {"createTime":"createTime","originalAsset":{"key":""},"name":"name","description":"description","updateTime":"updateTime","asset":{"key":""}}
    params = [('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/versions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalogproducer_catalogs_products_versions_delete(client):
    """Test case for cloudprivatecatalogproducer_catalogs_products_versions_delete

    
    """
    params = [('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example'),
                    ('force', True)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalogproducer_catalogs_products_versions_get(client):
    """Test case for cloudprivatecatalogproducer_catalogs_products_versions_get

    
    """
    params = [('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalogproducer_catalogs_products_versions_list(client):
    """Test case for cloudprivatecatalogproducer_catalogs_products_versions_list

    
    """
    params = [('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/versions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalogproducer_catalogs_products_versions_patch(client):
    """Test case for cloudprivatecatalogproducer_catalogs_products_versions_patch

    
    """
    body = {"createTime":"createTime","originalAsset":{"key":""},"name":"name","description":"description","updateTime":"updateTime","asset":{"key":""}}
    params = [('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalogproducer_catalogs_set_iam_policy(client):
    """Test case for cloudprivatecatalogproducer_catalogs_set_iam_policy

    
    """
    body = {"updateMask":"updateMask","policy":{"bindings":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]}],"etag":"etag","version":0,"auditConfigs":[{"auditLogConfigs":[{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]},{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]}],"service":"service"},{"auditLogConfigs":[{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]},{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]}],"service":"service"}]}}
    params = [('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{resourceset_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalogproducer_catalogs_test_iam_permissions(client):
    """Test case for cloudprivatecatalogproducer_catalogs_test_iam_permissions

    
    """
    body = {"permissions":["permissions","permissions"]}
    params = [('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{resourcetest_iam_permission}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalogproducer_catalogs_undelete(client):
    """Test case for cloudprivatecatalogproducer_catalogs_undelete

    
    """
    body = None
    params = [('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{nameundelet}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

