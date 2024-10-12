# TeamApi

All URIs are relative to *https://api.feedback.eu.pendo.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersInviteVendorUserPost_0**](TeamApi.md#usersInviteVendorUserPost_0) | **POST** /users/invite_vendor_user | Invite a VendorUser (Team member) |
| [**vendorUsersPost_0**](TeamApi.md#vendorUsersPost_0) | **POST** /vendor_users | Create or update a team member by their external_id |


<a id="usersInviteVendorUserPost_0"></a>
# **usersInviteVendorUserPost_0**
> usersInviteVendorUserPost_0(data)

Invite a VendorUser (Team member)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.feedback.eu.pendo.io");
    
    // Configure API key authorization: userApiKey (request header)
    ApiKeyAuth userApiKey (request header) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (request header)");
    userApiKey (request header).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (request header).setApiKeyPrefix("Token");

    // Configure API key authorization: userApiKey (query parameter)
    ApiKeyAuth userApiKey (query parameter) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (query parameter)");
    userApiKey (query parameter).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (query parameter).setApiKeyPrefix("Token");

    TeamApi apiInstance = new TeamApi(defaultClient);
    UsersInviteVendorUserPostRequest data = new UsersInviteVendorUserPostRequest(); // UsersInviteVendorUserPostRequest | 
    try {
      apiInstance.usersInviteVendorUserPost_0(data);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamApi#usersInviteVendorUserPost_0");
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
| **data** | [**UsersInviteVendorUserPostRequest**](UsersInviteVendorUserPostRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

<a id="vendorUsersPost_0"></a>
# **vendorUsersPost_0**
> vendorUsersPost_0(data)

Create or update a team member by their external_id

the POST /vendor_users is very similar to the POST /users/invite_vendor_user but /vendor_users is intended for consumers to refresh team member data periodically, rather than just a one-off user creation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.feedback.eu.pendo.io");
    
    // Configure API key authorization: userApiKey (request header)
    ApiKeyAuth userApiKey (request header) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (request header)");
    userApiKey (request header).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (request header).setApiKeyPrefix("Token");

    // Configure API key authorization: userApiKey (query parameter)
    ApiKeyAuth userApiKey (query parameter) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (query parameter)");
    userApiKey (query parameter).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (query parameter).setApiKeyPrefix("Token");

    TeamApi apiInstance = new TeamApi(defaultClient);
    VendorUsersPostRequest data = new VendorUsersPostRequest(); // VendorUsersPostRequest | 
    try {
      apiInstance.vendorUsersPost_0(data);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamApi#vendorUsersPost_0");
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
| **data** | [**VendorUsersPostRequest**](VendorUsersPostRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

