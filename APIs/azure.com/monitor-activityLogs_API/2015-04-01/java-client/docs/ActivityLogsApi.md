# ActivityLogsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activityLogsList**](ActivityLogsApi.md#activityLogsList) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/eventtypes/management/values |  |


<a id="activityLogsList"></a>
# **activityLogsList**
> EventDataCollection activityLogsList(apiVersion, $filter, subscriptionId, $select)



Provides the list of records from the activity logs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityLogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ActivityLogsApi apiInstance = new ActivityLogsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | Reduces the set of data collected.<br>This argument is required and it also requires at least the start date/time.<br>The **$filter** argument is very restricted and allows only the following patterns.<br>- *List events for a resource group*: $filter=eventTimestamp ge '2014-07-16T04:36:37.6407898Z' and eventTimestamp le '2014-07-20T04:36:37.6407898Z' and resourceGroupName eq 'resourceGroupName'.<br>- *List events for resource*: $filter=eventTimestamp ge '2014-07-16T04:36:37.6407898Z' and eventTimestamp le '2014-07-20T04:36:37.6407898Z' and resourceUri eq 'resourceURI'.<br>- *List events for a subscription in a time range*: $filter=eventTimestamp ge '2014-07-16T04:36:37.6407898Z' and eventTimestamp le '2014-07-20T04:36:37.6407898Z'.<br>- *List events for a resource provider*: $filter=eventTimestamp ge '2014-07-16T04:36:37.6407898Z' and eventTimestamp le '2014-07-20T04:36:37.6407898Z' and resourceProvider eq 'resourceProviderName'.<br>- *List events for a correlation Id*: $filter=eventTimestamp ge '2014-07-16T04:36:37.6407898Z' and eventTimestamp le '2014-07-20T04:36:37.6407898Z' and correlationId eq 'correlationID'.<br><br>**NOTE**: No other syntax is allowed.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String $select = "$select_example"; // String | Used to fetch events with only the given properties.<br>The **$select** argument is a comma separated list of property names to be returned. Possible values are: *authorization*, *claims*, *correlationId*, *description*, *eventDataId*, *eventName*, *eventTimestamp*, *httpRequest*, *level*, *operationId*, *operationName*, *properties*, *resourceGroupName*, *resourceProviderName*, *resourceId*, *status*, *submissionTimestamp*, *subStatus*, *subscriptionId*
    try {
      EventDataCollection result = apiInstance.activityLogsList(apiVersion, $filter, subscriptionId, $select);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityLogsApi#activityLogsList");
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
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| Reduces the set of data collected.&lt;br&gt;This argument is required and it also requires at least the start date/time.&lt;br&gt;The **$filter** argument is very restricted and allows only the following patterns.&lt;br&gt;- *List events for a resource group*: $filter&#x3D;eventTimestamp ge &#39;2014-07-16T04:36:37.6407898Z&#39; and eventTimestamp le &#39;2014-07-20T04:36:37.6407898Z&#39; and resourceGroupName eq &#39;resourceGroupName&#39;.&lt;br&gt;- *List events for resource*: $filter&#x3D;eventTimestamp ge &#39;2014-07-16T04:36:37.6407898Z&#39; and eventTimestamp le &#39;2014-07-20T04:36:37.6407898Z&#39; and resourceUri eq &#39;resourceURI&#39;.&lt;br&gt;- *List events for a subscription in a time range*: $filter&#x3D;eventTimestamp ge &#39;2014-07-16T04:36:37.6407898Z&#39; and eventTimestamp le &#39;2014-07-20T04:36:37.6407898Z&#39;.&lt;br&gt;- *List events for a resource provider*: $filter&#x3D;eventTimestamp ge &#39;2014-07-16T04:36:37.6407898Z&#39; and eventTimestamp le &#39;2014-07-20T04:36:37.6407898Z&#39; and resourceProvider eq &#39;resourceProviderName&#39;.&lt;br&gt;- *List events for a correlation Id*: $filter&#x3D;eventTimestamp ge &#39;2014-07-16T04:36:37.6407898Z&#39; and eventTimestamp le &#39;2014-07-20T04:36:37.6407898Z&#39; and correlationId eq &#39;correlationID&#39;.&lt;br&gt;&lt;br&gt;**NOTE**: No other syntax is allowed. | |
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **$select** | **String**| Used to fetch events with only the given properties.&lt;br&gt;The **$select** argument is a comma separated list of property names to be returned. Possible values are: *authorization*, *claims*, *correlationId*, *description*, *eventDataId*, *eventName*, *eventTimestamp*, *httpRequest*, *level*, *operationId*, *operationName*, *properties*, *resourceGroupName*, *resourceProviderName*, *resourceId*, *status*, *submissionTimestamp*, *subStatus*, *subscriptionId* | [optional] |

### Return type

[**EventDataCollection**](EventDataCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to get a page of events in the activity logs |  -  |
| **0** | Error response describing why the operation failed. |  -  |

