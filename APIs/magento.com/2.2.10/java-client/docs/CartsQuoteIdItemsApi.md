# CartsQuoteIdItemsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CartsQuoteIdItemsPost**](CartsQuoteIdItemsApi.md#v1CartsQuoteIdItemsPost) | **POST** /V1/carts/{quoteId}/items | carts/{quoteId}/items |


<a id="v1CartsQuoteIdItemsPost"></a>
# **v1CartsQuoteIdItemsPost**
> QuoteDataCartItemInterface v1CartsQuoteIdItemsPost(quoteId, quoteCartItemRepositoryV1SavePostRequest)

carts/{quoteId}/items

Add/update the specified cart item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsQuoteIdItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsQuoteIdItemsApi apiInstance = new CartsQuoteIdItemsApi(defaultClient);
    String quoteId = "quoteId_example"; // String | 
    QuoteCartItemRepositoryV1SavePostRequest quoteCartItemRepositoryV1SavePostRequest = new QuoteCartItemRepositoryV1SavePostRequest(); // QuoteCartItemRepositoryV1SavePostRequest | 
    try {
      QuoteDataCartItemInterface result = apiInstance.v1CartsQuoteIdItemsPost(quoteId, quoteCartItemRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsQuoteIdItemsApi#v1CartsQuoteIdItemsPost");
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
| **quoteId** | **String**|  | |
| **quoteCartItemRepositoryV1SavePostRequest** | [**QuoteCartItemRepositoryV1SavePostRequest**](QuoteCartItemRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**QuoteDataCartItemInterface**](QuoteDataCartItemInterface.md)

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

