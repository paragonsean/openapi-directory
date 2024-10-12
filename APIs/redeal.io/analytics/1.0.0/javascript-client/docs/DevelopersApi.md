# RedealAnalyticsApi.DevelopersApi

All URIs are relative to *https://analytics.redeal.io/api/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEvents**](DevelopersApi.md#getEvents) | **GET** /events | get events for analytics



## getEvents

> [EventRecord] getEvents(opts)

get events for analytics

By passing in the company, site or deal Id a set of user interaction event records is returned. For pagination of a large result set use queryexecutionid and nexttoken instead. 

### Example

```javascript
import RedealAnalyticsApi from 'redeal_analytics_api';

let apiInstance = new RedealAnalyticsApi.DevelopersApi();
let opts = {
  'company': "company_example", // String | pass an optional company Id
  'site': "site_example", // String | pass an optional site Id
  'deal': "deal_example", // String | pass an optional deal Id
  'type': "type_example", // String | type of records to return
  'nexttoken': "nexttoken_example", // String | next token to start returning records from
  'queryexecutionid': "queryexecutionid_example" // String | id of execution to get more records based on next token
};
apiInstance.getEvents(opts, (error, data, response) => {
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
 **company** | **String**| pass an optional company Id | [optional] 
 **site** | **String**| pass an optional site Id | [optional] 
 **deal** | **String**| pass an optional deal Id | [optional] 
 **type** | **String**| type of records to return | [optional] 
 **nexttoken** | **String**| next token to start returning records from | [optional] 
 **queryexecutionid** | **String**| id of execution to get more records based on next token | [optional] 

### Return type

[**[EventRecord]**](EventRecord.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

