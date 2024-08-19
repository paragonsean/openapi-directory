from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_call_analytics_category_request import CreateCallAnalyticsCategoryRequest
from openapi_server.models.create_call_analytics_category_response import CreateCallAnalyticsCategoryResponse
from openapi_server.models.create_language_model_request import CreateLanguageModelRequest
from openapi_server.models.create_language_model_response import CreateLanguageModelResponse
from openapi_server.models.create_medical_vocabulary_request import CreateMedicalVocabularyRequest
from openapi_server.models.create_medical_vocabulary_response import CreateMedicalVocabularyResponse
from openapi_server.models.create_vocabulary_filter_request import CreateVocabularyFilterRequest
from openapi_server.models.create_vocabulary_filter_response import CreateVocabularyFilterResponse
from openapi_server.models.create_vocabulary_request import CreateVocabularyRequest
from openapi_server.models.create_vocabulary_response import CreateVocabularyResponse
from openapi_server.models.delete_call_analytics_category_request import DeleteCallAnalyticsCategoryRequest
from openapi_server.models.delete_call_analytics_job_request import DeleteCallAnalyticsJobRequest
from openapi_server.models.delete_language_model_request import DeleteLanguageModelRequest
from openapi_server.models.delete_medical_transcription_job_request import DeleteMedicalTranscriptionJobRequest
from openapi_server.models.delete_medical_vocabulary_request import DeleteMedicalVocabularyRequest
from openapi_server.models.delete_transcription_job_request import DeleteTranscriptionJobRequest
from openapi_server.models.delete_vocabulary_filter_request import DeleteVocabularyFilterRequest
from openapi_server.models.delete_vocabulary_request import DeleteVocabularyRequest
from openapi_server.models.describe_language_model_request import DescribeLanguageModelRequest
from openapi_server.models.describe_language_model_response import DescribeLanguageModelResponse
from openapi_server.models.get_call_analytics_category_request import GetCallAnalyticsCategoryRequest
from openapi_server.models.get_call_analytics_category_response import GetCallAnalyticsCategoryResponse
from openapi_server.models.get_call_analytics_job_request import GetCallAnalyticsJobRequest
from openapi_server.models.get_call_analytics_job_response import GetCallAnalyticsJobResponse
from openapi_server.models.get_medical_transcription_job_request import GetMedicalTranscriptionJobRequest
from openapi_server.models.get_medical_transcription_job_response import GetMedicalTranscriptionJobResponse
from openapi_server.models.get_medical_vocabulary_request import GetMedicalVocabularyRequest
from openapi_server.models.get_medical_vocabulary_response import GetMedicalVocabularyResponse
from openapi_server.models.get_transcription_job_request import GetTranscriptionJobRequest
from openapi_server.models.get_transcription_job_response import GetTranscriptionJobResponse
from openapi_server.models.get_vocabulary_filter_request import GetVocabularyFilterRequest
from openapi_server.models.get_vocabulary_filter_response import GetVocabularyFilterResponse
from openapi_server.models.get_vocabulary_request import GetVocabularyRequest
from openapi_server.models.get_vocabulary_response import GetVocabularyResponse
from openapi_server.models.list_call_analytics_categories_request import ListCallAnalyticsCategoriesRequest
from openapi_server.models.list_call_analytics_categories_response import ListCallAnalyticsCategoriesResponse
from openapi_server.models.list_call_analytics_jobs_request import ListCallAnalyticsJobsRequest
from openapi_server.models.list_call_analytics_jobs_response import ListCallAnalyticsJobsResponse
from openapi_server.models.list_language_models_request import ListLanguageModelsRequest
from openapi_server.models.list_language_models_response import ListLanguageModelsResponse
from openapi_server.models.list_medical_transcription_jobs_request import ListMedicalTranscriptionJobsRequest
from openapi_server.models.list_medical_transcription_jobs_response import ListMedicalTranscriptionJobsResponse
from openapi_server.models.list_medical_vocabularies_request import ListMedicalVocabulariesRequest
from openapi_server.models.list_medical_vocabularies_response import ListMedicalVocabulariesResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_transcription_jobs_request import ListTranscriptionJobsRequest
from openapi_server.models.list_transcription_jobs_response import ListTranscriptionJobsResponse
from openapi_server.models.list_vocabularies_request import ListVocabulariesRequest
from openapi_server.models.list_vocabularies_response import ListVocabulariesResponse
from openapi_server.models.list_vocabulary_filters_request import ListVocabularyFiltersRequest
from openapi_server.models.list_vocabulary_filters_response import ListVocabularyFiltersResponse
from openapi_server.models.start_call_analytics_job_request import StartCallAnalyticsJobRequest
from openapi_server.models.start_call_analytics_job_response import StartCallAnalyticsJobResponse
from openapi_server.models.start_medical_transcription_job_request import StartMedicalTranscriptionJobRequest
from openapi_server.models.start_medical_transcription_job_response import StartMedicalTranscriptionJobResponse
from openapi_server.models.start_transcription_job_request import StartTranscriptionJobRequest
from openapi_server.models.start_transcription_job_response import StartTranscriptionJobResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_call_analytics_category_request import UpdateCallAnalyticsCategoryRequest
from openapi_server.models.update_call_analytics_category_response import UpdateCallAnalyticsCategoryResponse
from openapi_server.models.update_medical_vocabulary_request import UpdateMedicalVocabularyRequest
from openapi_server.models.update_medical_vocabulary_response import UpdateMedicalVocabularyResponse
from openapi_server.models.update_vocabulary_filter_request import UpdateVocabularyFilterRequest
from openapi_server.models.update_vocabulary_filter_response import UpdateVocabularyFilterResponse
from openapi_server.models.update_vocabulary_request import UpdateVocabularyRequest
from openapi_server.models.update_vocabulary_response import UpdateVocabularyResponse
from openapi_server import util


