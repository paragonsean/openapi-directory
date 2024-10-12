# DweetIo.AlertsApi

All URIs are relative to *https://dweet.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAlertGET**](AlertsApi.md#createAlertGET) | **GET** /alert/{who}/when/{thing}/{condition} | Create an alert for a thing. A thing must be locked before an alert can be set.
[**getAlert**](AlertsApi.md#getAlert) | **GET** /get/alert/for/{thing} | Get the alert attached to a thing.
[**removeAlert**](AlertsApi.md#removeAlert) | **GET** /remove/alert/for/{thing} | Remove an alert for a thing.



## createAlertGET

> createAlertGET(who, thing, condition, key)

Create an alert for a thing. A thing must be locked before an alert can be set.

### Example

```javascript
import DweetIo from 'dweet_io';

let apiInstance = new DweetIo.AlertsApi();
let who = "who_example"; // String | A comma separated list of Email addresses to send the alert to.
let thing = "thing_example"; // String | A unique name of a thing. It is recommended that you use a GUID as to avoid name collisions.
let condition = "condition_example"; // String | A condition that returns a string or a true value if a condition is met.
let key = "key_example"; // String | A valid key for a locked thing. If the thing is not locked, this can be ignored.
apiInstance.createAlertGET(who, thing, condition, key, (error, data, response) => {
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
 **who** | **String**| A comma separated list of Email addresses to send the alert to. | 
 **thing** | **String**| A unique name of a thing. It is recommended that you use a GUID as to avoid name collisions. | 
 **condition** | **String**| A condition that returns a string or a true value if a condition is met. | 
 **key** | **String**| A valid key for a locked thing. If the thing is not locked, this can be ignored. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAlert

> getAlert(thing, key)

Get the alert attached to a thing.

### Example

```javascript
import DweetIo from 'dweet_io';

let apiInstance = new DweetIo.AlertsApi();
let thing = "thing_example"; // String | A unique name of a thing.
let key = "key_example"; // String | A valid key for a locked thing. If the thing is not locked, this can be ignored.
apiInstance.getAlert(thing, key, (error, data, response) => {
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
 **thing** | **String**| A unique name of a thing. | 
 **key** | **String**| A valid key for a locked thing. If the thing is not locked, this can be ignored. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeAlert

> removeAlert(thing, key)

Remove an alert for a thing.

### Example

```javascript
import DweetIo from 'dweet_io';

let apiInstance = new DweetIo.AlertsApi();
let thing = "thing_example"; // String | A unique name of a thing.
let key = "key_example"; // String | A valid key for a locked thing. If the thing is not locked, this can be ignored.
apiInstance.removeAlert(thing, key, (error, data, response) => {
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
 **thing** | **String**| A unique name of a thing. | 
 **key** | **String**| A valid key for a locked thing. If the thing is not locked, this can be ignored. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

