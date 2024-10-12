# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.empty_response import EmptyResponse
from openapi_server.models.form_entry_response import FormEntryResponse
from openapi_server.models.form_response import FormResponse
from openapi_server.models.update_form_by_id_request_body import UpdateFormByIdRequestBody


pytestmark = pytest.mark.asyncio

async def test_delete_form_message_by_id(client):
    """Test case for delete_form_message_by_id

    Delete a receive form submission
    """
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/forms/entries/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_form_by_id(client):
    """Test case for get_form_by_id

    Get receive folder form by Id
    """
    params = [('include', 'share')]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': 'ev_access_token_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/forms/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_form_by_share_hash(client):
    """Test case for get_form_by_share_hash

    Get receive folder form settings
    """
    params = [('shareHash', 'share_hash_example'),
                    ('include', 'include_example')]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': 'ev_access_token_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/forms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_form_entries(client):
    """Test case for get_form_entries

    Get form data entries for a receive
    """
    params = [('limit', 10),
                    ('offset', 100)]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/forms/entries/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_form_by_id(client):
    """Test case for update_form_by_id

    Updates a form with given parameters
    """
    body = {"elements":[{"settings":{"isRequired":True,"senderEmail":False,"useAsFolderName":False},"name":"Your name","id":123,"type":"name","order":0},{"settings":{"isRequired":True,"senderEmail":False,"useAsFolderName":False},"name":"Your name","id":123,"type":"name","order":0}],"formDescription":"Send your files","submitButtonText":"Send Files","cssStyles":"#ev-widget-form {\n  /*Change this to change the font. Remove to use your website font*/\n  font-family: Helvetica Neue, sans-serif;\n  /*Makes the form the same width as your website */\n  margin: 0 -2%;\n}\n#ev-widget-form label{\n  width: 100%;\n}\n#ev-widget-form input,\n#ev-widget-form textarea {\n  /*Changes color and thickness of borders on form elements */\n  border: 2px solid #ccc;\n  /*Changes spacing inside the form elements (top/bottom and left/right */\n  padding: 5px 5px;\n  /* Changes how far away the inputs are from their label */\n  margin-top: 2px;\n}\n\n#ev-widget-form input:focus,\n#ev-widget-form textarea:focus {\n  /*Changes the color of the form elements when they are clicked in to */\n  border: 2px solid #b2cf88;\n  /*Removes glow effect from form elements that are clicked in to */\n  outline: none;\n}\n\n#ev-widget-form label {\n  font-size: 14px;\n  font-weight: bold;\n  /*Changes color of labels */\n  color: #232323\n}\n\n#ev-widget-form .ev-form-element-description {\n  /*Changes size of descriptions */\n  font-size: 12px;\n  /*Changes color of descriptions */\n  color: #777;\n  /* Changes how far away the descriptions are from their input */\n  margin-top: 2px;\n}\n\n#ev-widget-form textarea {\n  /* Makes textareas (multiline inputs) a taller. */\n  min-height: 90px;\n}     ","successMessage":"Your files were uploaded"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/forms/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

