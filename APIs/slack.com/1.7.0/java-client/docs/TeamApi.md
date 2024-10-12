# TeamApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**teamAccessLogs**](TeamApi.md#teamAccessLogs) | **GET** /team.accessLogs |  |
| [**teamBillableInfo**](TeamApi.md#teamBillableInfo) | **GET** /team.billableInfo |  |
| [**teamInfo**](TeamApi.md#teamInfo) | **GET** /team.info |  |
| [**teamIntegrationLogs**](TeamApi.md#teamIntegrationLogs) | **GET** /team.integrationLogs |  |
| [**teamProfileGet_0**](TeamApi.md#teamProfileGet_0) | **GET** /team.profile.get |  |


<a id="teamAccessLogs"></a>
# **teamAccessLogs**
> TeamAccessLogsSchema teamAccessLogs(token, before, count, page)



Gets the access logs for the current team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    TeamApi apiInstance = new TeamApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin`
    String before = "before_example"; // String | End of time range of logs to include in results (inclusive).
    String count = "count_example"; // String | 
    String page = "page_example"; // String | 
    try {
      TeamAccessLogsSchema result = apiInstance.teamAccessLogs(token, before, count, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamApi#teamAccessLogs");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin&#x60; | |
| **before** | **String**| End of time range of logs to include in results (inclusive). | [optional] |
| **count** | **String**|  | [optional] |
| **page** | **String**|  | [optional] |

### Return type

[**TeamAccessLogsSchema**](TeamAccessLogsSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This response demonstrates pagination and two access log entries. |  -  |
| **0** | A workspace must be on a paid plan to use this method, otherwise the &#x60;paid_only&#x60; error is thrown: |  -  |

<a id="teamBillableInfo"></a>
# **teamBillableInfo**
> DefaultSuccessTemplate teamBillableInfo(token, user)



Gets billable users information for the current team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    TeamApi apiInstance = new TeamApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin`
    String user = "user_example"; // String | A user to retrieve the billable information for. Defaults to all users.
    try {
      DefaultSuccessTemplate result = apiInstance.teamBillableInfo(token, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamApi#teamBillableInfo");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin&#x60; | |
| **user** | **String**| A user to retrieve the billable information for. Defaults to all users. | [optional] |

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

<a id="teamInfo"></a>
# **teamInfo**
> TeamInfoSchema teamInfo(token, team)



Gets information about the current team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    TeamApi apiInstance = new TeamApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `team:read`
    String team = "team_example"; // String | Team to get info on, if omitted, will return information about the current team. Will only return team that the authenticated token is allowed to see through external shared channels
    try {
      TeamInfoSchema result = apiInstance.teamInfo(token, team);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamApi#teamInfo");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;team:read&#x60; | |
| **team** | **String**| Team to get info on, if omitted, will return information about the current team. Will only return team that the authenticated token is allowed to see through external shared channels | [optional] |

### Return type

[**TeamInfoSchema**](TeamInfoSchema.md)

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

<a id="teamIntegrationLogs"></a>
# **teamIntegrationLogs**
> TeamIntegrationLogsSchema teamIntegrationLogs(token, appId, changeType, count, page, serviceId, user)



Gets the integration logs for the current team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    TeamApi apiInstance = new TeamApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin`
    String appId = "appId_example"; // String | Filter logs to this Slack app. Defaults to all logs.
    String changeType = "changeType_example"; // String | Filter logs with this change type. Defaults to all logs.
    String count = "count_example"; // String | 
    String page = "page_example"; // String | 
    String serviceId = "serviceId_example"; // String | Filter logs to this service. Defaults to all logs.
    String user = "user_example"; // String | Filter logs generated by this user’s actions. Defaults to all logs.
    try {
      TeamIntegrationLogsSchema result = apiInstance.teamIntegrationLogs(token, appId, changeType, count, page, serviceId, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamApi#teamIntegrationLogs");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin&#x60; | |
| **appId** | **String**| Filter logs to this Slack app. Defaults to all logs. | [optional] |
| **changeType** | **String**| Filter logs with this change type. Defaults to all logs. | [optional] |
| **count** | **String**|  | [optional] |
| **page** | **String**|  | [optional] |
| **serviceId** | **String**| Filter logs to this service. Defaults to all logs. | [optional] |
| **user** | **String**| Filter logs generated by this user’s actions. Defaults to all logs. | [optional] |

### Return type

[**TeamIntegrationLogsSchema**](TeamIntegrationLogsSchema.md)

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

<a id="teamProfileGet_0"></a>
# **teamProfileGet_0**
> TeamProfileGetSuccessSchema teamProfileGet_0(token, visibility)



Retrieve a team&#39;s profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    TeamApi apiInstance = new TeamApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `users.profile:read`
    String visibility = "visibility_example"; // String | Filter by visibility.
    try {
      TeamProfileGetSuccessSchema result = apiInstance.teamProfileGet_0(token, visibility);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamApi#teamProfileGet_0");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;users.profile:read&#x60; | |
| **visibility** | **String**| Filter by visibility. | [optional] |

### Return type

[**TeamProfileGetSuccessSchema**](TeamProfileGetSuccessSchema.md)

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

