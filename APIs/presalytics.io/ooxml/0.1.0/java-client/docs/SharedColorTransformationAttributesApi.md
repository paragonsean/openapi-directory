# SharedColorTransformationAttributesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedColortransformationattributesGetId**](SharedColorTransformationAttributesApi.md#sharedColortransformationattributesGetId) | **GET** /Shared/ColorTransformationAttributes/{id} | ColorTransformationAttributes: Get by Id |


<a id="sharedColortransformationattributesGetId"></a>
# **sharedColortransformationattributesGetId**
> SharedColorTransformationAttributes sharedColortransformationattributesGetId(id)

ColorTransformationAttributes: Get by Id

Get by Id: Use this method to retrieve a ColorTransformationAttributes object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedColorTransformationAttributesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedColorTransformationAttributesApi apiInstance = new SharedColorTransformationAttributesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      SharedColorTransformationAttributes result = apiInstance.sharedColortransformationattributesGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedColorTransformationAttributesApi#sharedColortransformationattributesGetId");
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

[**SharedColorTransformationAttributes**](SharedColorTransformationAttributes.md)

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

