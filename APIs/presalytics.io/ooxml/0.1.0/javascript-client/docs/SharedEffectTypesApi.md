# OoxmlAutomation.SharedEffectTypesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedEffecttypesGet**](SharedEffectTypesApi.md#sharedEffecttypesGet) | **GET** /Shared/EffectTypes | EffectTypes: List All Possible Types
[**sharedEffecttypesGetId**](SharedEffectTypesApi.md#sharedEffecttypesGetId) | **GET** /Shared/EffectTypes/{id} | EffectTypes: Get by Id
[**sharedEffecttypesTypeidGetTypeId**](SharedEffectTypesApi.md#sharedEffecttypesTypeidGetTypeId) | **GET** /Shared/EffectTypes/TypeId/{type_id} | EffectTypes: Get By Type Id



## sharedEffecttypesGet

> [SharedEffectTypes] sharedEffecttypesGet()

EffectTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the EffectTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Shared object space.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedEffectTypesApi();
apiInstance.sharedEffecttypesGet((error, data, response) => {
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

[**[SharedEffectTypes]**](SharedEffectTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## sharedEffecttypesGetId

> SharedEffectTypes sharedEffecttypesGetId(id)

EffectTypes: Get by Id

Get by Id: Use this method to retrieve a EffectTypes object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedEffectTypesApi();
let id = "id_example"; // String | 
apiInstance.sharedEffecttypesGetId(id, (error, data, response) => {
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

[**SharedEffectTypes**](SharedEffectTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## sharedEffecttypesTypeidGetTypeId

> SharedEffectTypes sharedEffecttypesTypeidGetTypeId(typeId)

EffectTypes: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedEffectTypesApi();
let typeId = 56; // Number | 
apiInstance.sharedEffecttypesTypeidGetTypeId(typeId, (error, data, response) => {
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

[**SharedEffectTypes**](SharedEffectTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

