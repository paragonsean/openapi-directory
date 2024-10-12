# AuthenticationOAuthApi

All URIs are relative to *https://api.trakt.tv*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authorizeApplication**](AuthenticationOAuthApi.md#authorizeApplication) | **GET** /oauth/authorize | Authorize Application |
| [**exchangeRefreshTokenForAccessToken**](AuthenticationOAuthApi.md#exchangeRefreshTokenForAccessToken) | **POST** /oauth/token | Exchange refresh_token for access_token |
| [**revokeAnAccessToken**](AuthenticationOAuthApi.md#revokeAnAccessToken) | **POST** /oauth/revoke | Revoke an access_token |


<a id="authorizeApplication"></a>
# **authorizeApplication**
> authorizeApplication(responseType, clientId, redirectUri, state, body)

Authorize Application

Construct then redirect to this URL. The Trakt website will request permissions for your app, which the user needs to approve. If the user isn&#39;t signed into Trakt, it will ask them to do so. Send &#x60;signup&#x3D;true&#x60; if you prefer the account sign up page to be the default.  **Note:** You should use the normal **https://trakt.tv** hostname when creating this URL and not the API URL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationOAuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    AuthenticationOAuthApi apiInstance = new AuthenticationOAuthApi(defaultClient);
    String responseType = "code"; // String | Must be set to code.
    String clientId = " "; // String | Get this from your app settings.
    String redirectUri = " "; // String | URI specified in your app settings.
    String state = " "; // String | State variable for CSRF purposes.
    String body = "body_example"; // String | Default to the sign up page.
    try {
      apiInstance.authorizeApplication(responseType, clientId, redirectUri, state, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationOAuthApi#authorizeApplication");
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
| **responseType** | **String**| Must be set to code. | |
| **clientId** | **String**| Get this from your app settings. | |
| **redirectUri** | **String**| URI specified in your app settings. | |
| **state** | **String**| State variable for CSRF purposes. | [optional] |
| **body** | **String**| Default to the sign up page. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="exchangeRefreshTokenForAccessToken"></a>
# **exchangeRefreshTokenForAccessToken**
> exchangeRefreshTokenForAccessToken(exchangeRefreshTokenForAccessTokenRequest)

Exchange refresh_token for access_token

Use the &#x60;refresh_token&#x60; to get a new &#x60;access_token&#x60; without asking the user to re-authenticate. The &#x60;access_token&#x60; is valid for 3 months before it needs to be refreshed again.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;refresh_token&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Saved from the initial token method. | | &#x60;client_id&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Get this from your app settings. | | &#x60;client_secret&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Get this from your app settings. | | &#x60;redirect_uri&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | URI specified in your app settings. | | &#x60;grant_type&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;* &lt;/a&gt; | string | &#x60;refresh_token&#x60; |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationOAuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    AuthenticationOAuthApi apiInstance = new AuthenticationOAuthApi(defaultClient);
    ExchangeRefreshTokenForAccessTokenRequest exchangeRefreshTokenForAccessTokenRequest = new ExchangeRefreshTokenForAccessTokenRequest(); // ExchangeRefreshTokenForAccessTokenRequest | 
    try {
      apiInstance.exchangeRefreshTokenForAccessToken(exchangeRefreshTokenForAccessTokenRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationOAuthApi#exchangeRefreshTokenForAccessToken");
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
| **exchangeRefreshTokenForAccessTokenRequest** | [**ExchangeRefreshTokenForAccessTokenRequest**](ExchangeRefreshTokenForAccessTokenRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If the &#x60;refresh_token&#x60; is valid, you&#39;ll get the &#x60;access_token&#x60; back. |  -  |
| **401** | If the &#x60;refresh_token&#x60; is invalid, you&#39;ll get a &#x60;401&#x60; error. |  -  |

<a id="revokeAnAccessToken"></a>
# **revokeAnAccessToken**
> revokeAnAccessToken(revokeAnAccessTokenRequest)

Revoke an access_token

An &#x60;access_token&#x60; can be revoked when a user signs out of their Trakt account in your app. This is not required, but might improve the user experience so the user doesn&#39;t have an unused app connection hanging around.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;token&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | A valid OAuth &#x60;access_token&#x60;. | | &#x60;client_id&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Get this from your app settings. | | &#x60;client_secret&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Get this from your app settings. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationOAuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    AuthenticationOAuthApi apiInstance = new AuthenticationOAuthApi(defaultClient);
    RevokeAnAccessTokenRequest revokeAnAccessTokenRequest = new RevokeAnAccessTokenRequest(); // RevokeAnAccessTokenRequest | 
    try {
      apiInstance.revokeAnAccessToken(revokeAnAccessTokenRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationOAuthApi#revokeAnAccessToken");
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
| **revokeAnAccessTokenRequest** | [**RevokeAnAccessTokenRequest**](RevokeAnAccessTokenRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

