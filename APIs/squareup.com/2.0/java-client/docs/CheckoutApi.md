# CheckoutApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCheckout**](CheckoutApi.md#createCheckout) | **POST** /v2/locations/{location_id}/checkouts | CreateCheckout |


<a id="createCheckout"></a>
# **createCheckout**
> CreateCheckoutResponse createCheckout(locationId, createCheckoutRequest)

CreateCheckout

Links a &#x60;checkoutId&#x60; to a &#x60;checkout_page_url&#x60; that customers are directed to in order to provide their payment information using a payment processing workflow hosted on connect.squareup.com.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CheckoutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CheckoutApi apiInstance = new CheckoutApi(defaultClient);
    String locationId = "locationId_example"; // String | The ID of the business location to associate the checkout with.
    CreateCheckoutRequest createCheckoutRequest = new CreateCheckoutRequest(); // CreateCheckoutRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      CreateCheckoutResponse result = apiInstance.createCheckout(locationId, createCheckoutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CheckoutApi#createCheckout");
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
| **locationId** | **String**| The ID of the business location to associate the checkout with. | |
| **createCheckoutRequest** | [**CreateCheckoutRequest**](CreateCheckoutRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**CreateCheckoutResponse**](CreateCheckoutResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

