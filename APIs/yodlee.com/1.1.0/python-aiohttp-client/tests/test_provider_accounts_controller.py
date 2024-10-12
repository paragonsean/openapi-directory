# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.provider_account_detail_response import ProviderAccountDetailResponse
from openapi_server.models.provider_account_preferences_request import ProviderAccountPreferencesRequest
from openapi_server.models.provider_account_request import ProviderAccountRequest
from openapi_server.models.provider_account_response import ProviderAccountResponse
from openapi_server.models.provider_account_user_profile_response import ProviderAccountUserProfileResponse
from openapi_server.models.updated_provider_account_response import UpdatedProviderAccountResponse
from openapi_server.models.yodlee_error import YodleeError


pytestmark = pytest.mark.asyncio

async def test_delete_provider_account(client):
    """Test case for delete_provider_account

    Delete Provider Account
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='DELETE',
        path='/providerAccounts/{provider_account_id}'.format(provider_account_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_credentials_or_refresh_provider_account(client):
    """Test case for edit_credentials_or_refresh_provider_account

    Update Account
    """
    body = {"consentId":0,"preferences":{"isDataExtractsEnabled":True,"linkedProviderAccountId":1,"isAutoRefreshEnabled":True},"aggregationSource":"SYSTEM","field":[{"image":"image","prefix":"prefix","minLength":5,"valueEditable":"valueEditable","isOptional":True,"suffix":"suffix","type":"text","isValueProvided":True,"name":"name","id":"id","value":"value","maxLength":5,"option":[{"displayText":"displayText","optionValue":"optionValue","isSelected":True},{"displayText":"displayText","optionValue":"optionValue","isSelected":True}]},{"image":"image","prefix":"prefix","minLength":5,"valueEditable":"valueEditable","isOptional":True,"suffix":"suffix","type":"text","isValueProvided":True,"name":"name","id":"id","value":"value","maxLength":5,"option":[{"displayText":"displayText","optionValue":"optionValue","isSelected":True},{"displayText":"displayText","optionValue":"optionValue","isSelected":True}]}],"datasetName":["BASIC_AGG_DATA","BASIC_AGG_DATA"],"dataset":[{"name":"BASIC_AGG_DATA","attribute":[{"container":["bank","bank"],"fromDate":"fromDate","toFinYear":"toFinYear","fromFinYear":"fromFinYear","containerAttributes":{"BANK":{"fullAccountNumberFields":["paymentAccountNumber","paymentAccountNumber"],"numberOfTransactionDays":6},"LOAN":{"fullAccountNumberFields":["paymentAccountNumber","paymentAccountNumber"],"numberOfTransactionDays":6},"CREDITCARD":{"fullAccountNumberFields":["paymentAccountNumber","paymentAccountNumber"],"numberOfTransactionDays":6},"INVESTMENT":{"fullAccountNumberFields":["paymentAccountNumber","paymentAccountNumber"],"numberOfTransactionDays":6},"INSURANCE":{"fullAccountNumberFields":["paymentAccountNumber","paymentAccountNumber"],"numberOfTransactionDays":6}},"toDate":"toDate","name":"BASIC_ACCOUNT_INFO"},{"container":["bank","bank"],"fromDate":"fromDate","toFinYear":"toFinYear","fromFinYear":"fromFinYear","containerAttributes":{"BANK":{"fullAccountNumberFields":["paymentAccountNumber","paymentAccountNumber"],"numberOfTransactionDays":6},"LOAN":{"fullAccountNumberFields":["paymentAccountNumber","paymentAccountNumber"],"numberOfTransactionDays":6},"CREDITCARD":{"fullAccountNumberFields":["paymentAccountNumber","paymentAccountNumber"],"numberOfTransactionDays":6},"INVESTMENT":{"fullAccountNumberFields":["paymentAccountNumber","paymentAccountNumber"],"numberOfTransactionDays":6},"INSURANCE":{"fullAccountNumberFields":["paymentAccountNumber","paymentAccountNumber"],"numberOfTransactionDays":6}},"toDate":"toDate","name":"BASIC_ACCOUNT_INFO"}]},{"name":"BASIC_AGG_DATA","attribute":[{"container":["bank","bank"],"fromDate":"fromDate","toFinYear":"toFinYear","fromFinYear":"fromFinYear","containerAttributes":{"BANK":{"fullAccountNumberFields":["paymentAccountNumber","paymentAccountNumber"],"numberOfTransactionDays":6},"LOAN":{"fullAccountNumberFields":["paymentAccountNumber","paymentAccountNumber"],"numberOfTransactionDays":6},"CREDITCARD":{"fullAccountNumberFields":["paymentAccountNumber","paymentAccountNumber"],"numberOfTransactionDays":6},"INVESTMENT":{"fullAccountNumberFields":["paymentAccountNumber","paymentAccountNumber"],"numberOfTransactionDays":6},"INSURANCE":{"fullAccountNumberFields":["paymentAccountNumber","paymentAccountNumber"],"numberOfTransactionDays":6}},"toDate":"toDate","name":"BASIC_ACCOUNT_INFO"},{"container":["bank","bank"],"fromDate":"fromDate","toFinYear":"toFinYear","fromFinYear":"fromFinYear","containerAttributes":{"BANK":{"fullAccountNumberFields":["paymentAccountNumber","paymentAccountNumber"],"numberOfTransactionDays":6},"LOAN":{"fullAccountNumberFields":["paymentAccountNumber","paymentAccountNumber"],"numberOfTransactionDays":6},"CREDITCARD":{"fullAccountNumberFields":["paymentAccountNumber","paymentAccountNumber"],"numberOfTransactionDays":6},"INVESTMENT":{"fullAccountNumberFields":["paymentAccountNumber","paymentAccountNumber"],"numberOfTransactionDays":6},"INSURANCE":{"fullAccountNumberFields":["paymentAccountNumber","paymentAccountNumber"],"numberOfTransactionDays":6}},"toDate":"toDate","name":"BASIC_ACCOUNT_INFO"}]}]}
    params = [('providerAccountIds', 'provider_account_ids_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/providerAccounts',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_provider_accounts(client):
    """Test case for get_all_provider_accounts

    Get Provider Accounts
    """
    params = [('include', 'include_example'),
                    ('providerIds', 'provider_ids_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/providerAccounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_provider_account(client):
    """Test case for get_provider_account

    Get Provider Account Details
    """
    params = [('include', 'include_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/providerAccounts/{provider_account_id}'.format(provider_account_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_provider_account_profiles(client):
    """Test case for get_provider_account_profiles

    Get User Profile Details
    """
    params = [('providerAccountId', 'provider_account_id_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/providerAccounts/profile',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_preferences(client):
    """Test case for update_preferences

    Update Preferences
    """
    body = {"preferences":{"isDataExtractsEnabled":True,"linkedProviderAccountId":1,"isAutoRefreshEnabled":True}}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/providerAccounts/{provider_account_id}/preferences'.format(provider_account_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

