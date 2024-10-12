# AdminTeamsApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminTeamsCreate**](AdminTeamsApi.md#adminTeamsCreate) | **POST** /admin.teams.create |  |
| [**adminTeamsList**](AdminTeamsApi.md#adminTeamsList) | **GET** /admin.teams.list |  |


<a id="adminTeamsCreate"></a>
# **adminTeamsCreate**
> DefaultSuccessTemplate adminTeamsCreate(token, teamDomain, teamName, teamDescription, teamDiscoverability)



Create an Enterprise team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminTeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminTeamsApi apiInstance = new AdminTeamsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
    String teamDomain = "teamDomain_example"; // String | Team domain (for example, slacksoftballteam).
    String teamName = "teamName_example"; // String | Team name (for example, Slack Softball Team).
    String teamDescription = "teamDescription_example"; // String | Description for the team.
    String teamDiscoverability = "teamDiscoverability_example"; // String | Who can join the team. A team's discoverability can be `open`, `closed`, `invite_only`, or `unlisted`.
    try {
      DefaultSuccessTemplate result = apiInstance.adminTeamsCreate(token, teamDomain, teamName, teamDescription, teamDiscoverability);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminTeamsApi#adminTeamsCreate");
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
| **teamDomain** | **String**| Team domain (for example, slacksoftballteam). | |
| **teamName** | **String**| Team name (for example, Slack Softball Team). | |
| **teamDescription** | **String**| Description for the team. | [optional] |
| **teamDiscoverability** | **String**| Who can join the team. A team&#39;s discoverability can be &#x60;open&#x60;, &#x60;closed&#x60;, &#x60;invite_only&#x60;, or &#x60;unlisted&#x60;. | [optional] |

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

<a id="adminTeamsList"></a>
# **adminTeamsList**
> DefaultSuccessTemplate adminTeamsList(token, limit, cursor)



List all teams on an Enterprise organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminTeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminTeamsApi apiInstance = new AdminTeamsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:read`
    Integer limit = 56; // Integer | The maximum number of items to return. Must be between 1 - 100 both inclusive.
    String cursor = "cursor_example"; // String | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.
    try {
      DefaultSuccessTemplate result = apiInstance.adminTeamsList(token, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminTeamsApi#adminTeamsList");
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
| **limit** | **Integer**| The maximum number of items to return. Must be between 1 - 100 both inclusive. | [optional] |
| **cursor** | **String**| Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page. | [optional] |

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

