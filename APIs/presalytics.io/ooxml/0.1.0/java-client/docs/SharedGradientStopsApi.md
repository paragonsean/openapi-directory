# SharedGradientStopsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedGradientstopsGetId**](SharedGradientStopsApi.md#sharedGradientstopsGetId) | **GET** /Shared/GradientStops/{id} | GradientStops: Get by Id |


<a id="sharedGradientstopsGetId"></a>
# **sharedGradientstopsGetId**
> SharedGradientStops sharedGradientstopsGetId(id)

GradientStops: Get by Id

Get by Id: Use this method to retrieve a GradientStops object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedGradientStopsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedGradientStopsApi apiInstance = new SharedGradientStopsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      SharedGradientStops result = apiInstance.sharedGradientstopsGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedGradientStopsApi#sharedGradientstopsGetId");
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

[**SharedGradientStops**](SharedGradientStops.md)

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

