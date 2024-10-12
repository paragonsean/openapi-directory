# WhoIsApi

All URIs are relative to *http://backend.id4i.de*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resolveWhoIsEntry_0**](WhoIsApi.md#resolveWhoIsEntry_0) | **GET** /whois/{id4n} | Resolve owner of id4n |


<a id="resolveWhoIsEntry_0"></a>
# **resolveWhoIsEntry_0**
> WhoIsResponse resolveWhoIsEntry_0(id4n)

Resolve owner of id4n

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WhoIsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");

    WhoIsApi apiInstance = new WhoIsApi(defaultClient);
    String id4n = "id4n_example"; // String | id4n
    try {
      WhoIsResponse result = apiInstance.resolveWhoIsEntry_0(id4n);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WhoIsApi#resolveWhoIsEntry_0");
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
| **id4n** | **String**| id4n | |

### Return type

[**WhoIsResponse**](WhoIsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

