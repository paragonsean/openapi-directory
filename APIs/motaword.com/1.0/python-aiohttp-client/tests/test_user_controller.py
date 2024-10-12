# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.active_widget import ActiveWidget
from openapi_server.models.client_project_stats import ClientProjectStats
from openapi_server.models.earnings import Earnings
from openapi_server.models.email import Email
from openapi_server.models.error import Error
from openapi_server.models.filter_vendor_request import FilterVendorRequest
from openapi_server.models.location_update_content import LocationUpdateContent
from openapi_server.models.notification_subscription import NotificationSubscription
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.password_update_content import PasswordUpdateContent
from openapi_server.models.payment_info import PaymentInfo
from openapi_server.models.permission_list import PermissionList
from openapi_server.models.popular_language_pairs import PopularLanguagePairs
from openapi_server.models.profile_picture_upload import ProfilePictureUpload
from openapi_server.models.responsivity_list import ResponsivityList
from openapi_server.models.send_email_confirmation200_response import SendEmailConfirmation200Response
from openapi_server.models.send_user_email_confirmation200_response import SendUserEmailConfirmation200Response
from openapi_server.models.send_user_email_confirmation202_response import SendUserEmailConfirmation202Response
from openapi_server.models.stats import Stats
from openapi_server.models.suspend_user_request import SuspendUserRequest
from openapi_server.models.update_payment_info import UpdatePaymentInfo
from openapi_server.models.user import User
from openapi_server.models.user_group_list import UserGroupList
from openapi_server.models.user_list import UserList
from openapi_server.models.user_update_content import UserUpdateContent
from openapi_server.models.vendor_tag import VendorTag


pytestmark = pytest.mark.asyncio

