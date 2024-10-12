# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.code_reference_request import CodeReferenceRequest
from openapi_server.models.delete_repository_reports_request import DeleteRepositoryReportsRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v1_code_references_delete_reports_post(client):
    """Test case for v1_code_references_delete_reports_post

    
    """
    body = {"configId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","repository":"repository","branch":"branch","settingId":0}
    headers = { 
        'Content-Type': 'application/*+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/code-references/delete-reports',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v1_code_references_post(client):
    """Test case for v1_code_references_post

    
    """
    body = {"flagReferences":[{"references":[{"file":"file","referenceLine":{"lineText":"lineText","lineNumber":0},"fileUrl":"fileUrl","postLines":[{"lineText":"lineText","lineNumber":0},{"lineText":"lineText","lineNumber":0}],"preLines":[{"lineText":"lineText","lineNumber":0},{"lineText":"lineText","lineNumber":0}]},{"file":"file","referenceLine":{"lineText":"lineText","lineNumber":0},"fileUrl":"fileUrl","postLines":[{"lineText":"lineText","lineNumber":0},{"lineText":"lineText","lineNumber":0}],"preLines":[{"lineText":"lineText","lineNumber":0},{"lineText":"lineText","lineNumber":0}]}],"settingId":6},{"references":[{"file":"file","referenceLine":{"lineText":"lineText","lineNumber":0},"fileUrl":"fileUrl","postLines":[{"lineText":"lineText","lineNumber":0},{"lineText":"lineText","lineNumber":0}],"preLines":[{"lineText":"lineText","lineNumber":0},{"lineText":"lineText","lineNumber":0}]},{"file":"file","referenceLine":{"lineText":"lineText","lineNumber":0},"fileUrl":"fileUrl","postLines":[{"lineText":"lineText","lineNumber":0},{"lineText":"lineText","lineNumber":0}],"preLines":[{"lineText":"lineText","lineNumber":0},{"lineText":"lineText","lineNumber":0}]}],"settingId":6}],"commitUrl":"commitUrl","configId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","uploader":"uploader","activeBranches":["activeBranches","activeBranches"],"repository":"repository","branch":"branch","commitHash":"commitHash"}
    headers = { 
        'Content-Type': 'application/*+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/code-references',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

