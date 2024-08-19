# NeoWsNearEarthObjectWebService.FeedApi

All URIs are relative to *http://www.neowsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieveNEOFeedToday**](FeedApi.md#retrieveNEOFeedToday) | **GET** /rest/v1/feed/today | Find Near Earth Objects for today
[**retrieveNearEarthObjectFeed**](FeedApi.md#retrieveNearEarthObjectFeed) | **GET** /rest/v1/feed | Find Near Earth Objects by date



## retrieveNEOFeedToday

> NearEarthObjectList retrieveNEOFeedToday(opts)

Find Near Earth Objects for today

Get a list of Near Earth Objects for today

### Example

```javascript
import NeoWsNearEarthObjectWebService from 'neo_ws__near_earth_object_web_service';

let apiInstance = new NeoWsNearEarthObjectWebService.FeedApi();
let opts = {
  'detailed': true // Boolean | detailed
};
apiInstance.retrieveNEOFeedToday(opts, (error, data, response) => {
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
 **detailed** | **Boolean**| detailed | [optional] 

### Return type

[**NearEarthObjectList**](NearEarthObjectList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveNearEarthObjectFeed

> NearEarthObjectList retrieveNearEarthObjectFeed(opts)

Find Near Earth Objects by date

Get a list of Near Earth Objects within a date range, The max range in one query is 7 days

### Example

```javascript
import NeoWsNearEarthObjectWebService from 'neo_ws__near_earth_object_web_service';

let apiInstance = new NeoWsNearEarthObjectWebService.FeedApi();
let opts = {
  'startDate': "startDate_example", // String | Start of date range search, format: yyyy-MM-dd - (ex: 2015-04-28)
  'endDate': "endDate_example", // String | End of date range search, format: yyyy-MM-dd - (ex: 2015-04-28). If left off search will extends 7 days from start_date
  'detailed': true // Boolean | detailed
};
apiInstance.retrieveNearEarthObjectFeed(opts, (error, data, response) => {
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
 **startDate** | **String**| Start of date range search, format: yyyy-MM-dd - (ex: 2015-04-28) | [optional] 
 **endDate** | **String**| End of date range search, format: yyyy-MM-dd - (ex: 2015-04-28). If left off search will extends 7 days from start_date | [optional] 
 **detailed** | **Boolean**| detailed | [optional] 

### Return type

[**NearEarthObjectList**](NearEarthObjectList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

