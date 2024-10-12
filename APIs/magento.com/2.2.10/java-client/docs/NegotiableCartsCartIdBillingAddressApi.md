# NegotiableCartsCartIdBillingAddressApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**negotiableQuoteBillingAddressManagementV1AssignPost**](NegotiableCartsCartIdBillingAddressApi.md#negotiableQuoteBillingAddressManagementV1AssignPost) | **POST** /V1/negotiable-carts/{cartId}/billing-address | negotiable-carts/{cartId}/billing-address |
| [**negotiableQuoteBillingAddressManagementV1GetGet**](NegotiableCartsCartIdBillingAddressApi.md#negotiableQuoteBillingAddressManagementV1GetGet) | **GET** /V1/negotiable-carts/{cartId}/billing-address | negotiable-carts/{cartId}/billing-address |


<a id="negotiableQuoteBillingAddressManagementV1AssignPost"></a>
# **negotiableQuoteBillingAddressManagementV1AssignPost**
> Integer negotiableQuoteBillingAddressManagementV1AssignPost(cartId, quoteBillingAddressManagementV1AssignPostRequest)

negotiable-carts/{cartId}/billing-address

Assigns a specified billing address to a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegotiableCartsCartIdBillingAddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    NegotiableCartsCartIdBillingAddressApi apiInstance = new NegotiableCartsCartIdBillingAddressApi(defaultClient);
    Integer cartId = 56; // Integer | The cart ID.
    QuoteBillingAddressManagementV1AssignPostRequest quoteBillingAddressManagementV1AssignPostRequest = new QuoteBillingAddressManagementV1AssignPostRequest(); // QuoteBillingAddressManagementV1AssignPostRequest | 
    try {
      Integer result = apiInstance.negotiableQuoteBillingAddressManagementV1AssignPost(cartId, quoteBillingAddressManagementV1AssignPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegotiableCartsCartIdBillingAddressApi#negotiableQuoteBillingAddressManagementV1AssignPost");
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
| **cartId** | **Integer**| The cart ID. | |
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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="negotiableQuoteBillingAddressManagementV1GetGet"></a>
# **negotiableQuoteBillingAddressManagementV1GetGet**
> QuoteDataAddressInterface negotiableQuoteBillingAddressManagementV1GetGet(cartId)

negotiable-carts/{cartId}/billing-address

Returns the billing address for a specified quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegotiableCartsCartIdBillingAddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    NegotiableCartsCartIdBillingAddressApi apiInstance = new NegotiableCartsCartIdBillingAddressApi(defaultClient);
    Integer cartId = 56; // Integer | The cart ID.
    try {
      QuoteDataAddressInterface result = apiInstance.negotiableQuoteBillingAddressManagementV1GetGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegotiableCartsCartIdBillingAddressApi#negotiableQuoteBillingAddressManagementV1GetGet");
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
| **cartId** | **Integer**| The cart ID. | |

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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

