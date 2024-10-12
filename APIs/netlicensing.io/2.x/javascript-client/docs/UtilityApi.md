# Labs64NetLicensingResTfulApiTestCenter.UtilityApi

All URIs are relative to *https://go.netlicensing.io/core/v2/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**licenseTypes**](UtilityApi.md#licenseTypes) | **GET** /utility/licenseTypes | List License Types
[**licensingModels**](UtilityApi.md#licensingModels) | **GET** /utility/licensingModels | List Licensing Models



## licenseTypes

> Netlicensing licenseTypes()

List License Types

Return a list of all License Types supported by the service

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.UtilityApi();
apiInstance.licenseTypes((error, data, response) => {
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

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## licensingModels

> Netlicensing licensingModels()

List Licensing Models

Return a list of all licensing models supported by the service

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.UtilityApi();
apiInstance.licensingModels((error, data, response) => {
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

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

