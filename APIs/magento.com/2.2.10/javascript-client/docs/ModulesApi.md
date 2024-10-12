# MagentoB2B.ModulesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backendModuleServiceV1GetModulesGet**](ModulesApi.md#backendModuleServiceV1GetModulesGet) | **GET** /V1/modules | modules



## backendModuleServiceV1GetModulesGet

> [String] backendModuleServiceV1GetModulesGet()

modules

Returns an array of enabled modules

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ModulesApi();
apiInstance.backendModuleServiceV1GetModulesGet((error, data, response) => {
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

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

