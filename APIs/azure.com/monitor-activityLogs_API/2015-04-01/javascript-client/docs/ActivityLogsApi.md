# MonitorManagementClient.ActivityLogsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activityLogsList**](ActivityLogsApi.md#activityLogsList) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/eventtypes/management/values | 



## activityLogsList

> EventDataCollection activityLogsList(apiVersion, filter, subscriptionId, opts)



Provides the list of records from the activity logs.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.ActivityLogsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let filter = "filter_example"; // String | Reduces the set of data collected.<br>This argument is required and it also requires at least the start date/time.<br>The **$filter** argument is very restricted and allows only the following patterns.<br>- *List events for a resource group*: $filter=eventTimestamp ge '2014-07-16T04:36:37.6407898Z' and eventTimestamp le '2014-07-20T04:36:37.6407898Z' and resourceGroupName eq 'resourceGroupName'.<br>- *List events for resource*: $filter=eventTimestamp ge '2014-07-16T04:36:37.6407898Z' and eventTimestamp le '2014-07-20T04:36:37.6407898Z' and resourceUri eq 'resourceURI'.<br>- *List events for a subscription in a time range*: $filter=eventTimestamp ge '2014-07-16T04:36:37.6407898Z' and eventTimestamp le '2014-07-20T04:36:37.6407898Z'.<br>- *List events for a resource provider*: $filter=eventTimestamp ge '2014-07-16T04:36:37.6407898Z' and eventTimestamp le '2014-07-20T04:36:37.6407898Z' and resourceProvider eq 'resourceProviderName'.<br>- *List events for a correlation Id*: $filter=eventTimestamp ge '2014-07-16T04:36:37.6407898Z' and eventTimestamp le '2014-07-20T04:36:37.6407898Z' and correlationId eq 'correlationID'.<br><br>**NOTE**: No other syntax is allowed.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let opts = {
  'select': "select_example" // String | Used to fetch events with only the given properties.<br>The **$select** argument is a comma separated list of property names to be returned. Possible values are: *authorization*, *claims*, *correlationId*, *description*, *eventDataId*, *eventName*, *eventTimestamp*, *httpRequest*, *level*, *operationId*, *operationName*, *properties*, *resourceGroupName*, *resourceProviderName*, *resourceId*, *status*, *submissionTimestamp*, *subStatus*, *subscriptionId*
};
apiInstance.activityLogsList(apiVersion, filter, subscriptionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| Reduces the set of data collected.&lt;br&gt;This argument is required and it also requires at least the start date/time.&lt;br&gt;The **$filter** argument is very restricted and allows only the following patterns.&lt;br&gt;- *List events for a resource group*: $filter&#x3D;eventTimestamp ge &#39;2014-07-16T04:36:37.6407898Z&#39; and eventTimestamp le &#39;2014-07-20T04:36:37.6407898Z&#39; and resourceGroupName eq &#39;resourceGroupName&#39;.&lt;br&gt;- *List events for resource*: $filter&#x3D;eventTimestamp ge &#39;2014-07-16T04:36:37.6407898Z&#39; and eventTimestamp le &#39;2014-07-20T04:36:37.6407898Z&#39; and resourceUri eq &#39;resourceURI&#39;.&lt;br&gt;- *List events for a subscription in a time range*: $filter&#x3D;eventTimestamp ge &#39;2014-07-16T04:36:37.6407898Z&#39; and eventTimestamp le &#39;2014-07-20T04:36:37.6407898Z&#39;.&lt;br&gt;- *List events for a resource provider*: $filter&#x3D;eventTimestamp ge &#39;2014-07-16T04:36:37.6407898Z&#39; and eventTimestamp le &#39;2014-07-20T04:36:37.6407898Z&#39; and resourceProvider eq &#39;resourceProviderName&#39;.&lt;br&gt;- *List events for a correlation Id*: $filter&#x3D;eventTimestamp ge &#39;2014-07-16T04:36:37.6407898Z&#39; and eventTimestamp le &#39;2014-07-20T04:36:37.6407898Z&#39; and correlationId eq &#39;correlationID&#39;.&lt;br&gt;&lt;br&gt;**NOTE**: No other syntax is allowed. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **select** | **String**| Used to fetch events with only the given properties.&lt;br&gt;The **$select** argument is a comma separated list of property names to be returned. Possible values are: *authorization*, *claims*, *correlationId*, *description*, *eventDataId*, *eventName*, *eventTimestamp*, *httpRequest*, *level*, *operationId*, *operationName*, *properties*, *resourceGroupName*, *resourceProviderName*, *resourceId*, *status*, *submissionTimestamp*, *subStatus*, *subscriptionId* | [optional] 

### Return type

[**EventDataCollection**](EventDataCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