async def create_call_analytics_category(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_call_analytics_category

    &lt;p&gt;Creates a new Call Analytics category.&lt;/p&gt; &lt;p&gt;All categories are automatically applied to your Call Analytics transcriptions. Note that in order to apply categories to your transcriptions, you must create them before submitting your transcription request, as categories cannot be applied retroactively.&lt;/p&gt; &lt;p&gt;When creating a new category, you can use the &lt;code&gt;InputType&lt;/code&gt; parameter to label the category as a &lt;code&gt;POST_CALL&lt;/code&gt; or a &lt;code&gt;REAL_TIME&lt;/code&gt; category. &lt;code&gt;POST_CALL&lt;/code&gt; categories can only be applied to post-call transcriptions and &lt;code&gt;REAL_TIME&lt;/code&gt; categories can only be applied to real-time transcriptions. If you do not include &lt;code&gt;InputType&lt;/code&gt;, your category is created as a &lt;code&gt;POST_CALL&lt;/code&gt; category by default.&lt;/p&gt; &lt;p&gt;Call Analytics categories are composed of rules. For each category, you must create between 1 and 20 rules. Rules can include these parameters: , , , and .&lt;/p&gt; &lt;p&gt;To update an existing category, see .&lt;/p&gt; &lt;p&gt;To learn more about Call Analytics categories, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-batch.html\&quot;&gt;Creating categories for post-call transcriptions&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-stream.html\&quot;&gt;Creating categories for real-time transcriptions&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateCallAnalyticsCategoryRequest.from_dict(body)
    return web.Response(status=200)


async def create_language_model(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_language_model

    &lt;p&gt;Creates a new custom language model.&lt;/p&gt; &lt;p&gt;When creating a new custom language model, you must specify:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you want a Wideband (audio sample rates over 16,000 Hz) or Narrowband (audio sample rates under 16,000 Hz) base model&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The location of your training and tuning files (this must be an Amazon S3 URI)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The language of your model&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A unique name for your model&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = CreateLanguageModelRequest.from_dict(body)
    return web.Response(status=200)


async def create_medical_vocabulary(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_medical_vocabulary

    &lt;p&gt;Creates a new custom medical vocabulary.&lt;/p&gt; &lt;p&gt;Before creating a new custom medical vocabulary, you must first upload a text file that contains your vocabulary table into an Amazon S3 bucket. Note that this differs from , where you can include a list of terms within your request using the &lt;code&gt;Phrases&lt;/code&gt; flag; &lt;code&gt;CreateMedicalVocabulary&lt;/code&gt; does not support the &lt;code&gt;Phrases&lt;/code&gt; flag and only accepts vocabularies in table format.&lt;/p&gt; &lt;p&gt;Each language has a character set that contains all allowed characters for that specific language. If you use unsupported characters, your custom vocabulary request fails. Refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html\&quot;&gt;Character Sets for Custom Vocabularies&lt;/a&gt; to get the character set for your language.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html\&quot;&gt;Custom vocabularies&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateMedicalVocabularyRequest.from_dict(body)
    return web.Response(status=200)


async def create_vocabulary(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_vocabulary

    &lt;p&gt;Creates a new custom vocabulary.&lt;/p&gt; &lt;p&gt;When creating a new custom vocabulary, you can either upload a text file that contains your new entries, phrases, and terms into an Amazon S3 bucket and include the URI in your request. Or you can include a list of terms directly in your request using the &lt;code&gt;Phrases&lt;/code&gt; flag.&lt;/p&gt; &lt;p&gt;Each language has a character set that contains all allowed characters for that specific language. If you use unsupported characters, your custom vocabulary request fails. Refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html\&quot;&gt;Character Sets for Custom Vocabularies&lt;/a&gt; to get the character set for your language.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html\&quot;&gt;Custom vocabularies&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateVocabularyRequest.from_dict(body)
    return web.Response(status=200)


async def create_vocabulary_filter(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_vocabulary_filter

    &lt;p&gt;Creates a new custom vocabulary filter.&lt;/p&gt; &lt;p&gt;You can use custom vocabulary filters to mask, delete, or flag specific words from your transcript. Custom vocabulary filters are commonly used to mask profanity in transcripts.&lt;/p&gt; &lt;p&gt;Each language has a character set that contains all allowed characters for that specific language. If you use unsupported characters, your custom vocabulary filter request fails. Refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html\&quot;&gt;Character Sets for Custom Vocabularies&lt;/a&gt; to get the character set for your language.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filtering.html\&quot;&gt;Vocabulary filtering&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateVocabularyFilterRequest.from_dict(body)
    return web.Response(status=200)


async def delete_call_analytics_category(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_call_analytics_category

    Deletes a Call Analytics category. To use this operation, specify the name of the category you want to delete using &lt;code&gt;CategoryName&lt;/code&gt;. Category names are case sensitive.

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
    body = DeleteCallAnalyticsCategoryRequest.from_dict(body)
    return web.Response(status=200)


async def delete_call_analytics_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_call_analytics_job

    Deletes a Call Analytics job. To use this operation, specify the name of the job you want to delete using &lt;code&gt;CallAnalyticsJobName&lt;/code&gt;. Job names are case sensitive.

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
    body = DeleteCallAnalyticsJobRequest.from_dict(body)
    return web.Response(status=200)


async def delete_language_model(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_language_model

    Deletes a custom language model. To use this operation, specify the name of the language model you want to delete using &lt;code&gt;ModelName&lt;/code&gt;. custom language model names are case sensitive.

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
    body = DeleteLanguageModelRequest.from_dict(body)
    return web.Response(status=200)


async def delete_medical_transcription_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_medical_transcription_job

    Deletes a medical transcription job. To use this operation, specify the name of the job you want to delete using &lt;code&gt;MedicalTranscriptionJobName&lt;/code&gt;. Job names are case sensitive.

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
    body = DeleteMedicalTranscriptionJobRequest.from_dict(body)
    return web.Response(status=200)


async def delete_medical_vocabulary(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_medical_vocabulary

    Deletes a custom medical vocabulary. To use this operation, specify the name of the custom vocabulary you want to delete using &lt;code&gt;VocabularyName&lt;/code&gt;. Custom vocabulary names are case sensitive.

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
    body = DeleteMedicalVocabularyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_transcription_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_transcription_job

    Deletes a transcription job. To use this operation, specify the name of the job you want to delete using &lt;code&gt;TranscriptionJobName&lt;/code&gt;. Job names are case sensitive.

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
    body = DeleteTranscriptionJobRequest.from_dict(body)
    return web.Response(status=200)


async def delete_vocabulary(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_vocabulary

    Deletes a custom vocabulary. To use this operation, specify the name of the custom vocabulary you want to delete using &lt;code&gt;VocabularyName&lt;/code&gt;. Custom vocabulary names are case sensitive.

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
    body = DeleteVocabularyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_vocabulary_filter(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_vocabulary_filter

    Deletes a custom vocabulary filter. To use this operation, specify the name of the custom vocabulary filter you want to delete using &lt;code&gt;VocabularyFilterName&lt;/code&gt;. Custom vocabulary filter names are case sensitive.

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
    body = DeleteVocabularyFilterRequest.from_dict(body)
    return web.Response(status=200)


async def describe_language_model(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_language_model

    &lt;p&gt;Provides information about the specified custom language model.&lt;/p&gt; &lt;p&gt;This operation also shows if the base language model that you used to create your custom language model has been updated. If Amazon Transcribe has updated the base model, you can create a new custom language model using the updated base model.&lt;/p&gt; &lt;p&gt;If you tried to create a new custom language model and the request wasn&#39;t successful, you can use &lt;code&gt;DescribeLanguageModel&lt;/code&gt; to help identify the reason for this failure.&lt;/p&gt;

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
    body = DescribeLanguageModelRequest.from_dict(body)
    return web.Response(status=200)


async def get_call_analytics_category(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_call_analytics_category

    &lt;p&gt;Provides information about the specified Call Analytics category.&lt;/p&gt; &lt;p&gt;To get a list of your Call Analytics categories, use the operation.&lt;/p&gt;

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
    body = GetCallAnalyticsCategoryRequest.from_dict(body)
    return web.Response(status=200)


async def get_call_analytics_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_call_analytics_job

    &lt;p&gt;Provides information about the specified Call Analytics job.&lt;/p&gt; &lt;p&gt;To view the job&#39;s status, refer to &lt;code&gt;CallAnalyticsJobStatus&lt;/code&gt;. If the status is &lt;code&gt;COMPLETED&lt;/code&gt;, the job is finished. You can find your completed transcript at the URI specified in &lt;code&gt;TranscriptFileUri&lt;/code&gt;. If the status is &lt;code&gt;FAILED&lt;/code&gt;, &lt;code&gt;FailureReason&lt;/code&gt; provides details on why your transcription job failed.&lt;/p&gt; &lt;p&gt;If you enabled personally identifiable information (PII) redaction, the redacted transcript appears at the location specified in &lt;code&gt;RedactedTranscriptFileUri&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If you chose to redact the audio in your media file, you can find your redacted media file at the location specified in &lt;code&gt;RedactedMediaFileUri&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To get a list of your Call Analytics jobs, use the operation.&lt;/p&gt;

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
    body = GetCallAnalyticsJobRequest.from_dict(body)
    return web.Response(status=200)


async def get_medical_transcription_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_medical_transcription_job

    &lt;p&gt;Provides information about the specified medical transcription job.&lt;/p&gt; &lt;p&gt;To view the status of the specified medical transcription job, check the &lt;code&gt;TranscriptionJobStatus&lt;/code&gt; field. If the status is &lt;code&gt;COMPLETED&lt;/code&gt;, the job is finished. You can find the results at the location specified in &lt;code&gt;TranscriptFileUri&lt;/code&gt;. If the status is &lt;code&gt;FAILED&lt;/code&gt;, &lt;code&gt;FailureReason&lt;/code&gt; provides details on why your transcription job failed.&lt;/p&gt; &lt;p&gt;To get a list of your medical transcription jobs, use the operation.&lt;/p&gt;

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
    body = GetMedicalTranscriptionJobRequest.from_dict(body)
    return web.Response(status=200)


async def get_medical_vocabulary(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_medical_vocabulary

    &lt;p&gt;Provides information about the specified custom medical vocabulary.&lt;/p&gt; &lt;p&gt;To view the status of the specified custom medical vocabulary, check the &lt;code&gt;VocabularyState&lt;/code&gt; field. If the status is &lt;code&gt;READY&lt;/code&gt;, your custom vocabulary is available to use. If the status is &lt;code&gt;FAILED&lt;/code&gt;, &lt;code&gt;FailureReason&lt;/code&gt; provides details on why your vocabulary failed.&lt;/p&gt; &lt;p&gt;To get a list of your custom medical vocabularies, use the operation.&lt;/p&gt;

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
    body = GetMedicalVocabularyRequest.from_dict(body)
    return web.Response(status=200)


async def get_transcription_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_transcription_job

    &lt;p&gt;Provides information about the specified transcription job.&lt;/p&gt; &lt;p&gt;To view the status of the specified transcription job, check the &lt;code&gt;TranscriptionJobStatus&lt;/code&gt; field. If the status is &lt;code&gt;COMPLETED&lt;/code&gt;, the job is finished. You can find the results at the location specified in &lt;code&gt;TranscriptFileUri&lt;/code&gt;. If the status is &lt;code&gt;FAILED&lt;/code&gt;, &lt;code&gt;FailureReason&lt;/code&gt; provides details on why your transcription job failed.&lt;/p&gt; &lt;p&gt;If you enabled content redaction, the redacted transcript can be found at the location specified in &lt;code&gt;RedactedTranscriptFileUri&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To get a list of your transcription jobs, use the operation.&lt;/p&gt;

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
    body = GetTranscriptionJobRequest.from_dict(body)
    return web.Response(status=200)


async def get_vocabulary(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_vocabulary

    &lt;p&gt;Provides information about the specified custom vocabulary.&lt;/p&gt; &lt;p&gt;To view the status of the specified custom vocabulary, check the &lt;code&gt;VocabularyState&lt;/code&gt; field. If the status is &lt;code&gt;READY&lt;/code&gt;, your custom vocabulary is available to use. If the status is &lt;code&gt;FAILED&lt;/code&gt;, &lt;code&gt;FailureReason&lt;/code&gt; provides details on why your custom vocabulary failed.&lt;/p&gt; &lt;p&gt;To get a list of your custom vocabularies, use the operation.&lt;/p&gt;

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
    body = GetVocabularyRequest.from_dict(body)
    return web.Response(status=200)


async def get_vocabulary_filter(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_vocabulary_filter

    &lt;p&gt;Provides information about the specified custom vocabulary filter.&lt;/p&gt; &lt;p&gt;To get a list of your custom vocabulary filters, use the operation.&lt;/p&gt;

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
    body = GetVocabularyFilterRequest.from_dict(body)
    return web.Response(status=200)


async def list_call_analytics_categories(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_call_analytics_categories

    &lt;p&gt;Provides a list of Call Analytics categories, including all rules that make up each category.&lt;/p&gt; &lt;p&gt;To get detailed information about a specific Call Analytics category, use the operation.&lt;/p&gt;

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
    body = ListCallAnalyticsCategoriesRequest.from_dict(body)
    return web.Response(status=200)


async def list_call_analytics_jobs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_call_analytics_jobs

    &lt;p&gt;Provides a list of Call Analytics jobs that match the specified criteria. If no criteria are specified, all Call Analytics jobs are returned.&lt;/p&gt; &lt;p&gt;To get detailed information about a specific Call Analytics job, use the operation.&lt;/p&gt;

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
    body = ListCallAnalyticsJobsRequest.from_dict(body)
    return web.Response(status=200)


async def list_language_models(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_language_models

    &lt;p&gt;Provides a list of custom language models that match the specified criteria. If no criteria are specified, all custom language models are returned.&lt;/p&gt; &lt;p&gt;To get detailed information about a specific custom language model, use the operation.&lt;/p&gt;

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
    body = ListLanguageModelsRequest.from_dict(body)
    return web.Response(status=200)


async def list_medical_transcription_jobs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_medical_transcription_jobs

    &lt;p&gt;Provides a list of medical transcription jobs that match the specified criteria. If no criteria are specified, all medical transcription jobs are returned.&lt;/p&gt; &lt;p&gt;To get detailed information about a specific medical transcription job, use the operation.&lt;/p&gt;

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
    body = ListMedicalTranscriptionJobsRequest.from_dict(body)
    return web.Response(status=200)


async def list_medical_vocabularies(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_medical_vocabularies

    &lt;p&gt;Provides a list of custom medical vocabularies that match the specified criteria. If no criteria are specified, all custom medical vocabularies are returned.&lt;/p&gt; &lt;p&gt;To get detailed information about a specific custom medical vocabulary, use the operation.&lt;/p&gt;

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
    body = ListMedicalVocabulariesRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    &lt;p&gt;Lists all tags associated with the specified transcription job, vocabulary, model, or resource.&lt;/p&gt; &lt;p&gt;To learn more about using tags with Amazon Transcribe, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html\&quot;&gt;Tagging resources&lt;/a&gt;.&lt;/p&gt;

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


async def list_transcription_jobs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_transcription_jobs

    &lt;p&gt;Provides a list of transcription jobs that match the specified criteria. If no criteria are specified, all transcription jobs are returned.&lt;/p&gt; &lt;p&gt;To get detailed information about a specific transcription job, use the operation.&lt;/p&gt;

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
    body = ListTranscriptionJobsRequest.from_dict(body)
    return web.Response(status=200)


async def list_vocabularies(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_vocabularies

    &lt;p&gt;Provides a list of custom vocabularies that match the specified criteria. If no criteria are specified, all custom vocabularies are returned.&lt;/p&gt; &lt;p&gt;To get detailed information about a specific custom vocabulary, use the operation.&lt;/p&gt;

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
    body = ListVocabulariesRequest.from_dict(body)
    return web.Response(status=200)


async def list_vocabulary_filters(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_vocabulary_filters

    &lt;p&gt;Provides a list of custom vocabulary filters that match the specified criteria. If no criteria are specified, all custom vocabularies are returned.&lt;/p&gt; &lt;p&gt;To get detailed information about a specific custom vocabulary filter, use the operation.&lt;/p&gt;

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
    body = ListVocabularyFiltersRequest.from_dict(body)
    return web.Response(status=200)


async def start_call_analytics_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_call_analytics_job

    &lt;p&gt;Transcribes the audio from a customer service call and applies any additional Request Parameters you choose to include in your request.&lt;/p&gt; &lt;p&gt;In addition to many standard transcription features, Call Analytics provides you with call characteristics, call summarization, speaker sentiment, and optional redaction of your text transcript and your audio file. You can also apply custom categories to flag specified conditions. To learn more about these features and insights, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/call-analytics.html\&quot;&gt;Analyzing call center audio with Call Analytics&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you want to apply categories to your Call Analytics job, you must create them before submitting your job request. Categories cannot be retroactively applied to a job. To create a new category, use the operation. To learn more about Call Analytics categories, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-batch.html\&quot;&gt;Creating categories for post-call transcriptions&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-stream.html\&quot;&gt;Creating categories for real-time transcriptions&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To make a &lt;code&gt;StartCallAnalyticsJob&lt;/code&gt; request, you must first upload your media file into an Amazon S3 bucket; you can then specify the Amazon S3 location of the file using the &lt;code&gt;Media&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;Note that job queuing is enabled by default for Call Analytics jobs.&lt;/p&gt; &lt;p&gt;You must include the following parameters in your &lt;code&gt;StartCallAnalyticsJob&lt;/code&gt; request:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;region&lt;/code&gt;: The Amazon Web Services Region where you are making your request. For a list of Amazon Web Services Regions supported with Amazon Transcribe, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/transcribe.html\&quot;&gt;Amazon Transcribe endpoints and quotas&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CallAnalyticsJobName&lt;/code&gt;: A custom name that you create for your transcription job that&#39;s unique within your Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DataAccessRoleArn&lt;/code&gt;: The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Media&lt;/code&gt; (&lt;code&gt;MediaFileUri&lt;/code&gt; or &lt;code&gt;RedactedMediaFileUri&lt;/code&gt;): The Amazon S3 location of your media file.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;With Call Analytics, you can redact the audio contained in your media file by including &lt;code&gt;RedactedMediaFileUri&lt;/code&gt;, instead of &lt;code&gt;MediaFileUri&lt;/code&gt;, to specify the location of your input audio. If you choose to redact your audio, you can find your redacted media at the location specified in the &lt;code&gt;RedactedMediaFileUri&lt;/code&gt; field of your response.&lt;/p&gt; &lt;/note&gt;

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
    body = StartCallAnalyticsJobRequest.from_dict(body)
    return web.Response(status=200)


async def start_medical_transcription_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_medical_transcription_job

    &lt;p&gt;Transcribes the audio from a medical dictation or conversation and applies any additional Request Parameters you choose to include in your request.&lt;/p&gt; &lt;p&gt;In addition to many standard transcription features, Amazon Transcribe Medical provides you with a robust medical vocabulary and, optionally, content identification, which adds flags to personal health information (PHI). To learn more about these features, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works-med.html\&quot;&gt;How Amazon Transcribe Medical works&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To make a &lt;code&gt;StartMedicalTranscriptionJob&lt;/code&gt; request, you must first upload your media file into an Amazon S3 bucket; you can then specify the S3 location of the file using the &lt;code&gt;Media&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;You must include the following parameters in your &lt;code&gt;StartMedicalTranscriptionJob&lt;/code&gt; request:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;region&lt;/code&gt;: The Amazon Web Services Region where you are making your request. For a list of Amazon Web Services Regions supported with Amazon Transcribe, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/transcribe.html\&quot;&gt;Amazon Transcribe endpoints and quotas&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;MedicalTranscriptionJobName&lt;/code&gt;: A custom name you create for your transcription job that is unique within your Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Media&lt;/code&gt; (&lt;code&gt;MediaFileUri&lt;/code&gt;): The Amazon S3 location of your media file.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LanguageCode&lt;/code&gt;: This must be &lt;code&gt;en-US&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;OutputBucketName&lt;/code&gt;: The Amazon S3 bucket where you want your transcript stored. If you want your output stored in a sub-folder of this bucket, you must also include &lt;code&gt;OutputKey&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Specialty&lt;/code&gt;: This must be &lt;code&gt;PRIMARYCARE&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Type&lt;/code&gt;: Choose whether your audio is a conversation or a dictation.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = StartMedicalTranscriptionJobRequest.from_dict(body)
    return web.Response(status=200)


async def start_transcription_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_transcription_job

    &lt;p&gt;Transcribes the audio from a media file and applies any additional Request Parameters you choose to include in your request.&lt;/p&gt; &lt;p&gt;To make a &lt;code&gt;StartTranscriptionJob&lt;/code&gt; request, you must first upload your media file into an Amazon S3 bucket; you can then specify the Amazon S3 location of the file using the &lt;code&gt;Media&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;You must include the following parameters in your &lt;code&gt;StartTranscriptionJob&lt;/code&gt; request:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;region&lt;/code&gt;: The Amazon Web Services Region where you are making your request. For a list of Amazon Web Services Regions supported with Amazon Transcribe, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/transcribe.html\&quot;&gt;Amazon Transcribe endpoints and quotas&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TranscriptionJobName&lt;/code&gt;: A custom name you create for your transcription job that is unique within your Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Media&lt;/code&gt; (&lt;code&gt;MediaFileUri&lt;/code&gt;): The Amazon S3 location of your media file.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;One of &lt;code&gt;LanguageCode&lt;/code&gt;, &lt;code&gt;IdentifyLanguage&lt;/code&gt;, or &lt;code&gt;IdentifyMultipleLanguages&lt;/code&gt;: If you know the language of your media file, specify it using the &lt;code&gt;LanguageCode&lt;/code&gt; parameter; you can find all valid language codes in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html\&quot;&gt;Supported languages&lt;/a&gt; table. If you don&#39;t know the languages spoken in your media, use either &lt;code&gt;IdentifyLanguage&lt;/code&gt; or &lt;code&gt;IdentifyMultipleLanguages&lt;/code&gt; and let Amazon Transcribe identify the languages for you.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = StartTranscriptionJobRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Adds one or more custom tags, each in the form of a key:value pair, to the specified resource.&lt;/p&gt; &lt;p&gt;To learn more about using tags with Amazon Transcribe, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html\&quot;&gt;Tagging resources&lt;/a&gt;.&lt;/p&gt;

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

    &lt;p&gt;Removes the specified tags from the specified Amazon Transcribe resource.&lt;/p&gt; &lt;p&gt;If you include &lt;code&gt;UntagResource&lt;/code&gt; in your request, you must also include &lt;code&gt;ResourceArn&lt;/code&gt; and &lt;code&gt;TagKeys&lt;/code&gt;.&lt;/p&gt;

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


async def update_call_analytics_category(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_call_analytics_category

    &lt;p&gt;Updates the specified Call Analytics category with new rules. Note that the &lt;code&gt;UpdateCallAnalyticsCategory&lt;/code&gt; operation overwrites all existing rules contained in the specified category. You cannot append additional rules onto an existing category.&lt;/p&gt; &lt;p&gt;To create a new category, see .&lt;/p&gt;

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
    body = UpdateCallAnalyticsCategoryRequest.from_dict(body)
    return web.Response(status=200)


async def update_medical_vocabulary(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_medical_vocabulary

    Updates an existing custom medical vocabulary with new values. This operation overwrites all existing information with your new values; you cannot append new terms onto an existing custom vocabulary.

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
    body = UpdateMedicalVocabularyRequest.from_dict(body)
    return web.Response(status=200)


async def update_vocabulary(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_vocabulary

    Updates an existing custom vocabulary with new values. This operation overwrites all existing information with your new values; you cannot append new terms onto an existing custom vocabulary.

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
    body = UpdateVocabularyRequest.from_dict(body)
    return web.Response(status=200)


async def update_vocabulary_filter(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_vocabulary_filter

    Updates an existing custom vocabulary filter with a new list of words. The new list you provide overwrites all previous entries; you cannot append new terms onto an existing custom vocabulary filter.

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
    body = UpdateVocabularyFilterRequest.from_dict(body)
    return web.Response(status=200)
