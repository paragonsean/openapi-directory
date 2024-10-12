# UsersApi

All URIs are relative to *https://api.nextauth.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteUser**](UsersApi.md#deleteUser) | **DELETE** /servers/{serverid}/users/{userid}/ | Delete a specific user |
| [**deleteUserAccounts**](UsersApi.md#deleteUserAccounts) | **DELETE** /servers/{serverid}/users/{userid}/accounts | Delete all accounts of a specific user |
| [**deleteUserAttribute**](UsersApi.md#deleteUserAttribute) | **DELETE** /servers/{serverid}/users/{userid}/attributes/{attributekey} | Delete specific attribute of a specific user |
| [**deleteUserAttributes**](UsersApi.md#deleteUserAttributes) | **DELETE** /servers/{serverid}/users/{userid}/attributes/ | Delete all attributes of a specific user |
| [**getUser**](UsersApi.md#getUser) | **GET** /servers/{serverid}/users/{userid}/accounts | Get all accounts of a specific user |
| [**getUserAttributes**](UsersApi.md#getUserAttributes) | **GET** /servers/{serverid}/users/{userid}/attributes/ | Get all attributes of a specific user |
| [**getUsers**](UsersApi.md#getUsers) | **GET** /servers/{serverid}/users/ | Get all users |
| [**registerUser**](UsersApi.md#registerUser) | **POST** /servers/{serverid}/sessions/registeruser | Register a userid for the currently logged in account. |
| [**setUserAttributes**](UsersApi.md#setUserAttributes) | **POST** /servers/{serverid}/users/{userid}/attributes/ | Set all attributes of a specific user |
| [**updateUserAttributes**](UsersApi.md#updateUserAttributes) | **PUT** /servers/{serverid}/users/{userid}/attributes/ | Update specified attributes of a specific user |


<a id="deleteUser"></a>
# **deleteUser**
> deleteUser(serverid, userid)

Delete a specific user

Delete a user. Required permission: &#39;users&#39;.

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
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String userid = "userid_example"; // String | User name
    try {
      apiInstance.deleteUser(serverid, userid);
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
| **serverid** | **String**| Base64 encoded server id | |
| **userid** | **String**| User name | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | On successful delete |  -  |
| **404** | User not found |  -  |

<a id="deleteUserAccounts"></a>
# **deleteUserAccounts**
> deleteUserAccounts(serverid, userid)

Delete all accounts of a specific user

Delete all accounts corresponding to this user. The user itself is not deleted. Required permission: &#39;accounts&#39; or &#39;users&#39;.

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
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String userid = "userid_example"; // String | User name
    try {
      apiInstance.deleteUserAccounts(serverid, userid);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#deleteUserAccounts");
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
| **serverid** | **String**| Base64 encoded server id | |
| **userid** | **String**| User name | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | On successful delete |  -  |

<a id="deleteUserAttribute"></a>
# **deleteUserAttribute**
> deleteUserAttribute(serverid, userid, attributekey)

Delete specific attribute of a specific user

Delete attribute with the specified key of a specific user. Required permission: &#39;users&#39;.

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
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String userid = "userid_example"; // String | User name
    String attributekey = "attributekey_example"; // String | Key of the attribute
    try {
      apiInstance.deleteUserAttribute(serverid, userid, attributekey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#deleteUserAttribute");
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
| **serverid** | **String**| Base64 encoded server id | |
| **userid** | **String**| User name | |
| **attributekey** | **String**| Key of the attribute | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | On successful delete |  -  |
| **404** | User not found |  -  |

<a id="deleteUserAttributes"></a>
# **deleteUserAttributes**
> deleteUserAttributes(serverid, userid)

Delete all attributes of a specific user

Delete all attributes of a specific user. Required permission: &#39;users&#39;.

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
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String userid = "userid_example"; // String | User name
    try {
      apiInstance.deleteUserAttributes(serverid, userid);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#deleteUserAttributes");
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
| **serverid** | **String**| Base64 encoded server id | |
| **userid** | **String**| User name | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | On successful delete |  -  |
| **404** | User not found |  -  |

<a id="getUser"></a>
# **getUser**
> Accounts getUser(serverid, userid, limit, marker, sort)

Get all accounts of a specific user

Returns an array containing all accounts corresponding to this user. Required permission: &#39;sessions&#39; or &#39;users&#39;.

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
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String userid = "userid_example"; // String | User name
    Integer limit = 56; // Integer | Limit the number of results
    Integer marker = 56; // Integer | Offset in the result list
    String sort = "sort_example"; // String | Sort the results by column. You can also specify ascending (default if not specified) or descending, e.g., *column:asc* . You can also sort by multiple columns, e.g., *column1:desc,column2:asc*
    try {
      Accounts result = apiInstance.getUser(serverid, userid, limit, marker, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUser");
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
| **serverid** | **String**| Base64 encoded server id | |
| **userid** | **String**| User name | |
| **limit** | **Integer**| Limit the number of results | [optional] |
| **marker** | **Integer**| Offset in the result list | [optional] |
| **sort** | **String**| Sort the results by column. You can also specify ascending (default if not specified) or descending, e.g., *column:asc* . You can also sort by multiple columns, e.g., *column1:desc,column2:asc* | [optional] |

### Return type

[**Accounts**](Accounts.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of accounts |  -  |

<a id="getUserAttributes"></a>
# **getUserAttributes**
> String getUserAttributes(serverid, userid)

Get all attributes of a specific user

Returns an array containing all attributes corresponding to this user. Required permission: &#39;sessions&#39; or &#39;users&#39;.

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
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String userid = "userid_example"; // String | User name
    try {
      String result = apiInstance.getUserAttributes(serverid, userid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUserAttributes");
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
| **serverid** | **String**| Base64 encoded server id | |
| **userid** | **String**| User name | |

### Return type

**String**

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of attributes |  -  |
| **404** | User not found |  -  |

<a id="getUsers"></a>
# **getUsers**
> Users getUsers(serverid, filter, search, limit, marker, sort)

Get all users

Returns an array of arrays containing all accounts corresponding to all users. Required permission: &#39;users&#39;.

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
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String filter = "filter_example"; // String | Filter users based on an attribute. Takes the format *attributename=attributevalue*. You can filter for multiple values at once, e.g. *group=in:group1,group2*
    String search = "search_example"; // String | Search for a username LIKE %search%
    Integer limit = 56; // Integer | Limit the number of results
    Integer marker = 56; // Integer | Offset in the result list
    String sort = "sort_example"; // String | Sort the results by column. You can also specify ascending (default if not specified) or descending, e.g., *column:asc* . You can also sort by multiple columns, e.g., *column1:desc,column2:asc*
    try {
      Users result = apiInstance.getUsers(serverid, filter, search, limit, marker, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUsers");
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
| **serverid** | **String**| Base64 encoded server id | |
| **filter** | **String**| Filter users based on an attribute. Takes the format *attributename&#x3D;attributevalue*. You can filter for multiple values at once, e.g. *group&#x3D;in:group1,group2* | [optional] |
| **search** | **String**| Search for a username LIKE %search% | [optional] |
| **limit** | **Integer**| Limit the number of results | [optional] |
| **marker** | **Integer**| Offset in the result list | [optional] |
| **sort** | **String**| Sort the results by column. You can also specify ascending (default if not specified) or descending, e.g., *column:asc* . You can also sort by multiple columns, e.g., *column1:desc,column2:asc* | [optional] |

### Return type

[**Users**](Users.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of users |  -  |

<a id="registerUser"></a>
# **registerUser**
> registerUser(serverid, xNonce, userid)

Register a userid for the currently logged in account.

Register a user for the currently logged in account. You can also directly pass a user name when generating an ENROL qr code. Required permission: &#39;users&#39;.

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
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
    String userid = "userid_example"; // String | Username to register
    try {
      apiInstance.registerUser(serverid, xNonce, userid);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#registerUser");
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
| **serverid** | **String**| Base64 encoded server id | |
| **xNonce** | **String**| Nonce to identify the browser/webserver session | |
| **userid** | **String**| Username to register | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="setUserAttributes"></a>
# **setUserAttributes**
> setUserAttributes(serverid, userid, attributes)

Set all attributes of a specific user

Set the attributes of a specific user. Prior attributes with keys that are not provided in the body of the request will be deleted. Creates the user if not exists. Required permission: &#39;users&#39;.

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
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String userid = "userid_example"; // String | User name
    Object attributes = null; // Object | Array of attributes
    try {
      apiInstance.setUserAttributes(serverid, userid, attributes);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#setUserAttributes");
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
| **serverid** | **String**| Base64 encoded server id | |
| **userid** | **String**| User name | |
| **attributes** | **Object**| Array of attributes | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateUserAttributes"></a>
# **updateUserAttributes**
> updateUserAttributes(serverid, userid, attributes)

Update specified attributes of a specific user

Update the specified attributes of a specific user. Prior attributes with keys that are not provided in the body of the request will not be deleted. Required permission: &#39;users&#39;.

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
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String userid = "userid_example"; // String | User name
    Object attributes = null; // Object | Array of attributes
    try {
      apiInstance.updateUserAttributes(serverid, userid, attributes);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#updateUserAttributes");
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
| **serverid** | **String**| Base64 encoded server id | |
| **userid** | **String**| User name | |
| **attributes** | **Object**| Array of attributes | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | On successful update |  -  |
| **404** | User not found |  -  |

