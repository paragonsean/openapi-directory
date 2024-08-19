# TokensApi

All URIs are relative to *https://api.shipengine.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tokensGetEphemeralToken**](TokensApi.md#tokensGetEphemeralToken) | **POST** /v1/tokens/ephemeral | Get Ephemeral Token |


<a id="tokensGetEphemeralToken"></a>
# **tokensGetEphemeralToken**
> TokensGetEphemeralTokenResponseBodyYaml tokensGetEphemeralToken(redirect)

Get Ephemeral Token

This endpoint returns a token that can be passed to an application for authorized access.  The lifetime of this token is 10 seconds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokensApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    TokensApi apiInstance = new TokensApi(defaultClient);
    Redirect redirect = Redirect.fromValue("shipengine-dashboard"); // Redirect | Include a redirect url to the application formatted with the ephemeral token.
    try {
      TokensGetEphemeralTokenResponseBodyYaml result = apiInstance.tokensGetEphemeralToken(redirect);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokensApi#tokensGetEphemeralToken");
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
| **redirect** | [**Redirect**](.md)| Include a redirect url to the application formatted with the ephemeral token. | [optional] [enum: shipengine-dashboard] |

### Return type

[**TokensGetEphemeralTokenResponseBodyYaml**](TokensGetEphemeralTokenResponseBodyYaml.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

