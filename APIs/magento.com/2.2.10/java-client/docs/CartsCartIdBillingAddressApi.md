# CartsCartIdBillingAddressApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CartsCartIdBillingAddressGet**](CartsCartIdBillingAddressApi.md#v1CartsCartIdBillingAddressGet) | **GET** /V1/carts/{cartId}/billing-address | carts/{cartId}/billing-address |
| [**v1CartsCartIdBillingAddressPost**](CartsCartIdBillingAddressApi.md#v1CartsCartIdBillingAddressPost) | **POST** /V1/carts/{cartId}/billing-address | carts/{cartId}/billing-address |


<a id="v1CartsCartIdBillingAddressGet"></a>
# **v1CartsCartIdBillingAddressGet**
> QuoteDataAddressInterface v1CartsCartIdBillingAddressGet(cartId)

carts/{cartId}/billing-address

Returns the billing address for a specified quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdBillingAddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdBillingAddressApi apiInstance = new CartsCartIdBillingAddressApi(defaultClient);
    Integer cartId = 56; // Integer | The cart ID.
    try {
      QuoteDataAddressInterface result = apiInstance.v1CartsCartIdBillingAddressGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdBillingAddressApi#v1CartsCartIdBillingAddressGet");
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

<a id="v1CartsCartIdBillingAddressPost"></a>
# **v1CartsCartIdBillingAddressPost**
> Integer v1CartsCartIdBillingAddressPost(cartId, quoteBillingAddressManagementV1AssignPostRequest)

carts/{cartId}/billing-address

Assigns a specified billing address to a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdBillingAddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdBillingAddressApi apiInstance = new CartsCartIdBillingAddressApi(defaultClient);
    Integer cartId = 56; // Integer | The cart ID.
    QuoteBillingAddressManagementV1AssignPostRequest quoteBillingAddressManagementV1AssignPostRequest = new QuoteBillingAddressManagementV1AssignPostRequest(); // QuoteBillingAddressManagementV1AssignPostRequest | 
    try {
      Integer result = apiInstance.v1CartsCartIdBillingAddressPost(cartId, quoteBillingAddressManagementV1AssignPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdBillingAddressApi#v1CartsCartIdBillingAddressPost");
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

