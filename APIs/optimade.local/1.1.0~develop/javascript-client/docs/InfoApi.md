# OptimadeApi.InfoApi

All URIs are relative to *http://optimade.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEntryInfoInfoEntryGet**](InfoApi.md#getEntryInfoInfoEntryGet) | **GET** /info/{entry} | Get Entry Info
[**getInfoInfoGet**](InfoApi.md#getInfoInfoGet) | **GET** /info | Get Info



## getEntryInfoInfoEntryGet

> EntryInfoResponse getEntryInfoInfoEntryGet(entry)

Get Entry Info

### Example

```javascript
import OptimadeApi from 'optimade_api';

let apiInstance = new OptimadeApi.InfoApi();
let entry = "entry_example"; // String | 
apiInstance.getEntryInfoInfoEntryGet(entry, (error, data, response) => {
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
 **entry** | **String**|  | 

### Return type

[**EntryInfoResponse**](EntryInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInfoInfoGet

> InfoResponse getInfoInfoGet()

Get Info

### Example

```javascript
import OptimadeApi from 'optimade_api';

let apiInstance = new OptimadeApi.InfoApi();
apiInstance.getInfoInfoGet((error, data, response) => {
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

[**InfoResponse**](InfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

