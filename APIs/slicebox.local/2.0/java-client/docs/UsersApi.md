# UsersApi

All URIs are relative to *http://slicebox.local/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersCurrentGet**](UsersApi.md#usersCurrentGet) | **GET** /users/current |  |
| [**usersGet**](UsersApi.md#usersGet) | **GET** /users |  |
| [**usersIdDelete**](UsersApi.md#usersIdDelete) | **DELETE** /users/{id} |  |
| [**usersLoginPost**](UsersApi.md#usersLoginPost) | **POST** /users/login |  |
| [**usersLogoutPost**](UsersApi.md#usersLogoutPost) | **POST** /users/logout |  |
| [**usersPost**](UsersApi.md#usersPost) | **POST** /users |  |


<a id="usersCurrentGet"></a>
# **usersCurrentGet**
> UserInfo usersCurrentGet()



obtain information on the currently logged in user as specified by the supplied session cookie, IP address and user agent.

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
    defaultClient.setBasePath("http://slicebox.local/api");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      UserInfo result = apiInstance.usersCurrentGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersCurrentGet");
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

[**UserInfo**](UserInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | user information |  -  |
| **404** | no user found for the supplied session cookie, IP address and user agent, or if any of the required headers are missing. |  -  |

<a id="usersGet"></a>
# **usersGet**
> List&lt;User&gt; usersGet(startindex, count)



Returns all users of slicebox

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
    defaultClient.setBasePath("http://slicebox.local/api");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Long startindex = 0L; // Long | start index of returned slice of users
    Long count = 20L; // Long | size of returned slice of users
    try {
      List<User> result = apiInstance.usersGet(startindex, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersGet");
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
| **startindex** | **Long**| start index of returned slice of users | [optional] [default to 0] |
| **count** | **Long**| size of returned slice of users | [optional] [default to 20] |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | user response |  -  |

<a id="usersIdDelete"></a>
# **usersIdDelete**
> usersIdDelete(id)



deletes a single user based on the ID supplied

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
    defaultClient.setBasePath("http://slicebox.local/api");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Long id = 56L; // Long | ID of user to delete
    try {
      apiInstance.usersIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersIdDelete");
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
| **id** | **Long**| ID of user to delete | |

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
| **204** | user deleted |  -  |

<a id="usersLoginPost"></a>
# **usersLoginPost**
> usersLoginPost(userPass)



Obtain a session cookie that can be used to authenticate future API calls from the present IP address and with the present user agent.

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
    defaultClient.setBasePath("http://slicebox.local/api");

    UsersApi apiInstance = new UsersApi(defaultClient);
    UserPass userPass = new UserPass(); // UserPass | username and password for user logging in
    try {
      apiInstance.usersLoginPost(userPass);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersLoginPost");
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
| **userPass** | [**UserPass**](UserPass.md)| username and password for user logging in | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | if the supplied credentials are valid. The response headers will contain Set-Cookie. |  -  |
| **401** | if the supplied credentials are invalid. |  -  |

<a id="usersLogoutPost"></a>
# **usersLogoutPost**
> usersLogoutPost()



Logout the current user by responding with a delete cookie header removing the session cookie for this user.

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
    defaultClient.setBasePath("http://slicebox.local/api");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      apiInstance.usersLogoutPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersLogoutPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | the user was logged out |  -  |

<a id="usersPost"></a>
# **usersPost**
> User usersPost(user)



Creates a new user. Dupicates are accepted but not added.

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
    defaultClient.setBasePath("http://slicebox.local/api");

    UsersApi apiInstance = new UsersApi(defaultClient);
    NewUser user = new NewUser(); // NewUser | User to add
    try {
      User result = apiInstance.usersPost(user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersPost");
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
| **user** | [**NewUser**](NewUser.md)| User to add | |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | user response |  -  |

