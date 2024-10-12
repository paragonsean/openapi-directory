# SharedFillMapApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedFillmapGetId**](SharedFillMapApi.md#sharedFillmapGetId) | **GET** /Shared/FillMap/{id} | FillMap: Get by Id |


<a id="sharedFillmapGetId"></a>
# **sharedFillmapGetId**
> SharedFillMap sharedFillmapGetId(id)

FillMap: Get by Id

Get by Id: Use this method to retrieve a FillMap object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedFillMapApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedFillMapApi apiInstance = new SharedFillMapApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      SharedFillMap result = apiInstance.sharedFillmapGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedFillMapApi#sharedFillmapGetId");
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
| **id** | **UUID**|  | |

### Return type

[**SharedFillMap**](SharedFillMap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

