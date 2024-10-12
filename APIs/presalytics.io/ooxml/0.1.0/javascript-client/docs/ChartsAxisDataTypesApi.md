# OoxmlAutomation.ChartsAxisDataTypesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chartAxisdatatypesGet**](ChartsAxisDataTypesApi.md#chartAxisdatatypesGet) | **GET** /Charts/AxisDataTypes | AxisDataTypes: List All Possible Types
[**chartAxisdatatypesGetId**](ChartsAxisDataTypesApi.md#chartAxisdatatypesGetId) | **GET** /Charts/AxisDataTypes/{id} | AxisDataTypes: Get by Id
[**chartAxisdatatypesTypeidGetTypeId**](ChartsAxisDataTypesApi.md#chartAxisdatatypesTypeidGetTypeId) | **GET** /Charts/AxisDataTypes/TypeId/{type_id} | AxisDataTypes: Get By Type Id



## chartAxisdatatypesGet

> [ChartAxisDataTypes] chartAxisdatatypesGet()

AxisDataTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the AxisDataTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Chart object space.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsAxisDataTypesApi();
apiInstance.chartAxisdatatypesGet((error, data, response) => {
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

[**[ChartAxisDataTypes]**](ChartAxisDataTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## chartAxisdatatypesGetId

> ChartAxisDataTypes chartAxisdatatypesGetId(id)

AxisDataTypes: Get by Id

Get by Id: Use this method to retrieve a AxisDataTypes object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsAxisDataTypesApi();
let id = "id_example"; // String | 
apiInstance.chartAxisdatatypesGetId(id, (error, data, response) => {
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

[**ChartAxisDataTypes**](ChartAxisDataTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## chartAxisdatatypesTypeidGetTypeId

> ChartAxisDataTypes chartAxisdatatypesTypeidGetTypeId(typeId)

AxisDataTypes: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsAxisDataTypesApi();
let typeId = 56; // Number | 
apiInstance.chartAxisdatatypesTypeidGetTypeId(typeId, (error, data, response) => {
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

[**ChartAxisDataTypes**](ChartAxisDataTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

