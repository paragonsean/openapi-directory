# OoxmlAutomation.ChartsRowNameFormatTypesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chartRownameformattypesGet**](ChartsRowNameFormatTypesApi.md#chartRownameformattypesGet) | **GET** /Charts/RowNameFormatTypes | RowNameFormatTypes: List All Possible Types
[**chartRownameformattypesGetId**](ChartsRowNameFormatTypesApi.md#chartRownameformattypesGetId) | **GET** /Charts/RowNameFormatTypes/{id} | RowNameFormatTypes: Get by Id
[**chartRownameformattypesTypeidGetTypeId**](ChartsRowNameFormatTypesApi.md#chartRownameformattypesTypeidGetTypeId) | **GET** /Charts/RowNameFormatTypes/TypeId/{type_id} | RowNameFormatTypes: Get By Type Id



## chartRownameformattypesGet

> [ChartRowNameFormatTypes] chartRownameformattypesGet()

RowNameFormatTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the RowNameFormatTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Chart object space.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsRowNameFormatTypesApi();
apiInstance.chartRownameformattypesGet((error, data, response) => {
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

[**[ChartRowNameFormatTypes]**](ChartRowNameFormatTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## chartRownameformattypesGetId

> ChartRowNameFormatTypes chartRownameformattypesGetId(id)

RowNameFormatTypes: Get by Id

Get by Id: Use this method to retrieve a RowNameFormatTypes object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsRowNameFormatTypesApi();
let id = "id_example"; // String | 
apiInstance.chartRownameformattypesGetId(id, (error, data, response) => {
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

[**ChartRowNameFormatTypes**](ChartRowNameFormatTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## chartRownameformattypesTypeidGetTypeId

> ChartRowNameFormatTypes chartRownameformattypesTypeidGetTypeId(typeId)

RowNameFormatTypes: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsRowNameFormatTypesApi();
let typeId = 56; // Number | 
apiInstance.chartRownameformattypesTypeidGetTypeId(typeId, (error, data, response) => {
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

[**ChartRowNameFormatTypes**](ChartRowNameFormatTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

