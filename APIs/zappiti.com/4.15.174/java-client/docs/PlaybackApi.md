# PlaybackApi

All URIs are relative to *http://192.168.1.5:8990*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lastMediaPost**](PlaybackApi.md#lastMediaPost) | **POST** /LastMedia | Get informations about last media playback |
| [**startVideoPost**](PlaybackApi.md#startVideoPost) | **POST** /StartVideo | Start the playback |


<a id="lastMediaPost"></a>
# **lastMediaPost**
> LastMediaResult lastMediaPost(body)

Get informations about last media playback

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaybackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://192.168.1.5:8990");

    PlaybackApi apiInstance = new PlaybackApi(defaultClient);
    LastMediaRequest body = new LastMediaRequest(); // LastMediaRequest | 
    try {
      LastMediaResult result = apiInstance.lastMediaPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaybackApi#lastMediaPost");
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
| **body** | [**LastMediaRequest**](LastMediaRequest.md)|  | |

### Return type

[**LastMediaResult**](LastMediaResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | LastMediaResult |  -  |

<a id="startVideoPost"></a>
# **startVideoPost**
> StartVideoResult startVideoPost(body)

Start the playback

Start the playback of the speficied video. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaybackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://192.168.1.5:8990");

    PlaybackApi apiInstance = new PlaybackApi(defaultClient);
    StartVideoRequest body = new StartVideoRequest(); // StartVideoRequest | 
    try {
      StartVideoResult result = apiInstance.startVideoPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaybackApi#startVideoPost");
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
| **body** | [**StartVideoRequest**](StartVideoRequest.md)|  | |

### Return type

[**StartVideoResult**](StartVideoResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | StartVideoResult |  -  |

