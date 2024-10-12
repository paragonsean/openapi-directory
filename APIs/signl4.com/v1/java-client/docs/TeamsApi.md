# TeamsApi

All URIs are relative to *https://connect.signl4.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**subscriptionsSubscriptionIdTeamsGet**](TeamsApi.md#subscriptionsSubscriptionIdTeamsGet) | **GET** /subscriptions/{subscriptionId}/teams | Get infos for all teams of the subscription. |
| [**teamsGet**](TeamsApi.md#teamsGet) | **GET** /teams | Get infos of all teams. |
| [**teamsTeamIdAlertReportsFileNameGet**](TeamsApi.md#teamsTeamIdAlertReportsFileNameGet) | **GET** /teams/{teamId}/alertReports/{fileName} | Returns Alert Report |
| [**teamsTeamIdAlertReportsGet**](TeamsApi.md#teamsTeamIdAlertReportsGet) | **GET** /teams/{teamId}/alertReports | Get information about downloadable alert reports |
| [**teamsTeamIdAlertSettingsGet**](TeamsApi.md#teamsTeamIdAlertSettingsGet) | **GET** /teams/{teamId}/alertSettings | Gets alert settings of a specific team. |
| [**teamsTeamIdAlertSettingsPost**](TeamsApi.md#teamsTeamIdAlertSettingsPost) | **POST** /teams/{teamId}/alertSettings | Sets alert settings of a specific team. |
| [**teamsTeamIdEventSourcesGet**](TeamsApi.md#teamsTeamIdEventSourcesGet) | **GET** /teams/{teamId}/eventSources | Gets event sources of a specific team. |
| [**teamsTeamIdGet**](TeamsApi.md#teamsTeamIdGet) | **GET** /teams/{teamId} | Gets infos of a specific team. |
| [**teamsTeamIdProfilePut**](TeamsApi.md#teamsTeamIdProfilePut) | **PUT** /teams/{teamId}/profile | Updates team profile of a team |
| [**teamsTeamIdSetupProgressGet**](TeamsApi.md#teamsTeamIdSetupProgressGet) | **GET** /teams/{teamId}/setupProgress | Gets setup progress of a specific team. |


<a id="subscriptionsSubscriptionIdTeamsGet"></a>
# **subscriptionsSubscriptionIdTeamsGet**
> List&lt;TeamInfo&gt; subscriptionsSubscriptionIdTeamsGet(subscriptionId)

Get infos for all teams of the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | 
    try {
      List<TeamInfo> result = apiInstance.subscriptionsSubscriptionIdTeamsGet(subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#subscriptionsSubscriptionIdTeamsGet");
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
| **subscriptionId** | **String**|  | |

### Return type

[**List&lt;TeamInfo&gt;**](TeamInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="teamsGet"></a>
# **teamsGet**
> List&lt;TeamInfo&gt; teamsGet()

Get infos of all teams.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    try {
      List<TeamInfo> result = apiInstance.teamsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsGet");
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

[**List&lt;TeamInfo&gt;**](TeamInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="teamsTeamIdAlertReportsFileNameGet"></a>
# **teamsTeamIdAlertReportsFileNameGet**
> File teamsTeamIdAlertReportsFileNameGet(teamId, fileName)

Returns Alert Report

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of team you want to get the duty report file infos for.
    String fileName = "fileName_example"; // String | File name of file you want to download.
    try {
      File result = apiInstance.teamsTeamIdAlertReportsFileNameGet(teamId, fileName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsTeamIdAlertReportsFileNameGet");
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
| **teamId** | **String**| ID of team you want to get the duty report file infos for. | |
| **fileName** | **String**| File name of file you want to download. | |

### Return type

[**File**](File.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="teamsTeamIdAlertReportsGet"></a>
# **teamsTeamIdAlertReportsGet**
> List&lt;Object&gt; teamsTeamIdAlertReportsGet(teamId)

Get information about downloadable alert reports

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of team you want to download reports from.
    try {
      List<Object> result = apiInstance.teamsTeamIdAlertReportsGet(teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsTeamIdAlertReportsGet");
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
| **teamId** | **String**| ID of team you want to download reports from. | |

### Return type

**List&lt;Object&gt;**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="teamsTeamIdAlertSettingsGet"></a>
# **teamsTeamIdAlertSettingsGet**
> AlertSettings teamsTeamIdAlertSettingsGet(teamId)

Gets alert settings of a specific team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of the team the settings should be retrieved for.
    try {
      AlertSettings result = apiInstance.teamsTeamIdAlertSettingsGet(teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsTeamIdAlertSettingsGet");
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
| **teamId** | **String**| ID of the team the settings should be retrieved for. | |

### Return type

[**AlertSettings**](AlertSettings.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="teamsTeamIdAlertSettingsPost"></a>
# **teamsTeamIdAlertSettingsPost**
> AlertSettings teamsTeamIdAlertSettingsPost(teamId, alertSettings)

Sets alert settings of a specific team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of the team the settings should be set for.
    AlertSettings alertSettings = new AlertSettings(); // AlertSettings | Alert settings to be set
    try {
      AlertSettings result = apiInstance.teamsTeamIdAlertSettingsPost(teamId, alertSettings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsTeamIdAlertSettingsPost");
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
| **teamId** | **String**| ID of the team the settings should be set for. | |
| **alertSettings** | [**AlertSettings**](AlertSettings.md)| Alert settings to be set | [optional] |

### Return type

[**AlertSettings**](AlertSettings.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="teamsTeamIdEventSourcesGet"></a>
# **teamsTeamIdEventSourcesGet**
> List&lt;EventSourceEndpointInfo&gt; teamsTeamIdEventSourcesGet(teamId)

Gets event sources of a specific team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of the team the sources should be retrieved for.
    try {
      List<EventSourceEndpointInfo> result = apiInstance.teamsTeamIdEventSourcesGet(teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsTeamIdEventSourcesGet");
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
| **teamId** | **String**| ID of the team the sources should be retrieved for. | |

### Return type

[**List&lt;EventSourceEndpointInfo&gt;**](EventSourceEndpointInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="teamsTeamIdGet"></a>
# **teamsTeamIdGet**
> TeamInfo teamsTeamIdGet(teamId)

Gets infos of a specific team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of the team that should be retrieved.
    try {
      TeamInfo result = apiInstance.teamsTeamIdGet(teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsTeamIdGet");
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
| **teamId** | **String**| ID of the team that should be retrieved. | |

### Return type

[**TeamInfo**](TeamInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="teamsTeamIdProfilePut"></a>
# **teamsTeamIdProfilePut**
> TeamInfo teamsTeamIdProfilePut(teamId, teamProfile)

Updates team profile of a team

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String teamId = "teamId_example"; // String | Team ID of team which should be updated.
    TeamProfile teamProfile = new TeamProfile(); // TeamProfile | 
    try {
      TeamInfo result = apiInstance.teamsTeamIdProfilePut(teamId, teamProfile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsTeamIdProfilePut");
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
| **teamId** | **String**| Team ID of team which should be updated. | |
| **teamProfile** | [**TeamProfile**](TeamProfile.md)|  | [optional] |

### Return type

[**TeamInfo**](TeamInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Server Error |  -  |

<a id="teamsTeamIdSetupProgressGet"></a>
# **teamsTeamIdSetupProgressGet**
> TeamSetupProgress teamsTeamIdSetupProgressGet(teamId)

Gets setup progress of a specific team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of the team the progress should be retrieved for.
    try {
      TeamSetupProgress result = apiInstance.teamsTeamIdSetupProgressGet(teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsTeamIdSetupProgressGet");
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
| **teamId** | **String**| ID of the team the progress should be retrieved for. | |

### Return type

[**TeamSetupProgress**](TeamSetupProgress.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

