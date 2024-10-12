# OoxmlAutomation.SharedEffectsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedEffectsGetId**](SharedEffectsApi.md#sharedEffectsGetId) | **GET** /Shared/Effects/{id} | Effects: Get by Id



## sharedEffectsGetId

> SharedEffects sharedEffectsGetId(id)

Effects: Get by Id

Get by Id: Use this method to retrieve a Effects object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedEffectsApi();
let id = "id_example"; // String | 
apiInstance.sharedEffectsGetId(id, (error, data, response) => {
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

[**SharedEffects**](SharedEffects.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

