# OptimadeApi.VersionsApi

All URIs are relative to *http://optimade.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getVersionsVersionsGet**](VersionsApi.md#getVersionsVersionsGet) | **GET** /versions | Get Versions



## getVersionsVersionsGet

> String getVersionsVersionsGet()

Get Versions

Respond with the text/csv representation for the served versions.

### Example

```javascript
import OptimadeApi from 'optimade_api';

let apiInstance = new OptimadeApi.VersionsApi();
apiInstance.getVersionsVersionsGet((error, data, response) => {
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
- **Accept**: text/csv; header=present

