from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_session_response import GetSessionResponse
from openapi_server.models.post_content_request import PostContentRequest
from openapi_server.models.post_content_response import PostContentResponse
from openapi_server.models.post_text_request import PostTextRequest
from openapi_server.models.post_text_response import PostTextResponse
from openapi_server import util


async def get_session(request: web.Request, bot_name, bot_alias, user_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, checkpoint_label_filter=None) -> web.Response:
    """get_session

    Returns session information for a specified bot, alias, and user ID.

    :param bot_name: The name of the bot that contains the session data.
    :type bot_name: str
    :param bot_alias: The alias in use for the bot that contains the session data.
    :type bot_alias: str
    :param user_id: The ID of the client application user. Amazon Lex uses this to identify a user&#39;s conversation with your bot. 
    :type user_id: str
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
    :param checkpoint_label_filter: &lt;p&gt;A string used to filter the intents returned in the &lt;code&gt;recentIntentSummaryView&lt;/code&gt; structure. &lt;/p&gt; &lt;p&gt;When you specify a filter, only intents with their &lt;code&gt;checkpointLabel&lt;/code&gt; field set to that string are returned.&lt;/p&gt;
    :type checkpoint_label_filter: str

    """
    return web.Response(status=200)


async def post_content(request: web.Request, bot_name, bot_alias, user_id, content_type, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_lex_session_attributes=None, x_amz_lex_request_attributes=None, accept=None, x_amz_lex_active_contexts=None) -> web.Response:
    """post_content

    &lt;p&gt; Sends user input (text or speech) to Amazon Lex. Clients use this API to send text and audio requests to Amazon Lex at runtime. Amazon Lex interprets the user input using the machine learning model that it built for the bot. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;PostContent&lt;/code&gt; operation supports audio input at 8kHz and 16kHz. You can use 8kHz audio to achieve higher speech recognition accuracy in telephone audio applications. &lt;/p&gt; &lt;p&gt; In response, Amazon Lex returns the next message to convey to the user. Consider the following example messages: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; For a user input \&quot;I would like a pizza,\&quot; Amazon Lex might return a response with a message eliciting slot data (for example, &lt;code&gt;PizzaSize&lt;/code&gt;): \&quot;What size pizza would you like?\&quot;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; After the user provides all of the pizza order information, Amazon Lex might return a response with a message to get user confirmation: \&quot;Order the pizza?\&quot;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; After the user replies \&quot;Yes\&quot; to the confirmation prompt, Amazon Lex might return a conclusion statement: \&quot;Thank you, your cheese pizza has been ordered.\&quot;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; Not all Amazon Lex messages require a response from the user. For example, conclusion statements do not require a response. Some messages require only a yes or no response. In addition to the &lt;code&gt;message&lt;/code&gt;, Amazon Lex provides additional context about the message in the response that you can use to enhance client behavior, such as displaying the appropriate client user interface. Consider the following examples: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; If the message is to elicit slot data, Amazon Lex returns the following context information: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;x-amz-lex-dialog-state&lt;/code&gt; header set to &lt;code&gt;ElicitSlot&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;x-amz-lex-intent-name&lt;/code&gt; header set to the intent name in the current context &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;x-amz-lex-slot-to-elicit&lt;/code&gt; header set to the slot name for which the &lt;code&gt;message&lt;/code&gt; is eliciting information &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;x-amz-lex-slots&lt;/code&gt; header set to a map of slots configured for the intent with their current values &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; If the message is a confirmation prompt, the &lt;code&gt;x-amz-lex-dialog-state&lt;/code&gt; header is set to &lt;code&gt;Confirmation&lt;/code&gt; and the &lt;code&gt;x-amz-lex-slot-to-elicit&lt;/code&gt; header is omitted. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; If the message is a clarification prompt configured for the intent, indicating that the user intent is not understood, the &lt;code&gt;x-amz-dialog-state&lt;/code&gt; header is set to &lt;code&gt;ElicitIntent&lt;/code&gt; and the &lt;code&gt;x-amz-slot-to-elicit&lt;/code&gt; header is omitted. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; In addition, Amazon Lex also returns your application-specific &lt;code&gt;sessionAttributes&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html\&quot;&gt;Managing Conversation Context&lt;/a&gt;. &lt;/p&gt;

    :param bot_name: Name of the Amazon Lex bot.
    :type bot_name: str
    :param bot_alias: Alias of the Amazon Lex bot.
    :type bot_alias: str
    :param user_id: &lt;p&gt;The ID of the client application user. Amazon Lex uses this to identify a user&#39;s conversation with your bot. At runtime, each request must contain the &lt;code&gt;userID&lt;/code&gt; field.&lt;/p&gt; &lt;p&gt;To decide the user ID to use for your application, consider the following factors.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;userID&lt;/code&gt; field must not contain any personally identifiable information of the user, for example, name, personal identification numbers, or other end user personal information.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you want a user to start a conversation on one device and continue on another device, use a user-specific identifier.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you want the same user to be able to have two independent conversations on two different devices, choose a device-specific identifier.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A user can&#39;t have two independent conversations with two different versions of the same bot. For example, a user can&#39;t have a conversation with the PROD and BETA versions of the same bot. If you anticipate that a user will need to have conversation with two different versions, for example, while testing, include the bot alias in the user ID to separate the two conversations.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type user_id: str
    :param content_type: &lt;p&gt; You pass this value as the &lt;code&gt;Content-Type&lt;/code&gt; HTTP header. &lt;/p&gt; &lt;p&gt; Indicates the audio format or text. The header value must start with one of the following prefixes: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;PCM format, audio data must be in little-endian byte order.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;audio/l16; rate&#x3D;16000; channels&#x3D;1&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;audio/x-l16; sample-rate&#x3D;16000; channel-count&#x3D;1&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;audio/lpcm; sample-rate&#x3D;8000; sample-size-bits&#x3D;16; channel-count&#x3D;1; is-big-endian&#x3D;false &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Opus format&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;audio/x-cbr-opus-with-preamble; preamble-size&#x3D;0; bit-rate&#x3D;256000; frame-size-milliseconds&#x3D;4&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Text format&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;text/plain; charset&#x3D;utf-8&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt;
    :type content_type: str
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
    :param x_amz_lex_session_attributes: &lt;p&gt;You pass this value as the &lt;code&gt;x-amz-lex-session-attributes&lt;/code&gt; HTTP header.&lt;/p&gt; &lt;p&gt;Application-specific information passed between Amazon Lex and a client application. The value must be a JSON serialized and base64 encoded map with string keys and values. The total size of the &lt;code&gt;sessionAttributes&lt;/code&gt; and &lt;code&gt;requestAttributes&lt;/code&gt; headers is limited to 12 KB.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-session-attribs\&quot;&gt;Setting Session Attributes&lt;/a&gt;.&lt;/p&gt;
    :type x_amz_lex_session_attributes: str
    :param x_amz_lex_request_attributes: &lt;p&gt;You pass this value as the &lt;code&gt;x-amz-lex-request-attributes&lt;/code&gt; HTTP header.&lt;/p&gt; &lt;p&gt;Request-specific information passed between Amazon Lex and a client application. The value must be a JSON serialized and base64 encoded map with string keys and values. The total size of the &lt;code&gt;requestAttributes&lt;/code&gt; and &lt;code&gt;sessionAttributes&lt;/code&gt; headers is limited to 12 KB.&lt;/p&gt; &lt;p&gt;The namespace &lt;code&gt;x-amz-lex:&lt;/code&gt; is reserved for special attributes. Don&#39;t create any request attributes with the prefix &lt;code&gt;x-amz-lex:&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-request-attribs\&quot;&gt;Setting Request Attributes&lt;/a&gt;.&lt;/p&gt;
    :type x_amz_lex_request_attributes: str
    :param accept: &lt;p&gt; You pass this value as the &lt;code&gt;Accept&lt;/code&gt; HTTP header. &lt;/p&gt; &lt;p&gt; The message Amazon Lex returns in the response can be either text or speech based on the &lt;code&gt;Accept&lt;/code&gt; HTTP header value in the request. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; If the value is &lt;code&gt;text/plain; charset&#x3D;utf-8&lt;/code&gt;, Amazon Lex returns text in the response. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; If the value begins with &lt;code&gt;audio/&lt;/code&gt;, Amazon Lex returns speech in the response. Amazon Lex uses Amazon Polly to generate the speech (using the configuration you specified in the &lt;code&gt;Accept&lt;/code&gt; header). For example, if you specify &lt;code&gt;audio/mpeg&lt;/code&gt; as the value, Amazon Lex returns speech in the MPEG format.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the value is &lt;code&gt;audio/pcm&lt;/code&gt;, the speech returned is &lt;code&gt;audio/pcm&lt;/code&gt; in 16-bit, little endian format. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following are the accepted values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;audio/mpeg&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;audio/ogg&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;audio/pcm&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;text/plain; charset&#x3D;utf-8&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;audio/* (defaults to mpeg)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt;
    :type accept: str
    :param x_amz_lex_active_contexts: &lt;p&gt;A list of contexts active for the request. A context can be activated when a previous intent is fulfilled, or by including the context in the request,&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a list of contexts, Amazon Lex will use the current list of contexts for the session. If you specify an empty list, all contexts for the session are cleared.&lt;/p&gt;
    :type x_amz_lex_active_contexts: str

    """
    body = PostContentRequest.from_dict(body)
    return web.Response(status=200)


