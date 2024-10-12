# Wellknown.DefaultApi

All URIs are relative to *https://wellknown.ai/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPluginsGet**](DefaultApi.md#apiPluginsGet) | **GET** /api/plugins | 



## apiPluginsGet

> apiPluginsGet()



Returns a list of Wellknown ai-plugins json objects from the Wellknown ai-plugins registry.

### Example

```javascript
import Wellknown from 'wellknown';

let apiInstance = new Wellknown.DefaultApi();
apiInstance.apiPluginsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

