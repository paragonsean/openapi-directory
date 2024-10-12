# DialogApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dialogOpen**](DialogApi.md#dialogOpen) | **GET** /dialog.open |  |


<a id="dialogOpen"></a>
# **dialogOpen**
> DialogOpenSchema dialogOpen(token, dialog, triggerId)



Open a dialog with a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DialogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    DialogApi apiInstance = new DialogApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `none`
    String dialog = "dialog_example"; // String | The dialog definition. This must be a JSON-encoded string.
    String triggerId = "triggerId_example"; // String | Exchange a trigger to post to the user.
    try {
      DialogOpenSchema result = apiInstance.dialogOpen(token, dialog, triggerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DialogApi#dialogOpen");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;none&#x60; | |
| **dialog** | **String**| The dialog definition. This must be a JSON-encoded string. | |
| **triggerId** | **String**| Exchange a trigger to post to the user. | |

### Return type

[**DialogOpenSchema**](DialogOpenSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response is quite minimal. |  -  |
| **0** | Typical error response, before getting to any possible validation errors. |  -  |

