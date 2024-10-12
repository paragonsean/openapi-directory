# PaymentMethodsMerchantLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMerchantsMerchantIdPaymentMethodSettings**](PaymentMethodsMerchantLevelApi.md#getMerchantsMerchantIdPaymentMethodSettings) | **GET** /merchants/{merchantId}/paymentMethodSettings | Get all payment methods |
| [**getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId**](PaymentMethodsMerchantLevelApi.md#getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId) | **GET** /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId} | Get payment method details |
| [**getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomains**](PaymentMethodsMerchantLevelApi.md#getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomains) | **GET** /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/getApplePayDomains | Get Apple Pay domains |
| [**patchMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId**](PaymentMethodsMerchantLevelApi.md#patchMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId) | **PATCH** /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId} | Update a payment method |
| [**postMerchantsMerchantIdPaymentMethodSettings**](PaymentMethodsMerchantLevelApi.md#postMerchantsMerchantIdPaymentMethodSettings) | **POST** /merchants/{merchantId}/paymentMethodSettings | Request a payment method |
| [**postMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomains**](PaymentMethodsMerchantLevelApi.md#postMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomains) | **POST** /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/addApplePayDomains | Add an Apple Pay domain |


<a id="getMerchantsMerchantIdPaymentMethodSettings"></a>
# **getMerchantsMerchantIdPaymentMethodSettings**
> PaymentMethodResponse getMerchantsMerchantIdPaymentMethodSettings(merchantId, storeId, businessLineId, pageSize, pageNumber)

Get all payment methods

Returns details for all payment methods of the merchant account identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentMethodsMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PaymentMethodsMerchantLevelApi apiInstance = new PaymentMethodsMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    String storeId = "storeId_example"; // String | The unique identifier of the store for which to return the payment methods.
    String businessLineId = "businessLineId_example"; // String | The unique identifier of the Business Line for which to return the payment methods.
    Integer pageSize = 56; // Integer | The number of items to have on a page, maximum 100. The default is 10 items on a page.
    Integer pageNumber = 56; // Integer | The number of the page to fetch.
    try {
      PaymentMethodResponse result = apiInstance.getMerchantsMerchantIdPaymentMethodSettings(merchantId, storeId, businessLineId, pageSize, pageNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentMethodsMerchantLevelApi#getMerchantsMerchantIdPaymentMethodSettings");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **storeId** | **String**| The unique identifier of the store for which to return the payment methods. | [optional] |
| **businessLineId** | **String**| The unique identifier of the Business Line for which to return the payment methods. | [optional] |
| **pageSize** | **Integer**| The number of items to have on a page, maximum 100. The default is 10 items on a page. | [optional] |
| **pageNumber** | **Integer**| The number of the page to fetch. | [optional] |

### Return type

[**PaymentMethodResponse**](PaymentMethodResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **429** |  |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId"></a>
# **getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId**
> PaymentMethod getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId(merchantId, paymentMethodId)

Get payment method details

Returns details for the merchant account and the payment method identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentMethodsMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PaymentMethodsMerchantLevelApi apiInstance = new PaymentMethodsMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    String paymentMethodId = "paymentMethodId_example"; // String | The unique identifier of the payment method.
    try {
      PaymentMethod result = apiInstance.getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId(merchantId, paymentMethodId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentMethodsMerchantLevelApi#getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **paymentMethodId** | **String**| The unique identifier of the payment method. | |

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **429** |  |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomains"></a>
# **getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomains**
> ApplePayInfo getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomains(merchantId, paymentMethodId)

Get Apple Pay domains

Returns all Apple Pay domains that are registered with the merchant account and the payment method identified in the path. For more information, see [Apple Pay documentation](https://docs.adyen.com/payment-methods/apple-pay/enable-apple-pay#register-merchant-domain).  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentMethodsMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PaymentMethodsMerchantLevelApi apiInstance = new PaymentMethodsMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    String paymentMethodId = "paymentMethodId_example"; // String | The unique identifier of the payment method.
    try {
      ApplePayInfo result = apiInstance.getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomains(merchantId, paymentMethodId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentMethodsMerchantLevelApi#getMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomains");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **paymentMethodId** | **String**| The unique identifier of the payment method. | |

### Return type

[**ApplePayInfo**](ApplePayInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="patchMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId"></a>
# **patchMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId**
> PaymentMethod patchMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId(merchantId, paymentMethodId, updatePaymentMethodInfo)

Update a payment method

Updates payment method details for the merchant account and the payment method identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read and write 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentMethodsMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PaymentMethodsMerchantLevelApi apiInstance = new PaymentMethodsMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    String paymentMethodId = "paymentMethodId_example"; // String | The unique identifier of the payment method.
    UpdatePaymentMethodInfo updatePaymentMethodInfo = new UpdatePaymentMethodInfo(); // UpdatePaymentMethodInfo | 
    try {
      PaymentMethod result = apiInstance.patchMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId(merchantId, paymentMethodId, updatePaymentMethodInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentMethodsMerchantLevelApi#patchMerchantsMerchantIdPaymentMethodSettingsPaymentMethodId");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **paymentMethodId** | **String**| The unique identifier of the payment method. | |
| **updatePaymentMethodInfo** | [**UpdatePaymentMethodInfo**](UpdatePaymentMethodInfo.md)|  | [optional] |

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **429** |  |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postMerchantsMerchantIdPaymentMethodSettings"></a>
# **postMerchantsMerchantIdPaymentMethodSettings**
> PaymentMethod postMerchantsMerchantIdPaymentMethodSettings(merchantId, paymentMethodSetupInfo)

Request a payment method

Sends a request to add a new payment method to the merchant account identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read and write 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentMethodsMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PaymentMethodsMerchantLevelApi apiInstance = new PaymentMethodsMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    PaymentMethodSetupInfo paymentMethodSetupInfo = new PaymentMethodSetupInfo(); // PaymentMethodSetupInfo | 
    try {
      PaymentMethod result = apiInstance.postMerchantsMerchantIdPaymentMethodSettings(merchantId, paymentMethodSetupInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentMethodsMerchantLevelApi#postMerchantsMerchantIdPaymentMethodSettings");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **paymentMethodSetupInfo** | [**PaymentMethodSetupInfo**](PaymentMethodSetupInfo.md)|  | [optional] |

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **429** |  |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomains"></a>
# **postMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomains**
> postMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomains(merchantId, paymentMethodId, applePayInfo)

Add an Apple Pay domain

Adds the new domain to the list of Apple Pay domains that are registered with the merchant account and the payment method identified in the path. For more information, see [Apple Pay documentation](https://docs.adyen.com/payment-methods/apple-pay/enable-apple-pay#register-merchant-domain).  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read and write 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentMethodsMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PaymentMethodsMerchantLevelApi apiInstance = new PaymentMethodsMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    String paymentMethodId = "paymentMethodId_example"; // String | The unique identifier of the payment method.
    ApplePayInfo applePayInfo = new ApplePayInfo(); // ApplePayInfo | 
    try {
      apiInstance.postMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomains(merchantId, paymentMethodId, applePayInfo);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentMethodsMerchantLevelApi#postMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomains");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **paymentMethodId** | **String**| The unique identifier of the payment method. | |
| **applePayInfo** | [**ApplePayInfo**](ApplePayInfo.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content - look at the actual response code for the status of the request.  |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **429** |  |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

