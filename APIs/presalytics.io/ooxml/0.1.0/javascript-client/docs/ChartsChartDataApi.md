# OoxmlAutomation.ChartsChartDataApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chartChartdataGetId**](ChartsChartDataApi.md#chartChartdataGetId) | **GET** /Charts/ChartData/{id} | ChartData: Get by Id



## chartChartdataGetId

> ChartChartData chartChartdataGetId(id)

ChartData: Get by Id

Get by Id: Use this method to retrieve a ChartData object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsChartDataApi();
let id = "id_example"; // String | 
apiInstance.chartChartdataGetId(id, (error, data, response) => {
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

[**ChartChartData**](ChartChartData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

