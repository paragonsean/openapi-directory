# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_login_and_get_bearer_token(client):
    """Test case for login_and_get_bearer_token

    Login and get bearer token
    """
    params = [('email', '{{email}}'),
                    ('password', '{{password}}')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/login',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logout(client):
    """Test case for logout

    Logout
    """
    params = [('email', '{{email}}')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/logout',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register(client):
    """Test case for register

    Register
    """
    params = [('first_name', 'Felix'),
                    ('last_name', 'Weber'),
                    ('company_name', 'Fiverr'),
                    ('shop_url', 'https;//www.fiverr.de'),
                    ('email', 'fiverr2@fiverr.de'),
                    ('store_name', 'Fiverr Store'),
                    ('store_url', 'https;//www.fiverr.de'),
                    ('password', '12345678'),
                    ('fromuser', '1')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/register',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register_and_create_store_connection_for_woo_commerce(client):
    """Test case for register_and_create_store_connection_for_woo_commerce

    Register and Create Store Connection for WooCommerce
    """
    params = [('first_name', 'Felix'),
                    ('last_name', 'Weber'),
                    ('company_name', 'Fiverr'),
                    ('shop_url', 'https;//www.fiverr.de'),
                    ('email', 'fiver3r23@fiverr.de'),
                    ('store_name', 'Fiverr Store'),
                    ('store_url', 'https;//www.fiverr.de'),
                    ('password', '12345678'),
                    ('fromuser', '1'),
                    ('api_url', 'https://woocommerce-351439-1090797.cloudwaysapps.com/'),
                    ('consumer_key', 'ck_59b23d313ae372feaf211652c318fbe4501abda2'),
                    ('consumer_secret', 'cs_acc202d648bfa6b69efe553bb25086230ba116a7')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/register_woocommerce',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

