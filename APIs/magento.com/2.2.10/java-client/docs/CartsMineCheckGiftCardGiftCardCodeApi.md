# CartsMineCheckGiftCardGiftCardCodeApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**giftCardAccountGiftCardAccountManagementV1CheckGiftCardGet**](CartsMineCheckGiftCardGiftCardCodeApi.md#giftCardAccountGiftCardAccountManagementV1CheckGiftCardGet) | **GET** /V1/carts/mine/checkGiftCard/{giftCardCode} | carts/mine/checkGiftCard/{giftCardCode} |


<a id="giftCardAccountGiftCardAccountManagementV1CheckGiftCardGet"></a>
# **giftCardAccountGiftCardAccountManagementV1CheckGiftCardGet**
> BigDecimal giftCardAccountGiftCardAccountManagementV1CheckGiftCardGet(giftCardCode)

carts/mine/checkGiftCard/{giftCardCode}



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineCheckGiftCardGiftCardCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineCheckGiftCardGiftCardCodeApi apiInstance = new CartsMineCheckGiftCardGiftCardCodeApi(defaultClient);
    String giftCardCode = "giftCardCode_example"; // String | 
    try {
      BigDecimal result = apiInstance.giftCardAccountGiftCardAccountManagementV1CheckGiftCardGet(giftCardCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineCheckGiftCardGiftCardCodeApi#giftCardAccountGiftCardAccountManagementV1CheckGiftCardGet");
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
| **giftCardCode** | **String**|  | |

### Return type

[**BigDecimal**](BigDecimal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

