# OoxmlAutomation.ChartsRowsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chartRowsGetId**](ChartsRowsApi.md#chartRowsGetId) | **GET** /Charts/Rows/{id} | Rows: Get by Id



## chartRowsGetId

> ChartRows chartRowsGetId(id)

Rows: Get by Id

Get by Id: Use this method to retrieve a Rows object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsRowsApi();
let id = "id_example"; // String | 
apiInstance.chartRowsGetId(id, (error, data, response) => {
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

[**ChartRows**](ChartRows.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

