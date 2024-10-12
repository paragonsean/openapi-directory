# TvApi.ScheduleApi

All URIs are relative to *https://tv.api.pressassociation.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listSchedule**](ScheduleApi.md#listSchedule) | **GET** /schedule | Schedule Collection



## listSchedule

> Object listSchedule(channelId, start, opts)

Schedule Collection

The schedule endpoint produces a linear TV schedule for a given channel and date range.   - The date range supplied must be no larger than 21 days.  - If no end data is passed the API will default to start date + 24 hours.

### Example

```javascript
import TvApi from 'tv_api';
let defaultClient = TvApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TvApi.ScheduleApi();
let channelId = "channelId_example"; // String | The identifier for the selected channel.
let start = "'2015-05-05T00:00:00'"; // String | The Start Date for the schedule.
let opts = {
  'end': "'2015-05-06T00:00:00'", // String | The End Date for the schedule.
  'aliases': true // Boolean | Flag to display Legacy and Provider Ids.
};
apiInstance.listSchedule(channelId, start, opts, (error, data, response) => {
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
 **channelId** | **String**| The identifier for the selected channel. | 
 **start** | **String**| The Start Date for the schedule. | [default to &#39;2015-05-05T00:00:00&#39;]
 **end** | **String**| The End Date for the schedule. | [optional] [default to &#39;2015-05-06T00:00:00&#39;]
 **aliases** | **Boolean**| Flag to display Legacy and Provider Ids. | [optional] [default to true]

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

