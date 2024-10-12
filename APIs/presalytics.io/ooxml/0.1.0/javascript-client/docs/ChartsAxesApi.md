# OoxmlAutomation.ChartsAxesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chartAxesGetId**](ChartsAxesApi.md#chartAxesGetId) | **GET** /Charts/Axes/{id} | Axes: Get by Id



## chartAxesGetId

> ChartAxes chartAxesGetId(id)

Axes: Get by Id

Get by Id: Use this method to retrieve a Axes object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsAxesApi();
let id = "id_example"; // String | 
apiInstance.chartAxesGetId(id, (error, data, response) => {
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

[**ChartAxes**](ChartAxes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

