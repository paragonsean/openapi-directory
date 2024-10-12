# TerminalActionsTerminalLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postTerminalsScheduleActions**](TerminalActionsTerminalLevelApi.md#postTerminalsScheduleActions) | **POST** /terminals/scheduleActions | Create a terminal action |


<a id="postTerminalsScheduleActions"></a>
# **postTerminalsScheduleActions**
> ScheduleTerminalActionsResponse postTerminalsScheduleActions(scheduleTerminalActionsRequest)

Create a terminal action

Schedules a [terminal action](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api) by specifying the action and the terminals that the action must be applied to.   The following restrictions apply: * You can schedule only one action at a time. For example, to install a new app version and remove an old app version, you have to make two API requests.  * The maximum number of terminals in a request is **100**. For example, to apply an action to 250 terminals, you have to divide the terminals over three API requests.  * If there is an error with one or more terminal IDs in the request, the action is scheduled for none of the terminals. You need to fix the error and try again.   To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal actions read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalActionsTerminalLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TerminalActionsTerminalLevelApi apiInstance = new TerminalActionsTerminalLevelApi(defaultClient);
    ScheduleTerminalActionsRequest scheduleTerminalActionsRequest = new ScheduleTerminalActionsRequest(); // ScheduleTerminalActionsRequest | 
    try {
      ScheduleTerminalActionsResponse result = apiInstance.postTerminalsScheduleActions(scheduleTerminalActionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalActionsTerminalLevelApi#postTerminalsScheduleActions");
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
| **scheduleTerminalActionsRequest** | [**ScheduleTerminalActionsRequest**](ScheduleTerminalActionsRequest.md)|  | [optional] |

### Return type

[**ScheduleTerminalActionsResponse**](ScheduleTerminalActionsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

