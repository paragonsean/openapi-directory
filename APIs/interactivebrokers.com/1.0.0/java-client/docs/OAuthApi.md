# OAuthApi

All URIs are relative to *https://www.interactivebrokers.com/tradingapi/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**oauthAccessTokenPost**](OAuthApi.md#oauthAccessTokenPost) | **POST** /oauth/access_token | Obtain a access token |
| [**oauthLiveSessionTokenPost**](OAuthApi.md#oauthLiveSessionTokenPost) | **POST** /oauth/live_session_token | Obtain a live session token |
| [**oauthRequestTokenPost**](OAuthApi.md#oauthRequestTokenPost) | **POST** /oauth/request_token | Obtain a request token |


<a id="oauthAccessTokenPost"></a>
# **oauthAccessTokenPost**
> OauthAccessTokenPost200Response oauthAccessTokenPost(oauthAccessTokenPostRequest)

Obtain a access token

Obtain an access token using the request token and the verification code you received after the user provided authorization. See section 6.3 of the OAuth v1.0a specification for more details.  

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
    defaultClient.setBasePath("https://www.interactivebrokers.com/tradingapi/v1");
    
    // Configure API key authorization: cookieAuth
    ApiKeyAuth cookieAuth = (ApiKeyAuth) defaultClient.getAuthentication("cookieAuth");
    cookieAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cookieAuth.setApiKeyPrefix("Token");

    OAuthApi apiInstance = new OAuthApi(defaultClient);
    OauthAccessTokenPostRequest oauthAccessTokenPostRequest = new OauthAccessTokenPostRequest(); // OauthAccessTokenPostRequest | OAuth Parameters
    try {
      OauthAccessTokenPost200Response result = apiInstance.oauthAccessTokenPost(oauthAccessTokenPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OAuthApi#oauthAccessTokenPost");
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
| **oauthAccessTokenPostRequest** | [**OauthAccessTokenPostRequest**](OauthAccessTokenPostRequest.md)| OAuth Parameters | |

### Return type

[**OauthAccessTokenPost200Response**](OauthAccessTokenPost200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Access token and token secret |  -  |
| **400** | Unsuccessfull response |  -  |
| **401** | Unsuccessfull response |  -  |
| **403** | Unsuccessfull response |  -  |
| **408** | Unsuccessfull response |  -  |

<a id="oauthLiveSessionTokenPost"></a>
# **oauthLiveSessionTokenPost**
> OauthLiveSessionTokenPost200Response oauthLiveSessionTokenPost(oauthLiveSessionTokenPostRequest)

Obtain a live session token

In order to access protected IB resources, a live session token is required. This endpoint allows consumers to obtain a live session token to access these resources using an OAuth access token and the Diffie-Hellman prime and generator supplied during the registration process. Note this is an additional IB-specific step, and not part of the OAuth v1.0a specification. Please refer to the \&quot;OAuth at Interactive Brokers\&quot; document for more details.  https://www.interactivebrokers.com/webtradingapi/oauth.pdf 

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
    defaultClient.setBasePath("https://www.interactivebrokers.com/tradingapi/v1");
    
    // Configure API key authorization: cookieAuth
    ApiKeyAuth cookieAuth = (ApiKeyAuth) defaultClient.getAuthentication("cookieAuth");
    cookieAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cookieAuth.setApiKeyPrefix("Token");

    OAuthApi apiInstance = new OAuthApi(defaultClient);
    OauthLiveSessionTokenPostRequest oauthLiveSessionTokenPostRequest = new OauthLiveSessionTokenPostRequest(); // OauthLiveSessionTokenPostRequest | OAuth Parameters
    try {
      OauthLiveSessionTokenPost200Response result = apiInstance.oauthLiveSessionTokenPost(oauthLiveSessionTokenPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OAuthApi#oauthLiveSessionTokenPost");
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
| **oauthLiveSessionTokenPostRequest** | [**OauthLiveSessionTokenPostRequest**](OauthLiveSessionTokenPostRequest.md)| OAuth Parameters | |

### Return type

[**OauthLiveSessionTokenPost200Response**](OauthLiveSessionTokenPost200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | DH response |  -  |
| **400** | Unsuccessfull response |  -  |
| **401** | Unsuccessfull response |  -  |
| **403** | Unsuccessfull response |  -  |
| **408** | Unsuccessfull response |  -  |

<a id="oauthRequestTokenPost"></a>
# **oauthRequestTokenPost**
> OauthRequestTokenPost200Response oauthRequestTokenPost(oauthRequestTokenPostRequest)

Obtain a request token

Obtain a request token. See section 6.1 of the OAuth v1.0a specification for more information. http://oauth.net/core/1.0a/#auth_step1  Note we do not return an oauth_token_secret in the response as we are using RSA signatures rather than PLAINTEXT authentication.  

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
    defaultClient.setBasePath("https://www.interactivebrokers.com/tradingapi/v1");
    
    // Configure API key authorization: cookieAuth
    ApiKeyAuth cookieAuth = (ApiKeyAuth) defaultClient.getAuthentication("cookieAuth");
    cookieAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cookieAuth.setApiKeyPrefix("Token");

    OAuthApi apiInstance = new OAuthApi(defaultClient);
    OauthRequestTokenPostRequest oauthRequestTokenPostRequest = new OauthRequestTokenPostRequest(); // OauthRequestTokenPostRequest | OAuth Parameters
    try {
      OauthRequestTokenPost200Response result = apiInstance.oauthRequestTokenPost(oauthRequestTokenPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OAuthApi#oauthRequestTokenPost");
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
| **oauthRequestTokenPostRequest** | [**OauthRequestTokenPostRequest**](OauthRequestTokenPostRequest.md)| OAuth Parameters | |

### Return type

[**OauthRequestTokenPost200Response**](OauthRequestTokenPost200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OAuth token |  -  |
| **400** | Unsuccessfull response |  -  |
| **401** | Unsuccessfull response |  -  |
| **403** | Unsuccessfull response |  -  |
| **408** | Unsuccessfull response |  -  |

