# OoxmlAutomation.SharedFillTypesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedFilltypesGet**](SharedFillTypesApi.md#sharedFilltypesGet) | **GET** /Shared/FillTypes | FillTypes: List All Possible Types
[**sharedFilltypesGetId**](SharedFillTypesApi.md#sharedFilltypesGetId) | **GET** /Shared/FillTypes/{id} | FillTypes: Get by Id
[**sharedFilltypesTypeidGetTypeId**](SharedFillTypesApi.md#sharedFilltypesTypeidGetTypeId) | **GET** /Shared/FillTypes/TypeId/{type_id} | FillTypes: Get By Type Id



## sharedFilltypesGet

> [SharedFillTypes] sharedFilltypesGet()

FillTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the FillTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Shared object space.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedFillTypesApi();
apiInstance.sharedFilltypesGet((error, data, response) => {
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

[**[SharedFillTypes]**](SharedFillTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## sharedFilltypesGetId

> SharedFillTypes sharedFilltypesGetId(id)

FillTypes: Get by Id

Get by Id: Use this method to retrieve a FillTypes object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedFillTypesApi();
let id = "id_example"; // String | 
apiInstance.sharedFilltypesGetId(id, (error, data, response) => {
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

[**SharedFillTypes**](SharedFillTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## sharedFilltypesTypeidGetTypeId

> SharedFillTypes sharedFilltypesTypeidGetTypeId(typeId)

FillTypes: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedFillTypesApi();
let typeId = 56; // Number | 
apiInstance.sharedFilltypesTypeidGetTypeId(typeId, (error, data, response) => {
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

[**SharedFillTypes**](SharedFillTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