async def test_approve_vendor_application(client):
    """Test case for approve_vendor_application

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{user_id}/approve'.format(user_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_user(client):
    """Test case for create_user

    Create a new user
    """
    body = {"birthday":"2000-01-23","country":"country","language_pairs":[{"source_language":"source_language","target_language":"target_language"},{"source_language":"source_language","target_language":"target_language"}],"do_not_contact":True,"city":"city","timezone":"timezone","last_seen_online_at":9,"created_at":2,"locale":"locale","mailing":{"zip":"zip","country":"country","city":"city","phone":"phone","street":"street","state":"state"},"zip_code":"zip_code","billing":{"zip":"zip","country":"country","city":"city","phone":"phone","street":"street","name":"","state":"state"},"profile_picture_path":"profile_picture_path","street":"street","vendor":{"is_proofreader":True,"language_pairs":[{"source_language":"source_language","target_language":"target_language"},{"source_language":"source_language","target_language":"target_language"}],"tms_user_name":"tms_user_name","is_frozen":True,"native_language":"native_language","paypal_email":"paypal_email","require_1099":True,"tags":[null,null],"can_work_manual_files":True,"email_open_rate":7.386282,"pam_tqs":1.2315135,"profile_survey":{"provides_postedit_service":"provides_postedit_service","software":"software","translator_association":"translator_association","sdl_trados":"sdl_trados","smartling":"smartling","transsuite_2000":"transsuite_2000","dtp_software":"dtp_software","is_sworn_translator":"is_sworn_translator","daily_translation_capacity":"daily_translation_capacity","experience":"experience","working_timezone":"working_timezone","vendor_profile_lsp":"vendor_profile_lsp","subtitle_edit":"subtitle_edit","reference":"reference","skype_id":"skype_id","is_certified_translator":"is_certified_translator","memoq":"memoq","smartcat":"smartcat","wordbee":"wordbee","wordfast":"wordfast","memsource":"memsource","subtitle_workshop":"subtitle_workshop","xbench":"xbench","work_type":"work_type","omegat":"omegat","current_services":"current_services","xtm":"xtm","daily_proofreading_capacity":"daily_proofreading_capacity","work_with":"work_with","proofreader_experience":"proofreader_experience","specialization":"specialization","working_as":"working_as","provides_creative_writing_service":"provides_creative_writing_service"},"vendor_type":"vendor_type"},"has_pwd":True,"client":{"nps":1.4658129,"corporate":{"name":"name","logo":"logo","phone_number":"phone_number","id":6,"email":"email"},"subjects":{"key":5}},"links":{"projects":{"href":"href"},"stats":{"href":"href"},"login_as":{"href":"href"},"self":{"href":"href"},"responsivity":{"href":"href"}},"id":7,"state":"state","first_name":"first_name","email":"email","is_proofreader":True,"tms_user_name":"tms_user_name","native_language":"native_language","last_name":"last_name","is_prospect":True,"nps":3.6160767,"can_work_manual_files":True,"corporate_id":5,"is_sales_person":True,"name":"name","is_vendor":True,"phone_number":"phone_number","is_client":True,"is_developer":True,"social_media":{"facebook_url":"facebook_url","linkedIn_url":"linkedIn_url","twitter_url":"twitter_url"},"status":"status","user_groups":[{"permissions":["permissions","permissions"],"corporate_id":2,"name":"name","id":4},{"permissions":["permissions","permissions"],"corporate_id":2,"name":"name","id":4}]}
    params = [('notify', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_account(client):
    """Test case for delete_account

    Delete your account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/delete-account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user_account(client):
    """Test case for delete_user_account

    Delete requester account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{user_id}/delete-account'.format(user_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_downgrade_proofreader(client):
    """Test case for downgrade_proofreader

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/downgrade-proofreader',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_downgrade_user_proofreader(client):
    """Test case for downgrade_user_proofreader

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{user_id}/downgrade-proofreader'.format(user_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_freeze_account(client):
    """Test case for freeze_account

    Freeze account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/freeze-account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_freeze_user_account(client):
    """Test case for freeze_user_account

    Freeze requester account for project notifications
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{user_id}/freeze-account'.format(user_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_vendor_tags(client):
    """Test case for get_all_vendor_tags

    Returns all vendor tags for vendors filter
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/tags',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_earnings(client):
    """Test case for get_earnings

    View your vendor earnings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/earnings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_filtered_vendors(client):
    """Test case for get_filtered_vendors

    Filter vendors based on provided parameters
    """
    body = {"country":["country","country"],"translator_association":"translator_association","dtp_software":["dtp_software","dtp_software"],"experience":["experience","experience"],"vendor_profile_lsp":"vendor_profile_lsp","subtitle_edit":4,"reference":"reference","skype_id":"skype_id","is_certified_translator":True,"id":[7,7],"memsource":2,"user_working_timezone":["user_working_timezone","user_working_timezone"],"work_type":"work_type","destination_languages":[2,2],"omegat":7,"last_online":"last_online","quote_file_subjects":["quote_file_subjects","quote_file_subjects"],"daily_proofreading_capacity":5,"work_with":"work_with","specialization":["specialization","specialization"],"working_as":["working_as","working_as"],"vendor_tags":["vendor_tags","vendor_tags"],"status":["status","status"],"provides_postedit_service":True,"communication_channel":["communication_channel","communication_channel"],"project_count":1,"clients":[0,0],"language_pairs":[[9,9],[9,9]],"min_tqs":4.145608029883936,"sdl_trados":1,"smartling":7,"transsuite_2000":9,"created_at":"created_at","is_sworn_translator":True,"daily_translation_capacity":5,"search":"search","word_count":9,"memoq":3,"smartcat":6,"wordbee":6,"first_name":"first_name","last_worked":"last_worked","corporates":[1,1],"vendor_type":["vendor_type","vendor_type"],"wordfast":8,"subtitle_workshop":5,"vendor_working_timezone":["vendor_working_timezone","vendor_working_timezone"],"xbench":9,"last_name":"last_name","current_services":["current_services","current_services"],"corporate_ids_for_auth":[6,6],"xtm":6,"email_address":"email_address","proofreader_experience":1,"source_languages":[1,1],"provides_creative_writing_service":True}
    params = [('page', 56),
                    ('per_page', 56),
                    ('order_by', 'order_by_example'),
                    ('order', 'order_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/filter',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_me(client):
    """Test case for get_me

    View your account info
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_info(client):
    """Test case for get_payment_info

    View your payment and billing info
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/payment',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_permissions(client):
    """Test case for get_permissions

    View your permissions
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/permissions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_responsivity(client):
    """Test case for get_responsivity

    View your vendor responsiveness
    """
    params = [('period', monthly)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/responsivity',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_stats(client):
    """Test case for get_stats

    View your account statistics
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_this_user_groups(client):
    """Test case for get_this_user_groups

    Returns a list of user groups that this user belongs to.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{user_id}/user-groups'.format(user_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user(client):
    """Test case for get_user

    Get user information, including client or vendor specific info.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{user_id}'.format(user_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_earnings(client):
    """Test case for get_user_earnings

    Returns your vendor earnings. Includes real-time earnings from ongoing projects, and fixed earnings from completed projects. Also includes total earnings and string edits.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{user_id}/earnings'.format(user_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_groups(client):
    """Test case for get_user_groups

    View your user groups
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/user-groups',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_payment_info(client):
    """Test case for get_user_payment_info

    View user's payment and billing info
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{user_id}/payment'.format(user_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_permissions(client):
    """Test case for get_user_permissions

    Returns a list of permissions that this user is authorized for.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{user_id}/permissions'.format(user_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_popular_pairs(client):
    """Test case for get_user_popular_pairs

    Returns the language pairs that the user has ordered most.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{user_id}/stats/popular-pairs'.format(user_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_project_stats(client):
    """Test case for get_user_project_stats

    Returns a user's project statistics.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{user_id}/stats/projects'.format(user_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_responsivity(client):
    """Test case for get_user_responsivity

    Returns a user's vendor responsivity stats
    """
    params = [('period', monthly)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{user_id}/responsivity'.format(user_id=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_stats(client):
    """Test case for get_user_stats

    Returns a user's client and vendor statistics. This used to be called \"summary\" (\\@deprecated).
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{user_id}/stats'.format(user_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users(client):
    """Test case for get_users

    Get a list of platform users
    """
    params = [('page', 1),
                    ('per_page', 10),
                    ('user_type', all),
                    ('search', 'search_example'),
                    ('email', 'email_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_log_location(client):
    """Test case for log_location

    Log user's current location. This data is used in our Intelligent Project Manager for various data analysis, including project prioritization for vendors and account validation.
    """
    body = {"lon":6.0274563,"lat":0.8008282,"timestamp":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/location',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_make_proofreader(client):
    """Test case for make_proofreader

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/make-proofreader',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_make_user_proofreader(client):
    """Test case for make_user_proofreader

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{user_id}/make-proofreader'.format(user_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reject_vendor_application(client):
    """Test case for reject_vendor_application

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{user_id}/reject'.format(user_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_email_confirmation(client):
    """Test case for send_email_confirmation

    Sends email confirmation email for current user
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/resend-email-confirmation',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_password_reminder(client):
    """Test case for send_password_reminder

    Sends password reset email to the user's registered email address
    """
    body = {"email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/send-password-reminder',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_user_email_confirmation(client):
    """Test case for send_user_email_confirmation

    Sends email confirmation email for a user
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{user_id}/resend-email-confirmation'.format(user_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscribe_notification(client):
    """Test case for subscribe_notification

    Subscribe to push notifications
    """
    body = {"endpoint":"endpoint","type":"OneSignal","device":"iOS"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/notifications/subscribe',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscribe_user_notification(client):
    """Test case for subscribe_user_notification

    
    """
    body = {"endpoint":"endpoint","type":"OneSignal","device":"iOS"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{user_id}/notifications/subscribe'.format(user_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suspend_user(client):
    """Test case for suspend_user

    
    """
    body = {"reason":"reason"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{user_id}/suspend'.format(user_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unfreeze_account(client):
    """Test case for unfreeze_account

    Defreeze your account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/unfreeze-account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unfreeze_user_account(client):
    """Test case for unfreeze_user_account

    Unfreeze requester account for project notifications
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{user_id}/unfreeze-account'.format(user_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unsubscribe_notification(client):
    """Test case for unsubscribe_notification

    
    """
    body = {"endpoint":"endpoint","type":"OneSignal","device":"iOS"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/notifications/unsubscribe',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unsubscribe_user_notification(client):
    """Test case for unsubscribe_user_notification

    
    """
    body = {"endpoint":"endpoint","type":"OneSignal","device":"iOS"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{user_id}/notifications/unsubscribe'.format(user_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_me(client):
    """Test case for update_me

    Update your account info
    """
    body = {"zip":"zip","birthday":"2000-01-23","country":"country","city":"city","paypal_email":"paypal_email","last_name":"last_name","require_1099":True,"notify":True,"phone":"phone","street":"street","state":"state","id":0,"first_name":"first_name","email":"email","notifications":{"sms_enabled":True,"phone_number":"phone_number"},"user_groups":[6,6]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/me',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_password(client):
    """Test case for update_password

    Update your account password
    """
    body = {"password":"password"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/password',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_payment_info(client):
    """Test case for update_payment_info

    Update payment info
    """
    body = {"zip":"zip","country":"country","save_as_corporate_primary":True,"stripeToken":"stripeToken","city":"city","phone":"phone","street":"street","bin":"bin","share_with_corporate_users":True,"state":"state"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/payment',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_user(client):
    """Test case for update_user

    
    """
    body = {"zip":"zip","birthday":"2000-01-23","country":"country","city":"city","paypal_email":"paypal_email","last_name":"last_name","require_1099":True,"notify":True,"phone":"phone","street":"street","state":"state","id":0,"first_name":"first_name","email":"email","notifications":{"sms_enabled":True,"phone_number":"phone_number"},"user_groups":[6,6]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{user_id}'.format(user_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_user_group(client):
    """Test case for update_user_group

    
    """
    body = {"debug_mode":True,"restricted_domains":"restricted_domains","created_at":"2000-01-23T04:56:07.000+00:00","use_cache":True,"reboot_on_url_change":True,"admin_mode":True,"pages":"pages","query_name":"locale","test_mode":True,"theme":"theme","url_mode":"url_mode","id":0,"url_change_mode":"url_change_mode","live":True,"allow_query_in_url":True,"force_cache_refresh_interval":True,"path_regex":"path_regex","variables":"variables","hit_backend_for_existing":True,"use_dummy_translations":True,"modify_links":True,"sections":"sections","token":"token","language_mappings":"language_mappings","allow_hash_in_url":True,"follow_user":True,"auto_detect_source_language":True,"elements":"elements","name":"name","position":"position","optimize_per_page":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{user_id}/user-groups'.format(user_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_user_payment_info(client):
    """Test case for update_user_payment_info

    Update user payment info
    """
    body = {"cards":[{"bin":"bin","id":0,"is_default":True,"payment_code":"payment_code"},{"bin":"bin","id":0,"is_default":True,"payment_code":"payment_code"}],"shared_card":{"bin":"bin","id":0,"is_default":True,"payment_code":"payment_code"},"corporate":{"auto_charge":True,"allow_api_invoicing":True,"allow_payment_code":True,"contact_email_address":"contact_email_address","card":{"bin":"bin","id":0,"is_default":True,"payment_code":"payment_code"},"billing":{"zip":"zip","country":"country","city":"city","phone":"phone","street":"street","name":"","state":"state"},"payment_code":"payment_code"},"card":{"bin":"bin","id":0,"is_default":True,"payment_code":"payment_code"},"billing":{"zip":"zip","country":"country","city":"city","phone":"phone","street":"street","name":"","state":"state"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{user_id}/payment'.format(user_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_upload_profile_picture(client):
    """Test case for upload_profile_picture

    Upload profile picture
    """
    body = {"profile_picture":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/profile-picture',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_upload_user_profile_picture(client):
    """Test case for upload_user_profile_picture

    
    """
    body = {"profile_picture":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{user_id}/profile-picture'.format(user_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

