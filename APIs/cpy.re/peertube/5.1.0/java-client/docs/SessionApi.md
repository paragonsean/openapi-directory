# SessionApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOAuthClient**](SessionApi.md#getOAuthClient) | **GET** /api/v1/oauth-clients/local | Login prerequisite |
| [**getOAuthToken**](SessionApi.md#getOAuthToken) | **POST** /api/v1/users/token | Login |
| [**revokeOAuthToken**](SessionApi.md#revokeOAuthToken) | **POST** /api/v1/users/revoke-token | Logout |


<a id="getOAuthClient"></a>
# **getOAuthClient**
> OAuthClient getOAuthClient()

Login prerequisite

You need to retrieve a client id and secret before [logging in](#operation/getOAuthToken).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    SessionApi apiInstance = new SessionApi(defaultClient);
    try {
      OAuthClient result = apiInstance.getOAuthClient();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionApi#getOAuthClient");
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

[**OAuthClient**](OAuthClient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getOAuthToken"></a>
# **getOAuthToken**
> GetOAuthToken200Response getOAuthToken(clientId, clientSecret, grantType, password, username, refreshToken)

Login

With your [client id and secret](#operation/getOAuthClient), you can retrieve an access and refresh tokens.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    SessionApi apiInstance = new SessionApi(defaultClient);
    String clientId = "clientId_example"; // String | 
    String clientSecret = "clientSecret_example"; // String | 
    String grantType = "password"; // String | 
    String password = "password_example"; // String | 
    String username = "username_example"; // String | immutable name of the user, used to find or mention its actor
    String refreshToken = "refreshToken_example"; // String | 
    try {
      GetOAuthToken200Response result = apiInstance.getOAuthToken(clientId, clientSecret, grantType, password, username, refreshToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionApi#getOAuthToken");
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
| **clientId** | **String**|  | [optional] |
| **clientSecret** | **String**|  | [optional] |
| **grantType** | **String**|  | [optional] [default to password] [enum: password, refresh_token] |
| **password** | **String**|  | [optional] |
| **username** | **String**| immutable name of the user, used to find or mention its actor | [optional] |
| **refreshToken** | **String**|  | [optional] |

### Return type

[**GetOAuthToken200Response**](GetOAuthToken200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Disambiguate via &#x60;type&#x60;: - &#x60;invalid_client&#x60; for an unmatched &#x60;client_id&#x60; - &#x60;invalid_grant&#x60; for unmatched credentials  |  -  |
| **401** | Disambiguate via &#x60;type&#x60;: - default value for a regular authentication failure - &#x60;invalid_token&#x60; for an expired token  |  -  |

<a id="revokeOAuthToken"></a>
# **revokeOAuthToken**
> revokeOAuthToken()

Logout

Revokes your access token and its associated refresh token, destroying your current session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    SessionApi apiInstance = new SessionApi(defaultClient);
    try {
      apiInstance.revokeOAuthToken();
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionApi#revokeOAuthToken");
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

