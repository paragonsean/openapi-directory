# OoxmlAutomation.TablesColumnsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tablesColumnsGetId**](TablesColumnsApi.md#tablesColumnsGetId) | **GET** /Tables/Columns/{id} | Columns: Get by Id



## tablesColumnsGetId

> TableColumns tablesColumnsGetId(id)

Columns: Get by Id

Get by Id: Use this method to retrieve a Columns object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.TablesColumnsApi();
let id = "id_example"; // String | 
apiInstance.tablesColumnsGetId(id, (error, data, response) => {
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

[**TableColumns**](TableColumns.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

