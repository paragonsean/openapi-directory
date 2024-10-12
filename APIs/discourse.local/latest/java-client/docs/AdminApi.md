# AdminApi

All URIs are relative to *http://discourse.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminGetUser_0**](AdminApi.md#adminGetUser_0) | **GET** /admin/users/{id}.json | Get a user by id |
| [**adminListUsers_0**](AdminApi.md#adminListUsers_0) | **GET** /admin/users/list/{flag}.json | Get a list of users |
| [**anonymizeUser_0**](AdminApi.md#anonymizeUser_0) | **PUT** /admin/users/{id}/anonymize.json | Anonymize a user |
| [**deleteUser_0**](AdminApi.md#deleteUser_0) | **DELETE** /admin/users/{id}.json | Delete a user |
| [**logOutUser_0**](AdminApi.md#logOutUser_0) | **POST** /admin/users/{id}/log_out.json | Log a user out |
| [**refreshGravatar_0**](AdminApi.md#refreshGravatar_0) | **POST** /user_avatar/{username}/refresh_gravatar.json | Refresh gravatar |
| [**silenceUser_0**](AdminApi.md#silenceUser_0) | **PUT** /admin/users/{id}/silence.json | Silence a user |
| [**suspendUser_0**](AdminApi.md#suspendUser_0) | **PUT** /admin/users/{id}/suspend.json | Suspend a user |


<a id="adminGetUser_0"></a>
# **adminGetUser_0**
> AdminGetUser200Response adminGetUser_0(id)

Get a user by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    AdminApi apiInstance = new AdminApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      AdminGetUser200Response result = apiInstance.adminGetUser_0(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminApi#adminGetUser_0");
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
| **id** | **Integer**|  | |

### Return type

[**AdminGetUser200Response**](AdminGetUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="adminListUsers_0"></a>
# **adminListUsers_0**
> Set&lt;AdminListUsers200ResponseInner&gt; adminListUsers_0(flag, order, asc, page, showEmails)

Get a list of users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    AdminApi apiInstance = new AdminApi(defaultClient);
    String flag = "active"; // String | 
    String order = "created"; // String | 
    String asc = "true"; // String | 
    Integer page = 56; // Integer | 
    Boolean showEmails = true; // Boolean | 
    try {
      Set<AdminListUsers200ResponseInner> result = apiInstance.adminListUsers_0(flag, order, asc, page, showEmails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminApi#adminListUsers_0");
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
| **flag** | **String**|  | [enum: active, new, staff, suspended, blocked, suspect] |
| **order** | **String**|  | [optional] [enum: created, last_emailed, seen, username, email, trust_level, days_visited, posts_read, topics_viewed, posts, read_time] |
| **asc** | **String**|  | [optional] [enum: true] |
| **page** | **Integer**|  | [optional] |
| **showEmails** | **Boolean**|  | [optional] |

### Return type

[**Set&lt;AdminListUsers200ResponseInner&gt;**](AdminListUsers200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="anonymizeUser_0"></a>
# **anonymizeUser_0**
> AnonymizeUser200Response anonymizeUser_0(id)

Anonymize a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    AdminApi apiInstance = new AdminApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      AnonymizeUser200Response result = apiInstance.anonymizeUser_0(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminApi#anonymizeUser_0");
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
| **id** | **Integer**|  | |

### Return type

[**AnonymizeUser200Response**](AnonymizeUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="deleteUser_0"></a>
# **deleteUser_0**
> DeleteUser200Response deleteUser_0(id, deleteUserRequest)

Delete a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    AdminApi apiInstance = new AdminApi(defaultClient);
    Integer id = 56; // Integer | 
    DeleteUserRequest deleteUserRequest = new DeleteUserRequest(); // DeleteUserRequest | 
    try {
      DeleteUser200Response result = apiInstance.deleteUser_0(id, deleteUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminApi#deleteUser_0");
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
| **id** | **Integer**|  | |
| **deleteUserRequest** | [**DeleteUserRequest**](DeleteUserRequest.md)|  | [optional] |

### Return type

[**DeleteUser200Response**](DeleteUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="logOutUser_0"></a>
# **logOutUser_0**
> DeleteGroup200Response logOutUser_0(id)

Log a user out

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    AdminApi apiInstance = new AdminApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      DeleteGroup200Response result = apiInstance.logOutUser_0(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminApi#logOutUser_0");
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
| **id** | **Integer**|  | |

### Return type

[**DeleteGroup200Response**](DeleteGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="refreshGravatar_0"></a>
# **refreshGravatar_0**
> RefreshGravatar200Response refreshGravatar_0(username)

Refresh gravatar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    AdminApi apiInstance = new AdminApi(defaultClient);
    String username = "username_example"; // String | 
    try {
      RefreshGravatar200Response result = apiInstance.refreshGravatar_0(username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminApi#refreshGravatar_0");
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

[**RefreshGravatar200Response**](RefreshGravatar200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="silenceUser_0"></a>
# **silenceUser_0**
> SilenceUser200Response silenceUser_0(id, silenceUserRequest)

Silence a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    AdminApi apiInstance = new AdminApi(defaultClient);
    Integer id = 56; // Integer | 
    SilenceUserRequest silenceUserRequest = new SilenceUserRequest(); // SilenceUserRequest | 
    try {
      SilenceUser200Response result = apiInstance.silenceUser_0(id, silenceUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminApi#silenceUser_0");
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
| **id** | **Integer**|  | |
| **silenceUserRequest** | [**SilenceUserRequest**](SilenceUserRequest.md)|  | [optional] |

### Return type

[**SilenceUser200Response**](SilenceUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="suspendUser_0"></a>
# **suspendUser_0**
> SuspendUser200Response suspendUser_0(id, suspendUserRequest)

Suspend a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    AdminApi apiInstance = new AdminApi(defaultClient);
    Integer id = 56; // Integer | 
    SuspendUserRequest suspendUserRequest = new SuspendUserRequest(); // SuspendUserRequest | 
    try {
      SuspendUser200Response result = apiInstance.suspendUser_0(id, suspendUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminApi#suspendUser_0");
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
| **id** | **Integer**|  | |
| **suspendUserRequest** | [**SuspendUserRequest**](SuspendUserRequest.md)|  | [optional] |

### Return type

[**SuspendUser200Response**](SuspendUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

