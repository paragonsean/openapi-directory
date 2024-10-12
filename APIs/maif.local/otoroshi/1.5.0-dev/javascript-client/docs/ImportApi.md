# OtoroshiAdminApi.ImportApi

All URIs are relative to *http://otoroshi-api.oto.tools*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fullExport**](ImportApi.md#fullExport) | **GET** /api/otoroshi.json | Export the full state of Otoroshi
[**fullImport**](ImportApi.md#fullImport) | **POST** /api/otoroshi.json | Import the full state of Otoroshi
[**fullImportFromFile**](ImportApi.md#fullImportFromFile) | **POST** /api/import | Import the full state of Otoroshi as a file



## fullExport

> ImportExport fullExport()

Export the full state of Otoroshi

Export the full state of Otoroshi

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ImportApi();
apiInstance.fullExport((error, data, response) => {
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

[**ImportExport**](ImportExport.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fullImport

> Done fullImport(opts)

Import the full state of Otoroshi

Import the full state of Otoroshi

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ImportApi();
let opts = {
  'importExport': new OtoroshiAdminApi.ImportExport() // ImportExport | 
};
apiInstance.fullImport(opts, (error, data, response) => {
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
 **importExport** | [**ImportExport**](ImportExport.md)|  | [optional] 

### Return type

[**Done**](Done.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## fullImportFromFile

> Done fullImportFromFile(opts)

Import the full state of Otoroshi as a file

Import the full state of Otoroshi as a file

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ImportApi();
let opts = {
  'importExport': new OtoroshiAdminApi.ImportExport() // ImportExport | 
};
apiInstance.fullImportFromFile(opts, (error, data, response) => {
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
 **importExport** | [**ImportExport**](ImportExport.md)|  | [optional] 

### Return type

[**Done**](Done.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

