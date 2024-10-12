# CartsCartIdEstimateShippingMethodsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CartsCartIdEstimateShippingMethodsPost**](CartsCartIdEstimateShippingMethodsApi.md#v1CartsCartIdEstimateShippingMethodsPost) | **POST** /V1/carts/{cartId}/estimate-shipping-methods | carts/{cartId}/estimate-shipping-methods |


<a id="v1CartsCartIdEstimateShippingMethodsPost"></a>
# **v1CartsCartIdEstimateShippingMethodsPost**
> List&lt;QuoteDataShippingMethodInterface&gt; v1CartsCartIdEstimateShippingMethodsPost(cartId, quoteShipmentEstimationV1EstimateByExtendedAddressPostRequest)

carts/{cartId}/estimate-shipping-methods

Estimate shipping by address and return list of available shipping methods

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdEstimateShippingMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdEstimateShippingMethodsApi apiInstance = new CartsCartIdEstimateShippingMethodsApi(defaultClient);
    String cartId = "cartId_example"; // String | 
    QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest quoteShipmentEstimationV1EstimateByExtendedAddressPostRequest = new QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest(); // QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest | 
    try {
      List<QuoteDataShippingMethodInterface> result = apiInstance.v1CartsCartIdEstimateShippingMethodsPost(cartId, quoteShipmentEstimationV1EstimateByExtendedAddressPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdEstimateShippingMethodsApi#v1CartsCartIdEstimateShippingMethodsPost");
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
| **cartId** | **String**|  | |
| **quoteShipmentEstimationV1EstimateByExtendedAddressPostRequest** | [**QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest**](QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest.md)|  | [optional] |

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

