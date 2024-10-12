# StoreWebsitesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storeWebsiteRepositoryV1GetListGet**](StoreWebsitesApi.md#storeWebsiteRepositoryV1GetListGet) | **GET** /V1/store/websites | store/websites |


<a id="storeWebsiteRepositoryV1GetListGet"></a>
# **storeWebsiteRepositoryV1GetListGet**
> List&lt;StoreDataWebsiteInterface&gt; storeWebsiteRepositoryV1GetListGet()

store/websites

Retrieve list of all websites

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoreWebsitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    StoreWebsitesApi apiInstance = new StoreWebsitesApi(defaultClient);
    try {
      List<StoreDataWebsiteInterface> result = apiInstance.storeWebsiteRepositoryV1GetListGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoreWebsitesApi#storeWebsiteRepositoryV1GetListGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;StoreDataWebsiteInterface&gt;**](StoreDataWebsiteInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

