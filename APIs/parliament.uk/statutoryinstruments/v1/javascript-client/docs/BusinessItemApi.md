# StatutoryInstrumentsApi.BusinessItemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBusinessItemById**](BusinessItemApi.md#getBusinessItemById) | **GET** /api/v1/BusinessItem/{id} | Returns business item by ID.



## getBusinessItemById

> BusinessItemResource getBusinessItemById(id, opts)

Returns business item by ID.

### Example

```javascript
import StatutoryInstrumentsApi from 'statutory_instruments_api';

let apiInstance = new StatutoryInstrumentsApi.BusinessItemApi();
let id = "id_example"; // String | Business item with the ID specified
let opts = {
  'laidPaper': new StatutoryInstrumentsApi.LaidPaperType() // LaidPaperType | Business item by laid paper type
};
apiInstance.getBusinessItemById(id, opts, (error, data, response) => {
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
 **laidPaper** | [**LaidPaperType**](.md)| Business item by laid paper type | [optional] 

### Return type

[**BusinessItemResource**](BusinessItemResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

