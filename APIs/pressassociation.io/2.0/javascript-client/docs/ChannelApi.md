# TvApi.ChannelApi

All URIs are relative to *https://tv.api.pressassociation.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getChannel**](ChannelApi.md#getChannel) | **GET** /channel/{channelId} | Channel Detail
[**listChannels**](ChannelApi.md#listChannels) | **GET** /channel | Channel Collection



## getChannel

> Object getChannel(channelId, opts)

Channel Detail

Return the content of the selected channel.

### Example

```javascript
import TvApi from 'tv_api';
let defaultClient = TvApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TvApi.ChannelApi();
let channelId = "channelId_example"; // String | The identifier for the selected channel.
let opts = {
  'aliases': true // Boolean | Flag to display Legacy and Provider Ids.
};
apiInstance.getChannel(channelId, opts, (error, data, response) => {
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
 **aliases** | **Boolean**| Flag to display Legacy and Provider Ids. | [optional] [default to true]

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannels

> Object listChannels(opts)

Channel Collection

If you are interested in a list of channels that have had there schedule updated you can filter by the following query params.  - scheduleStart  - scheduleEnd  - scheduleUpdatedSince  adding these query params will filter the channel collection to only return channels that have been updated within the given range, updatedSince stores the state of your previous call.  Example Usage: Every 10 minutes get me the channels that have updated schedules for the next 2 weeks.  /channel?platform&#x3D;{uuid}&amp;scheduleStart&#x3D;{today}&amp;scheduleEnd&#x3D;{today + 2 weeks}&amp;updatedSince&#x3D;{10 minutes ago}  Also please note epg numbers are only exposed when a platform and region are passed to the query.

### Example

```javascript
import TvApi from 'tv_api';
let defaultClient = TvApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TvApi.ChannelApi();
let opts = {
  'platformId': "'d3b26caa-8c7d-5f97-9eff-40fcf1a6f8d3'", // String | The identifier for the selected platform. Multiple platforms can be passed to the API without a region Id. Passing multiple platforms without a region will not return epg numbers as these are linked to a platform and region.
  'regionId': "'afa4f624-da9b-54ce-b514-570345dbbdce'", // String | The platform region ID for the channel selection.
  'aliases': true, // Boolean | Flag to display Legacy and Provider Ids.
  'date': "'2018-09-15'", // String | Date of the Channel State to select, this will display channel names and attributes in the future or past.
  'scheduleStart': "'2015-05-05T00:00:00'", // String | The Start Date for the schedule.
  'scheduleEnd': "'2015-05-06T00:00:00'", // String | The End Date for the schedule.
  'scheduleUpdatedSince': "'2015-05-05T00:00:00'" // String | Schedule Updated Since
};
apiInstance.listChannels(opts, (error, data, response) => {
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
 **platformId** | **String**| The identifier for the selected platform. Multiple platforms can be passed to the API without a region Id. Passing multiple platforms without a region will not return epg numbers as these are linked to a platform and region. | [optional] [default to &#39;d3b26caa-8c7d-5f97-9eff-40fcf1a6f8d3&#39;]
 **regionId** | **String**| The platform region ID for the channel selection. | [optional] [default to &#39;afa4f624-da9b-54ce-b514-570345dbbdce&#39;]
 **aliases** | **Boolean**| Flag to display Legacy and Provider Ids. | [optional] [default to true]
 **date** | **String**| Date of the Channel State to select, this will display channel names and attributes in the future or past. | [optional] [default to &#39;2018-09-15&#39;]
 **scheduleStart** | **String**| The Start Date for the schedule. | [optional] [default to &#39;2015-05-05T00:00:00&#39;]
 **scheduleEnd** | **String**| The End Date for the schedule. | [optional] [default to &#39;2015-05-06T00:00:00&#39;]
 **scheduleUpdatedSince** | **String**| Schedule Updated Since | [optional] [default to &#39;2015-05-05T00:00:00&#39;]

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

