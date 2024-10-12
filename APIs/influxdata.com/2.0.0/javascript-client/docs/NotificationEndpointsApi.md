# InfluxOssApiService.NotificationEndpointsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNotificationEndpoint**](NotificationEndpointsApi.md#createNotificationEndpoint) | **POST** /notificationEndpoints | Add a notification endpoint
[**deleteNotificationEndpointsID**](NotificationEndpointsApi.md#deleteNotificationEndpointsID) | **DELETE** /notificationEndpoints/{endpointID} | Delete a notification endpoint
[**deleteNotificationEndpointsIDLabelsID**](NotificationEndpointsApi.md#deleteNotificationEndpointsIDLabelsID) | **DELETE** /notificationEndpoints/{endpointID}/labels/{labelID} | Delete a label from a notification endpoint
[**getNotificationEndpoints**](NotificationEndpointsApi.md#getNotificationEndpoints) | **GET** /notificationEndpoints | List all notification endpoints
[**getNotificationEndpointsID**](NotificationEndpointsApi.md#getNotificationEndpointsID) | **GET** /notificationEndpoints/{endpointID} | Retrieve a notification endpoint
[**getNotificationEndpointsIDLabels**](NotificationEndpointsApi.md#getNotificationEndpointsIDLabels) | **GET** /notificationEndpoints/{endpointID}/labels | List all labels for a notification endpoint
[**patchNotificationEndpointsID**](NotificationEndpointsApi.md#patchNotificationEndpointsID) | **PATCH** /notificationEndpoints/{endpointID} | Update a notification endpoint
[**postNotificationEndpointIDLabels**](NotificationEndpointsApi.md#postNotificationEndpointIDLabels) | **POST** /notificationEndpoints/{endpointID}/labels | Add a label to a notification endpoint
[**putNotificationEndpointsID**](NotificationEndpointsApi.md#putNotificationEndpointsID) | **PUT** /notificationEndpoints/{endpointID} | Update a notification endpoint



## createNotificationEndpoint

> NotificationEndpoint createNotificationEndpoint(postNotificationEndpoint)

Add a notification endpoint

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.NotificationEndpointsApi();
let postNotificationEndpoint = new InfluxOssApiService.PostNotificationEndpoint(); // PostNotificationEndpoint | Notification endpoint to create
apiInstance.createNotificationEndpoint(postNotificationEndpoint, (error, data, response) => {
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
 **postNotificationEndpoint** | [**PostNotificationEndpoint**](PostNotificationEndpoint.md)| Notification endpoint to create | 

### Return type

[**NotificationEndpoint**](NotificationEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNotificationEndpointsID

> deleteNotificationEndpointsID(endpointID, opts)

Delete a notification endpoint

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.NotificationEndpointsApi();
let endpointID = "endpointID_example"; // String | The notification endpoint ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteNotificationEndpointsID(endpointID, opts, (error, data, response) => {
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
 **endpointID** | **String**| The notification endpoint ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteNotificationEndpointsIDLabelsID

> deleteNotificationEndpointsIDLabelsID(endpointID, labelID, opts)

Delete a label from a notification endpoint

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.NotificationEndpointsApi();
let endpointID = "endpointID_example"; // String | The notification endpoint ID.
let labelID = "labelID_example"; // String | The ID of the label to delete.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteNotificationEndpointsIDLabelsID(endpointID, labelID, opts, (error, data, response) => {
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
 **endpointID** | **String**| The notification endpoint ID. | 
 **labelID** | **String**| The ID of the label to delete. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNotificationEndpoints

> NotificationEndpoints getNotificationEndpoints(orgID, opts)

List all notification endpoints

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.NotificationEndpointsApi();
let orgID = "orgID_example"; // String | Only show notification endpoints that belong to specific organization ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'offset': 56, // Number | 
  'limit': 20 // Number | 
};
apiInstance.getNotificationEndpoints(orgID, opts, (error, data, response) => {
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
 **orgID** | **String**| Only show notification endpoints that belong to specific organization ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **offset** | **Number**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 20]

### Return type

[**NotificationEndpoints**](NotificationEndpoints.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNotificationEndpointsID

> NotificationEndpoint getNotificationEndpointsID(endpointID, opts)

Retrieve a notification endpoint

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.NotificationEndpointsApi();
let endpointID = "endpointID_example"; // String | The notification endpoint ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getNotificationEndpointsID(endpointID, opts, (error, data, response) => {
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
 **endpointID** | **String**| The notification endpoint ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**NotificationEndpoint**](NotificationEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNotificationEndpointsIDLabels

> LabelsResponse getNotificationEndpointsIDLabels(endpointID, opts)

List all labels for a notification endpoint

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.NotificationEndpointsApi();
let endpointID = "endpointID_example"; // String | The notification endpoint ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getNotificationEndpointsIDLabels(endpointID, opts, (error, data, response) => {
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
 **endpointID** | **String**| The notification endpoint ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelsResponse**](LabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchNotificationEndpointsID

> NotificationEndpoint patchNotificationEndpointsID(endpointID, notificationEndpointUpdate, opts)

Update a notification endpoint

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.NotificationEndpointsApi();
let endpointID = "endpointID_example"; // String | The notification endpoint ID.
let notificationEndpointUpdate = new InfluxOssApiService.NotificationEndpointUpdate(); // NotificationEndpointUpdate | Check update to apply
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchNotificationEndpointsID(endpointID, notificationEndpointUpdate, opts, (error, data, response) => {
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
 **endpointID** | **String**| The notification endpoint ID. | 
 **notificationEndpointUpdate** | [**NotificationEndpointUpdate**](NotificationEndpointUpdate.md)| Check update to apply | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**NotificationEndpoint**](NotificationEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postNotificationEndpointIDLabels

> LabelResponse postNotificationEndpointIDLabels(endpointID, labelMapping, opts)

Add a label to a notification endpoint

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.NotificationEndpointsApi();
let endpointID = "endpointID_example"; // String | The notification endpoint ID.
let labelMapping = new InfluxOssApiService.LabelMapping(); // LabelMapping | Label to add
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postNotificationEndpointIDLabels(endpointID, labelMapping, opts, (error, data, response) => {
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
 **endpointID** | **String**| The notification endpoint ID. | 
 **labelMapping** | [**LabelMapping**](LabelMapping.md)| Label to add | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putNotificationEndpointsID

> NotificationEndpoint putNotificationEndpointsID(endpointID, notificationEndpoint, opts)

Update a notification endpoint

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.NotificationEndpointsApi();
let endpointID = "endpointID_example"; // String | The notification endpoint ID.
let notificationEndpoint = new InfluxOssApiService.NotificationEndpoint(); // NotificationEndpoint | A new notification endpoint to replace the existing endpoint with
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.putNotificationEndpointsID(endpointID, notificationEndpoint, opts, (error, data, response) => {
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
 **endpointID** | **String**| The notification endpoint ID. | 
 **notificationEndpoint** | [**NotificationEndpoint**](NotificationEndpoint.md)| A new notification endpoint to replace the existing endpoint with | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**NotificationEndpoint**](NotificationEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

