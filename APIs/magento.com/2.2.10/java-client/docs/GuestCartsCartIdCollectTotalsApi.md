# GuestCartsCartIdCollectTotalsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteGuestCartTotalManagementV1CollectTotalsPut**](GuestCartsCartIdCollectTotalsApi.md#quoteGuestCartTotalManagementV1CollectTotalsPut) | **PUT** /V1/guest-carts/{cartId}/collect-totals | guest-carts/{cartId}/collect-totals |


<a id="quoteGuestCartTotalManagementV1CollectTotalsPut"></a>
# **quoteGuestCartTotalManagementV1CollectTotalsPut**
> QuoteDataTotalsInterface quoteGuestCartTotalManagementV1CollectTotalsPut(cartId, quoteCartTotalManagementV1CollectTotalsPutRequest)

guest-carts/{cartId}/collect-totals

Set shipping/billing methods and additional data for cart and collect totals for guest.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdCollectTotalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdCollectTotalsApi apiInstance = new GuestCartsCartIdCollectTotalsApi(defaultClient);
    String cartId = "cartId_example"; // String | The cart ID.
    QuoteCartTotalManagementV1CollectTotalsPutRequest quoteCartTotalManagementV1CollectTotalsPutRequest = new QuoteCartTotalManagementV1CollectTotalsPutRequest(); // QuoteCartTotalManagementV1CollectTotalsPutRequest | 
    try {
      QuoteDataTotalsInterface result = apiInstance.quoteGuestCartTotalManagementV1CollectTotalsPut(cartId, quoteCartTotalManagementV1CollectTotalsPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdCollectTotalsApi#quoteGuestCartTotalManagementV1CollectTotalsPut");
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
| **cartId** | **String**| The cart ID. | |
| **quoteCartTotalManagementV1CollectTotalsPutRequest** | [**QuoteCartTotalManagementV1CollectTotalsPutRequest**](QuoteCartTotalManagementV1CollectTotalsPutRequest.md)|  | [optional] |

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

