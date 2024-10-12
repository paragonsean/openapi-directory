# Pims.CapacitiesApi

All URIs are relative to *https://demo.pims.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchAllEventsCapacities**](CapacitiesApi.md#fetchAllEventsCapacities) | **GET** /events/{event_id}/capacities | Find all capacities for one event
[**fetchOneEventCapacity**](CapacitiesApi.md#fetchOneEventCapacity) | **GET** /events/{event_id}/capacities/{capacity_id} | Get one capacity by ID



## fetchAllEventsCapacities

> [EventsCapacitiesEntity] fetchAllEventsCapacities(eventId, opts)

Find all capacities for one event

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.CapacitiesApi();
let eventId = 56; // Number | ID of the targeted event.
let opts = {
  'showIgnored': false, // Boolean | If set to `false`, show only the [event-]categories which are not ignored. If set to `true`, show everything.
  'sort': "'date'", // String | Sort the capacities in the corresponding order.
  'pageSize': 25 // Number | Pagination size, i.e. maximum number of items to be displayed in the response.
};
apiInstance.fetchAllEventsCapacities(eventId, opts, (error, data, response) => {
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
 **eventId** | **Number**| ID of the targeted event. | 
 **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the [event-]categories which are not ignored. If set to &#x60;true&#x60;, show everything. | [optional] [default to false]
 **sort** | **String**| Sort the capacities in the corresponding order. | [optional] [default to &#39;date&#39;]
 **pageSize** | **Number**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25]

### Return type

[**[EventsCapacitiesEntity]**](EventsCapacitiesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json


## fetchOneEventCapacity

> EventsCapacitiesEntity fetchOneEventCapacity(eventId, capacityId, opts)

Get one capacity by ID

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.CapacitiesApi();
let eventId = 56; // Number | ID of the targeted event.
let capacityId = 56; // Number | ID of the targeted capacity.
let opts = {
  'showIgnored': false // Boolean | If set to `false`, show only the [event-]categories which are not ignored. If set to `true`, show everything.
};
apiInstance.fetchOneEventCapacity(eventId, capacityId, opts, (error, data, response) => {
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
 **eventId** | **Number**| ID of the targeted event. | 
 **capacityId** | **Number**| ID of the targeted capacity. | 
 **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the [event-]categories which are not ignored. If set to &#x60;true&#x60;, show everything. | [optional] [default to false]

### Return type

[**EventsCapacitiesEntity**](EventsCapacitiesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json

