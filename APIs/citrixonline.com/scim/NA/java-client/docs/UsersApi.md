# UsersApi

All URIs are relative to *https://api.citrixonline.com/identity/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createUsers**](UsersApi.md#createUsers) | **POST** /Users | Create User |
| [**deleteUser**](UsersApi.md#deleteUser) | **DELETE** /Users/{userKey} | Delete User |
| [**getMe**](UsersApi.md#getMe) | **GET** /Users/me | Get Current User |
| [**getUser**](UsersApi.md#getUser) | **GET** /Users/{userKey} | Get User |
| [**getUsers**](UsersApi.md#getUsers) | **GET** /Users | Get Users |
| [**replaceMe**](UsersApi.md#replaceMe) | **PUT** /Users/me | Replace Current User |
| [**replaceUser**](UsersApi.md#replaceUser) | **PUT** /Users/{userKey} | Replace User |
| [**updateMe**](UsersApi.md#updateMe) | **PATCH** /Users/me | Update Current User |
| [**updateUser**](UsersApi.md#updateUser) | **PATCH** /Users/{userKey} | Update User |


<a id="createUsers"></a>
# **createUsers**
> User createUsers(authorization, body)

Create User

Creates a new organization user and adds them to the user domain. The user email domain must match an existing organization email domain.

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
    defaultClient.setBasePath("https://api.citrixonline.com/identity/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
    UserDefinition body = new UserDefinition(); // UserDefinition | The details of the user to create
    try {
      User result = apiInstance.createUsers(authorization, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#createUsers");
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
| **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | |
| **body** | [**UserDefinition**](UserDefinition.md)| The details of the user to create | |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The user has been created. |  -  |
| **400** | One of the following requirements is not met:&lt;br /&gt;The userName field is required.&lt;br /&gt;The userName field must be non-empty.&lt;br /&gt;The userName field cannot exceed 128 characters.&lt;br /&gt;The locale field must be composed of 1 or 2 parts.&lt;br /&gt;The locale language sub-field must be ISO-639.&lt;br /&gt;The locale country sub-field must be ISO-3166.&lt;br /&gt;The timezone field must be a valid timezone.&lt;br /&gt;The givenName field must not exceed 60 characters.&lt;br /&gt;The familyName field must not exceed 60 characters. |  -  |
| **401** | Client is not sufficiently authorized. |  -  |
| **403** | Invalid token passed |  -  |
| **409** | Username is already in use. |  -  |
| **502** | Authentication, account, or email verification gateway error occurred. |  -  |
| **504** | Authentication, account, or email verification gateway timeout occurred. |  -  |

<a id="deleteUser"></a>
# **deleteUser**
> deleteUser(authorization, userKey)

Delete User

Deletes a user from the organization (but not from the account).

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
    defaultClient.setBasePath("https://api.citrixonline.com/identity/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
    Long userKey = 56L; // Long | The key of the user to query. The user must be in the organization domain
    try {
      apiInstance.deleteUser(authorization, userKey);
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
| **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | |
| **userKey** | **Long**| The key of the user to query. The user must be in the organization domain | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request has succeeded. |  -  |
| **401** | Client is not sufficiently authorized |  -  |
| **403** | Invalid token passed |  -  |
| **404** | User not found |  -  |
| **502** | Authentication or account gateway error occurred |  -  |
| **504** | Authentication or account gateway timeout occurred |  -  |

<a id="getMe"></a>
# **getMe**
> User getMe(authorization)

Get Current User

Queries the identity of the current authenticated user.

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
    defaultClient.setBasePath("https://api.citrixonline.com/identity/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
    try {
      User result = apiInstance.getMe(authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getMe");
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
| **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request has succeeded. |  -  |
| **401** | Client is not sufficiently authorized |  -  |
| **403** | Invalid token passed |  -  |
| **404** | User not found |  -  |
| **502** | Authentication or account gateway error occurred |  -  |
| **504** | Authentication or account gateway timeout occurred |  -  |

<a id="getUser"></a>
# **getUser**
> User getUser(authorization, userKey)

Get User

Queries user identity in the organization domain.

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
    defaultClient.setBasePath("https://api.citrixonline.com/identity/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
    Long userKey = 56L; // Long | The key of the user to query. The user must be in the organization domain
    try {
      User result = apiInstance.getUser(authorization, userKey);
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
| **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | |
| **userKey** | **Long**| The key of the user to query. The user must be in the organization domain | |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request has succeeded. |  -  |
| **401** | Client is not sufficiently authorized |  -  |
| **403** | Invalid token passed |  -  |
| **404** | User not found |  -  |
| **502** | Authentication or account gateway error occurred |  -  |
| **504** | Authentication or account gateway timeout occurred |  -  |

<a id="getUsers"></a>
# **getUsers**
> UserCollection getUsers(authorization, filter)

Get Users

Queries multiple user identities in the organization domain. Filtering is available.

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
    defaultClient.setBasePath("https://api.citrixonline.com/identity/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
    String filter = "filter_example"; // String |  Without a filter, all users in a user domain are returned. The filter parameter must be a properly formed SCIM filter using either the operator eq (equals) or the operator sw (starts with). The filter works for userName, displayName, name.givenName, and name.familyName attributes. For example, /Users?filter=name.familyName%20eq%20%%22Smith%22
    try {
      UserCollection result = apiInstance.getUsers(authorization, filter);
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
| **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | |
| **filter** | **String**|  Without a filter, all users in a user domain are returned. The filter parameter must be a properly formed SCIM filter using either the operator eq (equals) or the operator sw (starts with). The filter works for userName, displayName, name.givenName, and name.familyName attributes. For example, /Users?filter&#x3D;name.familyName%20eq%20%%22Smith%22 | [optional] |

### Return type

[**UserCollection**](UserCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request has succeeded. |  -  |
| **400** | Invalid filter syntax |  -  |
| **401** | Client is not sufficiently authorized |  -  |
| **403** | Invalid token passed |  -  |
| **502** | Authentication or account gateway error occurred |  -  |
| **504** | Authentication or account gateway timeout occurred |  -  |

<a id="replaceMe"></a>
# **replaceMe**
> User replaceMe(authorization, body)

Replace Current User

Changes the current authenticated user&#39;s displayName, locale, timezone, username and password. The request must include the full user definition (to modify one or more values without sending the full definition, see Update User). The replaced user email domain must be an existing organization email domain. 

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
    defaultClient.setBasePath("https://api.citrixonline.com/identity/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
    UserDefinition body = new UserDefinition(); // UserDefinition | The new user data
    try {
      User result = apiInstance.replaceMe(authorization, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#replaceMe");
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
| **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | |
| **body** | [**UserDefinition**](UserDefinition.md)| The new user data | |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The current user has been replaced. |  -  |
| **400** | One of the following requirements is not met:&lt;br /&gt;The userName field is required.&lt;br /&gt;The userName field must be non-empty.&lt;br /&gt;The userName field cannot exceed 128 characters.&lt;br /&gt;The locale field must be composed of 1 or 2 parts.&lt;br /&gt;The locale language sub-field must be ISO-639.&lt;br /&gt;The locale country sub-field must be ISO-3166.&lt;br /&gt;The timezone field must be a valid timezone.&lt;br /&gt;The givenName field must not exceed 60 characters.&lt;br /&gt;The familyName field must not exceed 60 characters. |  -  |
| **401** | Client is not sufficiently authorized |  -  |
| **403** | Invalid token passed |  -  |
| **404** | User not found |  -  |
| **409** | Email address conflict |  -  |
| **502** | Authentication or account gateway error occurred |  -  |
| **504** | Authentication or account gateway timeout occurred |  -  |

<a id="replaceUser"></a>
# **replaceUser**
> User replaceUser(authorization, userKey, body)

Replace User

Changes an existing user&#39;s displayName, locale, timezone, username and password. The request must include the full user definition (to modify one or more values without sending the full definition, see Update User). The replaced user email domain must be an existing organization email domain.

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
    defaultClient.setBasePath("https://api.citrixonline.com/identity/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
    Long userKey = 56L; // Long | The key of the user to query. The user must be in the organization domain
    UserDefinition body = new UserDefinition(); // UserDefinition | The new user data
    try {
      User result = apiInstance.replaceUser(authorization, userKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#replaceUser");
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
| **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | |
| **userKey** | **Long**| The key of the user to query. The user must be in the organization domain | |
| **body** | [**UserDefinition**](UserDefinition.md)| The new user data | |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The user has been replaced. |  -  |
| **400** | One of the following requirements is not met:&lt;br /&gt;The userName field is required.&lt;br /&gt;The userName field must be non-empty.&lt;br /&gt;The userName field cannot exceed 128 characters.&lt;br /&gt;The locale field must be composed of 1 or 2 parts.&lt;br /&gt;The locale language sub-field must be ISO-639.&lt;br /&gt;The locale country sub-field must be ISO-3166.&lt;br /&gt;The timezone field must be a valid timezone.&lt;br /&gt;The givenName field must not exceed 60 characters.&lt;br /&gt;The familyName field must not exceed 60 characters. |  -  |
| **401** | Client is not sufficiently authorized |  -  |
| **403** | Invalid token passed |  -  |
| **404** | User not found |  -  |
| **409** | Email address conflict |  -  |
| **502** | Authentication or account gateway error occurred |  -  |
| **504** | Authentication or account gateway timeout occurred |  -  |

<a id="updateMe"></a>
# **updateMe**
> User updateMe(authorization, body)

Update Current User

Changes a limited set (or all if you choose) of the current authenticated user&#39;s data. The updated user email domain must be an existing organization email domain. 

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
    defaultClient.setBasePath("https://api.citrixonline.com/identity/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
    UserDefinition body = new UserDefinition(); // UserDefinition | The new user data
    try {
      User result = apiInstance.updateMe(authorization, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#updateMe");
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
| **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | |
| **body** | [**UserDefinition**](UserDefinition.md)| The new user data | |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The current user has been updated. |  -  |
| **400** | One of the following requirements is not met:&lt;br /&gt;The userName field is required.&lt;br /&gt;The userName field must be non-empty.&lt;br /&gt;The userName field cannot exceed 128 characters.&lt;br /&gt;The locale field must be composed of 1 or 2 parts.&lt;br /&gt;The locale language sub-field must be ISO-639.&lt;br /&gt;The locale country sub-field must be ISO-3166.&lt;br /&gt;The timezone field must be a valid timezone.&lt;br /&gt;The givenName field must not exceed 60 characters.&lt;br /&gt;The familyName field must not exceed 60 characters. |  -  |
| **401** | Client is not sufficiently authorized |  -  |
| **403** | Invalid token passed |  -  |
| **404** | User not found |  -  |
| **409** | Email address conflict |  -  |
| **502** | Authentication or account gateway error occurred |  -  |
| **504** | Authentication or account gateway timeout occurred |  -  |

<a id="updateUser"></a>
# **updateUser**
> User updateUser(authorization, userKey, body)

Update User

Changes a limited set (or all if you choose) of the user&#39;s data. The updated user email domain must be an existing organization email domain.

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
    defaultClient.setBasePath("https://api.citrixonline.com/identity/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
    Long userKey = 56L; // Long | The key of the user to query. The user must be in the organization domain
    UserDefinition body = new UserDefinition(); // UserDefinition | The new user data
    try {
      User result = apiInstance.updateUser(authorization, userKey, body);
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
| **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | |
| **userKey** | **Long**| The key of the user to query. The user must be in the organization domain | |
| **body** | [**UserDefinition**](UserDefinition.md)| The new user data | |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The user has been updated. |  -  |
| **400** | One of the following requirements is not met:&lt;br /&gt;The userName field is required.&lt;br /&gt;The userName field must be non-empty.&lt;br /&gt;The userName field cannot exceed 128 characters.&lt;br /&gt;The locale field must be composed of 1 or 2 parts.&lt;br /&gt;The locale language sub-field must be ISO-639.&lt;br /&gt;The locale country sub-field must be ISO-3166.&lt;br /&gt;The timezone field must be a valid timezone.&lt;br /&gt;The givenName field must not exceed 60 characters.&lt;br /&gt;The familyName field must not exceed 60 characters. |  -  |
| **401** | Client is not sufficiently authorized |  -  |
| **403** | Invalid token passed |  -  |
| **404** | User not found |  -  |
| **409** | Email address conflict |  -  |
| **502** | Authentication or account gateway error occurred |  -  |
| **504** | Authentication or account gateway timeout occurred |  -  |

