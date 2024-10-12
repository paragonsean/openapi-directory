# TaskrouterV1TaskQueuesStatisticsApi

All URIs are relative to *https://taskrouter.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listTaskQueuesStatistics**](TaskrouterV1TaskQueuesStatisticsApi.md#listTaskQueuesStatistics) | **GET** /v1/Workspaces/{WorkspaceSid}/TaskQueues/Statistics |  |


<a id="listTaskQueuesStatistics"></a>
# **listTaskQueuesStatistics**
> ListTaskQueuesStatisticsResponse listTaskQueuesStatistics(workspaceSid, endDate, friendlyName, minutes, startDate, taskChannel, splitByWaitTime, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1TaskQueuesStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1TaskQueuesStatisticsApi apiInstance = new TaskrouterV1TaskQueuesStatisticsApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the TaskQueues to read.
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
    String friendlyName = "friendlyName_example"; // String | The `friendly_name` of the TaskQueue statistics to read.
    Integer minutes = 56; // Integer | Only calculate statistics since this many minutes in the past. The default is 15 minutes.
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    String taskChannel = "taskChannel_example"; // String | Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
    String splitByWaitTime = "splitByWaitTime_example"; // String | A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListTaskQueuesStatisticsResponse result = apiInstance.listTaskQueuesStatistics(workspaceSid, endDate, friendlyName, minutes, startDate, taskChannel, splitByWaitTime, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1TaskQueuesStatisticsApi#listTaskQueuesStatistics");
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
| **workspaceSid** | **String**| The SID of the Workspace with the TaskQueues to read. | |
| **endDate** | **OffsetDateTime**| Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time. | [optional] |
| **friendlyName** | **String**| The &#x60;friendly_name&#x60; of the TaskQueue statistics to read. | [optional] |
| **minutes** | **Integer**| Only calculate statistics since this many minutes in the past. The default is 15 minutes. | [optional] |
| **startDate** | **OffsetDateTime**| Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] |
| **taskChannel** | **String**| Only calculate statistics on this TaskChannel. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;. | [optional] |
| **splitByWaitTime** | **String**| A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListTaskQueuesStatisticsResponse**](ListTaskQueuesStatisticsResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

