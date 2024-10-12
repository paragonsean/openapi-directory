# Apacta.ReportsApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reportsGet**](ReportsApi.md#reportsGet) | **GET** /reports | 



## reportsGet

> reportsGet()



View list of report types

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.ReportsApi();
apiInstance.reportsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

