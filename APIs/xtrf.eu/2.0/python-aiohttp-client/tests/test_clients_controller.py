# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_token_dto import AccessTokenDTO
from openapi_server.models.access_token_request_dto import AccessTokenRequestDTO
from openapi_server.models.address_dto import AddressDTO
from openapi_server.models.contact_dto import ContactDTO
from openapi_server.models.custom_field_dto import CustomFieldDTO
from openapi_server.models.customer_dto import CustomerDTO
from openapi_server.models.customer_person_dto import CustomerPersonDTO
from openapi_server.models.entity_with_name_dto import EntityWithNameDTO
from openapi_server.models.person_contact_dto import PersonContactDTO


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_create2(client):
    """Test case for create2

    Creates a new person.
    """
    body = /home-api/assets/examples/customers/persons/create.json#requestBody
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/customers/persons',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create3(client):
    """Test case for create3

    Creates a new client.
    """
    body = {"limitAccessToPeopleResponsible":True,"notes":"notes","categoriesIds":[5,5],"responsiblePersons":{"projectCoordinatorId":7,"projectManagerId":1,"accountManagerId":6,"salesPersonId":4},"customFields":[{"name":"name","type":"TEXT","value":"{}","key":"key"},{"name":"name","type":"TEXT","value":"{}","key":"key"}],"accounting":{"taxNumbers":[{"number":"number","type":"type"},{"number":"number","type":"type"}]},"idNumber":"idNumber","accountOnCustomerServer":"accountOnCustomerServer","correspondenceAddress":{"city":"city","sameAsBillingAddress":True,"postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","provinceId":6,"countryId":0},"clientFirstQuoteDate":"2000-01-23T04:56:07.000+00:00","contact":{"emails":{"cc":["cc","cc"],"additional":["additional","additional"],"primary":"primary"},"sms":"sms","phones":["phones","phones"],"websites":["websites","websites"],"fax":"fax"},"clientNumberOfQuotes":2,"id":7,"clientFirstProjectDate":"2000-01-23T04:56:07.000+00:00","branchId":1,"clientLastQuoteDate":"2000-01-23T04:56:07.000+00:00","contractNumber":"contractNumber","fullName":"fullName","salesNotes":"salesNotes","industriesIds":[9,9],"persons":[{"lastName":"lastName","numberOfProjects":1,"lastProjectDate":"2000-01-23T04:56:07.000+00:00","gender":"FEMALE","customFields":[{"name":"name","type":"TEXT","value":"{}","key":"key"},{"name":"name","type":"TEXT","value":"{}","key":"key"}],"active":True,"firstProjectDate":"2000-01-23T04:56:07.000+00:00","numberOfQuotes":1,"lastQuoteDate":"2000-01-23T04:56:07.000+00:00","positionId":1,"motherTonguesIds":[7,7],"contact":{"emails":{"additional":["additional","additional"],"primary":"primary"},"sms":"sms","phones":["phones","phones"],"fax":"fax"},"customerId":2,"name":"name","firstQuoteDate":"2000-01-23T04:56:07.000+00:00","id":4},{"lastName":"lastName","numberOfProjects":1,"lastProjectDate":"2000-01-23T04:56:07.000+00:00","gender":"FEMALE","customFields":[{"name":"name","type":"TEXT","value":"{}","key":"key"},{"name":"name","type":"TEXT","value":"{}","key":"key"}],"active":True,"firstProjectDate":"2000-01-23T04:56:07.000+00:00","numberOfQuotes":1,"lastQuoteDate":"2000-01-23T04:56:07.000+00:00","positionId":1,"motherTonguesIds":[7,7],"contact":{"emails":{"additional":["additional","additional"],"primary":"primary"},"sms":"sms","phones":["phones","phones"],"fax":"fax"},"customerId":2,"name":"name","firstQuoteDate":"2000-01-23T04:56:07.000+00:00","id":4}],"name":"name","clientNumberOfProjects":5,"billingAddress":{"city":"city","sameAsBillingAddress":True,"postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","provinceId":6,"countryId":0},"clientLastProjectDate":"2000-01-23T04:56:07.000+00:00","leadSourceId":3,"status":"ACTIVE"}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/customers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete3(client):
    """Test case for delete3

    Removes a person.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/customers/persons/{person_id}'.format(person_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete4(client):
    """Test case for delete4

    Removes a customer price list.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/customers/priceLists/{price_list_id}'.format(price_list_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete5(client):
    """Test case for delete5

    Removes a client.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/customers/{customer_id}'.format(customer_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_generate_single_use_sign_in_token(client):
    """Test case for generate_single_use_sign_in_token

    Generates a single use sign-in token.
    """
    body = /home-api/assets/examples/customers/persons/generateSingleUseSignInToken.json#requestBody
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/customers/persons/accessToken',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_address(client):
    """Test case for get_address

    Returns address of a given client.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/customers/{customer_id}/address'.format(customer_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_ids1(client):
    """Test case for get_all_ids1

    Returns persons' internal identifiers.
    """
    params = [('updatedSince', 56)]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/customers/persons/ids',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_ids2(client):
    """Test case for get_all_ids2

    Returns clients' internal identifiers.
    """
    params = [('updatedSince', 56),
                    ('nameEquals', 'name_equals_example'),
                    ('emailEquals', 'email_equals_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/customers/ids',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_names_with_ids(client):
    """Test case for get_all_names_with_ids

    Returns list of simple clients representations
    """
    params = [('updatedSince', 56)]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/customers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_by_id1(client):
    """Test case for get_by_id1

    Returns person details.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/customers/persons/{person_id}'.format(person_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_by_id2(client):
    """Test case for get_by_id2

    Returns client details.
    """
    params = [('embed', 'embed_example')]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/customers/{customer_id}'.format(customer_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_categories(client):
    """Test case for get_categories

    Returns categories of a given client.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/customers/{customer_id}/categories'.format(customer_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contact(client):
    """Test case for get_contact

    Returns contact of a given person.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/customers/persons/{person_id}/contact'.format(person_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contact1(client):
    """Test case for get_contact1

    Returns contact of a given client.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/customers/{customer_id}/contact'.format(customer_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_correspondence_address(client):
    """Test case for get_correspondence_address

    Returns correspondence address of a given client.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/customers/{customer_id}/correspondenceAddress'.format(customer_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_field(client):
    """Test case for get_custom_field

    Returns custom field of a given client.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/customers/{customer_id}/customFields/{custom_field_key}'.format(customer_id=56, custom_field_key='custom_field_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_fields(client):
    """Test case for get_custom_fields

    Returns custom fields of a given person.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/customers/persons/{person_id}/customFields'.format(person_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_fields1(client):
    """Test case for get_custom_fields1

    Returns custom fields of a given client.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/customers/{customer_id}/customFields'.format(customer_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_industries(client):
    """Test case for get_industries

    Returns industries of a given client.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/customers/{customer_id}/industries'.format(customer_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_update1(client):
    """Test case for update1

    Updates an existing person.
    """
    body = /home-api/assets/examples/customers/persons/update.json#requestBody
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/customers/persons/{person_id}'.format(person_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update2(client):
    """Test case for update2

    Updates an existing client.
    """
    body = {"limitAccessToPeopleResponsible":True,"notes":"notes","categoriesIds":[5,5],"responsiblePersons":{"projectCoordinatorId":7,"projectManagerId":1,"accountManagerId":6,"salesPersonId":4},"customFields":[{"name":"name","type":"TEXT","value":"{}","key":"key"},{"name":"name","type":"TEXT","value":"{}","key":"key"}],"accounting":{"taxNumbers":[{"number":"number","type":"type"},{"number":"number","type":"type"}]},"idNumber":"idNumber","accountOnCustomerServer":"accountOnCustomerServer","correspondenceAddress":{"city":"city","sameAsBillingAddress":True,"postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","provinceId":6,"countryId":0},"clientFirstQuoteDate":"2000-01-23T04:56:07.000+00:00","contact":{"emails":{"cc":["cc","cc"],"additional":["additional","additional"],"primary":"primary"},"sms":"sms","phones":["phones","phones"],"websites":["websites","websites"],"fax":"fax"},"clientNumberOfQuotes":2,"id":7,"clientFirstProjectDate":"2000-01-23T04:56:07.000+00:00","branchId":1,"clientLastQuoteDate":"2000-01-23T04:56:07.000+00:00","contractNumber":"contractNumber","fullName":"fullName","salesNotes":"salesNotes","industriesIds":[9,9],"persons":[{"lastName":"lastName","numberOfProjects":1,"lastProjectDate":"2000-01-23T04:56:07.000+00:00","gender":"FEMALE","customFields":[{"name":"name","type":"TEXT","value":"{}","key":"key"},{"name":"name","type":"TEXT","value":"{}","key":"key"}],"active":True,"firstProjectDate":"2000-01-23T04:56:07.000+00:00","numberOfQuotes":1,"lastQuoteDate":"2000-01-23T04:56:07.000+00:00","positionId":1,"motherTonguesIds":[7,7],"contact":{"emails":{"additional":["additional","additional"],"primary":"primary"},"sms":"sms","phones":["phones","phones"],"fax":"fax"},"customerId":2,"name":"name","firstQuoteDate":"2000-01-23T04:56:07.000+00:00","id":4},{"lastName":"lastName","numberOfProjects":1,"lastProjectDate":"2000-01-23T04:56:07.000+00:00","gender":"FEMALE","customFields":[{"name":"name","type":"TEXT","value":"{}","key":"key"},{"name":"name","type":"TEXT","value":"{}","key":"key"}],"active":True,"firstProjectDate":"2000-01-23T04:56:07.000+00:00","numberOfQuotes":1,"lastQuoteDate":"2000-01-23T04:56:07.000+00:00","positionId":1,"motherTonguesIds":[7,7],"contact":{"emails":{"additional":["additional","additional"],"primary":"primary"},"sms":"sms","phones":["phones","phones"],"fax":"fax"},"customerId":2,"name":"name","firstQuoteDate":"2000-01-23T04:56:07.000+00:00","id":4}],"name":"name","clientNumberOfProjects":5,"billingAddress":{"city":"city","sameAsBillingAddress":True,"postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","provinceId":6,"countryId":0},"clientLastProjectDate":"2000-01-23T04:56:07.000+00:00","leadSourceId":3,"status":"ACTIVE"}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/customers/{customer_id}'.format(customer_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_address(client):
    """Test case for update_address

    Updates address of a given client.
    """
    body = {"city":"city","sameAsBillingAddress":True,"postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","provinceId":6,"countryId":0}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/customers/{customer_id}/address'.format(customer_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_categories(client):
    """Test case for update_categories

    Updates categories of a given client.
    """
    body = /home-api/assets/examples/customers/updateCategories.json#requestBody
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/customers/{customer_id}/categories'.format(customer_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_update_contact(client):
    """Test case for update_contact

    Updates contact of a given person.
    """
    body = /home-api/assets/examples/customers/persons/updateContact.json#requestBody
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/customers/persons/{person_id}/contact'.format(person_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_contact1(client):
    """Test case for update_contact1

    Updates contact of a given client.
    """
    body = {"emails":{"cc":["cc","cc"],"additional":["additional","additional"],"primary":"primary"},"sms":"sms","phones":["phones","phones"],"websites":["websites","websites"],"fax":"fax"}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/customers/{customer_id}/contact'.format(customer_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_correspondence_address(client):
    """Test case for update_correspondence_address

    Updates correspondence address of a given client.
    """
    body = {"city":"city","sameAsBillingAddress":True,"postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","provinceId":6,"countryId":0}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/customers/{customer_id}/correspondenceAddress'.format(customer_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_custom_field(client):
    """Test case for update_custom_field

    Updates given custom field of a given client.
    """
    body = {"name":"name","type":"TEXT","value":"{}","key":"key"}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/customers/{customer_id}/customFields/{custom_field_key}'.format(customer_id=56, custom_field_key='custom_field_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_update_custom_fields(client):
    """Test case for update_custom_fields

    Updates custom fields of a given person.
    """
    body = /home-api/assets/examples/customers/persons/updateCustomFields.json#requestBody
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/customers/persons/{person_id}/customFields'.format(person_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_custom_fields1(client):
    """Test case for update_custom_fields1

    Updates custom fields of a given client.
    """
    body = {"name":"name","type":"TEXT","value":"{}","key":"key"}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/customers/{customer_id}/customFields'.format(customer_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_industries(client):
    """Test case for update_industries

    Updates industries of a given client.
    """
    body = /home-api/assets/examples/customers/updateIndustries.json#requestBody
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/customers/{customer_id}/industries'.format(customer_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

