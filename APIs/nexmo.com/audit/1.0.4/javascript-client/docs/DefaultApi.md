# AuditApi.DefaultApi

All URIs are relative to *https://api.nexmo.com/beta/audit*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEvent**](DefaultApi.md#getEvent) | **GET** /events/{id} | Retrieve individual audit event
[**getEvents**](DefaultApi.md#getEvents) | **GET** /events | Retrieve audit events
[**getEventsOptions**](DefaultApi.md#getEventsOptions) | **OPTIONS** /events | Retrieve audit event types



## getEvent

> AuditEvent getEvent(id)

Retrieve individual audit event

Get the specified audit event. 

### Example

```javascript
import AuditApi from 'audit_api';
let defaultClient = AuditApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new AuditApi.DefaultApi();
let id = "aaaaaaaa-bbbb-cccc-dddd-0123456789ab"; // String | The UUID of the audit event to retrieve
apiInstance.getEvent(id, (error, data, response) => {
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
 **id** | **String**| The UUID of the audit event to retrieve | 

### Return type

[**AuditEvent**](AuditEvent.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEvents

> AuditResp getEvents(opts)

Retrieve audit events

Get a series of audit events describing changes made to your Vonage API account over time. 

### Example

```javascript
import AuditApi from 'audit_api';
let defaultClient = AuditApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new AuditApi.DefaultApi();
let opts = {
  'eventType': new AuditApi.EventTypes(), // EventTypes | Filter results by this event type.
  'dateFrom': "dateFrom_example", // String | Start of time range for audit events. DateTime in ISO-8601 format.
  'dateTo': "dateTo_example", // String | End of time range for audit events. DateTime in ISO-8601 format.
  'searchText': "searchText_example", // String | Return only audit events where the JSON object contains this search text. Must be legal text for a JSON attribute value, that is quotes and braces must be escaped.
  'page': "page_example", // String | Page number starting with page 1.
  'size': 30 // Number | Number of elements per page.
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
 **eventType** | [**EventTypes**](.md)| Filter results by this event type. | [optional] 
 **dateFrom** | **String**| Start of time range for audit events. DateTime in ISO-8601 format. | [optional] 
 **dateTo** | **String**| End of time range for audit events. DateTime in ISO-8601 format. | [optional] 
 **searchText** | **String**| Return only audit events where the JSON object contains this search text. Must be legal text for a JSON attribute value, that is quotes and braces must be escaped. | [optional] 
 **page** | **String**| Page number starting with page 1. | [optional] 
 **size** | **Number**| Number of elements per page. | [optional] [default to 30]

### Return type

[**AuditResp**](AuditResp.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventsOptions

> AuditEventTypesResp getEventsOptions()

Retrieve audit event types

Get audit event types. 

### Example

```javascript
import AuditApi from 'audit_api';
let defaultClient = AuditApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new AuditApi.DefaultApi();
apiInstance.getEventsOptions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**AuditEventTypesResp**](AuditEventTypesResp.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

