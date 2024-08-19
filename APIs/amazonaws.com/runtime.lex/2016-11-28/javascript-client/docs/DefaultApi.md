# AmazonLexRuntimeService.DefaultApi

All URIs are relative to *http://runtime.lex.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteSession**](DefaultApi.md#deleteSession) | **DELETE** /bot/{botName}/alias/{botAlias}/user/{userId}/session | 
[**getSession**](DefaultApi.md#getSession) | **GET** /bot/{botName}/alias/{botAlias}/user/{userId}/session/ | 
[**postContent**](DefaultApi.md#postContent) | **POST** /bot/{botName}/alias/{botAlias}/user/{userId}/content#Content-Type | 
[**postText**](DefaultApi.md#postText) | **POST** /bot/{botName}/alias/{botAlias}/user/{userId}/text | 
[**putSession**](DefaultApi.md#putSession) | **POST** /bot/{botName}/alias/{botAlias}/user/{userId}/session | 



## deleteSession

> DeleteSessionResponse deleteSession(botName, botAlias, userId, opts)



Removes session information for a specified bot, alias, and user ID. 

### Example

```javascript
import AmazonLexRuntimeService from 'amazon_lex_runtime_service';
let defaultClient = AmazonLexRuntimeService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexRuntimeService.DefaultApi();
let botName = "botName_example"; // String | The name of the bot that contains the session data.
let botAlias = "botAlias_example"; // String | The alias in use for the bot that contains the session data.
let userId = "userId_example"; // String | The identifier of the user associated with the session data.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSession(botName, botAlias, userId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **botName** | **String**| The name of the bot that contains the session data. | 
 **botAlias** | **String**| The alias in use for the bot that contains the session data. | 
 **userId** | **String**| The identifier of the user associated with the session data. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteSessionResponse**](DeleteSessionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSession

> GetSessionResponse getSession(botName, botAlias, userId, opts)



Returns session information for a specified bot, alias, and user ID.

### Example

```javascript
import AmazonLexRuntimeService from 'amazon_lex_runtime_service';
let defaultClient = AmazonLexRuntimeService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexRuntimeService.DefaultApi();
let botName = "botName_example"; // String | The name of the bot that contains the session data.
let botAlias = "botAlias_example"; // String | The alias in use for the bot that contains the session data.
let userId = "userId_example"; // String | The ID of the client application user. Amazon Lex uses this to identify a user's conversation with your bot. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'checkpointLabelFilter': "checkpointLabelFilter_example" // String | <p>A string used to filter the intents returned in the <code>recentIntentSummaryView</code> structure. </p> <p>When you specify a filter, only intents with their <code>checkpointLabel</code> field set to that string are returned.</p>
};
apiInstance.getSession(botName, botAlias, userId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **botName** | **String**| The name of the bot that contains the session data. | 
 **botAlias** | **String**| The alias in use for the bot that contains the session data. | 
 **userId** | **String**| The ID of the client application user. Amazon Lex uses this to identify a user&#39;s conversation with your bot.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **checkpointLabelFilter** | **String**| &lt;p&gt;A string used to filter the intents returned in the &lt;code&gt;recentIntentSummaryView&lt;/code&gt; structure. &lt;/p&gt; &lt;p&gt;When you specify a filter, only intents with their &lt;code&gt;checkpointLabel&lt;/code&gt; field set to that string are returned.&lt;/p&gt; | [optional] 

### Return type

[**GetSessionResponse**](GetSessionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postContent

> PostContentResponse postContent(botName, botAlias, userId, contentType, postContentRequest, opts)



&lt;p&gt; Sends user input (text or speech) to Amazon Lex. Clients use this API to send text and audio requests to Amazon Lex at runtime. Amazon Lex interprets the user input using the machine learning model that it built for the bot. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;PostContent&lt;/code&gt; operation supports audio input at 8kHz and 16kHz. You can use 8kHz audio to achieve higher speech recognition accuracy in telephone audio applications. &lt;/p&gt; &lt;p&gt; In response, Amazon Lex returns the next message to convey to the user. Consider the following example messages: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; For a user input \&quot;I would like a pizza,\&quot; Amazon Lex might return a response with a message eliciting slot data (for example, &lt;code&gt;PizzaSize&lt;/code&gt;): \&quot;What size pizza would you like?\&quot;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; After the user provides all of the pizza order information, Amazon Lex might return a response with a message to get user confirmation: \&quot;Order the pizza?\&quot;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; After the user replies \&quot;Yes\&quot; to the confirmation prompt, Amazon Lex might return a conclusion statement: \&quot;Thank you, your cheese pizza has been ordered.\&quot;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; Not all Amazon Lex messages require a response from the user. For example, conclusion statements do not require a response. Some messages require only a yes or no response. In addition to the &lt;code&gt;message&lt;/code&gt;, Amazon Lex provides additional context about the message in the response that you can use to enhance client behavior, such as displaying the appropriate client user interface. Consider the following examples: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; If the message is to elicit slot data, Amazon Lex returns the following context information: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;x-amz-lex-dialog-state&lt;/code&gt; header set to &lt;code&gt;ElicitSlot&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;x-amz-lex-intent-name&lt;/code&gt; header set to the intent name in the current context &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;x-amz-lex-slot-to-elicit&lt;/code&gt; header set to the slot name for which the &lt;code&gt;message&lt;/code&gt; is eliciting information &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;x-amz-lex-slots&lt;/code&gt; header set to a map of slots configured for the intent with their current values &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; If the message is a confirmation prompt, the &lt;code&gt;x-amz-lex-dialog-state&lt;/code&gt; header is set to &lt;code&gt;Confirmation&lt;/code&gt; and the &lt;code&gt;x-amz-lex-slot-to-elicit&lt;/code&gt; header is omitted. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; If the message is a clarification prompt configured for the intent, indicating that the user intent is not understood, the &lt;code&gt;x-amz-dialog-state&lt;/code&gt; header is set to &lt;code&gt;ElicitIntent&lt;/code&gt; and the &lt;code&gt;x-amz-slot-to-elicit&lt;/code&gt; header is omitted. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; In addition, Amazon Lex also returns your application-specific &lt;code&gt;sessionAttributes&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html\&quot;&gt;Managing Conversation Context&lt;/a&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonLexRuntimeService from 'amazon_lex_runtime_service';
let defaultClient = AmazonLexRuntimeService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexRuntimeService.DefaultApi();
let botName = "botName_example"; // String | Name of the Amazon Lex bot.
let botAlias = "botAlias_example"; // String | Alias of the Amazon Lex bot.
let userId = "userId_example"; // String | <p>The ID of the client application user. Amazon Lex uses this to identify a user's conversation with your bot. At runtime, each request must contain the <code>userID</code> field.</p> <p>To decide the user ID to use for your application, consider the following factors.</p> <ul> <li> <p>The <code>userID</code> field must not contain any personally identifiable information of the user, for example, name, personal identification numbers, or other end user personal information.</p> </li> <li> <p>If you want a user to start a conversation on one device and continue on another device, use a user-specific identifier.</p> </li> <li> <p>If you want the same user to be able to have two independent conversations on two different devices, choose a device-specific identifier.</p> </li> <li> <p>A user can't have two independent conversations with two different versions of the same bot. For example, a user can't have a conversation with the PROD and BETA versions of the same bot. If you anticipate that a user will need to have conversation with two different versions, for example, while testing, include the bot alias in the user ID to separate the two conversations.</p> </li> </ul>
let contentType = "contentType_example"; // String | <p> You pass this value as the <code>Content-Type</code> HTTP header. </p> <p> Indicates the audio format or text. The header value must start with one of the following prefixes: </p> <ul> <li> <p>PCM format, audio data must be in little-endian byte order.</p> <ul> <li> <p>audio/l16; rate=16000; channels=1</p> </li> <li> <p>audio/x-l16; sample-rate=16000; channel-count=1</p> </li> <li> <p>audio/lpcm; sample-rate=8000; sample-size-bits=16; channel-count=1; is-big-endian=false </p> </li> </ul> </li> <li> <p>Opus format</p> <ul> <li> <p>audio/x-cbr-opus-with-preamble; preamble-size=0; bit-rate=256000; frame-size-milliseconds=4</p> </li> </ul> </li> <li> <p>Text format</p> <ul> <li> <p>text/plain; charset=utf-8</p> </li> </ul> </li> </ul>
let postContentRequest = new AmazonLexRuntimeService.PostContentRequest(); // PostContentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzLexSessionAttributes': "xAmzLexSessionAttributes_example", // String | <p>You pass this value as the <code>x-amz-lex-session-attributes</code> HTTP header.</p> <p>Application-specific information passed between Amazon Lex and a client application. The value must be a JSON serialized and base64 encoded map with string keys and values. The total size of the <code>sessionAttributes</code> and <code>requestAttributes</code> headers is limited to 12 KB.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-session-attribs\">Setting Session Attributes</a>.</p>
  'xAmzLexRequestAttributes': "xAmzLexRequestAttributes_example", // String | <p>You pass this value as the <code>x-amz-lex-request-attributes</code> HTTP header.</p> <p>Request-specific information passed between Amazon Lex and a client application. The value must be a JSON serialized and base64 encoded map with string keys and values. The total size of the <code>requestAttributes</code> and <code>sessionAttributes</code> headers is limited to 12 KB.</p> <p>The namespace <code>x-amz-lex:</code> is reserved for special attributes. Don't create any request attributes with the prefix <code>x-amz-lex:</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-request-attribs\">Setting Request Attributes</a>.</p>
  'accept': "accept_example", // String | <p> You pass this value as the <code>Accept</code> HTTP header. </p> <p> The message Amazon Lex returns in the response can be either text or speech based on the <code>Accept</code> HTTP header value in the request. </p> <ul> <li> <p> If the value is <code>text/plain; charset=utf-8</code>, Amazon Lex returns text in the response. </p> </li> <li> <p> If the value begins with <code>audio/</code>, Amazon Lex returns speech in the response. Amazon Lex uses Amazon Polly to generate the speech (using the configuration you specified in the <code>Accept</code> header). For example, if you specify <code>audio/mpeg</code> as the value, Amazon Lex returns speech in the MPEG format.</p> </li> <li> <p>If the value is <code>audio/pcm</code>, the speech returned is <code>audio/pcm</code> in 16-bit, little endian format. </p> </li> <li> <p>The following are the accepted values:</p> <ul> <li> <p>audio/mpeg</p> </li> <li> <p>audio/ogg</p> </li> <li> <p>audio/pcm</p> </li> <li> <p>text/plain; charset=utf-8</p> </li> <li> <p>audio/_* (defaults to mpeg)</p> </li> </ul> </li> </ul>
  'xAmzLexActiveContexts': "xAmzLexActiveContexts_example" // String | <p>A list of contexts active for the request. A context can be activated when a previous intent is fulfilled, or by including the context in the request,</p> <p>If you don't specify a list of contexts, Amazon Lex will use the current list of contexts for the session. If you specify an empty list, all contexts for the session are cleared.</p>
};
apiInstance.postContent(botName, botAlias, userId, contentType, postContentRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **botName** | **String**| Name of the Amazon Lex bot. | 
 **botAlias** | **String**| Alias of the Amazon Lex bot. | 
 **userId** | **String**| &lt;p&gt;The ID of the client application user. Amazon Lex uses this to identify a user&#39;s conversation with your bot. At runtime, each request must contain the &lt;code&gt;userID&lt;/code&gt; field.&lt;/p&gt; &lt;p&gt;To decide the user ID to use for your application, consider the following factors.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;userID&lt;/code&gt; field must not contain any personally identifiable information of the user, for example, name, personal identification numbers, or other end user personal information.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you want a user to start a conversation on one device and continue on another device, use a user-specific identifier.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you want the same user to be able to have two independent conversations on two different devices, choose a device-specific identifier.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A user can&#39;t have two independent conversations with two different versions of the same bot. For example, a user can&#39;t have a conversation with the PROD and BETA versions of the same bot. If you anticipate that a user will need to have conversation with two different versions, for example, while testing, include the bot alias in the user ID to separate the two conversations.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
 **contentType** | **String**| &lt;p&gt; You pass this value as the &lt;code&gt;Content-Type&lt;/code&gt; HTTP header. &lt;/p&gt; &lt;p&gt; Indicates the audio format or text. The header value must start with one of the following prefixes: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;PCM format, audio data must be in little-endian byte order.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;audio/l16; rate&#x3D;16000; channels&#x3D;1&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;audio/x-l16; sample-rate&#x3D;16000; channel-count&#x3D;1&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;audio/lpcm; sample-rate&#x3D;8000; sample-size-bits&#x3D;16; channel-count&#x3D;1; is-big-endian&#x3D;false &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Opus format&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;audio/x-cbr-opus-with-preamble; preamble-size&#x3D;0; bit-rate&#x3D;256000; frame-size-milliseconds&#x3D;4&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Text format&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;text/plain; charset&#x3D;utf-8&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; | 
 **postContentRequest** | [**PostContentRequest**](PostContentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzLexSessionAttributes** | **String**| &lt;p&gt;You pass this value as the &lt;code&gt;x-amz-lex-session-attributes&lt;/code&gt; HTTP header.&lt;/p&gt; &lt;p&gt;Application-specific information passed between Amazon Lex and a client application. The value must be a JSON serialized and base64 encoded map with string keys and values. The total size of the &lt;code&gt;sessionAttributes&lt;/code&gt; and &lt;code&gt;requestAttributes&lt;/code&gt; headers is limited to 12 KB.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-session-attribs\&quot;&gt;Setting Session Attributes&lt;/a&gt;.&lt;/p&gt; | [optional] 
 **xAmzLexRequestAttributes** | **String**| &lt;p&gt;You pass this value as the &lt;code&gt;x-amz-lex-request-attributes&lt;/code&gt; HTTP header.&lt;/p&gt; &lt;p&gt;Request-specific information passed between Amazon Lex and a client application. The value must be a JSON serialized and base64 encoded map with string keys and values. The total size of the &lt;code&gt;requestAttributes&lt;/code&gt; and &lt;code&gt;sessionAttributes&lt;/code&gt; headers is limited to 12 KB.&lt;/p&gt; &lt;p&gt;The namespace &lt;code&gt;x-amz-lex:&lt;/code&gt; is reserved for special attributes. Don&#39;t create any request attributes with the prefix &lt;code&gt;x-amz-lex:&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-request-attribs\&quot;&gt;Setting Request Attributes&lt;/a&gt;.&lt;/p&gt; | [optional] 
 **accept** | **String**| &lt;p&gt; You pass this value as the &lt;code&gt;Accept&lt;/code&gt; HTTP header. &lt;/p&gt; &lt;p&gt; The message Amazon Lex returns in the response can be either text or speech based on the &lt;code&gt;Accept&lt;/code&gt; HTTP header value in the request. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; If the value is &lt;code&gt;text/plain; charset&#x3D;utf-8&lt;/code&gt;, Amazon Lex returns text in the response. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; If the value begins with &lt;code&gt;audio/&lt;/code&gt;, Amazon Lex returns speech in the response. Amazon Lex uses Amazon Polly to generate the speech (using the configuration you specified in the &lt;code&gt;Accept&lt;/code&gt; header). For example, if you specify &lt;code&gt;audio/mpeg&lt;/code&gt; as the value, Amazon Lex returns speech in the MPEG format.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the value is &lt;code&gt;audio/pcm&lt;/code&gt;, the speech returned is &lt;code&gt;audio/pcm&lt;/code&gt; in 16-bit, little endian format. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following are the accepted values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;audio/mpeg&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;audio/ogg&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;audio/pcm&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;text/plain; charset&#x3D;utf-8&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;audio/_* (defaults to mpeg)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
 **xAmzLexActiveContexts** | **String**| &lt;p&gt;A list of contexts active for the request. A context can be activated when a previous intent is fulfilled, or by including the context in the request,&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a list of contexts, Amazon Lex will use the current list of contexts for the session. If you specify an empty list, all contexts for the session are cleared.&lt;/p&gt; | [optional] 

### Return type

[**PostContentResponse**](PostContentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postText

> PostTextResponse postText(botName, botAlias, userId, postTextRequest, opts)



&lt;p&gt;Sends user input to Amazon Lex. Client applications can use this API to send requests to Amazon Lex at runtime. Amazon Lex then interprets the user input using the machine learning model it built for the bot. &lt;/p&gt; &lt;p&gt; In response, Amazon Lex returns the next &lt;code&gt;message&lt;/code&gt; to convey to the user an optional &lt;code&gt;responseCard&lt;/code&gt; to display. Consider the following example messages: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; For a user input \&quot;I would like a pizza\&quot;, Amazon Lex might return a response with a message eliciting slot data (for example, PizzaSize): \&quot;What size pizza would you like?\&quot; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; After the user provides all of the pizza order information, Amazon Lex might return a response with a message to obtain user confirmation \&quot;Proceed with the pizza order?\&quot;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; After the user replies to a confirmation prompt with a \&quot;yes\&quot;, Amazon Lex might return a conclusion statement: \&quot;Thank you, your cheese pizza has been ordered.\&quot;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; Not all Amazon Lex messages require a user response. For example, a conclusion statement does not require a response. Some messages require only a \&quot;yes\&quot; or \&quot;no\&quot; user response. In addition to the &lt;code&gt;message&lt;/code&gt;, Amazon Lex provides additional context about the message in the response that you might use to enhance client behavior, for example, to display the appropriate client user interface. These are the &lt;code&gt;slotToElicit&lt;/code&gt;, &lt;code&gt;dialogState&lt;/code&gt;, &lt;code&gt;intentName&lt;/code&gt;, and &lt;code&gt;slots&lt;/code&gt; fields in the response. Consider the following examples: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the message is to elicit slot data, Amazon Lex returns the following context information:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;dialogState&lt;/code&gt; set to ElicitSlot &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;intentName&lt;/code&gt; set to the intent name in the current context &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;slotToElicit&lt;/code&gt; set to the slot name for which the &lt;code&gt;message&lt;/code&gt; is eliciting information &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;slots&lt;/code&gt; set to a map of slots, configured for the intent, with currently known values &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; If the message is a confirmation prompt, the &lt;code&gt;dialogState&lt;/code&gt; is set to ConfirmIntent and &lt;code&gt;SlotToElicit&lt;/code&gt; is set to null. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the message is a clarification prompt (configured for the intent) that indicates that user intent is not understood, the &lt;code&gt;dialogState&lt;/code&gt; is set to ElicitIntent and &lt;code&gt;slotToElicit&lt;/code&gt; is set to null. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; In addition, Amazon Lex also returns your application-specific &lt;code&gt;sessionAttributes&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html\&quot;&gt;Managing Conversation Context&lt;/a&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonLexRuntimeService from 'amazon_lex_runtime_service';
let defaultClient = AmazonLexRuntimeService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexRuntimeService.DefaultApi();
let botName = "botName_example"; // String | The name of the Amazon Lex bot.
let botAlias = "botAlias_example"; // String | The alias of the Amazon Lex bot.
let userId = "userId_example"; // String | <p>The ID of the client application user. Amazon Lex uses this to identify a user's conversation with your bot. At runtime, each request must contain the <code>userID</code> field.</p> <p>To decide the user ID to use for your application, consider the following factors.</p> <ul> <li> <p>The <code>userID</code> field must not contain any personally identifiable information of the user, for example, name, personal identification numbers, or other end user personal information.</p> </li> <li> <p>If you want a user to start a conversation on one device and continue on another device, use a user-specific identifier.</p> </li> <li> <p>If you want the same user to be able to have two independent conversations on two different devices, choose a device-specific identifier.</p> </li> <li> <p>A user can't have two independent conversations with two different versions of the same bot. For example, a user can't have a conversation with the PROD and BETA versions of the same bot. If you anticipate that a user will need to have conversation with two different versions, for example, while testing, include the bot alias in the user ID to separate the two conversations.</p> </li> </ul>
let postTextRequest = new AmazonLexRuntimeService.PostTextRequest(); // PostTextRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.postText(botName, botAlias, userId, postTextRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **botName** | **String**| The name of the Amazon Lex bot. | 
 **botAlias** | **String**| The alias of the Amazon Lex bot. | 
 **userId** | **String**| &lt;p&gt;The ID of the client application user. Amazon Lex uses this to identify a user&#39;s conversation with your bot. At runtime, each request must contain the &lt;code&gt;userID&lt;/code&gt; field.&lt;/p&gt; &lt;p&gt;To decide the user ID to use for your application, consider the following factors.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;userID&lt;/code&gt; field must not contain any personally identifiable information of the user, for example, name, personal identification numbers, or other end user personal information.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you want a user to start a conversation on one device and continue on another device, use a user-specific identifier.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you want the same user to be able to have two independent conversations on two different devices, choose a device-specific identifier.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A user can&#39;t have two independent conversations with two different versions of the same bot. For example, a user can&#39;t have a conversation with the PROD and BETA versions of the same bot. If you anticipate that a user will need to have conversation with two different versions, for example, while testing, include the bot alias in the user ID to separate the two conversations.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
 **postTextRequest** | [**PostTextRequest**](PostTextRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PostTextResponse**](PostTextResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putSession

> PutSessionResponse putSession(botName, botAlias, userId, putSessionRequest, opts)



&lt;p&gt;Creates a new session or modifies an existing session with an Amazon Lex bot. Use this operation to enable your application to set the state of the bot.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lex/latest/dg/how-session-api.html\&quot;&gt;Managing Sessions&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonLexRuntimeService from 'amazon_lex_runtime_service';
let defaultClient = AmazonLexRuntimeService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexRuntimeService.DefaultApi();
let botName = "botName_example"; // String | The name of the bot that contains the session data.
let botAlias = "botAlias_example"; // String | The alias in use for the bot that contains the session data.
let userId = "userId_example"; // String | The ID of the client application user. Amazon Lex uses this to identify a user's conversation with your bot. 
let putSessionRequest = new AmazonLexRuntimeService.PutSessionRequest(); // PutSessionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'accept': "accept_example" // String | <p>The message that Amazon Lex returns in the response can be either text or speech based depending on the value of this field.</p> <ul> <li> <p>If the value is <code>text/plain; charset=utf-8</code>, Amazon Lex returns text in the response.</p> </li> <li> <p>If the value begins with <code>audio/</code>, Amazon Lex returns speech in the response. Amazon Lex uses Amazon Polly to generate the speech in the configuration that you specify. For example, if you specify <code>audio/mpeg</code> as the value, Amazon Lex returns speech in the MPEG format.</p> </li> <li> <p>If the value is <code>audio/pcm</code>, the speech is returned as <code>audio/pcm</code> in 16-bit, little endian format.</p> </li> <li> <p>The following are the accepted values:</p> <ul> <li> <p> <code>audio/mpeg</code> </p> </li> <li> <p> <code>audio/ogg</code> </p> </li> <li> <p> <code>audio/pcm</code> </p> </li> <li> <p> <code>audio/_*</code> (defaults to mpeg)</p> </li> <li> <p> <code>text/plain; charset=utf-8</code> </p> </li> </ul> </li> </ul>
};
apiInstance.putSession(botName, botAlias, userId, putSessionRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **botName** | **String**| The name of the bot that contains the session data. | 
 **botAlias** | **String**| The alias in use for the bot that contains the session data. | 
 **userId** | **String**| The ID of the client application user. Amazon Lex uses this to identify a user&#39;s conversation with your bot.  | 
 **putSessionRequest** | [**PutSessionRequest**](PutSessionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **accept** | **String**| &lt;p&gt;The message that Amazon Lex returns in the response can be either text or speech based depending on the value of this field.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the value is &lt;code&gt;text/plain; charset&#x3D;utf-8&lt;/code&gt;, Amazon Lex returns text in the response.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the value begins with &lt;code&gt;audio/&lt;/code&gt;, Amazon Lex returns speech in the response. Amazon Lex uses Amazon Polly to generate the speech in the configuration that you specify. For example, if you specify &lt;code&gt;audio/mpeg&lt;/code&gt; as the value, Amazon Lex returns speech in the MPEG format.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the value is &lt;code&gt;audio/pcm&lt;/code&gt;, the speech is returned as &lt;code&gt;audio/pcm&lt;/code&gt; in 16-bit, little endian format.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following are the accepted values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;audio/mpeg&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;audio/ogg&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;audio/pcm&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;audio/_*&lt;/code&gt; (defaults to mpeg)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;text/plain; charset&#x3D;utf-8&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 

### Return type

[**PutSessionResponse**](PutSessionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

