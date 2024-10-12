# UtilityApi

All URIs are relative to *https://checkout-test.adyen.com/v50*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postApplePaySessions**](UtilityApi.md#postApplePaySessions) | **POST** /applePay/sessions | Get an Apple Pay session |
| [**postOriginKeys**](UtilityApi.md#postOriginKeys) | **POST** /originKeys | Create originKey values for domains |


<a id="postApplePaySessions"></a>
# **postApplePaySessions**
> ApplePaySessionResponse postApplePaySessions(idempotencyKey, applePaySessionRequest)

Get an Apple Pay session

You need to use this endpoint if you have an API-only integration with Apple Pay which uses Adyen&#39;s Apple Pay certificate.  The endpoint returns the Apple Pay session data which you need to complete the [Apple Pay session validation](https://docs.adyen.com/payment-methods/apple-pay/api-only?tab&#x3D;adyen-certificate-validation_1#complete-apple-pay-session-validation).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://checkout-test.adyen.com/v50");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    UtilityApi apiInstance = new UtilityApi(defaultClient);
    String idempotencyKey = "37ca9c97-d1d1-4c62-89e8-706891a563ed"; // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    ApplePaySessionRequest applePaySessionRequest = new ApplePaySessionRequest(); // ApplePaySessionRequest | 
    try {
      ApplePaySessionResponse result = apiInstance.postApplePaySessions(idempotencyKey, applePaySessionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilityApi#postApplePaySessions");
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
| **idempotencyKey** | **String**| A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). | [optional] |
| **applePaySessionRequest** | [**ApplePaySessionRequest**](ApplePaySessionRequest.md)|  | [optional] |

### Return type

[**ApplePaySessionResponse**](ApplePaySessionResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  * Idempotency-Key -  <br>  |

<a id="postOriginKeys"></a>
# **postOriginKeys**
> UtilityResponse postOriginKeys(idempotencyKey, utilityRequest)

Create originKey values for domains

This operation takes the origin domains and returns a JSON object containing the corresponding origin keys for the domains.  &gt; If you&#39;re still using origin key for your Web Drop-in or Components integration, we recommend [switching to client key](https://docs.adyen.com/development-resources/client-side-authentication/migrate-from-origin-key-to-client-key). This allows you to use a single key for all origins, add or remove origins without generating a new key, and detect the card type from the number entered in your payment form. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://checkout-test.adyen.com/v50");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    UtilityApi apiInstance = new UtilityApi(defaultClient);
    String idempotencyKey = "37ca9c97-d1d1-4c62-89e8-706891a563ed"; // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    UtilityRequest utilityRequest = new UtilityRequest(); // UtilityRequest | 
    try {
      UtilityResponse result = apiInstance.postOriginKeys(idempotencyKey, utilityRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilityApi#postOriginKeys");
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
| **idempotencyKey** | **String**| A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). | [optional] |
| **utilityRequest** | [**UtilityRequest**](UtilityRequest.md)|  | [optional] |

### Return type

[**UtilityResponse**](UtilityResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  * Idempotency-Key -  <br>  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  * Idempotency-Key -  <br>  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

