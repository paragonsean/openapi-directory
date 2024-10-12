# UsersFindAndModifyUsersApi

All URIs are relative to *https://market.openchannel.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersGet**](UsersFindAndModifyUsersApi.md#usersGet) | **GET** /users | Returns a paginated list of users |
| [**usersUserIdDelete**](UsersFindAndModifyUsersApi.md#usersUserIdDelete) | **DELETE** /users/{userId} | Removes a single user |
| [**usersUserIdGet**](UsersFindAndModifyUsersApi.md#usersUserIdGet) | **GET** /users/{userId} | Return a single user |
| [**usersUserIdPatch**](UsersFindAndModifyUsersApi.md#usersUserIdPatch) | **PATCH** /users/{userId} | Updates user fields |
| [**usersUserIdPost**](UsersFindAndModifyUsersApi.md#usersUserIdPost) | **POST** /users/{userId} | Updates a single user or adds the user if they don&#39;t exist |


<a id="usersGet"></a>
# **usersGet**
> UserPages usersGet(query, sort, pageNumber, limit)

Returns a paginated list of users

- Results are paginated and the default is value is 100 if no limit is provided 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersFindAndModifyUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    UsersFindAndModifyUsersApi apiInstance = new UsersFindAndModifyUsersApi(defaultClient);
    String query = "query_example"; // String | A query document. Example: {'name':'John'} matches all the users that have the name 'John'
    String sort = "sort_example"; // String | A sort document. Example: {'name':1} sorts the results by name in ascending order
    Integer pageNumber = 56; // Integer | The result set page number to be returned
    Integer limit = 56; // Integer | The maximum number of results to return per page
    try {
      UserPages result = apiInstance.usersGet(query, sort, pageNumber, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersFindAndModifyUsersApi#usersGet");
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
| **query** | **String**| A query document. Example: {&#39;name&#39;:&#39;John&#39;} matches all the users that have the name &#39;John&#39; | [optional] |
| **sort** | **String**| A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order | [optional] |
| **pageNumber** | **Integer**| The result set page number to be returned | [optional] |
| **limit** | **Integer**| The maximum number of results to return per page | [optional] |

### Return type

[**UserPages**](UserPages.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **0** | OK |  -  |

<a id="usersUserIdDelete"></a>
# **usersUserIdDelete**
> usersUserIdDelete(userId)

Removes a single user

- Results are returned for the market provided within the basic authentication credentials 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersFindAndModifyUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    UsersFindAndModifyUsersApi apiInstance = new UsersFindAndModifyUsersApi(defaultClient);
    String userId = "userId_example"; // String | The id of the user to be removed
    try {
      apiInstance.usersUserIdDelete(userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersFindAndModifyUsersApi#usersUserIdDelete");
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
| **userId** | **String**| The id of the user to be removed | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - User is not found |  -  |
| **0** | OK |  -  |

<a id="usersUserIdGet"></a>
# **usersUserIdGet**
> User usersUserIdGet(userId)

Return a single user

- Results are returned for the market provided within the basic authentication credentials 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersFindAndModifyUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    UsersFindAndModifyUsersApi apiInstance = new UsersFindAndModifyUsersApi(defaultClient);
    String userId = "userId_example"; // String | The id of the user to be located
    try {
      User result = apiInstance.usersUserIdGet(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersFindAndModifyUsersApi#usersUserIdGet");
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
| **userId** | **String**| The id of the user to be located | |

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - User is not found |  -  |
| **0** | OK |  -  |

<a id="usersUserIdPatch"></a>
# **usersUserIdPatch**
> User usersUserIdPatch(userId, type, email, username, name, customData)

Updates user fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersFindAndModifyUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    UsersFindAndModifyUsersApi apiInstance = new UsersFindAndModifyUsersApi(defaultClient);
    String userId = "userId_example"; // String | The id of the user to be updated
    String type = "type_example"; // String | The type for this user
    String email = "email_example"; // String | The user's email
    String username = "username_example"; // String | The user's username
    String name = "name_example"; // String | The user's name
    String customData = "customData_example"; // String | A custom JSON object that you can create and attach to this record
    try {
      User result = apiInstance.usersUserIdPatch(userId, type, email, username, name, customData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersFindAndModifyUsersApi#usersUserIdPatch");
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
| **userId** | **String**| The id of the user to be updated | |
| **type** | **String**| The type for this user | [optional] |
| **email** | **String**| The user&#39;s email | [optional] |
| **username** | **String**| The user&#39;s username | [optional] |
| **name** | **String**| The user&#39;s name | [optional] |
| **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] |

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - User is not found |  -  |
| **0** | OK |  -  |

<a id="usersUserIdPost"></a>
# **usersUserIdPost**
> User usersUserIdPost(userId, type, email, username, name, customData)

Updates a single user or adds the user if they don&#39;t exist

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersFindAndModifyUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    UsersFindAndModifyUsersApi apiInstance = new UsersFindAndModifyUsersApi(defaultClient);
    String userId = "userId_example"; // String | The id of the user to be updated
    String type = "type_example"; // String | The type for this user
    String email = "email_example"; // String | The user's email
    String username = "username_example"; // String | The user's username
    String name = "name_example"; // String | The user's name
    String customData = "customData_example"; // String | A custom JSON object that you can create and attach to this record
    try {
      User result = apiInstance.usersUserIdPost(userId, type, email, username, name, customData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersFindAndModifyUsersApi#usersUserIdPost");
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
| **userId** | **String**| The id of the user to be updated | |
| **type** | **String**| The type for this user | [optional] |
| **email** | **String**| The user&#39;s email | [optional] |
| **username** | **String**| The user&#39;s username | [optional] |
| **name** | **String**| The user&#39;s name | [optional] |
| **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] |

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **0** | OK |  -  |

