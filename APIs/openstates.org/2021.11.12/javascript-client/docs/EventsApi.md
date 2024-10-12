# OpenStatesApiV3.EventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eventDetailEventsEventIdGet**](EventsApi.md#eventDetailEventsEventIdGet) | **GET** /events/{event_id} | Event Detail
[**eventListEventsGet**](EventsApi.md#eventListEventsGet) | **GET** /events | Event List



## eventDetailEventsEventIdGet

> Event eventDetailEventsEventIdGet(eventId, opts)

Event Detail

Get details on a single event by ID.

### Example

```javascript
import OpenStatesApiV3 from 'open_states_api_v3';

let apiInstance = new OpenStatesApiV3.EventsApi();
let eventId = "eventId_example"; // String | 
let opts = {
  'include': [new OpenStatesApiV3.EventInclude()], // [EventInclude] | Additional includes for the Event response.
  'apikey': "apikey_example", // String | 
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.eventDetailEventsEventIdGet(eventId, opts, (error, data, response) => {
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
 **eventId** | **String**|  | 
 **include** | [**[EventInclude]**](EventInclude.md)| Additional includes for the Event response. | [optional] 
 **apikey** | **String**|  | [optional] 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**Event**](Event.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventListEventsGet

> EventList eventListEventsGet(opts)

Event List

### Example

```javascript
import OpenStatesApiV3 from 'open_states_api_v3';

let apiInstance = new OpenStatesApiV3.EventsApi();
let opts = {
  'jurisdiction': "jurisdiction_example", // String | Filter by jurisdiction name or ID.
  'deleted': false, // Boolean | Return events marked as deleted?
  'before': "before_example", // String | Limit results to those starting before a given datetime.
  'after': "after_example", // String | Limit results to those starting before a given datetime.
  'requireBills': false, // Boolean | Limit results to events with associated bills.
  'include': [new OpenStatesApiV3.EventInclude()], // [EventInclude] | Additional includes for the Event response.
  'apikey': "apikey_example", // String | 
  'page': 1, // Number | 
  'perPage': 20, // Number | 
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.eventListEventsGet(opts, (error, data, response) => {
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
 **jurisdiction** | **String**| Filter by jurisdiction name or ID. | [optional] 
 **deleted** | **Boolean**| Return events marked as deleted? | [optional] [default to false]
 **before** | **String**| Limit results to those starting before a given datetime. | [optional] 
 **after** | **String**| Limit results to those starting before a given datetime. | [optional] 
 **requireBills** | **Boolean**| Limit results to events with associated bills. | [optional] [default to false]
 **include** | [**[EventInclude]**](EventInclude.md)| Additional includes for the Event response. | [optional] 
 **apikey** | **String**|  | [optional] 
 **page** | **Number**|  | [optional] [default to 1]
 **perPage** | **Number**|  | [optional] [default to 20]
 **xApiKey** | **String**|  | [optional] 

### Return type

[**EventList**](EventList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

