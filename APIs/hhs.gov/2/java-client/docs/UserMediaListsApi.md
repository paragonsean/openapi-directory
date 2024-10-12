# UserMediaListsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourcesUserMediaListsIdJsonGet**](UserMediaListsApi.md#resourcesUserMediaListsIdJsonGet) | **GET** /resources/userMediaLists/{id}.json | Get UserMediaList by ID |


<a id="resourcesUserMediaListsIdJsonGet"></a>
# **resourcesUserMediaListsIdJsonGet**
> List&lt;MediaItemWrapped&gt; resourcesUserMediaListsIdJsonGet(id, displayMethod)

Get UserMediaList by ID

Get a specific user media list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserMediaListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    UserMediaListsApi apiInstance = new UserMediaListsApi(defaultClient);
    Long id = 56L; // Long | The id of the record to look up
    String displayMethod = "displayMethod_example"; // String | Method used to render an html request. Accepts one: [mv, list, feed]
    try {
      List<MediaItemWrapped> result = apiInstance.resourcesUserMediaListsIdJsonGet(id, displayMethod);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserMediaListsApi#resourcesUserMediaListsIdJsonGet");
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
| **id** | **Long**| The id of the record to look up | |
| **displayMethod** | **String**| Method used to render an html request. Accepts one: [mv, list, feed] | [optional] |

### Return type

[**List&lt;MediaItemWrapped&gt;**](MediaItemWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a specific user media list by &#39;id&#39;. |  -  |
| **400** | Invalid ID |  -  |
| **500** | Internal Server Error |  -  |

