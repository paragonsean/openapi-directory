# PiWebApi2018Sp1SwaggerSpec.HomeApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**homeGet**](HomeApi.md#homeGet) | **GET** / | Get top level links for this PI System Web API instance.



## homeGet

> Landing homeGet()

Get top level links for this PI System Web API instance.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.HomeApi();
apiInstance.homeGet((error, data, response) => {
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

[**Landing**](Landing.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application

