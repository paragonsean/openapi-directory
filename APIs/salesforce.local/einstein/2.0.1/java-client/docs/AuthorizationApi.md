# AuthorizationApi

All URIs are relative to *http://salesforce.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**generateTokenV2**](AuthorizationApi.md#generateTokenV2) | **POST** /v2/oauth2/token | Generate an OAuth Token |
| [**revokeRefreshTokenV2**](AuthorizationApi.md#revokeRefreshTokenV2) | **DELETE** /v2/oauth2/tokens/{token} | Delete a Refresh Token |


<a id="generateTokenV2"></a>
# **generateTokenV2**
> GenerateAccessTokenResponse generateTokenV2(assertion, grantType, refreshToken, scope, validFor)

Generate an OAuth Token

Returns an OAuth access token or a refresh token. You must pass a valid access token in the header of each API call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");

    AuthorizationApi apiInstance = new AuthorizationApi(defaultClient);
    String assertion = "assertion_example"; // String | encrypted payload to identify yourself
    String grantType = "urn:ietf:params:oauth:grant-type:jwt-bearer"; // String | specify the authentication method desired
    String refreshToken = "refreshToken_example"; // String | The refresh token you created previously.
    String scope = "scope_example"; // String | set to `offline` to generate a refresh token
    Integer validFor = 60; // Integer | Number of seconds until the access token expires. Default is 60 seconds. Maximum value is 30 days
    try {
      GenerateAccessTokenResponse result = apiInstance.generateTokenV2(assertion, grantType, refreshToken, scope, validFor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationApi#generateTokenV2");
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
| **assertion** | **String**| encrypted payload to identify yourself | [optional] |
| **grantType** | **String**| specify the authentication method desired | [optional] [enum: urn:ietf:params:oauth:grant-type:jwt-bearer, refresh_token] |
| **refreshToken** | **String**| The refresh token you created previously. | [optional] |
| **scope** | **String**| set to &#x60;offline&#x60; to generate a refresh token | [optional] |
| **validFor** | **Integer**| Number of seconds until the access token expires. Default is 60 seconds. Maximum value is 30 days | [optional] [default to 60] |

### Return type

[**GenerateAccessTokenResponse**](GenerateAccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | access token result |  -  |

<a id="revokeRefreshTokenV2"></a>
# **revokeRefreshTokenV2**
> revokeRefreshTokenV2(token)

Delete a Refresh Token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    AuthorizationApi apiInstance = new AuthorizationApi(defaultClient);
    String token = "SOME_REFRESH_TOKEN"; // String | the token to revoke
    try {
      apiInstance.revokeRefreshTokenV2(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationApi#revokeRefreshTokenV2");
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
| **token** | **String**| the token to revoke | |

### Return type

null (empty response body)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | deleted, with no content returned |  -  |
| **400** | token cannot be removed |  -  |
| **404** | token not found |  -  |

