# PollingPlacesApi.DefaultApi

All URIs are relative to *http://api.phila.gov/polling-places/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rootGet**](DefaultApi.md#rootGet) | **GET** / | Get Polling Places Data



## rootGet

> Features rootGet(ward, division, opts)

Get Polling Places Data

### Example

```javascript
import PollingPlacesApi from 'polling_places_api';

let apiInstance = new PollingPlacesApi.DefaultApi();
let ward = 56; // Number | Ward Number
let division = 56; // Number | Division Number
let opts = {
  'callback': "callback_example" // String | Optional parameter for jsonp support.
};
apiInstance.rootGet(ward, division, opts, (error, data, response) => {
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
 **ward** | **Number**| Ward Number | 
 **division** | **Number**| Division Number | 
 **callback** | **String**| Optional parameter for jsonp support. | [optional] 

### Return type

[**Features**](Features.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

