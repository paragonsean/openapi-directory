# FlinksterApiNg.IndexApi

All URIs are relative to *https://api.deutschebahn.com/flinkster-api-ng/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getIndex**](IndexApi.md#getIndex) | **GET** /index | Show index.



## getIndex

> JsonCollection getIndex()

Show index.

Show Service index.

### Example

```javascript
import FlinksterApiNg from 'flinkster_api_ng';

let apiInstance = new FlinksterApiNg.IndexApi();
apiInstance.getIndex((error, data, response) => {
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

[**JsonCollection**](JsonCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

