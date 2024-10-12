# OoxmlAutomation.ChartsRowColApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chartRowcolGet**](ChartsRowColApi.md#chartRowcolGet) | **GET** /Charts/RowCol | RowCol: List All Possible Types
[**chartRowcolGetId**](ChartsRowColApi.md#chartRowcolGetId) | **GET** /Charts/RowCol/{id} | RowCol: Get by Id
[**chartRowcolTypeidGetTypeId**](ChartsRowColApi.md#chartRowcolTypeidGetTypeId) | **GET** /Charts/RowCol/TypeId/{type_id} | RowCol: Get By Type Id



## chartRowcolGet

> [ChartRowCol] chartRowcolGet()

RowCol: List All Possible Types

List Types: Use this method to retreive a list of possible options for the RowCol type. Use the Id from oneof the returned elements on to make changes to elements in the Chart object space.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsRowColApi();
apiInstance.chartRowcolGet((error, data, response) => {
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

[**[ChartRowCol]**](ChartRowCol.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## chartRowcolGetId

> ChartRowCol chartRowcolGetId(id)

RowCol: Get by Id

Get by Id: Use this method to retrieve a RowCol object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsRowColApi();
let id = "id_example"; // String | 
apiInstance.chartRowcolGetId(id, (error, data, response) => {
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

[**ChartRowCol**](ChartRowCol.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## chartRowcolTypeidGetTypeId

> ChartRowCol chartRowcolTypeidGetTypeId(typeId)

RowCol: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsRowColApi();
let typeId = 56; // Number | 
apiInstance.chartRowcolTypeidGetTypeId(typeId, (error, data, response) => {
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

[**ChartRowCol**](ChartRowCol.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

