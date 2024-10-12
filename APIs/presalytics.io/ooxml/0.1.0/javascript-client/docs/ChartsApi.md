# OoxmlAutomation.ChartsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chartsChartsChartupdateGetId**](ChartsApi.md#chartsChartsChartupdateGetId) | **GET** /Charts/ChartUpdate/{id} | Charts: Get Chart Data
[**chartsChartsChartupdatePutId**](ChartsApi.md#chartsChartsChartupdatePutId) | **PUT** /Charts/ChartUpdate/{id} | Charts: Update Chart Data
[**chartsChartsChildobjectsGetId**](ChartsApi.md#chartsChartsChildobjectsGetId) | **GET** /Charts/ChildObjects/{id} | Charts: Get Dependent Objects Tree
[**chartsChartsDetailsGetId**](ChartsApi.md#chartsChartsDetailsGetId) | **GET** /Charts/Details/{id} | Charts: Get Details
[**chartsChartsGetId**](ChartsApi.md#chartsChartsGetId) | **GET** /Charts/{id} | Charts: Get by Id
[**chartsChartsOpenofficexmlGetIdUpdated**](ChartsApi.md#chartsChartsOpenofficexmlGetIdUpdated) | **GET** /Charts/OpenOfficeXml/{id} | Charts: Get Underlying Xml
[**chartsChartsOpenofficexmlPutId**](ChartsApi.md#chartsChartsOpenofficexmlPutId) | **PUT** /Charts/OpenOfficeXml/{id} | Charts: Modify Underlying Xml
[**chartsChartsSvgGetIdUseCache**](ChartsApi.md#chartsChartsSvgGetIdUseCache) | **GET** /Charts/Svg/{id} | Charts: Get Svg file



## chartsChartsChartupdateGetId

> ChartChartDataDTO chartsChartsChartupdateGetId(id)

Charts: Get Chart Data

Gets a ChartDataDTO object, usually used for downstream analytics and chart updates

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsApi();
let id = "id_example"; // String | 
apiInstance.chartsChartsChartupdateGetId(id, (error, data, response) => {
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

[**ChartChartDataDTO**](ChartChartDataDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chartsChartsChartupdatePutId

> chartsChartsChartupdatePutId(id, opts)

Charts: Update Chart Data

Simplifies chart update by allowing users to supply data via ChartDataDTO

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsApi();
let id = "id_example"; // String | The Chart Id
let opts = {
  'chartChartDataDTO': new OoxmlAutomation.ChartChartDataDTO() // ChartChartDataDTO | The ChartDataDto Object
};
apiInstance.chartsChartsChartupdatePutId(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The Chart Id | 
 **chartChartDataDTO** | [**ChartChartDataDTO**](ChartChartDataDTO.md)| The ChartDataDto Object | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json


## chartsChartsChildobjectsGetId

> [ChildObjects] chartsChartsChildobjectsGetId(id)

Charts: Get Dependent Objects Tree

This endpoint is helpful for helping users and bots identify dependent objects to this Chart and retreive their corresponding metadata in order to make modifications to those objects in downstream operations.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsApi();
let id = "id_example"; // String | 
apiInstance.chartsChartsChildobjectsGetId(id, (error, data, response) => {
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

[**[ChildObjects]**](ChildObjects.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chartsChartsDetailsGetId

> ChartChartsDetails chartsChartsDetailsGetId(id)

Charts: Get Details

Returns object metadata and information about relative dependent objects 

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsApi();
let id = "id_example"; // String | 
apiInstance.chartsChartsDetailsGetId(id, (error, data, response) => {
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

[**ChartChartsDetails**](ChartChartsDetails.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chartsChartsGetId

> ChartCharts chartsChartsGetId(id)

Charts: Get by Id

Get by Id: Use this method to retrieve a Charts object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsApi();
let id = "id_example"; // String | An Id of the respository DTO elemennt
apiInstance.chartsChartsGetId(id, (error, data, response) => {
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
 **id** | **String**| An Id of the respository DTO elemennt | 

### Return type

[**ChartCharts**](ChartCharts.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chartsChartsOpenofficexmlGetIdUpdated

> OoxmlDTO chartsChartsOpenofficexmlGetIdUpdated(id, opts)

Charts: Get Underlying Xml

Return the subset of the xml content from within the latest edited version of the OpenXmlDocument from this Chart object.  The returned xml data conforms to the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm).  Use this endpoint a starting point for building client-side extensions that modify Presalytics widgets containing Chart objects.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsApi();
let id = "id_example"; // String | 
let opts = {
  'updated': true // Boolean | Indicates whether API should return the orginal uploaded xml (false) or the actively updated version (true, default)
};
apiInstance.chartsChartsOpenofficexmlGetIdUpdated(id, opts, (error, data, response) => {
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
 **updated** | **Boolean**| Indicates whether API should return the orginal uploaded xml (false) or the actively updated version (true, default) | [optional] [default to true]

### Return type

[**OoxmlDTO**](OoxmlDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chartsChartsOpenofficexmlPutId

> chartsChartsOpenofficexmlPutId(id, opts)

Charts: Modify Underlying Xml

Directly eidt the underlying xml of a Chart object within an OpenOpenXml (e.g. Excel, Powerpoint) document. This endpoint will validatate the submitted xml against the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm) prior to saving modification.  Invalid xml will rejected by this endpoint and a (hopefully) helpful error message will be returned.  Use this endpoint for client-side automation of modifications ot Chart objects.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsApi();
let id = "id_example"; // String | 
let opts = {
  'ooxmlDTO': new OoxmlAutomation.OoxmlDTO() // OoxmlDTO | 
};
apiInstance.chartsChartsOpenofficexmlPutId(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **ooxmlDTO** | [**OoxmlDTO**](OoxmlDTO.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json


## chartsChartsSvgGetIdUseCache

> File chartsChartsSvgGetIdUseCache(id, opts)

Charts: Get Svg file

This endpoint is helpful for rending this Chart as an svg or image object that can then be rendered in a story, dashboard or website.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ChartsApi();
let id = "id_example"; // String | 
let opts = {
  'useCache': false // Boolean | Indicates whether API should retrieve content from a cache if aviable (true, default), or force an update (false)
};
apiInstance.chartsChartsSvgGetIdUseCache(id, opts, (error, data, response) => {
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
 **useCache** | **Boolean**| Indicates whether API should retrieve content from a cache if aviable (true, default), or force an update (false) | [optional] [default to false]

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/svg+xml, application/json

