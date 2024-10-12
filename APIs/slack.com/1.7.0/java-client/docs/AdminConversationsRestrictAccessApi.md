# AdminConversationsRestrictAccessApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminConversationsRestrictAccessAddGroup**](AdminConversationsRestrictAccessApi.md#adminConversationsRestrictAccessAddGroup) | **POST** /admin.conversations.restrictAccess.addGroup |  |
| [**adminConversationsRestrictAccessListGroups**](AdminConversationsRestrictAccessApi.md#adminConversationsRestrictAccessListGroups) | **GET** /admin.conversations.restrictAccess.listGroups |  |
| [**adminConversationsRestrictAccessRemoveGroup**](AdminConversationsRestrictAccessApi.md#adminConversationsRestrictAccessRemoveGroup) | **POST** /admin.conversations.restrictAccess.removeGroup |  |


<a id="adminConversationsRestrictAccessAddGroup"></a>
# **adminConversationsRestrictAccessAddGroup**
> DefaultSuccessTemplate adminConversationsRestrictAccessAddGroup(channelId, groupId, token, teamId)



Add an allowlist of IDP groups for accessing a channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminConversationsRestrictAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminConversationsRestrictAccessApi apiInstance = new AdminConversationsRestrictAccessApi(defaultClient);
    String channelId = "channelId_example"; // String | The channel to link this group to.
    String groupId = "groupId_example"; // String | The [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) ID to be an allowlist for the private channel.
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:write`
    String teamId = "teamId_example"; // String | The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization.
    try {
      DefaultSuccessTemplate result = apiInstance.adminConversationsRestrictAccessAddGroup(channelId, groupId, token, teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminConversationsRestrictAccessApi#adminConversationsRestrictAccessAddGroup");
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
| **channelId** | **String**| The channel to link this group to. | |
| **groupId** | **String**| The [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) ID to be an allowlist for the private channel. | |
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.conversations:write&#x60; | |
| **teamId** | **String**| The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization. | [optional] |

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

<a id="adminConversationsRestrictAccessListGroups"></a>
# **adminConversationsRestrictAccessListGroups**
> DefaultSuccessTemplate adminConversationsRestrictAccessListGroups(token, channelId, teamId)



List all IDP Groups linked to a channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminConversationsRestrictAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminConversationsRestrictAccessApi apiInstance = new AdminConversationsRestrictAccessApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:read`
    String channelId = "channelId_example"; // String | 
    String teamId = "teamId_example"; // String | The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization.
    try {
      DefaultSuccessTemplate result = apiInstance.adminConversationsRestrictAccessListGroups(token, channelId, teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminConversationsRestrictAccessApi#adminConversationsRestrictAccessListGroups");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.conversations:read&#x60; | |
| **channelId** | **String**|  | |
| **teamId** | **String**| The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization. | [optional] |

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

<a id="adminConversationsRestrictAccessRemoveGroup"></a>
# **adminConversationsRestrictAccessRemoveGroup**
> DefaultSuccessTemplate adminConversationsRestrictAccessRemoveGroup(channelId, groupId, teamId, token)



Remove a linked IDP group linked from a private channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminConversationsRestrictAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminConversationsRestrictAccessApi apiInstance = new AdminConversationsRestrictAccessApi(defaultClient);
    String channelId = "channelId_example"; // String | The channel to remove the linked group from.
    String groupId = "groupId_example"; // String | The [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) ID to remove from the private channel.
    String teamId = "teamId_example"; // String | The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization.
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:write`
    try {
      DefaultSuccessTemplate result = apiInstance.adminConversationsRestrictAccessRemoveGroup(channelId, groupId, teamId, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminConversationsRestrictAccessApi#adminConversationsRestrictAccessRemoveGroup");
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
| **channelId** | **String**| The channel to remove the linked group from. | |
| **groupId** | **String**| The [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) ID to remove from the private channel. | |
| **teamId** | **String**| The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization. | |
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.conversations:write&#x60; | |

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

