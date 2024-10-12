# SlidesGraphicsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**slidesGraphicsGetId**](SlidesGraphicsApi.md#slidesGraphicsGetId) | **GET** /Slides/Graphics/{id} | Graphics: Get by Id |


<a id="slidesGraphicsGetId"></a>
# **slidesGraphicsGetId**
> SlideGraphics slidesGraphicsGetId(id)

Graphics: Get by Id

Get by Id: Use this method to retrieve a Graphics object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlidesGraphicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SlidesGraphicsApi apiInstance = new SlidesGraphicsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      SlideGraphics result = apiInstance.slidesGraphicsGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlidesGraphicsApi#slidesGraphicsGetId");
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

[**SlideGraphics**](SlideGraphics.md)

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

