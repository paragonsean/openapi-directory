# SalesLoftPlatform.CadenceExportsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2CadenceExportsIdJsonGet**](CadenceExportsApi.md#v2CadenceExportsIdJsonGet) | **GET** /v2/cadence_exports/{id}.json | Export a cadence



## v2CadenceExportsIdJsonGet

> CadenceExport v2CadenceExportsIdJsonGet(id)

Export a cadence

Exports a cadence as JSON. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.CadenceExportsApi();
let id = "id_example"; // String | Cadence ID
apiInstance.v2CadenceExportsIdJsonGet(id, (error, data, response) => {
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
 **id** | **String**| Cadence ID | 

### Return type

[**CadenceExport**](CadenceExport.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

