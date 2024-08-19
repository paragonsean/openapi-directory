# BandsintownApi.ArtistEventsApi

All URIs are relative to *https://rest.bandsintown.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artistEvents**](ArtistEventsApi.md#artistEvents) | **GET** /artists/{artistname}/events | Get upcoming, past, or all artist events, or events within a date range



## artistEvents

> [EventData] artistEvents(artistname, appId, opts)

Get upcoming, past, or all artist events, or events within a date range

artist events 

### Example

```javascript
import BandsintownApi from 'bandsintown_api';

let apiInstance = new BandsintownApi.ArtistEventsApi();
let artistname = "artistname_example"; // String | The name of the artist. If it contains one of the special characters below, please be sure to replace it by the corresponding code: for / use %252F, for ? use %253F, for * use %252A, and for \" use %27C
let appId = "appId_example"; // String | The application ID assigned to you by Bandsintown
let opts = {
  'date': "date_example" // String | Can be one of the following values: \"upcoming\", \"past\", \"all\", or a date range e.g. \"2015-05-05,2017-05-05\". If not specified, only upcoming shows are returned
};
apiInstance.artistEvents(artistname, appId, opts, (error, data, response) => {
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
 **artistname** | **String**| The name of the artist. If it contains one of the special characters below, please be sure to replace it by the corresponding code: for / use %252F, for ? use %253F, for * use %252A, and for \&quot; use %27C | 
 **appId** | **String**| The application ID assigned to you by Bandsintown | 
 **date** | **String**| Can be one of the following values: \&quot;upcoming\&quot;, \&quot;past\&quot;, \&quot;all\&quot;, or a date range e.g. \&quot;2015-05-05,2017-05-05\&quot;. If not specified, only upcoming shows are returned | [optional] 

### Return type

[**[EventData]**](EventData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

