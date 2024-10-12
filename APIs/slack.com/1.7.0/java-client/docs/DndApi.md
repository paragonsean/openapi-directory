# DndApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dndEndDnd**](DndApi.md#dndEndDnd) | **POST** /dnd.endDnd |  |
| [**dndEndSnooze**](DndApi.md#dndEndSnooze) | **POST** /dnd.endSnooze |  |
| [**dndInfo**](DndApi.md#dndInfo) | **GET** /dnd.info |  |
| [**dndSetSnooze**](DndApi.md#dndSetSnooze) | **POST** /dnd.setSnooze |  |
| [**dndTeamInfo**](DndApi.md#dndTeamInfo) | **GET** /dnd.teamInfo |  |


<a id="dndEndDnd"></a>
# **dndEndDnd**
> DndEndDndSchema dndEndDnd(token)



Ends the current user&#39;s Do Not Disturb session immediately.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DndApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    DndApi apiInstance = new DndApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `dnd:write`
    try {
      DndEndDndSchema result = apiInstance.dndEndDnd(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DndApi#dndEndDnd");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;dnd:write&#x60; | |

### Return type

[**DndEndDndSchema**](DndEndDndSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="dndEndSnooze"></a>
# **dndEndSnooze**
> DndEndSnoozeSchema dndEndSnooze(token)



Ends the current user&#39;s snooze mode immediately.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DndApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    DndApi apiInstance = new DndApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `dnd:write`
    try {
      DndEndSnoozeSchema result = apiInstance.dndEndSnooze(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DndApi#dndEndSnooze");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;dnd:write&#x60; | |

### Return type

[**DndEndSnoozeSchema**](DndEndSnoozeSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="dndInfo"></a>
# **dndInfo**
> DndInfoSchema dndInfo(token, user)



Retrieves a user&#39;s current Do Not Disturb status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DndApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    DndApi apiInstance = new DndApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `dnd:read`
    String user = "user_example"; // String | User to fetch status for (defaults to current user)
    try {
      DndInfoSchema result = apiInstance.dndInfo(token, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DndApi#dndInfo");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;dnd:read&#x60; | [optional] |
| **user** | **String**| User to fetch status for (defaults to current user) | [optional] |

### Return type

[**DndInfoSchema**](DndInfoSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="dndSetSnooze"></a>
# **dndSetSnooze**
> DndSetSnoozeSchema dndSetSnooze(numMinutes, token)



Turns on Do Not Disturb mode for the current user, or changes its duration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DndApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    DndApi apiInstance = new DndApi(defaultClient);
    String numMinutes = "numMinutes_example"; // String | Number of minutes, from now, to snooze until.
    String token = "token_example"; // String | Authentication token. Requires scope: `dnd:write`
    try {
      DndSetSnoozeSchema result = apiInstance.dndSetSnooze(numMinutes, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DndApi#dndSetSnooze");
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
| **numMinutes** | **String**| Number of minutes, from now, to snooze until. | |
| **token** | **String**| Authentication token. Requires scope: &#x60;dnd:write&#x60; | |

### Return type

[**DndSetSnoozeSchema**](DndSetSnoozeSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="dndTeamInfo"></a>
# **dndTeamInfo**
> DefaultSuccessTemplate dndTeamInfo(token, users)



Retrieves the Do Not Disturb status for up to 50 users on a team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DndApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    DndApi apiInstance = new DndApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `dnd:read`
    String users = "users_example"; // String | Comma-separated list of users to fetch Do Not Disturb status for
    try {
      DefaultSuccessTemplate result = apiInstance.dndTeamInfo(token, users);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DndApi#dndTeamInfo");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;dnd:read&#x60; | [optional] |
| **users** | **String**| Comma-separated list of users to fetch Do Not Disturb status for | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

