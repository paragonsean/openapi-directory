from typing import List, Dict
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
from openapi_server import util


async def associate_entities_to_experience(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_entities_to_experience

    Grants users or groups in your IAM Identity Center identity source access to your Amazon Kendra experience. You can create an Amazon Kendra experience such as a search application. For more information on creating a search application experience, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html\&quot;&gt;Building a search experience with no code&lt;/a&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociateEntitiesToExperienceRequest.from_dict(body)
    return web.Response(status=200)


async def associate_personas_to_entities(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_personas_to_entities

    Defines the specific permissions of users or groups in your IAM Identity Center identity source with access to your Amazon Kendra experience. You can create an Amazon Kendra experience such as a search application. For more information on creating a search application experience, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html\&quot;&gt;Building a search experience with no code&lt;/a&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociatePersonasToEntitiesRequest.from_dict(body)
    return web.Response(status=200)


async def batch_delete_document(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_delete_document

    &lt;p&gt;Removes one or more documents from an index. The documents must have been added with the &lt;code&gt;BatchPutDocument&lt;/code&gt; API.&lt;/p&gt; &lt;p&gt;The documents are deleted asynchronously. You can see the progress of the deletion by using Amazon Web Services CloudWatch. Any error messages related to the processing of the batch are sent to you CloudWatch log.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchDeleteDocumentRequest.from_dict(body)
    return web.Response(status=200)


async def batch_delete_featured_results_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_delete_featured_results_set

    Removes one or more sets of featured results. Features results are placed above all other results for certain queries. If there&#39;s an exact match of a query, then one or more specific documents are featured in the search results.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchDeleteFeaturedResultsSetRequest.from_dict(body)
    return web.Response(status=200)


async def batch_get_document_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_get_document_status

    &lt;p&gt;Returns the indexing status for one or more documents submitted with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/API_BatchPutDocument.html\&quot;&gt; BatchPutDocument&lt;/a&gt; API.&lt;/p&gt; &lt;p&gt;When you use the &lt;code&gt;BatchPutDocument&lt;/code&gt; API, documents are indexed asynchronously. You can use the &lt;code&gt;BatchGetDocumentStatus&lt;/code&gt; API to get the current status of a list of documents so that you can determine if they have been successfully indexed.&lt;/p&gt; &lt;p&gt;You can also use the &lt;code&gt;BatchGetDocumentStatus&lt;/code&gt; API to check the status of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/API_BatchDeleteDocument.html\&quot;&gt; BatchDeleteDocument&lt;/a&gt; API. When a document is deleted from the index, Amazon Kendra returns &lt;code&gt;NOT_FOUND&lt;/code&gt; as the status.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchGetDocumentStatusRequest.from_dict(body)
    return web.Response(status=200)


async def batch_put_document(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_put_document

    &lt;p&gt;Adds one or more documents to an index.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;BatchPutDocument&lt;/code&gt; API enables you to ingest inline documents or a set of documents stored in an Amazon S3 bucket. Use this API to ingest your text and unstructured text into an index, add custom attributes to the documents, and to attach an access control list to the documents added to the index.&lt;/p&gt; &lt;p&gt;The documents are indexed asynchronously. You can see the progress of the batch using Amazon Web Services CloudWatch. Any error messages related to processing the batch are sent to your Amazon Web Services CloudWatch log.&lt;/p&gt; &lt;p&gt;For an example of ingesting inline documents using Python and Java SDKs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/in-adding-binary-doc.html\&quot;&gt;Adding files directly to an index&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchPutDocumentRequest.from_dict(body)
    return web.Response(status=200)


async def clear_query_suggestions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """clear_query_suggestions

    &lt;p&gt;Clears existing query suggestions from an index.&lt;/p&gt; &lt;p&gt;This deletes existing suggestions only, not the queries in the query log. After you clear suggestions, Amazon Kendra learns new suggestions based on new queries added to the query log from the time you cleared suggestions. If you do not see any new suggestions, then please allow Amazon Kendra to collect enough queries to learn new suggestions.&lt;/p&gt; &lt;p&gt; &lt;code&gt;ClearQuerySuggestions&lt;/code&gt; is currently not supported in the Amazon Web Services GovCloud (US-West) region.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ClearQuerySuggestionsRequest.from_dict(body)
    return web.Response(status=200)


async def create_access_control_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_access_control_configuration

    &lt;p&gt;Creates an access configuration for your documents. This includes user and group access information for your documents. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.&lt;/p&gt; &lt;p&gt;You can use this to re-configure your existing document level access control without indexing all of your documents again. For example, your index contains top-secret company documents that only certain employees or users should access. One of these users leaves the company or switches to a team that should be blocked from accessing top-secret documents. The user still has access to top-secret documents because the user had access when your documents were previously indexed. You can create a specific access control configuration for the user with deny access. You can later update the access control configuration to allow access if the user returns to the company and re-joins the &#39;top-secret&#39; team. You can re-configure access control for your documents as circumstances change.&lt;/p&gt; &lt;p&gt;To apply your access control configuration to certain documents, you call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/API_BatchPutDocument.html\&quot;&gt;BatchPutDocument&lt;/a&gt; API with the &lt;code&gt;AccessControlConfigurationId&lt;/code&gt; included in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/API_Document.html\&quot;&gt;Document&lt;/a&gt; object. If you use an S3 bucket as a data source, you update the &lt;code&gt;.metadata.json&lt;/code&gt; with the &lt;code&gt;AccessControlConfigurationId&lt;/code&gt; and synchronize your data source. Amazon Kendra currently only supports access control configuration for S3 data sources and documents indexed using the &lt;code&gt;BatchPutDocument&lt;/code&gt; API.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateAccessControlConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def create_data_source(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_data_source

    &lt;p&gt;Creates a data source connector that you want to use with an Amazon Kendra index.&lt;/p&gt; &lt;p&gt;You specify a name, data source connector type and description for your data source. You also specify configuration information for the data source connector.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateDataSource&lt;/code&gt; is a synchronous operation. The operation returns 200 if the data source was successfully created. Otherwise, an exception is raised.&lt;/p&gt; &lt;p&gt;For an example of creating an index and data source using the Python SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/gs-python.html\&quot;&gt;Getting started with Python SDK&lt;/a&gt;. For an example of creating an index and data source using the Java SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/gs-java.html\&quot;&gt;Getting started with Java SDK&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateDataSourceRequest.from_dict(body)
    return web.Response(status=200)


async def create_experience(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_experience

    Creates an Amazon Kendra experience such as a search application. For more information on creating a search application experience, including using the Python and Java SDKs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html\&quot;&gt;Building a search experience with no code&lt;/a&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateExperienceRequest.from_dict(body)
    return web.Response(status=200)


async def create_faq(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_faq

    &lt;p&gt;Creates a set of frequently ask questions (FAQs) using a specified FAQ file stored in an Amazon S3 bucket.&lt;/p&gt; &lt;p&gt;Adding FAQs to an index is an asynchronous operation.&lt;/p&gt; &lt;p&gt;For an example of adding an FAQ to an index using Python and Java SDKs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/in-creating-faq.html#using-faq-file\&quot;&gt;Using your FAQ file&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateFaqRequest.from_dict(body)
    return web.Response(status=200)


async def create_featured_results_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_featured_results_set

    &lt;p&gt;Creates a set of featured results to display at the top of the search results page. Featured results are placed above all other results for certain queries. You map specific queries to specific documents for featuring in the results. If a query contains an exact match, then one or more specific documents are featured in the search results.&lt;/p&gt; &lt;p&gt;You can create up to 50 sets of featured results per index. You can request to increase this limit by contacting &lt;a href&#x3D;\&quot;http://aws.amazon.com/contact-us/\&quot;&gt;Support&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateFeaturedResultsSetRequest.from_dict(body)
    return web.Response(status=200)


async def create_index(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_index

    &lt;p&gt;Creates an Amazon Kendra index. Index creation is an asynchronous API. To determine if index creation has completed, check the &lt;code&gt;Status&lt;/code&gt; field returned from a call to &lt;code&gt;DescribeIndex&lt;/code&gt;. The &lt;code&gt;Status&lt;/code&gt; field is set to &lt;code&gt;ACTIVE&lt;/code&gt; when the index is ready to use.&lt;/p&gt; &lt;p&gt;Once the index is active you can index your documents using the &lt;code&gt;BatchPutDocument&lt;/code&gt; API or using one of the supported data sources.&lt;/p&gt; &lt;p&gt;For an example of creating an index and data source using the Python SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/gs-python.html\&quot;&gt;Getting started with Python SDK&lt;/a&gt;. For an example of creating an index and data source using the Java SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/gs-java.html\&quot;&gt;Getting started with Java SDK&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateIndexRequest.from_dict(body)
    return web.Response(status=200)


async def create_query_suggestions_block_list(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_query_suggestions_block_list

    &lt;p&gt;Creates a block list to exlcude certain queries from suggestions.&lt;/p&gt; &lt;p&gt;Any query that contains words or phrases specified in the block list is blocked or filtered out from being shown as a suggestion.&lt;/p&gt; &lt;p&gt;You need to provide the file location of your block list text file in your S3 bucket. In your text file, enter each block word or phrase on a separate line.&lt;/p&gt; &lt;p&gt;For information on the current quota limits for block lists, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/quotas.html\&quot;&gt;Quotas for Amazon Kendra&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateQuerySuggestionsBlockList&lt;/code&gt; is currently not supported in the Amazon Web Services GovCloud (US-West) region.&lt;/p&gt; &lt;p&gt;For an example of creating a block list for query suggestions using the Python SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/query-suggestions.html#query-suggestions-blocklist\&quot;&gt;Query suggestions block list&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateQuerySuggestionsBlockListRequest.from_dict(body)
    return web.Response(status=200)


async def create_thesaurus(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_thesaurus

    &lt;p&gt;Creates a thesaurus for an index. The thesaurus contains a list of synonyms in Solr format.&lt;/p&gt; &lt;p&gt;For an example of adding a thesaurus file to an index, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/index-synonyms-adding-thesaurus-file.html\&quot;&gt;Adding custom synonyms to an index&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateThesaurusRequest.from_dict(body)
    return web.Response(status=200)


async def delete_access_control_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_access_control_configuration

    Deletes an access control configuration that you created for your documents in an index. This includes user and group access information for your documents. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteAccessControlConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_data_source(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_data_source

    Deletes an Amazon Kendra data source connector. An exception is not thrown if the data source is already being deleted. While the data source is being deleted, the &lt;code&gt;Status&lt;/code&gt; field returned by a call to the &lt;code&gt;DescribeDataSource&lt;/code&gt; API is set to &lt;code&gt;DELETING&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/delete-data-source.html\&quot;&gt;Deleting Data Sources&lt;/a&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteDataSourceRequest.from_dict(body)
    return web.Response(status=200)


async def delete_experience(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_experience

    Deletes your Amazon Kendra experience such as a search application. For more information on creating a search application experience, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html\&quot;&gt;Building a search experience with no code&lt;/a&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteExperienceRequest.from_dict(body)
    return web.Response(status=200)


async def delete_faq(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_faq

    Removes an FAQ from an index.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteFaqRequest.from_dict(body)
    return web.Response(status=200)


async def delete_index(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_index

    Deletes an existing Amazon Kendra index. An exception is not thrown if the index is already being deleted. While the index is being deleted, the &lt;code&gt;Status&lt;/code&gt; field returned by a call to the &lt;code&gt;DescribeIndex&lt;/code&gt; API is set to &lt;code&gt;DELETING&lt;/code&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteIndexRequest.from_dict(body)
    return web.Response(status=200)


async def delete_principal_mapping(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_principal_mapping

    &lt;p&gt;Deletes a group so that all users and sub groups that belong to the group can no longer access documents only available to that group.&lt;/p&gt; &lt;p&gt;For example, after deleting the group \&quot;Summer Interns\&quot;, all interns who belonged to that group no longer see intern-only documents in their search results.&lt;/p&gt; &lt;p&gt;If you want to delete or replace users or sub groups of a group, you need to use the &lt;code&gt;PutPrincipalMapping&lt;/code&gt; operation. For example, if a user in the group \&quot;Engineering\&quot; leaves the engineering team and another user takes their place, you provide an updated list of users or sub groups that belong to the \&quot;Engineering\&quot; group when calling &lt;code&gt;PutPrincipalMapping&lt;/code&gt;. You can update your internal list of users or sub groups and input this list when calling &lt;code&gt;PutPrincipalMapping&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DeletePrincipalMapping&lt;/code&gt; is currently not supported in the Amazon Web Services GovCloud (US-West) region.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeletePrincipalMappingRequest.from_dict(body)
    return web.Response(status=200)


async def delete_query_suggestions_block_list(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_query_suggestions_block_list

    &lt;p&gt;Deletes a block list used for query suggestions for an index.&lt;/p&gt; &lt;p&gt;A deleted block list might not take effect right away. Amazon Kendra needs to refresh the entire suggestions list to add back the queries that were previously blocked.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DeleteQuerySuggestionsBlockList&lt;/code&gt; is currently not supported in the Amazon Web Services GovCloud (US-West) region.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteQuerySuggestionsBlockListRequest.from_dict(body)
    return web.Response(status=200)


async def delete_thesaurus(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_thesaurus

    Deletes an existing Amazon Kendra thesaurus. 

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteThesaurusRequest.from_dict(body)
    return web.Response(status=200)


async def describe_access_control_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_access_control_configuration

    Gets information about an access control configuration that you created for your documents in an index. This includes user and group access information for your documents. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeAccessControlConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def describe_data_source(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_data_source

    Gets information about an Amazon Kendra data source connector.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeDataSourceRequest.from_dict(body)
    return web.Response(status=200)


async def describe_experience(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_experience

    Gets information about your Amazon Kendra experience such as a search application. For more information on creating a search application experience, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html\&quot;&gt;Building a search experience with no code&lt;/a&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeExperienceRequest.from_dict(body)
    return web.Response(status=200)


async def describe_faq(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_faq

    Gets information about an FAQ list.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeFaqRequest.from_dict(body)
    return web.Response(status=200)


async def describe_featured_results_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_featured_results_set

    Gets information about a set of featured results. Features results are placed above all other results for certain queries. If there&#39;s an exact match of a query, then one or more specific documents are featured in the search results.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeFeaturedResultsSetRequest.from_dict(body)
    return web.Response(status=200)


async def describe_index(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_index

    Gets information about an existing Amazon Kendra index.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeIndexRequest.from_dict(body)
    return web.Response(status=200)


async def describe_principal_mapping(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_principal_mapping

    &lt;p&gt;Describes the processing of &lt;code&gt;PUT&lt;/code&gt; and &lt;code&gt;DELETE&lt;/code&gt; actions for mapping users to their groups. This includes information on the status of actions currently processing or yet to be processed, when actions were last updated, when actions were received by Amazon Kendra, the latest action that should process and apply after other actions, and useful error messages if an action could not be processed.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DescribePrincipalMapping&lt;/code&gt; is currently not supported in the Amazon Web Services GovCloud (US-West) region.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribePrincipalMappingRequest.from_dict(body)
    return web.Response(status=200)


async def describe_query_suggestions_block_list(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_query_suggestions_block_list

    &lt;p&gt;Gets information about a block list used for query suggestions for an index.&lt;/p&gt; &lt;p&gt;This is used to check the current settings that are applied to a block list.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DescribeQuerySuggestionsBlockList&lt;/code&gt; is currently not supported in the Amazon Web Services GovCloud (US-West) region.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeQuerySuggestionsBlockListRequest.from_dict(body)
    return web.Response(status=200)


async def describe_query_suggestions_config(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_query_suggestions_config

    &lt;p&gt;Gets information on the settings of query suggestions for an index.&lt;/p&gt; &lt;p&gt;This is used to check the current settings applied to query suggestions.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DescribeQuerySuggestionsConfig&lt;/code&gt; is currently not supported in the Amazon Web Services GovCloud (US-West) region.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeQuerySuggestionsConfigRequest.from_dict(body)
    return web.Response(status=200)


async def describe_thesaurus(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_thesaurus

    Gets information about an existing Amazon Kendra thesaurus.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeThesaurusRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_entities_from_experience(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_entities_from_experience

    Prevents users or groups in your IAM Identity Center identity source from accessing your Amazon Kendra experience. You can create an Amazon Kendra experience such as a search application. For more information on creating a search application experience, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html\&quot;&gt;Building a search experience with no code&lt;/a&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DisassociateEntitiesFromExperienceRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_personas_from_entities(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_personas_from_entities

    Removes the specific permissions of users or groups in your IAM Identity Center identity source with access to your Amazon Kendra experience. You can create an Amazon Kendra experience such as a search application. For more information on creating a search application experience, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html\&quot;&gt;Building a search experience with no code&lt;/a&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DisassociatePersonasFromEntitiesRequest.from_dict(body)
    return web.Response(status=200)


async def get_query_suggestions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_query_suggestions

    &lt;p&gt;Fetches the queries that are suggested to your users.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetQuerySuggestions&lt;/code&gt; is currently not supported in the Amazon Web Services GovCloud (US-West) region.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetQuerySuggestionsRequest.from_dict(body)
    return web.Response(status=200)


async def get_snapshots(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_snapshots

    Retrieves search metrics data. The data provides a snapshot of how your users interact with your search application and how effective the application is.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = GetSnapshotsRequest.from_dict(body)
    return web.Response(status=200)


async def list_access_control_configurations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_access_control_configurations

    Lists one or more access control configurations for an index. This includes user and group access information for your documents. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListAccessControlConfigurationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_data_source_sync_jobs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_data_source_sync_jobs

    Gets statistics about synchronizing a data source connector.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListDataSourceSyncJobsRequest.from_dict(body)
    return web.Response(status=200)


async def list_data_sources(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_data_sources

    Lists the data source connectors that you have created.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListDataSourcesRequest.from_dict(body)
    return web.Response(status=200)


async def list_entity_personas(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_entity_personas

    Lists specific permissions of users and groups with access to your Amazon Kendra experience.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListEntityPersonasRequest.from_dict(body)
    return web.Response(status=200)


async def list_experience_entities(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_experience_entities

    Lists users or groups in your IAM Identity Center identity source that are granted access to your Amazon Kendra experience. You can create an Amazon Kendra experience such as a search application. For more information on creating a search application experience, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html\&quot;&gt;Building a search experience with no code&lt;/a&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListExperienceEntitiesRequest.from_dict(body)
    return web.Response(status=200)


async def list_experiences(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_experiences

    Lists one or more Amazon Kendra experiences. You can create an Amazon Kendra experience such as a search application. For more information on creating a search application experience, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html\&quot;&gt;Building a search experience with no code&lt;/a&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListExperiencesRequest.from_dict(body)
    return web.Response(status=200)


async def list_faqs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_faqs

    Gets a list of FAQ lists associated with an index.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListFaqsRequest.from_dict(body)
    return web.Response(status=200)


async def list_featured_results_sets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_featured_results_sets

    Lists all your sets of featured results for a given index. Features results are placed above all other results for certain queries. If there&#39;s an exact match of a query, then one or more specific documents are featured in the search results.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ListFeaturedResultsSetsRequest.from_dict(body)
    return web.Response(status=200)


async def list_groups_older_than_ordering_id(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_groups_older_than_ordering_id

    &lt;p&gt;Provides a list of groups that are mapped to users before a given ordering or timestamp identifier.&lt;/p&gt; &lt;p&gt; &lt;code&gt;ListGroupsOlderThanOrderingId&lt;/code&gt; is currently not supported in the Amazon Web Services GovCloud (US-West) region.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListGroupsOlderThanOrderingIdRequest.from_dict(body)
    return web.Response(status=200)


async def list_indices(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_indices

    Lists the Amazon Kendra indexes that you created.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListIndicesRequest.from_dict(body)
    return web.Response(status=200)


async def list_query_suggestions_block_lists(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_query_suggestions_block_lists

    &lt;p&gt;Lists the block lists used for query suggestions for an index.&lt;/p&gt; &lt;p&gt;For information on the current quota limits for block lists, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/quotas.html\&quot;&gt;Quotas for Amazon Kendra&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;ListQuerySuggestionsBlockLists&lt;/code&gt; is currently not supported in the Amazon Web Services GovCloud (US-West) region.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListQuerySuggestionsBlockListsRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Gets a list of tags associated with a specified resource. Indexes, FAQs, and data sources can have tags associated with them.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ListTagsForResourceRequest.from_dict(body)
    return web.Response(status=200)


async def list_thesauri(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_thesauri

    Lists the thesauri for an index.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListThesauriRequest.from_dict(body)
    return web.Response(status=200)


async def put_principal_mapping(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_principal_mapping

    &lt;p&gt;Maps users to their groups so that you only need to provide the user ID when you issue the query.&lt;/p&gt; &lt;p&gt;You can also map sub groups to groups. For example, the group \&quot;Company Intellectual Property Teams\&quot; includes sub groups \&quot;Research\&quot; and \&quot;Engineering\&quot;. These sub groups include their own list of users or people who work in these teams. Only users who work in research and engineering, and therefore belong in the intellectual property group, can see top-secret company documents in their search results.&lt;/p&gt; &lt;p&gt;This is useful for user context filtering, where search results are filtered based on the user or their group access to documents. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html\&quot;&gt;Filtering on user context&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If more than five &lt;code&gt;PUT&lt;/code&gt; actions for a group are currently processing, a validation exception is thrown.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutPrincipalMappingRequest.from_dict(body)
    return web.Response(status=200)


async def query(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """query

    &lt;p&gt;Searches an index given an input query.&lt;/p&gt; &lt;p&gt;You can configure boosting or relevance tuning at the query level to override boosting at the index level, filter based on document fields/attributes and faceted search, and filter based on the user or their group access to documents. You can also include certain fields in the response that might provide useful additional information.&lt;/p&gt; &lt;p&gt;A query response contains three types of results.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Relevant suggested answers. The answers can be either a text excerpt or table excerpt. The answer can be highlighted in the excerpt.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Matching FAQs or questions-answer from your FAQ file.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Relevant documents. This result type includes an excerpt of the document with the document title. The searched terms can be highlighted in the excerpt.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can specify that the query return only one type of result using the &lt;code&gt;QueryResultTypeFilter&lt;/code&gt; parameter. Each query returns the 100 most relevant results. If you filter result type to only question-answers, a maximum of four results are returned. If you filter result type to only answers, a maximum of three results are returned.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = QueryRequest.from_dict(body)
    return web.Response(status=200)


async def retrieve(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """retrieve

    &lt;p&gt;Retrieves relevant passages or text excerpts given an input query.&lt;/p&gt; &lt;p&gt;This API is similar to the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/APIReference/API_Query.html\&quot;&gt;Query&lt;/a&gt; API. However, by default, the &lt;code&gt;Query&lt;/code&gt; API only returns excerpt passages of up to 100 token words. With the &lt;code&gt;Retrieve&lt;/code&gt; API, you can retrieve longer passages of up to 200 token words and up to 100 semantically relevant passages. This doesn&#39;t include question-answer or FAQ type responses from your index. The passages are text excerpts that can be semantically extracted from multiple documents and multiple parts of the same document. If in extreme cases your documents produce no relevant passages using the &lt;code&gt;Retrieve&lt;/code&gt; API, you can alternatively use the &lt;code&gt;Query&lt;/code&gt; API.&lt;/p&gt; &lt;p&gt;You can also do the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Override boosting at the index level&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Filter based on document fields or attributes&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Filter based on the user or their group access to documents&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can also include certain fields in the response that might provide useful additional information.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RetrieveRequest.from_dict(body)
    return web.Response(status=200)


async def start_data_source_sync_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_data_source_sync_job

    Starts a synchronization job for a data source connector. If a synchronization job is already in progress, Amazon Kendra returns a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartDataSourceSyncJobRequest.from_dict(body)
    return web.Response(status=200)


async def stop_data_source_sync_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_data_source_sync_job

    Stops a synchronization job that is currently running. You can&#39;t stop a scheduled synchronization job.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StopDataSourceSyncJobRequest.from_dict(body)
    return web.Response(status=200)


async def submit_feedback(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """submit_feedback

    &lt;p&gt;Enables you to provide feedback to Amazon Kendra to improve the performance of your index.&lt;/p&gt; &lt;p&gt; &lt;code&gt;SubmitFeedback&lt;/code&gt; is currently not supported in the Amazon Web Services GovCloud (US-West) region.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = SubmitFeedbackRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds the specified tag to the specified index, FAQ, or data source resource. If the tag already exists, the existing value is replaced with the new value.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes a tag from an index, FAQ, or a data source.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UntagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def update_access_control_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_access_control_configuration

    &lt;p&gt;Updates an access control configuration for your documents in an index. This includes user and group access information for your documents. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.&lt;/p&gt; &lt;p&gt;You can update an access control configuration you created without indexing all of your documents again. For example, your index contains top-secret company documents that only certain employees or users should access. You created an &#39;allow&#39; access control configuration for one user who recently joined the &#39;top-secret&#39; team, switching from a team with &#39;deny&#39; access to top-secret documents. However, the user suddenly returns to their previous team and should no longer have access to top secret documents. You can update the access control configuration to re-configure access control for your documents as circumstances change.&lt;/p&gt; &lt;p&gt;You call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/API_BatchPutDocument.html\&quot;&gt;BatchPutDocument&lt;/a&gt; API to apply the updated access control configuration, with the &lt;code&gt;AccessControlConfigurationId&lt;/code&gt; included in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/API_Document.html\&quot;&gt;Document&lt;/a&gt; object. If you use an S3 bucket as a data source, you synchronize your data source to apply the &lt;code&gt;AccessControlConfigurationId&lt;/code&gt; in the &lt;code&gt;.metadata.json&lt;/code&gt; file. Amazon Kendra currently only supports access control configuration for S3 data sources and documents indexed using the &lt;code&gt;BatchPutDocument&lt;/code&gt; API.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateAccessControlConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def update_data_source(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_data_source

    Updates an existing Amazon Kendra data source connector.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateDataSourceRequest.from_dict(body)
    return web.Response(status=200)


async def update_experience(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_experience

    Updates your Amazon Kendra experience such as a search application. For more information on creating a search application experience, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html\&quot;&gt;Building a search experience with no code&lt;/a&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateExperienceRequest.from_dict(body)
    return web.Response(status=200)


async def update_featured_results_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_featured_results_set

    Updates a set of featured results. Features results are placed above all other results for certain queries. You map specific queries to specific documents for featuring in the results. If a query contains an exact match of a query, then one or more specific documents are featured in the search results.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateFeaturedResultsSetRequest.from_dict(body)
    return web.Response(status=200)


async def update_index(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_index

    Updates an existing Amazon Kendra index.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateIndexRequest.from_dict(body)
    return web.Response(status=200)


async def update_query_suggestions_block_list(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_query_suggestions_block_list

    &lt;p&gt;Updates a block list used for query suggestions for an index.&lt;/p&gt; &lt;p&gt;Updates to a block list might not take effect right away. Amazon Kendra needs to refresh the entire suggestions list to apply any updates to the block list. Other changes not related to the block list apply immediately.&lt;/p&gt; &lt;p&gt;If a block list is updating, then you need to wait for the first update to finish before submitting another update.&lt;/p&gt; &lt;p&gt;Amazon Kendra supports partial updates, so you only need to provide the fields you want to update.&lt;/p&gt; &lt;p&gt; &lt;code&gt;UpdateQuerySuggestionsBlockList&lt;/code&gt; is currently not supported in the Amazon Web Services GovCloud (US-West) region.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateQuerySuggestionsBlockListRequest.from_dict(body)
    return web.Response(status=200)


async def update_query_suggestions_config(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_query_suggestions_config

    &lt;p&gt;Updates the settings of query suggestions for an index.&lt;/p&gt; &lt;p&gt;Amazon Kendra supports partial updates, so you only need to provide the fields you want to update.&lt;/p&gt; &lt;p&gt;If an update is currently processing, you need to wait for the update to finish before making another update.&lt;/p&gt; &lt;p&gt;Updates to query suggestions settings might not take effect right away. The time for your updated settings to take effect depends on the updates made and the number of search queries in your index.&lt;/p&gt; &lt;p&gt;You can still enable/disable query suggestions at any time.&lt;/p&gt; &lt;p&gt; &lt;code&gt;UpdateQuerySuggestionsConfig&lt;/code&gt; is currently not supported in the Amazon Web Services GovCloud (US-West) region.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateQuerySuggestionsConfigRequest.from_dict(body)
    return web.Response(status=200)


async def update_thesaurus(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_thesaurus

    Updates a thesaurus for an index.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateThesaurusRequest.from_dict(body)
    return web.Response(status=200)
