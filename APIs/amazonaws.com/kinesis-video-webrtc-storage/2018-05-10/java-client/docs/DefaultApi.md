# DefaultApi

All URIs are relative to *http://kinesisvideo.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**joinStorageSession**](DefaultApi.md#joinStorageSession) | **POST** /joinStorageSession |  |


<a id="joinStorageSession"></a>
# **joinStorageSession**
> joinStorageSession(joinStorageSessionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt; Join the ongoing one way-video and/or multi-way audio WebRTC session as a video producing device for an input channel. If there’s no existing session for the channel, a new streaming session needs to be created, and the Amazon Resource Name (ARN) of the signaling channel must be provided. &lt;/p&gt; &lt;p&gt;Currently for the &lt;code&gt;SINGLE_MASTER&lt;/code&gt; type, a video producing device is able to ingest both audio and video media into a stream, while viewers can only ingest audio. Both a video producing device and viewers can join the session first, and wait for other participants.&lt;/p&gt; &lt;p&gt;While participants are having peer to peer conversations through webRTC, the ingested media session will be stored into the Kinesis Video Stream. Multiple viewers are able to playback real-time media.&lt;/p&gt; &lt;p&gt;Customers can also use existing Kinesis Video Streams features like &lt;code&gt;HLS&lt;/code&gt; or &lt;code&gt;DASH&lt;/code&gt; playback, Image generation, and more with ingested WebRTC media.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Assume that only one video producing device client can be associated with a session for the channel. If more than one client joins the session of a specific channel as a video producing device, the most recent client request takes precedence. &lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("http://kinesisvideo.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    JoinStorageSessionRequest joinStorageSessionRequest = new JoinStorageSessionRequest(); // JoinStorageSessionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.joinStorageSession(joinStorageSessionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#joinStorageSession");
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
| **joinStorageSessionRequest** | [**JoinStorageSessionRequest**](JoinStorageSessionRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ClientLimitExceededException |  -  |
| **481** | InvalidArgumentException |  -  |
| **482** | AccessDeniedException |  -  |
| **483** | ResourceNotFoundException |  -  |

