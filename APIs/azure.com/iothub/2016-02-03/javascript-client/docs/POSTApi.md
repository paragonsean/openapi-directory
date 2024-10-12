# IotHubClient.POSTApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iotHubResourceCheckNameAvailability**](POSTApi.md#iotHubResourceCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Devices/checkNameAvailability | Check if an IoT hub name is available.
[**iotHubResourceExportDevices**](POSTApi.md#iotHubResourceExportDevices) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/exportDevices | Exports all the device identities in the IoT hub identity registry to an Azure Storage blob container. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities.
[**iotHubResourceGetKeysForKeyName**](POSTApi.md#iotHubResourceGetKeysForKeyName) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/IotHubKeys/{keyName}/listkeys | Get a shared access policy by name from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security.
[**iotHubResourceImportDevices**](POSTApi.md#iotHubResourceImportDevices) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/importDevices | Import, update, or delete device identities in the IoT hub identity registry from a blob. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities.
[**iotHubResourceListKeys**](POSTApi.md#iotHubResourceListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/listkeys | Get the security metadata for an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security.



## iotHubResourceCheckNameAvailability

> IotHubNameAvailabilityInfo iotHubResourceCheckNameAvailability(apiVersion, subscriptionId, operationInputs)

Check if an IoT hub name is available.

Check if an IoT hub name is available.

### Example

```javascript
import IotHubClient from 'iot_hub_client';

let apiInstance = new IotHubClient.POSTApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let operationInputs = new IotHubClient.OperationInputs(); // OperationInputs | Set the name parameter in the OperationInputs structure to the name of the IoT hub to check.
apiInstance.iotHubResourceCheckNameAvailability(apiVersion, subscriptionId, operationInputs, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **operationInputs** | [**OperationInputs**](OperationInputs.md)| Set the name parameter in the OperationInputs structure to the name of the IoT hub to check. | 

### Return type

[**IotHubNameAvailabilityInfo**](IotHubNameAvailabilityInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## iotHubResourceExportDevices

> JobResponse iotHubResourceExportDevices(apiVersion, subscriptionId, resourceGroupName, resourceName, exportDevicesParameters)

Exports all the device identities in the IoT hub identity registry to an Azure Storage blob container. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities.

Exports all the device identities in the IoT hub identity registry to an Azure Storage blob container. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities.

### Example

```javascript
import IotHubClient from 'iot_hub_client';

let apiInstance = new IotHubClient.POSTApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
let exportDevicesParameters = new IotHubClient.ExportDevicesRequest(); // ExportDevicesRequest | The parameters that specify the export devices operation.
apiInstance.iotHubResourceExportDevices(apiVersion, subscriptionId, resourceGroupName, resourceName, exportDevicesParameters, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | 
 **resourceName** | **String**| The name of the IoT hub. | 
 **exportDevicesParameters** | [**ExportDevicesRequest**](ExportDevicesRequest.md)| The parameters that specify the export devices operation. | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## iotHubResourceGetKeysForKeyName

> SharedAccessSignatureAuthorizationRule iotHubResourceGetKeysForKeyName(apiVersion, subscriptionId, resourceGroupName, resourceName, keyName)

Get a shared access policy by name from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security.

Get a shared access policy by name from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security.

### Example

```javascript
import IotHubClient from 'iot_hub_client';

let apiInstance = new IotHubClient.POSTApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
let keyName = "keyName_example"; // String | The name of the shared access policy.
apiInstance.iotHubResourceGetKeysForKeyName(apiVersion, subscriptionId, resourceGroupName, resourceName, keyName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | 
 **resourceName** | **String**| The name of the IoT hub. | 
 **keyName** | **String**| The name of the shared access policy. | 

### Return type

[**SharedAccessSignatureAuthorizationRule**](SharedAccessSignatureAuthorizationRule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## iotHubResourceImportDevices

> JobResponse iotHubResourceImportDevices(apiVersion, subscriptionId, resourceGroupName, resourceName, importDevicesParameters)

Import, update, or delete device identities in the IoT hub identity registry from a blob. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities.

Import, update, or delete device identities in the IoT hub identity registry from a blob. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities.

### Example

```javascript
import IotHubClient from 'iot_hub_client';

let apiInstance = new IotHubClient.POSTApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
let importDevicesParameters = new IotHubClient.ImportDevicesRequest(); // ImportDevicesRequest | The parameters that specify the import devices operation.
apiInstance.iotHubResourceImportDevices(apiVersion, subscriptionId, resourceGroupName, resourceName, importDevicesParameters, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | 
 **resourceName** | **String**| The name of the IoT hub. | 
 **importDevicesParameters** | [**ImportDevicesRequest**](ImportDevicesRequest.md)| The parameters that specify the import devices operation. | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## iotHubResourceListKeys

> SharedAccessSignatureAuthorizationRuleListResult iotHubResourceListKeys(apiVersion, subscriptionId, resourceGroupName, resourceName)

Get the security metadata for an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security.

Get the security metadata for an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security.

### Example

```javascript
import IotHubClient from 'iot_hub_client';

let apiInstance = new IotHubClient.POSTApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
apiInstance.iotHubResourceListKeys(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | 
 **resourceName** | **String**| The name of the IoT hub. | 

### Return type

[**SharedAccessSignatureAuthorizationRuleListResult**](SharedAccessSignatureAuthorizationRuleListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

