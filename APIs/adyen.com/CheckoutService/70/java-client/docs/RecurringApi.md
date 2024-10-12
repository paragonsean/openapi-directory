# RecurringApi

All URIs are relative to *https://checkout-test.adyen.com/v70*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteStoredPaymentMethodsStoredPaymentMethodId**](RecurringApi.md#deleteStoredPaymentMethodsStoredPaymentMethodId) | **DELETE** /storedPaymentMethods/{storedPaymentMethodId} | Delete a token for stored payment details |
| [**getStoredPaymentMethods**](RecurringApi.md#getStoredPaymentMethods) | **GET** /storedPaymentMethods | Get tokens for stored payment details |


<a id="deleteStoredPaymentMethodsStoredPaymentMethodId"></a>
# **deleteStoredPaymentMethodsStoredPaymentMethodId**
> deleteStoredPaymentMethodsStoredPaymentMethodId(storedPaymentMethodId, shopperReference, merchantAccount)

Delete a token for stored payment details

Deletes the token identified in the path. The token can no longer be used with payment requests.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecurringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://checkout-test.adyen.com/v70");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    RecurringApi apiInstance = new RecurringApi(defaultClient);
    String storedPaymentMethodId = "storedPaymentMethodId_example"; // String | The unique identifier of the token.
    String shopperReference = "shopperReference_example"; // String | Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. > Your reference must not include personally identifiable information (PII), for example name or email address.
    String merchantAccount = "merchantAccount_example"; // String | Your merchant account.
    try {
      apiInstance.deleteStoredPaymentMethodsStoredPaymentMethodId(storedPaymentMethodId, shopperReference, merchantAccount);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecurringApi#deleteStoredPaymentMethodsStoredPaymentMethodId");
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
| **storedPaymentMethodId** | **String**| The unique identifier of the token. | |
| **shopperReference** | **String**| Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. &gt; Your reference must not include personally identifiable information (PII), for example name or email address. | |
| **merchantAccount** | **String**| Your merchant account. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content - look at the actual response code for the status of the request.  |  -  |

<a id="getStoredPaymentMethods"></a>
# **getStoredPaymentMethods**
> ListStoredPaymentMethodsResponse getStoredPaymentMethods(shopperReference, merchantAccount)

Get tokens for stored payment details

Lists the tokens for stored payment details for the shopper identified in the path, if there are any available. The token ID can be used with payment requests for the shopper&#39;s payment. A summary of the stored details is included.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecurringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://checkout-test.adyen.com/v70");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    RecurringApi apiInstance = new RecurringApi(defaultClient);
    String shopperReference = "shopperReference_example"; // String | Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. > Your reference must not include personally identifiable information (PII), for example name or email address.
    String merchantAccount = "merchantAccount_example"; // String | Your merchant account.
    try {
      ListStoredPaymentMethodsResponse result = apiInstance.getStoredPaymentMethods(shopperReference, merchantAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecurringApi#getStoredPaymentMethods");
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
| **shopperReference** | **String**| Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. &gt; Your reference must not include personally identifiable information (PII), for example name or email address. | [optional] |
| **merchantAccount** | **String**| Your merchant account. | [optional] |

### Return type

[**ListStoredPaymentMethodsResponse**](ListStoredPaymentMethodsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

