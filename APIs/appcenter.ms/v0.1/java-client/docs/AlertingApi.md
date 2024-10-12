# AlertingApi

All URIs are relative to *https://api.appcenter.ms*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bugTrackerGetRepoIssueFromCrash**](AlertingApi.md#bugTrackerGetRepoIssueFromCrash) | **GET** /v0.1/apps/{owner_name}/{app_name}/bugtracker/crashGroup/{crash_group_id} |  |
| [**bugtrackerGetSettings**](AlertingApi.md#bugtrackerGetSettings) | **GET** /v0.1/apps/{owner_name}/{app_name}/bugtracker |  |
| [**notificationsGetAppEmailSettings**](AlertingApi.md#notificationsGetAppEmailSettings) | **GET** /v0.1/apps/{owner_name}/{app_name}/notifications/emailSettings |  |
| [**notificationsGetUserEmailSettings**](AlertingApi.md#notificationsGetUserEmailSettings) | **GET** /v0.1/user/notifications/emailSettings |  |
| [**webhooksList**](AlertingApi.md#webhooksList) | **GET** /v0.1/apps/{owner_name}/{app_name}/webhooks |  |


<a id="bugTrackerGetRepoIssueFromCrash"></a>
# **bugTrackerGetRepoIssueFromCrash**
> BugTrackerGetRepoIssueFromCrash200Response bugTrackerGetRepoIssueFromCrash(crashGroupId, ownerName, appName)



Get project issue related to a crash group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AlertingApi apiInstance = new AlertingApi(defaultClient);
    String crashGroupId = "crashGroupId_example"; // String | CrashGroup Id
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      BugTrackerGetRepoIssueFromCrash200Response result = apiInstance.bugTrackerGetRepoIssueFromCrash(crashGroupId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertingApi#bugTrackerGetRepoIssueFromCrash");
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
| **crashGroupId** | **String**| CrashGroup Id | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**BugTrackerGetRepoIssueFromCrash200Response**](BugTrackerGetRepoIssueFromCrash200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error code with reason |  -  |

<a id="bugtrackerGetSettings"></a>
# **bugtrackerGetSettings**
> BugtrackerGetSettings200Response bugtrackerGetSettings(ownerName, appName)



Get bug tracker settings for a particular app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AlertingApi apiInstance = new AlertingApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      BugtrackerGetSettings200Response result = apiInstance.bugtrackerGetSettings(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertingApi#bugtrackerGetSettings");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**BugtrackerGetSettings200Response**](BugtrackerGetSettings200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error code with reason |  -  |

<a id="notificationsGetAppEmailSettings"></a>
# **notificationsGetAppEmailSettings**
> NotificationsGetAppEmailSettings200Response notificationsGetAppEmailSettings(ownerName, appName)



Get Email notification settings of user for a particular app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AlertingApi apiInstance = new AlertingApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      NotificationsGetAppEmailSettings200Response result = apiInstance.notificationsGetAppEmailSettings(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertingApi#notificationsGetAppEmailSettings");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**NotificationsGetAppEmailSettings200Response**](NotificationsGetAppEmailSettings200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error code with reason |  -  |

<a id="notificationsGetUserEmailSettings"></a>
# **notificationsGetUserEmailSettings**
> NotificationsGetUserEmailSettings200Response notificationsGetUserEmailSettings()



Get Default email notification settings for the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AlertingApi apiInstance = new AlertingApi(defaultClient);
    try {
      NotificationsGetUserEmailSettings200Response result = apiInstance.notificationsGetUserEmailSettings();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertingApi#notificationsGetUserEmailSettings");
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

[**NotificationsGetUserEmailSettings200Response**](NotificationsGetUserEmailSettings200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error code with reason |  -  |

<a id="webhooksList"></a>
# **webhooksList**
> WebhooksList200Response webhooksList(ownerName, appName)



Get web hooks configured for a particular app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AlertingApi apiInstance = new AlertingApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      WebhooksList200Response result = apiInstance.webhooksList(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertingApi#webhooksList");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**WebhooksList200Response**](WebhooksList200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error code with reason |  -  |

