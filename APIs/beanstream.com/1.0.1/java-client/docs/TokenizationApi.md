# TokenizationApi

All URIs are relative to *https://www.beanstream.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**scriptsTokenizationTokensPost**](TokenizationApi.md#scriptsTokenizationTokensPost) | **POST** /scripts/tokenization/tokens | Tokenize credit card |


<a id="scriptsTokenizationTokensPost"></a>
# **scriptsTokenizationTokensPost**
> TokenResponse scriptsTokenizationTokensPost(tokenRequest)

Tokenize credit card

NOTE that the full URL for this API call is https://www.beanstream.com/scripts/tokenization/tokens. Turn a credit card into a token using this service. This helps lessen your PCI scope by not passing the credit card information to your server. Instead you turn the card number into a token in the client app, then send the token to the server. When you send the token to Beanstream to make a payment, Beanstream then looks up the card number from that token and makes the payment. Tokens can also be used to create payment profiles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokenizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.beanstream.com/api/v1");

    TokenizationApi apiInstance = new TokenizationApi(defaultClient);
    TokenRequest tokenRequest = new TokenRequest(); // TokenRequest | 
    try {
      TokenResponse result = apiInstance.scriptsTokenizationTokensPost(tokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokenizationApi#scriptsTokenizationTokensPost");
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
| **tokenRequest** | [**TokenRequest**](TokenRequest.md)|  | [optional] |

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Token response object. One will always be returned even if the data or card was invalid. The validity of the card is not checked with this API call. |  -  |

