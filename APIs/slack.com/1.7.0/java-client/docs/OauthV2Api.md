# OauthV2Api

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**oauthV2Access**](OauthV2Api.md#oauthV2Access) | **GET** /oauth.v2.access |  |


<a id="oauthV2Access"></a>
# **oauthV2Access**
> DefaultSuccessTemplate oauthV2Access(code, clientId, clientSecret, redirectUri)



Exchanges a temporary OAuth verifier code for an access token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    OauthV2Api apiInstance = new OauthV2Api(defaultClient);
    String code = "code_example"; // String | The `code` param returned via the OAuth callback.
    String clientId = "clientId_example"; // String | Issued when you created your application.
    String clientSecret = "clientSecret_example"; // String | Issued when you created your application.
    String redirectUri = "redirectUri_example"; // String | This must match the originally submitted URI (if one was sent).
    try {
      DefaultSuccessTemplate result = apiInstance.oauthV2Access(code, clientId, clientSecret, redirectUri);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthV2Api#oauthV2Access");
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

