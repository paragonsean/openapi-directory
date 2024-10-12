# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delete_bank_account_request import DeleteBankAccountRequest
from openapi_server.models.delete_legal_arrangement_request import DeleteLegalArrangementRequest
from openapi_server.models.delete_payout_method_request import DeletePayoutMethodRequest
from openapi_server.models.delete_shareholder_request import DeleteShareholderRequest
from openapi_server.models.delete_signatories_request import DeleteSignatoriesRequest
from openapi_server.models.generic_response import GenericResponse
from openapi_server.models.get_uploaded_documents_request import GetUploadedDocumentsRequest
from openapi_server.models.get_uploaded_documents_response import GetUploadedDocumentsResponse
from openapi_server.models.perform_verification_request import PerformVerificationRequest
from openapi_server.models.service_error import ServiceError
from openapi_server.models.update_account_holder_response import UpdateAccountHolderResponse
from openapi_server.models.upload_document_request import UploadDocumentRequest


pytestmark = pytest.mark.asyncio

async def test_post_check_account_holder(client):
    """Test case for post_check_account_holder

    Trigger verification
    """
    body = {"accountStateType":"LimitedPayout","accountHolderCode":"accountHolderCode","tier":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Account/v5/checkAccountHolder',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_delete_bank_accounts(client):
    """Test case for post_delete_bank_accounts

    Delete bank accounts
    """
    body = {"accountHolderCode":"accountHolderCode","bankAccountUUIDs":["bankAccountUUIDs","bankAccountUUIDs"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Account/v5/deleteBankAccounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_delete_legal_arrangements(client):
    """Test case for post_delete_legal_arrangements

    Delete legal arrangements
    """
    body = {"accountHolderCode":"accountHolderCode","legalArrangements":[{"legalArrangementCode":"legalArrangementCode","legalArrangementEntityCodes":["legalArrangementEntityCodes","legalArrangementEntityCodes"]},{"legalArrangementCode":"legalArrangementCode","legalArrangementEntityCodes":["legalArrangementEntityCodes","legalArrangementEntityCodes"]}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Account/v5/deleteLegalArrangements',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_delete_payout_methods(client):
    """Test case for post_delete_payout_methods

    Delete payout methods
    """
    body = {"accountHolderCode":"accountHolderCode","payoutMethodCodes":["payoutMethodCodes","payoutMethodCodes"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Account/v5/deletePayoutMethods',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_delete_shareholders(client):
    """Test case for post_delete_shareholders

    Delete shareholders
    """
    body = {"accountHolderCode":"accountHolderCode","shareholderCodes":["shareholderCodes","shareholderCodes"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Account/v5/deleteShareholders',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_delete_signatories(client):
    """Test case for post_delete_signatories

    Delete signatories
    """
    body = {"accountHolderCode":"accountHolderCode","signatoryCodes":["signatoryCodes","signatoryCodes"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Account/v5/deleteSignatories',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_get_uploaded_documents(client):
    """Test case for post_get_uploaded_documents

    Get documents
    """
    body = {"accountHolderCode":"accountHolderCode","bankAccountUUID":"bankAccountUUID","shareholderCode":"shareholderCode"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Account/v5/getUploadedDocuments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_upload_document(client):
    """Test case for post_upload_document

    Upload a document
    """
    body = {"documentContent":"documentContent","documentDetail":{"accountHolderCode":"accountHolderCode","bankAccountUUID":"bankAccountUUID","filename":"filename","signatoryCode":"signatoryCode","documentType":"BANK_STATEMENT","description":"description","shareholderCode":"shareholderCode"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Account/v5/uploadDocument',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

