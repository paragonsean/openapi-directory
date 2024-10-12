# DeprecatedServicesApi

All URIs are relative to *https://viatorapi.viator.com/service*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**merchantCancellation**](DeprecatedServicesApi.md#merchantCancellation) | **POST** /merchant/cancellation | /merchant/cancellation |


<a id="merchantCancellation"></a>
# **merchantCancellation**
> MerchantCancellation200Response merchantCancellation(acceptLanguage, merchantCancellationRequest)

/merchant/cancellation

Cancel a booking **Note**: This service has been replaced by the [cancellationReasons](#operation/cancellationReasons), [bookingQuote](#operation/bookingQuote) and [cancelBooking](#operation/cancelBooking) endpoints 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeprecatedServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    DeprecatedServicesApi apiInstance = new DeprecatedServicesApi(defaultClient);
    String acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    MerchantCancellationRequest merchantCancellationRequest = new MerchantCancellationRequest(); // MerchantCancellationRequest | 
    try {
      MerchantCancellation200Response result = apiInstance.merchantCancellation(acceptLanguage, merchantCancellationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeprecatedServicesApi#merchantCancellation");
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
| **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | |
| **merchantCancellationRequest** | [**MerchantCancellationRequest**](MerchantCancellationRequest.md)|  | [optional] |

### Return type

[**MerchantCancellation200Response**](MerchantCancellation200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Error |  -  |

