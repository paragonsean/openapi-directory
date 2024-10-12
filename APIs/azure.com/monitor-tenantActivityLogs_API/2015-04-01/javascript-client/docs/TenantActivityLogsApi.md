# MonitorManagementClient.TenantActivityLogsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenantActivityLogsList**](TenantActivityLogsApi.md#tenantActivityLogsList) | **GET** /providers/microsoft.insights/eventtypes/management/values | 



## tenantActivityLogsList

> EventDataCollection tenantActivityLogsList(apiVersion, opts)



Gets the Activity Logs for the Tenant.&lt;br&gt;Everything that is applicable to the API to get the Activity Logs for the subscription is applicable to this API (the parameters, $filter, etc.).&lt;br&gt;One thing to point out here is that this API does *not* retrieve the logs at the individual subscription of the tenant but only surfaces the logs that were generated at the tenant level.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.TenantActivityLogsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | Reduces the set of data collected. <br>The **$filter** is very restricted and allows only the following patterns.<br>- List events for a resource group: $filter=eventTimestamp ge '<Start Time>' and eventTimestamp le '<End Time>' and eventChannels eq 'Admin, Operation' and resourceGroupName eq '<ResourceGroupName>'.<br>- List events for resource: $filter=eventTimestamp ge '<Start Time>' and eventTimestamp le '<End Time>' and eventChannels eq 'Admin, Operation' and resourceUri eq '<ResourceURI>'.<br>- List events for a subscription: $filter=eventTimestamp ge '<Start Time>' and eventTimestamp le '<End Time>' and eventChannels eq 'Admin, Operation'.<br>- List events for a resource provider: $filter=eventTimestamp ge '<Start Time>' and eventTimestamp le '<End Time>' and eventChannels eq 'Admin, Operation' and resourceProvider eq '<ResourceProviderName>'.<br>- List events for a correlation Id: api-version=2014-04-01&$filter=eventTimestamp ge '2014-07-16T04:36:37.6407898Z' and eventTimestamp le '2014-07-20T04:36:37.6407898Z' and eventChannels eq 'Admin, Operation' and correlationId eq '<CorrelationID>'.<br>**NOTE**: No other syntax is allowed.
  'select': "select_example" // String | Used to fetch events with only the given properties.<br>The **$select** argument is a comma separated list of property names to be returned. Possible values are: *authorization*, *claims*, *correlationId*, *description*, *eventDataId*, *eventName*, *eventTimestamp*, *httpRequest*, *level*, *operationId*, *operationName*, *properties*, *resourceGroupName*, *resourceProviderName*, *resourceId*, *status*, *submissionTimestamp*, *subStatus*, *subscriptionId*
};
apiInstance.tenantActivityLogsList(apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| Reduces the set of data collected. &lt;br&gt;The **$filter** is very restricted and allows only the following patterns.&lt;br&gt;- List events for a resource group: $filter&#x3D;eventTimestamp ge &#39;&lt;Start Time&gt;&#39; and eventTimestamp le &#39;&lt;End Time&gt;&#39; and eventChannels eq &#39;Admin, Operation&#39; and resourceGroupName eq &#39;&lt;ResourceGroupName&gt;&#39;.&lt;br&gt;- List events for resource: $filter&#x3D;eventTimestamp ge &#39;&lt;Start Time&gt;&#39; and eventTimestamp le &#39;&lt;End Time&gt;&#39; and eventChannels eq &#39;Admin, Operation&#39; and resourceUri eq &#39;&lt;ResourceURI&gt;&#39;.&lt;br&gt;- List events for a subscription: $filter&#x3D;eventTimestamp ge &#39;&lt;Start Time&gt;&#39; and eventTimestamp le &#39;&lt;End Time&gt;&#39; and eventChannels eq &#39;Admin, Operation&#39;.&lt;br&gt;- List events for a resource provider: $filter&#x3D;eventTimestamp ge &#39;&lt;Start Time&gt;&#39; and eventTimestamp le &#39;&lt;End Time&gt;&#39; and eventChannels eq &#39;Admin, Operation&#39; and resourceProvider eq &#39;&lt;ResourceProviderName&gt;&#39;.&lt;br&gt;- List events for a correlation Id: api-version&#x3D;2014-04-01&amp;$filter&#x3D;eventTimestamp ge &#39;2014-07-16T04:36:37.6407898Z&#39; and eventTimestamp le &#39;2014-07-20T04:36:37.6407898Z&#39; and eventChannels eq &#39;Admin, Operation&#39; and correlationId eq &#39;&lt;CorrelationID&gt;&#39;.&lt;br&gt;**NOTE**: No other syntax is allowed. | [optional] 
 **select** | **String**| Used to fetch events with only the given properties.&lt;br&gt;The **$select** argument is a comma separated list of property names to be returned. Possible values are: *authorization*, *claims*, *correlationId*, *description*, *eventDataId*, *eventName*, *eventTimestamp*, *httpRequest*, *level*, *operationId*, *operationName*, *properties*, *resourceGroupName*, *resourceProviderName*, *resourceId*, *status*, *submissionTimestamp*, *subStatus*, *subscriptionId* | [optional] 

### Return type

[**EventDataCollection**](EventDataCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

