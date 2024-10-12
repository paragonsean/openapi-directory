# PiWebApi2018Sp1SwaggerSpec.ChannelApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channelInstances**](ChannelApi.md#channelInstances) | **GET** /channels/instances | Retrieves a list of currently running channel instances.



## channelInstances

> ItemsChannelInstance channelInstances()

Retrieves a list of currently running channel instances.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ChannelApi();
apiInstance.channelInstances((error, data, response) => {
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

[**ItemsChannelInstance**](ItemsChannelInstance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application

