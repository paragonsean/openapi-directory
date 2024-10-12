# StoreStoreGroupsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storeGroupRepositoryV1GetListGet**](StoreStoreGroupsApi.md#storeGroupRepositoryV1GetListGet) | **GET** /V1/store/storeGroups | store/storeGroups |


<a id="storeGroupRepositoryV1GetListGet"></a>
# **storeGroupRepositoryV1GetListGet**
> List&lt;StoreDataGroupInterface&gt; storeGroupRepositoryV1GetListGet()

store/storeGroups

Retrieve list of all groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoreStoreGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    StoreStoreGroupsApi apiInstance = new StoreStoreGroupsApi(defaultClient);
    try {
      List<StoreDataGroupInterface> result = apiInstance.storeGroupRepositoryV1GetListGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoreStoreGroupsApi#storeGroupRepositoryV1GetListGet");
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

[**List&lt;StoreDataGroupInterface&gt;**](StoreDataGroupInterface.md)

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

