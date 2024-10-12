# OoxmlAutomation.SharedLineEndSizesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedLineendsizesGet**](SharedLineEndSizesApi.md#sharedLineendsizesGet) | **GET** /Shared/LineEndSizes | LineEndSizes: List All Possible Types
[**sharedLineendsizesGetId**](SharedLineEndSizesApi.md#sharedLineendsizesGetId) | **GET** /Shared/LineEndSizes/{id} | LineEndSizes: Get by Id
[**sharedLineendsizesTypeidGetTypeId**](SharedLineEndSizesApi.md#sharedLineendsizesTypeidGetTypeId) | **GET** /Shared/LineEndSizes/TypeId/{type_id} | LineEndSizes: Get By Type Id



## sharedLineendsizesGet

> [SharedLineEndSizes] sharedLineendsizesGet()

LineEndSizes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the LineEndSizes type. Use the Id from oneof the returned elements on to make changes to elements in the Shared object space.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedLineEndSizesApi();
apiInstance.sharedLineendsizesGet((error, data, response) => {
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

[**[SharedLineEndSizes]**](SharedLineEndSizes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## sharedLineendsizesGetId

> SharedLineEndSizes sharedLineendsizesGetId(id)

LineEndSizes: Get by Id

Get by Id: Use this method to retrieve a LineEndSizes object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedLineEndSizesApi();
let id = "id_example"; // String | 
apiInstance.sharedLineendsizesGetId(id, (error, data, response) => {
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

[**SharedLineEndSizes**](SharedLineEndSizes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## sharedLineendsizesTypeidGetTypeId

> SharedLineEndSizes sharedLineendsizesTypeidGetTypeId(typeId)

LineEndSizes: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedLineEndSizesApi();
let typeId = 56; // Number | 
apiInstance.sharedLineendsizesTypeidGetTypeId(typeId, (error, data, response) => {
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

[**SharedLineEndSizes**](SharedLineEndSizes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

