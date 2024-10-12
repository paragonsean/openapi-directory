# UsersApi

All URIs are relative to *https://circuitsandbox.net/rest/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLabel**](UsersApi.md#getLabel) | **GET** /users/labels | Returns all user labels |
| [**getPresence**](UsersApi.md#getPresence) | **GET** /users/presence | Gets the presence status |
| [**getProfile**](UsersApi.md#getProfile) | **GET** /users/profile | Gets the authenticated user&#39;s profile information |
| [**getSupportInfo**](UsersApi.md#getSupportInfo) | **GET** /users/supportinfo | Gets the support information |
| [**getUserByEmailAddress**](UsersApi.md#getUserByEmailAddress) | **GET** /users/{emailAddress}/getUserByEmail | Get user by email |
| [**getUserById**](UsersApi.md#getUserById) | **GET** /users/{id} | Gets the user&#39;s profile information |
| [**getUserPresence**](UsersApi.md#getUserPresence) | **GET** /users/{id}/presence | Gets the presence status |
| [**searchUser**](UsersApi.md#searchUser) | **GET** /users | Search for users |
| [**searchUsersList**](UsersApi.md#searchUsersList) | **GET** /users/list | Search multiple users. |
| [**setUserPresence**](UsersApi.md#setUserPresence) | **PUT** /users/presence | Updates the presence status |


<a id="getLabel"></a>
# **getLabel**
> List&lt;Label&gt; getLabel()

Returns all user labels

Returns all labels of the user that were defined either explicit or implicit via assignment to conversations. OauthScopes: READ_USER_PROFILE, ORGANIZE_CONVERSATIONS

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      List<Label> result = apiInstance.getLabel();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getLabel");
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

[**List&lt;Label&gt;**](Label.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of labels |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getPresence"></a>
# **getPresence**
> List&lt;Presence&gt; getPresence(userIds)

Gets the presence status

Gets the presence status of the users whose IDs or email addresses are given. OauthScopes: READ_USER

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    List<String> userIds = Arrays.asList(); // List<String> | A list of unique user IDs or email addresses of the users you want to query the presence state for
    try {
      List<Presence> result = apiInstance.getPresence(userIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getPresence");
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
| **userIds** | [**List&lt;String&gt;**](String.md)| A list of unique user IDs or email addresses of the users you want to query the presence state for | |

### Return type

[**List&lt;Presence&gt;**](Presence.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The presence states |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the userIds passed as parameter are not provided in the correct format&lt;/li&gt;&lt;li&gt; or a valid email address&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **404** | One or more of the users do not exist |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getProfile"></a>
# **getProfile**
> User getProfile()

Gets the authenticated user&#39;s profile information

Gets the authenticated user&#39;s profile information. OauthScopes: READ_USER_PROFILE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      User result = apiInstance.getProfile();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getProfile");
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

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets the authenticated user&#39;s profile information |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getSupportInfo"></a>
# **getSupportInfo**
> SupportInfo getSupportInfo()

Gets the support information

Gets the support information for the tenant of the requesting user OauthScopes: READ_USER_PROFILE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      SupportInfo result = apiInstance.getSupportInfo();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getSupportInfo");
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

[**SupportInfo**](SupportInfo.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful, the support information returned |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getUserByEmailAddress"></a>
# **getUserByEmailAddress**
> User getUserByEmailAddress(emailAddress, secondaryLookup)

Get user by email

Get user by first or secondary email address OauthScopes: READ_USER_PROFILE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String emailAddress = "emailAddress_example"; // String | The main or secondary email address of a user.
    Boolean secondaryLookup = true; // Boolean | secondaryLookup enabled (default = false)
    try {
      User result = apiInstance.getUserByEmailAddress(emailAddress, secondaryLookup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUserByEmailAddress");
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
| **emailAddress** | **String**| The main or secondary email address of a user. | |
| **secondaryLookup** | **Boolean**| secondaryLookup enabled (default &#x3D; false) | [optional] |

### Return type

[**User**](User.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User successfully retrieved |  -  |
| **401** | The authentication was not successful |  -  |
| **404** | User not found or not a session guest.  |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getUserById"></a>
# **getUserById**
> User getUserById(id)

Gets the user&#39;s profile information

Gets the profile information of the user with the given ID. OauthScopes: READ_USER

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "id_example"; // String | The unique ID or the email address of the user to fetch
    try {
      User result = apiInstance.getUserById(id);
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
| **id** | **String**| The unique ID or the email address of the user to fetch | |

### Return type

[**User**](User.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful, the user profile is returned |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the data format of the passed user does not match either a UUID (user primary key)&lt;/li&gt;&lt;li&gt; or an valid email address&lt;/li&gt;&lt;li&gt;or a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **404** | The user does not exist |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getUserPresence"></a>
# **getUserPresence**
> Presence getUserPresence(id)

Gets the presence status

Gets the presence status of the users whose ID or email address is given. OauthScopes: READ_USER

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "id_example"; // String | The unique ID or the email address of the user to fetch.
    try {
      Presence result = apiInstance.getUserPresence(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUserPresence");
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
| **id** | **String**| The unique ID or the email address of the user to fetch. | |

### Return type

[**Presence**](Presence.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The presence state |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the data format of the passed user does not match either a UUID (user primary key)&lt;/li&gt;&lt;li&gt; or a valid email address&lt;/li&gt;&lt;li&gt;or a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **404** | The user does not exist |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="searchUser"></a>
# **searchUser**
> List&lt;User&gt; searchUser(name)

Search for users

Search for users based on an email address or username OauthScopes: READ_USER

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String name = "name_example"; // String | Search for a user by name
    try {
      List<User> result = apiInstance.searchUser(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#searchUser");
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
| **name** | **String**| Search for a user by name | |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The users which match the search criteria |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **404** | The search term did not much any results |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="searchUsersList"></a>
# **searchUsersList**
> List&lt;User&gt; searchUsersList(name, returnFullUserInfo, secondaryLookup)

Search multiple users.

Search multiple users given by id or email address. OauthScopes: READ_USER

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    List<String> name = Arrays.asList(); // List<String> | Multiple email addresses or UUIDs.
    Boolean returnFullUserInfo = false; // Boolean | Boolean, return full user info?
    Boolean secondaryLookup = false; // Boolean | Boolean, lookup secondary email?
    try {
      List<User> result = apiInstance.searchUsersList(name, returnFullUserInfo, secondaryLookup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#searchUsersList");
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
| **name** | [**List&lt;String&gt;**](String.md)| Multiple email addresses or UUIDs. | |
| **returnFullUserInfo** | **Boolean**| Boolean, return full user info? | [optional] [default to false] |
| **secondaryLookup** | **Boolean**| Boolean, lookup secondary email? | [optional] [default to false] |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | At least one user was found and returned in a list |  -  |
| **400** | Bad Request |  -  |
| **401** | The authentication was not successful |  -  |
| **404** | No user was found |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="setUserPresence"></a>
# **setUserPresence**
> Presence setUserPresence(state, clearDND, dndUntil, statusMessage)

Updates the presence status

Updates the presence status of the authenticated user. OauthScopes: WRITE_USER_PROFILE, MANAGE_PRESENCE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String state = "state_example"; // String | The user's presence.
    Boolean clearDND = false; // Boolean | Clear the DND of the user.
    OffsetDateTime dndUntil = OffsetDateTime.now(); // OffsetDateTime | Timestamp until the DND state of the user is active. This field is mandatory when the state is set to DND.
    String statusMessage = "statusMessage_example"; // String | An optional status message that is displayed instead of the location
    try {
      Presence result = apiInstance.setUserPresence(state, clearDND, dndUntil, statusMessage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#setUserPresence");
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
| **state** | **String**| The user&#39;s presence. | |
| **clearDND** | **Boolean**| Clear the DND of the user. | [optional] [default to false] |
| **dndUntil** | **OffsetDateTime**| Timestamp until the DND state of the user is active. This field is mandatory when the state is set to DND. | [optional] |
| **statusMessage** | **String**| An optional status message that is displayed instead of the location | [optional] |

### Return type

[**Presence**](Presence.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The presence states |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the presence state is DND and the data format of the passed dndUntil is missing &lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

