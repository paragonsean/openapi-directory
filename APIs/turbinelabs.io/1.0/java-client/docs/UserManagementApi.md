# UserManagementApi

All URIs are relative to *https://api.turbinelabs.io/v1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminUserSelfAccessTokenAccessTokenKeyDelete**](UserManagementApi.md#adminUserSelfAccessTokenAccessTokenKeyDelete) | **DELETE** /admin/user/self/access_token/{access-token-key} | Delete the specified access token. |
| [**adminUserSelfAccessTokensGet**](UserManagementApi.md#adminUserSelfAccessTokensGet) | **GET** /admin/user/self/access_tokens | Lists Access Tokens that are configured for the authenticated user. |
| [**adminUserSelfAccessTokensPost**](UserManagementApi.md#adminUserSelfAccessTokensPost) | **POST** /admin/user/self/access_tokens | Creates a new Access Token and associates it with the authenticated user. |
| [**adminUserSelfGet**](UserManagementApi.md#adminUserSelfGet) | **GET** /admin/user/self | Returns the user object for the account authorized and making this request. |


<a id="adminUserSelfAccessTokenAccessTokenKeyDelete"></a>
# **adminUserSelfAccessTokenAccessTokenKeyDelete**
> adminUserSelfAccessTokenAccessTokenKeyDelete(accessTokenKey, checksum)

Delete the specified access token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    UserManagementApi apiInstance = new UserManagementApi(defaultClient);
    String accessTokenKey = "9cd24183-f848-48f8-6f55-0f0724070000"; // String | the key of the Access Token that should be deleted
    String checksum = "9cd24183-f848-48f8-6f55-0f07240700b9"; // String | the current checksum of the user to be modified
    try {
      apiInstance.adminUserSelfAccessTokenAccessTokenKeyDelete(accessTokenKey, checksum);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserManagementApi#adminUserSelfAccessTokenAccessTokenKeyDelete");
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
| **accessTokenKey** | **String**| the key of the Access Token that should be deleted | |
| **checksum** | **String**| the current checksum of the user to be modified | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An empty result if the API key deletion was successful. |  -  |
| **0** | An error; may be unexpected or validation error if the last API was removed. |  -  |

<a id="adminUserSelfAccessTokensGet"></a>
# **adminUserSelfAccessTokensGet**
> MultiAccessTokens adminUserSelfAccessTokensGet()

Lists Access Tokens that are configured for the authenticated user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    UserManagementApi apiInstance = new UserManagementApi(defaultClient);
    try {
      MultiAccessTokens result = apiInstance.adminUserSelfAccessTokensGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserManagementApi#adminUserSelfAccessTokensGet");
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

[**MultiAccessTokens**](MultiAccessTokens.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Access Tokens defined for the authenticated user. |  -  |
| **0** | Unexpected error |  -  |

<a id="adminUserSelfAccessTokensPost"></a>
# **adminUserSelfAccessTokensPost**
> AccessToken adminUserSelfAccessTokensPost(description)

Creates a new Access Token and associates it with the authenticated user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    UserManagementApi apiInstance = new UserManagementApi(defaultClient);
    AccessTokenDescription description = new AccessTokenDescription(); // AccessTokenDescription | A short string (<255 characters) describing the expected use of the token.
    try {
      AccessToken result = apiInstance.adminUserSelfAccessTokensPost(description);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserManagementApi#adminUserSelfAccessTokensPost");
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
| **description** | [**AccessTokenDescription**](AccessTokenDescription.md)| A short string (&lt;255 characters) describing the expected use of the token. | |

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The new Access Token that was created. |  -  |
| **0** | Unexpected error |  -  |

<a id="adminUserSelfGet"></a>
# **adminUserSelfGet**
> User adminUserSelfGet()

Returns the user object for the account authorized and making this request.

Request the user object for an authorized requesting account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    UserManagementApi apiInstance = new UserManagementApi(defaultClient);
    try {
      User result = apiInstance.adminUserSelfGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserManagementApi#adminUserSelfGet");
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

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The authorized user. |  -  |
| **0** | Unexpected error. |  -  |

