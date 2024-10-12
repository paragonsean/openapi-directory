# IotHubClient.POSTApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iotHubManualFailover**](POSTApi.md#iotHubManualFailover) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{iotHubName}/failover | Manually initiate a failover for the IoT Hub to its secondary region
[**iotHubResourceCheckNameAvailability**](POSTApi.md#iotHubResourceCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Devices/checkNameAvailability | Check if an IoT hub name is available
[**iotHubResourceExportDevices**](POSTApi.md#iotHubResourceExportDevices) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/exportDevices | Exports all the device identities in the IoT hub identity registry to an Azure Storage blob container. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities
[**iotHubResourceGetKeysForKeyName**](POSTApi.md#iotHubResourceGetKeysForKeyName) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/IotHubKeys/{keyName}/listkeys | Get a shared access policy by name from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security
[**iotHubResourceImportDevices**](POSTApi.md#iotHubResourceImportDevices) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/importDevices | Import, update, or delete device identities in the IoT hub identity registry from a blob. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities
[**iotHubResourceListKeys**](POSTApi.md#iotHubResourceListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/listkeys | Get the security metadata for an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security
[**iotHubResourceTestAllRoutes**](POSTApi.md#iotHubResourceTestAllRoutes) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{iotHubName}/routing/routes/$testall | Test all routes
[**iotHubResourceTestRoute**](POSTApi.md#iotHubResourceTestRoute) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{iotHubName}/routing/routes/$testnew | Test the new route



## iotHubManualFailover

> iotHubManualFailover(iotHubName, subscriptionId, resourceGroupName, apiVersion, failoverInput)

Manually initiate a failover for the IoT Hub to its secondary region

Manually initiate a failover for the IoT Hub to its secondary region. To learn more, see https://aka.ms/manualfailover

### Example

```javascript
import IotHubClient from 'iot_hub_client';
let defaultClient = IotHubClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotHubClient.POSTApi();
let iotHubName = "iotHubName_example"; // String | Name of the IoT hub to failover
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group containing the IoT hub resource
let apiVersion = "apiVersion_example"; // String | The version of the API.
let failoverInput = new IotHubClient.FailoverInput(); // FailoverInput | Region to failover to. Must be the Azure paired region. Get the value from the secondary location in the locations property. To learn more, see https://aka.ms/manualfailover/region
apiInstance.iotHubManualFailover(iotHubName, subscriptionId, resourceGroupName, apiVersion, failoverInput, (error, data, response) => {
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
 **iotHubName** | **String**| Name of the IoT hub to failover | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| Name of the resource group containing the IoT hub resource | 
 **apiVersion** | **String**| The version of the API. | 
 **failoverInput** | [**FailoverInput**](FailoverInput.md)| Region to failover to. Must be the Azure paired region. Get the value from the secondary location in the locations property. To learn more, see https://aka.ms/manualfailover/region | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## iotHubResourceCheckNameAvailability

> IotHubNameAvailabilityInfo iotHubResourceCheckNameAvailability(apiVersion, subscriptionId, operationInputs)

Check if an IoT hub name is available

Check if an IoT hub name is available.

### Example

```javascript
import IotHubClient from 'iot_hub_client';
let defaultClient = IotHubClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

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

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## iotHubResourceExportDevices

> JobResponse iotHubResourceExportDevices(apiVersion, subscriptionId, resourceGroupName, resourceName, exportDevicesParameters)

Exports all the device identities in the IoT hub identity registry to an Azure Storage blob container. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities

Exports all the device identities in the IoT hub identity registry to an Azure Storage blob container. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities.

### Example

```javascript
import IotHubClient from 'iot_hub_client';
let defaultClient = IotHubClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

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

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## iotHubResourceGetKeysForKeyName

> SharedAccessSignatureAuthorizationRule iotHubResourceGetKeysForKeyName(apiVersion, subscriptionId, resourceGroupName, resourceName, keyName)

Get a shared access policy by name from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security

Get a shared access policy by name from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security.

### Example

```javascript
import IotHubClient from 'iot_hub_client';
let defaultClient = IotHubClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

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

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iotHubResourceImportDevices

> JobResponse iotHubResourceImportDevices(apiVersion, subscriptionId, resourceGroupName, resourceName, importDevicesParameters)

Import, update, or delete device identities in the IoT hub identity registry from a blob. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities

Import, update, or delete device identities in the IoT hub identity registry from a blob. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities.

### Example

```javascript
import IotHubClient from 'iot_hub_client';
let defaultClient = IotHubClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

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

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## iotHubResourceListKeys

> SharedAccessSignatureAuthorizationRuleListResult iotHubResourceListKeys(apiVersion, subscriptionId, resourceGroupName, resourceName)

Get the security metadata for an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security

Get the security metadata for an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security.

### Example

```javascript
import IotHubClient from 'iot_hub_client';
let defaultClient = IotHubClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

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

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iotHubResourceTestAllRoutes

> TestAllRoutesResult iotHubResourceTestAllRoutes(iotHubName, subscriptionId, resourceGroupName, apiVersion, input)

Test all routes

Test all routes configured in this Iot Hub

### Example

```javascript
import IotHubClient from 'iot_hub_client';
let defaultClient = IotHubClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotHubClient.POSTApi();
let iotHubName = "iotHubName_example"; // String | IotHub to be tested
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | resource group which Iot Hub belongs to
let apiVersion = "apiVersion_example"; // String | The version of the API.
let input = new IotHubClient.TestAllRoutesInput(); // TestAllRoutesInput | Input for testing all routes
apiInstance.iotHubResourceTestAllRoutes(iotHubName, subscriptionId, resourceGroupName, apiVersion, input, (error, data, response) => {
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
 **iotHubName** | **String**| IotHub to be tested | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| resource group which Iot Hub belongs to | 
 **apiVersion** | **String**| The version of the API. | 
 **input** | [**TestAllRoutesInput**](TestAllRoutesInput.md)| Input for testing all routes | 

### Return type

[**TestAllRoutesResult**](TestAllRoutesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## iotHubResourceTestRoute

> TestRouteResult iotHubResourceTestRoute(iotHubName, subscriptionId, resourceGroupName, apiVersion, input)

Test the new route

Test the new route for this Iot Hub

### Example

```javascript
import IotHubClient from 'iot_hub_client';
let defaultClient = IotHubClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotHubClient.POSTApi();
let iotHubName = "iotHubName_example"; // String | IotHub to be tested
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | resource group which Iot Hub belongs to
let apiVersion = "apiVersion_example"; // String | The version of the API.
let input = new IotHubClient.TestRouteInput(); // TestRouteInput | Route that needs to be tested
apiInstance.iotHubResourceTestRoute(iotHubName, subscriptionId, resourceGroupName, apiVersion, input, (error, data, response) => {
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
 **iotHubName** | **String**| IotHub to be tested | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| resource group which Iot Hub belongs to | 
 **apiVersion** | **String**| The version of the API. | 
 **input** | [**TestRouteInput**](TestRouteInput.md)| Route that needs to be tested | 

### Return type

[**TestRouteResult**](TestRouteResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

