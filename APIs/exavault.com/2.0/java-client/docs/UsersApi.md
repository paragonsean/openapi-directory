# UsersApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addUser**](UsersApi.md#addUser) | **POST** /users | Create a user |
| [**deleteUser**](UsersApi.md#deleteUser) | **DELETE** /users/{id} | Delete a user |
| [**getUserById**](UsersApi.md#getUserById) | **GET** /users/{id} | Get info for a user |
| [**listUsers**](UsersApi.md#listUsers) | **GET** /users | Get a list of users |
| [**updateUser**](UsersApi.md#updateUser) | **PATCH** /users/{id} | Update a user |


<a id="addUser"></a>
# **addUser**
> UserResponse addUser(evApiKey, evAccessToken, addUserRequestBody)

Create a user

Adds a new user to the account. The user may be configured as an admin or standard user, and (if a standard user) may be assigned a restricted [home directory](/docs/account/04-users/00-introduction#setting-the-user-s-home-directory) and restricted [permissions](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions).   **Notes:**  - You must be an [admin-level user](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to use this.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API key required to make the API call
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    AddUserRequestBody addUserRequestBody = new AddUserRequestBody(); // AddUserRequestBody | 
    try {
      UserResponse result = apiInstance.addUser(evApiKey, evAccessToken, addUserRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#addUser");
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
| **evApiKey** | **String**| API key required to make the API call | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **addUserRequestBody** | [**AddUserRequestBody**](AddUserRequestBody.md)|  | [optional] |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Operation |  -  |

<a id="deleteUser"></a>
# **deleteUser**
> EmptyResponse deleteUser(id, evApiKey, evAccessToken)

Delete a user

Delete a user from the account. Deleting a user does **NOT** delete any files from the account; it merely removes a user&#39;s access. Aternatively, locking a user via the [PATCH /users/{id}](#operation/updateUser) will keep the user in your account, but make it unable to log in.   Resources and shares owned by the deleted user will be owned by the master user after the deletion.  **Notes:**   - You must have [admin-level access](/docs/account/04-users/01-admin-users) to delete a user. - The primary owner of the account cannot be deleted. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 2224; // Integer | The user's ID. Note that this is our internal ID, and _not the username_. You can obtain it by calling the [GET /users](#operation/listUsers) method.
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
    String evAccessToken = "19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1"; // String | Access token required to make the API call.
    try {
      EmptyResponse result = apiInstance.deleteUser(id, evApiKey, evAccessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#deleteUser");
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
| **id** | **Integer**| The user&#39;s ID. Note that this is our internal ID, and _not the username_. You can obtain it by calling the [GET /users](#operation/listUsers) method. | |
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="getUserById"></a>
# **getUserById**
> UserResponse getUserById(id, evApiKey, evAccessToken, include)

Get info for a user

Get the details for a specific user. You can use the &#x60;include&#x60; parameter to also get the details of related records, such as the account or the home directory.  **Notes:**  - You must have [admin or master](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) access to use this.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 2224; // Integer | The user's ID. Note that this is our internal ID, and _not the username_. You can obtain it by calling the [GET /users](#operation/listUsers) method.
    String evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key
    String evAccessToken = "19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1"; // String | Access token required to make the API call.
    String include = "homeResource,ownerAccount"; // String | Comma-separated list of relationships to include in response. Possible values include **homeResource** and **ownerAccount**.
    try {
      UserResponse result = apiInstance.getUserById(id, evApiKey, evAccessToken, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUserById");
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
| **id** | **Integer**| The user&#39;s ID. Note that this is our internal ID, and _not the username_. You can obtain it by calling the [GET /users](#operation/listUsers) method. | |
| **evApiKey** | **String**| API Key | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **include** | **String**| Comma-separated list of relationships to include in response. Possible values include **homeResource** and **ownerAccount**. | [optional] |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="listUsers"></a>
# **listUsers**
> UserCollectionResponse listUsers(evApiKey, evAccessToken, username, homeResource, nickname, email, role, status, search, offset, sort, limit, include)

Get a list of users

Get a list of the users in your account. There are three main types of searches you can do with this method:  1. Search for a user by username. If you provide the &#x60;username&#x60; parameter in your call, then only the user who exactly matches that username will be in the list of matches. Any other parameters are ignored. 1. Search for a user by individual filter fields (&#x60;nickname&#x60;,&#x60;email&#x60;,&#x60;role&#x60;,&#x60;status&#x60;,&#x60;homeDir&#x60;). Users in the list will be ones who match all of the filters you choose to search by. For example, you could look for users with the \&quot;admin\&quot; &#x60;role&#x60; AND &#x60;email&#x60; addresses ending in \&quot;*@acme.com\&quot;.  1. Search for a user by search string. If you provide the &#x60;search&#x60; parameter, users whose nickname OR email OR role OR homeDir match value your provide.  **Notes:**  - You must be an [admin-level user](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to use this. - The homeDir is the full path to the user&#39;s home directory, not a resource ID or hash.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    String username = "testuser"; // String | The username of the user you are looking for. Only entries with the same username as this will be in the list of results. Does not support wildcard searches.
    String homeResource = "homeResource_example"; // String | Resource identifier for user's home directory. Does not support wildcard searches.
    String nickname = "nickname_example"; // String | Nickname to search for. Ignored if `username` is provided. Supports wildcard searches.
    String email = "*@example.co"; // String | Email to search for. Ignored if `username` is provided. Supports wildcard searches
    String role = "use"; // String | Types of users to include the list. Ignored if `username` is provided. Valid options are **admin**, **master** and **user**
    Integer status = 56; // Integer | Whether a user is locked. Ignored if `username` is provided. **0** means user is locked, **1** means user is not locked. 
    String search = "search_example"; // String | Searches the nickname, email, role and homeDir fields for the provided value. Ignored if `username` is provided. Supports wildcard searches.
    Integer offset = 50; // Integer | Starting user record in the result set. Can be used for pagination.
    String sort = "homeDir,-modified"; // String | Sort order or matching users. You can sort by multiple columns by separating sort options with a comma; the sort will be applied in the order specified. The sort order for each sort field is ascending unless it is prefixed with a minus (“-“), in which case it will be descending.  Valid sort fields are: **nickname**, **username**, **email**, **homeDir** and **modified**
    Integer limit = 100; // Integer | Number of users to return. Can be used for pagination.
    String include = "homeResource,ownerAccount"; // String | Comma separated list of relationships to include in response. Valid options are **homeResource** and **ownerAccount**.
    try {
      UserCollectionResponse result = apiInstance.listUsers(evApiKey, evAccessToken, username, homeResource, nickname, email, role, status, search, offset, sort, limit, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#listUsers");
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
| **evApiKey** | **String**| API key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **username** | **String**| The username of the user you are looking for. Only entries with the same username as this will be in the list of results. Does not support wildcard searches. | [optional] |
| **homeResource** | **String**| Resource identifier for user&#39;s home directory. Does not support wildcard searches. | [optional] |
| **nickname** | **String**| Nickname to search for. Ignored if &#x60;username&#x60; is provided. Supports wildcard searches. | [optional] |
| **email** | **String**| Email to search for. Ignored if &#x60;username&#x60; is provided. Supports wildcard searches | [optional] |
| **role** | **String**| Types of users to include the list. Ignored if &#x60;username&#x60; is provided. Valid options are **admin**, **master** and **user** | [optional] |
| **status** | **Integer**| Whether a user is locked. Ignored if &#x60;username&#x60; is provided. **0** means user is locked, **1** means user is not locked.  | [optional] |
| **search** | **String**| Searches the nickname, email, role and homeDir fields for the provided value. Ignored if &#x60;username&#x60; is provided. Supports wildcard searches. | [optional] |
| **offset** | **Integer**| Starting user record in the result set. Can be used for pagination. | [optional] |
| **sort** | **String**| Sort order or matching users. You can sort by multiple columns by separating sort options with a comma; the sort will be applied in the order specified. The sort order for each sort field is ascending unless it is prefixed with a minus (“-“), in which case it will be descending.  Valid sort fields are: **nickname**, **username**, **email**, **homeDir** and **modified** | [optional] |
| **limit** | **Integer**| Number of users to return. Can be used for pagination. | [optional] |
| **include** | **String**| Comma separated list of relationships to include in response. Valid options are **homeResource** and **ownerAccount**. | [optional] |

### Return type

[**UserCollectionResponse**](UserCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="updateUser"></a>
# **updateUser**
> UserResponse updateUser(id, evApiKey, evAccessToken, updateUserRequestBody)

Update a user

Updates the settings for the user. Note that the unique key for this API call is our internal ID, and _not_ the username, as the username can be changed.  In the request body, you should only send the parameters for values that you wish to change for the user.  **Notes:**  - You must have [admin or master](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) access to edit other users. If you have user-level access, you can only update your own user settings. - You cannot edit a master user with this method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 2224; // Integer | The user's ID. Note that this is our internal ID, and _not the username_. You can obtain it by calling the [GET /users](#operation/listUsers) method.
    String evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API key required to make the API call.
    String evAccessToken = "19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1"; // String | Access token required to make the API call.
    UpdateUserRequestBody updateUserRequestBody = new UpdateUserRequestBody(); // UpdateUserRequestBody | 
    try {
      UserResponse result = apiInstance.updateUser(id, evApiKey, evAccessToken, updateUserRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#updateUser");
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
| **id** | **Integer**| The user&#39;s ID. Note that this is our internal ID, and _not the username_. You can obtain it by calling the [GET /users](#operation/listUsers) method. | |
| **evApiKey** | **String**| API key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **updateUserRequestBody** | [**UpdateUserRequestBody**](UpdateUserRequestBody.md)|  | [optional] |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

