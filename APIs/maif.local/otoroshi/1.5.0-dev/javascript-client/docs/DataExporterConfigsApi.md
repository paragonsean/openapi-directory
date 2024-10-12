# OtoroshiAdminApi.DataExporterConfigsApi

All URIs are relative to *http://otoroshi-api.oto.tools*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBulkDataExporterConfigs**](DataExporterConfigsApi.md#createBulkDataExporterConfigs) | **POST** /api/data-exporter-configs/_bulk | Create a new data exporter configs
[**createDataExporterConfig**](DataExporterConfigsApi.md#createDataExporterConfig) | **POST** /api/data-exporter-configs | Create a new data exporter config
[**dataExporterTemplate**](DataExporterConfigsApi.md#dataExporterTemplate) | **GET** /api/data-exporter-configs/_template | Get all data exporter configs
[**deleteDataExporterConfig**](DataExporterConfigsApi.md#deleteDataExporterConfig) | **DELETE** /api/data-exporter-configs/{dataExporterConfigId} | Delete a data exporter config
[**deletebulkDataExporterConfig**](DataExporterConfigsApi.md#deletebulkDataExporterConfig) | **DELETE** /api/data-exporter-configs/_bulk | Delete a data exporter config
[**findAllDataExporters**](DataExporterConfigsApi.md#findAllDataExporters) | **GET** /api/data-exporter-configs | Get all data exporter configs
[**findDataExporterConfigById**](DataExporterConfigsApi.md#findDataExporterConfigById) | **GET** /api/data-exporter-configs/{dataExporterConfigId} | Get a data exporter config
[**patchBulkDataExporterConfig**](DataExporterConfigsApi.md#patchBulkDataExporterConfig) | **PATCH** /api/data-exporter-configs/_bulk | Update a data exporter configs with a diff
[**patchDataExporterConfig**](DataExporterConfigsApi.md#patchDataExporterConfig) | **PATCH** /api/data-exporter-configs/{dataExporterConfigId} | Update a data exporter config with a diff
[**updateBulkDataExporterConfig**](DataExporterConfigsApi.md#updateBulkDataExporterConfig) | **PUT** /api/data-exporter-configs/_bulk | Update a data exporter configs
[**updateDataExporterConfig**](DataExporterConfigsApi.md#updateDataExporterConfig) | **PUT** /api/data-exporter-configs/{dataExporterConfigId} | Update a data exporter config



## createBulkDataExporterConfigs

> [CreateBulkDataExporterConfigs200ResponseInner] createBulkDataExporterConfigs(opts)

Create a new data exporter configs

Create a new data exporter configs

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.DataExporterConfigsApi();
let opts = {
  'dataExporterConfig': new OtoroshiAdminApi.DataExporterConfig() // DataExporterConfig | 
};
apiInstance.createBulkDataExporterConfigs(opts, (error, data, response) => {
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
 **dataExporterConfig** | [**DataExporterConfig**](DataExporterConfig.md)|  | [optional] 

### Return type

[**[CreateBulkDataExporterConfigs200ResponseInner]**](CreateBulkDataExporterConfigs200ResponseInner.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/ndjson
- **Accept**: application/json


## createDataExporterConfig

> DataExporterConfig createDataExporterConfig(opts)

Create a new data exporter config

Create a new data exporter config

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.DataExporterConfigsApi();
let opts = {
  'dataExporterConfig': new OtoroshiAdminApi.DataExporterConfig() // DataExporterConfig | 
};
apiInstance.createDataExporterConfig(opts, (error, data, response) => {
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
 **dataExporterConfig** | [**DataExporterConfig**](DataExporterConfig.md)|  | [optional] 

### Return type

[**DataExporterConfig**](DataExporterConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dataExporterTemplate

> DataExporterConfig dataExporterTemplate(opts)

Get all data exporter configs

Get all data exporter configs

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.DataExporterConfigsApi();
let opts = {
  'type': "type_example" // String | The data exporter config type
};
apiInstance.dataExporterTemplate(opts, (error, data, response) => {
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
 **type** | **String**| The data exporter config type | [optional] 

### Return type

[**DataExporterConfig**](DataExporterConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDataExporterConfig

> Deleted deleteDataExporterConfig(dataExporterConfigId)

Delete a data exporter config

Delete a data exporter config

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.DataExporterConfigsApi();
let dataExporterConfigId = "dataExporterConfigId_example"; // String | The data exporter config id
apiInstance.deleteDataExporterConfig(dataExporterConfigId, (error, data, response) => {
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
 **dataExporterConfigId** | **String**| The data exporter config id | 

### Return type

[**Deleted**](Deleted.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletebulkDataExporterConfig

> [DeletebulkDataExporterConfig200ResponseInner] deletebulkDataExporterConfig(opts)

Delete a data exporter config

Delete a data exporter config

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.DataExporterConfigsApi();
let opts = {
  'patchInner': [new OtoroshiAdminApi.PatchInner()] // [PatchInner] | 
};
apiInstance.deletebulkDataExporterConfig(opts, (error, data, response) => {
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
 **patchInner** | [**[PatchInner]**](PatchInner.md)|  | [optional] 

### Return type

[**[DeletebulkDataExporterConfig200ResponseInner]**](DeletebulkDataExporterConfig200ResponseInner.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/ndjson
- **Accept**: application/json


## findAllDataExporters

> [DataExporterConfig] findAllDataExporters()

Get all data exporter configs

Get all data exporter configs

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.DataExporterConfigsApi();
apiInstance.findAllDataExporters((error, data, response) => {
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

[**[DataExporterConfig]**](DataExporterConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findDataExporterConfigById

> DataExporterConfig findDataExporterConfigById(dataExporterConfigId)

Get a data exporter config

Get a data exporter config

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.DataExporterConfigsApi();
let dataExporterConfigId = "dataExporterConfigId_example"; // String | The data exporter config id
apiInstance.findDataExporterConfigById(dataExporterConfigId, (error, data, response) => {
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
 **dataExporterConfigId** | **String**| The data exporter config id | 

### Return type

[**DataExporterConfig**](DataExporterConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchBulkDataExporterConfig

> [UpdateBulkDataExporterConfig200ResponseInner] patchBulkDataExporterConfig(opts)

Update a data exporter configs with a diff

Update a data exporter configs with a diff

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.DataExporterConfigsApi();
let opts = {
  'patchInner': [new OtoroshiAdminApi.PatchInner()] // [PatchInner] | 
};
apiInstance.patchBulkDataExporterConfig(opts, (error, data, response) => {
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
 **patchInner** | [**[PatchInner]**](PatchInner.md)|  | [optional] 

### Return type

[**[UpdateBulkDataExporterConfig200ResponseInner]**](UpdateBulkDataExporterConfig200ResponseInner.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/ndjson
- **Accept**: application/json


## patchDataExporterConfig

> DataExporterConfig patchDataExporterConfig(dataExporterConfigId, opts)

Update a data exporter config with a diff

Update a data exporter config with a diff

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.DataExporterConfigsApi();
let dataExporterConfigId = "dataExporterConfigId_example"; // String | The data exporter config id
let opts = {
  'patchInner': [new OtoroshiAdminApi.PatchInner()] // [PatchInner] | 
};
apiInstance.patchDataExporterConfig(dataExporterConfigId, opts, (error, data, response) => {
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
 **dataExporterConfigId** | **String**| The data exporter config id | 
 **patchInner** | [**[PatchInner]**](PatchInner.md)|  | [optional] 

### Return type

[**DataExporterConfig**](DataExporterConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBulkDataExporterConfig

> [UpdateBulkDataExporterConfig200ResponseInner] updateBulkDataExporterConfig(opts)

Update a data exporter configs

Update a data exporter configs

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.DataExporterConfigsApi();
let opts = {
  'dataExporterConfig': new OtoroshiAdminApi.DataExporterConfig() // DataExporterConfig | 
};
apiInstance.updateBulkDataExporterConfig(opts, (error, data, response) => {
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
 **dataExporterConfig** | [**DataExporterConfig**](DataExporterConfig.md)|  | [optional] 

### Return type

[**[UpdateBulkDataExporterConfig200ResponseInner]**](UpdateBulkDataExporterConfig200ResponseInner.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/ndjson
- **Accept**: application/json


## updateDataExporterConfig

> DataExporterConfig updateDataExporterConfig(dataExporterConfigId, opts)

Update a data exporter config

Update a data exporter config

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.DataExporterConfigsApi();
let dataExporterConfigId = "dataExporterConfigId_example"; // String | The data exporter config id
let opts = {
  'dataExporterConfig': new OtoroshiAdminApi.DataExporterConfig() // DataExporterConfig | 
};
apiInstance.updateDataExporterConfig(dataExporterConfigId, opts, (error, data, response) => {
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
 **dataExporterConfigId** | **String**| The data exporter config id | 
 **dataExporterConfig** | [**DataExporterConfig**](DataExporterConfig.md)|  | [optional] 

### Return type

[**DataExporterConfig**](DataExporterConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

