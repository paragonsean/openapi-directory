# JellyfinApi.TimeSyncApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getUtcTime**](TimeSyncApi.md#getUtcTime) | **GET** /GetUtcTime | Gets the current UTC time.



## getUtcTime

> UtcTimeResponse getUtcTime()

Gets the current UTC time.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.TimeSyncApi();
apiInstance.getUtcTime((error, data, response) => {
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

[**UtcTimeResponse**](UtcTimeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

