from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_assistant_association_request import CreateAssistantAssociationRequest
from openapi_server.models.create_assistant_association_response import CreateAssistantAssociationResponse
from openapi_server.models.create_assistant_request import CreateAssistantRequest
from openapi_server.models.create_assistant_response import CreateAssistantResponse
from openapi_server.models.create_content_request import CreateContentRequest
from openapi_server.models.create_content_response import CreateContentResponse
from openapi_server.models.create_knowledge_base_request import CreateKnowledgeBaseRequest
from openapi_server.models.create_knowledge_base_response import CreateKnowledgeBaseResponse
from openapi_server.models.create_session_request import CreateSessionRequest
from openapi_server.models.create_session_response import CreateSessionResponse
from openapi_server.models.get_assistant_association_response import GetAssistantAssociationResponse
from openapi_server.models.get_assistant_response import GetAssistantResponse
from openapi_server.models.get_content_response import GetContentResponse
from openapi_server.models.get_content_summary_response import GetContentSummaryResponse
from openapi_server.models.get_knowledge_base_response import GetKnowledgeBaseResponse
from openapi_server.models.get_recommendations_response import GetRecommendationsResponse
from openapi_server.models.get_session_response import GetSessionResponse
from openapi_server.models.list_assistant_associations_response import ListAssistantAssociationsResponse
from openapi_server.models.list_assistants_response import ListAssistantsResponse
from openapi_server.models.list_contents_response import ListContentsResponse
from openapi_server.models.list_knowledge_bases_response import ListKnowledgeBasesResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.notify_recommendations_received_request import NotifyRecommendationsReceivedRequest
from openapi_server.models.notify_recommendations_received_response import NotifyRecommendationsReceivedResponse
from openapi_server.models.query_assistant_request import QueryAssistantRequest
from openapi_server.models.query_assistant_response import QueryAssistantResponse
from openapi_server.models.search_content_request import SearchContentRequest
from openapi_server.models.search_content_response import SearchContentResponse
from openapi_server.models.search_sessions_response import SearchSessionsResponse
from openapi_server.models.start_content_upload_request import StartContentUploadRequest
from openapi_server.models.start_content_upload_response import StartContentUploadResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_content_request import UpdateContentRequest
from openapi_server.models.update_content_response import UpdateContentResponse
from openapi_server.models.update_knowledge_base_template_uri_request import UpdateKnowledgeBaseTemplateUriRequest
from openapi_server.models.update_knowledge_base_template_uri_response import UpdateKnowledgeBaseTemplateUriResponse
from openapi_server import util


