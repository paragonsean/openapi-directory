# OoxmlAutomation.SharedColorTransformationAttributesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedColortransformationattributesGetId**](SharedColorTransformationAttributesApi.md#sharedColortransformationattributesGetId) | **GET** /Shared/ColorTransformationAttributes/{id} | ColorTransformationAttributes: Get by Id



## sharedColortransformationattributesGetId

> SharedColorTransformationAttributes sharedColortransformationattributesGetId(id)

ColorTransformationAttributes: Get by Id

Get by Id: Use this method to retrieve a ColorTransformationAttributes object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedColorTransformationAttributesApi();
let id = "id_example"; // String | 
apiInstance.sharedColortransformationattributesGetId(id, (error, data, response) => {
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

[**SharedColorTransformationAttributes**](SharedColorTransformationAttributes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

