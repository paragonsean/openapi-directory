# AdminTeamsAdminsApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminTeamsAdminsList**](AdminTeamsAdminsApi.md#adminTeamsAdminsList) | **GET** /admin.teams.admins.list |  |


<a id="adminTeamsAdminsList"></a>
# **adminTeamsAdminsList**
> DefaultSuccessTemplate adminTeamsAdminsList(token, teamId, limit, cursor)



List all of the admins on a given workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminTeamsAdminsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminTeamsAdminsApi apiInstance = new AdminTeamsAdminsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:read`
    String teamId = "teamId_example"; // String | 
    Integer limit = 56; // Integer | The maximum number of items to return.
    String cursor = "cursor_example"; // String | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.
    try {
      DefaultSuccessTemplate result = apiInstance.adminTeamsAdminsList(token, teamId, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminTeamsAdminsApi#adminTeamsAdminsList");
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
| **limit** | **Integer**| The maximum number of items to return. | [optional] |
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

