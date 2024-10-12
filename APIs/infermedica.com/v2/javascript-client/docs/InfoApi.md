# InfermedicaApi.InfoApi

All URIs are relative to *https://api.infermedica.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDatabaseInfo**](InfoApi.md#getDatabaseInfo) | **GET** /info | Get database information



## getDatabaseInfo

> InfoPublic getDatabaseInfo(opts)

Get database information

Returns information about data used by diagnostic engine.

### Example

```javascript
import InfermedicaApi from 'infermedica_api';

let apiInstance = new InfermedicaApi.InfoApi();
let opts = {
  'ageValue': 18, // Number | age value
  'ageUnit': "year" // String | unit in which age value was provided
};
apiInstance.getDatabaseInfo(opts, (error, data, response) => {
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
 **ageValue** | **Number**| age value | [optional] 
 **ageUnit** | **String**| unit in which age value was provided | [optional] [default to &#39;year&#39;]

### Return type

[**InfoPublic**](InfoPublic.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

