# CartsMineEstimateShippingMethodsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteShipmentEstimationV1EstimateByExtendedAddressPost**](CartsMineEstimateShippingMethodsApi.md#quoteShipmentEstimationV1EstimateByExtendedAddressPost) | **POST** /V1/carts/mine/estimate-shipping-methods | carts/mine/estimate-shipping-methods |


<a id="quoteShipmentEstimationV1EstimateByExtendedAddressPost"></a>
# **quoteShipmentEstimationV1EstimateByExtendedAddressPost**
> List&lt;QuoteDataShippingMethodInterface&gt; quoteShipmentEstimationV1EstimateByExtendedAddressPost(quoteShipmentEstimationV1EstimateByExtendedAddressPostRequest)

carts/mine/estimate-shipping-methods

Estimate shipping by address and return list of available shipping methods

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineEstimateShippingMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineEstimateShippingMethodsApi apiInstance = new CartsMineEstimateShippingMethodsApi(defaultClient);
    QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest quoteShipmentEstimationV1EstimateByExtendedAddressPostRequest = new QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest(); // QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest | 
    try {
      List<QuoteDataShippingMethodInterface> result = apiInstance.quoteShipmentEstimationV1EstimateByExtendedAddressPost(quoteShipmentEstimationV1EstimateByExtendedAddressPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineEstimateShippingMethodsApi#quoteShipmentEstimationV1EstimateByExtendedAddressPost");
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

