# CollectionsApi

All URIs are relative to *http://api.thenounproject.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllCollections**](CollectionsApi.md#getAllCollections) | **GET** /collections | Get all collections |


<a id="getAllCollections"></a>
# **getAllCollections**
> getAllCollections(limit, offset, page)

Get all collections

Return&#39;s a list of all collections

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.thenounproject.com");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    Integer limit = 56; // Integer | Maximum number of results
    Integer offset = 56; // Integer | Number of results to displace or skip over
    Integer page = 56; // Integer | Number of results of limit length to displace or skip over
    try {
      apiInstance.getAllCollections(limit, offset, page);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#getAllCollections");
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
| **limit** | **Integer**| Maximum number of results | [optional] |
| **offset** | **Integer**| Number of results to displace or skip over | [optional] |
| **page** | **Integer**| Number of results of limit length to displace or skip over | [optional] |

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
| **200** | No response was specified |  -  |

