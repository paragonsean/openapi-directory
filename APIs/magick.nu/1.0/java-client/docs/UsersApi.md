# UsersApi

All URIs are relative to *http://devui.magick.nu/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getUsersEmailEmail**](UsersApi.md#getUsersEmailEmail) | **GET** /users/email/{email} | Check if email is available |
| [**getUsersUsernameUsername**](UsersApi.md#getUsersUsernameUsername) | **GET** /users/username/{username} | Check if username is available |
| [**postUsers**](UsersApi.md#postUsers) | **POST** /users | Create a new Tradeworks User |
| [**putUsersPasswordUsername**](UsersApi.md#putUsersPasswordUsername) | **PUT** /users/password/{username} | Update user&#39;s password |


<a id="getUsersEmailEmail"></a>
# **getUsersEmailEmail**
> getUsersEmailEmail(email)

Check if email is available

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
    defaultClient.setBasePath("http://devui.magick.nu/rest");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String email = "email_example"; // String | 
    try {
      apiInstance.getUsersEmailEmail(email);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUsersEmailEmail");
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
| **email** | **String**|  | |

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
| **200** | No response was specified |  -  |

<a id="getUsersUsernameUsername"></a>
# **getUsersUsernameUsername**
> getUsersUsernameUsername(username)

Check if username is available

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
    defaultClient.setBasePath("http://devui.magick.nu/rest");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String username = "username_example"; // String | 
    try {
      apiInstance.getUsersUsernameUsername(username);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUsersUsernameUsername");
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
| **username** | **String**|  | |

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
| **200** | No response was specified |  -  |

<a id="postUsers"></a>
# **postUsers**
> postUsers(body)

Create a new Tradeworks User

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
    defaultClient.setBasePath("http://devui.magick.nu/rest");

    UsersApi apiInstance = new UsersApi(defaultClient);
    UserDTO body = new UserDTO(); // UserDTO | 
    try {
      apiInstance.postUsers(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#postUsers");
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
| **body** | [**UserDTO**](UserDTO.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="putUsersPasswordUsername"></a>
# **putUsersPasswordUsername**
> putUsersPasswordUsername(username, body)

Update user&#39;s password

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
    defaultClient.setBasePath("http://devui.magick.nu/rest");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String username = "username_example"; // String | 
    PasswordDTO body = new PasswordDTO(); // PasswordDTO | 
    try {
      apiInstance.putUsersPasswordUsername(username, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#putUsersPasswordUsername");
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
| **username** | **String**|  | |
| **body** | [**PasswordDTO**](PasswordDTO.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

