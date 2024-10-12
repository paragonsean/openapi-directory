# AdminTeamsSettingsApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminTeamsSettingsInfo**](AdminTeamsSettingsApi.md#adminTeamsSettingsInfo) | **GET** /admin.teams.settings.info |  |
| [**adminTeamsSettingsSetDefaultChannels**](AdminTeamsSettingsApi.md#adminTeamsSettingsSetDefaultChannels) | **POST** /admin.teams.settings.setDefaultChannels |  |
| [**adminTeamsSettingsSetDescription**](AdminTeamsSettingsApi.md#adminTeamsSettingsSetDescription) | **POST** /admin.teams.settings.setDescription |  |
| [**adminTeamsSettingsSetDiscoverability**](AdminTeamsSettingsApi.md#adminTeamsSettingsSetDiscoverability) | **POST** /admin.teams.settings.setDiscoverability |  |
| [**adminTeamsSettingsSetIcon**](AdminTeamsSettingsApi.md#adminTeamsSettingsSetIcon) | **POST** /admin.teams.settings.setIcon |  |
| [**adminTeamsSettingsSetName**](AdminTeamsSettingsApi.md#adminTeamsSettingsSetName) | **POST** /admin.teams.settings.setName |  |


<a id="adminTeamsSettingsInfo"></a>
# **adminTeamsSettingsInfo**
> DefaultSuccessTemplate adminTeamsSettingsInfo(token, teamId)



Fetch information about settings in a workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminTeamsSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminTeamsSettingsApi apiInstance = new AdminTeamsSettingsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:read`
    String teamId = "teamId_example"; // String | 
    try {
      DefaultSuccessTemplate result = apiInstance.adminTeamsSettingsInfo(token, teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminTeamsSettingsApi#adminTeamsSettingsInfo");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:read&#x60; | |
| **teamId** | **String**|  | |

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

<a id="adminTeamsSettingsSetDefaultChannels"></a>
# **adminTeamsSettingsSetDefaultChannels**
> DefaultSuccessTemplate adminTeamsSettingsSetDefaultChannels(channelIds, teamId, token)



Set the default channels of a workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminTeamsSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminTeamsSettingsApi apiInstance = new AdminTeamsSettingsApi(defaultClient);
    String channelIds = "channelIds_example"; // String | An array of channel IDs.
    String teamId = "teamId_example"; // String | ID for the workspace to set the default channel for.
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
    try {
      DefaultSuccessTemplate result = apiInstance.adminTeamsSettingsSetDefaultChannels(channelIds, teamId, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminTeamsSettingsApi#adminTeamsSettingsSetDefaultChannels");
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
| **channelIds** | **String**| An array of channel IDs. | |
| **teamId** | **String**| ID for the workspace to set the default channel for. | |
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:write&#x60; | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

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

<a id="adminTeamsSettingsSetDescription"></a>
# **adminTeamsSettingsSetDescription**
> DefaultSuccessTemplate adminTeamsSettingsSetDescription(token, description, teamId)



Set the description of a given workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminTeamsSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminTeamsSettingsApi apiInstance = new AdminTeamsSettingsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
    String description = "description_example"; // String | The new description for the workspace.
    String teamId = "teamId_example"; // String | ID for the workspace to set the description for.
    try {
      DefaultSuccessTemplate result = apiInstance.adminTeamsSettingsSetDescription(token, description, teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminTeamsSettingsApi#adminTeamsSettingsSetDescription");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:write&#x60; | |
| **description** | **String**| The new description for the workspace. | |
| **teamId** | **String**| ID for the workspace to set the description for. | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

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

<a id="adminTeamsSettingsSetDiscoverability"></a>
# **adminTeamsSettingsSetDiscoverability**
> DefaultSuccessTemplate adminTeamsSettingsSetDiscoverability(token, discoverability, teamId)



An API method that allows admins to set the discoverability of a given workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminTeamsSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminTeamsSettingsApi apiInstance = new AdminTeamsSettingsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
    String discoverability = "discoverability_example"; // String | This workspace's discovery setting. It must be set to one of `open`, `invite_only`, `closed`, or `unlisted`.
    String teamId = "teamId_example"; // String | The ID of the workspace to set discoverability on.
    try {
      DefaultSuccessTemplate result = apiInstance.adminTeamsSettingsSetDiscoverability(token, discoverability, teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminTeamsSettingsApi#adminTeamsSettingsSetDiscoverability");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:write&#x60; | |
| **discoverability** | **String**| This workspace&#39;s discovery setting. It must be set to one of &#x60;open&#x60;, &#x60;invite_only&#x60;, &#x60;closed&#x60;, or &#x60;unlisted&#x60;. | |
| **teamId** | **String**| The ID of the workspace to set discoverability on. | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

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

<a id="adminTeamsSettingsSetIcon"></a>
# **adminTeamsSettingsSetIcon**
> DefaultSuccessTemplate adminTeamsSettingsSetIcon(imageUrl, teamId, token)



Sets the icon of a workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminTeamsSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminTeamsSettingsApi apiInstance = new AdminTeamsSettingsApi(defaultClient);
    String imageUrl = "imageUrl_example"; // String | Image URL for the icon
    String teamId = "teamId_example"; // String | ID for the workspace to set the icon for.
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
    try {
      DefaultSuccessTemplate result = apiInstance.adminTeamsSettingsSetIcon(imageUrl, teamId, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminTeamsSettingsApi#adminTeamsSettingsSetIcon");
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
| **imageUrl** | **String**| Image URL for the icon | |
| **teamId** | **String**| ID for the workspace to set the icon for. | |
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:write&#x60; | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

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

<a id="adminTeamsSettingsSetName"></a>
# **adminTeamsSettingsSetName**
> DefaultSuccessTemplate adminTeamsSettingsSetName(token, name, teamId)



Set the name of a given workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminTeamsSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminTeamsSettingsApi apiInstance = new AdminTeamsSettingsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
    String name = "name_example"; // String | The new name of the workspace.
    String teamId = "teamId_example"; // String | ID for the workspace to set the name for.
    try {
      DefaultSuccessTemplate result = apiInstance.adminTeamsSettingsSetName(token, name, teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminTeamsSettingsApi#adminTeamsSettingsSetName");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:write&#x60; | |
| **name** | **String**| The new name of the workspace. | |
| **teamId** | **String**| ID for the workspace to set the name for. | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

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

