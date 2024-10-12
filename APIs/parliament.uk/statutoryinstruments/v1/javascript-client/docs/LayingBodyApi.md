# StatutoryInstrumentsApi.LayingBodyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLayingBodies**](LayingBodyApi.md#getLayingBodies) | **GET** /api/v1/LayingBody | Returns all laying bodies.



## getLayingBodies

> LayingBodyResourceCollection getLayingBodies()

Returns all laying bodies.

### Example

```javascript
import StatutoryInstrumentsApi from 'statutory_instruments_api';

let apiInstance = new StatutoryInstrumentsApi.LayingBodyApi();
apiInstance.getLayingBodies((error, data, response) => {
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

[**LayingBodyResourceCollection**](LayingBodyResourceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

