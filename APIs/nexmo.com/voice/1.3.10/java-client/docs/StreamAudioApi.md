# StreamAudioApi

All URIs are relative to *https://api.nexmo.com/v1/calls*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**startStream**](StreamAudioApi.md#startStream) | **PUT** /{uuid}/stream | Play an audio file into a call |
| [**stopStream**](StreamAudioApi.md#stopStream) | **DELETE** /{uuid}/stream | Stop playing an audio file into a call |


<a id="startStream"></a>
# **startStream**
> StartStreamResponse startStream(uuid, startStreamRequest)

Play an audio file into a call

Play an audio file into a call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamAudioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v1/calls");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    StreamAudioApi apiInstance = new StreamAudioApi(defaultClient);
    String uuid = "63f61863-4a51-4f6b-86e1-46edebcf9356"; // String | UUID of the Call Leg
    StartStreamRequest startStreamRequest = new StartStreamRequest(); // StartStreamRequest | action to perform
    try {
      StartStreamResponse result = apiInstance.startStream(uuid, startStreamRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamAudioApi#startStream");
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
| **startStreamRequest** | [**StartStreamRequest**](StartStreamRequest.md)| action to perform | |

### Return type

[**StartStreamResponse**](StartStreamResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |

<a id="stopStream"></a>
# **stopStream**
> StopStreamResponse stopStream(uuid)

Stop playing an audio file into a call

Stop playing an audio file into a call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamAudioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v1/calls");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    StreamAudioApi apiInstance = new StreamAudioApi(defaultClient);
    String uuid = "63f61863-4a51-4f6b-86e1-46edebcf9356"; // String | UUID of the Call Leg
    try {
      StopStreamResponse result = apiInstance.stopStream(uuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamAudioApi#stopStream");
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

[**StopStreamResponse**](StopStreamResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |

