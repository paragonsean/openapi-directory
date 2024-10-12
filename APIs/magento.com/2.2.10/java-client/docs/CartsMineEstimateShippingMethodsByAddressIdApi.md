# CartsMineEstimateShippingMethodsByAddressIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteShippingMethodManagementV1EstimateByAddressIdPost**](CartsMineEstimateShippingMethodsByAddressIdApi.md#quoteShippingMethodManagementV1EstimateByAddressIdPost) | **POST** /V1/carts/mine/estimate-shipping-methods-by-address-id | carts/mine/estimate-shipping-methods-by-address-id |


<a id="quoteShippingMethodManagementV1EstimateByAddressIdPost"></a>
# **quoteShippingMethodManagementV1EstimateByAddressIdPost**
> List&lt;QuoteDataShippingMethodInterface&gt; quoteShippingMethodManagementV1EstimateByAddressIdPost(quoteShippingMethodManagementV1EstimateByAddressIdPostRequest)

carts/mine/estimate-shipping-methods-by-address-id

Estimate shipping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineEstimateShippingMethodsByAddressIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineEstimateShippingMethodsByAddressIdApi apiInstance = new CartsMineEstimateShippingMethodsByAddressIdApi(defaultClient);
    QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest quoteShippingMethodManagementV1EstimateByAddressIdPostRequest = new QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest(); // QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest | 
    try {
      List<QuoteDataShippingMethodInterface> result = apiInstance.quoteShippingMethodManagementV1EstimateByAddressIdPost(quoteShippingMethodManagementV1EstimateByAddressIdPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineEstimateShippingMethodsByAddressIdApi#quoteShippingMethodManagementV1EstimateByAddressIdPost");
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

