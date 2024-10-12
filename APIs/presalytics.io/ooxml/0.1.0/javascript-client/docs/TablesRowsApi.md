# OoxmlAutomation.TablesRowsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tablesRowsGetId**](TablesRowsApi.md#tablesRowsGetId) | **GET** /Tables/Rows/{id} | Rows: Get by Id



## tablesRowsGetId

> TableRows tablesRowsGetId(id)

Rows: Get by Id

Get by Id: Use this method to retrieve a Rows object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.TablesRowsApi();
let id = "id_example"; // String | 
apiInstance.tablesRowsGetId(id, (error, data, response) => {
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

[**TableRows**](TableRows.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

