# OauthApi

All URIs are relative to *https://api.shutterstock.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authorize**](OauthApi.md#authorize) | **GET** /v2/oauth/authorize | Authorize applications |
| [**createAccessToken**](OauthApi.md#createAccessToken) | **POST** /v2/oauth/access_token | Get access tokens |


<a id="authorize"></a>
# **authorize**
> authorize(clientId, redirectUri, responseType, state, realm, scope)

Authorize applications

This endpoint returns a redirect URI (in the &#39;Location&#39; header) that the customer uses to authorize your application and, together with POST /v2/oauth/access_token, generate an access token that represents that authorization.

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
    defaultClient.setBasePath("https://api.shutterstock.com");

    OauthApi apiInstance = new OauthApi(defaultClient);
    String clientId = "6d097450b209c6dcd859"; // String | Client ID (Consumer Key) of your application
    String redirectUri = "localhost"; // String | The callback URI to send the request to after authorization; must use a host name that is registered with your application
    String responseType = "code"; // String | Type of temporary authorization code that will be used to generate an access code; the only valid value is 'code'
    String state = "1540290465000"; // String | Unique value used by the calling app to verify the request
    String realm = "customer"; // String | User type to be authorized (usually 'customer')
    String scope = "user.view"; // String | Space-separated list of scopes to be authorized
    try {
      apiInstance.authorize(clientId, redirectUri, responseType, state, realm, scope);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#authorize");
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
| **clientId** | **String**| Client ID (Consumer Key) of your application | |
| **redirectUri** | **String**| The callback URI to send the request to after authorization; must use a host name that is registered with your application | |
| **responseType** | **String**| Type of temporary authorization code that will be used to generate an access code; the only valid value is &#39;code&#39; | [enum: code] |
| **state** | **String**| Unique value used by the calling app to verify the request | |
| **realm** | **String**| User type to be authorized (usually &#39;customer&#39;) | [optional] [default to customer] [enum: customer, contributor] |
| **scope** | **String**| Space-separated list of scopes to be authorized | [optional] [default to user.view] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | Redirect user to authenticate with Shutterstock |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="createAccessToken"></a>
# **createAccessToken**
> OauthAccessTokenResponse createAccessToken(createAccessTokenRequest)

Get access tokens

This endpoint returns an access token for the specified user and with the specified scopes. The token does not expire until the user changes their password. The body parameters must be encoded as form data.

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
    defaultClient.setBasePath("https://api.shutterstock.com");

    OauthApi apiInstance = new OauthApi(defaultClient);
    CreateAccessTokenRequest createAccessTokenRequest = new CreateAccessTokenRequest(); // CreateAccessTokenRequest | 
    try {
      OauthAccessTokenResponse result = apiInstance.createAccessToken(createAccessTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#createAccessToken");
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
| **createAccessTokenRequest** | [**CreateAccessTokenRequest**](CreateAccessTokenRequest.md)|  | [optional] |

### Return type

[**OauthAccessTokenResponse**](OauthAccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

