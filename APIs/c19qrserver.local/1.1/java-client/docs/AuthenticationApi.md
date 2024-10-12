# AuthenticationApi

All URIs are relative to *http://c19qrserver.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**loginPost**](AuthenticationApi.md#loginPost) | **POST** /login | Log in to get an API token |
| [**logoutPost**](AuthenticationApi.md#logoutPost) | **POST** /logout | Log out |


<a id="loginPost"></a>
# **loginPost**
> LoginResponse loginPost(sample1)

Log in to get an API token

Submit your email and password to get an API token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://c19qrserver.local");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    Sample1 sample1 = new Sample1(); // Sample1 | The login payload
    try {
      LoginResponse result = apiInstance.loginPost(sample1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#loginPost");
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
| **sample1** | [**Sample1**](Sample1.md)| The login payload | |

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="logoutPost"></a>
# **logoutPost**
> logoutPost()

Log out

Log out by deleting your token off the server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://c19qrserver.local");
    
    // Configure API key authorization: TokenHeader
    ApiKeyAuth TokenHeader = (ApiKeyAuth) defaultClient.getAuthentication("TokenHeader");
    TokenHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenHeader.setApiKeyPrefix("Token");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    try {
      apiInstance.logoutPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#logoutPost");
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

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

