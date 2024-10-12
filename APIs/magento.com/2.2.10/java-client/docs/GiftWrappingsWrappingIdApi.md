# GiftWrappingsWrappingIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**giftWrappingWrappingRepositoryV1SavePut**](GiftWrappingsWrappingIdApi.md#giftWrappingWrappingRepositoryV1SavePut) | **PUT** /V1/gift-wrappings/{wrappingId} | gift-wrappings/{wrappingId} |


<a id="giftWrappingWrappingRepositoryV1SavePut"></a>
# **giftWrappingWrappingRepositoryV1SavePut**
> GiftWrappingDataWrappingInterface giftWrappingWrappingRepositoryV1SavePut(wrappingId, giftWrappingWrappingRepositoryV1SavePostRequest)

gift-wrappings/{wrappingId}

Create/Update new gift wrapping with data object values

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GiftWrappingsWrappingIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GiftWrappingsWrappingIdApi apiInstance = new GiftWrappingsWrappingIdApi(defaultClient);
    String wrappingId = "wrappingId_example"; // String | 
    GiftWrappingWrappingRepositoryV1SavePostRequest giftWrappingWrappingRepositoryV1SavePostRequest = new GiftWrappingWrappingRepositoryV1SavePostRequest(); // GiftWrappingWrappingRepositoryV1SavePostRequest | 
    try {
      GiftWrappingDataWrappingInterface result = apiInstance.giftWrappingWrappingRepositoryV1SavePut(wrappingId, giftWrappingWrappingRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GiftWrappingsWrappingIdApi#giftWrappingWrappingRepositoryV1SavePut");
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
| **wrappingId** | **String**|  | |
| **giftWrappingWrappingRepositoryV1SavePostRequest** | [**GiftWrappingWrappingRepositoryV1SavePostRequest**](GiftWrappingWrappingRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**GiftWrappingDataWrappingInterface**](GiftWrappingDataWrappingInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

