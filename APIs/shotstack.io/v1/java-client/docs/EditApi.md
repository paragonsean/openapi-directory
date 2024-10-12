# EditApi

All URIs are relative to *https://api.shotstack.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRender**](EditApi.md#getRender) | **GET** /render/{id} | Get Render Status |
| [**postRender**](EditApi.md#postRender) | **POST** /render | Render Asset |


<a id="getRender"></a>
# **getRender**
> RenderResponse getRender(id)

Get Render Status

Get the rendering status, temporary asset url and details of a render by ID.  **base URL:** https://api.shotstack.io/{version}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shotstack.io/v1");
    
    // Configure API key authorization: DeveloperKey
    ApiKeyAuth DeveloperKey = (ApiKeyAuth) defaultClient.getAuthentication("DeveloperKey");
    DeveloperKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DeveloperKey.setApiKeyPrefix("Token");

    EditApi apiInstance = new EditApi(defaultClient);
    String id = "id_example"; // String | The id of the timeline render task in UUID format
    try {
      RenderResponse result = apiInstance.getRender(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditApi#getRender");
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
| **id** | **String**| The id of the timeline render task in UUID format | |

### Return type

[**RenderResponse**](RenderResponse.md)

### Authorization

[DeveloperKey](../README.md#DeveloperKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The render status details |  -  |

<a id="postRender"></a>
# **postRender**
> QueuedResponse postRender(edit)

Render Asset

Queue and render the contents of a timeline as a video, image or audio file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shotstack.io/v1");
    
    // Configure API key authorization: DeveloperKey
    ApiKeyAuth DeveloperKey = (ApiKeyAuth) defaultClient.getAuthentication("DeveloperKey");
    DeveloperKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DeveloperKey.setApiKeyPrefix("Token");

    EditApi apiInstance = new EditApi(defaultClient);
    Edit edit = new Edit(); // Edit | The video, image or audio edit specified using JSON.  **base URL:** https://api.shotstack.io/{version}
    try {
      QueuedResponse result = apiInstance.postRender(edit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditApi#postRender");
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
| **edit** | [**Edit**](Edit.md)| The video, image or audio edit specified using JSON.  **base URL:** https://api.shotstack.io/{version} | |

### Return type

[**QueuedResponse**](QueuedResponse.md)

### Authorization

[DeveloperKey](../README.md#DeveloperKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The queued render details |  -  |

