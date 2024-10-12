# OoxmlAutomation.SharedDashTypesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedDashtypesGet**](SharedDashTypesApi.md#sharedDashtypesGet) | **GET** /Shared/DashTypes | DashTypes: List All Possible Types
[**sharedDashtypesGetId**](SharedDashTypesApi.md#sharedDashtypesGetId) | **GET** /Shared/DashTypes/{id} | DashTypes: Get by Id
[**sharedDashtypesTypeidGetTypeId**](SharedDashTypesApi.md#sharedDashtypesTypeidGetTypeId) | **GET** /Shared/DashTypes/TypeId/{type_id} | DashTypes: Get By Type Id



## sharedDashtypesGet

> [SharedDashTypes] sharedDashtypesGet()

DashTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the DashTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Shared object space.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedDashTypesApi();
apiInstance.sharedDashtypesGet((error, data, response) => {
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

[**[SharedDashTypes]**](SharedDashTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## sharedDashtypesGetId

> SharedDashTypes sharedDashtypesGetId(id)

DashTypes: Get by Id

Get by Id: Use this method to retrieve a DashTypes object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedDashTypesApi();
let id = "id_example"; // String | 
apiInstance.sharedDashtypesGetId(id, (error, data, response) => {
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

[**SharedDashTypes**](SharedDashTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## sharedDashtypesTypeidGetTypeId

> SharedDashTypes sharedDashtypesTypeidGetTypeId(typeId)

DashTypes: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedDashTypesApi();
let typeId = 56; // Number | 
apiInstance.sharedDashtypesTypeidGetTypeId(typeId, (error, data, response) => {
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

[**SharedDashTypes**](SharedDashTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

