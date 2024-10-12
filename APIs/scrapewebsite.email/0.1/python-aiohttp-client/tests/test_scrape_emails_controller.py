# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_g_etv1_scrape_emails_format(client):
    """Test case for g_etv1_scrape_emails_format

    Returns a list of emails scraped by priority (ie. e-mails appear on top level pages are first). Please note that subsequent calls to the same url will be fetched from the <b>cache</b> (14 day flush). <br/><br/>Will also parse patterns such as hello[at]site.com, hello[at]site[dot]com, hello(at)site.com, hello(at)site(dot)com, hello @ site.com, hello @ site . com. <br/><br/>Please do note we cannot parse sites that require a login (for now), so for some Facebook pages it is not possible at the moment to fetch the e-mail.<br/><br/>Finally, please note that the api will fetch links for up to 2 minutes. After that time it will start analysing the pages which have been scraped. <b>Therefore</b> please ensure that your client has a timeout of at least <b>150 seconds</b> (2 mins to fetch and the rest to parse). <br/><br/><b>Please note</b> that due to the fact that the api goes out to fetch the pages, the server allows only 1 concurrent request/ip. Requests which are made while the 1 request is still processing will result in a 429 code.<br/><br/><b>Please note</b> that as of May 25, 2014, the main mechanism of tracking usage will be done via Mashape. You can get the free calls by signing up with the FREE plan.<br/><br/>Please visit <a href='https://www.mashape.com/tommytcchan/scrape-website-email'>https://www.mashape.com/tommytcchan/scrape-website-email</a>.<br/><br/><b>There is now a limit of 5 requests per day using this sample interface.</b><br/><br/>
    """
    params = [('website', 'website_example'),
                    ('must_include', 'must_include_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/scrape_emails.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

