# BillbeeApi.EventsApi

All URIs are relative to *https://app.billbee.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eventApiGetList**](EventsApi.md#eventApiGetList) | **GET** /api/v1/events | Get a list of all events optionally filtered by date. This request is extra throttled to 2 calls per page per hour.



## eventApiGetList

> Object eventApiGetList(opts)

Get a list of all events optionally filtered by date. This request is extra throttled to 2 calls per page per hour.

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.EventsApi();
let opts = {
  'minDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Specifies the oldest date to include in the response
  'maxDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Specifies the newest date to include in the response
  'page': 56, // Number | Specifies the page to request
  'pageSize': 56, // Number | Specifies the pagesize. Defaults to 50, max value is 250
  'typeId': [null], // [Number] | Filter for specific event types
  'orderId': 789 // Number | Filter for specific order id
};
apiInstance.eventApiGetList(opts, (error, data, response) => {
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
 **minDate** | **Date**| Specifies the oldest date to include in the response | [optional] 
 **maxDate** | **Date**| Specifies the newest date to include in the response | [optional] 
 **page** | **Number**| Specifies the page to request | [optional] 
 **pageSize** | **Number**| Specifies the pagesize. Defaults to 50, max value is 250 | [optional] 
 **typeId** | [**[Number]**](Number.md)| Filter for specific event types | [optional] 
 **orderId** | **Number**| Filter for specific order id | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

