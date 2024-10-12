# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.body import Body
from openapi_server.models.payment_data import PaymentData
from openapi_server.models.payment_provider import PaymentProvider


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_payments_billings_bid_1(client):
    """Test case for delete_organisations_id_payments_billings_bid_1

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/payments/billings/{bid}'.format(id='id_example', bid='bid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_payments_recurring_1(client):
    """Test case for delete_organisations_id_payments_recurring_1

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/payments/recurring'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_payments_billings_bid_0(client):
    """Test case for delete_self_payments_billings_bid_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/payments/billings/{bid}'.format(bid='bid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_payments_methods_mid_0(client):
    """Test case for delete_self_payments_methods_mid_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/payments/methods/{m_id}'.format(m_id='m_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_payments_recurring_0(client):
    """Test case for delete_self_payments_recurring_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/payments/recurring',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_payments_billings_1(client):
    """Test case for get_organisations_id_payments_billings_1

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/payments/billings'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_payments_billings_bid_1(client):
    """Test case for get_organisations_id_payments_billings_bid_1

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/payments/billings/{bid}'.format(id='id_example', bid='bid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_payments_billings_bid_pdf_1(client):
    """Test case for get_organisations_id_payments_billings_bid_pdf_1

    
    """
    params = [('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/payments/billings/{bid_pd}'.format(id='id_example', bid='bid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_payments_full_price_price_1(client):
    """Test case for get_organisations_id_payments_full_price_price_1

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/payments/fullprice/{price}'.format(id='id_example', price='price_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payments_coupons_name_0(client):
    """Test case for get_payments_coupons_name_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/payments/coupons/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payments_providers_0(client):
    """Test case for get_payments_providers_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/payments/providers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payments_tokens_stripe_0(client):
    """Test case for get_payments_tokens_stripe_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/payments/tokens/stripe',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_payments_billings_0(client):
    """Test case for get_self_payments_billings_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/payments/billings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_payments_billings_bid_0(client):
    """Test case for get_self_payments_billings_bid_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/payments/billings/{bid}'.format(bid='bid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_payments_billings_bid_pdf_0(client):
    """Test case for get_self_payments_billings_bid_pdf_0

    
    """
    params = [('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/payments/billings/{bid_pd}'.format(bid='bid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_payments_fullprice_price_0(client):
    """Test case for get_self_payments_fullprice_price_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/payments/fullprice/{price}'.format(price='price_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_payments_methods_0(client):
    """Test case for get_self_payments_methods_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/payments/methods',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_payments_billings_unpaid_get_1(client):
    """Test case for organisations_id_payments_billings_unpaid_get_1

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/payments/billings/unpaid'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_payments_methods_default_get_1(client):
    """Test case for organisations_id_payments_methods_default_get_1

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/payments/methods/default'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_payments_methods_default_put_1(client):
    """Test case for organisations_id_payments_methods_default_put_1

    
    """
    body = {"deviceData":"deviceData","type":"NEW_CARD","token":"token"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/payments/methods/default'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_payments_methods_get_1(client):
    """Test case for organisations_id_payments_methods_get_1

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/payments/methods'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_payments_methods_mid_delete_1(client):
    """Test case for organisations_id_payments_methods_mid_delete_1

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/payments/methods/{m_id}'.format(m_id='m_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_payments_methods_post_1(client):
    """Test case for organisations_id_payments_methods_post_1

    
    """
    body = {"body":"body"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/organisations/{id}/payments/methods'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_payments_monthlyinvoice_get_1(client):
    """Test case for organisations_id_payments_monthlyinvoice_get_1

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/payments/monthlyinvoice'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_payments_monthlyinvoice_maxcredit_put_1(client):
    """Test case for organisations_id_payments_monthlyinvoice_maxcredit_put_1

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/payments/monthlyinvoice/maxcredit'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_payments_recurring_get_1(client):
    """Test case for organisations_id_payments_recurring_get_1

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/payments/recurring'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payments_assets_pay_button_token_button_png_get_0(client):
    """Test case for payments_assets_pay_button_token_button_png_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/payments/assets/pay_button/{token}/button.png'.format(token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payments_bid_end_stripe_post_0(client):
    """Test case for payments_bid_end_stripe_post_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/payments/{bid}/end/stripe'.format(bid='bid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_organisations_id_payments_billings_1(client):
    """Test case for post_organisations_id_payments_billings_1

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/organisations/{id}/payments/billings'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_self_payments_billings_0(client):
    """Test case for post_self_payments_billings_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/self/payments/billings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_self_payments_methods_0(client):
    """Test case for post_self_payments_methods_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/self/payments/methods',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_organisations_id_payments_billings_bid_1(client):
    """Test case for put_organisations_id_payments_billings_bid_1

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/payments/billings/{bid}'.format(id='id_example', bid='bid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_self_payments_billings_bid_0(client):
    """Test case for put_self_payments_billings_bid_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/payments/billings/{bid}'.format(bid='bid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_payments_methods_default_get_0(client):
    """Test case for self_payments_methods_default_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/payments/methods/default',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_payments_methods_default_put_0(client):
    """Test case for self_payments_methods_default_put_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/payments/methods/default',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_payments_monthlyinvoice_get_0(client):
    """Test case for self_payments_monthlyinvoice_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/payments/monthlyinvoice',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_payments_monthlyinvoice_maxcredit_put_0(client):
    """Test case for self_payments_monthlyinvoice_maxcredit_put_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/payments/monthlyinvoice/maxcredit',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_payments_recurring_get_0(client):
    """Test case for self_payments_recurring_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/payments/recurring',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_payments_tokens_stripe_get_0(client):
    """Test case for self_payments_tokens_stripe_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/payments/tokens/stripe',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

