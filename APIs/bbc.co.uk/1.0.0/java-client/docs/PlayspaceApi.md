# PlayspaceApi

All URIs are relative to *https://rms.api.bbc.co.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getContainer**](PlayspaceApi.md#getContainer) | **GET** /my/playspace/containers/{id} | Playspace Container by ID |
| [**suggestContainer**](PlayspaceApi.md#suggestContainer) | **GET** /my/playspace/containers/suggested | Suggested Playspace Container |


<a id="getContainer"></a>
# **getContainer**
> PlayspaceContainer getContainer(authorization, xAPIKey, id)

Playspace Container by ID

Playspace Container by ID 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayspaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    PlayspaceApi apiInstance = new PlayspaceApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String id = "id_example"; // String | Playspace Container ID
    try {
      PlayspaceContainer result = apiInstance.getContainer(authorization, xAPIKey, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayspaceApi#getContainer");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAPIKey** | **String**| API_KEY | |
| **id** | **String**| Playspace Container ID | |

### Return type

[**PlayspaceContainer**](PlayspaceContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | There was an error with the supplied &#x60;Authorization&#x60; header. |  -  |
| **404** | No Playspace container with given ID could be found. |  -  |

<a id="suggestContainer"></a>
# **suggestContainer**
> PlayspaceContainer suggestContainer(authorization, xAPIKey, previousPid, previousContainer)

Suggested Playspace Container

Suggested Playspace Container 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayspaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    PlayspaceApi apiInstance = new PlayspaceApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String previousPid = "previousPid_example"; // String | Clip or Episode PID of the previous or first content item in the Playspace stream.
    String previousContainer = "previousContainer_example"; // String | Container ID of the previous container in the Playspace stream.
    try {
      PlayspaceContainer result = apiInstance.suggestContainer(authorization, xAPIKey, previousPid, previousContainer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayspaceApi#suggestContainer");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAPIKey** | **String**| API_KEY | |
| **previousPid** | **String**| Clip or Episode PID of the previous or first content item in the Playspace stream. | |
| **previousContainer** | **String**| Container ID of the previous container in the Playspace stream. | [optional] |

### Return type

[**PlayspaceContainer**](PlayspaceContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | There was an error with the supplied &#x60;Authorization&#x60; header. |  -  |

