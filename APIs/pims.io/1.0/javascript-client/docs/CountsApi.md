# Pims.CountsApi

All URIs are relative to *https://demo.pims.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchAllDetailedTicketCounts**](CountsApi.md#fetchAllDetailedTicketCounts) | **GET** /events/{event_id}/ticket-counts/detailed | Find all detailed ticket counts for one event
[**fetchAllTicketCounts**](CountsApi.md#fetchAllTicketCounts) | **GET** /events/{event_id}/ticket-counts | Find all ticket counts for one event
[**fetchOneDetailedTicketCount**](CountsApi.md#fetchOneDetailedTicketCount) | **GET** /events/{event_id}/ticket-counts/detailed/{ticket_count_id} | Get one detailed ticket count by ID
[**fetchOneTicketCount**](CountsApi.md#fetchOneTicketCount) | **GET** /events/{event_id}/ticket-counts/{ticket_count_id} | Get one ticket count by ID



## fetchAllDetailedTicketCounts

> [TicketCountsDetailedEntity] fetchAllDetailedTicketCounts(eventId, opts)

Find all detailed ticket counts for one event

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.CountsApi();
let eventId = 56; // Number | ID of the targeted event.
let opts = {
  'fromDate': new Date("2013-10-20"), // Date | Find only the ticket counts after this date.
  'toDate': new Date("2013-10-20"), // Date | Find only the ticket counts before this date.
  'showIgnored': false, // Boolean | If set to `false`, show only the [event-]categories/[event-]price ranges/[event]channels which are not ignored. If set to `true`, show everything.
  'showNotApproved': false, // Boolean | If set to `false`, show only the approved ticket counts. If set to `true`, show all the ticket counts.
  'sort': "'date'", // String | Sort the ticket counts in the corresponding order.
  'pageSize': 25 // Number | Pagination size, i.e. maximum number of items to be displayed in the response.
};
apiInstance.fetchAllDetailedTicketCounts(eventId, opts, (error, data, response) => {
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
 **fromDate** | **Date**| Find only the ticket counts after this date. | [optional] 
 **toDate** | **Date**| Find only the ticket counts before this date. | [optional] 
 **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the [event-]categories/[event-]price ranges/[event]channels which are not ignored. If set to &#x60;true&#x60;, show everything. | [optional] [default to false]
 **showNotApproved** | **Boolean**| If set to &#x60;false&#x60;, show only the approved ticket counts. If set to &#x60;true&#x60;, show all the ticket counts. | [optional] [default to false]
 **sort** | **String**| Sort the ticket counts in the corresponding order. | [optional] [default to &#39;date&#39;]
 **pageSize** | **Number**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25]

### Return type

[**[TicketCountsDetailedEntity]**](TicketCountsDetailedEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json


## fetchAllTicketCounts

> [TicketCountsEntity] fetchAllTicketCounts(eventId, opts)

Find all ticket counts for one event

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.CountsApi();
let eventId = 56; // Number | ID of the targeted event.
let opts = {
  'fromDate': new Date("2013-10-20"), // Date | Find only the ticket counts after this date.
  'toDate': new Date("2013-10-20"), // Date | Find only the ticket counts before this date.
  'showIgnored': false, // Boolean | If set to `false`, show only the [event-]categories/[event-]price ranges/[event]channels which are not ignored. If set to `true`, show everything.
  'showNotApproved': false, // Boolean | If set to `false`, show only the approved ticket counts. If set to `true`, show all the ticket counts.
  'sort': "'date'", // String | Sort the ticket counts in the corresponding order.
  'pageSize': 25 // Number | Pagination size, i.e. maximum number of items to be displayed in the response.
};
apiInstance.fetchAllTicketCounts(eventId, opts, (error, data, response) => {
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
 **fromDate** | **Date**| Find only the ticket counts after this date. | [optional] 
 **toDate** | **Date**| Find only the ticket counts before this date. | [optional] 
 **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the [event-]categories/[event-]price ranges/[event]channels which are not ignored. If set to &#x60;true&#x60;, show everything. | [optional] [default to false]
 **showNotApproved** | **Boolean**| If set to &#x60;false&#x60;, show only the approved ticket counts. If set to &#x60;true&#x60;, show all the ticket counts. | [optional] [default to false]
 **sort** | **String**| Sort the ticket counts in the corresponding order. | [optional] [default to &#39;date&#39;]
 **pageSize** | **Number**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25]

### Return type

[**[TicketCountsEntity]**](TicketCountsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json


## fetchOneDetailedTicketCount

> TicketCountsDetailedEntity fetchOneDetailedTicketCount(eventId, ticketCountId, opts)

Get one detailed ticket count by ID

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.CountsApi();
let eventId = 56; // Number | ID of the targeted event.
let ticketCountId = 56; // Number | ID of the targeted ticket count.
let opts = {
  'showIgnored': false // Boolean | If set to `false`, show only the [event-]categories/[event-]price ranges/[event]channels which are not ignored. If set to `true`, show everything.
};
apiInstance.fetchOneDetailedTicketCount(eventId, ticketCountId, opts, (error, data, response) => {
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
 **ticketCountId** | **Number**| ID of the targeted ticket count. | 
 **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the [event-]categories/[event-]price ranges/[event]channels which are not ignored. If set to &#x60;true&#x60;, show everything. | [optional] [default to false]

### Return type

[**TicketCountsDetailedEntity**](TicketCountsDetailedEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json


## fetchOneTicketCount

> TicketCountsEntity fetchOneTicketCount(eventId, ticketCountId, opts)

Get one ticket count by ID

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.CountsApi();
let eventId = 56; // Number | ID of the targeted event.
let ticketCountId = 56; // Number | ID of the targeted ticket count.
let opts = {
  'showIgnored': false // Boolean | If set to `false`, show only the [event-]categories/[event-]price ranges/[event]channels which are not ignored. If set to `true`, show everything.
};
apiInstance.fetchOneTicketCount(eventId, ticketCountId, opts, (error, data, response) => {
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
 **ticketCountId** | **Number**| ID of the targeted ticket count. | 
 **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the [event-]categories/[event-]price ranges/[event]channels which are not ignored. If set to &#x60;true&#x60;, show everything. | [optional] [default to false]

### Return type

[**TicketCountsEntity**](TicketCountsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json

