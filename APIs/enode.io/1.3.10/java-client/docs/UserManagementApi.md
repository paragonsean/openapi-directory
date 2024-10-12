# UserManagementApi

All URIs are relative to *https://api.test.enode.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteUsersUserid**](UserManagementApi.md#deleteUsersUserid) | **DELETE** /users/{userId} | Unlink User |
| [**deleteUsersUseridAuthorization**](UserManagementApi.md#deleteUsersUseridAuthorization) | **DELETE** /users/{userId}/authorization | Deauthorize User |
| [**postUsersUseridLink**](UserManagementApi.md#postUsersUseridLink) | **POST** /users/{userId}/link | Link User |


<a id="deleteUsersUserid"></a>
# **deleteUsersUserid**
> deleteUsersUserid(userId)

Unlink User

Deletes a User and all of their data permanently, and invalidates any associated sessions, authorization codes, and access/refresh tokens

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: ClientAccessToken
    OAuth ClientAccessToken = (OAuth) defaultClient.getAuthentication("ClientAccessToken");
    ClientAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    UserManagementApi apiInstance = new UserManagementApi(defaultClient);
    String userId = "userId_example"; // String | ID of the User
    try {
      apiInstance.deleteUsersUserid(userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserManagementApi#deleteUsersUserid");
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
| **userId** | **String**| ID of the User | |

### Return type

null (empty response body)

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="deleteUsersUseridAuthorization"></a>
# **deleteUsersUseridAuthorization**
> deleteUsersUseridAuthorization(userId)

Deauthorize User

Deletes the User&#39;s stored vendor authorizations and credentials, invalidates any associated sessions, authorization codes, and access/refresh tokens.  All other User data is retained, and if the User is sent through the Link User flow in the future their account will be just as they left it.  No webhook events will be generated for a deauthorized user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: ClientAccessToken
    OAuth ClientAccessToken = (OAuth) defaultClient.getAuthentication("ClientAccessToken");
    ClientAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    UserManagementApi apiInstance = new UserManagementApi(defaultClient);
    String userId = "userId_example"; // String | ID of the User
    try {
      apiInstance.deleteUsersUseridAuthorization(userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserManagementApi#deleteUsersUseridAuthorization");
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
| **userId** | **String**| ID of the User | |

### Return type

null (empty response body)

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="postUsersUseridLink"></a>
# **postUsersUseridLink**
> PostUsersUseridLink200Response postUsersUseridLink(userId, postUsersUseridLinkRequest)

Link User

Creates an Enode Link session attached to the provided User ID. If this User does not exist, it will be created. The returned &#x60;linkState&#x60; gives the user short-lived access to Enode Link.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: ClientAccessToken
    OAuth ClientAccessToken = (OAuth) defaultClient.getAuthentication("ClientAccessToken");
    ClientAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    UserManagementApi apiInstance = new UserManagementApi(defaultClient);
    String userId = "userId_example"; // String | ID of the User
    PostUsersUseridLinkRequest postUsersUseridLinkRequest = new PostUsersUseridLinkRequest(); // PostUsersUseridLinkRequest | 
    try {
      PostUsersUseridLink200Response result = apiInstance.postUsersUseridLink(userId, postUsersUseridLinkRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserManagementApi#postUsersUseridLink");
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
| **userId** | **String**| ID of the User | |
| **postUsersUseridLinkRequest** | [**PostUsersUseridLinkRequest**](PostUsersUseridLinkRequest.md)|  | [optional] |

### Return type

[**PostUsersUseridLink200Response**](PostUsersUseridLink200Response.md)

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |

