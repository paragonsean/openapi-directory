# SharedSolidFillsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedSolidfillsGetId**](SharedSolidFillsApi.md#sharedSolidfillsGetId) | **GET** /Shared/SolidFills/{id} | SolidFills: Get by Id |


<a id="sharedSolidfillsGetId"></a>
# **sharedSolidfillsGetId**
> SharedSolidFills sharedSolidfillsGetId(id)

SolidFills: Get by Id

Get by Id: Use this method to retrieve a SolidFills object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedSolidFillsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedSolidFillsApi apiInstance = new SharedSolidFillsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      SharedSolidFills result = apiInstance.sharedSolidfillsGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedSolidFillsApi#sharedSolidfillsGetId");
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

[**SharedSolidFills**](SharedSolidFills.md)

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