async def create_assistant(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_assistant

    Creates an Amazon Connect Wisdom assistant.

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
    body = CreateAssistantRequest.from_dict(body)
    return web.Response(status=200)


async def create_assistant_association(request: web.Request, assistant_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_assistant_association

    Creates an association between an Amazon Connect Wisdom assistant and another resource. Currently, the only supported association is with a knowledge base. An assistant can have only a single association.

    :param assistant_id: The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type assistant_id: str
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
    body = CreateAssistantAssociationRequest.from_dict(body)
    return web.Response(status=200)


async def create_content(request: web.Request, knowledge_base_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_content

    Creates Wisdom content. Before to calling this API, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html\&quot;&gt;StartContentUpload&lt;/a&gt; to upload an asset.

    :param knowledge_base_id: The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type knowledge_base_id: str
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
    body = CreateContentRequest.from_dict(body)
    return web.Response(status=200)


async def create_knowledge_base(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_knowledge_base

    &lt;p&gt;Creates a knowledge base.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When using this API, you cannot reuse &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appintegrations/latest/APIReference/Welcome.html\&quot;&gt;Amazon AppIntegrations&lt;/a&gt; DataIntegrations with external knowledge bases such as Salesforce and ServiceNow. If you do, you&#39;ll get an &lt;code&gt;InvalidRequestException&lt;/code&gt; error. &lt;/p&gt; &lt;p&gt;For example, you&#39;re programmatically managing your external knowledge base, and you want to add or remove one of the fields that is being ingested from Salesforce. Do the following:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wisdom/latest/APIReference/API_DeleteKnowledgeBase.html\&quot;&gt;DeleteKnowledgeBase&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteDataIntegration.html\&quot;&gt;DeleteDataIntegration&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html\&quot;&gt;CreateDataIntegration&lt;/a&gt; to recreate the DataIntegration or a create different one.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call CreateKnowledgeBase.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;/note&gt;

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
    body = CreateKnowledgeBaseRequest.from_dict(body)
    return web.Response(status=200)


async def create_session(request: web.Request, assistant_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_session

    Creates a session. A session is a contextual container used for generating recommendations. Amazon Connect creates a new Wisdom session for each contact on which Wisdom is enabled.

    :param assistant_id: The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type assistant_id: str
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
    body = CreateSessionRequest.from_dict(body)
    return web.Response(status=200)


async def delete_assistant(request: web.Request, assistant_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_assistant

    Deletes an assistant.

    :param assistant_id: The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type assistant_id: str
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
    return web.Response(status=200)


async def delete_assistant_association(request: web.Request, assistant_association_id, assistant_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_assistant_association

    Deletes an assistant association.

    :param assistant_association_id: The identifier of the assistant association. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type assistant_association_id: str
    :param assistant_id: The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type assistant_id: str
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
    return web.Response(status=200)


async def delete_content(request: web.Request, content_id, knowledge_base_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_content

    Deletes the content.

    :param content_id: The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type content_id: str
    :param knowledge_base_id: The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type knowledge_base_id: str
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
    return web.Response(status=200)


async def delete_knowledge_base(request: web.Request, knowledge_base_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_knowledge_base

    &lt;p&gt;Deletes the knowledge base.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When you use this API to delete an external knowledge base such as Salesforce or ServiceNow, you must also delete the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appintegrations/latest/APIReference/Welcome.html\&quot;&gt;Amazon AppIntegrations&lt;/a&gt; DataIntegration. This is because you can&#39;t reuse the DataIntegration after it&#39;s been associated with an external knowledge base. However, you can delete and recreate it. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteDataIntegration.html\&quot;&gt;DeleteDataIntegration&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html\&quot;&gt;CreateDataIntegration&lt;/a&gt; in the &lt;i&gt;Amazon AppIntegrations API Reference&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

    :param knowledge_base_id: The knowledge base to delete content from. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type knowledge_base_id: str
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
    return web.Response(status=200)


async def get_assistant(request: web.Request, assistant_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_assistant

    Retrieves information about an assistant.

    :param assistant_id: The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type assistant_id: str
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
    return web.Response(status=200)


async def get_assistant_association(request: web.Request, assistant_association_id, assistant_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_assistant_association

    Retrieves information about an assistant association.

    :param assistant_association_id: The identifier of the assistant association. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type assistant_association_id: str
    :param assistant_id: The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type assistant_id: str
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
    return web.Response(status=200)


async def get_content(request: web.Request, content_id, knowledge_base_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_content

    Retrieves content, including a pre-signed URL to download the content.

    :param content_id: The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type content_id: str
    :param knowledge_base_id: The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type knowledge_base_id: str
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
    return web.Response(status=200)


async def get_content_summary(request: web.Request, content_id, knowledge_base_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_content_summary

    Retrieves summary information about the content.

    :param content_id: The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type content_id: str
    :param knowledge_base_id: The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type knowledge_base_id: str
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
    return web.Response(status=200)


async def get_knowledge_base(request: web.Request, knowledge_base_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_knowledge_base

    Retrieves information about the knowledge base.

    :param knowledge_base_id: The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type knowledge_base_id: str
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
    return web.Response(status=200)


async def get_recommendations(request: web.Request, assistant_id, session_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, wait_time_seconds=None) -> web.Response:
    """get_recommendations

    Retrieves recommendations for the specified session. To avoid retrieving the same recommendations in subsequent calls, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wisdom/latest/APIReference/API_NotifyRecommendationsReceived.html\&quot;&gt;NotifyRecommendationsReceived&lt;/a&gt;. This API supports long-polling behavior with the &lt;code&gt;waitTimeSeconds&lt;/code&gt; parameter. Short poll is the default behavior and only returns recommendations already available. To perform a manual query against an assistant, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wisdom/latest/APIReference/API_QueryAssistant.html\&quot;&gt;QueryAssistant&lt;/a&gt;.

    :param assistant_id: The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type assistant_id: str
    :param session_id: The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type session_id: str
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
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param wait_time_seconds: The duration (in seconds) for which the call waits for a recommendation to be made available before returning. If a recommendation is available, the call returns sooner than &lt;code&gt;WaitTimeSeconds&lt;/code&gt;. If no messages are available and the wait time expires, the call returns successfully with an empty list.
    :type wait_time_seconds: int

    """
    return web.Response(status=200)


async def get_session(request: web.Request, assistant_id, session_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_session

    Retrieves information for a specified session.

    :param assistant_id: The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type assistant_id: str
    :param session_id: The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type session_id: str
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
    return web.Response(status=200)


async def list_assistant_associations(request: web.Request, assistant_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_assistant_associations

    Lists information about assistant associations.

    :param assistant_id: The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type assistant_id: str
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
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_assistants(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_assistants

    Lists information about assistants.

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
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_contents(request: web.Request, knowledge_base_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_contents

    Lists the content.

    :param knowledge_base_id: The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type knowledge_base_id: str
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
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_knowledge_bases(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_knowledge_bases

    Lists the knowledge bases.

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
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Lists the tags for the specified resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource.
    :type resource_arn: str
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
    return web.Response(status=200)


async def notify_recommendations_received(request: web.Request, assistant_id, session_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """notify_recommendations_received

    Removes the specified recommendations from the specified assistant&#39;s queue of newly available recommendations. You can use this API in conjunction with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetRecommendations.html\&quot;&gt;GetRecommendations&lt;/a&gt; and a &lt;code&gt;waitTimeSeconds&lt;/code&gt; input for long-polling behavior and avoiding duplicate recommendations.

    :param assistant_id: The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type assistant_id: str
    :param session_id: The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type session_id: str
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
    body = NotifyRecommendationsReceivedRequest.from_dict(body)
    return web.Response(status=200)


async def query_assistant(request: web.Request, assistant_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """query_assistant

    Performs a manual search against the specified assistant. To retrieve recommendations for an assistant, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetRecommendations.html\&quot;&gt;GetRecommendations&lt;/a&gt;. 

    :param assistant_id: The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type assistant_id: str
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
    body = QueryAssistantRequest.from_dict(body)
    return web.Response(status=200)


async def remove_knowledge_base_template_uri(request: web.Request, knowledge_base_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_knowledge_base_template_uri

    Removes a URI template from a knowledge base.

    :param knowledge_base_id: The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type knowledge_base_id: str
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
    return web.Response(status=200)


async def search_content(request: web.Request, knowledge_base_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """search_content

    Searches for content in a specified knowledge base. Can be used to get a specific content resource by its name.

    :param knowledge_base_id: The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type knowledge_base_id: str
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
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str

    """
    body = SearchContentRequest.from_dict(body)
    return web.Response(status=200)


async def search_sessions(request: web.Request, assistant_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """search_sessions

    Searches for sessions.

    :param assistant_id: The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type assistant_id: str
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
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str

    """
    body = SearchContentRequest.from_dict(body)
    return web.Response(status=200)


async def start_content_upload(request: web.Request, knowledge_base_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_content_upload

    Get a URL to upload content to a knowledge base. To upload content, first make a PUT request to the returned URL with your file, making sure to include the required headers. Then use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wisdom/latest/APIReference/API_CreateContent.html\&quot;&gt;CreateContent&lt;/a&gt; to finalize the content creation process or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wisdom/latest/APIReference/API_UpdateContent.html\&quot;&gt;UpdateContent&lt;/a&gt; to modify an existing resource. You can only upload content to a knowledge base of type CUSTOM.

    :param knowledge_base_id: The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type knowledge_base_id: str
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
    body = StartContentUploadRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds the specified tags to the specified resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource.
    :type resource_arn: str
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


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes the specified tags from the specified resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource.
    :type resource_arn: str
    :param tag_keys: The tag keys.
    :type tag_keys: List[str]
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
    return web.Response(status=200)


async def update_content(request: web.Request, content_id, knowledge_base_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_content

    Updates information about the content.

    :param content_id: The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type content_id: str
    :param knowledge_base_id: The identifier of the knowledge base. Can be either the ID or the ARN
    :type knowledge_base_id: str
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
    body = UpdateContentRequest.from_dict(body)
    return web.Response(status=200)


async def update_knowledge_base_template_uri(request: web.Request, knowledge_base_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_knowledge_base_template_uri

    Updates the template URI of a knowledge base. This is only supported for knowledge bases of type EXTERNAL. Include a single variable in &lt;code&gt;${variable}&lt;/code&gt; format; this interpolated by Wisdom using ingested content. For example, if you ingest a Salesforce article, it has an &lt;code&gt;Id&lt;/code&gt; value, and you can set the template URI to &lt;code&gt;https://myInstanceName.lightning.force.com/lightning/r/Knowledge__kav/*${Id}*/view&lt;/code&gt;. 

    :param knowledge_base_id: The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
    :type knowledge_base_id: str
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
    body = UpdateKnowledgeBaseTemplateUriRequest.from_dict(body)
    return web.Response(status=200)
