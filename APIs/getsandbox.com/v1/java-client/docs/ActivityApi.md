# ActivityApi

All URIs are relative to *https://getsandbox.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSandboxesActivity**](ActivityApi.md#getSandboxesActivity) | **GET** /1/activity/search | searchActivity |


<a id="getSandboxesActivity"></a>
# **getSandboxesActivity**
> List&lt;ActivityMessage&gt; getSandboxesActivity(fromTimestamp, sourceSandboxes, keyword, allTypes, maxResults)

searchActivity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://getsandbox.com/api");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    Long fromTimestamp = 56L; // Long | Timestamp to start search from, epoch time in milliseconds.
    String sourceSandboxes = "sourceSandboxes_example"; // String | Comma-separated list of Sandbox names to search.
    String keyword = "keyword_example"; // String | A keyword to search activities by, will match any part of the ActivityMessage.
    Boolean allTypes = true; // Boolean | Flag to return all types of activity, defaults to just Requests
    Integer maxResults = 56; // Integer | Maximum number of results to return
    try {
      List<ActivityMessage> result = apiInstance.getSandboxesActivity(fromTimestamp, sourceSandboxes, keyword, allTypes, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#getSandboxesActivity");
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
| **fromTimestamp** | **Long**| Timestamp to start search from, epoch time in milliseconds. | [optional] |
| **sourceSandboxes** | **String**| Comma-separated list of Sandbox names to search. | [optional] |
| **keyword** | **String**| A keyword to search activities by, will match any part of the ActivityMessage. | [optional] |
| **allTypes** | **Boolean**| Flag to return all types of activity, defaults to just Requests | [optional] |
| **maxResults** | **Integer**| Maximum number of results to return | [optional] |

### Return type

[**List&lt;ActivityMessage&gt;**](ActivityMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

