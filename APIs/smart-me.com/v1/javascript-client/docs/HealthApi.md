# SmartMe.HealthApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthGet**](HealthApi.md#healthGet) | **GET** /api/Health | A method returning HTTP 200 OK when queried.              It is used by Kubernetes probes to determine whether the app is healthy.



## healthGet

> Object healthGet()

A method returning HTTP 200 OK when queried.              It is used by Kubernetes probes to determine whether the app is healthy.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.HealthApi();
apiInstance.healthGet((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

