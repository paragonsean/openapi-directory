# PiWebApi2018Sp1SwaggerSpec.ConfigurationApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurationDelete**](ConfigurationApi.md#configurationDelete) | **DELETE** /system/configuration/{key} | Delete a configuration item.
[**configurationGet**](ConfigurationApi.md#configurationGet) | **GET** /system/configuration/{key} | Get the value of a configuration item.
[**configurationList**](ConfigurationApi.md#configurationList) | **GET** /system/configuration | Get the current system configuration.



## configurationDelete

> configurationDelete(key)

Delete a configuration item.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ConfigurationApi();
let key = "key_example"; // String | The key of the configuration item to remove.
apiInstance.configurationDelete(key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| The key of the configuration item to remove. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## configurationGet

> Object configurationGet(key)

Get the value of a configuration item.

The response content may vary based on the configuration item&#39;s data type.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ConfigurationApi();
let key = "key_example"; // String | The key of the configuration item.
apiInstance.configurationGet(key, (error, data, response) => {
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
 **key** | **String**| The key of the configuration item. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## configurationList

> {String: Object} configurationList()

Get the current system configuration.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ConfigurationApi();
apiInstance.configurationList((error, data, response) => {
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

**{String: Object}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application

