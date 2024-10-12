# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.associate_member_request import AssociateMemberRequest
from openapi_server.models.associate_member_response import AssociateMemberResponse
from openapi_server.models.batch_get_account_status_request import BatchGetAccountStatusRequest
from openapi_server.models.batch_get_account_status_response import BatchGetAccountStatusResponse
from openapi_server.models.batch_get_code_snippet_request import BatchGetCodeSnippetRequest
from openapi_server.models.batch_get_code_snippet_response import BatchGetCodeSnippetResponse
from openapi_server.models.batch_get_finding_details_request import BatchGetFindingDetailsRequest
from openapi_server.models.batch_get_finding_details_response import BatchGetFindingDetailsResponse
from openapi_server.models.batch_get_free_trial_info_request import BatchGetFreeTrialInfoRequest
from openapi_server.models.batch_get_free_trial_info_response import BatchGetFreeTrialInfoResponse
from openapi_server.models.batch_get_member_ec2_deep_inspection_status_request import BatchGetMemberEc2DeepInspectionStatusRequest
from openapi_server.models.batch_get_member_ec2_deep_inspection_status_response import BatchGetMemberEc2DeepInspectionStatusResponse
from openapi_server.models.batch_update_member_ec2_deep_inspection_status_request import BatchUpdateMemberEc2DeepInspectionStatusRequest
from openapi_server.models.batch_update_member_ec2_deep_inspection_status_response import BatchUpdateMemberEc2DeepInspectionStatusResponse
from openapi_server.models.cancel_findings_report_request import CancelFindingsReportRequest
from openapi_server.models.cancel_findings_report_response import CancelFindingsReportResponse
from openapi_server.models.cancel_sbom_export_request import CancelSbomExportRequest
from openapi_server.models.cancel_sbom_export_response import CancelSbomExportResponse
from openapi_server.models.create_filter_request import CreateFilterRequest
from openapi_server.models.create_filter_response import CreateFilterResponse
from openapi_server.models.create_findings_report_request import CreateFindingsReportRequest
from openapi_server.models.create_findings_report_response import CreateFindingsReportResponse
from openapi_server.models.create_sbom_export_request import CreateSbomExportRequest
from openapi_server.models.create_sbom_export_response import CreateSbomExportResponse
from openapi_server.models.delete_filter_request import DeleteFilterRequest
from openapi_server.models.delete_filter_response import DeleteFilterResponse
from openapi_server.models.describe_organization_configuration_response import DescribeOrganizationConfigurationResponse
from openapi_server.models.disable_delegated_admin_account_request import DisableDelegatedAdminAccountRequest
from openapi_server.models.disable_delegated_admin_account_response import DisableDelegatedAdminAccountResponse
from openapi_server.models.disable_request import DisableRequest
from openapi_server.models.disable_response import DisableResponse
from openapi_server.models.disassociate_member_request import DisassociateMemberRequest
from openapi_server.models.disassociate_member_response import DisassociateMemberResponse
from openapi_server.models.enable_delegated_admin_account_request import EnableDelegatedAdminAccountRequest
from openapi_server.models.enable_delegated_admin_account_response import EnableDelegatedAdminAccountResponse
from openapi_server.models.enable_request import EnableRequest
from openapi_server.models.enable_response import EnableResponse
from openapi_server.models.get_configuration_response import GetConfigurationResponse
from openapi_server.models.get_delegated_admin_account_response import GetDelegatedAdminAccountResponse
from openapi_server.models.get_ec2_deep_inspection_configuration_response import GetEc2DeepInspectionConfigurationResponse
from openapi_server.models.get_encryption_key_response import GetEncryptionKeyResponse
from openapi_server.models.get_findings_report_status_request import GetFindingsReportStatusRequest
from openapi_server.models.get_findings_report_status_response import GetFindingsReportStatusResponse
from openapi_server.models.get_member_request import GetMemberRequest
from openapi_server.models.get_member_response import GetMemberResponse
from openapi_server.models.get_sbom_export_request import GetSbomExportRequest
from openapi_server.models.get_sbom_export_response import GetSbomExportResponse
from openapi_server.models.list_account_permissions_request import ListAccountPermissionsRequest
from openapi_server.models.list_account_permissions_response import ListAccountPermissionsResponse
from openapi_server.models.list_coverage_request import ListCoverageRequest
from openapi_server.models.list_coverage_response import ListCoverageResponse
from openapi_server.models.list_coverage_statistics_request import ListCoverageStatisticsRequest
from openapi_server.models.list_coverage_statistics_response import ListCoverageStatisticsResponse
from openapi_server.models.list_delegated_admin_accounts_request import ListDelegatedAdminAccountsRequest
from openapi_server.models.list_delegated_admin_accounts_response import ListDelegatedAdminAccountsResponse
from openapi_server.models.list_filters_request import ListFiltersRequest
from openapi_server.models.list_filters_response import ListFiltersResponse
from openapi_server.models.list_finding_aggregations_request import ListFindingAggregationsRequest
from openapi_server.models.list_finding_aggregations_response import ListFindingAggregationsResponse
from openapi_server.models.list_findings_request import ListFindingsRequest
from openapi_server.models.list_findings_response import ListFindingsResponse
from openapi_server.models.list_members_request import ListMembersRequest
from openapi_server.models.list_members_response import ListMembersResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_usage_totals_request import ListUsageTotalsRequest
from openapi_server.models.list_usage_totals_response import ListUsageTotalsResponse
from openapi_server.models.reset_encryption_key_request import ResetEncryptionKeyRequest
from openapi_server.models.search_vulnerabilities_request import SearchVulnerabilitiesRequest
from openapi_server.models.search_vulnerabilities_response import SearchVulnerabilitiesResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_configuration_request import UpdateConfigurationRequest
from openapi_server.models.update_ec2_deep_inspection_configuration_request import UpdateEc2DeepInspectionConfigurationRequest
from openapi_server.models.update_ec2_deep_inspection_configuration_response import UpdateEc2DeepInspectionConfigurationResponse
from openapi_server.models.update_encryption_key_request import UpdateEncryptionKeyRequest
from openapi_server.models.update_filter_request import UpdateFilterRequest
from openapi_server.models.update_filter_response import UpdateFilterResponse
from openapi_server.models.update_org_ec2_deep_inspection_configuration_request import UpdateOrgEc2DeepInspectionConfigurationRequest
from openapi_server.models.update_organization_configuration_request import UpdateOrganizationConfigurationRequest
from openapi_server.models.update_organization_configuration_response import UpdateOrganizationConfigurationResponse


