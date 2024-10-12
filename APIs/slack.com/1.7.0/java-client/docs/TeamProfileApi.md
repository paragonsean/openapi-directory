# TeamProfileApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**teamProfileGet**](TeamProfileApi.md#teamProfileGet) | **GET** /team.profile.get |  |


<a id="teamProfileGet"></a>
# **teamProfileGet**
> TeamProfileGetSuccessSchema teamProfileGet(token, visibility)



Retrieve a team&#39;s profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    TeamProfileApi apiInstance = new TeamProfileApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `users.profile:read`
    String visibility = "visibility_example"; // String | Filter by visibility.
    try {
      TeamProfileGetSuccessSchema result = apiInstance.teamProfileGet(token, visibility);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamProfileApi#teamProfileGet");
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

