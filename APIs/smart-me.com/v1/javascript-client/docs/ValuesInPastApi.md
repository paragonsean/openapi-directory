# SmartMe.ValuesInPastApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**valuesInPastGet**](ValuesInPastApi.md#valuesInPastGet) | **GET** /api/ValuesInPast/{id} | Gets all (last) values of a device              The first Value found before the given Date is returned.



## valuesInPastGet

> ValuesData valuesInPastGet(id, date)

Gets all (last) values of a device              The first Value found before the given Date is returned.

Gets the Values for a device at a given Date. The first Value found before the given Date is returned.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.ValuesInPastApi();
let id = "id_example"; // String | The ID of the device
let date = new Date("2013-10-20T19:20:30+01:00"); // Date | the date of the value
apiInstance.valuesInPastGet(id, date, (error, data, response) => {
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
 **date** | **Date**| the date of the value | 

### Return type

[**ValuesData**](ValuesData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

