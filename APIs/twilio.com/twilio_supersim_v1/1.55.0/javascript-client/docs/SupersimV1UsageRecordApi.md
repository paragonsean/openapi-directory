# TwilioSupersim.SupersimV1UsageRecordApi

All URIs are relative to *https://supersim.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listUsageRecord**](SupersimV1UsageRecordApi.md#listUsageRecord) | **GET** /v1/UsageRecords | 



## listUsageRecord

> ListUsageRecordResponse listUsageRecord(opts)



List UsageRecords

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1UsageRecordApi();
let opts = {
  'sim': "sim_example", // String | SID or unique name of a Sim resource. Only show UsageRecords representing usage incurred by this Super SIM.
  'fleet': "fleet_example", // String | SID or unique name of a Fleet resource. Only show UsageRecords representing usage for Super SIMs belonging to this Fleet resource at the time the usage occurred.
  'network': "network_example", // String | SID of a Network resource. Only show UsageRecords representing usage on this network.
  'isoCountry': "isoCountry_example", // String | Alpha-2 ISO Country Code. Only show UsageRecords representing usage in this country.
  'group': "group_example", // UsageRecordEnumGroup | Dimension over which to aggregate usage records. Can be: `sim`, `fleet`, `network`, `isoCountry`. Default is to not aggregate across any of these dimensions, UsageRecords will be aggregated into the time buckets described by the `Granularity` parameter.
  'granularity': "granularity_example", // UsageRecordEnumGranularity | Time-based grouping that UsageRecords should be aggregated by. Can be: `hour`, `day`, or `all`. Default is `all`. `all` returns one UsageRecord that describes the usage for the entire period.
  'startTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Only include usage that occurred at or after this time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is one month before the `end_time`.
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Only include usage that occurred before this time (exclusive), specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is the current time.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listUsageRecord(opts, (error, data, response) => {
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
 **sim** | **String**| SID or unique name of a Sim resource. Only show UsageRecords representing usage incurred by this Super SIM. | [optional] 
 **fleet** | **String**| SID or unique name of a Fleet resource. Only show UsageRecords representing usage for Super SIMs belonging to this Fleet resource at the time the usage occurred. | [optional] 
 **network** | **String**| SID of a Network resource. Only show UsageRecords representing usage on this network. | [optional] 
 **isoCountry** | **String**| Alpha-2 ISO Country Code. Only show UsageRecords representing usage in this country. | [optional] 
 **group** | **UsageRecordEnumGroup**| Dimension over which to aggregate usage records. Can be: &#x60;sim&#x60;, &#x60;fleet&#x60;, &#x60;network&#x60;, &#x60;isoCountry&#x60;. Default is to not aggregate across any of these dimensions, UsageRecords will be aggregated into the time buckets described by the &#x60;Granularity&#x60; parameter. | [optional] 
 **granularity** | **UsageRecordEnumGranularity**| Time-based grouping that UsageRecords should be aggregated by. Can be: &#x60;hour&#x60;, &#x60;day&#x60;, or &#x60;all&#x60;. Default is &#x60;all&#x60;. &#x60;all&#x60; returns one UsageRecord that describes the usage for the entire period. | [optional] 
 **startTime** | **Date**| Only include usage that occurred at or after this time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is one month before the &#x60;end_time&#x60;. | [optional] 
 **endTime** | **Date**| Only include usage that occurred before this time (exclusive), specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is the current time. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListUsageRecordResponse**](ListUsageRecordResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

