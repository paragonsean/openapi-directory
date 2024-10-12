# GuestGiftregistryCartIdEstimateShippingMethodsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**giftRegistryGuestCartShippingMethodManagementV1EstimateByRegistryIdPost**](GuestGiftregistryCartIdEstimateShippingMethodsApi.md#giftRegistryGuestCartShippingMethodManagementV1EstimateByRegistryIdPost) | **POST** /V1/guest-giftregistry/{cartId}/estimate-shipping-methods | guest-giftregistry/{cartId}/estimate-shipping-methods |


<a id="giftRegistryGuestCartShippingMethodManagementV1EstimateByRegistryIdPost"></a>
# **giftRegistryGuestCartShippingMethodManagementV1EstimateByRegistryIdPost**
> List&lt;QuoteDataShippingMethodInterface&gt; giftRegistryGuestCartShippingMethodManagementV1EstimateByRegistryIdPost(cartId, giftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest)

guest-giftregistry/{cartId}/estimate-shipping-methods

Estimate shipping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestGiftregistryCartIdEstimateShippingMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestGiftregistryCartIdEstimateShippingMethodsApi apiInstance = new GuestGiftregistryCartIdEstimateShippingMethodsApi(defaultClient);
    String cartId = "cartId_example"; // String | The shopping cart ID.
    GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest giftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest = new GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest(); // GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest | 
    try {
      List<QuoteDataShippingMethodInterface> result = apiInstance.giftRegistryGuestCartShippingMethodManagementV1EstimateByRegistryIdPost(cartId, giftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestGiftregistryCartIdEstimateShippingMethodsApi#giftRegistryGuestCartShippingMethodManagementV1EstimateByRegistryIdPost");
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
| **cartId** | **String**| The shopping cart ID. | |
| **giftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest** | [**GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest**](GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest.md)|  | [optional] |

### Return type

[**List&lt;QuoteDataShippingMethodInterface&gt;**](QuoteDataShippingMethodInterface.md)

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
| **0** | Unexpected error |  -  |

