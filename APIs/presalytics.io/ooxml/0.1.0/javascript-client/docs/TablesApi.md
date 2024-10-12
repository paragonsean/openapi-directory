# OoxmlAutomation.TablesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tablesTablesChildobjectsGetId**](TablesApi.md#tablesTablesChildobjectsGetId) | **GET** /Tables/ChildObjects/{id} | Tables: Get Dependent Objects Tree
[**tablesTablesDetailsGetId**](TablesApi.md#tablesTablesDetailsGetId) | **GET** /Tables/Details/{id} | Tables: Get Details
[**tablesTablesGetId**](TablesApi.md#tablesTablesGetId) | **GET** /Tables/{id} | Tables: Get by Id
[**tablesTablesOpenofficexmlGetIdUpdated**](TablesApi.md#tablesTablesOpenofficexmlGetIdUpdated) | **GET** /Tables/OpenOfficeXml/{id} | Tables: Get Underlying Xml
[**tablesTablesOpenofficexmlPutId**](TablesApi.md#tablesTablesOpenofficexmlPutId) | **PUT** /Tables/OpenOfficeXml/{id} | Tables: Modify Underlying Xml
[**tablesTablesSvgGetIdUseCache**](TablesApi.md#tablesTablesSvgGetIdUseCache) | **GET** /Tables/Svg/{id} | Tables: Get Svg file
[**tablesTablesTableupdateGetId**](TablesApi.md#tablesTablesTableupdateGetId) | **GET** /Tables/TableUpdate/{id} | Table: Get Table Data
[**tablesTablesTableupdatePutId**](TablesApi.md#tablesTablesTableupdatePutId) | **PUT** /Tables/TableUpdate/{id} | Tables: Update Table Data



## tablesTablesChildobjectsGetId

> [ChildObjects] tablesTablesChildobjectsGetId(id)

Tables: Get Dependent Objects Tree

This endpoint is helpful for helping users and bots identify dependent objects to this Table and retreive their corresponding metadata in order to make modifications to those objects in downstream operations.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.TablesApi();
let id = "id_example"; // String | 
apiInstance.tablesTablesChildobjectsGetId(id, (error, data, response) => {
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


## tablesTablesDetailsGetId

> TableTablesDetails tablesTablesDetailsGetId(id)

Tables: Get Details

Returns object metadata and information about relative dependent objects 

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.TablesApi();
let id = "id_example"; // String | 
apiInstance.tablesTablesDetailsGetId(id, (error, data, response) => {
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

[**TableTablesDetails**](TableTablesDetails.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tablesTablesGetId

> TableTables tablesTablesGetId(id)

Tables: Get by Id

Get by Id: Use this method to retrieve a Tables object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.TablesApi();
let id = "id_example"; // String | An Id of the respository DTO elemennt
apiInstance.tablesTablesGetId(id, (error, data, response) => {
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

[**TableTables**](TableTables.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tablesTablesOpenofficexmlGetIdUpdated

> OoxmlDTO tablesTablesOpenofficexmlGetIdUpdated(id, opts)

Tables: Get Underlying Xml

Return the subset of the xml content from within the latest edited version of the OpenXmlDocument from this Table object.  The returned xml data conforms to the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm).  Use this endpoint a starting point for building client-side extensions that modify Presalytics widgets containing Table objects.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.TablesApi();
let id = "id_example"; // String | 
let opts = {
  'updated': true // Boolean | Indicates whether API should return the orginal uploaded xml (false) or the actively updated version (true, default)
};
apiInstance.tablesTablesOpenofficexmlGetIdUpdated(id, opts, (error, data, response) => {
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


## tablesTablesOpenofficexmlPutId

> tablesTablesOpenofficexmlPutId(id, opts)

Tables: Modify Underlying Xml

Directly eidt the underlying xml of a Table object within an OpenOpenXml (e.g. Excel, Powerpoint) document. This endpoint will validatate the submitted xml against the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm) prior to saving modification.  Invalid xml will rejected by this endpoint and a (hopefully) helpful error message will be returned.  Use this endpoint for client-side automation of modifications ot Table objects.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.TablesApi();
let id = "id_example"; // String | 
let opts = {
  'ooxmlDTO': new OoxmlAutomation.OoxmlDTO() // OoxmlDTO | 
};
apiInstance.tablesTablesOpenofficexmlPutId(id, opts, (error, data, response) => {
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


## tablesTablesSvgGetIdUseCache

> File tablesTablesSvgGetIdUseCache(id, opts)

Tables: Get Svg file

This endpoint is helpful for rending this Table as an svg or image object that can then be rendered in a story, dashboard or website.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.TablesApi();
let id = "id_example"; // String | 
let opts = {
  'useCache': false // Boolean | Indicates whether API should retrieve content from a cache if aviable (true, default), or force an update (false)
};
apiInstance.tablesTablesSvgGetIdUseCache(id, opts, (error, data, response) => {
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


## tablesTablesTableupdateGetId

> TableTableDataDTO tablesTablesTableupdateGetId(id)

Table: Get Table Data

Gets a TabletDataDTO object, usually used for downstream updates to table content

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.TablesApi();
let id = "id_example"; // String | 
apiInstance.tablesTablesTableupdateGetId(id, (error, data, response) => {
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

[**TableTableDataDTO**](TableTableDataDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tablesTablesTableupdatePutId

> tablesTablesTableupdatePutId(id, opts)

Tables: Update Table Data

Simplifies table update by allowing users to supply strings to table cells  via TableDataDTO

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.TablesApi();
let id = "id_example"; // String | 
let opts = {
  'tableTableDataDTO': new OoxmlAutomation.TableTableDataDTO() // TableTableDataDTO | 
};
apiInstance.tablesTablesTableupdatePutId(id, opts, (error, data, response) => {
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
 **tableTableDataDTO** | [**TableTableDataDTO**](TableTableDataDTO.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json

