# OoxmlAutomation.TablesCellsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tablesCellsGetId**](TablesCellsApi.md#tablesCellsGetId) | **GET** /Tables/Cells/{id} | Cells: Get by Id



## tablesCellsGetId

> TableCells tablesCellsGetId(id)

Cells: Get by Id

Get by Id: Use this method to retrieve a Cells object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.TablesCellsApi();
let id = "id_example"; // String | 
apiInstance.tablesCellsGetId(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**TableCells**](TableCells.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

