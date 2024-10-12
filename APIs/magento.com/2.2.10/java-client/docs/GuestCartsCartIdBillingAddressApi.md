# GuestCartsCartIdBillingAddressApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteGuestBillingAddressManagementV1AssignPost**](GuestCartsCartIdBillingAddressApi.md#quoteGuestBillingAddressManagementV1AssignPost) | **POST** /V1/guest-carts/{cartId}/billing-address | guest-carts/{cartId}/billing-address |
| [**quoteGuestBillingAddressManagementV1GetGet**](GuestCartsCartIdBillingAddressApi.md#quoteGuestBillingAddressManagementV1GetGet) | **GET** /V1/guest-carts/{cartId}/billing-address | guest-carts/{cartId}/billing-address |


<a id="quoteGuestBillingAddressManagementV1AssignPost"></a>
# **quoteGuestBillingAddressManagementV1AssignPost**
> Integer quoteGuestBillingAddressManagementV1AssignPost(cartId, quoteBillingAddressManagementV1AssignPostRequest)

guest-carts/{cartId}/billing-address

Assign a specified billing address to a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdBillingAddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdBillingAddressApi apiInstance = new GuestCartsCartIdBillingAddressApi(defaultClient);
    String cartId = "cartId_example"; // String | The cart ID.
    QuoteBillingAddressManagementV1AssignPostRequest quoteBillingAddressManagementV1AssignPostRequest = new QuoteBillingAddressManagementV1AssignPostRequest(); // QuoteBillingAddressManagementV1AssignPostRequest | 
    try {
      Integer result = apiInstance.quoteGuestBillingAddressManagementV1AssignPost(cartId, quoteBillingAddressManagementV1AssignPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdBillingAddressApi#quoteGuestBillingAddressManagementV1AssignPost");
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
| **quoteBillingAddressManagementV1AssignPostRequest** | [**QuoteBillingAddressManagementV1AssignPostRequest**](QuoteBillingAddressManagementV1AssignPostRequest.md)|  | [optional] |

### Return type

**Integer**

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
| **0** | Unexpected error |  -  |

<a id="quoteGuestBillingAddressManagementV1GetGet"></a>
# **quoteGuestBillingAddressManagementV1GetGet**
> QuoteDataAddressInterface quoteGuestBillingAddressManagementV1GetGet(cartId)

guest-carts/{cartId}/billing-address

Return the billing address for a specified quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdBillingAddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdBillingAddressApi apiInstance = new GuestCartsCartIdBillingAddressApi(defaultClient);
    String cartId = "cartId_example"; // String | The cart ID.
    try {
      QuoteDataAddressInterface result = apiInstance.quoteGuestBillingAddressManagementV1GetGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdBillingAddressApi#quoteGuestBillingAddressManagementV1GetGet");
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

### Return type

[**QuoteDataAddressInterface**](QuoteDataAddressInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **0** | Unexpected error |  -  |

