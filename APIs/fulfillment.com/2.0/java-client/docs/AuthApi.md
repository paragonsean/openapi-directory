# AuthApi

All URIs are relative to *https://api.fulfillment.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postOauthAccessToken**](AuthApi.md#postOauthAccessToken) | **POST** /oauth/access_token | Generate an Access Token |


<a id="postOauthAccessToken"></a>
# **postOauthAccessToken**
> AccessTokenResponseV2 postOauthAccessToken(body)

Generate an Access Token

By default tokens are valid for 7 days while refresh tokens are valid for 30 days. If your &#x60;grant_type&#x60; is \&quot;password\&quot; include the &#x60;username&#x60; and &#x60;password&#x60;, if however your &#x60;grant_type&#x60; is \&quot;refresh_token\&quot; the username/password are not required, instead set the &#x60;refresh_token&#x60;

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
    defaultClient.setBasePath("https://api.fulfillment.com/v2");

    AuthApi apiInstance = new AuthApi(defaultClient);
    AccessTokenRequestV2 body = new AccessTokenRequestV2(); // AccessTokenRequestV2 | Get an access token
    try {
      AccessTokenResponseV2 result = apiInstance.postOauthAccessToken(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#postOauthAccessToken");
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
| **body** | [**AccessTokenRequestV2**](AccessTokenRequestV2.md)| Get an access token | |

### Return type

[**AccessTokenResponseV2**](AccessTokenResponseV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Authorized |  -  |
| **401** | Unauthorized |  -  |

