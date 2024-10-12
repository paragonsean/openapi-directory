# UsersApi

All URIs are relative to *https://io.adafruit.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**currentUser**](UsersApi.md#currentUser) | **GET** /user | Get information about the current user |
| [**getCurrentUserThrottle**](UsersApi.md#getCurrentUserThrottle) | **GET** /{username}/throttle | Get the user&#39;s data rate limit and current activity level. |


<a id="currentUser"></a>
# **currentUser**
> User currentUser()

Get information about the current user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      User result = apiInstance.currentUser();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#currentUser");
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

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A User record |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="getCurrentUserThrottle"></a>
# **getCurrentUserThrottle**
> GetCurrentUserThrottle200Response getCurrentUserThrottle(username)

Get the user&#39;s data rate limit and current activity level.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    try {
      GetCurrentUserThrottle200Response result = apiInstance.getCurrentUserThrottle(username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getCurrentUserThrottle");
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
| **username** | **String**| a valid username string | |

### Return type

[**GetCurrentUserThrottle200Response**](GetCurrentUserThrottle200Response.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data rate limit and current actions. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

