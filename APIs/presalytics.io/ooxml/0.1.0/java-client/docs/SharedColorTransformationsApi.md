# SharedColorTransformationsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedColortransformationsGetId**](SharedColorTransformationsApi.md#sharedColortransformationsGetId) | **GET** /Shared/ColorTransformations/{id} | ColorTransformations: Get by Id |


<a id="sharedColortransformationsGetId"></a>
# **sharedColortransformationsGetId**
> SharedColorTransformations sharedColortransformationsGetId(id)

ColorTransformations: Get by Id

Get by Id: Use this method to retrieve a ColorTransformations object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedColorTransformationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedColorTransformationsApi apiInstance = new SharedColorTransformationsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      SharedColorTransformations result = apiInstance.sharedColortransformationsGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedColorTransformationsApi#sharedColortransformationsGetId");
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

[**SharedColorTransformations**](SharedColorTransformations.md)

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

