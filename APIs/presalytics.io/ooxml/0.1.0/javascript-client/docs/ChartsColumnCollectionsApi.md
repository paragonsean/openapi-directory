# OoxmlAutomation.ChartsColumnCollectionsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chartColumncollectionsGetId**](ChartsColumnCollectionsApi.md#chartColumncollectionsGetId) | **GET** /Charts/ColumnCollections/{id} | ColumnCollections: Get by Id



## chartColumncollectionsGetId

> ChartColumnCollections chartColumncollectionsGetId(id)

ColumnCollections: Get by Id

Get by Id: Use this method to retrieve a ColumnCollections object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsColumnCollectionsApi();
let id = "id_example"; // String | 
apiInstance.chartColumncollectionsGetId(id, (error, data, response) => {
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

[**ChartColumnCollections**](ChartColumnCollections.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

