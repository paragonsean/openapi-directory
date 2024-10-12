# AccountApi

All URIs are relative to *https://api.flat.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAuthenticatedUser**](AccountApi.md#getAuthenticatedUser) | **GET** /me | Get current user profile |


<a id="getAuthenticatedUser"></a>
# **getAuthenticatedUser**
> UserDetails getAuthenticatedUser(onlyId)

Get current user profile

Get details about the current authenticated User. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountApi apiInstance = new AccountApi(defaultClient);
    Boolean onlyId = false; // Boolean | Only return the user id
    try {
      UserDetails result = apiInstance.getAuthenticatedUser(onlyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#getAuthenticatedUser");
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
| **onlyId** | **Boolean**| Only return the user id | [optional] [default to false] |

### Return type

[**UserDetails**](UserDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current user details |  -  |
| **0** | Error |  -  |

