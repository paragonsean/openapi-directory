# CommerceManagementClient.CommerceApi

All URIs are relative to *https://management.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriberUsageAggregatesList**](CommerceApi.md#subscriberUsageAggregatesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Commerce/subscriberUsageAggregates | 



## subscriberUsageAggregatesList

> UsageAggregatePage subscriberUsageAggregatesList(subscriptionId, apiVersion, reportedStartTime, reportedEndTime, opts)



Gets a collection of SubscriberUsageAggregates, which are UsageAggregates from direct tenants.

### Example

```javascript
import CommerceManagementClient from 'commerce_management_client';
let defaultClient = CommerceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CommerceManagementClient.CommerceApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let apiVersion = "'2015-06-01-preview'"; // String | Client Api Version.
let reportedStartTime = new Date("2013-10-20T19:20:30+01:00"); // Date | The reported start time (inclusive).
let reportedEndTime = new Date("2013-10-20T19:20:30+01:00"); // Date | The reported end time (exclusive).
let opts = {
  'aggregationGranularity': "aggregationGranularity_example", // String | The aggregation granularity.
  'subscriberId': "subscriberId_example", // String | The tenant subscription identifier.
  'continuationToken': "continuationToken_example" // String | The continuation token.
};
apiInstance.subscriberUsageAggregatesList(subscriptionId, apiVersion, reportedStartTime, reportedEndTime, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-06-01-preview&#39;]
 **reportedStartTime** | **Date**| The reported start time (inclusive). | 
 **reportedEndTime** | **Date**| The reported end time (exclusive). | 
 **aggregationGranularity** | **String**| The aggregation granularity. | [optional] 
 **subscriberId** | **String**| The tenant subscription identifier. | [optional] 
 **continuationToken** | **String**| The continuation token. | [optional] 

### Return type

[**UsageAggregatePage**](UsageAggregatePage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

