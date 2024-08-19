# AuthApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authOauthTokenPost**](AuthApi.md#authOauthTokenPost) | **POST** /auth/oauth/token | Send client credentials and get an access token. |


<a id="authOauthTokenPost"></a>
# **authOauthTokenPost**
> authOauthTokenPost(clientId, clientSecret, grantType, scope)

Send client credentials and get an access token.

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
    String clientId = "clientId_example"; // String | Your app's client_id. Get from API dashboard.
    String clientSecret = "clientSecret_example"; // String | Your app's client_secret. Get from API dashboard.
    String grantType = "client_credentials"; // String | Grant Type.
    String scope = "verse chapter"; // String | The resources that you would like to access.
    try {
      apiInstance.authOauthTokenPost(clientId, clientSecret, grantType, scope);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#authOauthTokenPost");
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
| **clientId** | **String**| Your app&#39;s client_id. Get from API dashboard. | |
| **clientSecret** | **String**| Your app&#39;s client_secret. Get from API dashboard. | |
| **grantType** | **String**| Grant Type. | [default to client_credentials] |
| **scope** | **String**| The resources that you would like to access. | [default to verse chapter] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success: Everything worked as expected. |  -  |
| **400** | Bad Request: The request was unacceptable due to wrong parameter(s). |  -  |
| **401** | Unauthorized: Invalid access_token used. |  -  |
| **402** | Request Failed. |  -  |
| **500** | Server Error: Something went wrong on our end. |  -  |

