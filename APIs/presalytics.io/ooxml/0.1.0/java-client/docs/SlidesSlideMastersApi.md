# SlidesSlideMastersApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**slidesSlidemastersGetId**](SlidesSlideMastersApi.md#slidesSlidemastersGetId) | **GET** /Slides/SlideMasters/{id} | SlideMasters: Get by Id |


<a id="slidesSlidemastersGetId"></a>
# **slidesSlidemastersGetId**
> SlideSlideMasters slidesSlidemastersGetId(id)

SlideMasters: Get by Id

Get by Id: Use this method to retrieve a SlideMasters object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlidesSlideMastersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SlidesSlideMastersApi apiInstance = new SlidesSlideMastersApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      SlideSlideMasters result = apiInstance.slidesSlidemastersGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlidesSlideMastersApi#slidesSlidemastersGetId");
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

[**SlideSlideMasters**](SlideSlideMasters.md)

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

