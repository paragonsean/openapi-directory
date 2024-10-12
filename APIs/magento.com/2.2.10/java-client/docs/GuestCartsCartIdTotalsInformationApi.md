# GuestCartsCartIdTotalsInformationApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkoutGuestTotalsInformationManagementV1CalculatePost**](GuestCartsCartIdTotalsInformationApi.md#checkoutGuestTotalsInformationManagementV1CalculatePost) | **POST** /V1/guest-carts/{cartId}/totals-information | guest-carts/{cartId}/totals-information |


<a id="checkoutGuestTotalsInformationManagementV1CalculatePost"></a>
# **checkoutGuestTotalsInformationManagementV1CalculatePost**
> QuoteDataTotalsInterface checkoutGuestTotalsInformationManagementV1CalculatePost(cartId, checkoutTotalsInformationManagementV1CalculatePostRequest)

guest-carts/{cartId}/totals-information

Calculate quote totals based on address and shipping method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdTotalsInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdTotalsInformationApi apiInstance = new GuestCartsCartIdTotalsInformationApi(defaultClient);
    String cartId = "cartId_example"; // String | 
    CheckoutTotalsInformationManagementV1CalculatePostRequest checkoutTotalsInformationManagementV1CalculatePostRequest = new CheckoutTotalsInformationManagementV1CalculatePostRequest(); // CheckoutTotalsInformationManagementV1CalculatePostRequest | 
    try {
      QuoteDataTotalsInterface result = apiInstance.checkoutGuestTotalsInformationManagementV1CalculatePost(cartId, checkoutTotalsInformationManagementV1CalculatePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdTotalsInformationApi#checkoutGuestTotalsInformationManagementV1CalculatePost");
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
| **0** | Unexpected error |  -  |

