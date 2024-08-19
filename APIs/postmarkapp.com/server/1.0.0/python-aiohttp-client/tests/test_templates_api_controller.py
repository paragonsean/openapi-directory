# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_template_request import CreateTemplateRequest
from openapi_server.models.edit_template_request import EditTemplateRequest
from openapi_server.models.email_with_template_request import EmailWithTemplateRequest
from openapi_server.models.send_email_response import SendEmailResponse
from openapi_server.models.send_email_templated_batch_request import SendEmailTemplatedBatchRequest
from openapi_server.models.standard_postmark_response import StandardPostmarkResponse
from openapi_server.models.template_detail_response import TemplateDetailResponse
from openapi_server.models.template_listing_response import TemplateListingResponse
from openapi_server.models.template_record_response import TemplateRecordResponse
from openapi_server.models.template_validation_request import TemplateValidationRequest
from openapi_server.models.template_validation_response import TemplateValidationResponse


pytestmark = pytest.mark.asyncio

async def test_delete_template(client):
    """Test case for delete_template

    Delete a Template
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='DELETE',
        path='/templates/{template_id_or_alias}'.format(template_id_or_alias='template_id_or_alias_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_single_template(client):
    """Test case for get_single_template

    Get a Template
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/templates/{template_id_or_alias}'.format(template_id_or_alias='template_id_or_alias_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_templates(client):
    """Test case for list_templates

    Get the Templates associated with this Server
    """
    params = [('Count', 3.4),
                    ('Offset', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/templates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_email_batch_with_templates_0(client):
    """Test case for send_email_batch_with_templates_0

    Send a batch of email using templates.
    """
    body = {"Messages":[{"Cc":"Cc","Bcc":"Bcc","InlineCss":True,"Headers":[{"Value":"Value","Name":"Name"},{"Value":"Value","Name":"Name"}],"TrackLinks":"None","From":"From","TemplateModel":"{}","Attachments":[{"ContentType":"ContentType","Content":"Content","ContentID":"ContentID","Name":"Name"},{"ContentType":"ContentType","Content":"Content","ContentID":"ContentID","Name":"Name"}],"TemplateAlias":"TemplateAlias","TrackOpens":True,"ReplyTo":"ReplyTo","Tag":"Tag","To":"To","TemplateId":0},{"Cc":"Cc","Bcc":"Bcc","InlineCss":True,"Headers":[{"Value":"Value","Name":"Name"},{"Value":"Value","Name":"Name"}],"TrackLinks":"None","From":"From","TemplateModel":"{}","Attachments":[{"ContentType":"ContentType","Content":"Content","ContentID":"ContentID","Name":"Name"},{"ContentType":"ContentType","Content":"Content","ContentID":"ContentID","Name":"Name"}],"TemplateAlias":"TemplateAlias","TrackOpens":True,"ReplyTo":"ReplyTo","Tag":"Tag","To":"To","TemplateId":0}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='POST',
        path='/email/batchWithTemplates',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_email_with_template_0(client):
    """Test case for send_email_with_template_0

    Send an email using a Template
    """
    body = {"Cc":"Cc","Bcc":"Bcc","InlineCss":True,"Headers":[{"Value":"Value","Name":"Name"},{"Value":"Value","Name":"Name"}],"TrackLinks":"None","From":"From","TemplateModel":"{}","Attachments":[{"ContentType":"ContentType","Content":"Content","ContentID":"ContentID","Name":"Name"},{"ContentType":"ContentType","Content":"Content","ContentID":"ContentID","Name":"Name"}],"TemplateAlias":"TemplateAlias","TrackOpens":True,"ReplyTo":"ReplyTo","Tag":"Tag","To":"To","TemplateId":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='POST',
        path='/email/withTemplate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_templates_post(client):
    """Test case for templates_post

    Create a Template
    """
    body = {"TextBody":"TextBody","HtmlBody":"HtmlBody","Alias":"Alias","Subject":"Subject","Name":"Name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='POST',
        path='/templates',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_template_content(client):
    """Test case for test_template_content

    Test Template Content
    """
    body = {"TestRenderModel":"{}","TextBody":"TextBody","HtmlBody":"HtmlBody","InlineCssForHtmlTestRender":True,"Subject":"Subject"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='POST',
        path='/templates/validate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_template(client):
    """Test case for update_template

    Update a Template
    """
    body = {"TextBody":"TextBody","HtmlBody":"HtmlBody","Alias":"Alias","Subject":"Subject","Name":"Name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='PUT',
        path='/templates/{template_id_or_alias}'.format(template_id_or_alias='template_id_or_alias_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

