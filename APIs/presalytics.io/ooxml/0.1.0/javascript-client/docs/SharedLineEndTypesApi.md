# OoxmlAutomation.SharedLineEndTypesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedLineendtypesGet**](SharedLineEndTypesApi.md#sharedLineendtypesGet) | **GET** /Shared/LineEndTypes | LineEndTypes: List All Possible Types
[**sharedLineendtypesGetId**](SharedLineEndTypesApi.md#sharedLineendtypesGetId) | **GET** /Shared/LineEndTypes/{id} | LineEndTypes: Get by Id
[**sharedLineendtypesTypeidGetTypeId**](SharedLineEndTypesApi.md#sharedLineendtypesTypeidGetTypeId) | **GET** /Shared/LineEndTypes/TypeId/{type_id} | LineEndTypes: Get By Type Id



## sharedLineendtypesGet

> [SharedLineEndTypes] sharedLineendtypesGet()

LineEndTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the LineEndTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Shared object space.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedLineEndTypesApi();
apiInstance.sharedLineendtypesGet((error, data, response) => {
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

[**[SharedLineEndTypes]**](SharedLineEndTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## sharedLineendtypesGetId

> SharedLineEndTypes sharedLineendtypesGetId(id)

LineEndTypes: Get by Id

Get by Id: Use this method to retrieve a LineEndTypes object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedLineEndTypesApi();
let id = "id_example"; // String | 
apiInstance.sharedLineendtypesGetId(id, (error, data, response) => {
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

[**SharedLineEndTypes**](SharedLineEndTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## sharedLineendtypesTypeidGetTypeId

> SharedLineEndTypes sharedLineendtypesTypeidGetTypeId(typeId)

LineEndTypes: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedLineEndTypesApi();
let typeId = 56; // Number | 
apiInstance.sharedLineendtypesTypeidGetTypeId(typeId, (error, data, response) => {
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

[**SharedLineEndTypes**](SharedLineEndTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

