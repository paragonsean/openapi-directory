# OauthApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**oauthAccess**](OauthApi.md#oauthAccess) | **GET** /oauth.access |  |
| [**oauthToken**](OauthApi.md#oauthToken) | **GET** /oauth.token |  |
| [**oauthV2Access_0**](OauthApi.md#oauthV2Access_0) | **GET** /oauth.v2.access |  |


<a id="oauthAccess"></a>
# **oauthAccess**
> DefaultSuccessTemplate oauthAccess(clientId, clientSecret, code, redirectUri, singleChannel)



Exchanges a temporary OAuth verifier code for an access token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    OauthApi apiInstance = new OauthApi(defaultClient);
    String clientId = "clientId_example"; // String | Issued when you created your application.
    String clientSecret = "clientSecret_example"; // String | Issued when you created your application.
    String code = "code_example"; // String | The `code` param returned via the OAuth callback.
    String redirectUri = "redirectUri_example"; // String | This must match the originally submitted URI (if one was sent).
    Boolean singleChannel = true; // Boolean | Request the user to add your app only to a single channel. Only valid with a [legacy workspace app](https://api.slack.com/legacy-workspace-apps).
    try {
      DefaultSuccessTemplate result = apiInstance.oauthAccess(clientId, clientSecret, code, redirectUri, singleChannel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#oauthAccess");
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
| **clientId** | **String**| Issued when you created your application. | [optional] |
| **clientSecret** | **String**| Issued when you created your application. | [optional] |
| **code** | **String**| The &#x60;code&#x60; param returned via the OAuth callback. | [optional] |
| **redirectUri** | **String**| This must match the originally submitted URI (if one was sent). | [optional] |
| **singleChannel** | **Boolean**| Request the user to add your app only to a single channel. Only valid with a [legacy workspace app](https://api.slack.com/legacy-workspace-apps). | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful user token negotiation for a single scope |  -  |
| **0** | Typical error response |  -  |

<a id="oauthToken"></a>
# **oauthToken**
> DefaultSuccessTemplate oauthToken(clientId, clientSecret, code, redirectUri, singleChannel)



Exchanges a temporary OAuth verifier code for a workspace token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    OauthApi apiInstance = new OauthApi(defaultClient);
    String clientId = "clientId_example"; // String | Issued when you created your application.
    String clientSecret = "clientSecret_example"; // String | Issued when you created your application.
    String code = "code_example"; // String | The `code` param returned via the OAuth callback.
    String redirectUri = "redirectUri_example"; // String | This must match the originally submitted URI (if one was sent).
    Boolean singleChannel = true; // Boolean | Request the user to add your app only to a single channel.
    try {
      DefaultSuccessTemplate result = apiInstance.oauthToken(clientId, clientSecret, code, redirectUri, singleChannel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#oauthToken");
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
| **clientId** | **String**| Issued when you created your application. | [optional] |
| **clientSecret** | **String**| Issued when you created your application. | [optional] |
| **code** | **String**| The &#x60;code&#x60; param returned via the OAuth callback. | [optional] |
| **redirectUri** | **String**| This must match the originally submitted URI (if one was sent). | [optional] |
| **singleChannel** | **Boolean**| Request the user to add your app only to a single channel. | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success example using a workspace app produces a very different kind of response |  -  |
| **0** | Typical error response |  -  |

<a id="oauthV2Access_0"></a>
# **oauthV2Access_0**
> DefaultSuccessTemplate oauthV2Access_0(code, clientId, clientSecret, redirectUri)



Exchanges a temporary OAuth verifier code for an access token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    OauthApi apiInstance = new OauthApi(defaultClient);
    String code = "code_example"; // String | The `code` param returned via the OAuth callback.
    String clientId = "clientId_example"; // String | Issued when you created your application.
    String clientSecret = "clientSecret_example"; // String | Issued when you created your application.
    String redirectUri = "redirectUri_example"; // String | This must match the originally submitted URI (if one was sent).
    try {
      DefaultSuccessTemplate result = apiInstance.oauthV2Access_0(code, clientId, clientSecret, redirectUri);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#oauthV2Access_0");
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
| **code** | **String**| The &#x60;code&#x60; param returned via the OAuth callback. | |
| **clientId** | **String**| Issued when you created your application. | [optional] |
| **clientSecret** | **String**| Issued when you created your application. | [optional] |
| **redirectUri** | **String**| This must match the originally submitted URI (if one was sent). | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful token request with scopes for both a bot user and a user token |  -  |
| **0** | Typical error response |  -  |

