# StoreStoreViewsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storeStoreRepositoryV1GetListGet**](StoreStoreViewsApi.md#storeStoreRepositoryV1GetListGet) | **GET** /V1/store/storeViews | store/storeViews |


<a id="storeStoreRepositoryV1GetListGet"></a>
# **storeStoreRepositoryV1GetListGet**
> List&lt;StoreDataStoreInterface&gt; storeStoreRepositoryV1GetListGet()

store/storeViews

Retrieve list of all stores

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoreStoreViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    StoreStoreViewsApi apiInstance = new StoreStoreViewsApi(defaultClient);
    try {
      List<StoreDataStoreInterface> result = apiInstance.storeStoreRepositoryV1GetListGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoreStoreViewsApi#storeStoreRepositoryV1GetListGet");
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

[**List&lt;StoreDataStoreInterface&gt;**](StoreDataStoreInterface.md)

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

