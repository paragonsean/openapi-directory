# CartsMineSelectedPaymentMethodApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quotePaymentMethodManagementV1GetGet**](CartsMineSelectedPaymentMethodApi.md#quotePaymentMethodManagementV1GetGet) | **GET** /V1/carts/mine/selected-payment-method | carts/mine/selected-payment-method |
| [**quotePaymentMethodManagementV1SetPut**](CartsMineSelectedPaymentMethodApi.md#quotePaymentMethodManagementV1SetPut) | **PUT** /V1/carts/mine/selected-payment-method | carts/mine/selected-payment-method |


<a id="quotePaymentMethodManagementV1GetGet"></a>
# **quotePaymentMethodManagementV1GetGet**
> QuoteDataPaymentInterface quotePaymentMethodManagementV1GetGet()

carts/mine/selected-payment-method

Returns the payment method for a specified shopping cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineSelectedPaymentMethodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineSelectedPaymentMethodApi apiInstance = new CartsMineSelectedPaymentMethodApi(defaultClient);
    try {
      QuoteDataPaymentInterface result = apiInstance.quotePaymentMethodManagementV1GetGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineSelectedPaymentMethodApi#quotePaymentMethodManagementV1GetGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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

<a id="quotePaymentMethodManagementV1SetPut"></a>
# **quotePaymentMethodManagementV1SetPut**
> String quotePaymentMethodManagementV1SetPut(quotePaymentMethodManagementV1SetPutRequest)

carts/mine/selected-payment-method

Adds a specified payment method to a specified shopping cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineSelectedPaymentMethodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineSelectedPaymentMethodApi apiInstance = new CartsMineSelectedPaymentMethodApi(defaultClient);
    QuotePaymentMethodManagementV1SetPutRequest quotePaymentMethodManagementV1SetPutRequest = new QuotePaymentMethodManagementV1SetPutRequest(); // QuotePaymentMethodManagementV1SetPutRequest | 
    try {
      String result = apiInstance.quotePaymentMethodManagementV1SetPut(quotePaymentMethodManagementV1SetPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineSelectedPaymentMethodApi#quotePaymentMethodManagementV1SetPut");
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

