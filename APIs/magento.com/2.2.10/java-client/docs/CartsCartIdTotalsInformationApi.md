# CartsCartIdTotalsInformationApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CartsCartIdTotalsInformationPost**](CartsCartIdTotalsInformationApi.md#v1CartsCartIdTotalsInformationPost) | **POST** /V1/carts/{cartId}/totals-information | carts/{cartId}/totals-information |


<a id="v1CartsCartIdTotalsInformationPost"></a>
# **v1CartsCartIdTotalsInformationPost**
> QuoteDataTotalsInterface v1CartsCartIdTotalsInformationPost(cartId, checkoutTotalsInformationManagementV1CalculatePostRequest)

carts/{cartId}/totals-information

Calculate quote totals based on address and shipping method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdTotalsInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdTotalsInformationApi apiInstance = new CartsCartIdTotalsInformationApi(defaultClient);
    Integer cartId = 56; // Integer | 
    CheckoutTotalsInformationManagementV1CalculatePostRequest checkoutTotalsInformationManagementV1CalculatePostRequest = new CheckoutTotalsInformationManagementV1CalculatePostRequest(); // CheckoutTotalsInformationManagementV1CalculatePostRequest | 
    try {
      QuoteDataTotalsInterface result = apiInstance.v1CartsCartIdTotalsInformationPost(cartId, checkoutTotalsInformationManagementV1CalculatePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdTotalsInformationApi#v1CartsCartIdTotalsInformationPost");
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
| **cartId** | **Integer**|  | |
| **checkoutTotalsInformationManagementV1CalculatePostRequest** | [**CheckoutTotalsInformationManagementV1CalculatePostRequest**](CheckoutTotalsInformationManagementV1CalculatePostRequest.md)|  | [optional] |

### Return type

[**QuoteDataTotalsInterface**](QuoteDataTotalsInterface.md)

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

