# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_account_id_get(client):
    """Test case for account_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Key2': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/account/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_id_options(client):
    """Test case for account_id_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/account/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_options(client):
    """Test case for account_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_post(client):
    """Test case for account_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Key2': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_block_get(client):
    """Test case for block_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Key2': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/block',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_block_id_get(client):
    """Test case for block_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Key2': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/block/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_block_id_options(client):
    """Test case for block_id_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/block/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_block_id_transaction_get(client):
    """Test case for block_id_transaction_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Key2': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/block/{id}/transaction'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_block_id_transaction_index_get(client):
    """Test case for block_id_transaction_index_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Key2': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/block/{id}/transaction/{index}'.format(index='index_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_block_id_transaction_index_options(client):
    """Test case for block_id_transaction_index_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/block/{id}/transaction/{index}'.format(id='id_example', index='index_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_block_id_transaction_options(client):
    """Test case for block_id_transaction_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/block/{id}/transaction'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_block_options(client):
    """Test case for block_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/block',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blockchain_get(client):
    """Test case for blockchain_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Key2': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/blockchain',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blockchain_id_get(client):
    """Test case for blockchain_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Key2': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/blockchain/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blockchain_id_options(client):
    """Test case for blockchain_id_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/blockchain/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blockchain_options(client):
    """Test case for blockchain_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/blockchain',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contract_id_get(client):
    """Test case for contract_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Key2': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/contract/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contract_id_options(client):
    """Test case for contract_id_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/contract/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contract_id_post(client):
    """Test case for contract_id_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Key2': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/contract/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contract_options(client):
    """Test case for contract_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/contract',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contract_post(client):
    """Test case for contract_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/contract',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_echo_options(client):
    """Test case for echo_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/echo',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_erc20_address_get(client):
    """Test case for erc20_address_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/erc20/{address}'.format(address='address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_erc20_address_options(client):
    """Test case for erc20_address_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/erc20/{address}'.format(address='address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_erc20_address_post(client):
    """Test case for erc20_address_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/erc20/{address}'.format(address='address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_erc20_get(client):
    """Test case for erc20_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/erc20',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_erc20_options(client):
    """Test case for erc20_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/erc20',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_erc20_post(client):
    """Test case for erc20_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/erc20',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_key_get(client):
    """Test case for key_get

    
    """
    params = [('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/key',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_key_key_delete(client):
    """Test case for key_key_delete

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/1/key/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_key_key_options(client):
    """Test case for key_key_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/key/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_key_options(client):
    """Test case for key_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/key',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_key_post(client):
    """Test case for key_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/key',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_root_options(client):
    """Test case for root_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transaction_hash_get(client):
    """Test case for transaction_hash_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Key2': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/transaction/{hash}'.format(hash='hash_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transaction_hash_options(client):
    """Test case for transaction_hash_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/transaction/{hash}'.format(hash='hash_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transaction_hash_receipt_get(client):
    """Test case for transaction_hash_receipt_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Key2': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/transaction/{hash}/receipt'.format(hash='hash_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transaction_hash_receipt_options(client):
    """Test case for transaction_hash_receipt_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/transaction/{hash}/receipt'.format(hash='hash_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transaction_options(client):
    """Test case for transaction_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/transaction',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transaction_post(client):
    """Test case for transaction_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Key2': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/transaction',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_version_get(client):
    """Test case for version_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/version',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_version_options(client):
    """Test case for version_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/version',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wallet_account_get(client):
    """Test case for wallet_account_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/wallet/account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wallet_account_id_contract_post(client):
    """Test case for wallet_account_id_contract_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/wallet/account/{id}/contract'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wallet_account_id_erc20_post(client):
    """Test case for wallet_account_id_erc20_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/wallet/account/{id}/erc20'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wallet_account_id_get(client):
    """Test case for wallet_account_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/wallet/account/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wallet_account_id_options(client):
    """Test case for wallet_account_id_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/wallet/account/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wallet_account_id_pay_options(client):
    """Test case for wallet_account_id_pay_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/wallet/account/{id}/pay'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wallet_account_id_pay_post(client):
    """Test case for wallet_account_id_pay_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/wallet/account/{id}/pay'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wallet_account_options(client):
    """Test case for wallet_account_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/wallet/account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wallet_account_post(client):
    """Test case for wallet_account_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/wallet/account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wallet_get(client):
    """Test case for wallet_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/wallet',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wallet_options(client):
    """Test case for wallet_options

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='OPTIONS',
        path='/1/wallet',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wallet_post(client):
    """Test case for wallet_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/wallet',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

