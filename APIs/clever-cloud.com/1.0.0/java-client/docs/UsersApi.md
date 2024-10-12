# UsersApi

All URIs are relative to *https://api.clever-cloud.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getUsersIdApplications_1**](UsersApi.md#getUsersIdApplications_1) | **GET** /users/{id}/applications |  |
| [**getUsersId_0**](UsersApi.md#getUsersId_0) | **GET** /users/{id} |  |
| [**getUsersUserIdGitInfo_0**](UsersApi.md#getUsersUserIdGitInfo_0) | **GET** /users/{userId}/git-info |  |
| [**postUsers_0**](UsersApi.md#postUsers_0) | **POST** /users |  |


<a id="getUsersIdApplications_1"></a>
# **getUsersIdApplications_1**
> List&lt;Application&gt; getUsersIdApplications_1(id)



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
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      List<Application> result = apiInstance.getUsersIdApplications_1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUsersIdApplications_1");
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
| **id** | **String**|  | |

### Return type

[**List&lt;Application&gt;**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getApplications |  -  |

<a id="getUsersId_0"></a>
# **getUsersId_0**
> User getUsersId_0(id)



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
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      User result = apiInstance.getUsersId_0(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUsersId_0");
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
| **id** | **String**|  | |

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
| **200** | getUser |  -  |

<a id="getUsersUserIdGitInfo_0"></a>
# **getUsersUserIdGitInfo_0**
> getUsersUserIdGitInfo_0(userId)



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
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | 
    try {
      apiInstance.getUsersUserIdGitInfo_0(userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUsersUserIdGitInfo_0");
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
| **userId** | **String**|  | |

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
| **200** | getGitInfo |  -  |

<a id="postUsers_0"></a>
# **postUsers_0**
> postUsers_0(wannabeUser, invitationKey, addonBetaInvitationKey, email, pass, urlNext, terms)



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
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    UsersApi apiInstance = new UsersApi(defaultClient);
    WannabeUser wannabeUser = new WannabeUser(); // WannabeUser | 
    String invitationKey = "invitationKey_example"; // String | 
    String addonBetaInvitationKey = "addonBetaInvitationKey_example"; // String | 
    String email = "email_example"; // String | 
    String pass = "pass_example"; // String | 
    String urlNext = "urlNext_example"; // String | 
    String terms = "terms_example"; // String | 
    try {
      apiInstance.postUsers_0(wannabeUser, invitationKey, addonBetaInvitationKey, email, pass, urlNext, terms);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#postUsers_0");
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
| **wannabeUser** | [**WannabeUser**](WannabeUser.md)|  | |
| **invitationKey** | **String**|  | [optional] |
| **addonBetaInvitationKey** | **String**|  | [optional] |
| **email** | **String**|  | [optional] |
| **pass** | **String**|  | [optional] |
| **urlNext** | **String**|  | [optional] |
| **terms** | **String**|  | [optional] |

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
| **200** | createUser createUserFromForm |  -  |

