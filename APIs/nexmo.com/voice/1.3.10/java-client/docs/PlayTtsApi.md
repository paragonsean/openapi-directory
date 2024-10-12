# PlayTtsApi

All URIs are relative to *https://api.nexmo.com/v1/calls*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**startTalk**](PlayTtsApi.md#startTalk) | **PUT** /{uuid}/talk | Play text to speech into a call |
| [**stopTalk**](PlayTtsApi.md#stopTalk) | **DELETE** /{uuid}/talk | Stop text to speech in a call |


<a id="startTalk"></a>
# **startTalk**
> StartTalkResponse startTalk(uuid, startTalkRequest)

Play text to speech into a call

Play text to speech into a call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayTtsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v1/calls");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PlayTtsApi apiInstance = new PlayTtsApi(defaultClient);
    String uuid = "63f61863-4a51-4f6b-86e1-46edebcf9356"; // String | UUID of the Call Leg
    StartTalkRequest startTalkRequest = new StartTalkRequest(); // StartTalkRequest | Action to perform
    try {
      StartTalkResponse result = apiInstance.startTalk(uuid, startTalkRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayTtsApi#startTalk");
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
| **uuid** | **String**| UUID of the Call Leg | |
| **startTalkRequest** | [**StartTalkRequest**](StartTalkRequest.md)| Action to perform | [optional] |

### Return type

[**StartTalkResponse**](StartTalkResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |

<a id="stopTalk"></a>
# **stopTalk**
> StopTalkResponse stopTalk(uuid)

Stop text to speech in a call

Stop text to speech in a call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayTtsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v1/calls");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PlayTtsApi apiInstance = new PlayTtsApi(defaultClient);
    String uuid = "63f61863-4a51-4f6b-86e1-46edebcf9356"; // String | UUID of the Call Leg
    try {
      StopTalkResponse result = apiInstance.stopTalk(uuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayTtsApi#stopTalk");
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
| **uuid** | **String**| UUID of the Call Leg | |

### Return type

[**StopTalkResponse**](StopTalkResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |

