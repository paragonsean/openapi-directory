# FilesComApi.ExternalEventsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getExternalEvents**](ExternalEventsApi.md#getExternalEvents) | **GET** /external_events | List External Events
[**getExternalEventsId**](ExternalEventsApi.md#getExternalEventsId) | **GET** /external_events/{id} | Show External Event
[**postExternalEvents**](ExternalEventsApi.md#postExternalEvents) | **POST** /external_events | Create External Event



## getExternalEvents

> [ExternalEventEntity] getExternalEvents(opts)

List External Events

List External Events

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ExternalEventsApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[remote_server_type]=desc`). Valid fields are `remote_server_type`, `site_id`, `folder_behavior_id`, `event_type`, `created_at` or `status`.
  'filter': {key: null}, // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `created_at`, `event_type`, `remote_server_type`, `status` or `folder_behavior_id`. Valid field combinations are `[ event_type, status, created_at ]`, `[ event_type, created_at ]` or `[ status, created_at ]`.
  'filterGt': {key: null}, // Object | If set, return records where the specified field is greater than the supplied value. Valid fields are `created_at`.
  'filterGteq': {key: null}, // Object | If set, return records where the specified field is greater than or equal the supplied value. Valid fields are `created_at`.
  'filterPrefix': {key: null}, // Object | If set, return records where the specified field is prefixed by the supplied value. Valid fields are `remote_server_type`.
  'filterLt': {key: null}, // Object | If set, return records where the specified field is less than the supplied value. Valid fields are `created_at`.
  'filterLteq': {key: null} // Object | If set, return records where the specified field is less than or equal the supplied value. Valid fields are `created_at`.
};
apiInstance.getExternalEvents(opts, (error, data, response) => {
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
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[remote_server_type]&#x3D;desc&#x60;). Valid fields are &#x60;remote_server_type&#x60;, &#x60;site_id&#x60;, &#x60;folder_behavior_id&#x60;, &#x60;event_type&#x60;, &#x60;created_at&#x60; or &#x60;status&#x60;. | [optional] 
 **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;created_at&#x60;, &#x60;event_type&#x60;, &#x60;remote_server_type&#x60;, &#x60;status&#x60; or &#x60;folder_behavior_id&#x60;. Valid field combinations are &#x60;[ event_type, status, created_at ]&#x60;, &#x60;[ event_type, created_at ]&#x60; or &#x60;[ status, created_at ]&#x60;. | [optional] 
 **filterGt** | [**Object**](.md)| If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;created_at&#x60;. | [optional] 
 **filterGteq** | [**Object**](.md)| If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;created_at&#x60;. | [optional] 
 **filterPrefix** | [**Object**](.md)| If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;remote_server_type&#x60;. | [optional] 
 **filterLt** | [**Object**](.md)| If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;created_at&#x60;. | [optional] 
 **filterLteq** | [**Object**](.md)| If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;created_at&#x60;. | [optional] 

### Return type

[**[ExternalEventEntity]**](ExternalEventEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getExternalEventsId

> ExternalEventEntity getExternalEventsId(id)

Show External Event

Show External Event

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ExternalEventsApi();
let id = 56; // Number | External Event ID.
apiInstance.getExternalEventsId(id, (error, data, response) => {
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
 **id** | **Number**| External Event ID. | 

### Return type

[**ExternalEventEntity**](ExternalEventEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postExternalEvents

> ExternalEventEntity postExternalEvents(body, status)

Create External Event

Create External Event

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ExternalEventsApi();
let body = "body_example"; // String | Event body
let status = "status_example"; // String | Status of event.
apiInstance.postExternalEvents(body, status, (error, data, response) => {
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
 **body** | **String**| Event body | 
 **status** | **String**| Status of event. | 

### Return type

[**ExternalEventEntity**](ExternalEventEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

