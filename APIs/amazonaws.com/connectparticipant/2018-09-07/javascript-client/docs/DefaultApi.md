# AmazonConnectParticipantService.DefaultApi

All URIs are relative to *http://participant.connect.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**completeAttachmentUpload**](DefaultApi.md#completeAttachmentUpload) | **POST** /participant/complete-attachment-upload#X-Amz-Bearer | 
[**createParticipantConnection**](DefaultApi.md#createParticipantConnection) | **POST** /participant/connection#X-Amz-Bearer | 
[**disconnectParticipant**](DefaultApi.md#disconnectParticipant) | **POST** /participant/disconnect#X-Amz-Bearer | 
[**getAttachment**](DefaultApi.md#getAttachment) | **POST** /participant/attachment#X-Amz-Bearer | 
[**getTranscript**](DefaultApi.md#getTranscript) | **POST** /participant/transcript#X-Amz-Bearer | 
[**sendEvent**](DefaultApi.md#sendEvent) | **POST** /participant/event#X-Amz-Bearer | 
[**sendMessage**](DefaultApi.md#sendMessage) | **POST** /participant/message#X-Amz-Bearer | 
[**startAttachmentUpload**](DefaultApi.md#startAttachmentUpload) | **POST** /participant/start-attachment-upload#X-Amz-Bearer | 



## completeAttachmentUpload

> Object completeAttachmentUpload(xAmzBearer, completeAttachmentUploadRequest, opts)



&lt;p&gt;Allows you to confirm that the attachment has been uploaded using the pre-signed URL provided in StartAttachmentUpload API. &lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectParticipantService from 'amazon_connect_participant_service';
let defaultClient = AmazonConnectParticipantService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectParticipantService.DefaultApi();
let xAmzBearer = "xAmzBearer_example"; // String | The authentication token associated with the participant's connection.
let completeAttachmentUploadRequest = new AmazonConnectParticipantService.CompleteAttachmentUploadRequest(); // CompleteAttachmentUploadRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.completeAttachmentUpload(xAmzBearer, completeAttachmentUploadRequest, opts, (error, data, response) => {
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
 **xAmzBearer** | **String**| The authentication token associated with the participant&#39;s connection. | 
 **completeAttachmentUploadRequest** | [**CompleteAttachmentUploadRequest**](CompleteAttachmentUploadRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createParticipantConnection

> CreateParticipantConnectionResponse createParticipantConnection(xAmzBearer, createParticipantConnectionRequest, opts)



&lt;p&gt;Creates the participant&#39;s connection. &lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ParticipantToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ConnectionToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The participant token is valid for the lifetime of the participant – until they are part of a contact.&lt;/p&gt; &lt;p&gt;The response URL for &lt;code&gt;WEBSOCKET&lt;/code&gt; Type has a connect expiry timeout of 100s. Clients must manually connect to the returned websocket URL and subscribe to the desired topic. &lt;/p&gt; &lt;p&gt;For chat, you need to publish the following on the established websocket connection:&lt;/p&gt; &lt;p&gt; &lt;code&gt;{\&quot;topic\&quot;:\&quot;aws/subscribe\&quot;,\&quot;content\&quot;:{\&quot;topics\&quot;:[\&quot;aws/chat\&quot;]}}&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Upon websocket URL expiry, as specified in the response ConnectionExpiry parameter, clients need to call this API again to obtain a new websocket URL and perform the same steps as before.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Message streaming support&lt;/b&gt;: This API can also be used together with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_StartContactStreaming.html\&quot;&gt;StartContactStreaming&lt;/a&gt; API to create a participant connection for chat contacts that are not using a websocket. For more information about message streaming, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/chat-message-streaming.html\&quot;&gt;Enable real-time chat message streaming&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Feature specifications&lt;/b&gt;: For information about feature specifications, such as the allowed number of open websocket connections per participant, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#feature-limits\&quot;&gt;Feature specifications&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonConnectParticipantService from 'amazon_connect_participant_service';
let defaultClient = AmazonConnectParticipantService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectParticipantService.DefaultApi();
let xAmzBearer = "xAmzBearer_example"; // String | <p>This is a header parameter.</p> <p>The ParticipantToken as obtained from <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html\">StartChatContact</a> API response.</p>
let createParticipantConnectionRequest = new AmazonConnectParticipantService.CreateParticipantConnectionRequest(); // CreateParticipantConnectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createParticipantConnection(xAmzBearer, createParticipantConnectionRequest, opts, (error, data, response) => {
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
 **xAmzBearer** | **String**| &lt;p&gt;This is a header parameter.&lt;/p&gt; &lt;p&gt;The ParticipantToken as obtained from &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html\&quot;&gt;StartChatContact&lt;/a&gt; API response.&lt;/p&gt; | 
 **createParticipantConnectionRequest** | [**CreateParticipantConnectionRequest**](CreateParticipantConnectionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateParticipantConnectionResponse**](CreateParticipantConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disconnectParticipant

> Object disconnectParticipant(xAmzBearer, disconnectParticipantRequest, opts)



&lt;p&gt;Disconnects a participant. &lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectParticipantService from 'amazon_connect_participant_service';
let defaultClient = AmazonConnectParticipantService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectParticipantService.DefaultApi();
let xAmzBearer = "xAmzBearer_example"; // String | The authentication token associated with the participant's connection.
let disconnectParticipantRequest = new AmazonConnectParticipantService.DisconnectParticipantRequest(); // DisconnectParticipantRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disconnectParticipant(xAmzBearer, disconnectParticipantRequest, opts, (error, data, response) => {
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
 **xAmzBearer** | **String**| The authentication token associated with the participant&#39;s connection. | 
 **disconnectParticipantRequest** | [**DisconnectParticipantRequest**](DisconnectParticipantRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAttachment

> GetAttachmentResponse getAttachment(xAmzBearer, getAttachmentRequest, opts)



&lt;p&gt;Provides a pre-signed URL for download of a completed attachment. This is an asynchronous API for use with active contacts.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectParticipantService from 'amazon_connect_participant_service';
let defaultClient = AmazonConnectParticipantService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectParticipantService.DefaultApi();
let xAmzBearer = "xAmzBearer_example"; // String | The authentication token associated with the participant's connection.
let getAttachmentRequest = new AmazonConnectParticipantService.GetAttachmentRequest(); // GetAttachmentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAttachment(xAmzBearer, getAttachmentRequest, opts, (error, data, response) => {
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
 **xAmzBearer** | **String**| The authentication token associated with the participant&#39;s connection. | 
 **getAttachmentRequest** | [**GetAttachmentRequest**](GetAttachmentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAttachmentResponse**](GetAttachmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTranscript

> GetTranscriptResponse getTranscript(xAmzBearer, getTranscriptRequest, opts)



&lt;p&gt;Retrieves a transcript of the session, including details about any attachments. For information about accessing past chat contact transcripts for a persistent chat, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/chat-persistence.html\&quot;&gt;Enable persistent chat&lt;/a&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectParticipantService from 'amazon_connect_participant_service';
let defaultClient = AmazonConnectParticipantService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectParticipantService.DefaultApi();
let xAmzBearer = "xAmzBearer_example"; // String | The authentication token associated with the participant's connection.
let getTranscriptRequest = new AmazonConnectParticipantService.GetTranscriptRequest(); // GetTranscriptRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.getTranscript(xAmzBearer, getTranscriptRequest, opts, (error, data, response) => {
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
 **xAmzBearer** | **String**| The authentication token associated with the participant&#39;s connection. | 
 **getTranscriptRequest** | [**GetTranscriptRequest**](GetTranscriptRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**GetTranscriptResponse**](GetTranscriptResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendEvent

> SendEventResponse sendEvent(xAmzBearer, sendEventRequest, opts)



&lt;p&gt;Sends an event. &lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectParticipantService from 'amazon_connect_participant_service';
let defaultClient = AmazonConnectParticipantService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectParticipantService.DefaultApi();
let xAmzBearer = "xAmzBearer_example"; // String | The authentication token associated with the participant's connection.
let sendEventRequest = new AmazonConnectParticipantService.SendEventRequest(); // SendEventRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.sendEvent(xAmzBearer, sendEventRequest, opts, (error, data, response) => {
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
 **xAmzBearer** | **String**| The authentication token associated with the participant&#39;s connection. | 
 **sendEventRequest** | [**SendEventRequest**](SendEventRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SendEventResponse**](SendEventResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendMessage

> SendMessageResponse sendMessage(xAmzBearer, sendMessageRequest, opts)



&lt;p&gt;Sends a message.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectParticipantService from 'amazon_connect_participant_service';
let defaultClient = AmazonConnectParticipantService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectParticipantService.DefaultApi();
let xAmzBearer = "xAmzBearer_example"; // String | The authentication token associated with the connection.
let sendMessageRequest = new AmazonConnectParticipantService.SendMessageRequest(); // SendMessageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.sendMessage(xAmzBearer, sendMessageRequest, opts, (error, data, response) => {
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
 **xAmzBearer** | **String**| The authentication token associated with the connection. | 
 **sendMessageRequest** | [**SendMessageRequest**](SendMessageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SendMessageResponse**](SendMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startAttachmentUpload

> StartAttachmentUploadResponse startAttachmentUpload(xAmzBearer, startAttachmentUploadRequest, opts)



&lt;p&gt;Provides a pre-signed Amazon S3 URL in response for uploading the file directly to S3.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectParticipantService from 'amazon_connect_participant_service';
let defaultClient = AmazonConnectParticipantService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectParticipantService.DefaultApi();
let xAmzBearer = "xAmzBearer_example"; // String | The authentication token associated with the participant's connection.
let startAttachmentUploadRequest = new AmazonConnectParticipantService.StartAttachmentUploadRequest(); // StartAttachmentUploadRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startAttachmentUpload(xAmzBearer, startAttachmentUploadRequest, opts, (error, data, response) => {
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
 **xAmzBearer** | **String**| The authentication token associated with the participant&#39;s connection. | 
 **startAttachmentUploadRequest** | [**StartAttachmentUploadRequest**](StartAttachmentUploadRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartAttachmentUploadResponse**](StartAttachmentUploadResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

