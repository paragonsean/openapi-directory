# CartsQuoteIdGiftCardsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**giftCardAccountGiftCardAccountManagementV1GetListByQuoteIdGet**](CartsQuoteIdGiftCardsApi.md#giftCardAccountGiftCardAccountManagementV1GetListByQuoteIdGet) | **GET** /V1/carts/{quoteId}/giftCards | carts/{quoteId}/giftCards |


<a id="giftCardAccountGiftCardAccountManagementV1GetListByQuoteIdGet"></a>
# **giftCardAccountGiftCardAccountManagementV1GetListByQuoteIdGet**
> GiftCardAccountDataGiftCardAccountInterface giftCardAccountGiftCardAccountManagementV1GetListByQuoteIdGet(quoteId)

carts/{quoteId}/giftCards

Return GiftCard Account cards

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsQuoteIdGiftCardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsQuoteIdGiftCardsApi apiInstance = new CartsQuoteIdGiftCardsApi(defaultClient);
    Integer quoteId = 56; // Integer | 
    try {
      GiftCardAccountDataGiftCardAccountInterface result = apiInstance.giftCardAccountGiftCardAccountManagementV1GetListByQuoteIdGet(quoteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsQuoteIdGiftCardsApi#giftCardAccountGiftCardAccountManagementV1GetListByQuoteIdGet");
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
| **quoteId** | **Integer**|  | |

### Return type

[**GiftCardAccountDataGiftCardAccountInterface**](GiftCardAccountDataGiftCardAccountInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

