# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.associate_entities_to_experience_request import AssociateEntitiesToExperienceRequest
from openapi_server.models.associate_entities_to_experience_response import AssociateEntitiesToExperienceResponse
from openapi_server.models.associate_personas_to_entities_request import AssociatePersonasToEntitiesRequest
from openapi_server.models.associate_personas_to_entities_response import AssociatePersonasToEntitiesResponse
from openapi_server.models.batch_delete_document_request import BatchDeleteDocumentRequest
from openapi_server.models.batch_delete_document_response import BatchDeleteDocumentResponse
from openapi_server.models.batch_delete_featured_results_set_request import BatchDeleteFeaturedResultsSetRequest
from openapi_server.models.batch_delete_featured_results_set_response import BatchDeleteFeaturedResultsSetResponse
from openapi_server.models.batch_get_document_status_request import BatchGetDocumentStatusRequest
from openapi_server.models.batch_get_document_status_response import BatchGetDocumentStatusResponse
from openapi_server.models.batch_put_document_request import BatchPutDocumentRequest
from openapi_server.models.batch_put_document_response import BatchPutDocumentResponse
from openapi_server.models.clear_query_suggestions_request import ClearQuerySuggestionsRequest
from openapi_server.models.create_access_control_configuration_request import CreateAccessControlConfigurationRequest
from openapi_server.models.create_access_control_configuration_response import CreateAccessControlConfigurationResponse
from openapi_server.models.create_data_source_request import CreateDataSourceRequest
from openapi_server.models.create_data_source_response import CreateDataSourceResponse
from openapi_server.models.create_experience_request import CreateExperienceRequest
from openapi_server.models.create_experience_response import CreateExperienceResponse
from openapi_server.models.create_faq_request import CreateFaqRequest
from openapi_server.models.create_faq_response import CreateFaqResponse
from openapi_server.models.create_featured_results_set_request import CreateFeaturedResultsSetRequest
from openapi_server.models.create_featured_results_set_response import CreateFeaturedResultsSetResponse
from openapi_server.models.create_index_request import CreateIndexRequest
from openapi_server.models.create_index_response import CreateIndexResponse
from openapi_server.models.create_query_suggestions_block_list_request import CreateQuerySuggestionsBlockListRequest
from openapi_server.models.create_query_suggestions_block_list_response import CreateQuerySuggestionsBlockListResponse
from openapi_server.models.create_thesaurus_request import CreateThesaurusRequest
from openapi_server.models.create_thesaurus_response import CreateThesaurusResponse
from openapi_server.models.delete_access_control_configuration_request import DeleteAccessControlConfigurationRequest
from openapi_server.models.delete_data_source_request import DeleteDataSourceRequest
from openapi_server.models.delete_experience_request import DeleteExperienceRequest
from openapi_server.models.delete_faq_request import DeleteFaqRequest
from openapi_server.models.delete_index_request import DeleteIndexRequest
from openapi_server.models.delete_principal_mapping_request import DeletePrincipalMappingRequest
from openapi_server.models.delete_query_suggestions_block_list_request import DeleteQuerySuggestionsBlockListRequest
from openapi_server.models.delete_thesaurus_request import DeleteThesaurusRequest
from openapi_server.models.describe_access_control_configuration_request import DescribeAccessControlConfigurationRequest
from openapi_server.models.describe_access_control_configuration_response import DescribeAccessControlConfigurationResponse
from openapi_server.models.describe_data_source_request import DescribeDataSourceRequest
from openapi_server.models.describe_data_source_response import DescribeDataSourceResponse
from openapi_server.models.describe_experience_request import DescribeExperienceRequest
from openapi_server.models.describe_experience_response import DescribeExperienceResponse
from openapi_server.models.describe_faq_request import DescribeFaqRequest
from openapi_server.models.describe_faq_response import DescribeFaqResponse
from openapi_server.models.describe_featured_results_set_request import DescribeFeaturedResultsSetRequest
from openapi_server.models.describe_featured_results_set_response import DescribeFeaturedResultsSetResponse
from openapi_server.models.describe_index_request import DescribeIndexRequest
from openapi_server.models.describe_index_response import DescribeIndexResponse
from openapi_server.models.describe_principal_mapping_request import DescribePrincipalMappingRequest
from openapi_server.models.describe_principal_mapping_response import DescribePrincipalMappingResponse
from openapi_server.models.describe_query_suggestions_block_list_request import DescribeQuerySuggestionsBlockListRequest
from openapi_server.models.describe_query_suggestions_block_list_response import DescribeQuerySuggestionsBlockListResponse
from openapi_server.models.describe_query_suggestions_config_request import DescribeQuerySuggestionsConfigRequest
from openapi_server.models.describe_query_suggestions_config_response import DescribeQuerySuggestionsConfigResponse
from openapi_server.models.describe_thesaurus_request import DescribeThesaurusRequest
from openapi_server.models.describe_thesaurus_response import DescribeThesaurusResponse
from openapi_server.models.disassociate_entities_from_experience_request import DisassociateEntitiesFromExperienceRequest
from openapi_server.models.disassociate_entities_from_experience_response import DisassociateEntitiesFromExperienceResponse
from openapi_server.models.disassociate_personas_from_entities_request import DisassociatePersonasFromEntitiesRequest
from openapi_server.models.disassociate_personas_from_entities_response import DisassociatePersonasFromEntitiesResponse
from openapi_server.models.get_query_suggestions_request import GetQuerySuggestionsRequest
from openapi_server.models.get_query_suggestions_response import GetQuerySuggestionsResponse
from openapi_server.models.get_snapshots_request import GetSnapshotsRequest
from openapi_server.models.get_snapshots_response import GetSnapshotsResponse
from openapi_server.models.list_access_control_configurations_request import ListAccessControlConfigurationsRequest
from openapi_server.models.list_access_control_configurations_response import ListAccessControlConfigurationsResponse
from openapi_server.models.list_data_source_sync_jobs_request import ListDataSourceSyncJobsRequest
from openapi_server.models.list_data_source_sync_jobs_response import ListDataSourceSyncJobsResponse
from openapi_server.models.list_data_sources_request import ListDataSourcesRequest
from openapi_server.models.list_data_sources_response import ListDataSourcesResponse
from openapi_server.models.list_entity_personas_request import ListEntityPersonasRequest
from openapi_server.models.list_entity_personas_response import ListEntityPersonasResponse
from openapi_server.models.list_experience_entities_request import ListExperienceEntitiesRequest
from openapi_server.models.list_experience_entities_response import ListExperienceEntitiesResponse
from openapi_server.models.list_experiences_request import ListExperiencesRequest
from openapi_server.models.list_experiences_response import ListExperiencesResponse
from openapi_server.models.list_faqs_request import ListFaqsRequest
from openapi_server.models.list_faqs_response import ListFaqsResponse
from openapi_server.models.list_featured_results_sets_request import ListFeaturedResultsSetsRequest
from openapi_server.models.list_featured_results_sets_response import ListFeaturedResultsSetsResponse
from openapi_server.models.list_groups_older_than_ordering_id_request import ListGroupsOlderThanOrderingIdRequest
from openapi_server.models.list_groups_older_than_ordering_id_response import ListGroupsOlderThanOrderingIdResponse
from openapi_server.models.list_indices_request import ListIndicesRequest
from openapi_server.models.list_indices_response import ListIndicesResponse
from openapi_server.models.list_query_suggestions_block_lists_request import ListQuerySuggestionsBlockListsRequest
from openapi_server.models.list_query_suggestions_block_lists_response import ListQuerySuggestionsBlockListsResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_thesauri_request import ListThesauriRequest
from openapi_server.models.list_thesauri_response import ListThesauriResponse
from openapi_server.models.put_principal_mapping_request import PutPrincipalMappingRequest
from openapi_server.models.query_request import QueryRequest
from openapi_server.models.query_result import QueryResult
from openapi_server.models.retrieve_request import RetrieveRequest
from openapi_server.models.retrieve_result import RetrieveResult
from openapi_server.models.start_data_source_sync_job_request import StartDataSourceSyncJobRequest
from openapi_server.models.start_data_source_sync_job_response import StartDataSourceSyncJobResponse
from openapi_server.models.stop_data_source_sync_job_request import StopDataSourceSyncJobRequest
from openapi_server.models.submit_feedback_request import SubmitFeedbackRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_access_control_configuration_request import UpdateAccessControlConfigurationRequest
from openapi_server.models.update_data_source_request import UpdateDataSourceRequest
from openapi_server.models.update_experience_request import UpdateExperienceRequest
from openapi_server.models.update_featured_results_set_request import UpdateFeaturedResultsSetRequest
from openapi_server.models.update_featured_results_set_response import UpdateFeaturedResultsSetResponse
from openapi_server.models.update_index_request import UpdateIndexRequest
from openapi_server.models.update_query_suggestions_block_list_request import UpdateQuerySuggestionsBlockListRequest
from openapi_server.models.update_query_suggestions_config_request import UpdateQuerySuggestionsConfigRequest
from openapi_server.models.update_thesaurus_request import UpdateThesaurusRequest


