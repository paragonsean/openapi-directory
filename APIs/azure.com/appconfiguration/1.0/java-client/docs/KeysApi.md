# KeysApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkKeys**](KeysApi.md#checkKeys) | **HEAD** /keys | Requests the headers and status of the given resource. |
| [**getKeys**](KeysApi.md#getKeys) | **GET** /keys | Gets a list of keys. |


<a id="checkKeys"></a>
# **checkKeys**
> checkKeys(apiVersion, name, syncToken, after, acceptDatetime)

Requests the headers and status of the given resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String name = "name_example"; // String | A filter for the name of the returned keys.
    String syncToken = "syncToken_example"; // String | Used to guarantee real-time consistency between requests.
    String after = "after_example"; // String | Instructs the server to return elements that appear after the element referred to by the specified token.
    String acceptDatetime = "acceptDatetime_example"; // String | Requests the server to respond with the state of the resource at the specified time.
    try {
      apiInstance.checkKeys(apiVersion, name, syncToken, after, acceptDatetime);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#checkKeys");
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
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **name** | **String**| A filter for the name of the returned keys. | [optional] |
| **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] |
| **after** | **String**| Instructs the server to return elements that appear after the element referred to by the specified token. | [optional] |
| **acceptDatetime** | **String**| Requests the server to respond with the state of the resource at the specified time. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * Sync-Token - Enables real-time consistency between requests by providing the returned value in the next request made to the server. <br>  |
| **0** | Error response describing why the operation failed |  -  |

<a id="getKeys"></a>
# **getKeys**
> KeyListResult getKeys(apiVersion, name, syncToken, after, acceptDatetime)

Gets a list of keys.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String name = "name_example"; // String | A filter for the name of the returned keys.
    String syncToken = "syncToken_example"; // String | Used to guarantee real-time consistency between requests.
    String after = "after_example"; // String | Instructs the server to return elements that appear after the element referred to by the specified token.
    String acceptDatetime = "acceptDatetime_example"; // String | Requests the server to respond with the state of the resource at the specified time.
    try {
      KeyListResult result = apiInstance.getKeys(apiVersion, name, syncToken, after, acceptDatetime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#getKeys");
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
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **name** | **String**| A filter for the name of the returned keys. | [optional] |
| **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] |
| **after** | **String**| Instructs the server to return elements that appear after the element referred to by the specified token. | [optional] |
| **acceptDatetime** | **String**| Requests the server to respond with the state of the resource at the specified time. | [optional] |

### Return type

[**KeyListResult**](KeyListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.microsoft.appconfig.keyset+json, application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * Sync-Token - Enables real-time consistency between requests by providing the returned value in the next request made to the server. <br>  |
| **0** | Error response describing why the operation failed |  -  |

