# SnippetApi

All URIs are relative to *https://api.musixmatch.com/ws/1.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**trackSnippetGetGet**](SnippetApi.md#trackSnippetGetGet) | **GET** /track.snippet.get |  |


<a id="trackSnippetGetGet"></a>
# **trackSnippetGetGet**
> TrackSnippetGetGet200Response trackSnippetGetGet(trackId, format, paramCallback)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnippetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.musixmatch.com/ws/1.1");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    SnippetApi apiInstance = new SnippetApi(defaultClient);
    String trackId = "trackId_example"; // String | The musiXmatch track id
    String format = "json"; // String | output format: json, jsonp, xml.
    String paramCallback = "paramCallback_example"; // String | jsonp callback
    try {
      TrackSnippetGetGet200Response result = apiInstance.trackSnippetGetGet(trackId, format, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnippetApi#trackSnippetGetGet");
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
| **trackId** | **String**| The musiXmatch track id | |
| **format** | **String**| output format: json, jsonp, xml. | [optional] [default to json] |
| **paramCallback** | **String**| jsonp callback | [optional] |

### Return type

[**TrackSnippetGetGet200Response**](TrackSnippetGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful. |  -  |

