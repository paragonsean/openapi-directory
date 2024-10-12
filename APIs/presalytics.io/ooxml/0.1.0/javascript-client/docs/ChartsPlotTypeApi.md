# OoxmlAutomation.ChartsPlotTypeApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chartPlottypeGet**](ChartsPlotTypeApi.md#chartPlottypeGet) | **GET** /Charts/PlotType | PlotType: List All Possible Types
[**chartPlottypeGetId**](ChartsPlotTypeApi.md#chartPlottypeGetId) | **GET** /Charts/PlotType/{id} | PlotType: Get by Id
[**chartPlottypeTypeidGetTypeId**](ChartsPlotTypeApi.md#chartPlottypeTypeidGetTypeId) | **GET** /Charts/PlotType/TypeId/{type_id} | PlotType: Get By Type Id



## chartPlottypeGet

> [ChartPlotType] chartPlottypeGet()

PlotType: List All Possible Types

List Types: Use this method to retreive a list of possible options for the PlotType type. Use the Id from oneof the returned elements on to make changes to elements in the Chart object space.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsPlotTypeApi();
apiInstance.chartPlottypeGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[ChartPlotType]**](ChartPlotType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## chartPlottypeGetId

> ChartPlotType chartPlottypeGetId(id)

PlotType: Get by Id

Get by Id: Use this method to retrieve a PlotType object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsPlotTypeApi();
let id = "id_example"; // String | 
apiInstance.chartPlottypeGetId(id, (error, data, response) => {
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

[**ChartPlotType**](ChartPlotType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## chartPlottypeTypeidGetTypeId

> ChartPlotType chartPlottypeTypeidGetTypeId(typeId)

PlotType: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsPlotTypeApi();
let typeId = 56; // Number | 
apiInstance.chartPlottypeTypeidGetTypeId(typeId, (error, data, response) => {
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
 **typeId** | **Number**|  | 

### Return type

[**ChartPlotType**](ChartPlotType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

