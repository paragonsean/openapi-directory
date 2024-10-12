# RemindersApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**remindersAdd**](RemindersApi.md#remindersAdd) | **POST** /reminders.add |  |
| [**remindersComplete**](RemindersApi.md#remindersComplete) | **POST** /reminders.complete |  |
| [**remindersDelete**](RemindersApi.md#remindersDelete) | **POST** /reminders.delete |  |
| [**remindersInfo**](RemindersApi.md#remindersInfo) | **GET** /reminders.info |  |
| [**remindersList**](RemindersApi.md#remindersList) | **GET** /reminders.list |  |


<a id="remindersAdd"></a>
# **remindersAdd**
> RemindersAddSchema remindersAdd(token, text, time, user)



Creates a reminder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RemindersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    RemindersApi apiInstance = new RemindersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `reminders:write`
    String text = "text_example"; // String | The content of the reminder
    String time = "time_example"; // String | When this reminder should happen: the Unix timestamp (up to five years from now), the number of seconds until the reminder (if within 24 hours), or a natural language description (Ex. \\\"in 15 minutes,\\\" or \\\"every Thursday\\\")
    String user = "user_example"; // String | The user who will receive the reminder. If no user is specified, the reminder will go to user who created it.
    try {
      RemindersAddSchema result = apiInstance.remindersAdd(token, text, time, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RemindersApi#remindersAdd");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;reminders:write&#x60; | |
| **text** | **String**| The content of the reminder | |
| **time** | **String**| When this reminder should happen: the Unix timestamp (up to five years from now), the number of seconds until the reminder (if within 24 hours), or a natural language description (Ex. \\\&quot;in 15 minutes,\\\&quot; or \\\&quot;every Thursday\\\&quot;) | |
| **user** | **String**| The user who will receive the reminder. If no user is specified, the reminder will go to user who created it. | [optional] |

### Return type

[**RemindersAddSchema**](RemindersAddSchema.md)

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

<a id="remindersComplete"></a>
# **remindersComplete**
> RemindersCompleteSchema remindersComplete(token, reminder)



Marks a reminder as complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RemindersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    RemindersApi apiInstance = new RemindersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `reminders:write`
    String reminder = "reminder_example"; // String | The ID of the reminder to be marked as complete
    try {
      RemindersCompleteSchema result = apiInstance.remindersComplete(token, reminder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RemindersApi#remindersComplete");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;reminders:write&#x60; | [optional] |
| **reminder** | **String**| The ID of the reminder to be marked as complete | [optional] |

### Return type

[**RemindersCompleteSchema**](RemindersCompleteSchema.md)

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

<a id="remindersDelete"></a>
# **remindersDelete**
> RemindersDeleteSchema remindersDelete(token, reminder)



Deletes a reminder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RemindersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    RemindersApi apiInstance = new RemindersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `reminders:write`
    String reminder = "reminder_example"; // String | The ID of the reminder
    try {
      RemindersDeleteSchema result = apiInstance.remindersDelete(token, reminder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RemindersApi#remindersDelete");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;reminders:write&#x60; | [optional] |
| **reminder** | **String**| The ID of the reminder | [optional] |

### Return type

[**RemindersDeleteSchema**](RemindersDeleteSchema.md)

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

<a id="remindersInfo"></a>
# **remindersInfo**
> RemindersInfoSchema remindersInfo(token, reminder)



Gets information about a reminder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RemindersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    RemindersApi apiInstance = new RemindersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `reminders:read`
    String reminder = "reminder_example"; // String | The ID of the reminder
    try {
      RemindersInfoSchema result = apiInstance.remindersInfo(token, reminder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RemindersApi#remindersInfo");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;reminders:read&#x60; | [optional] |
| **reminder** | **String**| The ID of the reminder | [optional] |

### Return type

[**RemindersInfoSchema**](RemindersInfoSchema.md)

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

<a id="remindersList"></a>
# **remindersList**
> RemindersListSchema remindersList(token)



Lists all reminders created by or for a given user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RemindersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    RemindersApi apiInstance = new RemindersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `reminders:read`
    try {
      RemindersListSchema result = apiInstance.remindersList(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RemindersApi#remindersList");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;reminders:read&#x60; | [optional] |

### Return type

[**RemindersListSchema**](RemindersListSchema.md)

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

