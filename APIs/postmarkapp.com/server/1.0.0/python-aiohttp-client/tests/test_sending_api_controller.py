# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.email_with_template_request import EmailWithTemplateRequest
from openapi_server.models.send_email_request import SendEmailRequest
from openapi_server.models.send_email_response import SendEmailResponse
from openapi_server.models.send_email_templated_batch_request import SendEmailTemplatedBatchRequest
from openapi_server.models.standard_postmark_response import StandardPostmarkResponse


pytestmark = pytest.mark.asyncio

async def test_send_email(client):
    """Test case for send_email

    Send a single email
    """
    body = {"Cc":"Cc","Bcc":"Bcc","Headers":[{"Value":"Value","Name":"Name"},{"Value":"Value","Name":"Name"}],"TrackLinks":"None","From":"From","Attachments":[{"ContentType":"ContentType","Content":"Content","ContentID":"ContentID","Name":"Name"},{"ContentType":"ContentType","Content":"Content","ContentID":"ContentID","Name":"Name"}],"Subject":"Subject","TrackOpens":True,"ReplyTo":"ReplyTo","TextBody":"TextBody","HtmlBody":"HtmlBody","Tag":"Tag","To":"To"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='POST',
        path='/email',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_email_batch(client):
    """Test case for send_email_batch

    Send a batch of emails
    """
    body = {"Cc":"Cc","Bcc":"Bcc","Headers":[{"Value":"Value","Name":"Name"},{"Value":"Value","Name":"Name"}],"TrackLinks":"None","From":"From","Attachments":[{"ContentType":"ContentType","Content":"Content","ContentID":"ContentID","Name":"Name"},{"ContentType":"ContentType","Content":"Content","ContentID":"ContentID","Name":"Name"}],"Subject":"Subject","TrackOpens":True,"ReplyTo":"ReplyTo","TextBody":"TextBody","HtmlBody":"HtmlBody","Tag":"Tag","To":"To"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='POST',
        path='/email/batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_email_batch_with_templates(client):
    """Test case for send_email_batch_with_templates

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

async def test_send_email_with_template(client):
    """Test case for send_email_with_template

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

