# BioLinkApi.IdentifierMapperApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getIdentifierMapper**](IdentifierMapperApi.md#getIdentifierMapper) | **GET** /identifier/mapper/{source}/{target}/ | TODO maps a list of identifiers from a source to a target



## getIdentifierMapper

> [Association] getIdentifierMapper(source, target)

TODO maps a list of identifiers from a source to a target

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.IdentifierMapperApi();
let source = "source_example"; // String | 
let target = "target_example"; // String | 
apiInstance.getIdentifierMapper(source, target, (error, data, response) => {
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
 **source** | **String**|  | 
 **target** | **String**|  | 

### Return type

[**[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

