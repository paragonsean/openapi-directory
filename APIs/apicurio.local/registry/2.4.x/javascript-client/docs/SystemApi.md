# ApicurioRegistryApiV2.SystemApi

All URIs are relative to *http://apicurio.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getResourceLimits**](SystemApi.md#getResourceLimits) | **GET** /system/limits | Get resource limits information
[**getSystemInfo**](SystemApi.md#getSystemInfo) | **GET** /system/info | Get system information



## getResourceLimits

> Limits getResourceLimits()

Get resource limits information

This operation retrieves the list of limitations on used resources, that are applied on the current instance of Registry.

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.SystemApi();
apiInstance.getResourceLimits((error, data, response) => {
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

[**Limits**](Limits.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSystemInfo

> SystemInfo getSystemInfo()

Get system information

This operation retrieves information about the running registry system, such as the version of the software and when it was built.

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.SystemApi();
apiInstance.getSystemInfo((error, data, response) => {
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

[**SystemInfo**](SystemInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