pytestmark = pytest.mark.asyncio

async def test_associate_member(client):
    """Test case for associate_member

    
    """
    body = {"accountId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/members/associate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_get_account_status(client):
    """Test case for batch_get_account_status

    
    """
    body = {"accountIds":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/status/batch/get',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_get_code_snippet(client):
    """Test case for batch_get_code_snippet

    
    """
    body = {"findingArns":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/codesnippet/batchget',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_get_finding_details(client):
    """Test case for batch_get_finding_details

    
    """
    body = {"findingArns":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/findings/details/batch/get',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_get_free_trial_info(client):
    """Test case for batch_get_free_trial_info

    
    """
    body = {"accountIds":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/freetrialinfo/batchget',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_get_member_ec2_deep_inspection_status(client):
    """Test case for batch_get_member_ec2_deep_inspection_status

    
    """
    body = {"accountIds":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ec2deepinspectionstatus/member/batch/get',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_update_member_ec2_deep_inspection_status(client):
    """Test case for batch_update_member_ec2_deep_inspection_status

    
    """
    body = {"accountIds":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ec2deepinspectionstatus/member/batch/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_findings_report(client):
    """Test case for cancel_findings_report

    
    """
    body = {"reportId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/reporting/cancel',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_sbom_export(client):
    """Test case for cancel_sbom_export

    
    """
    body = {"reportId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sbomexport/cancel',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_filter(client):
    """Test case for create_filter

    
    """
    body = {"filterCriteria":{"portRange":"","fixAvailable":"","resourceId":"","awsAccountId":"","componentId":"","codeVulnerabilityDetectorName":"","ecrImageHash":"","vendorSeverity":"","vulnerabilitySource":"","lambdaFunctionRuntime":"","codeVulnerabilityDetectorTags":"","title":"","ecrImagePushedAt":"","ecrImageRepositoryName":"","ecrImageRegistry":"","firstObservedAt":"","resourceTags":"","vulnerabilityId":"","lambdaFunctionName":"","ec2InstanceSubnetId":"","updatedAt":"","severity":"","componentType":"","relatedVulnerabilities":"","lastObservedAt":"","ec2InstanceImageId":"","epssScore":"","vulnerablePackages":"","lambdaFunctionLayers":"","inspectorScore":"","lambdaFunctionLastModifiedAt":"","lambdaFunctionExecutionRoleArn":"","findingType":"","ecrImageArchitecture":"","ec2InstanceVpcId":"","ecrImageTags":"","findingStatus":"","codeVulnerabilityFilePath":"","exploitAvailable":"","findingArn":"","networkProtocol":"","resourceType":""},"reason":"","name":"","action":"","description":"","tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/filters/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_findings_report(client):
    """Test case for create_findings_report

    
    """
    body = {"filterCriteria":{"portRange":"","fixAvailable":"","resourceId":"","awsAccountId":"","componentId":"","codeVulnerabilityDetectorName":"","ecrImageHash":"","vendorSeverity":"","vulnerabilitySource":"","lambdaFunctionRuntime":"","codeVulnerabilityDetectorTags":"","title":"","ecrImagePushedAt":"","ecrImageRepositoryName":"","ecrImageRegistry":"","firstObservedAt":"","resourceTags":"","vulnerabilityId":"","lambdaFunctionName":"","ec2InstanceSubnetId":"","updatedAt":"","severity":"","componentType":"","relatedVulnerabilities":"","lastObservedAt":"","ec2InstanceImageId":"","epssScore":"","vulnerablePackages":"","lambdaFunctionLayers":"","inspectorScore":"","lambdaFunctionLastModifiedAt":"","lambdaFunctionExecutionRoleArn":"","findingType":"","ecrImageArchitecture":"","ec2InstanceVpcId":"","ecrImageTags":"","findingStatus":"","codeVulnerabilityFilePath":"","exploitAvailable":"","findingArn":"","networkProtocol":"","resourceType":""},"s3Destination":{"bucketName":"","kmsKeyArn":"","keyPrefix":""},"reportFormat":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/reporting/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_sbom_export(client):
    """Test case for create_sbom_export

    
    """
    body = {"s3Destination":{"bucketName":"","kmsKeyArn":"","keyPrefix":""},"resourceFilterCriteria":{"accountId":"","ec2InstanceTags":"","resourceId":"","ecrImageTags":"","lambdaFunctionName":"","lambdaFunctionTags":"","ecrRepositoryName":"","resourceType":""},"reportFormat":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sbomexport/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_filter(client):
    """Test case for delete_filter

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/filters/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_organization_configuration(client):
    """Test case for describe_organization_configuration

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/organizationconfiguration/describe',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable(client):
    """Test case for disable

    
    """
    body = {"resourceTypes":"","accountIds":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/disable',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_delegated_admin_account(client):
    """Test case for disable_delegated_admin_account

    
    """
    body = {"delegatedAdminAccountId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/delegatedadminaccounts/disable',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disassociate_member(client):
    """Test case for disassociate_member

    
    """
    body = {"accountId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/members/disassociate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable(client):
    """Test case for enable

    
    """
    body = {"resourceTypes":"","accountIds":"","clientToken":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/enable',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_delegated_admin_account(client):
    """Test case for enable_delegated_admin_account

    
    """
    body = {"delegatedAdminAccountId":"","clientToken":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/delegatedadminaccounts/enable',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_configuration(client):
    """Test case for get_configuration

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/configuration/get',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_delegated_admin_account(client):
    """Test case for get_delegated_admin_account

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/delegatedadminaccounts/get',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ec2_deep_inspection_configuration(client):
    """Test case for get_ec2_deep_inspection_configuration

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ec2deepinspectionconfiguration/get',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_encryption_key(client):
    """Test case for get_encryption_key

    
    """
    params = [('resourceType', 'resource_type_example'),
                    ('scanType', 'scan_type_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/encryptionkey/get#resourceType&scanType',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_findings_report_status(client):
    """Test case for get_findings_report_status

    
    """
    body = {"reportId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/reporting/status/get',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_member(client):
    """Test case for get_member

    
    """
    body = {"accountId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/members/get',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sbom_export(client):
    """Test case for get_sbom_export

    
    """
    body = {"reportId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sbomexport/get',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_account_permissions(client):
    """Test case for list_account_permissions

    
    """
    body = {"maxResults":"","nextToken":"","service":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/accountpermissions/list',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_coverage(client):
    """Test case for list_coverage

    
    """
    body = {"filterCriteria":{"lastScannedAt":"","ec2InstanceTags":"","resourceId":"","lambdaFunctionTags":"","lambdaFunctionRuntime":"","scanStatusCode":"","ecrRepositoryName":"","accountId":"","scanStatusReason":"","ecrImageTags":"","lambdaFunctionName":"","scanType":"","resourceType":""},"maxResults":"","nextToken":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/coverage/list',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_coverage_statistics(client):
    """Test case for list_coverage_statistics

    
    """
    body = {"filterCriteria":{"lastScannedAt":"","ec2InstanceTags":"","resourceId":"","lambdaFunctionTags":"","lambdaFunctionRuntime":"","scanStatusCode":"","ecrRepositoryName":"","accountId":"","scanStatusReason":"","ecrImageTags":"","lambdaFunctionName":"","scanType":"","resourceType":""},"nextToken":"","groupBy":""}
    params = [('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/coverage/statistics/list',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_delegated_admin_accounts(client):
    """Test case for list_delegated_admin_accounts

    
    """
    body = {"maxResults":"","nextToken":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/delegatedadminaccounts/list',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_filters(client):
    """Test case for list_filters

    
    """
    body = {"maxResults":"","nextToken":"","action":"","arns":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/filters/list',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_finding_aggregations(client):
    """Test case for list_finding_aggregations

    
    """
    body = {"aggregationType":"","accountIds":"","maxResults":"","nextToken":"","aggregationRequest":{"findingTypeAggregation":{"findingType":"","sortOrder":"","sortBy":"","resourceType":""},"imageLayerAggregation":{"layerHashes":"","repositories":"","sortOrder":"","sortBy":"","resourceIds":""},"repositoryAggregation":{"repositories":"","sortOrder":"","sortBy":""},"amiAggregation":{"sortOrder":"","sortBy":"","amis":""},"lambdaLayerAggregation":{"functionNames":"","layerArns":"","sortOrder":"","sortBy":"","resourceIds":""},"accountAggregation":{"findingType":"","sortOrder":"","sortBy":"","resourceType":""},"packageAggregation":{"packageNames":"","sortOrder":"","sortBy":""},"ec2InstanceAggregation":{"operatingSystems":"","instanceIds":"","sortOrder":"","instanceTags":"","sortBy":"","amis":""},"awsEcrContainerAggregation":{"architectures":"","imageShas":"","repositories":"","sortOrder":"","sortBy":"","imageTags":"","resourceIds":""},"lambdaFunctionAggregation":{"functionNames":"","runtimes":"","sortOrder":"","functionTags":"","sortBy":"","resourceIds":""},"titleAggregation":{"findingType":"","vulnerabilityIds":"","sortOrder":"","sortBy":"","titles":"","resourceType":""}}}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/findings/aggregation/list',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_findings(client):
    """Test case for list_findings

    
    """
    body = {"filterCriteria":{"portRange":"","fixAvailable":"","resourceId":"","awsAccountId":"","componentId":"","codeVulnerabilityDetectorName":"","ecrImageHash":"","vendorSeverity":"","vulnerabilitySource":"","lambdaFunctionRuntime":"","codeVulnerabilityDetectorTags":"","title":"","ecrImagePushedAt":"","ecrImageRepositoryName":"","ecrImageRegistry":"","firstObservedAt":"","resourceTags":"","vulnerabilityId":"","lambdaFunctionName":"","ec2InstanceSubnetId":"","updatedAt":"","severity":"","componentType":"","relatedVulnerabilities":"","lastObservedAt":"","ec2InstanceImageId":"","epssScore":"","vulnerablePackages":"","lambdaFunctionLayers":"","inspectorScore":"","lambdaFunctionLastModifiedAt":"","lambdaFunctionExecutionRoleArn":"","findingType":"","ecrImageArchitecture":"","ec2InstanceVpcId":"","ecrImageTags":"","findingStatus":"","codeVulnerabilityFilePath":"","exploitAvailable":"","findingArn":"","networkProtocol":"","resourceType":""},"maxResults":"","nextToken":"","sortCriteria":{"field":"","sortOrder":""}}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/findings/list',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_members(client):
    """Test case for list_members

    
    """
    body = {"maxResults":"","nextToken":"","onlyAssociated":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/members/list',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tags_for_resource(client):
    """Test case for list_tags_for_resource

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tags/{resource_arn}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_usage_totals(client):
    """Test case for list_usage_totals

    
    """
    body = {"accountIds":"","maxResults":"","nextToken":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/usage/list',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_encryption_key(client):
    """Test case for reset_encryption_key

    
    """
    body = {"scanType":"","resourceType":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/encryptionkey/reset',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_vulnerabilities(client):
    """Test case for search_vulnerabilities

    
    """
    body = {"filterCriteria":{"vulnerabilityIds":""},"nextToken":""}
    params = [('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vulnerabilities/search',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_resource(client):
    """Test case for tag_resource

    
    """
    body = {"tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tags/{resource_arn}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_untag_resource(client):
    """Test case for untag_resource

    
    """
    params = [('tagKeys', ['tag_keys_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/tags/{resource_arntag_key}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_configuration(client):
    """Test case for update_configuration

    
    """
    body = {"ecrConfiguration":{"rescanDuration":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/configuration/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_ec2_deep_inspection_configuration(client):
    """Test case for update_ec2_deep_inspection_configuration

    
    """
    body = {"activateDeepInspection":"","packagePaths":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ec2deepinspectionconfiguration/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_encryption_key(client):
    """Test case for update_encryption_key

    
    """
    body = {"kmsKeyId":"","scanType":"","resourceType":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/encryptionkey/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_filter(client):
    """Test case for update_filter

    
    """
    body = {"filterCriteria":{"portRange":"","fixAvailable":"","resourceId":"","awsAccountId":"","componentId":"","codeVulnerabilityDetectorName":"","ecrImageHash":"","vendorSeverity":"","vulnerabilitySource":"","lambdaFunctionRuntime":"","codeVulnerabilityDetectorTags":"","title":"","ecrImagePushedAt":"","ecrImageRepositoryName":"","ecrImageRegistry":"","firstObservedAt":"","resourceTags":"","vulnerabilityId":"","lambdaFunctionName":"","ec2InstanceSubnetId":"","updatedAt":"","severity":"","componentType":"","relatedVulnerabilities":"","lastObservedAt":"","ec2InstanceImageId":"","epssScore":"","vulnerablePackages":"","lambdaFunctionLayers":"","inspectorScore":"","lambdaFunctionLastModifiedAt":"","lambdaFunctionExecutionRoleArn":"","findingType":"","ecrImageArchitecture":"","ec2InstanceVpcId":"","ecrImageTags":"","findingStatus":"","codeVulnerabilityFilePath":"","exploitAvailable":"","findingArn":"","networkProtocol":"","resourceType":""},"reason":"","filterArn":"","name":"","action":"","description":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/filters/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_org_ec2_deep_inspection_configuration(client):
    """Test case for update_org_ec2_deep_inspection_configuration

    
    """
    body = {"orgPackagePaths":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ec2deepinspectionconfiguration/org/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_configuration(client):
    """Test case for update_organization_configuration

    
    """
    body = {"autoEnable":{"lambda":"","ec2":"","ecr":"","lambdaCode":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/organizationconfiguration/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

