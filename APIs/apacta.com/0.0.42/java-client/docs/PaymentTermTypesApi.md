# PaymentTermTypesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentTermTypesGet**](PaymentTermTypesApi.md#paymentTermTypesGet) | **GET** /payment_term_types | Get a list of payment term types |
| [**paymentTermTypesPaymentTermTypeIdGet**](PaymentTermTypesApi.md#paymentTermTypesPaymentTermTypeIdGet) | **GET** /payment_term_types/{payment_term_type_id} | Details of 1 payment term type |


<a id="paymentTermTypesGet"></a>
# **paymentTermTypesGet**
> PaymentTermTypesGet200Response paymentTermTypesGet()

Get a list of payment term types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentTermTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    PaymentTermTypesApi apiInstance = new PaymentTermTypesApi(defaultClient);
    try {
      PaymentTermTypesGet200Response result = apiInstance.paymentTermTypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentTermTypesApi#paymentTermTypesGet");
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

[**PaymentTermTypesGet200Response**](PaymentTermTypesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="paymentTermTypesPaymentTermTypeIdGet"></a>
# **paymentTermTypesPaymentTermTypeIdGet**
> PaymentTermTypesPaymentTermTypeIdGet200Response paymentTermTypesPaymentTermTypeIdGet(paymentTermTypeId)

Details of 1 payment term type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentTermTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    PaymentTermTypesApi apiInstance = new PaymentTermTypesApi(defaultClient);
    String paymentTermTypeId = "paymentTermTypeId_example"; // String | 
    try {
      PaymentTermTypesPaymentTermTypeIdGet200Response result = apiInstance.paymentTermTypesPaymentTermTypeIdGet(paymentTermTypeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentTermTypesApi#paymentTermTypesPaymentTermTypeIdGet");
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
| **paymentTermTypeId** | **String**|  | |

### Return type

[**PaymentTermTypesPaymentTermTypeIdGet200Response**](PaymentTermTypesPaymentTermTypeIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

