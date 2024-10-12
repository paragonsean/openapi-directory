# TokensApi

All URIs are relative to *https://api.sandbox.velopayments.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resendToken**](TokensApi.md#resendToken) | **POST** /v2/users/{userId}/tokens | Resend a token |


<a id="resendToken"></a>
# **resendToken**
> resendToken(userId, resendTokenRequest)

Resend a token

&lt;p&gt;Resend the specified token &lt;/p&gt; &lt;p&gt;The token to resend must already exist for the user &lt;/p&gt; &lt;p&gt;It will be revoked and a new one issued&lt;/p&gt; 

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    TokensApi apiInstance = new TokensApi(defaultClient);
    UUID userId = UUID.randomUUID(); // UUID | The UUID of the User.
    ResendTokenRequest resendTokenRequest = new ResendTokenRequest(); // ResendTokenRequest | The type of token to resend
    try {
      apiInstance.resendToken(userId, resendTokenRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokensApi#resendToken");
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
| **userId** | **UUID**| The UUID of the User. | |
| **resendTokenRequest** | [**ResendTokenRequest**](ResendTokenRequest.md)| The type of token to resend | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | request completed okay |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

