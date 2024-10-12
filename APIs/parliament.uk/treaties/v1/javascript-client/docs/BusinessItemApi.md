# TreatiesApi.BusinessItemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBusinessItemById**](BusinessItemApi.md#getBusinessItemById) | **GET** /api/BusinessItem/{id} | Returns business item by ID.



## getBusinessItemById

> BusinessItemResource getBusinessItemById(id)

Returns business item by ID.

### Example

```javascript
import TreatiesApi from 'treaties_api';

let apiInstance = new TreatiesApi.BusinessItemApi();
let id = "id_example"; // String | Business item with the ID specified
apiInstance.getBusinessItemById(id, (error, data, response) => {
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
 **id** | **String**| Business item with the ID specified | 

### Return type

[**BusinessItemResource**](BusinessItemResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

