# BotsApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**botsInfo**](BotsApi.md#botsInfo) | **GET** /bots.info |  |


<a id="botsInfo"></a>
# **botsInfo**
> BotsInfoSchema botsInfo(token, bot)



Gets information about a bot user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    BotsApi apiInstance = new BotsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `users:read`
    String bot = "bot_example"; // String | Bot user to get info on
    try {
      BotsInfoSchema result = apiInstance.botsInfo(token, bot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BotsApi#botsInfo");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;users:read&#x60; | |
| **bot** | **String**| Bot user to get info on | [optional] |

### Return type

[**BotsInfoSchema**](BotsInfoSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | When successful, returns bot info by bot ID. |  -  |
| **0** | When no bot can be found, it returns an error. |  -  |

