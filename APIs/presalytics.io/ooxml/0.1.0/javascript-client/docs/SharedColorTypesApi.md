# OoxmlAutomation.SharedColorTypesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedColortypesGet**](SharedColorTypesApi.md#sharedColortypesGet) | **GET** /Shared/ColorTypes | ColorTypes: List All Possible Types
[**sharedColortypesGetId**](SharedColorTypesApi.md#sharedColortypesGetId) | **GET** /Shared/ColorTypes/{id} | ColorTypes: Get by Id
[**sharedColortypesTypeidGetTypeId**](SharedColorTypesApi.md#sharedColortypesTypeidGetTypeId) | **GET** /Shared/ColorTypes/TypeId/{type_id} | ColorTypes: Get By Type Id



## sharedColortypesGet

> [SharedColorTypes] sharedColortypesGet()

ColorTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the ColorTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Shared object space.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedColorTypesApi();
apiInstance.sharedColortypesGet((error, data, response) => {
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

[**[SharedColorTypes]**](SharedColorTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## sharedColortypesGetId

> SharedColorTypes sharedColortypesGetId(id)

ColorTypes: Get by Id

Get by Id: Use this method to retrieve a ColorTypes object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedColorTypesApi();
let id = "id_example"; // String | 
apiInstance.sharedColortypesGetId(id, (error, data, response) => {
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

[**SharedColorTypes**](SharedColorTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## sharedColortypesTypeidGetTypeId

> SharedColorTypes sharedColortypesTypeidGetTypeId(typeId)

ColorTypes: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedColorTypesApi();
let typeId = 56; // Number | 
apiInstance.sharedColortypesTypeidGetTypeId(typeId, (error, data, response) => {
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

[**SharedColorTypes**](SharedColorTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

