# ApplePayApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**registerDomain**](ApplePayApi.md#registerDomain) | **POST** /v2/apple-pay/domains | RegisterDomain |


<a id="registerDomain"></a>
# **registerDomain**
> RegisterDomainResponse registerDomain(registerDomainRequest)

RegisterDomain

Activates a domain for use with Apple Pay on the Web and Square. A validation is performed on this domain by Apple to ensure that it is properly set up as an Apple Pay enabled domain.  This endpoint provides an easy way for platform developers to bulk activate Apple Pay on the Web with Square for merchants using their platform.  To learn more about Web Apple Pay, see [Add the Apple Pay on the Web Button](https://developer.squareup.com/docs/payment-form/add-digital-wallets/apple-pay).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplePayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ApplePayApi apiInstance = new ApplePayApi(defaultClient);
    RegisterDomainRequest registerDomainRequest = new RegisterDomainRequest(); // RegisterDomainRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      RegisterDomainResponse result = apiInstance.registerDomain(registerDomainRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplePayApi#registerDomain");
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
| **registerDomainRequest** | [**RegisterDomainRequest**](RegisterDomainRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**RegisterDomainResponse**](RegisterDomainResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

