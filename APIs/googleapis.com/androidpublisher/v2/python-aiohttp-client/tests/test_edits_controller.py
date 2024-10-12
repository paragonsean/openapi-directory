# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apk import Apk
from openapi_server.models.apk_listing import ApkListing
from openapi_server.models.apk_listings_list_response import ApkListingsListResponse
from openapi_server.models.apks_add_externally_hosted_request import ApksAddExternallyHostedRequest
from openapi_server.models.apks_add_externally_hosted_response import ApksAddExternallyHostedResponse
from openapi_server.models.apks_list_response import ApksListResponse
from openapi_server.models.app_details import AppDetails
from openapi_server.models.app_edit import AppEdit
from openapi_server.models.bundle import Bundle
from openapi_server.models.bundles_list_response import BundlesListResponse
from openapi_server.models.deobfuscation_files_upload_response import DeobfuscationFilesUploadResponse
from openapi_server.models.expansion_file import ExpansionFile
from openapi_server.models.expansion_files_upload_response import ExpansionFilesUploadResponse
from openapi_server.models.images_delete_all_response import ImagesDeleteAllResponse
from openapi_server.models.images_list_response import ImagesListResponse
from openapi_server.models.images_upload_response import ImagesUploadResponse
from openapi_server.models.listing import Listing
from openapi_server.models.listings_list_response import ListingsListResponse
from openapi_server.models.testers import Testers
from openapi_server.models.track import Track
from openapi_server.models.tracks_list_response import TracksListResponse


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_apklistings_delete(client):
    """Test case for androidpublisher_edits_apklistings_delete

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/apks/{apk_version_code}/listings/{language}'.format(package_name='package_name_example', edit_id='edit_id_example', apk_version_code=56, language='language_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_apklistings_deleteall(client):
    """Test case for androidpublisher_edits_apklistings_deleteall

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/apks/{apk_version_code}/listings'.format(package_name='package_name_example', edit_id='edit_id_example', apk_version_code=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_apklistings_get(client):
    """Test case for androidpublisher_edits_apklistings_get

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/apks/{apk_version_code}/listings/{language}'.format(package_name='package_name_example', edit_id='edit_id_example', apk_version_code=56, language='language_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_apklistings_list(client):
    """Test case for androidpublisher_edits_apklistings_list

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/apks/{apk_version_code}/listings'.format(package_name='package_name_example', edit_id='edit_id_example', apk_version_code=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_apklistings_patch(client):
    """Test case for androidpublisher_edits_apklistings_patch

    
    """
    body = {"recentChanges":"recentChanges","language":"language"}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/apks/{apk_version_code}/listings/{language}'.format(package_name='package_name_example', edit_id='edit_id_example', apk_version_code=56, language='language_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_apklistings_update(client):
    """Test case for androidpublisher_edits_apklistings_update

    
    """
    body = {"recentChanges":"recentChanges","language":"language"}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/apks/{apk_version_code}/listings/{language}'.format(package_name='package_name_example', edit_id='edit_id_example', apk_version_code=56, language='language_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_apks_addexternallyhosted(client):
    """Test case for androidpublisher_edits_apks_addexternallyhosted

    
    """
    body = {"externallyHostedApk":{"usesFeatures":["usesFeatures","usesFeatures"],"fileSha1Base64":"fileSha1Base64","minimumSdk":6,"maximumSdk":0,"versionName":"versionName","versionCode":5,"applicationLabel":"applicationLabel","fileSize":"fileSize","certificateBase64s":["certificateBase64s","certificateBase64s"],"externallyHostedUrl":"externallyHostedUrl","iconBase64":"iconBase64","packageName":"packageName","nativeCodes":["nativeCodes","nativeCodes"],"usesPermissions":[{"maxSdkVersion":1,"name":"name"},{"maxSdkVersion":1,"name":"name"}],"fileSha256Base64":"fileSha256Base64"}}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/apks/externallyHosted'.format(package_name='package_name_example', edit_id='edit_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_apks_list(client):
    """Test case for androidpublisher_edits_apks_list

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/apks'.format(package_name='package_name_example', edit_id='edit_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_apks_upload(client):
    """Test case for androidpublisher_edits_apks_upload

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/apks'.format(package_name='package_name_example', edit_id='edit_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_bundles_list(client):
    """Test case for androidpublisher_edits_bundles_list

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/bundles'.format(package_name='package_name_example', edit_id='edit_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_bundles_upload(client):
    """Test case for androidpublisher_edits_bundles_upload

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('ackBundleInstallationWarning', True)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/bundles'.format(package_name='package_name_example', edit_id='edit_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_commit(client):
    """Test case for androidpublisher_edits_commit

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_idcommi}'.format(package_name='package_name_example', edit_id='edit_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_delete(client):
    """Test case for androidpublisher_edits_delete

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}'.format(package_name='package_name_example', edit_id='edit_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_deobfuscationfiles_upload(client):
    """Test case for androidpublisher_edits_deobfuscationfiles_upload

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/apks/{apk_version_code}/deobfuscationFiles/{deobfuscation_file_type}'.format(package_name='package_name_example', edit_id='edit_id_example', apk_version_code=56, deobfuscation_file_type='deobfuscation_file_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_details_get(client):
    """Test case for androidpublisher_edits_details_get

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/details'.format(package_name='package_name_example', edit_id='edit_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_details_patch(client):
    """Test case for androidpublisher_edits_details_patch

    
    """
    body = {"defaultLanguage":"defaultLanguage","contactEmail":"contactEmail","contactWebsite":"contactWebsite","contactPhone":"contactPhone"}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/details'.format(package_name='package_name_example', edit_id='edit_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_details_update(client):
    """Test case for androidpublisher_edits_details_update

    
    """
    body = {"defaultLanguage":"defaultLanguage","contactEmail":"contactEmail","contactWebsite":"contactWebsite","contactPhone":"contactPhone"}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/details'.format(package_name='package_name_example', edit_id='edit_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_expansionfiles_get(client):
    """Test case for androidpublisher_edits_expansionfiles_get

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/apks/{apk_version_code}/expansionFiles/{expansion_file_type}'.format(package_name='package_name_example', edit_id='edit_id_example', apk_version_code=56, expansion_file_type='expansion_file_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_expansionfiles_patch(client):
    """Test case for androidpublisher_edits_expansionfiles_patch

    
    """
    body = {"fileSize":"fileSize","referencesVersion":0}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/apks/{apk_version_code}/expansionFiles/{expansion_file_type}'.format(package_name='package_name_example', edit_id='edit_id_example', apk_version_code=56, expansion_file_type='expansion_file_type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_expansionfiles_update(client):
    """Test case for androidpublisher_edits_expansionfiles_update

    
    """
    body = {"fileSize":"fileSize","referencesVersion":0}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/apks/{apk_version_code}/expansionFiles/{expansion_file_type}'.format(package_name='package_name_example', edit_id='edit_id_example', apk_version_code=56, expansion_file_type='expansion_file_type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_expansionfiles_upload(client):
    """Test case for androidpublisher_edits_expansionfiles_upload

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/apks/{apk_version_code}/expansionFiles/{expansion_file_type}'.format(package_name='package_name_example', edit_id='edit_id_example', apk_version_code=56, expansion_file_type='expansion_file_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_get(client):
    """Test case for androidpublisher_edits_get

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}'.format(package_name='package_name_example', edit_id='edit_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_images_delete(client):
    """Test case for androidpublisher_edits_images_delete

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/listings/{language}/{image_type}/{image_id}'.format(package_name='package_name_example', edit_id='edit_id_example', language='language_example', image_type='image_type_example', image_id='image_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_images_deleteall(client):
    """Test case for androidpublisher_edits_images_deleteall

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/listings/{language}/{image_type}'.format(package_name='package_name_example', edit_id='edit_id_example', language='language_example', image_type='image_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_images_list(client):
    """Test case for androidpublisher_edits_images_list

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/listings/{language}/{image_type}'.format(package_name='package_name_example', edit_id='edit_id_example', language='language_example', image_type='image_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_images_upload(client):
    """Test case for androidpublisher_edits_images_upload

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/listings/{language}/{image_type}'.format(package_name='package_name_example', edit_id='edit_id_example', language='language_example', image_type='image_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_insert(client):
    """Test case for androidpublisher_edits_insert

    
    """
    body = {"expiryTimeSeconds":"expiryTimeSeconds","id":"id"}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v2/applications/{package_name}/edits'.format(package_name='package_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_listings_delete(client):
    """Test case for androidpublisher_edits_listings_delete

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/listings/{language}'.format(package_name='package_name_example', edit_id='edit_id_example', language='language_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_listings_deleteall(client):
    """Test case for androidpublisher_edits_listings_deleteall

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/listings'.format(package_name='package_name_example', edit_id='edit_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_listings_get(client):
    """Test case for androidpublisher_edits_listings_get

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/listings/{language}'.format(package_name='package_name_example', edit_id='edit_id_example', language='language_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_listings_list(client):
    """Test case for androidpublisher_edits_listings_list

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/listings'.format(package_name='package_name_example', edit_id='edit_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_listings_patch(client):
    """Test case for androidpublisher_edits_listings_patch

    
    """
    body = {"language":"language","shortDescription":"shortDescription","video":"video","fullDescription":"fullDescription","title":"title"}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/listings/{language}'.format(package_name='package_name_example', edit_id='edit_id_example', language='language_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_listings_update(client):
    """Test case for androidpublisher_edits_listings_update

    
    """
    body = {"language":"language","shortDescription":"shortDescription","video":"video","fullDescription":"fullDescription","title":"title"}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/listings/{language}'.format(package_name='package_name_example', edit_id='edit_id_example', language='language_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_testers_get(client):
    """Test case for androidpublisher_edits_testers_get

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/testers/{track}'.format(package_name='package_name_example', edit_id='edit_id_example', track='track_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_testers_patch(client):
    """Test case for androidpublisher_edits_testers_patch

    
    """
    body = {"googleGroups":["googleGroups","googleGroups"]}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/testers/{track}'.format(package_name='package_name_example', edit_id='edit_id_example', track='track_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_testers_update(client):
    """Test case for androidpublisher_edits_testers_update

    
    """
    body = {"googleGroups":["googleGroups","googleGroups"]}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/testers/{track}'.format(package_name='package_name_example', edit_id='edit_id_example', track='track_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_tracks_get(client):
    """Test case for androidpublisher_edits_tracks_get

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/tracks/{track}'.format(package_name='package_name_example', edit_id='edit_id_example', track='track_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_tracks_list(client):
    """Test case for androidpublisher_edits_tracks_list

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/tracks'.format(package_name='package_name_example', edit_id='edit_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_tracks_patch(client):
    """Test case for androidpublisher_edits_tracks_patch

    
    """
    body = {"userFraction":0.8008281904610115,"versionCodes":[6,6],"track":"track"}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/tracks/{track}'.format(package_name='package_name_example', edit_id='edit_id_example', track='track_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_tracks_update(client):
    """Test case for androidpublisher_edits_tracks_update

    
    """
    body = {"userFraction":0.8008281904610115,"versionCodes":[6,6],"track":"track"}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_id}/tracks/{track}'.format(package_name='package_name_example', edit_id='edit_id_example', track='track_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_edits_validate(client):
    """Test case for androidpublisher_edits_validate

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v2/applications/{package_name}/edits/{edit_idvalidat}'.format(package_name='package_name_example', edit_id='edit_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

