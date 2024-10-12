# AdminConversationsEkmApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminConversationsEkmListOriginalConnectedChannelInfo**](AdminConversationsEkmApi.md#adminConversationsEkmListOriginalConnectedChannelInfo) | **GET** /admin.conversations.ekm.listOriginalConnectedChannelInfo |  |


<a id="adminConversationsEkmListOriginalConnectedChannelInfo"></a>
# **adminConversationsEkmListOriginalConnectedChannelInfo**
> DefaultSuccessTemplate adminConversationsEkmListOriginalConnectedChannelInfo(token, channelIds, teamIds, limit, cursor)



List all disconnected channels—i.e., channels that were once connected to other workspaces and then disconnected—and the corresponding original channel IDs for key revocation with EKM.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminConversationsEkmApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminConversationsEkmApi apiInstance = new AdminConversationsEkmApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:read`
    String channelIds = "channelIds_example"; // String | A comma-separated list of channels to filter to.
    String teamIds = "teamIds_example"; // String | A comma-separated list of the workspaces to which the channels you would like returned belong.
    Integer limit = 56; // Integer | The maximum number of items to return. Must be between 1 - 1000 both inclusive.
    String cursor = "cursor_example"; // String | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.
    try {
      DefaultSuccessTemplate result = apiInstance.adminConversationsEkmListOriginalConnectedChannelInfo(token, channelIds, teamIds, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminConversationsEkmApi#adminConversationsEkmListOriginalConnectedChannelInfo");
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
| **channelIds** | **String**| A comma-separated list of channels to filter to. | [optional] |
| **teamIds** | **String**| A comma-separated list of the workspaces to which the channels you would like returned belong. | [optional] |
| **limit** | **Integer**| The maximum number of items to return. Must be between 1 - 1000 both inclusive. | [optional] |
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

