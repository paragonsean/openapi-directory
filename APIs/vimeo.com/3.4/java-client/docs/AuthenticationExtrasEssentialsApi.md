# AuthenticationExtrasEssentialsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**clientAuth**](AuthenticationExtrasEssentialsApi.md#clientAuth) | **POST** /oauth/authorize/client | Authorize a client with OAuth |
| [**convertAccessToken**](AuthenticationExtrasEssentialsApi.md#convertAccessToken) | **POST** /oauth/authorize/vimeo_oauth1 | Convert OAuth 1 access tokens to OAuth 2 access tokens |
| [**deleteToken**](AuthenticationExtrasEssentialsApi.md#deleteToken) | **DELETE** /tokens | Revoke the current access token |
| [**exchangeAuthCode**](AuthenticationExtrasEssentialsApi.md#exchangeAuthCode) | **POST** /oauth/access_token | Exchange an authorization code for an access token |
| [**verifyToken**](AuthenticationExtrasEssentialsApi.md#verifyToken) | **GET** /oauth/verify | Verify an OAuth 2 token |


<a id="clientAuth"></a>
# **clientAuth**
> Auth clientAuth(clientAuthRequest)

Authorize a client with OAuth

For information on utilizing OAuth client authorization, see our [authentication](/api/authentication#generate-unauthenticated-tokens) documentation or the [Client Credentials Grant](https://tools.ietf.org/html/draft-ietf-oauth-v2-31#section-4.4) section of the [OAuth spec](https://tools.ietf.org/html/draft-ietf-oauth-v2-31.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationExtrasEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AuthenticationExtrasEssentialsApi apiInstance = new AuthenticationExtrasEssentialsApi(defaultClient);
    ClientAuthRequest clientAuthRequest = new ClientAuthRequest(); // ClientAuthRequest | 
    try {
      Auth result = apiInstance.clientAuth(clientAuthRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationExtrasEssentialsApi#clientAuth");
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
| **clientAuthRequest** | [**ClientAuthRequest**](ClientAuthRequest.md)|  | |

### Return type

[**Auth**](Auth.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.auth+json
 - **Accept**: application/vnd.vimeo.auth+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The authorization was successful. |  -  |
| **401** | Error code 8001: No such client secret exists. |  -  |

<a id="convertAccessToken"></a>
# **convertAccessToken**
> Auth convertAccessToken(convertAccessTokenRequest)

Convert OAuth 1 access tokens to OAuth 2 access tokens

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationExtrasEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AuthenticationExtrasEssentialsApi apiInstance = new AuthenticationExtrasEssentialsApi(defaultClient);
    ConvertAccessTokenRequest convertAccessTokenRequest = new ConvertAccessTokenRequest(); // ConvertAccessTokenRequest | 
    try {
      Auth result = apiInstance.convertAccessToken(convertAccessTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationExtrasEssentialsApi#convertAccessToken");
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
| **convertAccessTokenRequest** | [**ConvertAccessTokenRequest**](ConvertAccessTokenRequest.md)|  | |

### Return type

[**Auth**](Auth.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.auth+json
 - **Accept**: application/vnd.vimeo.auth+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tokens were converted. |  -  |
| **400** | * The token is invalid. * The token has unauthorized scopes. |  -  |

<a id="deleteToken"></a>
# **deleteToken**
> Auth deleteToken()

Revoke the current access token

This method enables an app to notify the API that it is done with a token and that the token can be discarded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationExtrasEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AuthenticationExtrasEssentialsApi apiInstance = new AuthenticationExtrasEssentialsApi(defaultClient);
    try {
      Auth result = apiInstance.deleteToken();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationExtrasEssentialsApi#deleteToken");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Auth**](Auth.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.auth+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The token was revoked. |  -  |
| **400** | You can&#39;t revoke access for an OAuth 1 token. |  -  |

<a id="exchangeAuthCode"></a>
# **exchangeAuthCode**
> Auth exchangeAuthCode(exchangeAuthCodeRequest)

Exchange an authorization code for an access token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationExtrasEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AuthenticationExtrasEssentialsApi apiInstance = new AuthenticationExtrasEssentialsApi(defaultClient);
    ExchangeAuthCodeRequest exchangeAuthCodeRequest = new ExchangeAuthCodeRequest(); // ExchangeAuthCodeRequest | 
    try {
      Auth result = apiInstance.exchangeAuthCode(exchangeAuthCodeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationExtrasEssentialsApi#exchangeAuthCode");
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
| **exchangeAuthCodeRequest** | [**ExchangeAuthCodeRequest**](ExchangeAuthCodeRequest.md)|  | |

### Return type

[**Auth**](Auth.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.auth+json
 - **Accept**: application/vnd.vimeo.auth+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The authorization code was exchanged. |  -  |
| **400** | * The grant type is invalid. * The authorization code is invalid. * The redirect URI doesn&#39;t match the URI to create the authorization code. |  -  |

<a id="verifyToken"></a>
# **verifyToken**
> Auth verifyToken()

Verify an OAuth 2 token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationExtrasEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AuthenticationExtrasEssentialsApi apiInstance = new AuthenticationExtrasEssentialsApi(defaultClient);
    try {
      Auth result = apiInstance.verifyToken();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationExtrasEssentialsApi#verifyToken");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Auth**](Auth.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.auth+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The token was verified. |  -  |
| **401** | The token isn&#39;t a valid OAuth 2 token. |  -  |

