# UserApi

All URIs are relative to *https://api.feedback.eu.pendo.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersGet**](UserApi.md#usersGet) | **GET** /users | fetch User records |
| [**usersIdDelete**](UserApi.md#usersIdDelete) | **DELETE** /users/{id} | Delete a User |
| [**usersIdGet**](UserApi.md#usersIdGet) | **GET** /users/{id} | Get a User record |
| [**usersIdPut**](UserApi.md#usersIdPut) | **PUT** /users/{id} | Update a User |
| [**usersIdTagsDelete**](UserApi.md#usersIdTagsDelete) | **DELETE** /users/{id}/tags | Delete custom User tags |
| [**usersIdTagsGet**](UserApi.md#usersIdTagsGet) | **GET** /users/{id}/tags | Get custom User tags |
| [**usersIdTagsPost**](UserApi.md#usersIdTagsPost) | **POST** /users/{id}/tags | Overwrite current custom User tags with the given tags |
| [**usersInviteEndUserPost**](UserApi.md#usersInviteEndUserPost) | **POST** /users/invite_end_user | Invite an EndUser (customer) |
| [**usersInviteVendorUserPost**](UserApi.md#usersInviteVendorUserPost) | **POST** /users/invite_vendor_user | Invite a VendorUser (Team member) |
| [**usersPost**](UserApi.md#usersPost) | **POST** /users | Ping to create or update an EndUser and Account in one call |
| [**usersSearchGet**](UserApi.md#usersSearchGet) | **GET** /users/search | Find a User with a query |
| [**vendorUsersPost**](UserApi.md#vendorUsersPost) | **POST** /vendor_users | Create or update a team member by their external_id |


<a id="usersGet"></a>
# **usersGet**
> List&lt;User&gt; usersGet(role, account, start, limit, orderBy, orderDir)

fetch User records

get a list of User records

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

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

    UserApi apiInstance = new UserApi(defaultClient);
    String role = "endUser"; // String | role
    Integer account = 56; // Integer | Filter by Account ID, if supplied. Only useful if role param is endUser
    Integer start = 0; // Integer | Offset to start at
    Integer limit = 300; // Integer | Limit the number of records returned. Max value can be 300. If limit is set to more than 300 the api will return an error
    String orderBy = "orderBy_example"; // String | The field to use for sort
    String orderDir = "asc"; // String | The sort direction
    try {
      List<User> result = apiInstance.usersGet(role, account, start, limit, orderBy, orderDir);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#usersGet");
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
| **role** | **String**| role | [enum: endUser, vendorUser] |
| **account** | **Integer**| Filter by Account ID, if supplied. Only useful if role param is endUser | [optional] |
| **start** | **Integer**| Offset to start at | [optional] [default to 0] |
| **limit** | **Integer**| Limit the number of records returned. Max value can be 300. If limit is set to more than 300 the api will return an error | [optional] [default to 300] |
| **orderBy** | **String**| The field to use for sort | [optional] |
| **orderDir** | **String**| The sort direction | [optional] [enum: asc, desc] |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User records |  -  |

<a id="usersIdDelete"></a>
# **usersIdDelete**
> User usersIdDelete(id)

Delete a User

This removes most traces of a User&#39;s existence from the system. For an EndUser you might want to consider just letting them churn after a period of inactivity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

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

    UserApi apiInstance = new UserApi(defaultClient);
    BigDecimal id = new BigDecimal(78); // BigDecimal | 
    try {
      User result = apiInstance.usersIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#usersIdDelete");
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
| **id** | **BigDecimal**|  | |

### Return type

[**User**](User.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the deleted User |  -  |

<a id="usersIdGet"></a>
# **usersIdGet**
> User usersIdGet(id)

Get a User record

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

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

    UserApi apiInstance = new UserApi(defaultClient);
    BigDecimal id = new BigDecimal(78); // BigDecimal | 
    try {
      User result = apiInstance.usersIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#usersIdGet");
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
| **id** | **BigDecimal**|  | |

### Return type

[**User**](User.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the User record |  -  |
| **410** | User has been deleted |  -  |

<a id="usersIdPut"></a>
# **usersIdPut**
> User usersIdPut(id, user)

Update a User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

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

    UserApi apiInstance = new UserApi(defaultClient);
    BigDecimal id = new BigDecimal(78); // BigDecimal | Feedback's User ID
    UsersIdPutRequest user = new UsersIdPutRequest(); // UsersIdPutRequest | 
    try {
      User result = apiInstance.usersIdPut(id, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#usersIdPut");
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
| **id** | **BigDecimal**| Feedback&#39;s User ID | |
| **user** | [**UsersIdPutRequest**](UsersIdPutRequest.md)|  | [optional] |

### Return type

[**User**](User.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updated User |  -  |

<a id="usersIdTagsDelete"></a>
# **usersIdTagsDelete**
> usersIdTagsDelete(id)

Delete custom User tags

Removes all custom tags associated with the User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

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

    UserApi apiInstance = new UserApi(defaultClient);
    BigDecimal id = new BigDecimal(78); // BigDecimal | Feedback's User ID
    try {
      apiInstance.usersIdTagsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#usersIdTagsDelete");
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
| **id** | **BigDecimal**| Feedback&#39;s User ID | |

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

<a id="usersIdTagsGet"></a>
# **usersIdTagsGet**
> usersIdTagsGet(id)

Get custom User tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

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

    UserApi apiInstance = new UserApi(defaultClient);
    BigDecimal id = new BigDecimal(78); // BigDecimal | Feedback's User ID
    try {
      apiInstance.usersIdTagsGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#usersIdTagsGet");
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
| **id** | **BigDecimal**| Feedback&#39;s User ID | |

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of maps specifying tags under each tag group, for example:  [  {&#39;impacts&#39; &#x3D;&gt; [&#39;sales&#39;]},  {&#39;resources&#39; &#x3D;&gt; [&#39;dev&#39;, &#39;test&#39;, &#39;support&#39;]}  ] |  -  |
| **404** | User not found |  -  |

<a id="usersIdTagsPost"></a>
# **usersIdTagsPost**
> usersIdTagsPost(id, tags)

Overwrite current custom User tags with the given tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

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

    UserApi apiInstance = new UserApi(defaultClient);
    BigDecimal id = new BigDecimal(78); // BigDecimal | Feedback's User ID
    Object tags = null; // Object | An array of maps specifying tags under each tag group, for example:  [  {'impacts' => ['sales']},  {'resources' => ['dev', 'test', 'support']}  ]
    try {
      apiInstance.usersIdTagsPost(id, tags);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#usersIdTagsPost");
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
| **id** | **BigDecimal**| Feedback&#39;s User ID | |
| **tags** | **Object**| An array of maps specifying tags under each tag group, for example:  [  {&#39;impacts&#39; &#x3D;&gt; [&#39;sales&#39;]},  {&#39;resources&#39; &#x3D;&gt; [&#39;dev&#39;, &#39;test&#39;, &#39;support&#39;]}  ] | |

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated User tags |  -  |
| **404** | User not found |  -  |

<a id="usersInviteEndUserPost"></a>
# **usersInviteEndUserPost**
> usersInviteEndUserPost(data)

Invite an EndUser (customer)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

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

    UserApi apiInstance = new UserApi(defaultClient);
    UsersInviteEndUserPostRequest data = new UsersInviteEndUserPostRequest(); // UsersInviteEndUserPostRequest | 
    try {
      apiInstance.usersInviteEndUserPost(data);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#usersInviteEndUserPost");
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
| **data** | [**UsersInviteEndUserPostRequest**](UsersInviteEndUserPostRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

<a id="usersInviteVendorUserPost"></a>
# **usersInviteVendorUserPost**
> usersInviteVendorUserPost(data)

Invite a VendorUser (Team member)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

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

    UserApi apiInstance = new UserApi(defaultClient);
    UsersInviteVendorUserPostRequest data = new UsersInviteVendorUserPostRequest(); // UsersInviteVendorUserPostRequest | 
    try {
      apiInstance.usersInviteVendorUserPost(data);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#usersInviteVendorUserPost");
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

<a id="usersPost"></a>
# **usersPost**
> usersPost(data)

Ping to create or update an EndUser and Account in one call

Replicates much of the functionality of the widget ping, allowing callers to create or update User records for End Users. If you call this with a new User and/or Account, the record will be created. If you call for an existing User/Account, the record will be updated. You can also call this at EndUser login time, or more frequently, to notify Feedback that the EndUser has been seen. This keeps Feedback&#39;s &#39;last seen&#39; data fresh and updates your reporting. This endpoint is used by our Zapier integration. The only value allowed in user.roles is &#39;endUser&#39;. The id you supply here for the User and Account should be your own unique id, which Feedback calls external_id. This probably isn&#39;t the same as Feedback&#39;s id seen elsewhere in the API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

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

    UserApi apiInstance = new UserApi(defaultClient);
    EndUserPing data = new EndUserPing(); // EndUserPing | the account and user
    try {
      apiInstance.usersPost(data);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#usersPost");
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
| **data** | [**EndUserPing**](EndUserPing.md)| the account and user | |

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
| **200** | Success |  -  |

<a id="usersSearchGet"></a>
# **usersSearchGet**
> User usersSearchGet(externalId, email, role)

Find a User with a query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

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

    UserApi apiInstance = new UserApi(defaultClient);
    String externalId = "externalId_example"; // String | Find using your external ID, rather than the ID generated by Feedback
    String email = "email_example"; // String | Find user by their email address. Role param must be specified when using this option
    String role = "endUser"; // String | Users role ('vendorUser' or 'endUser'). Only useful when finding a user by their email address
    try {
      User result = apiInstance.usersSearchGet(externalId, email, role);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#usersSearchGet");
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
| **externalId** | **String**| Find using your external ID, rather than the ID generated by Feedback | [optional] |
| **email** | **String**| Find user by their email address. Role param must be specified when using this option | [optional] |
| **role** | **String**| Users role (&#39;vendorUser&#39; or &#39;endUser&#39;). Only useful when finding a user by their email address | [optional] [enum: endUser, vendorUser] |

### Return type

[**User**](User.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the User record |  -  |
| **410** | User has been deleted |  -  |

<a id="vendorUsersPost"></a>
# **vendorUsersPost**
> vendorUsersPost(data)

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
import org.openapitools.client.api.UserApi;

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

    UserApi apiInstance = new UserApi(defaultClient);
    VendorUsersPostRequest data = new VendorUsersPostRequest(); // VendorUsersPostRequest | 
    try {
      apiInstance.vendorUsersPost(data);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#vendorUsersPost");
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

