# OoxmlAutomation.ChartsRowCollectionsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chartRowcollectionsGetId**](ChartsRowCollectionsApi.md#chartRowcollectionsGetId) | **GET** /Charts/RowCollections/{id} | RowCollections: Get by Id



## chartRowcollectionsGetId

> ChartRowCollections chartRowcollectionsGetId(id)

RowCollections: Get by Id

Get by Id: Use this method to retrieve a RowCollections object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsRowCollectionsApi();
let id = "id_example"; // String | 
apiInstance.chartRowcollectionsGetId(id, (error, data, response) => {
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

[**ChartRowCollections**](ChartRowCollections.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

