# CartsCartIdSelectedPaymentMethodApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CartsCartIdSelectedPaymentMethodGet**](CartsCartIdSelectedPaymentMethodApi.md#v1CartsCartIdSelectedPaymentMethodGet) | **GET** /V1/carts/{cartId}/selected-payment-method | carts/{cartId}/selected-payment-method |
| [**v1CartsCartIdSelectedPaymentMethodPut**](CartsCartIdSelectedPaymentMethodApi.md#v1CartsCartIdSelectedPaymentMethodPut) | **PUT** /V1/carts/{cartId}/selected-payment-method | carts/{cartId}/selected-payment-method |


<a id="v1CartsCartIdSelectedPaymentMethodGet"></a>
# **v1CartsCartIdSelectedPaymentMethodGet**
> QuoteDataPaymentInterface v1CartsCartIdSelectedPaymentMethodGet(cartId)

carts/{cartId}/selected-payment-method

Returns the payment method for a specified shopping cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdSelectedPaymentMethodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdSelectedPaymentMethodApi apiInstance = new CartsCartIdSelectedPaymentMethodApi(defaultClient);
    Integer cartId = 56; // Integer | The cart ID.
    try {
      QuoteDataPaymentInterface result = apiInstance.v1CartsCartIdSelectedPaymentMethodGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdSelectedPaymentMethodApi#v1CartsCartIdSelectedPaymentMethodGet");
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

[**QuoteDataPaymentInterface**](QuoteDataPaymentInterface.md)

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

<a id="v1CartsCartIdSelectedPaymentMethodPut"></a>
# **v1CartsCartIdSelectedPaymentMethodPut**
> String v1CartsCartIdSelectedPaymentMethodPut(cartId, quotePaymentMethodManagementV1SetPutRequest)

carts/{cartId}/selected-payment-method

Adds a specified payment method to a specified shopping cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdSelectedPaymentMethodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdSelectedPaymentMethodApi apiInstance = new CartsCartIdSelectedPaymentMethodApi(defaultClient);
    Integer cartId = 56; // Integer | The cart ID.
    QuotePaymentMethodManagementV1SetPutRequest quotePaymentMethodManagementV1SetPutRequest = new QuotePaymentMethodManagementV1SetPutRequest(); // QuotePaymentMethodManagementV1SetPutRequest | 
    try {
      String result = apiInstance.v1CartsCartIdSelectedPaymentMethodPut(cartId, quotePaymentMethodManagementV1SetPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdSelectedPaymentMethodApi#v1CartsCartIdSelectedPaymentMethodPut");
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
| **quotePaymentMethodManagementV1SetPutRequest** | [**QuotePaymentMethodManagementV1SetPutRequest**](QuotePaymentMethodManagementV1SetPutRequest.md)|  | [optional] |

### Return type

**String**

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