async def post_text(request: web.Request, bot_name, bot_alias, user_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """post_text

    &lt;p&gt;Sends user input to Amazon Lex. Client applications can use this API to send requests to Amazon Lex at runtime. Amazon Lex then interprets the user input using the machine learning model it built for the bot. &lt;/p&gt; &lt;p&gt; In response, Amazon Lex returns the next &lt;code&gt;message&lt;/code&gt; to convey to the user an optional &lt;code&gt;responseCard&lt;/code&gt; to display. Consider the following example messages: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; For a user input \&quot;I would like a pizza\&quot;, Amazon Lex might return a response with a message eliciting slot data (for example, PizzaSize): \&quot;What size pizza would you like?\&quot; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; After the user provides all of the pizza order information, Amazon Lex might return a response with a message to obtain user confirmation \&quot;Proceed with the pizza order?\&quot;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; After the user replies to a confirmation prompt with a \&quot;yes\&quot;, Amazon Lex might return a conclusion statement: \&quot;Thank you, your cheese pizza has been ordered.\&quot;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; Not all Amazon Lex messages require a user response. For example, a conclusion statement does not require a response. Some messages require only a \&quot;yes\&quot; or \&quot;no\&quot; user response. In addition to the &lt;code&gt;message&lt;/code&gt;, Amazon Lex provides additional context about the message in the response that you might use to enhance client behavior, for example, to display the appropriate client user interface. These are the &lt;code&gt;slotToElicit&lt;/code&gt;, &lt;code&gt;dialogState&lt;/code&gt;, &lt;code&gt;intentName&lt;/code&gt;, and &lt;code&gt;slots&lt;/code&gt; fields in the response. Consider the following examples: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the message is to elicit slot data, Amazon Lex returns the following context information:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;dialogState&lt;/code&gt; set to ElicitSlot &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;intentName&lt;/code&gt; set to the intent name in the current context &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;slotToElicit&lt;/code&gt; set to the slot name for which the &lt;code&gt;message&lt;/code&gt; is eliciting information &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;slots&lt;/code&gt; set to a map of slots, configured for the intent, with currently known values &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; If the message is a confirmation prompt, the &lt;code&gt;dialogState&lt;/code&gt; is set to ConfirmIntent and &lt;code&gt;SlotToElicit&lt;/code&gt; is set to null. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the message is a clarification prompt (configured for the intent) that indicates that user intent is not understood, the &lt;code&gt;dialogState&lt;/code&gt; is set to ElicitIntent and &lt;code&gt;slotToElicit&lt;/code&gt; is set to null. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; In addition, Amazon Lex also returns your application-specific &lt;code&gt;sessionAttributes&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html\&quot;&gt;Managing Conversation Context&lt;/a&gt;. &lt;/p&gt;

    :param bot_name: The name of the Amazon Lex bot.
    :type bot_name: str
    :param bot_alias: The alias of the Amazon Lex bot.
    :type bot_alias: str
    :param user_id: &lt;p&gt;The ID of the client application user. Amazon Lex uses this to identify a user&#39;s conversation with your bot. At runtime, each request must contain the &lt;code&gt;userID&lt;/code&gt; field.&lt;/p&gt; &lt;p&gt;To decide the user ID to use for your application, consider the following factors.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;userID&lt;/code&gt; field must not contain any personally identifiable information of the user, for example, name, personal identification numbers, or other end user personal information.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you want a user to start a conversation on one device and continue on another device, use a user-specific identifier.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you want the same user to be able to have two independent conversations on two different devices, choose a device-specific identifier.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A user can&#39;t have two independent conversations with two different versions of the same bot. For example, a user can&#39;t have a conversation with the PROD and BETA versions of the same bot. If you anticipate that a user will need to have conversation with two different versions, for example, while testing, include the bot alias in the user ID to separate the two conversations.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type user_id: str
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
    body = PostTextRequest.from_dict(body)
    return web.Response(status=200)
