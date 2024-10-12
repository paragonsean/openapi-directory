# AdminInviteRequestsDeniedApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminInviteRequestsDeniedList**](AdminInviteRequestsDeniedApi.md#adminInviteRequestsDeniedList) | **GET** /admin.inviteRequests.denied.list |  |


<a id="adminInviteRequestsDeniedList"></a>
# **adminInviteRequestsDeniedList**
> DefaultSuccessTemplate adminInviteRequestsDeniedList(token, teamId, cursor, limit)



List all denied workspace invite requests.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminInviteRequestsDeniedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminInviteRequestsDeniedApi apiInstance = new AdminInviteRequestsDeniedApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.invites:read`
    String teamId = "teamId_example"; // String | ID for the workspace where the invite requests were made.
    String cursor = "cursor_example"; // String | Value of the `next_cursor` field sent as part of the previous api response
    Integer limit = 56; // Integer | The number of results that will be returned by the API on each invocation. Must be between 1 - 1000 both inclusive
    try {
      DefaultSuccessTemplate result = apiInstance.adminInviteRequestsDeniedList(token, teamId, cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminInviteRequestsDeniedApi#adminInviteRequestsDeniedList");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.invites:read&#x60; | |
| **teamId** | **String**| ID for the workspace where the invite requests were made. | [optional] |
| **cursor** | **String**| Value of the &#x60;next_cursor&#x60; field sent as part of the previous api response | [optional] |
| **limit** | **Integer**| The number of results that will be returned by the API on each invocation. Must be between 1 - 1000 both inclusive | [optional] |

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

