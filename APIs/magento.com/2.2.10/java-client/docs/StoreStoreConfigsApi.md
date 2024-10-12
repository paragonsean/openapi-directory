# StoreStoreConfigsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storeStoreConfigManagerV1GetStoreConfigsGet**](StoreStoreConfigsApi.md#storeStoreConfigManagerV1GetStoreConfigsGet) | **GET** /V1/store/storeConfigs | store/storeConfigs |


<a id="storeStoreConfigManagerV1GetStoreConfigsGet"></a>
# **storeStoreConfigManagerV1GetStoreConfigsGet**
> List&lt;StoreDataStoreConfigInterface&gt; storeStoreConfigManagerV1GetStoreConfigsGet(storeCodes)

store/storeConfigs



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoreStoreConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    StoreStoreConfigsApi apiInstance = new StoreStoreConfigsApi(defaultClient);
    List<String> storeCodes = Arrays.asList(); // List<String> | 
    try {
      List<StoreDataStoreConfigInterface> result = apiInstance.storeStoreConfigManagerV1GetStoreConfigsGet(storeCodes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoreStoreConfigsApi#storeStoreConfigManagerV1GetStoreConfigsGet");
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
| **storeCodes** | [**List&lt;String&gt;**](String.md)|  | [optional] |

### Return type

[**List&lt;StoreDataStoreConfigInterface&gt;**](StoreDataStoreConfigInterface.md)

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

