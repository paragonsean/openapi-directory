# Pims.EventsApi

All URIs are relative to *https://demo.pims.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchAllEvents**](EventsApi.md#fetchAllEvents) | **GET** /events | Find all events
[**fetchAllSeriesEvents**](EventsApi.md#fetchAllSeriesEvents) | **GET** /series/{series_id}/events | Find all events for one series
[**fetchAllVenuesEvents**](EventsApi.md#fetchAllVenuesEvents) | **GET** /venues/{venue_id}/events | Find all events for one venue
[**fetchOneEvent**](EventsApi.md#fetchOneEvent) | **GET** /events/{event_id} | Get one event by ID



## fetchAllEvents

> [EventsEntity] fetchAllEvents(opts)

Find all events

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.EventsApi();
let opts = {
  'label': "label_example", // String | Find only the events whose label contains this value.
  'fromDatetime': new Date("2013-10-20"), // Date | Find only the events starting after this date.
  'toDatetime': new Date("2013-10-20"), // Date | Find only the events starting before this date.
  'city': "city_example", // String | Find only the events whose venue city (or metropolitan area) contains this value.
  'sort': "'label'", // String | Sort the events in the corresponding order.
  'pageSize': 25, // Number | Pagination size, i.e. maximum number of items to be displayed in the response.
  'acceptLanguage': "'en'" // String | Language used for the translatable labels.
};
apiInstance.fetchAllEvents(opts, (error, data, response) => {
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
 **label** | **String**| Find only the events whose label contains this value. | [optional] 
 **fromDatetime** | **Date**| Find only the events starting after this date. | [optional] 
 **toDatetime** | **Date**| Find only the events starting before this date. | [optional] 
 **city** | **String**| Find only the events whose venue city (or metropolitan area) contains this value. | [optional] 
 **sort** | **String**| Sort the events in the corresponding order. | [optional] [default to &#39;label&#39;]
 **pageSize** | **Number**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25]
 **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to &#39;en&#39;]

### Return type

[**[EventsEntity]**](EventsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json


## fetchAllSeriesEvents

> [EventsEntity] fetchAllSeriesEvents(seriesId, opts)

Find all events for one series

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.EventsApi();
let seriesId = 56; // Number | ID of the targeted series.
let opts = {
  'fromDatetime': new Date("2013-10-20"), // Date | Find only the events starting after this date.
  'toDatetime': new Date("2013-10-20"), // Date | Find only the events starting before this date.
  'city': "city_example", // String | Find only the events whose venue city (or metropolitan area) contains this value.
  'sort': "'label'", // String | Sort the events in the corresponding order.
  'pageSize': 25, // Number | Pagination size, i.e. maximum number of items to be displayed in the response.
  'acceptLanguage': "'en'" // String | Language used for the translatable labels.
};
apiInstance.fetchAllSeriesEvents(seriesId, opts, (error, data, response) => {
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
 **seriesId** | **Number**| ID of the targeted series. | 
 **fromDatetime** | **Date**| Find only the events starting after this date. | [optional] 
 **toDatetime** | **Date**| Find only the events starting before this date. | [optional] 
 **city** | **String**| Find only the events whose venue city (or metropolitan area) contains this value. | [optional] 
 **sort** | **String**| Sort the events in the corresponding order. | [optional] [default to &#39;label&#39;]
 **pageSize** | **Number**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25]
 **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to &#39;en&#39;]

### Return type

[**[EventsEntity]**](EventsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json


## fetchAllVenuesEvents

> [EventsEntity] fetchAllVenuesEvents(venueId, opts)

Find all events for one venue

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.EventsApi();
let venueId = 56; // Number | ID of the targeted venue.
let opts = {
  'fromDatetime': new Date("2013-10-20"), // Date | Find only the events starting after this date.
  'toDatetime': new Date("2013-10-20"), // Date | Find only the events starting before this date.
  'city': "city_example", // String | Find only the events whose venue city (or metropolitan area) contains this value.
  'sort': "'label'", // String | Sort the events in the corresponding order.
  'pageSize': 25, // Number | Pagination size, i.e. maximum number of items to be displayed in the response.
  'acceptLanguage': "'en'" // String | Language used for the translatable labels.
};
apiInstance.fetchAllVenuesEvents(venueId, opts, (error, data, response) => {
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
 **venueId** | **Number**| ID of the targeted venue. | 
 **fromDatetime** | **Date**| Find only the events starting after this date. | [optional] 
 **toDatetime** | **Date**| Find only the events starting before this date. | [optional] 
 **city** | **String**| Find only the events whose venue city (or metropolitan area) contains this value. | [optional] 
 **sort** | **String**| Sort the events in the corresponding order. | [optional] [default to &#39;label&#39;]
 **pageSize** | **Number**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25]
 **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to &#39;en&#39;]

### Return type

[**[EventsEntity]**](EventsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json


## fetchOneEvent

> EventsEntity fetchOneEvent(eventId, opts)

Get one event by ID

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.EventsApi();
let eventId = 56; // Number | ID of the targeted event.
let opts = {
  'acceptLanguage': "'en'" // String | Language used for the translatable labels.
};
apiInstance.fetchOneEvent(eventId, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to &#39;en&#39;]

### Return type

[**EventsEntity**](EventsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json

