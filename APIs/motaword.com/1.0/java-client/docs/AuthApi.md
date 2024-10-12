# AuthApi

All URIs are relative to *https://api.motaword.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAccessToken**](AuthApi.md#getAccessToken) | **POST** /token | Retrieve an access token |


<a id="getAccessToken"></a>
# **getAccessToken**
> Token getAccessToken(tokenRequest)

Retrieve an access token

MotaWord API is using OAuth2 procedures when authenticating or authorizing your API call. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AuthApi apiInstance = new AuthApi(defaultClient);
    TokenRequest tokenRequest = new TokenRequest(); // TokenRequest | 
    try {
      Token result = apiInstance.getAccessToken(tokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#getAccessToken");
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

[**Token**](Token.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Authentication response |  -  |
| **0** | Authentication error - for vendor auth, it will also fail if their account is not approved yet. In that case, the error response will include \&quot;account_status\&quot; key. |  -  |

