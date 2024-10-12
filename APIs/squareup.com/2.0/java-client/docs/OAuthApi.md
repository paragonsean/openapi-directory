# OAuthApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**obtainToken**](OAuthApi.md#obtainToken) | **POST** /oauth2/token | ObtainToken |
| [**renewToken**](OAuthApi.md#renewToken) | **POST** /oauth2/clients/{client_id}/access-token/renew | RenewToken |
| [**revokeToken**](OAuthApi.md#revokeToken) | **POST** /oauth2/revoke | RevokeToken |


<a id="obtainToken"></a>
# **obtainToken**
> ObtainTokenResponse obtainToken(obtainTokenRequest)

ObtainToken

Returns an OAuth access token.  The endpoint supports distinct methods of obtaining OAuth access tokens. Applications specify a method by adding the &#x60;grant_type&#x60; parameter in the request and also provide relevant information.  __Note:__ Regardless of the method application specified, the endpoint always returns two items; an OAuth access token and a refresh token in the response.  __OAuth tokens should only live on secure servers. Application clients should never interact directly with OAuth tokens__.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OAuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");

    OAuthApi apiInstance = new OAuthApi(defaultClient);
    ObtainTokenRequest obtainTokenRequest = new ObtainTokenRequest(); // ObtainTokenRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      ObtainTokenResponse result = apiInstance.obtainToken(obtainTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OAuthApi#obtainToken");
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
| **obtainTokenRequest** | [**ObtainTokenRequest**](ObtainTokenRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**ObtainTokenResponse**](ObtainTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="renewToken"></a>
# **renewToken**
> RenewTokenResponse renewToken(clientId, renewTokenRequest)

RenewToken

&#x60;RenewToken&#x60; is deprecated. For information about refreshing OAuth access tokens, see [Migrate from Renew to Refresh OAuth Tokens](https://developer.squareup.com/docs/oauth-api/migrate-to-refresh-tokens).   Renews an OAuth access token before it expires.  OAuth access tokens besides your application&#39;s personal access token expire after __30 days__. You can also renew expired tokens within __15 days__ of their expiration. You cannot renew an access token that has been expired for more than 15 days. Instead, the associated user must re-complete the OAuth flow from the beginning.  __Important:__ The &#x60;Authorization&#x60; header for this endpoint must have the following format:  &#x60;&#x60;&#x60; Authorization: Client APPLICATION_SECRET &#x60;&#x60;&#x60;  Replace &#x60;APPLICATION_SECRET&#x60; with the application secret on the Credentials page in the [developer dashboard](https://developer.squareup.com/apps).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OAuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure API key authorization: oauth2ClientSecret
    ApiKeyAuth oauth2ClientSecret = (ApiKeyAuth) defaultClient.getAuthentication("oauth2ClientSecret");
    oauth2ClientSecret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //oauth2ClientSecret.setApiKeyPrefix("Token");

    OAuthApi apiInstance = new OAuthApi(defaultClient);
    String clientId = "clientId_example"; // String | Your application ID, available from the [developer dashboard](https://developer.squareup.com/apps).
    RenewTokenRequest renewTokenRequest = new RenewTokenRequest(); // RenewTokenRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      RenewTokenResponse result = apiInstance.renewToken(clientId, renewTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OAuthApi#renewToken");
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
| **clientId** | **String**| Your application ID, available from the [developer dashboard](https://developer.squareup.com/apps). | |
| **renewTokenRequest** | [**RenewTokenRequest**](RenewTokenRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**RenewTokenResponse**](RenewTokenResponse.md)

### Authorization

[oauth2ClientSecret](../README.md#oauth2ClientSecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="revokeToken"></a>
# **revokeToken**
> RevokeTokenResponse revokeToken(revokeTokenRequest)

RevokeToken

Revokes an access token generated with the OAuth flow.  If an account has more than one OAuth access token for your application, this endpoint revokes all of them, regardless of which token you specify. When an OAuth access token is revoked, all of the active subscriptions associated with that OAuth token are canceled immediately.  __Important:__ The &#x60;Authorization&#x60; header for this endpoint must have the following format:  &#x60;&#x60;&#x60; Authorization: Client APPLICATION_SECRET &#x60;&#x60;&#x60;  Replace &#x60;APPLICATION_SECRET&#x60; with the application secret on the OAuth page in the [developer dashboard](https://developer.squareup.com/apps).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OAuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure API key authorization: oauth2ClientSecret
    ApiKeyAuth oauth2ClientSecret = (ApiKeyAuth) defaultClient.getAuthentication("oauth2ClientSecret");
    oauth2ClientSecret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //oauth2ClientSecret.setApiKeyPrefix("Token");

    OAuthApi apiInstance = new OAuthApi(defaultClient);
    RevokeTokenRequest revokeTokenRequest = new RevokeTokenRequest(); // RevokeTokenRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      RevokeTokenResponse result = apiInstance.revokeToken(revokeTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OAuthApi#revokeToken");
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
| **revokeTokenRequest** | [**RevokeTokenRequest**](RevokeTokenRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**RevokeTokenResponse**](RevokeTokenResponse.md)

### Authorization

[oauth2ClientSecret](../README.md#oauth2ClientSecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

