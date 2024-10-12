# AutopilotV1TaskStatisticsApi

All URIs are relative to *https://autopilot.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchTaskStatistics**](AutopilotV1TaskStatisticsApi.md#fetchTaskStatistics) | **GET** /v1/Assistants/{AssistantSid}/Tasks/{TaskSid}/Statistics |  |


<a id="fetchTaskStatistics"></a>
# **fetchTaskStatistics**
> AutopilotV1AssistantTaskTaskStatistics fetchTaskStatistics(assistantSid, taskSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutopilotV1TaskStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://autopilot.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AutopilotV1TaskStatisticsApi apiInstance = new AutopilotV1TaskStatisticsApi(defaultClient);
    String assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
    String taskSid = "taskSid_example"; // String | The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) that is associated with the resource to fetch.
    try {
      AutopilotV1AssistantTaskTaskStatistics result = apiInstance.fetchTaskStatistics(assistantSid, taskSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutopilotV1TaskStatisticsApi#fetchTaskStatistics");
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
| **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch. | |
| **taskSid** | **String**| The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) that is associated with the resource to fetch. | |

### Return type

[**AutopilotV1AssistantTaskTaskStatistics**](AutopilotV1AssistantTaskTaskStatistics.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

