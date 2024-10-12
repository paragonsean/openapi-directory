# GiftregistryMineEstimateShippingMethodsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**giftRegistryShippingMethodManagementV1EstimateByRegistryIdPost**](GiftregistryMineEstimateShippingMethodsApi.md#giftRegistryShippingMethodManagementV1EstimateByRegistryIdPost) | **POST** /V1/giftregistry/mine/estimate-shipping-methods | giftregistry/mine/estimate-shipping-methods |


<a id="giftRegistryShippingMethodManagementV1EstimateByRegistryIdPost"></a>
# **giftRegistryShippingMethodManagementV1EstimateByRegistryIdPost**
> List&lt;QuoteDataShippingMethodInterface&gt; giftRegistryShippingMethodManagementV1EstimateByRegistryIdPost(giftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest)

giftregistry/mine/estimate-shipping-methods

Estimate shipping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GiftregistryMineEstimateShippingMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GiftregistryMineEstimateShippingMethodsApi apiInstance = new GiftregistryMineEstimateShippingMethodsApi(defaultClient);
    GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest giftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest = new GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest(); // GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest | 
    try {
      List<QuoteDataShippingMethodInterface> result = apiInstance.giftRegistryShippingMethodManagementV1EstimateByRegistryIdPost(giftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GiftregistryMineEstimateShippingMethodsApi#giftRegistryShippingMethodManagementV1EstimateByRegistryIdPost");
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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

