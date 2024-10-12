# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_datastore_admin_v1beta1_export_entities_request import GoogleDatastoreAdminV1beta1ExportEntitiesRequest
from openapi_server.models.google_datastore_admin_v1beta1_import_entities_request import GoogleDatastoreAdminV1beta1ImportEntitiesRequest
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_export(client):
    """Test case for datastore_projects_export

    
    """
    body = {"entityFilter":{"namespaceIds":["namespaceIds","namespaceIds"],"kinds":["kinds","kinds"]},"outputUrlPrefix":"outputUrlPrefix","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/projects/{project_idexpor}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_import(client):
    """Test case for datastore_projects_import

    
    """
    body = {"entityFilter":{"namespaceIds":["namespaceIds","namespaceIds"],"kinds":["kinds","kinds"]},"inputUrl":"inputUrl","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/projects/{project_idimpor}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

