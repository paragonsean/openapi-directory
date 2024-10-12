# RevisionsApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkRevisions**](RevisionsApi.md#checkRevisions) | **HEAD** /revisions | Requests the headers and status of the given resource. |
| [**getRevisions**](RevisionsApi.md#getRevisions) | **GET** /revisions | Gets a list of key-value revisions. |


<a id="checkRevisions"></a>
# **checkRevisions**
> checkRevisions(apiVersion, key, label, syncToken, after, acceptDatetime, $select)

Requests the headers and status of the given resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RevisionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    RevisionsApi apiInstance = new RevisionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String key = "key_example"; // String | A filter used to match keys.
    String label = "label_example"; // String | A filter used to match labels
    String syncToken = "syncToken_example"; // String | Used to guarantee real-time consistency between requests.
    String after = "after_example"; // String | Instructs the server to return elements that appear after the element referred to by the specified token.
    String acceptDatetime = "acceptDatetime_example"; // String | Requests the server to respond with the state of the resource at the specified time.
    List<String> $select = Arrays.asList(); // List<String> | Used to select what fields are present in the returned resource(s).
    try {
      apiInstance.checkRevisions(apiVersion, key, label, syncToken, after, acceptDatetime, $select);
    } catch (ApiException e) {
      System.err.println("Exception when calling RevisionsApi#checkRevisions");
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
| **key** | **String**| A filter used to match keys. | [optional] |
| **label** | **String**| A filter used to match labels | [optional] |
| **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] |
| **after** | **String**| Instructs the server to return elements that appear after the element referred to by the specified token. | [optional] |
| **acceptDatetime** | **String**| Requests the server to respond with the state of the resource at the specified time. | [optional] |
| **$select** | [**List&lt;String&gt;**](String.md)| Used to select what fields are present in the returned resource(s). | [optional] [enum: key, label, content_type, value, last_modified, tags, locked, etag] |

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

<a id="getRevisions"></a>
# **getRevisions**
> KeyValueListResult getRevisions(apiVersion, key, label, syncToken, after, acceptDatetime, $select)

Gets a list of key-value revisions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RevisionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    RevisionsApi apiInstance = new RevisionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String key = "key_example"; // String | A filter used to match keys.
    String label = "label_example"; // String | A filter used to match labels
    String syncToken = "syncToken_example"; // String | Used to guarantee real-time consistency between requests.
    String after = "after_example"; // String | Instructs the server to return elements that appear after the element referred to by the specified token.
    String acceptDatetime = "acceptDatetime_example"; // String | Requests the server to respond with the state of the resource at the specified time.
    List<String> $select = Arrays.asList(); // List<String> | Used to select what fields are present in the returned resource(s).
    try {
      KeyValueListResult result = apiInstance.getRevisions(apiVersion, key, label, syncToken, after, acceptDatetime, $select);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RevisionsApi#getRevisions");
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
| **key** | **String**| A filter used to match keys. | [optional] |
| **label** | **String**| A filter used to match labels | [optional] |
| **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] |
| **after** | **String**| Instructs the server to return elements that appear after the element referred to by the specified token. | [optional] |
| **acceptDatetime** | **String**| Requests the server to respond with the state of the resource at the specified time. | [optional] |
| **$select** | [**List&lt;String&gt;**](String.md)| Used to select what fields are present in the returned resource(s). | [optional] [enum: key, label, content_type, value, last_modified, tags, locked, etag] |

### Return type

[**KeyValueListResult**](KeyValueListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.microsoft.appconfig.kvset+json, application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * Sync-Token - Enables real-time consistency between requests by providing the returned value in the next request made to the server. <br>  |
| **0** | Error response describing why the operation failed |  -  |

