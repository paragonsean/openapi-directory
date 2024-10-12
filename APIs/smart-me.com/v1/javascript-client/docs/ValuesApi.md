# SmartMe.ValuesApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**valuesGet**](ValuesApi.md#valuesGet) | **GET** /api/Values/{id} | Gets all (last) values of a device



## valuesGet

> ValuesData valuesGet(id)

Gets all (last) values of a device

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.ValuesApi();
let id = "id_example"; // String | The ID of the device
apiInstance.valuesGet(id, (error, data, response) => {
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
 **id** | **String**| The ID of the device | 

### Return type

[**ValuesData**](ValuesData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

