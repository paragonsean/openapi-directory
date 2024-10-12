# DefaultApi

All URIs are relative to *https://modelpubsub.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV10SafeUnsafeImageWithTagsPost**](DefaultApi.md#apiV10SafeUnsafeImageWithTagsPost) | **POST** /api-v1.0/SafeUnsafeImageWithTags |  |


<a id="apiV10SafeUnsafeImageWithTagsPost"></a>
# **apiV10SafeUnsafeImageWithTagsPost**
> InlineResponse200 apiV10SafeUnsafeImageWithTagsPost(apiv10SafeUnsafeImageWithTagsBody)



Auto generated using Swagger Inspector

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://modelpubsub.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Apiv10SafeUnsafeImageWithTagsBody apiv10SafeUnsafeImageWithTagsBody = new Apiv10SafeUnsafeImageWithTagsBody(); // Apiv10SafeUnsafeImageWithTagsBody | 
    try {
      InlineResponse200 result = apiInstance.apiV10SafeUnsafeImageWithTagsPost(apiv10SafeUnsafeImageWithTagsBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV10SafeUnsafeImageWithTagsPost");
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
| **apiv10SafeUnsafeImageWithTagsBody** | [**Apiv10SafeUnsafeImageWithTagsBody**](Apiv10SafeUnsafeImageWithTagsBody.md)|  | [optional] |

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Auto generated using Swagger Inspector |  -  |

