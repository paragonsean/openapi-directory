from typing import List, Dict
from aiohttp import web

from openapi_server.models.describe_voices_output import DescribeVoicesOutput
from openapi_server.models.get_lexicon_output import GetLexiconOutput
from openapi_server.models.get_speech_synthesis_task_output import GetSpeechSynthesisTaskOutput
from openapi_server.models.list_lexicons_output import ListLexiconsOutput
from openapi_server.models.list_speech_synthesis_tasks_output import ListSpeechSynthesisTasksOutput
from openapi_server.models.put_lexicon_request import PutLexiconRequest
from openapi_server.models.start_speech_synthesis_task_output import StartSpeechSynthesisTaskOutput
from openapi_server.models.start_speech_synthesis_task_request import StartSpeechSynthesisTaskRequest
from openapi_server.models.synthesize_speech_output import SynthesizeSpeechOutput
from openapi_server.models.synthesize_speech_request import SynthesizeSpeechRequest
from openapi_server import util


async def delete_lexicon(request: web.Request, lexicon_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_lexicon

    &lt;p&gt;Deletes the specified pronunciation lexicon stored in an Amazon Web Services Region. A lexicon which has been deleted is not available for speech synthesis, nor is it possible to retrieve it using either the &lt;code&gt;GetLexicon&lt;/code&gt; or &lt;code&gt;ListLexicon&lt;/code&gt; APIs.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html\&quot;&gt;Managing Lexicons&lt;/a&gt;.&lt;/p&gt;

    :param lexicon_name: The name of the lexicon to delete. Must be an existing lexicon in the region.
    :type lexicon_name: str
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


async def describe_voices(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, engine=None, language_code=None, include_additional_language_codes=None, next_token=None) -> web.Response:
    """describe_voices

    &lt;p&gt;Returns the list of voices that are available for use when requesting speech synthesis. Each voice speaks a specified language, is either male or female, and is identified by an ID, which is the ASCII version of the voice name. &lt;/p&gt; &lt;p&gt;When synthesizing speech ( &lt;code&gt;SynthesizeSpeech&lt;/code&gt; ), you provide the voice ID for the voice you want from the list of voices returned by &lt;code&gt;DescribeVoices&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For example, you want your news reader application to read news in a specific language, but giving a user the option to choose the voice. Using the &lt;code&gt;DescribeVoices&lt;/code&gt; operation you can provide the user with a list of available voices to select from.&lt;/p&gt; &lt;p&gt; You can optionally specify a language code to filter the available voices. For example, if you specify &lt;code&gt;en-US&lt;/code&gt;, the operation returns a list of all available US English voices. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;polly:DescribeVoices&lt;/code&gt; action.&lt;/p&gt;

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
    :param engine: Specifies the engine (&lt;code&gt;standard&lt;/code&gt; or &lt;code&gt;neural&lt;/code&gt;) used by Amazon Polly when processing input text for speech synthesis. 
    :type engine: str
    :param language_code:  The language identification tag (ISO 639 code for the language name-ISO 3166 country code) for filtering the list of voices returned. If you don&#39;t specify this optional parameter, all available voices are returned. 
    :type language_code: str
    :param include_additional_language_codes: Boolean value indicating whether to return any bilingual voices that use the specified language as an additional language. For instance, if you request all languages that use US English (es-US), and there is an Italian voice that speaks both Italian (it-IT) and US English, that voice will be included if you specify &lt;code&gt;yes&lt;/code&gt; but not if you specify &lt;code&gt;no&lt;/code&gt;.
    :type include_additional_language_codes: bool
    :param next_token: An opaque pagination token returned from the previous &lt;code&gt;DescribeVoices&lt;/code&gt; operation. If present, this indicates where to continue the listing.
    :type next_token: str

    """
    return web.Response(status=200)


async def get_lexicon(request: web.Request, lexicon_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_lexicon

    Returns the content of the specified pronunciation lexicon stored in an Amazon Web Services Region. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html\&quot;&gt;Managing Lexicons&lt;/a&gt;.

    :param lexicon_name: Name of the lexicon.
    :type lexicon_name: str
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


async def get_speech_synthesis_task(request: web.Request, task_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_speech_synthesis_task

    Retrieves a specific SpeechSynthesisTask object based on its TaskID. This object contains information about the given speech synthesis task, including the status of the task, and a link to the S3 bucket containing the output of the task.

    :param task_id: The Amazon Polly generated identifier for a speech synthesis task.
    :type task_id: str
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


async def list_lexicons(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_lexicons

    Returns a list of pronunciation lexicons stored in an Amazon Web Services Region. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html\&quot;&gt;Managing Lexicons&lt;/a&gt;.

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
    :param next_token: An opaque pagination token returned from previous &lt;code&gt;ListLexicons&lt;/code&gt; operation. If present, indicates where to continue the list of lexicons.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_speech_synthesis_tasks(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, status=None) -> web.Response:
    """list_speech_synthesis_tasks

    Returns a list of SpeechSynthesisTask objects ordered by their creation date. This operation can filter the tasks by their status, for example, allowing users to list only tasks that are completed.

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
    :param max_results: Maximum number of speech synthesis tasks returned in a List operation.
    :type max_results: int
    :param next_token: The pagination token to use in the next request to continue the listing of speech synthesis tasks. 
    :type next_token: str
    :param status: Status of the speech synthesis tasks returned in a List operation
    :type status: str

    """
    return web.Response(status=200)


async def put_lexicon(request: web.Request, lexicon_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_lexicon

    &lt;p&gt;Stores a pronunciation lexicon in an Amazon Web Services Region. If a lexicon with the same name already exists in the region, it is overwritten by the new lexicon. Lexicon operations have eventual consistency, therefore, it might take some time before the lexicon is available to the SynthesizeSpeech operation.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html\&quot;&gt;Managing Lexicons&lt;/a&gt;.&lt;/p&gt;

    :param lexicon_name: Name of the lexicon. The name must follow the regular express format [0-9A-Za-z]{1,20}. That is, the name is a case-sensitive alphanumeric string up to 20 characters long. 
    :type lexicon_name: str
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
    body = PutLexiconRequest.from_dict(body)
    return web.Response(status=200)


async def start_speech_synthesis_task(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_speech_synthesis_task

    Allows the creation of an asynchronous synthesis task, by starting a new &lt;code&gt;SpeechSynthesisTask&lt;/code&gt;. This operation requires all the standard information needed for speech synthesis, plus the name of an Amazon S3 bucket for the service to store the output of the synthesis task and two optional parameters (&lt;code&gt;OutputS3KeyPrefix&lt;/code&gt; and &lt;code&gt;SnsTopicArn&lt;/code&gt;). Once the synthesis task is created, this operation will return a &lt;code&gt;SpeechSynthesisTask&lt;/code&gt; object, which will include an identifier of this task as well as the current status. The &lt;code&gt;SpeechSynthesisTask&lt;/code&gt; object is available for 72 hours after starting the asynchronous synthesis task.

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
    body = StartSpeechSynthesisTaskRequest.from_dict(body)
    return web.Response(status=200)


async def synthesize_speech(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """synthesize_speech

    Synthesizes UTF-8 input, plain text or SSML, to a stream of bytes. SSML input must be valid, well-formed SSML. Some alphabets might not be available with all the voices (for example, Cyrillic might not be read at all by English voices) unless phoneme mapping is used. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/polly/latest/dg/how-text-to-speech-works.html\&quot;&gt;How it Works&lt;/a&gt;.

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
    body = SynthesizeSpeechRequest.from_dict(body)
    return web.Response(status=200)
