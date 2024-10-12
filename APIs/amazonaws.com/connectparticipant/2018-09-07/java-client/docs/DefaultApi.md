# DefaultApi

All URIs are relative to *http://participant.connect.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**completeAttachmentUpload**](DefaultApi.md#completeAttachmentUpload) | **POST** /participant/complete-attachment-upload#X-Amz-Bearer |  |
| [**createParticipantConnection**](DefaultApi.md#createParticipantConnection) | **POST** /participant/connection#X-Amz-Bearer |  |
| [**disconnectParticipant**](DefaultApi.md#disconnectParticipant) | **POST** /participant/disconnect#X-Amz-Bearer |  |
| [**getAttachment**](DefaultApi.md#getAttachment) | **POST** /participant/attachment#X-Amz-Bearer |  |
| [**getTranscript**](DefaultApi.md#getTranscript) | **POST** /participant/transcript#X-Amz-Bearer |  |
| [**sendEvent**](DefaultApi.md#sendEvent) | **POST** /participant/event#X-Amz-Bearer |  |
| [**sendMessage**](DefaultApi.md#sendMessage) | **POST** /participant/message#X-Amz-Bearer |  |
| [**startAttachmentUpload**](DefaultApi.md#startAttachmentUpload) | **POST** /participant/start-attachment-upload#X-Amz-Bearer |  |


<a id="completeAttachmentUpload"></a>
# **completeAttachmentUpload**
> Object completeAttachmentUpload(xAmzBearer, completeAttachmentUploadRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Allows you to confirm that the attachment has been uploaded using the pre-signed URL provided in StartAttachmentUpload API. &lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://participant.connect.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzBearer = "xAmzBearer_example"; // String | The authentication token associated with the participant's connection.
    CompleteAttachmentUploadRequest completeAttachmentUploadRequest = new CompleteAttachmentUploadRequest(); // CompleteAttachmentUploadRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.completeAttachmentUpload(xAmzBearer, completeAttachmentUploadRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#completeAttachmentUpload");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzBearer** | **String**| The authentication token associated with the participant&#39;s connection. | |
| **completeAttachmentUploadRequest** | [**CompleteAttachmentUploadRequest**](CompleteAttachmentUploadRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ValidationException |  -  |
| **484** | ServiceQuotaExceededException |  -  |
| **485** | ConflictException |  -  |

<a id="createParticipantConnection"></a>
# **createParticipantConnection**
> CreateParticipantConnectionResponse createParticipantConnection(xAmzBearer, createParticipantConnectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates the participant&#39;s connection. &lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ParticipantToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ConnectionToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The participant token is valid for the lifetime of the participant – until they are part of a contact.&lt;/p&gt; &lt;p&gt;The response URL for &lt;code&gt;WEBSOCKET&lt;/code&gt; Type has a connect expiry timeout of 100s. Clients must manually connect to the returned websocket URL and subscribe to the desired topic. &lt;/p&gt; &lt;p&gt;For chat, you need to publish the following on the established websocket connection:&lt;/p&gt; &lt;p&gt; &lt;code&gt;{\&quot;topic\&quot;:\&quot;aws/subscribe\&quot;,\&quot;content\&quot;:{\&quot;topics\&quot;:[\&quot;aws/chat\&quot;]}}&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Upon websocket URL expiry, as specified in the response ConnectionExpiry parameter, clients need to call this API again to obtain a new websocket URL and perform the same steps as before.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Message streaming support&lt;/b&gt;: This API can also be used together with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_StartContactStreaming.html\&quot;&gt;StartContactStreaming&lt;/a&gt; API to create a participant connection for chat contacts that are not using a websocket. For more information about message streaming, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/chat-message-streaming.html\&quot;&gt;Enable real-time chat message streaming&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Feature specifications&lt;/b&gt;: For information about feature specifications, such as the allowed number of open websocket connections per participant, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#feature-limits\&quot;&gt;Feature specifications&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://participant.connect.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzBearer = "xAmzBearer_example"; // String | <p>This is a header parameter.</p> <p>The ParticipantToken as obtained from <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html\">StartChatContact</a> API response.</p>
    CreateParticipantConnectionRequest createParticipantConnectionRequest = new CreateParticipantConnectionRequest(); // CreateParticipantConnectionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateParticipantConnectionResponse result = apiInstance.createParticipantConnection(xAmzBearer, createParticipantConnectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createParticipantConnection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzBearer** | **String**| &lt;p&gt;This is a header parameter.&lt;/p&gt; &lt;p&gt;The ParticipantToken as obtained from &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html\&quot;&gt;StartChatContact&lt;/a&gt; API response.&lt;/p&gt; | |
| **createParticipantConnectionRequest** | [**CreateParticipantConnectionRequest**](CreateParticipantConnectionRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateParticipantConnectionResponse**](CreateParticipantConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ValidationException |  -  |

<a id="disconnectParticipant"></a>
# **disconnectParticipant**
> Object disconnectParticipant(xAmzBearer, disconnectParticipantRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Disconnects a participant. &lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://participant.connect.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzBearer = "xAmzBearer_example"; // String | The authentication token associated with the participant's connection.
    DisconnectParticipantRequest disconnectParticipantRequest = new DisconnectParticipantRequest(); // DisconnectParticipantRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.disconnectParticipant(xAmzBearer, disconnectParticipantRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#disconnectParticipant");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzBearer** | **String**| The authentication token associated with the participant&#39;s connection. | |
| **disconnectParticipantRequest** | [**DisconnectParticipantRequest**](DisconnectParticipantRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ValidationException |  -  |

<a id="getAttachment"></a>
# **getAttachment**
> GetAttachmentResponse getAttachment(xAmzBearer, getAttachmentRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Provides a pre-signed URL for download of a completed attachment. This is an asynchronous API for use with active contacts.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://participant.connect.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzBearer = "xAmzBearer_example"; // String | The authentication token associated with the participant's connection.
    GetAttachmentRequest getAttachmentRequest = new GetAttachmentRequest(); // GetAttachmentRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetAttachmentResponse result = apiInstance.getAttachment(xAmzBearer, getAttachmentRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAttachment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzBearer** | **String**| The authentication token associated with the participant&#39;s connection. | |
| **getAttachmentRequest** | [**GetAttachmentRequest**](GetAttachmentRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetAttachmentResponse**](GetAttachmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ValidationException |  -  |

<a id="getTranscript"></a>
# **getTranscript**
> GetTranscriptResponse getTranscript(xAmzBearer, getTranscriptRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



&lt;p&gt;Retrieves a transcript of the session, including details about any attachments. For information about accessing past chat contact transcripts for a persistent chat, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/chat-persistence.html\&quot;&gt;Enable persistent chat&lt;/a&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://participant.connect.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzBearer = "xAmzBearer_example"; // String | The authentication token associated with the participant's connection.
    GetTranscriptRequest getTranscriptRequest = new GetTranscriptRequest(); // GetTranscriptRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      GetTranscriptResponse result = apiInstance.getTranscript(xAmzBearer, getTranscriptRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getTranscript");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzBearer** | **String**| The authentication token associated with the participant&#39;s connection. | |
| **getTranscriptRequest** | [**GetTranscriptRequest**](GetTranscriptRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**GetTranscriptResponse**](GetTranscriptResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ValidationException |  -  |

<a id="sendEvent"></a>
# **sendEvent**
> SendEventResponse sendEvent(xAmzBearer, sendEventRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Sends an event. &lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://participant.connect.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzBearer = "xAmzBearer_example"; // String | The authentication token associated with the participant's connection.
    SendEventRequest sendEventRequest = new SendEventRequest(); // SendEventRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      SendEventResponse result = apiInstance.sendEvent(xAmzBearer, sendEventRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sendEvent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzBearer** | **String**| The authentication token associated with the participant&#39;s connection. | |
| **sendEventRequest** | [**SendEventRequest**](SendEventRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**SendEventResponse**](SendEventResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ValidationException |  -  |

<a id="sendMessage"></a>
# **sendMessage**
> SendMessageResponse sendMessage(xAmzBearer, sendMessageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Sends a message.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://participant.connect.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzBearer = "xAmzBearer_example"; // String | The authentication token associated with the connection.
    SendMessageRequest sendMessageRequest = new SendMessageRequest(); // SendMessageRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      SendMessageResponse result = apiInstance.sendMessage(xAmzBearer, sendMessageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sendMessage");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzBearer** | **String**| The authentication token associated with the connection. | |
| **sendMessageRequest** | [**SendMessageRequest**](SendMessageRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**SendMessageResponse**](SendMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ValidationException |  -  |

<a id="startAttachmentUpload"></a>
# **startAttachmentUpload**
> StartAttachmentUploadResponse startAttachmentUpload(xAmzBearer, startAttachmentUploadRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Provides a pre-signed Amazon S3 URL in response for uploading the file directly to S3.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://participant.connect.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzBearer = "xAmzBearer_example"; // String | The authentication token associated with the participant's connection.
    StartAttachmentUploadRequest startAttachmentUploadRequest = new StartAttachmentUploadRequest(); // StartAttachmentUploadRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartAttachmentUploadResponse result = apiInstance.startAttachmentUpload(xAmzBearer, startAttachmentUploadRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startAttachmentUpload");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzBearer** | **String**| The authentication token associated with the participant&#39;s connection. | |
| **startAttachmentUploadRequest** | [**StartAttachmentUploadRequest**](StartAttachmentUploadRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartAttachmentUploadResponse**](StartAttachmentUploadResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDeniedException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ValidationException |  -  |
| **484** | ServiceQuotaExceededException |  -  |

