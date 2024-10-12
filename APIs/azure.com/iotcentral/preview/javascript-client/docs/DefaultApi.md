# AzureIoTCentral.DefaultApi

All URIs are relative to *https://azure.local/api/preview*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTokensGet**](DefaultApi.md#apiTokensGet) | **GET** /apiTokens/{token_id} | Get an API token by ID.
[**apiTokensList**](DefaultApi.md#apiTokensList) | **GET** /apiTokens | Get the list of API tokens in an application.
[**apiTokensRemove**](DefaultApi.md#apiTokensRemove) | **DELETE** /apiTokens/{token_id} | Delete an API token.
[**apiTokensSet**](DefaultApi.md#apiTokensSet) | **PUT** /apiTokens/{token_id} | Create a new API token in the application.
[**continuousDataExportsGet**](DefaultApi.md#continuousDataExportsGet) | **GET** /continuousDataExports/{export_id} | Get a continuous data export by ID.
[**continuousDataExportsList**](DefaultApi.md#continuousDataExportsList) | **GET** /continuousDataExports | Get the list of continuous data exports in an application.
[**continuousDataExportsRemove**](DefaultApi.md#continuousDataExportsRemove) | **DELETE** /continuousDataExports/{export_id} | Delete a continuous data export.
[**continuousDataExportsSet**](DefaultApi.md#continuousDataExportsSet) | **PUT** /continuousDataExports/{export_id} | Create a new continuous data export or update an existing one by ID.
[**deviceTemplatesGet**](DefaultApi.md#deviceTemplatesGet) | **GET** /deviceTemplates/{device_template_id} | Get a device template by ID
[**deviceTemplatesGetMerged**](DefaultApi.md#deviceTemplatesGetMerged) | **GET** /deviceTemplates/{device_template_id}/merged | Get a merged device template by ID
[**deviceTemplatesList**](DefaultApi.md#deviceTemplatesList) | **GET** /deviceTemplates | Get the list of device templates in an application
[**deviceTemplatesListDevices**](DefaultApi.md#deviceTemplatesListDevices) | **GET** /deviceTemplates/{device_template_id}/devices | Get devices for a template
[**deviceTemplatesRemove**](DefaultApi.md#deviceTemplatesRemove) | **DELETE** /deviceTemplates/{device_template_id} | Delete a device template
[**deviceTemplatesSet**](DefaultApi.md#deviceTemplatesSet) | **PUT** /deviceTemplates/{device_template_id} | Create or update a device template by ID
[**devicesExecuteCommand**](DefaultApi.md#devicesExecuteCommand) | **POST** /devices/{device_id}/components/{component_name}/commands/{command_name} | Execute a device command
[**devicesGet**](DefaultApi.md#devicesGet) | **GET** /devices/{device_id} | Get a device by ID
[**devicesGetCloudProperties**](DefaultApi.md#devicesGetCloudProperties) | **GET** /devices/{device_id}/cloudProperties | Get device cloud properties
[**devicesGetCommandHistory**](DefaultApi.md#devicesGetCommandHistory) | **GET** /devices/{device_id}/components/{component_name}/commands/{command_name} | Get device command history
[**devicesGetComponentProperties**](DefaultApi.md#devicesGetComponentProperties) | **GET** /devices/{device_id}/components/{component_name}/properties | Get device properties for a specific component
[**devicesGetCredentials**](DefaultApi.md#devicesGetCredentials) | **GET** /devices/{device_id}/credentials | Get device credentials
[**devicesGetProperties**](DefaultApi.md#devicesGetProperties) | **GET** /devices/{device_id}/properties | Get device properties
[**devicesGetTelemetryValue**](DefaultApi.md#devicesGetTelemetryValue) | **GET** /devices/{device_id}/components/{component_name}/telemetry/{telemetry_name} | Get device telemetry value
[**devicesList**](DefaultApi.md#devicesList) | **GET** /devices | Get the list of devices in an application
[**devicesRemove**](DefaultApi.md#devicesRemove) | **DELETE** /devices/{device_id} | Delete a device
[**devicesSet**](DefaultApi.md#devicesSet) | **PUT** /devices/{device_id} | Create or update a device
[**devicesUpdateCloudProperties**](DefaultApi.md#devicesUpdateCloudProperties) | **PUT** /devices/{device_id}/cloudProperties | Update device cloud properties
[**devicesUpdateComponentProperties**](DefaultApi.md#devicesUpdateComponentProperties) | **PUT** /devices/{device_id}/components/{component_name}/properties | Update device properties for a specific component
[**devicesUpdateProperties**](DefaultApi.md#devicesUpdateProperties) | **PUT** /devices/{device_id}/properties | Update device properties
[**rolesGet**](DefaultApi.md#rolesGet) | **GET** /roles/{role_id} | Get a role by ID.
[**rolesList**](DefaultApi.md#rolesList) | **GET** /roles | Get the list of roles in an application.



## apiTokensGet

> ApiToken apiTokensGet(tokenId)

Get an API token by ID.

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let tokenId = "tokenId_example"; // String | Unique ID for the API token.
apiInstance.apiTokensGet(tokenId, (error, data, response) => {
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
 **tokenId** | **String**| Unique ID for the API token. | 

### Return type

[**ApiToken**](ApiToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiTokensList

> ApiTokenCollection apiTokensList()

Get the list of API tokens in an application.

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
apiInstance.apiTokensList((error, data, response) => {
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

[**ApiTokenCollection**](ApiTokenCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiTokensRemove

> apiTokensRemove(tokenId)

Delete an API token.

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let tokenId = "tokenId_example"; // String | Unique ID for the API token.
apiInstance.apiTokensRemove(tokenId, (error, data, response) => {
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
 **tokenId** | **String**| Unique ID for the API token. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTokensSet

> ApiToken apiTokensSet(tokenId, body)

Create a new API token in the application.

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let tokenId = "tokenId_example"; // String | Unique ID for the API token.
let body = new AzureIoTCentral.ApiToken(); // ApiToken | API token body.
apiInstance.apiTokensSet(tokenId, body, (error, data, response) => {
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
 **tokenId** | **String**| Unique ID for the API token. | 
 **body** | [**ApiToken**](ApiToken.md)| API token body. | 

### Return type

[**ApiToken**](ApiToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## continuousDataExportsGet

> ContinuousDataExport continuousDataExportsGet(exportId)

Get a continuous data export by ID.

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let exportId = "exportId_example"; // String | Unique ID for the continuous data export.
apiInstance.continuousDataExportsGet(exportId, (error, data, response) => {
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
 **exportId** | **String**| Unique ID for the continuous data export. | 

### Return type

[**ContinuousDataExport**](ContinuousDataExport.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## continuousDataExportsList

> ContinuousDataExportCollection continuousDataExportsList()

Get the list of continuous data exports in an application.

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
apiInstance.continuousDataExportsList((error, data, response) => {
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

[**ContinuousDataExportCollection**](ContinuousDataExportCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## continuousDataExportsRemove

> continuousDataExportsRemove(exportId)

Delete a continuous data export.

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let exportId = "exportId_example"; // String | Unique ID for the continuous data export.
apiInstance.continuousDataExportsRemove(exportId, (error, data, response) => {
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
 **exportId** | **String**| Unique ID for the continuous data export. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## continuousDataExportsSet

> ContinuousDataExport continuousDataExportsSet(exportId, body)

Create a new continuous data export or update an existing one by ID.

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let exportId = "exportId_example"; // String | Unique ID for the continuous data export.
let body = new AzureIoTCentral.ContinuousDataExport(); // ContinuousDataExport | Data export body.
apiInstance.continuousDataExportsSet(exportId, body, (error, data, response) => {
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
 **exportId** | **String**| Unique ID for the continuous data export. | 
 **body** | [**ContinuousDataExport**](ContinuousDataExport.md)| Data export body. | 

### Return type

[**ContinuousDataExport**](ContinuousDataExport.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deviceTemplatesGet

> DeviceTemplate deviceTemplatesGet(deviceTemplateId)

Get a device template by ID

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let deviceTemplateId = "deviceTemplateId_example"; // String | Unique ID of the device template.
apiInstance.deviceTemplatesGet(deviceTemplateId, (error, data, response) => {
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
 **deviceTemplateId** | **String**| Unique ID of the device template. | 

### Return type

[**DeviceTemplate**](DeviceTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deviceTemplatesGetMerged

> DeviceTemplate deviceTemplatesGetMerged(deviceTemplateId)

Get a merged device template by ID

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let deviceTemplateId = "deviceTemplateId_example"; // String | Unique ID of the device template.
apiInstance.deviceTemplatesGetMerged(deviceTemplateId, (error, data, response) => {
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
 **deviceTemplateId** | **String**| Unique ID of the device template. | 

### Return type

[**DeviceTemplate**](DeviceTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deviceTemplatesList

> DeviceTemplateCollection deviceTemplatesList()

Get the list of device templates in an application

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
apiInstance.deviceTemplatesList((error, data, response) => {
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

[**DeviceTemplateCollection**](DeviceTemplateCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deviceTemplatesListDevices

> DeviceCollection deviceTemplatesListDevices(deviceTemplateId)

Get devices for a template

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let deviceTemplateId = "deviceTemplateId_example"; // String | Unique ID of the device template.
apiInstance.deviceTemplatesListDevices(deviceTemplateId, (error, data, response) => {
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
 **deviceTemplateId** | **String**| Unique ID of the device template. | 

### Return type

[**DeviceCollection**](DeviceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deviceTemplatesRemove

> deviceTemplatesRemove(deviceTemplateId)

Delete a device template

Delete an existing device template by device ID.

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let deviceTemplateId = "deviceTemplateId_example"; // String | Unique ID of the device template.
apiInstance.deviceTemplatesRemove(deviceTemplateId, (error, data, response) => {
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
 **deviceTemplateId** | **String**| Unique ID of the device template. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deviceTemplatesSet

> DeviceTemplate deviceTemplatesSet(deviceTemplateId, body)

Create or update a device template by ID

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let deviceTemplateId = "deviceTemplateId_example"; // String | Unique ID of the device template.
let body = new AzureIoTCentral.DeviceTemplate(); // DeviceTemplate | Device template body.
apiInstance.deviceTemplatesSet(deviceTemplateId, body, (error, data, response) => {
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
 **deviceTemplateId** | **String**| Unique ID of the device template. | 
 **body** | [**DeviceTemplate**](DeviceTemplate.md)| Device template body. | 

### Return type

[**DeviceTemplate**](DeviceTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## devicesExecuteCommand

> DeviceCommand devicesExecuteCommand(deviceId, componentName, commandName, body)

Execute a device command

Execute a command on a device.

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let deviceId = "deviceId_example"; // String | Unique ID of the device.
let componentName = "componentName_example"; // String | Name of the device component.
let commandName = "commandName_example"; // String | Name of this device command.
let body = new AzureIoTCentral.DeviceCommand(); // DeviceCommand | Device command body.
apiInstance.devicesExecuteCommand(deviceId, componentName, commandName, body, (error, data, response) => {
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
 **deviceId** | **String**| Unique ID of the device. | 
 **componentName** | **String**| Name of the device component. | 
 **commandName** | **String**| Name of this device command. | 
 **body** | [**DeviceCommand**](DeviceCommand.md)| Device command body. | 

### Return type

[**DeviceCommand**](DeviceCommand.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## devicesGet

> Device devicesGet(deviceId)

Get a device by ID

Get details about an existing device by device ID.

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let deviceId = "deviceId_example"; // String | Unique ID of the device.
apiInstance.devicesGet(deviceId, (error, data, response) => {
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
 **deviceId** | **String**| Unique ID of the device. | 

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesGetCloudProperties

> {String: Object} devicesGetCloudProperties(deviceId)

Get device cloud properties

Get all cloud property values of a device by device ID.

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let deviceId = "deviceId_example"; // String | Unique ID of the device.
apiInstance.devicesGetCloudProperties(deviceId, (error, data, response) => {
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
 **deviceId** | **String**| Unique ID of the device. | 

### Return type

**{String: Object}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesGetCommandHistory

> DeviceCommandCollection devicesGetCommandHistory(deviceId, componentName, commandName)

Get device command history

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let deviceId = "deviceId_example"; // String | Unique ID of the device.
let componentName = "componentName_example"; // String | Name of the device component.
let commandName = "commandName_example"; // String | Name of this device command.
apiInstance.devicesGetCommandHistory(deviceId, componentName, commandName, (error, data, response) => {
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
 **deviceId** | **String**| Unique ID of the device. | 
 **componentName** | **String**| Name of the device component. | 
 **commandName** | **String**| Name of this device command. | 

### Return type

[**DeviceCommandCollection**](DeviceCommandCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesGetComponentProperties

> {String: Object} devicesGetComponentProperties(deviceId, componentName)

Get device properties for a specific component

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let deviceId = "deviceId_example"; // String | Unique ID of the device.
let componentName = "componentName_example"; // String | Name of the device component.
apiInstance.devicesGetComponentProperties(deviceId, componentName, (error, data, response) => {
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
 **deviceId** | **String**| Unique ID of the device. | 
 **componentName** | **String**| Name of the device component. | 

### Return type

**{String: Object}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesGetCredentials

> DeviceCredentials devicesGetCredentials(deviceId)

Get device credentials

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let deviceId = "deviceId_example"; // String | Unique ID of the device.
apiInstance.devicesGetCredentials(deviceId, (error, data, response) => {
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
 **deviceId** | **String**| Unique ID of the device. | 

### Return type

[**DeviceCredentials**](DeviceCredentials.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesGetProperties

> {String: Object} devicesGetProperties(deviceId)

Get device properties

Get all property values of a device by device ID.

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let deviceId = "deviceId_example"; // String | Unique ID of the device.
apiInstance.devicesGetProperties(deviceId, (error, data, response) => {
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
 **deviceId** | **String**| Unique ID of the device. | 

### Return type

**{String: Object}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesGetTelemetryValue

> Value devicesGetTelemetryValue(deviceId, componentName, telemetryName)

Get device telemetry value

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let deviceId = "deviceId_example"; // String | Unique ID of the device.
let componentName = "componentName_example"; // String | Name of the device component.
let telemetryName = "telemetryName_example"; // String | Name of this device telemetry.
apiInstance.devicesGetTelemetryValue(deviceId, componentName, telemetryName, (error, data, response) => {
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
 **deviceId** | **String**| Unique ID of the device. | 
 **componentName** | **String**| Name of the device component. | 
 **telemetryName** | **String**| Name of this device telemetry. | 

### Return type

[**Value**](Value.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesList

> DeviceCollection devicesList()

Get the list of devices in an application

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
apiInstance.devicesList((error, data, response) => {
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

[**DeviceCollection**](DeviceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesRemove

> devicesRemove(deviceId)

Delete a device

Delete an existing device by device ID.

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let deviceId = "deviceId_example"; // String | Unique ID of the device.
apiInstance.devicesRemove(deviceId, (error, data, response) => {
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
 **deviceId** | **String**| Unique ID of the device. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## devicesSet

> Device devicesSet(deviceId, body)

Create or update a device

Create a new device or update an existing one by device ID.

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let deviceId = "deviceId_example"; // String | Unique ID of the device.
let body = new AzureIoTCentral.Device(); // Device | Device body.
apiInstance.devicesSet(deviceId, body, (error, data, response) => {
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
 **deviceId** | **String**| Unique ID of the device. | 
 **body** | [**Device**](Device.md)| Device body. | 

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## devicesUpdateCloudProperties

> {String: Object} devicesUpdateCloudProperties(deviceId, body)

Update device cloud properties

Update all cloud property values of a device by device ID.

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let deviceId = "deviceId_example"; // String | Unique ID of the device.
let body = {key: null}; // {String: Object} | Device properties.
apiInstance.devicesUpdateCloudProperties(deviceId, body, (error, data, response) => {
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
 **deviceId** | **String**| Unique ID of the device. | 
 **body** | [**{String: Object}**](Object.md)| Device properties. | 

### Return type

**{String: Object}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## devicesUpdateComponentProperties

> {String: Object} devicesUpdateComponentProperties(deviceId, componentName, body)

Update device properties for a specific component

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let deviceId = "deviceId_example"; // String | Unique ID of the device.
let componentName = "componentName_example"; // String | Name of the device component.
let body = {key: null}; // {String: Object} | Device properties.
apiInstance.devicesUpdateComponentProperties(deviceId, componentName, body, (error, data, response) => {
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
 **deviceId** | **String**| Unique ID of the device. | 
 **componentName** | **String**| Name of the device component. | 
 **body** | [**{String: Object}**](Object.md)| Device properties. | 

### Return type

**{String: Object}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## devicesUpdateProperties

> {String: Object} devicesUpdateProperties(deviceId, body)

Update device properties

Update all property values of a device by device ID.

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let deviceId = "deviceId_example"; // String | Unique ID of the device.
let body = {key: null}; // {String: Object} | Device properties.
apiInstance.devicesUpdateProperties(deviceId, body, (error, data, response) => {
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
 **deviceId** | **String**| Unique ID of the device. | 
 **body** | [**{String: Object}**](Object.md)| Device properties. | 

### Return type

**{String: Object}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## rolesGet

> Role rolesGet(roleId)

Get a role by ID.

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
let roleId = "roleId_example"; // String | Unique ID for the role.
apiInstance.rolesGet(roleId, (error, data, response) => {
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
 **roleId** | **String**| Unique ID for the role. | 

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rolesList

> RoleCollection rolesList()

Get the list of roles in an application.

### Example

```javascript
import AzureIoTCentral from 'azure_io_t_central';

let apiInstance = new AzureIoTCentral.DefaultApi();
apiInstance.rolesList((error, data, response) => {
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

[**RoleCollection**](RoleCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

