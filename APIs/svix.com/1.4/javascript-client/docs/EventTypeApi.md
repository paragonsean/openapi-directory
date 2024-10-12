# SvixApi.EventTypeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createEventTypeApiV1EventTypePost**](EventTypeApi.md#createEventTypeApiV1EventTypePost) | **POST** /api/v1/event-type/ | Create Event Type
[**deleteEventTypeApiV1EventTypeEventTypeNameDelete**](EventTypeApi.md#deleteEventTypeApiV1EventTypeEventTypeNameDelete) | **DELETE** /api/v1/event-type/{event_type_name}/ | Archive Event Type
[**getEventTypeApiV1EventTypeEventTypeNameGet**](EventTypeApi.md#getEventTypeApiV1EventTypeEventTypeNameGet) | **GET** /api/v1/event-type/{event_type_name}/ | Get Event Type
[**listEventTypesApiV1EventTypeGet**](EventTypeApi.md#listEventTypesApiV1EventTypeGet) | **GET** /api/v1/event-type/ | List Event Types
[**updateEventTypeApiV1EventTypeEventTypeNamePut**](EventTypeApi.md#updateEventTypeApiV1EventTypeEventTypeNamePut) | **PUT** /api/v1/event-type/{event_type_name}/ | Update Event Type



## createEventTypeApiV1EventTypePost

> EventTypeOut createEventTypeApiV1EventTypePost(eventTypeIn, opts)

Create Event Type

Create new or unarchive existing event type.  Unarchiving an event type will allow endpoints to filter on it and messages to be sent with it. Endpoints filtering on the event type before archival will continue to filter on it. This operation does not preserve the description and schemas.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EventTypeApi();
let eventTypeIn = new SvixApi.EventTypeIn(); // EventTypeIn | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.createEventTypeApiV1EventTypePost(eventTypeIn, opts, (error, data, response) => {
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
 **eventTypeIn** | [**EventTypeIn**](EventTypeIn.md)|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**EventTypeOut**](EventTypeOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteEventTypeApiV1EventTypeEventTypeNameDelete

> deleteEventTypeApiV1EventTypeEventTypeNameDelete(eventTypeName, opts)

Archive Event Type

Archive an event type.  Endpoints already configured to filter on an event type will continue to do so after archival. However, new messages can not be sent with it and endpoints can not filter on it. An event type can be unarchived with the [create operation](#operation/create_event_type_api_v1_event_type__post).  If &#x60;expunge&#x3D;true&#x60; is set then the event type is deleted instead of archived. This can only be used in development environments.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EventTypeApi();
let eventTypeName = "user.signup"; // String | 
let opts = {
  'expunge': false, // Boolean | 
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.deleteEventTypeApiV1EventTypeEventTypeNameDelete(eventTypeName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eventTypeName** | **String**|  | 
 **expunge** | **Boolean**|  | [optional] [default to false]
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

null (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventTypeApiV1EventTypeEventTypeNameGet

> EventTypeOut getEventTypeApiV1EventTypeEventTypeNameGet(eventTypeName, opts)

Get Event Type

Get an event type.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EventTypeApi();
let eventTypeName = "user.signup"; // String | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.getEventTypeApiV1EventTypeEventTypeNameGet(eventTypeName, opts, (error, data, response) => {
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
 **eventTypeName** | **String**|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**EventTypeOut**](EventTypeOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEventTypesApiV1EventTypeGet

> ListResponseEventTypeOut listEventTypesApiV1EventTypeGet(opts)

List Event Types

Return the list of event types.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EventTypeApi();
let opts = {
  'iterator': "user.signup", // String | 
  'limit': 50, // Number | 
  'withContent': false, // Boolean | 
  'includeArchived': false, // Boolean | 
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.listEventTypesApiV1EventTypeGet(opts, (error, data, response) => {
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
 **iterator** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]
 **withContent** | **Boolean**|  | [optional] [default to false]
 **includeArchived** | **Boolean**|  | [optional] [default to false]
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**ListResponseEventTypeOut**](ListResponseEventTypeOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateEventTypeApiV1EventTypeEventTypeNamePut

> EventTypeOut updateEventTypeApiV1EventTypeEventTypeNamePut(eventTypeName, eventTypeUpdate, opts)

Update Event Type

Update an event type.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EventTypeApi();
let eventTypeName = "user.signup"; // String | 
let eventTypeUpdate = new SvixApi.EventTypeUpdate(); // EventTypeUpdate | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.updateEventTypeApiV1EventTypeEventTypeNamePut(eventTypeName, eventTypeUpdate, opts, (error, data, response) => {
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
 **eventTypeName** | **String**|  | 
 **eventTypeUpdate** | [**EventTypeUpdate**](EventTypeUpdate.md)|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**EventTypeOut**](EventTypeOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

