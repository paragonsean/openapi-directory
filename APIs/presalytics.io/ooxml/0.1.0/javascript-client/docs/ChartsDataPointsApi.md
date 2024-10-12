# OoxmlAutomation.ChartsDataPointsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chartDatapointsGetId**](ChartsDataPointsApi.md#chartDatapointsGetId) | **GET** /Charts/DataPoints/{id} | DataPoints: Get by Id



## chartDatapointsGetId

> ChartDataPoints chartDatapointsGetId(id)

DataPoints: Get by Id

Get by Id: Use this method to retrieve a DataPoints object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsDataPointsApi();
let id = "id_example"; // String | 
apiInstance.chartDatapointsGetId(id, (error, data, response) => {
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

[**ChartDataPoints**](ChartDataPoints.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

