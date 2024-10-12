# TwilioInsights.InsightsV1MetricApi

All URIs are relative to *https://insights.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listMetric**](InsightsV1MetricApi.md#listMetric) | **GET** /v1/Voice/{CallSid}/Metrics | 



## listMetric

> ListMetricResponse listMetric(callSid, opts)



Get a list of Call Metrics for a Call.

### Example

```javascript
import TwilioInsights from 'twilio_insights';
let defaultClient = TwilioInsights.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioInsights.InsightsV1MetricApi();
let callSid = "callSid_example"; // String | The unique SID identifier of the Call.
let opts = {
  'edge': "edge_example", // MetricEnumTwilioEdge | The Edge of this Metric. One of `unknown_edge`, `carrier_edge`, `sip_edge`, `sdk_edge` or `client_edge`.
  'direction': "direction_example", // MetricEnumStreamDirection | The Direction of this Metric. One of `unknown`, `inbound`, `outbound` or `both`.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listMetric(callSid, opts, (error, data, response) => {
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
 **callSid** | **String**| The unique SID identifier of the Call. | 
 **edge** | **MetricEnumTwilioEdge**| The Edge of this Metric. One of &#x60;unknown_edge&#x60;, &#x60;carrier_edge&#x60;, &#x60;sip_edge&#x60;, &#x60;sdk_edge&#x60; or &#x60;client_edge&#x60;. | [optional] 
 **direction** | **MetricEnumStreamDirection**| The Direction of this Metric. One of &#x60;unknown&#x60;, &#x60;inbound&#x60;, &#x60;outbound&#x60; or &#x60;both&#x60;. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListMetricResponse**](ListMetricResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

