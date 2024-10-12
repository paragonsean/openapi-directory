# CartsMineTotalsInformationApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkoutTotalsInformationManagementV1CalculatePost**](CartsMineTotalsInformationApi.md#checkoutTotalsInformationManagementV1CalculatePost) | **POST** /V1/carts/mine/totals-information | carts/mine/totals-information |


<a id="checkoutTotalsInformationManagementV1CalculatePost"></a>
# **checkoutTotalsInformationManagementV1CalculatePost**
> QuoteDataTotalsInterface checkoutTotalsInformationManagementV1CalculatePost(checkoutTotalsInformationManagementV1CalculatePostRequest)

carts/mine/totals-information

Calculate quote totals based on address and shipping method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineTotalsInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineTotalsInformationApi apiInstance = new CartsMineTotalsInformationApi(defaultClient);
    CheckoutTotalsInformationManagementV1CalculatePostRequest checkoutTotalsInformationManagementV1CalculatePostRequest = new CheckoutTotalsInformationManagementV1CalculatePostRequest(); // CheckoutTotalsInformationManagementV1CalculatePostRequest | 
    try {
      QuoteDataTotalsInterface result = apiInstance.checkoutTotalsInformationManagementV1CalculatePost(checkoutTotalsInformationManagementV1CalculatePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineTotalsInformationApi#checkoutTotalsInformationManagementV1CalculatePost");
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

