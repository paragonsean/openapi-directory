# CartsCartIdEstimateShippingMethodsByAddressIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CartsCartIdEstimateShippingMethodsByAddressIdPost**](CartsCartIdEstimateShippingMethodsByAddressIdApi.md#v1CartsCartIdEstimateShippingMethodsByAddressIdPost) | **POST** /V1/carts/{cartId}/estimate-shipping-methods-by-address-id | carts/{cartId}/estimate-shipping-methods-by-address-id |


<a id="v1CartsCartIdEstimateShippingMethodsByAddressIdPost"></a>
# **v1CartsCartIdEstimateShippingMethodsByAddressIdPost**
> List&lt;QuoteDataShippingMethodInterface&gt; v1CartsCartIdEstimateShippingMethodsByAddressIdPost(cartId, quoteShippingMethodManagementV1EstimateByAddressIdPostRequest)

carts/{cartId}/estimate-shipping-methods-by-address-id

Estimate shipping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdEstimateShippingMethodsByAddressIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdEstimateShippingMethodsByAddressIdApi apiInstance = new CartsCartIdEstimateShippingMethodsByAddressIdApi(defaultClient);
    Integer cartId = 56; // Integer | The shopping cart ID.
    QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest quoteShippingMethodManagementV1EstimateByAddressIdPostRequest = new QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest(); // QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest | 
    try {
      List<QuoteDataShippingMethodInterface> result = apiInstance.v1CartsCartIdEstimateShippingMethodsByAddressIdPost(cartId, quoteShippingMethodManagementV1EstimateByAddressIdPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdEstimateShippingMethodsByAddressIdApi#v1CartsCartIdEstimateShippingMethodsByAddressIdPost");
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
| **cartId** | **Integer**| The shopping cart ID. | |
| **quoteShippingMethodManagementV1EstimateByAddressIdPostRequest** | [**QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest**](QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest.md)|  | [optional] |

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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

