# AdminUsergroupsApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminUsergroupsAddChannels**](AdminUsergroupsApi.md#adminUsergroupsAddChannels) | **POST** /admin.usergroups.addChannels |  |
| [**adminUsergroupsAddTeams**](AdminUsergroupsApi.md#adminUsergroupsAddTeams) | **POST** /admin.usergroups.addTeams |  |
| [**adminUsergroupsListChannels**](AdminUsergroupsApi.md#adminUsergroupsListChannels) | **GET** /admin.usergroups.listChannels |  |
| [**adminUsergroupsRemoveChannels**](AdminUsergroupsApi.md#adminUsergroupsRemoveChannels) | **POST** /admin.usergroups.removeChannels |  |


<a id="adminUsergroupsAddChannels"></a>
# **adminUsergroupsAddChannels**
> DefaultSuccessTemplate adminUsergroupsAddChannels(token, channelIds, usergroupId, teamId)



Add one or more default channels to an IDP group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminUsergroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminUsergroupsApi apiInstance = new AdminUsergroupsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.usergroups:write`
    String channelIds = "channelIds_example"; // String | Comma separated string of channel IDs.
    String usergroupId = "usergroupId_example"; // String | ID of the IDP group to add default channels for.
    String teamId = "teamId_example"; // String | The workspace to add default channels in.
    try {
      DefaultSuccessTemplate result = apiInstance.adminUsergroupsAddChannels(token, channelIds, usergroupId, teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminUsergroupsApi#adminUsergroupsAddChannels");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.usergroups:write&#x60; | |
| **channelIds** | **String**| Comma separated string of channel IDs. | |
| **usergroupId** | **String**| ID of the IDP group to add default channels for. | |
| **teamId** | **String**| The workspace to add default channels in. | [optional] |

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
| **0** | Typical error response if the token provided is not associated with an Org Admin or Owner |  -  |

<a id="adminUsergroupsAddTeams"></a>
# **adminUsergroupsAddTeams**
> DefaultSuccessTemplate adminUsergroupsAddTeams(token, teamIds, usergroupId, autoProvision)



Associate one or more default workspaces with an organization-wide IDP group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminUsergroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminUsergroupsApi apiInstance = new AdminUsergroupsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
    String teamIds = "teamIds_example"; // String | A comma separated list of encoded team (workspace) IDs. Each workspace *MUST* belong to the organization associated with the token.
    String usergroupId = "usergroupId_example"; // String | An encoded usergroup (IDP Group) ID.
    Boolean autoProvision = true; // Boolean | When `true`, this method automatically creates new workspace accounts for the IDP group members.
    try {
      DefaultSuccessTemplate result = apiInstance.adminUsergroupsAddTeams(token, teamIds, usergroupId, autoProvision);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminUsergroupsApi#adminUsergroupsAddTeams");
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
| **teamIds** | **String**| A comma separated list of encoded team (workspace) IDs. Each workspace *MUST* belong to the organization associated with the token. | |
| **usergroupId** | **String**| An encoded usergroup (IDP Group) ID. | |
| **autoProvision** | **Boolean**| When &#x60;true&#x60;, this method automatically creates new workspace accounts for the IDP group members. | [optional] |

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

<a id="adminUsergroupsListChannels"></a>
# **adminUsergroupsListChannels**
> DefaultSuccessTemplate adminUsergroupsListChannels(token, usergroupId, teamId, includeNumMembers)



List the channels linked to an org-level IDP group (user group).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminUsergroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminUsergroupsApi apiInstance = new AdminUsergroupsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.usergroups:read`
    String usergroupId = "usergroupId_example"; // String | ID of the IDP group to list default channels for.
    String teamId = "teamId_example"; // String | ID of the the workspace.
    Boolean includeNumMembers = true; // Boolean | Flag to include or exclude the count of members per channel.
    try {
      DefaultSuccessTemplate result = apiInstance.adminUsergroupsListChannels(token, usergroupId, teamId, includeNumMembers);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminUsergroupsApi#adminUsergroupsListChannels");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.usergroups:read&#x60; | |
| **usergroupId** | **String**| ID of the IDP group to list default channels for. | |
| **teamId** | **String**| ID of the the workspace. | [optional] |
| **includeNumMembers** | **Boolean**| Flag to include or exclude the count of members per channel. | [optional] |

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
| **0** | Typical error response if the token provided is not associated with an Org Admin or Owner |  -  |

<a id="adminUsergroupsRemoveChannels"></a>
# **adminUsergroupsRemoveChannels**
> DefaultSuccessTemplate adminUsergroupsRemoveChannels(token, channelIds, usergroupId)



Remove one or more default channels from an org-level IDP group (user group).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminUsergroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminUsergroupsApi apiInstance = new AdminUsergroupsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.usergroups:write`
    String channelIds = "channelIds_example"; // String | Comma-separated string of channel IDs
    String usergroupId = "usergroupId_example"; // String | ID of the IDP Group
    try {
      DefaultSuccessTemplate result = apiInstance.adminUsergroupsRemoveChannels(token, channelIds, usergroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminUsergroupsApi#adminUsergroupsRemoveChannels");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.usergroups:write&#x60; | |
| **channelIds** | **String**| Comma-separated string of channel IDs | |
| **usergroupId** | **String**| ID of the IDP Group | |

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
| **0** | Typical error response if the token provided is not associated with an Org Admin or Owner |  -  |

