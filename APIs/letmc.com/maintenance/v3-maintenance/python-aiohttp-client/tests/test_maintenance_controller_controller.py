# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.maintenance_issue_model import MaintenanceIssueModel


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_maintenance_controller_create_maintenance_job(client):
    """Test case for maintenance_controller_create_maintenance_job

    Create a maintenance job for a specific branch
    """
    body = {"IssueNotes":"IssueNotes","TenantTitle":"TenantTitle","IssuePriority":"Low","IssueTitle":"IssueTitle","ExternalID":"ExternalID","TenantForename":"TenantForename","TenantPresenceRequested":True,"TenantPhonePrimary":"TenantPhonePrimary","PropertyCountry":"PropertyCountry","TenantPhoneSecondary":"TenantPhoneSecondary","ReportedAt":"2000-01-23T04:56:07.000+00:00","TenantSurname":"TenantSurname","Documents":[{"MimeType":"MimeType","URL":"URL"},{"MimeType":"MimeType","URL":"URL"}],"PropertyPostcode":"PropertyPostcode","IssueFault":"IssueFault","PropertyAddress2":"PropertyAddress2","PropertyAddress1":"PropertyAddress1","TenantEMailAddress":"TenantEMailAddress","PropertyAddress4":"PropertyAddress4","PropertyAddress3":"PropertyAddress3"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v3/maintenance/{short_name}/maintenance/{branch_id}/createmaintenancejob'.format(short_name='short_name_example', branch_id='branch_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

