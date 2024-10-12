# Wellknown.PluginsApi

All URIs are relative to *https://wellknown.ai/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getProvider**](PluginsApi.md#getProvider) | **GET** /plugins | List all the Wellknown AI Plugins.



## getProvider

> getProvider()

List all the Wellknown AI Plugins.

List all the Wellknown AI Plugins. Returns ai-plugin.json objects in an array

### Example

```javascript
import Wellknown from 'wellknown';

let apiInstance = new Wellknown.PluginsApi();
apiInstance.getProvider((error, data, response) => {
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

