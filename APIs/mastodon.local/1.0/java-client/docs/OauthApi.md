# OauthApi

All URIs are relative to *http://mastodon.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**oauthAuthorizeGet**](OauthApi.md#oauthAuthorizeGet) | **GET** /oauth/authorize |  |
| [**oauthRevokePost**](OauthApi.md#oauthRevokePost) | **POST** /oauth/revoke |  |
| [**oauthTokenPost**](OauthApi.md#oauthTokenPost) | **POST** /oauth/token |  |


<a id="oauthAuthorizeGet"></a>
# **oauthAuthorizeGet**
> oauthAuthorizeGet(responseType, clientId, redirectUri, scope, forceLogin)



Displays an authorization form to the user. If approved, it will create and return an authorization code, then redirect to the desired redirect_uri, or show the authorization code if urn:ietf:wg:oauth:2.0:oob was requested. The authorization code can be used while requesting a token to obtain access to user-level methods.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");

    OauthApi apiInstance = new OauthApi(defaultClient);
    String responseType = "responseType_example"; // String | Should be set equal to code.
    String clientId = "clientId_example"; // String | Client ID, obtained during app registration.
    String redirectUri = "redirectUri_example"; // String | Set a URI to redirect the user to. If this parameter is set to urn:ietf:wg:oauth:2.0:oob then the authorization code will be shown instead. Must match one of the redirect URIs declared during app registration.
    String scope = "scope_example"; // String | List of requested OAuth scopes, separated by spaces (or by pluses, if using query parameters). Must be a subset of scopes declared during app registration. If not provided, defaults to read.
    Boolean forceLogin = true; // Boolean | Added in 2.6.0. Forces the user to re-login, which is necessary for authorizing with multiple accounts from the same instance.
    try {
      apiInstance.oauthAuthorizeGet(responseType, clientId, redirectUri, scope, forceLogin);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#oauthAuthorizeGet");
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
| **responseType** | **String**| Should be set equal to code. | |
| **clientId** | **String**| Client ID, obtained during app registration. | |
| **redirectUri** | **String**| Set a URI to redirect the user to. If this parameter is set to urn:ietf:wg:oauth:2.0:oob then the authorization code will be shown instead. Must match one of the redirect URIs declared during app registration. | |
| **scope** | **String**| List of requested OAuth scopes, separated by spaces (or by pluses, if using query parameters). Must be a subset of scopes declared during app registration. If not provided, defaults to read. | [optional] |
| **forceLogin** | **Boolean**| Added in 2.6.0. Forces the user to re-login, which is necessary for authorizing with multiple accounts from the same instance. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The authorization code will be returned as a query parameter named code. |  -  |
| **400** | If the authorization code is incorrect or has been used already, the request will fail. |  -  |

<a id="oauthRevokePost"></a>
# **oauthRevokePost**
> oauthRevokePost(oauthRevokePostRequest)



Revoke an access token to make it no longer valid for use.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");

    OauthApi apiInstance = new OauthApi(defaultClient);
    OauthRevokePostRequest oauthRevokePostRequest = new OauthRevokePostRequest(); // OauthRevokePostRequest | 
    try {
      apiInstance.oauthRevokePost(oauthRevokePostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#oauthRevokePost");
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
| **oauthRevokePostRequest** | [**OauthRevokePostRequest**](OauthRevokePostRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If you own the provided token, the API call will provide an empty response. This operation is idempotent, so calling this API multiple times will still return OK. |  -  |
| **403** | If you provide a token you do not own, or no token at all, the API call will return a 403 error. |  -  |

<a id="oauthTokenPost"></a>
# **oauthTokenPost**
> OauthTokenPost200Response oauthTokenPost(oauthTokenPostRequest)



Returns an access token, to be used during API calls that are not public.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");

    OauthApi apiInstance = new OauthApi(defaultClient);
    OauthTokenPostRequest oauthTokenPostRequest = new OauthTokenPostRequest(); // OauthTokenPostRequest | 
    try {
      OauthTokenPost200Response result = apiInstance.oauthTokenPost(oauthTokenPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#oauthTokenPost");
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
| **oauthTokenPostRequest** | [**OauthTokenPostRequest**](OauthTokenPostRequest.md)|  | [optional] |

### Return type

[**OauthTokenPost200Response**](OauthTokenPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Store this access_token for later use with auth-required methods. The token should be passed as an HTTP Authorization header when making API calls, with the value Bearer access_token |  -  |
| **400** | If you try to request a scope that was not included when registering the app, the request will fail. |  -  |
| **401** | If client_id and client_secret do not match or are invalid, the request will fail. |  -  |

