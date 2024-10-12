# Class10UserUserIdEditedApi

All URIs are relative to */rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resource10UserUserIdEditedGetUserEditedSetlistsGET**](Class10UserUserIdEditedApi.md#resource10UserUserIdEditedGetUserEditedSetlistsGET) | **GET** /1.0/user/{userId}/edited | . |


<a id="resource10UserUserIdEditedGetUserEditedSetlistsGET"></a>
# **resource10UserUserIdEditedGetUserEditedSetlistsGET**
> JsonSetlists resource10UserUserIdEditedGetUserEditedSetlistsGET(userId, p)

.

&lt;p&gt; Get a list of setlists of concerts edited by a user. The list contains the current version, not the version edited. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class10UserUserIdEditedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/rest");

    Class10UserUserIdEditedApi apiInstance = new Class10UserUserIdEditedApi(defaultClient);
    String userId = "userId_example"; // String | the user's userId
    Integer p = 1; // Integer | the number of the result page
    try {
      JsonSetlists result = apiInstance.resource10UserUserIdEditedGetUserEditedSetlistsGET(userId, p);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class10UserUserIdEditedApi#resource10UserUserIdEditedGetUserEditedSetlistsGET");
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
| **userId** | **String**| the user&#39;s userId | |
| **p** | **Integer**| the number of the result page | [optional] [default to 1] |

### Return type

[**JsonSetlists**](JsonSetlists.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

