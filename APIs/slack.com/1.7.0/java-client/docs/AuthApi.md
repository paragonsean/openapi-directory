# AuthApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authRevoke**](AuthApi.md#authRevoke) | **GET** /auth.revoke |  |
| [**authTest**](AuthApi.md#authTest) | **GET** /auth.test |  |


<a id="authRevoke"></a>
# **authRevoke**
> AuthRevokeSchema authRevoke(token, test)



Revokes a token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AuthApi apiInstance = new AuthApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `none`
    Boolean test = true; // Boolean | Setting this parameter to `1` triggers a _testing mode_ where the specified token will not actually be revoked.
    try {
      AuthRevokeSchema result = apiInstance.authRevoke(token, test);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#authRevoke");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;none&#x60; | |
| **test** | **Boolean**| Setting this parameter to &#x60;1&#x60; triggers a _testing mode_ where the specified token will not actually be revoked. | [optional] |

### Return type

[**AuthRevokeSchema**](AuthRevokeSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="authTest"></a>
# **authTest**
> AuthTestSuccessSchema authTest(token)



Checks authentication &amp; identity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AuthApi apiInstance = new AuthApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `none`
    try {
      AuthTestSuccessSchema result = apiInstance.authTest(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#authTest");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;none&#x60; | |

### Return type

[**AuthTestSuccessSchema**](AuthTestSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Standard success response when used with a user token |  -  |
| **0** | Standard failure response when used with an invalid token |  -  |