pytestmark = pytest.mark.asyncio

async def test_associate_entities_to_experience(client):
    """Test case for associate_entities_to_experience

    
    """
    body = {"IndexId":"","EntityList":"","Id":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.AssociateEntitiesToExperience',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_associate_personas_to_entities(client):
    """Test case for associate_personas_to_entities

    
    """
    body = {"IndexId":"","Personas":"","Id":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.AssociatePersonasToEntities',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_delete_document(client):
    """Test case for batch_delete_document

    
    """
    body = {"IndexId":"","DocumentIdList":"","DataSourceSyncJobMetricTarget":{"DataSourceSyncJobId":"","DataSourceId":""}}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.BatchDeleteDocument',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_delete_featured_results_set(client):
    """Test case for batch_delete_featured_results_set

    
    """
    body = {"IndexId":"","FeaturedResultsSetIds":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.BatchDeleteFeaturedResultsSet',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_get_document_status(client):
    """Test case for batch_get_document_status

    
    """
    body = {"IndexId":"","DocumentInfoList":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.BatchGetDocumentStatus',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_put_document(client):
    """Test case for batch_put_document

    
    """
    body = {"CustomDocumentEnrichmentConfiguration":{"InlineConfigurations":"","PreExtractionHookConfiguration":{"S3Bucket":"","LambdaArn":"","InvocationCondition":{"Operator":"","ConditionDocumentAttributeKey":"","ConditionOnValue":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""}}},"PostExtractionHookConfiguration":{"S3Bucket":"","LambdaArn":"","InvocationCondition":{"Operator":"","ConditionDocumentAttributeKey":"","ConditionOnValue":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""}}},"RoleArn":""},"IndexId":"","Documents":"","RoleArn":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.BatchPutDocument',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clear_query_suggestions(client):
    """Test case for clear_query_suggestions

    
    """
    body = {"IndexId":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.ClearQuerySuggestions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_access_control_configuration(client):
    """Test case for create_access_control_configuration

    
    """
    body = {"AccessControlList":"","IndexId":"","HierarchicalAccessControlList":"","Description":"","ClientToken":"","Name":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.CreateAccessControlConfiguration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_data_source(client):
    """Test case for create_data_source

    
    """
    body = {"CustomDocumentEnrichmentConfiguration":{"InlineConfigurations":"","PreExtractionHookConfiguration":{"S3Bucket":"","LambdaArn":"","InvocationCondition":{"Operator":"","ConditionDocumentAttributeKey":"","ConditionOnValue":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""}}},"PostExtractionHookConfiguration":{"S3Bucket":"","LambdaArn":"","InvocationCondition":{"Operator":"","ConditionDocumentAttributeKey":"","ConditionOnValue":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""}}},"RoleArn":""},"IndexId":"","LanguageCode":"","Type":"","Description":"","Configuration":{"GoogleDriveConfiguration":{"SecretArn":"","ExcludeSharedDrives":"","ExcludeUserAccounts":"","InclusionPatterns":"","ExcludeMimeTypes":"","FieldMappings":"","ExclusionPatterns":""},"WebCrawlerConfiguration":{"AuthenticationConfiguration":{"BasicAuthentication":""},"MaxLinksPerPage":"","ProxyConfiguration":{"Port":"","Host":"","Credentials":""},"UrlExclusionPatterns":"","MaxUrlsPerMinuteCrawlRate":"","UrlInclusionPatterns":"","Urls":{"SiteMapsConfiguration":{"SiteMaps":""},"SeedUrlConfiguration":{"WebCrawlerMode":"","SeedUrls":""}},"MaxContentSizePerPageInMegaBytes":"","CrawlDepth":""},"SalesforceConfiguration":{"SecretArn":"","ServerUrl":"","IncludeAttachmentFilePatterns":"","StandardObjectConfigurations":"","StandardObjectAttachmentConfiguration":{"DocumentTitleFieldName":"","FieldMappings":""},"ExcludeAttachmentFilePatterns":"","CrawlAttachments":"","ChatterFeedConfiguration":{"DocumentTitleFieldName":"","IncludeFilterTypes":"","FieldMappings":"","DocumentDataFieldName":""},"KnowledgeArticleConfiguration":{"IncludedStates":"","StandardKnowledgeArticleTypeConfiguration":{"DocumentTitleFieldName":"","FieldMappings":"","DocumentDataFieldName":""},"CustomKnowledgeArticleTypeConfigurations":""}},"GitHubConfiguration":{"SaaSConfiguration":{"OrganizationName":"","HostUrl":""},"GitHubPullRequestDocumentAttachmentConfigurationFieldMappings":"","GitHubIssueCommentConfigurationFieldMappings":"","GitHubPullRequestCommentConfigurationFieldMappings":"","GitHubIssueDocumentConfigurationFieldMappings":"","UseChangeLog":"","OnPremiseConfiguration":{"OrganizationName":"","SslCertificateS3Path":{"Bucket":"","Key":""},"HostUrl":""},"SecretArn":"","InclusionFileNamePatterns":"","ExclusionFolderNamePatterns":"","Type":"","GitHubCommitConfigurationFieldMappings":"","GitHubIssueAttachmentConfigurationFieldMappings":"","GitHubPullRequestDocumentConfigurationFieldMappings":"","RepositoryFilter":"","InclusionFileTypePatterns":"","InclusionFolderNamePatterns":"","GitHubRepositoryConfigurationFieldMappings":"","GitHubDocumentCrawlProperties":{"CrawlPullRequest":"","CrawlPullRequestCommentAttachment":"","CrawlIssueComment":"","CrawlIssueCommentAttachment":"","CrawlPullRequestComment":"","CrawlIssue":"","CrawlRepositoryDocuments":""},"VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"ExclusionFileTypePatterns":"","ExclusionFileNamePatterns":""},"DatabaseConfiguration":{"SqlConfiguration":{"QueryIdentifiersEnclosingOption":""},"DatabaseEngineType":"","ConnectionConfiguration":{"SecretArn":"","TableName":"","DatabasePort":"","DatabaseHost":"","DatabaseName":""},"ColumnConfiguration":{"ChangeDetectingColumns":"","DocumentTitleColumnName":"","DocumentIdColumnName":"","DocumentDataColumnName":"","FieldMappings":""},"VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"AclConfiguration":{"AllowedGroupsColumnName":""}},"ConfluenceConfiguration":{"SecretArn":"","AttachmentConfiguration":{"AttachmentFieldMappings":"","CrawlAttachments":""},"ServerUrl":"","PageConfiguration":{"PageFieldMappings":""},"BlogConfiguration":{"BlogFieldMappings":""},"ProxyConfiguration":{"Port":"","Host":"","Credentials":""},"Version":"","VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"InclusionPatterns":"","ExclusionPatterns":"","SpaceConfiguration":{"ExcludeSpaces":"","SpaceFieldMappings":"","CrawlPersonalSpaces":"","CrawlArchivedSpaces":"","IncludeSpaces":""},"AuthenticationType":""},"WorkDocsConfiguration":{"CrawlComments":"","OrganizationId":"","InclusionPatterns":"","UseChangeLog":"","FieldMappings":"","ExclusionPatterns":""},"QuipConfiguration":{"SecretArn":"","CrawlChatRooms":"","ThreadFieldMappings":"","MessageFieldMappings":"","FolderIds":"","AttachmentFieldMappings":"","CrawlAttachments":"","InclusionPatterns":"","VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"Domain":"","CrawlFileComments":"","ExclusionPatterns":""},"TemplateConfiguration":{"Template":""},"ServiceNowConfiguration":{"SecretArn":"","HostUrl":"","ServiceCatalogConfiguration":{"DocumentTitleFieldName":"","IncludeAttachmentFilePatterns":"","ExcludeAttachmentFilePatterns":"","CrawlAttachments":"","FieldMappings":"","DocumentDataFieldName":""},"ServiceNowBuildVersion":"","KnowledgeArticleConfiguration":{"DocumentTitleFieldName":"","IncludeAttachmentFilePatterns":"","ExcludeAttachmentFilePatterns":"","FilterQuery":"","CrawlAttachments":"","FieldMappings":"","DocumentDataFieldName":""},"AuthenticationType":""},"BoxConfiguration":{"TaskFieldMappings":"","CrawlTasks":"","FileFieldMappings":"","CrawlWebLinks":"","UseChangeLog":"","EnterpriseId":"","SecretArn":"","WebLinkFieldMappings":"","CommentFieldMappings":"","CrawlComments":"","InclusionPatterns":"","VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"ExclusionPatterns":""},"S3Configuration":{"BucketName":"","InclusionPatterns":"","InclusionPrefixes":"","AccessControlListConfiguration":{"KeyPath":""},"ExclusionPatterns":"","DocumentsMetadataConfiguration":{"S3Prefix":""}},"SharePointConfiguration":{"CrawlAttachments":"","Urls":"","UseChangeLog":"","FieldMappings":"","SecretArn":"","DocumentTitleFieldName":"","SslCertificateS3Path":{"Bucket":"","Key":""},"DisableLocalGroups":"","ProxyConfiguration":{"Port":"","Host":"","Credentials":""},"InclusionPatterns":"","VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"ExclusionPatterns":"","SharePointVersion":"","AuthenticationType":""},"OneDriveConfiguration":{"TenantDomain":"","SecretArn":"","DisableLocalGroups":"","OneDriveUsers":{"OneDriveUserList":"","OneDriveUserS3Path":{"Bucket":"","Key":""}},"InclusionPatterns":"","FieldMappings":"","ExclusionPatterns":""},"FsxConfiguration":{"SecretArn":"","FileSystemType":"","FileSystemId":"","VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"InclusionPatterns":"","FieldMappings":"","ExclusionPatterns":""},"JiraConfiguration":{"Status":"","ProjectFieldMappings":"","IssueType":"","AttachmentFieldMappings":"","UseChangeLog":"","IssueFieldMappings":"","SecretArn":"","Project":"","CommentFieldMappings":"","IssueSubEntityFilter":"","WorkLogFieldMappings":"","InclusionPatterns":"","VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"JiraAccountUrl":"","ExclusionPatterns":""},"SlackConfiguration":{"ExcludeArchived":"","PrivateChannelFilter":"","PublicChannelFilter":"","CrawlBotMessage":"","TeamId":"","UseChangeLog":"","FieldMappings":"","SinceCrawlDate":"","SecretArn":"","VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"InclusionPatterns":"","SlackEntityList":"","LookBackPeriod":"","ExclusionPatterns":""},"AlfrescoConfiguration":{"WikiFieldMappings":"","SiteId":"","DocumentLibraryFieldMappings":"","SiteUrl":"","SecretArn":"","SslCertificateS3Path":{"Bucket":"","Key":""},"CrawlSystemFolders":"","CrawlComments":"","BlogFieldMappings":"","InclusionPatterns":"","VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"EntityFilter":"","ExclusionPatterns":""}},"Schedule":"","VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"ClientToken":"","RoleArn":"","Tags":"","Name":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.CreateDataSource',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_experience(client):
    """Test case for create_experience

    
    """
    body = {"IndexId":"","Description":"","Configuration":{"UserIdentityConfiguration":{"IdentityAttributeName":""},"ContentSourceConfiguration":{"DirectPutContent":"","DataSourceIds":"","FaqIds":""}},"ClientToken":"","RoleArn":"","Name":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.CreateExperience',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_faq(client):
    """Test case for create_faq

    
    """
    body = {"IndexId":"","LanguageCode":"","Description":"","S3Path":{"Bucket":"","Key":""},"FileFormat":"","ClientToken":"","RoleArn":"","Tags":"","Name":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.CreateFaq',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_featured_results_set(client):
    """Test case for create_featured_results_set

    
    """
    body = {"Status":"","IndexId":"","Description":"","FeaturedDocuments":"","QueryTexts":"","FeaturedResultsSetName":"","ClientToken":"","Tags":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.CreateFeaturedResultsSet',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_index(client):
    """Test case for create_index

    
    """
    body = {"Description":"","UserContextPolicy":"","UserGroupResolutionConfiguration":{"UserGroupResolutionMode":""},"ServerSideEncryptionConfiguration":{"KmsKeyId":""},"ClientToken":"","Edition":"","RoleArn":"","Tags":"","Name":"","UserTokenConfigurations":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.CreateIndex',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_query_suggestions_block_list(client):
    """Test case for create_query_suggestions_block_list

    
    """
    body = {"IndexId":"","Description":"","SourceS3Path":{"Bucket":"","Key":""},"ClientToken":"","RoleArn":"","Tags":"","Name":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.CreateQuerySuggestionsBlockList',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_thesaurus(client):
    """Test case for create_thesaurus

    
    """
    body = {"IndexId":"","Description":"","SourceS3Path":{"Bucket":"","Key":""},"ClientToken":"","RoleArn":"","Tags":"","Name":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.CreateThesaurus',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_access_control_configuration(client):
    """Test case for delete_access_control_configuration

    
    """
    body = {"IndexId":"","Id":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.DeleteAccessControlConfiguration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_data_source(client):
    """Test case for delete_data_source

    
    """
    body = {"IndexId":"","Id":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.DeleteDataSource',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_experience(client):
    """Test case for delete_experience

    
    """
    body = {"IndexId":"","Id":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.DeleteExperience',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_faq(client):
    """Test case for delete_faq

    
    """
    body = {"IndexId":"","Id":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.DeleteFaq',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_index(client):
    """Test case for delete_index

    
    """
    body = {"Id":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.DeleteIndex',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_principal_mapping(client):
    """Test case for delete_principal_mapping

    
    """
    body = {"IndexId":"","DataSourceId":"","OrderingId":"","GroupId":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.DeletePrincipalMapping',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_query_suggestions_block_list(client):
    """Test case for delete_query_suggestions_block_list

    
    """
    body = {"IndexId":"","Id":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.DeleteQuerySuggestionsBlockList',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_thesaurus(client):
    """Test case for delete_thesaurus

    
    """
    body = {"IndexId":"","Id":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.DeleteThesaurus',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_access_control_configuration(client):
    """Test case for describe_access_control_configuration

    
    """
    body = {"IndexId":"","Id":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.DescribeAccessControlConfiguration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_data_source(client):
    """Test case for describe_data_source

    
    """
    body = {"IndexId":"","Id":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.DescribeDataSource',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_experience(client):
    """Test case for describe_experience

    
    """
    body = {"IndexId":"","Id":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.DescribeExperience',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_faq(client):
    """Test case for describe_faq

    
    """
    body = {"IndexId":"","Id":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.DescribeFaq',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_featured_results_set(client):
    """Test case for describe_featured_results_set

    
    """
    body = {"IndexId":"","FeaturedResultsSetId":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.DescribeFeaturedResultsSet',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_index(client):
    """Test case for describe_index

    
    """
    body = {"Id":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.DescribeIndex',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_principal_mapping(client):
    """Test case for describe_principal_mapping

    
    """
    body = {"IndexId":"","DataSourceId":"","GroupId":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.DescribePrincipalMapping',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_query_suggestions_block_list(client):
    """Test case for describe_query_suggestions_block_list

    
    """
    body = {"IndexId":"","Id":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.DescribeQuerySuggestionsBlockList',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_query_suggestions_config(client):
    """Test case for describe_query_suggestions_config

    
    """
    body = {"IndexId":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.DescribeQuerySuggestionsConfig',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_thesaurus(client):
    """Test case for describe_thesaurus

    
    """
    body = {"IndexId":"","Id":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.DescribeThesaurus',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disassociate_entities_from_experience(client):
    """Test case for disassociate_entities_from_experience

    
    """
    body = {"IndexId":"","EntityList":"","Id":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.DisassociateEntitiesFromExperience',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disassociate_personas_from_entities(client):
    """Test case for disassociate_personas_from_entities

    
    """
    body = {"IndexId":"","EntityIds":"","Id":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.DisassociatePersonasFromEntities',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_query_suggestions(client):
    """Test case for get_query_suggestions

    
    """
    body = {"IndexId":"","QueryText":"","MaxSuggestionsCount":"","SuggestionTypes":"","AttributeSuggestionsConfig":{"AdditionalResponseAttributes":"","UserContext":{"UserId":"","Groups":"","DataSourceGroups":"","Token":""},"AttributeFilter":{"ContainsAny":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"LessThan":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"GreaterThan":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"NotFilter":{"ContainsAny":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"LessThan":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"GreaterThan":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"LessThanOrEquals":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"OrAllFilters":"","EqualsTo":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"GreaterThanOrEquals":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"AndAllFilters":"","ContainsAll":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""}},"LessThanOrEquals":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"OrAllFilters":"","EqualsTo":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"GreaterThanOrEquals":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"AndAllFilters":"","ContainsAll":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""}},"SuggestionAttributes":""}}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.GetQuerySuggestions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_snapshots(client):
    """Test case for get_snapshots

    
    """
    body = {"IndexId":"","NextToken":"","MetricType":"","MaxResults":"","Interval":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.GetSnapshots',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_access_control_configurations(client):
    """Test case for list_access_control_configurations

    
    """
    body = {"IndexId":"","NextToken":"","MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.ListAccessControlConfigurations',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_data_source_sync_jobs(client):
    """Test case for list_data_source_sync_jobs

    
    """
    body = {"IndexId":"","NextToken":"","StartTimeFilter":{"EndTime":"","StartTime":""},"MaxResults":"","StatusFilter":"","Id":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.ListDataSourceSyncJobs',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_data_sources(client):
    """Test case for list_data_sources

    
    """
    body = {"IndexId":"","NextToken":"","MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.ListDataSources',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_entity_personas(client):
    """Test case for list_entity_personas

    
    """
    body = {"IndexId":"","NextToken":"","MaxResults":"","Id":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.ListEntityPersonas',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_experience_entities(client):
    """Test case for list_experience_entities

    
    """
    body = {"IndexId":"","NextToken":"","Id":""}
    params = [('NextToken', 'next_token_example')]
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.ListExperienceEntities',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_experiences(client):
    """Test case for list_experiences

    
    """
    body = {"IndexId":"","NextToken":"","MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.ListExperiences',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_faqs(client):
    """Test case for list_faqs

    
    """
    body = {"IndexId":"","NextToken":"","MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.ListFaqs',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_featured_results_sets(client):
    """Test case for list_featured_results_sets

    
    """
    body = {"IndexId":"","NextToken":"","MaxResults":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.ListFeaturedResultsSets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_groups_older_than_ordering_id(client):
    """Test case for list_groups_older_than_ordering_id

    
    """
    body = {"IndexId":"","NextToken":"","MaxResults":"","DataSourceId":"","OrderingId":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.ListGroupsOlderThanOrderingId',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_indices(client):
    """Test case for list_indices

    
    """
    body = {"NextToken":"","MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.ListIndices',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_query_suggestions_block_lists(client):
    """Test case for list_query_suggestions_block_lists

    
    """
    body = {"IndexId":"","NextToken":"","MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.ListQuerySuggestionsBlockLists',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tags_for_resource(client):
    """Test case for list_tags_for_resource

    
    """
    body = {"ResourceARN":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.ListTagsForResource',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_thesauri(client):
    """Test case for list_thesauri

    
    """
    body = {"IndexId":"","NextToken":"","MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.ListThesauri',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_principal_mapping(client):
    """Test case for put_principal_mapping

    
    """
    body = {"IndexId":"","GroupMembers":{"MemberUsers":"","S3PathforGroupMembers":{"Bucket":"","Key":""},"MemberGroups":""},"DataSourceId":"","OrderingId":"","RoleArn":"","GroupId":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.PutPrincipalMapping',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query(client):
    """Test case for query

    
    """
    body = {"SortingConfiguration":{"SortOrder":"","DocumentAttributeKey":""},"IndexId":"","VisitorId":"","Facets":"","PageSize":"","RequestedDocumentAttributes":"","UserContext":{"UserId":"","Groups":"","DataSourceGroups":"","Token":""},"DocumentRelevanceOverrideConfigurations":"","QueryText":"","SpellCorrectionConfiguration":{"IncludeQuerySpellCheckSuggestions":""},"PageNumber":"","AttributeFilter":{"ContainsAny":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"LessThan":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"GreaterThan":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"NotFilter":{"ContainsAny":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"LessThan":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"GreaterThan":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"LessThanOrEquals":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"OrAllFilters":"","EqualsTo":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"GreaterThanOrEquals":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"AndAllFilters":"","ContainsAll":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""}},"LessThanOrEquals":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"OrAllFilters":"","EqualsTo":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"GreaterThanOrEquals":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"AndAllFilters":"","ContainsAll":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""}},"QueryResultTypeFilter":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.Query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve(client):
    """Test case for retrieve

    
    """
    body = {"IndexId":"","PageSize":"","PageNumber":"","RequestedDocumentAttributes":"","UserContext":{"UserId":"","Groups":"","DataSourceGroups":"","Token":""},"AttributeFilter":{"ContainsAny":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"LessThan":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"GreaterThan":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"NotFilter":{"ContainsAny":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"LessThan":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"GreaterThan":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"LessThanOrEquals":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"OrAllFilters":"","EqualsTo":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"GreaterThanOrEquals":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"AndAllFilters":"","ContainsAll":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""}},"LessThanOrEquals":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"OrAllFilters":"","EqualsTo":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"GreaterThanOrEquals":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""},"AndAllFilters":"","ContainsAll":{"Value":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""},"Key":""}},"DocumentRelevanceOverrideConfigurations":"","QueryText":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.Retrieve',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_data_source_sync_job(client):
    """Test case for start_data_source_sync_job

    
    """
    body = {"IndexId":"","Id":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.StartDataSourceSyncJob',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_data_source_sync_job(client):
    """Test case for stop_data_source_sync_job

    
    """
    body = {"IndexId":"","Id":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.StopDataSourceSyncJob',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_submit_feedback(client):
    """Test case for submit_feedback

    
    """
    body = {"IndexId":"","RelevanceFeedbackItems":"","QueryId":"","ClickFeedbackItems":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.SubmitFeedback',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_resource(client):
    """Test case for tag_resource

    
    """
    body = {"ResourceARN":"","Tags":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.TagResource',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_untag_resource(client):
    """Test case for untag_resource

    
    """
    body = {"ResourceARN":"","TagKeys":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.UntagResource',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_access_control_configuration(client):
    """Test case for update_access_control_configuration

    
    """
    body = {"AccessControlList":"","IndexId":"","HierarchicalAccessControlList":"","Description":"","Id":"","Name":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.UpdateAccessControlConfiguration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_data_source(client):
    """Test case for update_data_source

    
    """
    body = {"CustomDocumentEnrichmentConfiguration":{"InlineConfigurations":"","PreExtractionHookConfiguration":{"S3Bucket":"","LambdaArn":"","InvocationCondition":{"Operator":"","ConditionDocumentAttributeKey":"","ConditionOnValue":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""}}},"PostExtractionHookConfiguration":{"S3Bucket":"","LambdaArn":"","InvocationCondition":{"Operator":"","ConditionDocumentAttributeKey":"","ConditionOnValue":{"DateValue":"","LongValue":"","StringValue":"","StringListValue":""}}},"RoleArn":""},"IndexId":"","LanguageCode":"","Description":"","Configuration":{"GoogleDriveConfiguration":{"SecretArn":"","ExcludeSharedDrives":"","ExcludeUserAccounts":"","InclusionPatterns":"","ExcludeMimeTypes":"","FieldMappings":"","ExclusionPatterns":""},"WebCrawlerConfiguration":{"AuthenticationConfiguration":{"BasicAuthentication":""},"MaxLinksPerPage":"","ProxyConfiguration":{"Port":"","Host":"","Credentials":""},"UrlExclusionPatterns":"","MaxUrlsPerMinuteCrawlRate":"","UrlInclusionPatterns":"","Urls":{"SiteMapsConfiguration":{"SiteMaps":""},"SeedUrlConfiguration":{"WebCrawlerMode":"","SeedUrls":""}},"MaxContentSizePerPageInMegaBytes":"","CrawlDepth":""},"SalesforceConfiguration":{"SecretArn":"","ServerUrl":"","IncludeAttachmentFilePatterns":"","StandardObjectConfigurations":"","StandardObjectAttachmentConfiguration":{"DocumentTitleFieldName":"","FieldMappings":""},"ExcludeAttachmentFilePatterns":"","CrawlAttachments":"","ChatterFeedConfiguration":{"DocumentTitleFieldName":"","IncludeFilterTypes":"","FieldMappings":"","DocumentDataFieldName":""},"KnowledgeArticleConfiguration":{"IncludedStates":"","StandardKnowledgeArticleTypeConfiguration":{"DocumentTitleFieldName":"","FieldMappings":"","DocumentDataFieldName":""},"CustomKnowledgeArticleTypeConfigurations":""}},"GitHubConfiguration":{"SaaSConfiguration":{"OrganizationName":"","HostUrl":""},"GitHubPullRequestDocumentAttachmentConfigurationFieldMappings":"","GitHubIssueCommentConfigurationFieldMappings":"","GitHubPullRequestCommentConfigurationFieldMappings":"","GitHubIssueDocumentConfigurationFieldMappings":"","UseChangeLog":"","OnPremiseConfiguration":{"OrganizationName":"","SslCertificateS3Path":{"Bucket":"","Key":""},"HostUrl":""},"SecretArn":"","InclusionFileNamePatterns":"","ExclusionFolderNamePatterns":"","Type":"","GitHubCommitConfigurationFieldMappings":"","GitHubIssueAttachmentConfigurationFieldMappings":"","GitHubPullRequestDocumentConfigurationFieldMappings":"","RepositoryFilter":"","InclusionFileTypePatterns":"","InclusionFolderNamePatterns":"","GitHubRepositoryConfigurationFieldMappings":"","GitHubDocumentCrawlProperties":{"CrawlPullRequest":"","CrawlPullRequestCommentAttachment":"","CrawlIssueComment":"","CrawlIssueCommentAttachment":"","CrawlPullRequestComment":"","CrawlIssue":"","CrawlRepositoryDocuments":""},"VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"ExclusionFileTypePatterns":"","ExclusionFileNamePatterns":""},"DatabaseConfiguration":{"SqlConfiguration":{"QueryIdentifiersEnclosingOption":""},"DatabaseEngineType":"","ConnectionConfiguration":{"SecretArn":"","TableName":"","DatabasePort":"","DatabaseHost":"","DatabaseName":""},"ColumnConfiguration":{"ChangeDetectingColumns":"","DocumentTitleColumnName":"","DocumentIdColumnName":"","DocumentDataColumnName":"","FieldMappings":""},"VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"AclConfiguration":{"AllowedGroupsColumnName":""}},"ConfluenceConfiguration":{"SecretArn":"","AttachmentConfiguration":{"AttachmentFieldMappings":"","CrawlAttachments":""},"ServerUrl":"","PageConfiguration":{"PageFieldMappings":""},"BlogConfiguration":{"BlogFieldMappings":""},"ProxyConfiguration":{"Port":"","Host":"","Credentials":""},"Version":"","VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"InclusionPatterns":"","ExclusionPatterns":"","SpaceConfiguration":{"ExcludeSpaces":"","SpaceFieldMappings":"","CrawlPersonalSpaces":"","CrawlArchivedSpaces":"","IncludeSpaces":""},"AuthenticationType":""},"WorkDocsConfiguration":{"CrawlComments":"","OrganizationId":"","InclusionPatterns":"","UseChangeLog":"","FieldMappings":"","ExclusionPatterns":""},"QuipConfiguration":{"SecretArn":"","CrawlChatRooms":"","ThreadFieldMappings":"","MessageFieldMappings":"","FolderIds":"","AttachmentFieldMappings":"","CrawlAttachments":"","InclusionPatterns":"","VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"Domain":"","CrawlFileComments":"","ExclusionPatterns":""},"TemplateConfiguration":{"Template":""},"ServiceNowConfiguration":{"SecretArn":"","HostUrl":"","ServiceCatalogConfiguration":{"DocumentTitleFieldName":"","IncludeAttachmentFilePatterns":"","ExcludeAttachmentFilePatterns":"","CrawlAttachments":"","FieldMappings":"","DocumentDataFieldName":""},"ServiceNowBuildVersion":"","KnowledgeArticleConfiguration":{"DocumentTitleFieldName":"","IncludeAttachmentFilePatterns":"","ExcludeAttachmentFilePatterns":"","FilterQuery":"","CrawlAttachments":"","FieldMappings":"","DocumentDataFieldName":""},"AuthenticationType":""},"BoxConfiguration":{"TaskFieldMappings":"","CrawlTasks":"","FileFieldMappings":"","CrawlWebLinks":"","UseChangeLog":"","EnterpriseId":"","SecretArn":"","WebLinkFieldMappings":"","CommentFieldMappings":"","CrawlComments":"","InclusionPatterns":"","VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"ExclusionPatterns":""},"S3Configuration":{"BucketName":"","InclusionPatterns":"","InclusionPrefixes":"","AccessControlListConfiguration":{"KeyPath":""},"ExclusionPatterns":"","DocumentsMetadataConfiguration":{"S3Prefix":""}},"SharePointConfiguration":{"CrawlAttachments":"","Urls":"","UseChangeLog":"","FieldMappings":"","SecretArn":"","DocumentTitleFieldName":"","SslCertificateS3Path":{"Bucket":"","Key":""},"DisableLocalGroups":"","ProxyConfiguration":{"Port":"","Host":"","Credentials":""},"InclusionPatterns":"","VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"ExclusionPatterns":"","SharePointVersion":"","AuthenticationType":""},"OneDriveConfiguration":{"TenantDomain":"","SecretArn":"","DisableLocalGroups":"","OneDriveUsers":{"OneDriveUserList":"","OneDriveUserS3Path":{"Bucket":"","Key":""}},"InclusionPatterns":"","FieldMappings":"","ExclusionPatterns":""},"FsxConfiguration":{"SecretArn":"","FileSystemType":"","FileSystemId":"","VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"InclusionPatterns":"","FieldMappings":"","ExclusionPatterns":""},"JiraConfiguration":{"Status":"","ProjectFieldMappings":"","IssueType":"","AttachmentFieldMappings":"","UseChangeLog":"","IssueFieldMappings":"","SecretArn":"","Project":"","CommentFieldMappings":"","IssueSubEntityFilter":"","WorkLogFieldMappings":"","InclusionPatterns":"","VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"JiraAccountUrl":"","ExclusionPatterns":""},"SlackConfiguration":{"ExcludeArchived":"","PrivateChannelFilter":"","PublicChannelFilter":"","CrawlBotMessage":"","TeamId":"","UseChangeLog":"","FieldMappings":"","SinceCrawlDate":"","SecretArn":"","VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"InclusionPatterns":"","SlackEntityList":"","LookBackPeriod":"","ExclusionPatterns":""},"AlfrescoConfiguration":{"WikiFieldMappings":"","SiteId":"","DocumentLibraryFieldMappings":"","SiteUrl":"","SecretArn":"","SslCertificateS3Path":{"Bucket":"","Key":""},"CrawlSystemFolders":"","CrawlComments":"","BlogFieldMappings":"","InclusionPatterns":"","VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"EntityFilter":"","ExclusionPatterns":""}},"Schedule":"","Id":"","VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":""},"RoleArn":"","Name":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.UpdateDataSource',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_experience(client):
    """Test case for update_experience

    
    """
    body = {"IndexId":"","Description":"","Configuration":{"UserIdentityConfiguration":{"IdentityAttributeName":""},"ContentSourceConfiguration":{"DirectPutContent":"","DataSourceIds":"","FaqIds":""}},"Id":"","RoleArn":"","Name":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.UpdateExperience',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_featured_results_set(client):
    """Test case for update_featured_results_set

    
    """
    body = {"Status":"","IndexId":"","Description":"","FeaturedDocuments":"","QueryTexts":"","FeaturedResultsSetId":"","FeaturedResultsSetName":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.UpdateFeaturedResultsSet',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_index(client):
    """Test case for update_index

    
    """
    body = {"Description":"","DocumentMetadataConfigurationUpdates":"","UserContextPolicy":"","CapacityUnits":{"QueryCapacityUnits":"","StorageCapacityUnits":""},"UserGroupResolutionConfiguration":{"UserGroupResolutionMode":""},"Id":"","RoleArn":"","Name":"","UserTokenConfigurations":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.UpdateIndex',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_query_suggestions_block_list(client):
    """Test case for update_query_suggestions_block_list

    
    """
    body = {"IndexId":"","Description":"","Id":"","SourceS3Path":{"Bucket":"","Key":""},"RoleArn":"","Name":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.UpdateQuerySuggestionsBlockList',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_query_suggestions_config(client):
    """Test case for update_query_suggestions_config

    
    """
    body = {"IndexId":"","QueryLogLookBackWindowInDays":"","MinimumQueryCount":"","MinimumNumberOfQueryingUsers":"","Mode":"","IncludeQueriesWithoutUserInformation":"","AttributeSuggestionsConfig":{"AttributeSuggestionsMode":"","SuggestableConfigList":""}}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.UpdateQuerySuggestionsConfig',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_thesaurus(client):
    """Test case for update_thesaurus

    
    """
    body = {"IndexId":"","Description":"","Id":"","SourceS3Path":{"Bucket":"","Key":""},"RoleArn":"","Name":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSKendraFrontendService.UpdateThesaurus',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

