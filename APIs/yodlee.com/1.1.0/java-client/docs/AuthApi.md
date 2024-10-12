# AuthApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteApiKey**](AuthApi.md#deleteApiKey) | **DELETE** /auth/apiKey/{key} | Delete API Key |
| [**deleteToken**](AuthApi.md#deleteToken) | **DELETE** /auth/token | Delete Token |
| [**generateAccessToken**](AuthApi.md#generateAccessToken) | **POST** /auth/token | Generate Access Token |
| [**generateApiKey**](AuthApi.md#generateApiKey) | **POST** /auth/apiKey | Generate API Key |
| [**getApiKeys**](AuthApi.md#getApiKeys) | **GET** /auth/apiKey | Get API Keys |


<a id="deleteApiKey"></a>
# **deleteApiKey**
> deleteApiKey(key)

Delete API Key

This endpoint allows an existing API key to be deleted.&lt;br&gt;You can use one of the following authorization methods to access this API:&lt;br&gt;&lt;ol&gt;&lt;li&gt;cobsession&lt;/li&gt;&lt;li&gt;JWT token&lt;/li&gt;&lt;/ol&gt; &lt;b&gt;Notes:&lt;/b&gt; &lt;li&gt;This service is not available in developer sandbox environment and will be made availablefor testing in your dedicated environment. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AuthApi apiInstance = new AuthApi(defaultClient);
    String key = "key_example"; // String | key
    try {
      apiInstance.deleteApiKey(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#deleteApiKey");
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
| **key** | **String**| key | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **204** | No Content |  -  |
| **400** | Y807 : Resource not found&lt;br&gt;Y806 : Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="deleteToken"></a>
# **deleteToken**
> deleteToken()

Delete Token

This endpoint revokes the token passed in the Authorization header. This service is applicable for JWT-based (and all API key-based) authentication and also client credential (clientId and secret) based authentication. This service does not return a response body. The HTTP response code is 204 (success with no content). &lt;br&gt;Tokens generally have limited lifetime of up to 30 minutes. You will call this service when you finish working with one user, and you want to delete the valid token rather than simply letting it expire.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;li&gt;Revoking an access token (either type, admin or a user token) can take up to 2 minutes, as the tokens are stored on a distributed system.&lt;br/&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AuthApi apiInstance = new AuthApi(defaultClient);
    try {
      apiInstance.deleteToken();
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#deleteToken");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **401** | Y020 : Invalid token in authorization header&lt;br&gt;Y023 : Token has expired&lt;br&gt;Y016 : Api-Version header missing&lt;br&gt;Y015 : Unauthorized User&lt;br&gt;Y027 : Unsupported authentication type&lt;br&gt;Y007 : Authorization header missing&lt;br&gt;Y020 : Invalid token in authorization header |  -  |
| **404** | Not Found |  -  |

<a id="generateAccessToken"></a>
# **generateAccessToken**
> ClientCredentialTokenResponse generateAccessToken()

Generate Access Token

&lt;b&gt;Generate Access Token using client credential authentication.&lt;/b&gt;&lt;br&gt;This service returns access tokens required to access Yodlee 1.1 APIs. These tokens are the simplest and easiest of several alternatives for authenticating with Yodlee servers.&lt;br&gt;The most commonly used services obtain data specific to an end user (your customer). For these services, you need a &lt;b&gt;user access token&lt;/b&gt;. These are simply tokens created with the user name parameter (&lt;b&gt;loginName&lt;/b&gt;) set to the id of your end user.  &lt;i&gt;&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; You determine this id and you must ensure it&#39;s unique among all your customers.&lt;/i&gt; &lt;br&gt;&lt;br&gt;Each token issued has an associated user. The token passed in the http headers explicitly names the user referenced in that API call.&lt;br&gt;&lt;br&gt;Some of the APIs do administrative work, and don&#39;t reference an end user. &lt;br/&gt;One example of administrative work is key management. Another example is registering a new user explicitly, with &lt;b&gt;POST /user/register&lt;/b&gt; call or subscribe to webhook, with &lt;b&gt;POST /config/notifications/events/{eventName}&lt;/b&gt;. &lt;br/&gt;To invoke these, you need an &lt;b&gt;admin access token&lt;/b&gt;. Create this by passing in your admin user login name in place of a regular user name.&lt;br&gt;&lt;br&gt;This service also allows for simplified registration of new users. Any time you pass in a user name not already in use, the system will automatically implicitly create a new user for you. &lt;br&gt;This user will naturally have very few associated details. You can later provide additional user information by calling the &lt;b&gt;PUT user/register service&lt;/b&gt;.&lt;br&gt;&lt;br&gt;&lt;b&gt;Notes:&lt;/b&gt;&lt;li&gt;The content type has to be passed as application/x-www-form-urlencoded.&lt;li&gt;Upgrading to client credential authentication requires infrastructure reconfiguration. &lt;li&gt;Customers wishing to switch from another authentication scheme to client credential authentication, please contact Yodlee Client Services.&lt;/li&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AuthApi apiInstance = new AuthApi(defaultClient);
    try {
      ClientCredentialTokenResponse result = apiInstance.generateAccessToken();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#generateAccessToken");
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

[**ClientCredentialTokenResponse**](ClientCredentialTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **400** | Y800 : Invalid value for loginName&lt;br&gt;Y806 : Invalid input&lt;br&gt;Y801 : Invalid length for loginName&lt;br&gt;Y303 : clientId or secret is missing&lt;br&gt;Y301 : Invalid clientId or secret&lt;br&gt;Y305 : Access token can be issued only for pre-registered users&lt;br&gt;Y004 : Inactive user&lt;br&gt;Y901 : Service not supported&lt;br&gt; |  -  |
| **401** | Y016 : loginName header missing&lt;br&gt;Y015 : Unauthorized User&lt;br&gt;Y016 : Api-Version header missing&lt;br&gt;Y020 : Invalid token in authorization header&lt;br&gt;Y027 : Unsupported authentication type |  -  |
| **404** | Not Found |  -  |

<a id="generateApiKey"></a>
# **generateApiKey**
> ApiKeyResponse generateApiKey(apiKeyRequest)

Generate API Key

This endpoint is used to generate an API key. The RSA public key you provide should be in 2048 bit PKCS#8 encoded format. &lt;br&gt;A public key is a mandatory input for generating the API key.&lt;br/&gt;The public key should be a unique key. The apiKeyId you get in the response is what you should use to generate the JWT token.&lt;br&gt; You can use one of the following authorization methods to access&lt;br/&gt;this API:&lt;br&gt;&lt;ol&gt;&lt;li&gt;cobsession&lt;/li&gt;&lt;li&gt;JWT token&lt;/li&gt;&lt;/ol&gt; Alternatively, you can use base 64 encoded cobrandLogin and cobrandPassword in the Authorization header (Format: Authorization: Basic &lt;encoded value of cobrandLogin: cobrandPassword&gt;)&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;br&gt;&lt;li&gt;This service is not available in developer sandbox environment and will be made available for testing in your dedicated environment. The content type has to be passed as application/json for the body parameter.&lt;/li&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AuthApi apiInstance = new AuthApi(defaultClient);
    ApiKeyRequest apiKeyRequest = new ApiKeyRequest(); // ApiKeyRequest | apiKeyRequest
    try {
      ApiKeyResponse result = apiInstance.generateApiKey(apiKeyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#generateApiKey");
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
| **apiKeyRequest** | [**ApiKeyRequest**](ApiKeyRequest.md)| apiKeyRequest | |

### Return type

[**ApiKeyResponse**](ApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **400** | Y800 : Invalid value for RS512 publicKey&lt;br&gt;Y806 : Invalid input&lt;br&gt;Y824 : The maximum number of apiKey permitted is 5&lt;br&gt;Y811 : publicKey value already exists |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getApiKeys"></a>
# **getApiKeys**
> ApiKeyResponse getApiKeys()

Get API Keys

This endpoint provides the list of API keys that exist for a customer.&lt;br&gt;You can use one of the following authorization methods to access this API:&lt;br&gt;&lt;ol&gt;&lt;li&gt;cobsession&lt;/li&gt;&lt;li&gt;JWT token&lt;/li&gt;&lt;/ol&gt;&lt;b&gt;Notes:&lt;/b&gt;&lt;li&gt;This service is not available in developer sandbox environment and will be made available for testing in your dedicated environment. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AuthApi apiInstance = new AuthApi(defaultClient);
    try {
      ApiKeyResponse result = apiInstance.getApiKeys();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#getApiKeys");
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

[**ApiKeyResponse**](ApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

