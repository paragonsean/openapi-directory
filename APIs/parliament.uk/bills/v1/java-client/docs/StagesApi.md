# StagesApi

All URIs are relative to *https://bills-api.parliament.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1StagesGet**](StagesApi.md#apiV1StagesGet) | **GET** /api/v1/Stages | Returns a list of Bill stages. |


<a id="apiV1StagesGet"></a>
# **apiV1StagesGet**
> StageReferenceSearchResult apiV1StagesGet(skip, take)

Returns a list of Bill stages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bills-api.parliament.uk");

    StagesApi apiInstance = new StagesApi(defaultClient);
    Integer skip = 56; // Integer | 
    Integer take = 56; // Integer | 
    try {
      StageReferenceSearchResult result = apiInstance.apiV1StagesGet(skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StagesApi#apiV1StagesGet");
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
| **skip** | **Integer**|  | [optional] |
| **take** | **Integer**|  | [optional] |

### Return type

[**StageReferenceSearchResult**](StageReferenceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

