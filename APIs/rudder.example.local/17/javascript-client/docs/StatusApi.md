# RudderApi.StatusApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**none**](StatusApi.md#none) | **GET** /status | Check if Rudder is alive



## none

> String none()

Check if Rudder is alive

An unauthenticated API to check if Rudder web application is up and running. Be careful: this API does not follow other Rudder&#39;s API convention:  - it is not versioned, so the path is just &#x60;/api/status&#x60;; - it returns a plain text message.

### Example

```javascript
import RudderApi from 'rudder_api';

let apiInstance = new RudderApi.StatusApi();
apiInstance.none((error, data, response) => {
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

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

