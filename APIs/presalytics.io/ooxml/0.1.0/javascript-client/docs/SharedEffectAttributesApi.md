# OoxmlAutomation.SharedEffectAttributesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedEffectattributesGetId**](SharedEffectAttributesApi.md#sharedEffectattributesGetId) | **GET** /Shared/EffectAttributes/{id} | EffectAttributes: Get by Id



## sharedEffectattributesGetId

> SharedEffectAttributes sharedEffectattributesGetId(id)

EffectAttributes: Get by Id

Get by Id: Use this method to retrieve a EffectAttributes object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedEffectAttributesApi();
let id = "id_example"; // String | 
apiInstance.sharedEffectattributesGetId(id, (error, data, response) => {
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

[**SharedEffectAttributes**](SharedEffectAttributes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

