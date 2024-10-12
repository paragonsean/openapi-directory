# AwsIoTWireless.DefaultApi

All URIs are relative to *http://api.iotwireless.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateAwsAccountWithPartnerAccount**](DefaultApi.md#associateAwsAccountWithPartnerAccount) | **POST** /partner-accounts | 
[**associateMulticastGroupWithFuotaTask**](DefaultApi.md#associateMulticastGroupWithFuotaTask) | **PUT** /fuota-tasks/{Id}/multicast-group | 
[**associateWirelessDeviceWithFuotaTask**](DefaultApi.md#associateWirelessDeviceWithFuotaTask) | **PUT** /fuota-tasks/{Id}/wireless-device | 
[**associateWirelessDeviceWithMulticastGroup**](DefaultApi.md#associateWirelessDeviceWithMulticastGroup) | **PUT** /multicast-groups/{Id}/wireless-device | 
[**associateWirelessDeviceWithThing**](DefaultApi.md#associateWirelessDeviceWithThing) | **PUT** /wireless-devices/{Id}/thing | 
[**associateWirelessGatewayWithCertificate**](DefaultApi.md#associateWirelessGatewayWithCertificate) | **PUT** /wireless-gateways/{Id}/certificate | 
[**associateWirelessGatewayWithThing**](DefaultApi.md#associateWirelessGatewayWithThing) | **PUT** /wireless-gateways/{Id}/thing | 
[**cancelMulticastGroupSession**](DefaultApi.md#cancelMulticastGroupSession) | **DELETE** /multicast-groups/{Id}/session | 
[**createDestination**](DefaultApi.md#createDestination) | **POST** /destinations | 
[**createDeviceProfile**](DefaultApi.md#createDeviceProfile) | **POST** /device-profiles | 
[**createFuotaTask**](DefaultApi.md#createFuotaTask) | **POST** /fuota-tasks | 
[**createMulticastGroup**](DefaultApi.md#createMulticastGroup) | **POST** /multicast-groups | 
[**createNetworkAnalyzerConfiguration**](DefaultApi.md#createNetworkAnalyzerConfiguration) | **POST** /network-analyzer-configurations | 
[**createServiceProfile**](DefaultApi.md#createServiceProfile) | **POST** /service-profiles | 
[**createWirelessDevice**](DefaultApi.md#createWirelessDevice) | **POST** /wireless-devices | 
[**createWirelessGateway**](DefaultApi.md#createWirelessGateway) | **POST** /wireless-gateways | 
[**createWirelessGatewayTask**](DefaultApi.md#createWirelessGatewayTask) | **POST** /wireless-gateways/{Id}/tasks | 
[**createWirelessGatewayTaskDefinition**](DefaultApi.md#createWirelessGatewayTaskDefinition) | **POST** /wireless-gateway-task-definitions | 
[**deleteDestination**](DefaultApi.md#deleteDestination) | **DELETE** /destinations/{Name} | 
[**deleteDeviceProfile**](DefaultApi.md#deleteDeviceProfile) | **DELETE** /device-profiles/{Id} | 
[**deleteFuotaTask**](DefaultApi.md#deleteFuotaTask) | **DELETE** /fuota-tasks/{Id} | 
[**deleteMulticastGroup**](DefaultApi.md#deleteMulticastGroup) | **DELETE** /multicast-groups/{Id} | 
[**deleteNetworkAnalyzerConfiguration**](DefaultApi.md#deleteNetworkAnalyzerConfiguration) | **DELETE** /network-analyzer-configurations/{ConfigurationName} | 
[**deleteQueuedMessages**](DefaultApi.md#deleteQueuedMessages) | **DELETE** /wireless-devices/{Id}/data#messageId | 
[**deleteServiceProfile**](DefaultApi.md#deleteServiceProfile) | **DELETE** /service-profiles/{Id} | 
[**deleteWirelessDevice**](DefaultApi.md#deleteWirelessDevice) | **DELETE** /wireless-devices/{Id} | 
[**deleteWirelessDeviceImportTask**](DefaultApi.md#deleteWirelessDeviceImportTask) | **DELETE** /wireless_device_import_task/{Id} | 
[**deleteWirelessGateway**](DefaultApi.md#deleteWirelessGateway) | **DELETE** /wireless-gateways/{Id} | 
[**deleteWirelessGatewayTask**](DefaultApi.md#deleteWirelessGatewayTask) | **DELETE** /wireless-gateways/{Id}/tasks | 
[**deleteWirelessGatewayTaskDefinition**](DefaultApi.md#deleteWirelessGatewayTaskDefinition) | **DELETE** /wireless-gateway-task-definitions/{Id} | 
[**deregisterWirelessDevice**](DefaultApi.md#deregisterWirelessDevice) | **PATCH** /wireless-devices/{Identifier}/deregister | 
[**disassociateAwsAccountFromPartnerAccount**](DefaultApi.md#disassociateAwsAccountFromPartnerAccount) | **DELETE** /partner-accounts/{PartnerAccountId}#partnerType | 
[**disassociateMulticastGroupFromFuotaTask**](DefaultApi.md#disassociateMulticastGroupFromFuotaTask) | **DELETE** /fuota-tasks/{Id}/multicast-groups/{MulticastGroupId} | 
[**disassociateWirelessDeviceFromFuotaTask**](DefaultApi.md#disassociateWirelessDeviceFromFuotaTask) | **DELETE** /fuota-tasks/{Id}/wireless-devices/{WirelessDeviceId} | 
[**disassociateWirelessDeviceFromMulticastGroup**](DefaultApi.md#disassociateWirelessDeviceFromMulticastGroup) | **DELETE** /multicast-groups/{Id}/wireless-devices/{WirelessDeviceId} | 
[**disassociateWirelessDeviceFromThing**](DefaultApi.md#disassociateWirelessDeviceFromThing) | **DELETE** /wireless-devices/{Id}/thing | 
[**disassociateWirelessGatewayFromCertificate**](DefaultApi.md#disassociateWirelessGatewayFromCertificate) | **DELETE** /wireless-gateways/{Id}/certificate | 
[**disassociateWirelessGatewayFromThing**](DefaultApi.md#disassociateWirelessGatewayFromThing) | **DELETE** /wireless-gateways/{Id}/thing | 
[**getDestination**](DefaultApi.md#getDestination) | **GET** /destinations/{Name} | 
[**getDeviceProfile**](DefaultApi.md#getDeviceProfile) | **GET** /device-profiles/{Id} | 
[**getEventConfigurationByResourceTypes**](DefaultApi.md#getEventConfigurationByResourceTypes) | **GET** /event-configurations-resource-types | 
[**getFuotaTask**](DefaultApi.md#getFuotaTask) | **GET** /fuota-tasks/{Id} | 
[**getLogLevelsByResourceTypes**](DefaultApi.md#getLogLevelsByResourceTypes) | **GET** /log-levels | 
[**getMulticastGroup**](DefaultApi.md#getMulticastGroup) | **GET** /multicast-groups/{Id} | 
[**getMulticastGroupSession**](DefaultApi.md#getMulticastGroupSession) | **GET** /multicast-groups/{Id}/session | 
[**getNetworkAnalyzerConfiguration**](DefaultApi.md#getNetworkAnalyzerConfiguration) | **GET** /network-analyzer-configurations/{ConfigurationName} | 
[**getPartnerAccount**](DefaultApi.md#getPartnerAccount) | **GET** /partner-accounts/{PartnerAccountId}#partnerType | 
[**getPosition**](DefaultApi.md#getPosition) | **GET** /positions/{ResourceIdentifier}#resourceType | 
[**getPositionConfiguration**](DefaultApi.md#getPositionConfiguration) | **GET** /position-configurations/{ResourceIdentifier}#resourceType | 
[**getPositionEstimate**](DefaultApi.md#getPositionEstimate) | **POST** /position-estimate | 
[**getResourceEventConfiguration**](DefaultApi.md#getResourceEventConfiguration) | **GET** /event-configurations/{Identifier}#identifierType | 
[**getResourceLogLevel**](DefaultApi.md#getResourceLogLevel) | **GET** /log-levels/{ResourceIdentifier}#resourceType | 
[**getResourcePosition**](DefaultApi.md#getResourcePosition) | **GET** /resource-positions/{ResourceIdentifier}#resourceType | 
[**getServiceEndpoint**](DefaultApi.md#getServiceEndpoint) | **GET** /service-endpoint | 
[**getServiceProfile**](DefaultApi.md#getServiceProfile) | **GET** /service-profiles/{Id} | 
[**getWirelessDevice**](DefaultApi.md#getWirelessDevice) | **GET** /wireless-devices/{Identifier}#identifierType | 
[**getWirelessDeviceImportTask**](DefaultApi.md#getWirelessDeviceImportTask) | **GET** /wireless_device_import_task/{Id} | 
[**getWirelessDeviceStatistics**](DefaultApi.md#getWirelessDeviceStatistics) | **GET** /wireless-devices/{Id}/statistics | 
[**getWirelessGateway**](DefaultApi.md#getWirelessGateway) | **GET** /wireless-gateways/{Identifier}#identifierType | 
[**getWirelessGatewayCertificate**](DefaultApi.md#getWirelessGatewayCertificate) | **GET** /wireless-gateways/{Id}/certificate | 
[**getWirelessGatewayFirmwareInformation**](DefaultApi.md#getWirelessGatewayFirmwareInformation) | **GET** /wireless-gateways/{Id}/firmware-information | 
[**getWirelessGatewayStatistics**](DefaultApi.md#getWirelessGatewayStatistics) | **GET** /wireless-gateways/{Id}/statistics | 
[**getWirelessGatewayTask**](DefaultApi.md#getWirelessGatewayTask) | **GET** /wireless-gateways/{Id}/tasks | 
[**getWirelessGatewayTaskDefinition**](DefaultApi.md#getWirelessGatewayTaskDefinition) | **GET** /wireless-gateway-task-definitions/{Id} | 
[**listDestinations**](DefaultApi.md#listDestinations) | **GET** /destinations | 
[**listDeviceProfiles**](DefaultApi.md#listDeviceProfiles) | **GET** /device-profiles | 
[**listDevicesForWirelessDeviceImportTask**](DefaultApi.md#listDevicesForWirelessDeviceImportTask) | **GET** /wireless_device_import_task#id | 
[**listEventConfigurations**](DefaultApi.md#listEventConfigurations) | **GET** /event-configurations#resourceType | 
[**listFuotaTasks**](DefaultApi.md#listFuotaTasks) | **GET** /fuota-tasks | 
[**listMulticastGroups**](DefaultApi.md#listMulticastGroups) | **GET** /multicast-groups | 
[**listMulticastGroupsByFuotaTask**](DefaultApi.md#listMulticastGroupsByFuotaTask) | **GET** /fuota-tasks/{Id}/multicast-groups | 
[**listNetworkAnalyzerConfigurations**](DefaultApi.md#listNetworkAnalyzerConfigurations) | **GET** /network-analyzer-configurations | 
[**listPartnerAccounts**](DefaultApi.md#listPartnerAccounts) | **GET** /partner-accounts | 
[**listPositionConfigurations**](DefaultApi.md#listPositionConfigurations) | **GET** /position-configurations | 
[**listQueuedMessages**](DefaultApi.md#listQueuedMessages) | **GET** /wireless-devices/{Id}/data | 
[**listServiceProfiles**](DefaultApi.md#listServiceProfiles) | **GET** /service-profiles | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags#resourceArn | 
[**listWirelessDeviceImportTasks**](DefaultApi.md#listWirelessDeviceImportTasks) | **GET** /wireless_device_import_tasks | 
[**listWirelessDevices**](DefaultApi.md#listWirelessDevices) | **GET** /wireless-devices | 
[**listWirelessGatewayTaskDefinitions**](DefaultApi.md#listWirelessGatewayTaskDefinitions) | **GET** /wireless-gateway-task-definitions | 
[**listWirelessGateways**](DefaultApi.md#listWirelessGateways) | **GET** /wireless-gateways | 
[**putPositionConfiguration**](DefaultApi.md#putPositionConfiguration) | **PUT** /position-configurations/{ResourceIdentifier}#resourceType | 
[**putResourceLogLevel**](DefaultApi.md#putResourceLogLevel) | **PUT** /log-levels/{ResourceIdentifier}#resourceType | 
[**resetAllResourceLogLevels**](DefaultApi.md#resetAllResourceLogLevels) | **DELETE** /log-levels | 
[**resetResourceLogLevel**](DefaultApi.md#resetResourceLogLevel) | **DELETE** /log-levels/{ResourceIdentifier}#resourceType | 
[**sendDataToMulticastGroup**](DefaultApi.md#sendDataToMulticastGroup) | **POST** /multicast-groups/{Id}/data | 
[**sendDataToWirelessDevice**](DefaultApi.md#sendDataToWirelessDevice) | **POST** /wireless-devices/{Id}/data | 
[**startBulkAssociateWirelessDeviceWithMulticastGroup**](DefaultApi.md#startBulkAssociateWirelessDeviceWithMulticastGroup) | **PATCH** /multicast-groups/{Id}/bulk | 
[**startBulkDisassociateWirelessDeviceFromMulticastGroup**](DefaultApi.md#startBulkDisassociateWirelessDeviceFromMulticastGroup) | **POST** /multicast-groups/{Id}/bulk | 
[**startFuotaTask**](DefaultApi.md#startFuotaTask) | **PUT** /fuota-tasks/{Id} | 
[**startMulticastGroupSession**](DefaultApi.md#startMulticastGroupSession) | **PUT** /multicast-groups/{Id}/session | 
[**startSingleWirelessDeviceImportTask**](DefaultApi.md#startSingleWirelessDeviceImportTask) | **POST** /wireless_single_device_import_task | 
[**startWirelessDeviceImportTask**](DefaultApi.md#startWirelessDeviceImportTask) | **POST** /wireless_device_import_task | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags#resourceArn | 
[**testWirelessDevice**](DefaultApi.md#testWirelessDevice) | **POST** /wireless-devices/{Id}/test | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags#resourceArn&amp;tagKeys | 
[**updateDestination**](DefaultApi.md#updateDestination) | **PATCH** /destinations/{Name} | 
[**updateEventConfigurationByResourceTypes**](DefaultApi.md#updateEventConfigurationByResourceTypes) | **PATCH** /event-configurations-resource-types | 
[**updateFuotaTask**](DefaultApi.md#updateFuotaTask) | **PATCH** /fuota-tasks/{Id} | 
[**updateLogLevelsByResourceTypes**](DefaultApi.md#updateLogLevelsByResourceTypes) | **POST** /log-levels | 
[**updateMulticastGroup**](DefaultApi.md#updateMulticastGroup) | **PATCH** /multicast-groups/{Id} | 
[**updateNetworkAnalyzerConfiguration**](DefaultApi.md#updateNetworkAnalyzerConfiguration) | **PATCH** /network-analyzer-configurations/{ConfigurationName} | 
[**updatePartnerAccount**](DefaultApi.md#updatePartnerAccount) | **PATCH** /partner-accounts/{PartnerAccountId}#partnerType | 
[**updatePosition**](DefaultApi.md#updatePosition) | **PATCH** /positions/{ResourceIdentifier}#resourceType | 
[**updateResourceEventConfiguration**](DefaultApi.md#updateResourceEventConfiguration) | **PATCH** /event-configurations/{Identifier}#identifierType | 
[**updateResourcePosition**](DefaultApi.md#updateResourcePosition) | **PATCH** /resource-positions/{ResourceIdentifier}#resourceType | 
[**updateWirelessDevice**](DefaultApi.md#updateWirelessDevice) | **PATCH** /wireless-devices/{Id} | 
[**updateWirelessDeviceImportTask**](DefaultApi.md#updateWirelessDeviceImportTask) | **PATCH** /wireless_device_import_task/{Id} | 
[**updateWirelessGateway**](DefaultApi.md#updateWirelessGateway) | **PATCH** /wireless-gateways/{Id} | 



## associateAwsAccountWithPartnerAccount

> AssociateAwsAccountWithPartnerAccountResponse associateAwsAccountWithPartnerAccount(associateAwsAccountWithPartnerAccountRequest, opts)



Associates a partner account with your AWS account.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let associateAwsAccountWithPartnerAccountRequest = new AwsIoTWireless.AssociateAwsAccountWithPartnerAccountRequest(); // AssociateAwsAccountWithPartnerAccountRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateAwsAccountWithPartnerAccount(associateAwsAccountWithPartnerAccountRequest, opts, (error, data, response) => {
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
 **associateAwsAccountWithPartnerAccountRequest** | [**AssociateAwsAccountWithPartnerAccountRequest**](AssociateAwsAccountWithPartnerAccountRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AssociateAwsAccountWithPartnerAccountResponse**](AssociateAwsAccountWithPartnerAccountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associateMulticastGroupWithFuotaTask

> Object associateMulticastGroupWithFuotaTask(id, associateMulticastGroupWithFuotaTaskRequest, opts)



Associate a multicast group with a FUOTA task.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | 
let associateMulticastGroupWithFuotaTaskRequest = new AwsIoTWireless.AssociateMulticastGroupWithFuotaTaskRequest(); // AssociateMulticastGroupWithFuotaTaskRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateMulticastGroupWithFuotaTask(id, associateMulticastGroupWithFuotaTaskRequest, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **associateMulticastGroupWithFuotaTaskRequest** | [**AssociateMulticastGroupWithFuotaTaskRequest**](AssociateMulticastGroupWithFuotaTaskRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associateWirelessDeviceWithFuotaTask

> Object associateWirelessDeviceWithFuotaTask(id, associateWirelessDeviceWithFuotaTaskRequest, opts)



Associate a wireless device with a FUOTA task.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | 
let associateWirelessDeviceWithFuotaTaskRequest = new AwsIoTWireless.AssociateWirelessDeviceWithFuotaTaskRequest(); // AssociateWirelessDeviceWithFuotaTaskRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateWirelessDeviceWithFuotaTask(id, associateWirelessDeviceWithFuotaTaskRequest, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **associateWirelessDeviceWithFuotaTaskRequest** | [**AssociateWirelessDeviceWithFuotaTaskRequest**](AssociateWirelessDeviceWithFuotaTaskRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associateWirelessDeviceWithMulticastGroup

> Object associateWirelessDeviceWithMulticastGroup(id, associateWirelessDeviceWithFuotaTaskRequest, opts)



Associates a wireless device with a multicast group.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | 
let associateWirelessDeviceWithFuotaTaskRequest = new AwsIoTWireless.AssociateWirelessDeviceWithFuotaTaskRequest(); // AssociateWirelessDeviceWithFuotaTaskRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateWirelessDeviceWithMulticastGroup(id, associateWirelessDeviceWithFuotaTaskRequest, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **associateWirelessDeviceWithFuotaTaskRequest** | [**AssociateWirelessDeviceWithFuotaTaskRequest**](AssociateWirelessDeviceWithFuotaTaskRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associateWirelessDeviceWithThing

> Object associateWirelessDeviceWithThing(id, associateWirelessDeviceWithThingRequest, opts)



Associates a wireless device with a thing.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to update.
let associateWirelessDeviceWithThingRequest = new AwsIoTWireless.AssociateWirelessDeviceWithThingRequest(); // AssociateWirelessDeviceWithThingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateWirelessDeviceWithThing(id, associateWirelessDeviceWithThingRequest, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to update. | 
 **associateWirelessDeviceWithThingRequest** | [**AssociateWirelessDeviceWithThingRequest**](AssociateWirelessDeviceWithThingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associateWirelessGatewayWithCertificate

> AssociateWirelessGatewayWithCertificateResponse associateWirelessGatewayWithCertificate(id, associateWirelessGatewayWithCertificateRequest, opts)



Associates a wireless gateway with a certificate.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to update.
let associateWirelessGatewayWithCertificateRequest = new AwsIoTWireless.AssociateWirelessGatewayWithCertificateRequest(); // AssociateWirelessGatewayWithCertificateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateWirelessGatewayWithCertificate(id, associateWirelessGatewayWithCertificateRequest, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to update. | 
 **associateWirelessGatewayWithCertificateRequest** | [**AssociateWirelessGatewayWithCertificateRequest**](AssociateWirelessGatewayWithCertificateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AssociateWirelessGatewayWithCertificateResponse**](AssociateWirelessGatewayWithCertificateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associateWirelessGatewayWithThing

> Object associateWirelessGatewayWithThing(id, associateWirelessGatewayWithThingRequest, opts)



Associates a wireless gateway with a thing.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to update.
let associateWirelessGatewayWithThingRequest = new AwsIoTWireless.AssociateWirelessGatewayWithThingRequest(); // AssociateWirelessGatewayWithThingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateWirelessGatewayWithThing(id, associateWirelessGatewayWithThingRequest, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to update. | 
 **associateWirelessGatewayWithThingRequest** | [**AssociateWirelessGatewayWithThingRequest**](AssociateWirelessGatewayWithThingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cancelMulticastGroupSession

> Object cancelMulticastGroupSession(id, opts)



Cancels an existing multicast group session.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.cancelMulticastGroupSession(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createDestination

> CreateDestinationResponse createDestination(createDestinationRequest, opts)



Creates a new destination that maps a device message to an AWS IoT rule.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let createDestinationRequest = new AwsIoTWireless.CreateDestinationRequest(); // CreateDestinationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDestination(createDestinationRequest, opts, (error, data, response) => {
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
 **createDestinationRequest** | [**CreateDestinationRequest**](CreateDestinationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateDestinationResponse**](CreateDestinationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDeviceProfile

> CreateDeviceProfileResponse createDeviceProfile(createDeviceProfileRequest, opts)



Creates a new device profile.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let createDeviceProfileRequest = new AwsIoTWireless.CreateDeviceProfileRequest(); // CreateDeviceProfileRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDeviceProfile(createDeviceProfileRequest, opts, (error, data, response) => {
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
 **createDeviceProfileRequest** | [**CreateDeviceProfileRequest**](CreateDeviceProfileRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateDeviceProfileResponse**](CreateDeviceProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createFuotaTask

> CreateFuotaTaskResponse createFuotaTask(createFuotaTaskRequest, opts)



Creates a FUOTA task.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let createFuotaTaskRequest = new AwsIoTWireless.CreateFuotaTaskRequest(); // CreateFuotaTaskRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createFuotaTask(createFuotaTaskRequest, opts, (error, data, response) => {
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
 **createFuotaTaskRequest** | [**CreateFuotaTaskRequest**](CreateFuotaTaskRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateFuotaTaskResponse**](CreateFuotaTaskResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMulticastGroup

> CreateMulticastGroupResponse createMulticastGroup(createMulticastGroupRequest, opts)



Creates a multicast group.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let createMulticastGroupRequest = new AwsIoTWireless.CreateMulticastGroupRequest(); // CreateMulticastGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMulticastGroup(createMulticastGroupRequest, opts, (error, data, response) => {
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
 **createMulticastGroupRequest** | [**CreateMulticastGroupRequest**](CreateMulticastGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMulticastGroupResponse**](CreateMulticastGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkAnalyzerConfiguration

> CreateNetworkAnalyzerConfigurationResponse createNetworkAnalyzerConfiguration(createNetworkAnalyzerConfigurationRequest, opts)



Creates a new network analyzer configuration.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let createNetworkAnalyzerConfigurationRequest = new AwsIoTWireless.CreateNetworkAnalyzerConfigurationRequest(); // CreateNetworkAnalyzerConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createNetworkAnalyzerConfiguration(createNetworkAnalyzerConfigurationRequest, opts, (error, data, response) => {
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
 **createNetworkAnalyzerConfigurationRequest** | [**CreateNetworkAnalyzerConfigurationRequest**](CreateNetworkAnalyzerConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateNetworkAnalyzerConfigurationResponse**](CreateNetworkAnalyzerConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createServiceProfile

> CreateServiceProfileResponse createServiceProfile(createServiceProfileRequest, opts)



Creates a new service profile.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let createServiceProfileRequest = new AwsIoTWireless.CreateServiceProfileRequest(); // CreateServiceProfileRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createServiceProfile(createServiceProfileRequest, opts, (error, data, response) => {
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
 **createServiceProfileRequest** | [**CreateServiceProfileRequest**](CreateServiceProfileRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateServiceProfileResponse**](CreateServiceProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createWirelessDevice

> CreateWirelessDeviceResponse createWirelessDevice(createWirelessDeviceRequest, opts)



Provisions a wireless device.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let createWirelessDeviceRequest = new AwsIoTWireless.CreateWirelessDeviceRequest(); // CreateWirelessDeviceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createWirelessDevice(createWirelessDeviceRequest, opts, (error, data, response) => {
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
 **createWirelessDeviceRequest** | [**CreateWirelessDeviceRequest**](CreateWirelessDeviceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateWirelessDeviceResponse**](CreateWirelessDeviceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createWirelessGateway

> CreateWirelessGatewayResponse createWirelessGateway(createWirelessGatewayRequest, opts)



Provisions a wireless gateway.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let createWirelessGatewayRequest = new AwsIoTWireless.CreateWirelessGatewayRequest(); // CreateWirelessGatewayRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createWirelessGateway(createWirelessGatewayRequest, opts, (error, data, response) => {
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
 **createWirelessGatewayRequest** | [**CreateWirelessGatewayRequest**](CreateWirelessGatewayRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateWirelessGatewayResponse**](CreateWirelessGatewayResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createWirelessGatewayTask

> CreateWirelessGatewayTaskResponse createWirelessGatewayTask(id, createWirelessGatewayTaskRequest, opts)



Creates a task for a wireless gateway.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to update.
let createWirelessGatewayTaskRequest = new AwsIoTWireless.CreateWirelessGatewayTaskRequest(); // CreateWirelessGatewayTaskRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createWirelessGatewayTask(id, createWirelessGatewayTaskRequest, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to update. | 
 **createWirelessGatewayTaskRequest** | [**CreateWirelessGatewayTaskRequest**](CreateWirelessGatewayTaskRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateWirelessGatewayTaskResponse**](CreateWirelessGatewayTaskResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createWirelessGatewayTaskDefinition

> CreateWirelessGatewayTaskDefinitionResponse createWirelessGatewayTaskDefinition(createWirelessGatewayTaskDefinitionRequest, opts)



Creates a gateway task definition.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let createWirelessGatewayTaskDefinitionRequest = new AwsIoTWireless.CreateWirelessGatewayTaskDefinitionRequest(); // CreateWirelessGatewayTaskDefinitionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createWirelessGatewayTaskDefinition(createWirelessGatewayTaskDefinitionRequest, opts, (error, data, response) => {
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
 **createWirelessGatewayTaskDefinitionRequest** | [**CreateWirelessGatewayTaskDefinitionRequest**](CreateWirelessGatewayTaskDefinitionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateWirelessGatewayTaskDefinitionResponse**](CreateWirelessGatewayTaskDefinitionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDestination

> Object deleteDestination(name, opts)



Deletes a destination.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let name = "name_example"; // String | The name of the resource to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteDestination(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the resource to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDeviceProfile

> Object deleteDeviceProfile(id, opts)



Deletes a device profile.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteDeviceProfile(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteFuotaTask

> Object deleteFuotaTask(id, opts)



Deletes a FUOTA task.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteFuotaTask(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteMulticastGroup

> Object deleteMulticastGroup(id, opts)



Deletes a multicast group if it is not in use by a fuota task.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMulticastGroup(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteNetworkAnalyzerConfiguration

> Object deleteNetworkAnalyzerConfiguration(configurationName, opts)



Deletes a network analyzer configuration.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let configurationName = "configurationName_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteNetworkAnalyzerConfiguration(configurationName, opts, (error, data, response) => {
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
 **configurationName** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteQueuedMessages

> Object deleteQueuedMessages(id, messageId, opts)



Remove queued messages from the downlink queue.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of a given wireless device for which downlink messages will be deleted.
let messageId = "messageId_example"; // String | If message ID is <code>\"*\"</code>, it cleares the entire downlink queue for a given device, specified by the wireless device ID. Otherwise, the downlink message with the specified message ID will be deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'wirelessDeviceType': "wirelessDeviceType_example" // String | The wireless device type, which can be either Sidewalk or LoRaWAN.
};
apiInstance.deleteQueuedMessages(id, messageId, opts, (error, data, response) => {
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
 **id** | **String**| The ID of a given wireless device for which downlink messages will be deleted. | 
 **messageId** | **String**| If message ID is &lt;code&gt;\&quot;*\&quot;&lt;/code&gt;, it cleares the entire downlink queue for a given device, specified by the wireless device ID. Otherwise, the downlink message with the specified message ID will be deleted. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **wirelessDeviceType** | **String**| The wireless device type, which can be either Sidewalk or LoRaWAN. | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteServiceProfile

> Object deleteServiceProfile(id, opts)



Deletes a service profile.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteServiceProfile(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteWirelessDevice

> Object deleteWirelessDevice(id, opts)



Deletes a wireless device.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteWirelessDevice(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteWirelessDeviceImportTask

> Object deleteWirelessDeviceImportTask(id, opts)



Delete an import task.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The unique identifier of the import task to be deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteWirelessDeviceImportTask(id, opts, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the import task to be deleted. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteWirelessGateway

> Object deleteWirelessGateway(id, opts)



Deletes a wireless gateway.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteWirelessGateway(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteWirelessGatewayTask

> Object deleteWirelessGatewayTask(id, opts)



Deletes a wireless gateway task.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteWirelessGatewayTask(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteWirelessGatewayTaskDefinition

> Object deleteWirelessGatewayTaskDefinition(id, opts)



Deletes a wireless gateway task definition. Deleting this task definition does not affect tasks that are currently in progress.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteWirelessGatewayTaskDefinition(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deregisterWirelessDevice

> Object deregisterWirelessDevice(identifier, opts)



Deregister a wireless device from AWS IoT Wireless.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let identifier = "identifier_example"; // String | The identifier of the wireless device to deregister from AWS IoT Wireless.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'wirelessDeviceType': "wirelessDeviceType_example" // String | The type of wireless device to deregister from AWS IoT Wireless, which can be <code>LoRaWAN</code> or <code>Sidewalk</code>.
};
apiInstance.deregisterWirelessDevice(identifier, opts, (error, data, response) => {
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
 **identifier** | **String**| The identifier of the wireless device to deregister from AWS IoT Wireless. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **wirelessDeviceType** | **String**| The type of wireless device to deregister from AWS IoT Wireless, which can be &lt;code&gt;LoRaWAN&lt;/code&gt; or &lt;code&gt;Sidewalk&lt;/code&gt;. | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateAwsAccountFromPartnerAccount

> Object disassociateAwsAccountFromPartnerAccount(partnerAccountId, partnerType, opts)



Disassociates your AWS account from a partner account. If &lt;code&gt;PartnerAccountId&lt;/code&gt; and &lt;code&gt;PartnerType&lt;/code&gt; are &lt;code&gt;null&lt;/code&gt;, disassociates your AWS account from all partner accounts.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let partnerAccountId = "partnerAccountId_example"; // String | The partner account ID to disassociate from the AWS account.
let partnerType = "partnerType_example"; // String | The partner type.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateAwsAccountFromPartnerAccount(partnerAccountId, partnerType, opts, (error, data, response) => {
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
 **partnerAccountId** | **String**| The partner account ID to disassociate from the AWS account. | 
 **partnerType** | **String**| The partner type. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateMulticastGroupFromFuotaTask

> Object disassociateMulticastGroupFromFuotaTask(id, multicastGroupId, opts)



Disassociates a multicast group from a fuota task.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | 
let multicastGroupId = "multicastGroupId_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateMulticastGroupFromFuotaTask(id, multicastGroupId, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **multicastGroupId** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateWirelessDeviceFromFuotaTask

> Object disassociateWirelessDeviceFromFuotaTask(id, wirelessDeviceId, opts)



Disassociates a wireless device from a FUOTA task.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | 
let wirelessDeviceId = "wirelessDeviceId_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateWirelessDeviceFromFuotaTask(id, wirelessDeviceId, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **wirelessDeviceId** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateWirelessDeviceFromMulticastGroup

> Object disassociateWirelessDeviceFromMulticastGroup(id, wirelessDeviceId, opts)



Disassociates a wireless device from a multicast group.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | 
let wirelessDeviceId = "wirelessDeviceId_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateWirelessDeviceFromMulticastGroup(id, wirelessDeviceId, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **wirelessDeviceId** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateWirelessDeviceFromThing

> Object disassociateWirelessDeviceFromThing(id, opts)



Disassociates a wireless device from its currently associated thing.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to update.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateWirelessDeviceFromThing(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to update. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateWirelessGatewayFromCertificate

> Object disassociateWirelessGatewayFromCertificate(id, opts)



Disassociates a wireless gateway from its currently associated certificate.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to update.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateWirelessGatewayFromCertificate(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to update. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateWirelessGatewayFromThing

> Object disassociateWirelessGatewayFromThing(id, opts)



Disassociates a wireless gateway from its currently associated thing.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to update.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateWirelessGatewayFromThing(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to update. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDestination

> GetDestinationResponse getDestination(name, opts)



Gets information about a destination.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let name = "name_example"; // String | The name of the resource to get.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDestination(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the resource to get. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDestinationResponse**](GetDestinationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceProfile

> GetDeviceProfileResponse getDeviceProfile(id, opts)



Gets information about a device profile.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to get.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDeviceProfile(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to get. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDeviceProfileResponse**](GetDeviceProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventConfigurationByResourceTypes

> GetEventConfigurationByResourceTypesResponse getEventConfigurationByResourceTypes(opts)



Get the event configuration based on resource types.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getEventConfigurationByResourceTypes(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetEventConfigurationByResourceTypesResponse**](GetEventConfigurationByResourceTypesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFuotaTask

> GetFuotaTaskResponse getFuotaTask(id, opts)



Gets information about a FUOTA task.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getFuotaTask(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetFuotaTaskResponse**](GetFuotaTaskResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLogLevelsByResourceTypes

> GetLogLevelsByResourceTypesResponse getLogLevelsByResourceTypes(opts)



Returns current default log levels or log levels by resource types. Based on resource types, log levels can be for wireless device log options or wireless gateway log options.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getLogLevelsByResourceTypes(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetLogLevelsByResourceTypesResponse**](GetLogLevelsByResourceTypesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMulticastGroup

> GetMulticastGroupResponse getMulticastGroup(id, opts)



Gets information about a multicast group.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMulticastGroup(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMulticastGroupResponse**](GetMulticastGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMulticastGroupSession

> GetMulticastGroupSessionResponse getMulticastGroupSession(id, opts)



Gets information about a multicast group session.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMulticastGroupSession(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMulticastGroupSessionResponse**](GetMulticastGroupSessionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkAnalyzerConfiguration

> GetNetworkAnalyzerConfigurationResponse getNetworkAnalyzerConfiguration(configurationName, opts)



Get network analyzer configuration.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let configurationName = "configurationName_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getNetworkAnalyzerConfiguration(configurationName, opts, (error, data, response) => {
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
 **configurationName** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetNetworkAnalyzerConfigurationResponse**](GetNetworkAnalyzerConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPartnerAccount

> GetPartnerAccountResponse getPartnerAccount(partnerAccountId, partnerType, opts)



Gets information about a partner account. If &lt;code&gt;PartnerAccountId&lt;/code&gt; and &lt;code&gt;PartnerType&lt;/code&gt; are &lt;code&gt;null&lt;/code&gt;, returns all partner accounts.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let partnerAccountId = "partnerAccountId_example"; // String | The partner account ID to disassociate from the AWS account.
let partnerType = "partnerType_example"; // String | The partner type.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPartnerAccount(partnerAccountId, partnerType, opts, (error, data, response) => {
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
 **partnerAccountId** | **String**| The partner account ID to disassociate from the AWS account. | 
 **partnerType** | **String**| The partner type. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPartnerAccountResponse**](GetPartnerAccountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPosition

> GetPositionResponse getPosition(resourceIdentifier, resourceType, opts)



&lt;p&gt;Get the position information for a given resource.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This action is no longer supported. Calls to retrieve the position information should use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_GetResourcePosition.html\&quot;&gt;GetResourcePosition&lt;/a&gt; API operation instead.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let resourceIdentifier = "resourceIdentifier_example"; // String | Resource identifier used to retrieve the position information.
let resourceType = "resourceType_example"; // String | Resource type of the resource for which position information is retrieved.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPosition(resourceIdentifier, resourceType, opts, (error, data, response) => {
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
 **resourceIdentifier** | **String**| Resource identifier used to retrieve the position information. | 
 **resourceType** | **String**| Resource type of the resource for which position information is retrieved. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPositionResponse**](GetPositionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPositionConfiguration

> GetPositionConfigurationResponse getPositionConfiguration(resourceIdentifier, resourceType, opts)



&lt;p&gt;Get position configuration for a given resource.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This action is no longer supported. Calls to retrieve the position configuration should use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_GetResourcePosition.html\&quot;&gt;GetResourcePosition&lt;/a&gt; API operation instead.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let resourceIdentifier = "resourceIdentifier_example"; // String | Resource identifier used in a position configuration.
let resourceType = "resourceType_example"; // String | Resource type of the resource for which position configuration is retrieved.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPositionConfiguration(resourceIdentifier, resourceType, opts, (error, data, response) => {
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
 **resourceIdentifier** | **String**| Resource identifier used in a position configuration. | 
 **resourceType** | **String**| Resource type of the resource for which position configuration is retrieved. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPositionConfigurationResponse**](GetPositionConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPositionEstimate

> GetPositionEstimateResponse getPositionEstimate(getPositionEstimateRequest, opts)



Get estimated position information as a payload in GeoJSON format. The payload measurement data is resolved using solvers that are provided by third-party vendors.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let getPositionEstimateRequest = new AwsIoTWireless.GetPositionEstimateRequest(); // GetPositionEstimateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPositionEstimate(getPositionEstimateRequest, opts, (error, data, response) => {
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
 **getPositionEstimateRequest** | [**GetPositionEstimateRequest**](GetPositionEstimateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPositionEstimateResponse**](GetPositionEstimateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getResourceEventConfiguration

> GetResourceEventConfigurationResponse getResourceEventConfiguration(identifier, identifierType, opts)



Get the event configuration for a particular resource identifier.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let identifier = "identifier_example"; // String | Resource identifier to opt in for event messaging.
let identifierType = "identifierType_example"; // String | Identifier type of the particular resource identifier for event configuration.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'partnerType': "partnerType_example" // String | Partner type of the resource if the identifier type is <code>PartnerAccountId</code>.
};
apiInstance.getResourceEventConfiguration(identifier, identifierType, opts, (error, data, response) => {
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
 **identifier** | **String**| Resource identifier to opt in for event messaging. | 
 **identifierType** | **String**| Identifier type of the particular resource identifier for event configuration. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **partnerType** | **String**| Partner type of the resource if the identifier type is &lt;code&gt;PartnerAccountId&lt;/code&gt;. | [optional] 

### Return type

[**GetResourceEventConfigurationResponse**](GetResourceEventConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getResourceLogLevel

> GetResourceLogLevelResponse getResourceLogLevel(resourceIdentifier, resourceType, opts)



Fetches the log-level override, if any, for a given resource-ID and resource-type. It can be used for a wireless device or a wireless gateway.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let resourceIdentifier = "resourceIdentifier_example"; // String | 
let resourceType = "resourceType_example"; // String | The type of the resource, which can be <code>WirelessDevice</code> or <code>WirelessGateway</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getResourceLogLevel(resourceIdentifier, resourceType, opts, (error, data, response) => {
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
 **resourceIdentifier** | **String**|  | 
 **resourceType** | **String**| The type of the resource, which can be &lt;code&gt;WirelessDevice&lt;/code&gt; or &lt;code&gt;WirelessGateway&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetResourceLogLevelResponse**](GetResourceLogLevelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getResourcePosition

> GetResourcePositionResponse getResourcePosition(resourceIdentifier, resourceType, opts)



Get the position information for a given wireless device or a wireless gateway resource. The position information uses the &lt;a href&#x3D;\&quot;https://gisgeography.com/wgs84-world-geodetic-system/\&quot;&gt; World Geodetic System (WGS84)&lt;/a&gt;.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let resourceIdentifier = "resourceIdentifier_example"; // String | The identifier of the resource for which position information is retrieved. It can be the wireless device ID or the wireless gateway ID, depending on the resource type.
let resourceType = "resourceType_example"; // String | The type of resource for which position information is retrieved, which can be a wireless device or a wireless gateway.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getResourcePosition(resourceIdentifier, resourceType, opts, (error, data, response) => {
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
 **resourceIdentifier** | **String**| The identifier of the resource for which position information is retrieved. It can be the wireless device ID or the wireless gateway ID, depending on the resource type. | 
 **resourceType** | **String**| The type of resource for which position information is retrieved, which can be a wireless device or a wireless gateway. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetResourcePositionResponse**](GetResourcePositionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServiceEndpoint

> GetServiceEndpointResponse getServiceEndpoint(opts)



Gets the account-specific endpoint for Configuration and Update Server (CUPS) protocol or LoRaWAN Network Server (LNS) connections.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'serviceType': "serviceType_example" // String | The service type for which to get endpoint information about. Can be <code>CUPS</code> for the Configuration and Update Server endpoint, or <code>LNS</code> for the LoRaWAN Network Server endpoint or <code>CLAIM</code> for the global endpoint.
};
apiInstance.getServiceEndpoint(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **serviceType** | **String**| The service type for which to get endpoint information about. Can be &lt;code&gt;CUPS&lt;/code&gt; for the Configuration and Update Server endpoint, or &lt;code&gt;LNS&lt;/code&gt; for the LoRaWAN Network Server endpoint or &lt;code&gt;CLAIM&lt;/code&gt; for the global endpoint. | [optional] 

### Return type

[**GetServiceEndpointResponse**](GetServiceEndpointResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServiceProfile

> GetServiceProfileResponse getServiceProfile(id, opts)



Gets information about a service profile.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to get.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getServiceProfile(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to get. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetServiceProfileResponse**](GetServiceProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWirelessDevice

> GetWirelessDeviceResponse getWirelessDevice(identifier, identifierType, opts)



Gets information about a wireless device.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let identifier = "identifier_example"; // String | The identifier of the wireless device to get.
let identifierType = "identifierType_example"; // String | The type of identifier used in <code>identifier</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getWirelessDevice(identifier, identifierType, opts, (error, data, response) => {
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
 **identifier** | **String**| The identifier of the wireless device to get. | 
 **identifierType** | **String**| The type of identifier used in &lt;code&gt;identifier&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetWirelessDeviceResponse**](GetWirelessDeviceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWirelessDeviceImportTask

> GetWirelessDeviceImportTaskResponse getWirelessDeviceImportTask(id, opts)



Get information about an import task and count of device onboarding summary information for the import task.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The identifier of the import task for which information is requested.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getWirelessDeviceImportTask(id, opts, (error, data, response) => {
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
 **id** | **String**| The identifier of the import task for which information is requested. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetWirelessDeviceImportTaskResponse**](GetWirelessDeviceImportTaskResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWirelessDeviceStatistics

> GetWirelessDeviceStatisticsResponse getWirelessDeviceStatistics(id, opts)



Gets operating information about a wireless device.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the wireless device for which to get the data.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getWirelessDeviceStatistics(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the wireless device for which to get the data. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetWirelessDeviceStatisticsResponse**](GetWirelessDeviceStatisticsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWirelessGateway

> GetWirelessGatewayResponse getWirelessGateway(identifier, identifierType, opts)



Gets information about a wireless gateway.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let identifier = "identifier_example"; // String | The identifier of the wireless gateway to get.
let identifierType = "identifierType_example"; // String | The type of identifier used in <code>identifier</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getWirelessGateway(identifier, identifierType, opts, (error, data, response) => {
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
 **identifier** | **String**| The identifier of the wireless gateway to get. | 
 **identifierType** | **String**| The type of identifier used in &lt;code&gt;identifier&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetWirelessGatewayResponse**](GetWirelessGatewayResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWirelessGatewayCertificate

> GetWirelessGatewayCertificateResponse getWirelessGatewayCertificate(id, opts)



Gets the ID of the certificate that is currently associated with a wireless gateway.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to get.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getWirelessGatewayCertificate(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to get. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetWirelessGatewayCertificateResponse**](GetWirelessGatewayCertificateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWirelessGatewayFirmwareInformation

> GetWirelessGatewayFirmwareInformationResponse getWirelessGatewayFirmwareInformation(id, opts)



Gets the firmware version and other information about a wireless gateway.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to get.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getWirelessGatewayFirmwareInformation(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to get. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetWirelessGatewayFirmwareInformationResponse**](GetWirelessGatewayFirmwareInformationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWirelessGatewayStatistics

> GetWirelessGatewayStatisticsResponse getWirelessGatewayStatistics(id, opts)



Gets operating information about a wireless gateway.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the wireless gateway for which to get the data.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getWirelessGatewayStatistics(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the wireless gateway for which to get the data. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetWirelessGatewayStatisticsResponse**](GetWirelessGatewayStatisticsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWirelessGatewayTask

> GetWirelessGatewayTaskResponse getWirelessGatewayTask(id, opts)



Gets information about a wireless gateway task.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to get.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getWirelessGatewayTask(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to get. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetWirelessGatewayTaskResponse**](GetWirelessGatewayTaskResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWirelessGatewayTaskDefinition

> GetWirelessGatewayTaskDefinitionResponse getWirelessGatewayTaskDefinition(id, opts)



Gets information about a wireless gateway task definition.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to get.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getWirelessGatewayTaskDefinition(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to get. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetWirelessGatewayTaskDefinitionResponse**](GetWirelessGatewayTaskDefinitionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDestinations

> ListDestinationsResponse listDestinations(opts)



Lists the destinations registered to your AWS account.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return in this operation.
  'nextToken': "nextToken_example", // String | To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listDestinations(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in this operation. | [optional] 
 **nextToken** | **String**| To retrieve the next set of results, the &lt;code&gt;nextToken&lt;/code&gt; value from a previous response; otherwise &lt;b&gt;null&lt;/b&gt; to receive the first set of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListDestinationsResponse**](ListDestinationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDeviceProfiles

> ListDeviceProfilesResponse listDeviceProfiles(opts)



Lists the device profiles registered to your AWS account.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.
  'maxResults': 56, // Number | The maximum number of results to return in this operation.
  'deviceProfileType': "deviceProfileType_example", // String | A filter to list only device profiles that use this type, which can be <code>LoRaWAN</code> or <code>Sidewalk</code>.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listDeviceProfiles(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| To retrieve the next set of results, the &lt;code&gt;nextToken&lt;/code&gt; value from a previous response; otherwise &lt;b&gt;null&lt;/b&gt; to receive the first set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in this operation. | [optional] 
 **deviceProfileType** | **String**| A filter to list only device profiles that use this type, which can be &lt;code&gt;LoRaWAN&lt;/code&gt; or &lt;code&gt;Sidewalk&lt;/code&gt;. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListDeviceProfilesResponse**](ListDeviceProfilesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDevicesForWirelessDeviceImportTask

> ListDevicesForWirelessDeviceImportTaskResponse listDevicesForWirelessDeviceImportTask(id, opts)



List the Sidewalk devices in an import task and their onboarding status.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The identifier of the import task for which wireless devices are listed.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | 
  'nextToken': "nextToken_example", // String | To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <code>null</code> to receive the first set of results.
  'status': "status_example" // String | The status of the devices in the import task.
};
apiInstance.listDevicesForWirelessDeviceImportTask(id, opts, (error, data, response) => {
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
 **id** | **String**| The identifier of the import task for which wireless devices are listed. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**|  | [optional] 
 **nextToken** | **String**| To retrieve the next set of results, the &lt;code&gt;nextToken&lt;/code&gt; value from a previous response; otherwise &lt;code&gt;null&lt;/code&gt; to receive the first set of results. | [optional] 
 **status** | **String**| The status of the devices in the import task. | [optional] 

### Return type

[**ListDevicesForWirelessDeviceImportTaskResponse**](ListDevicesForWirelessDeviceImportTaskResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEventConfigurations

> ListEventConfigurationsResponse listEventConfigurations(resourceType, opts)



List event configurations where at least one event topic has been enabled.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let resourceType = "resourceType_example"; // String | Resource type to filter event configurations.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | 
  'nextToken': "nextToken_example" // String | To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.
};
apiInstance.listEventConfigurations(resourceType, opts, (error, data, response) => {
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
 **resourceType** | **String**| Resource type to filter event configurations. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**|  | [optional] 
 **nextToken** | **String**| To retrieve the next set of results, the &lt;code&gt;nextToken&lt;/code&gt; value from a previous response; otherwise &lt;b&gt;null&lt;/b&gt; to receive the first set of results. | [optional] 

### Return type

[**ListEventConfigurationsResponse**](ListEventConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFuotaTasks

> ListFuotaTasksResponse listFuotaTasks(opts)



Lists the FUOTA tasks registered to your AWS account.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.
  'maxResults': 56, // Number | 
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listFuotaTasks(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| To retrieve the next set of results, the &lt;code&gt;nextToken&lt;/code&gt; value from a previous response; otherwise &lt;b&gt;null&lt;/b&gt; to receive the first set of results. | [optional] 
 **maxResults** | **Number**|  | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListFuotaTasksResponse**](ListFuotaTasksResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMulticastGroups

> ListMulticastGroupsResponse listMulticastGroups(opts)



Lists the multicast groups registered to your AWS account.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.
  'maxResults': 56, // Number | 
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listMulticastGroups(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| To retrieve the next set of results, the &lt;code&gt;nextToken&lt;/code&gt; value from a previous response; otherwise &lt;b&gt;null&lt;/b&gt; to receive the first set of results. | [optional] 
 **maxResults** | **Number**|  | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListMulticastGroupsResponse**](ListMulticastGroupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMulticastGroupsByFuotaTask

> ListMulticastGroupsByFuotaTaskResponse listMulticastGroupsByFuotaTask(id, opts)



List all multicast groups associated with a fuota task.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.
  'maxResults': 56, // Number | 
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listMulticastGroupsByFuotaTask(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| To retrieve the next set of results, the &lt;code&gt;nextToken&lt;/code&gt; value from a previous response; otherwise &lt;b&gt;null&lt;/b&gt; to receive the first set of results. | [optional] 
 **maxResults** | **Number**|  | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListMulticastGroupsByFuotaTaskResponse**](ListMulticastGroupsByFuotaTaskResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listNetworkAnalyzerConfigurations

> ListNetworkAnalyzerConfigurationsResponse listNetworkAnalyzerConfigurations(opts)



Lists the network analyzer configurations.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | 
  'nextToken': "nextToken_example", // String | To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listNetworkAnalyzerConfigurations(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**|  | [optional] 
 **nextToken** | **String**| To retrieve the next set of results, the &lt;code&gt;nextToken&lt;/code&gt; value from a previous response; otherwise &lt;b&gt;null&lt;/b&gt; to receive the first set of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListNetworkAnalyzerConfigurationsResponse**](ListNetworkAnalyzerConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPartnerAccounts

> ListPartnerAccountsResponse listPartnerAccounts(opts)



Lists the partner accounts associated with your AWS account.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.
  'maxResults': 56 // Number | The maximum number of results to return in this operation.
};
apiInstance.listPartnerAccounts(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| To retrieve the next set of results, the &lt;code&gt;nextToken&lt;/code&gt; value from a previous response; otherwise &lt;b&gt;null&lt;/b&gt; to receive the first set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in this operation. | [optional] 

### Return type

[**ListPartnerAccountsResponse**](ListPartnerAccountsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPositionConfigurations

> ListPositionConfigurationsResponse listPositionConfigurations(opts)



&lt;p&gt;List position configurations for a given resource, such as positioning solvers.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This action is no longer supported. Calls to retrieve position information should use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_GetResourcePosition.html\&quot;&gt;GetResourcePosition&lt;/a&gt; API operation instead.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'resourceType': "resourceType_example", // String | Resource type for which position configurations are listed.
  'maxResults': 56, // Number | 
  'nextToken': "nextToken_example", // String | To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listPositionConfigurations(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **resourceType** | **String**| Resource type for which position configurations are listed. | [optional] 
 **maxResults** | **Number**|  | [optional] 
 **nextToken** | **String**| To retrieve the next set of results, the &lt;code&gt;nextToken&lt;/code&gt; value from a previous response; otherwise &lt;b&gt;null&lt;/b&gt; to receive the first set of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListPositionConfigurationsResponse**](ListPositionConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listQueuedMessages

> ListQueuedMessagesResponse listQueuedMessages(id, opts)



List queued messages in the downlink queue.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of a given wireless device which the downlink message packets are being sent.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.
  'maxResults': 56, // Number | The maximum number of results to return in this operation.
  'wirelessDeviceType': "wirelessDeviceType_example", // String | The wireless device type, whic can be either Sidewalk or LoRaWAN.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listQueuedMessages(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of a given wireless device which the downlink message packets are being sent. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| To retrieve the next set of results, the &lt;code&gt;nextToken&lt;/code&gt; value from a previous response; otherwise &lt;b&gt;null&lt;/b&gt; to receive the first set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in this operation. | [optional] 
 **wirelessDeviceType** | **String**| The wireless device type, whic can be either Sidewalk or LoRaWAN. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListQueuedMessagesResponse**](ListQueuedMessagesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listServiceProfiles

> ListServiceProfilesResponse listServiceProfiles(opts)



Lists the service profiles registered to your AWS account.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.
  'maxResults': 56, // Number | The maximum number of results to return in this operation.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listServiceProfiles(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| To retrieve the next set of results, the &lt;code&gt;nextToken&lt;/code&gt; value from a previous response; otherwise &lt;b&gt;null&lt;/b&gt; to receive the first set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in this operation. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListServiceProfilesResponse**](ListServiceProfilesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Lists the tags (metadata) you have assigned to the resource.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource for which you want to list tags.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The ARN of the resource for which you want to list tags. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWirelessDeviceImportTasks

> ListWirelessDeviceImportTasksResponse listWirelessDeviceImportTasks(opts)



List wireless devices that have been added to an import task.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | 
  'nextToken': "nextToken_example" // String | To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <code>null</code> to receive the first set of results.
};
apiInstance.listWirelessDeviceImportTasks(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**|  | [optional] 
 **nextToken** | **String**| To retrieve the next set of results, the &lt;code&gt;nextToken&lt;/code&gt; value from a previous response; otherwise &lt;code&gt;null&lt;/code&gt; to receive the first set of results. | [optional] 

### Return type

[**ListWirelessDeviceImportTasksResponse**](ListWirelessDeviceImportTasksResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWirelessDevices

> ListWirelessDevicesResponse listWirelessDevices(opts)



Lists the wireless devices registered to your AWS account.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return in this operation.
  'nextToken': "nextToken_example", // String | To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.
  'destinationName': "destinationName_example", // String | A filter to list only the wireless devices that use this destination.
  'deviceProfileId': "deviceProfileId_example", // String | A filter to list only the wireless devices that use this device profile.
  'serviceProfileId': "serviceProfileId_example", // String | A filter to list only the wireless devices that use this service profile.
  'wirelessDeviceType': "wirelessDeviceType_example", // String | A filter to list only the wireless devices that use this wireless device type.
  'fuotaTaskId': "fuotaTaskId_example", // String | 
  'multicastGroupId': "multicastGroupId_example", // String | 
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listWirelessDevices(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in this operation. | [optional] 
 **nextToken** | **String**| To retrieve the next set of results, the &lt;code&gt;nextToken&lt;/code&gt; value from a previous response; otherwise &lt;b&gt;null&lt;/b&gt; to receive the first set of results. | [optional] 
 **destinationName** | **String**| A filter to list only the wireless devices that use this destination. | [optional] 
 **deviceProfileId** | **String**| A filter to list only the wireless devices that use this device profile. | [optional] 
 **serviceProfileId** | **String**| A filter to list only the wireless devices that use this service profile. | [optional] 
 **wirelessDeviceType** | **String**| A filter to list only the wireless devices that use this wireless device type. | [optional] 
 **fuotaTaskId** | **String**|  | [optional] 
 **multicastGroupId** | **String**|  | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListWirelessDevicesResponse**](ListWirelessDevicesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWirelessGatewayTaskDefinitions

> ListWirelessGatewayTaskDefinitionsResponse listWirelessGatewayTaskDefinitions(opts)



List the wireless gateway tasks definitions registered to your AWS account.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return in this operation.
  'nextToken': "nextToken_example", // String | To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.
  'taskDefinitionType': "taskDefinitionType_example" // String | A filter to list only the wireless gateway task definitions that use this task definition type.
};
apiInstance.listWirelessGatewayTaskDefinitions(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in this operation. | [optional] 
 **nextToken** | **String**| To retrieve the next set of results, the &lt;code&gt;nextToken&lt;/code&gt; value from a previous response; otherwise &lt;b&gt;null&lt;/b&gt; to receive the first set of results. | [optional] 
 **taskDefinitionType** | **String**| A filter to list only the wireless gateway task definitions that use this task definition type. | [optional] 

### Return type

[**ListWirelessGatewayTaskDefinitionsResponse**](ListWirelessGatewayTaskDefinitionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWirelessGateways

> ListWirelessGatewaysResponse listWirelessGateways(opts)



Lists the wireless gateways registered to your AWS account.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.
  'maxResults': 56, // Number | The maximum number of results to return in this operation.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listWirelessGateways(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| To retrieve the next set of results, the &lt;code&gt;nextToken&lt;/code&gt; value from a previous response; otherwise &lt;b&gt;null&lt;/b&gt; to receive the first set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in this operation. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListWirelessGatewaysResponse**](ListWirelessGatewaysResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putPositionConfiguration

> Object putPositionConfiguration(resourceIdentifier, resourceType, putPositionConfigurationRequest, opts)



&lt;p&gt;Put position configuration for a given resource.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This action is no longer supported. Calls to update the position configuration should use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_UpdateResourcePosition.html\&quot;&gt;UpdateResourcePosition&lt;/a&gt; API operation instead.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let resourceIdentifier = "resourceIdentifier_example"; // String | Resource identifier used to update the position configuration.
let resourceType = "resourceType_example"; // String | Resource type of the resource for which you want to update the position configuration.
let putPositionConfigurationRequest = new AwsIoTWireless.PutPositionConfigurationRequest(); // PutPositionConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putPositionConfiguration(resourceIdentifier, resourceType, putPositionConfigurationRequest, opts, (error, data, response) => {
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
 **resourceIdentifier** | **String**| Resource identifier used to update the position configuration. | 
 **resourceType** | **String**| Resource type of the resource for which you want to update the position configuration. | 
 **putPositionConfigurationRequest** | [**PutPositionConfigurationRequest**](PutPositionConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putResourceLogLevel

> Object putResourceLogLevel(resourceIdentifier, resourceType, putResourceLogLevelRequest, opts)



Sets the log-level override for a resource-ID and resource-type. This option can be specified for a wireless gateway or a wireless device. A limit of 200 log level override can be set per account.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let resourceIdentifier = "resourceIdentifier_example"; // String | 
let resourceType = "resourceType_example"; // String | The type of the resource, which can be <code>WirelessDevice</code> or <code>WirelessGateway</code>.
let putResourceLogLevelRequest = new AwsIoTWireless.PutResourceLogLevelRequest(); // PutResourceLogLevelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putResourceLogLevel(resourceIdentifier, resourceType, putResourceLogLevelRequest, opts, (error, data, response) => {
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
 **resourceIdentifier** | **String**|  | 
 **resourceType** | **String**| The type of the resource, which can be &lt;code&gt;WirelessDevice&lt;/code&gt; or &lt;code&gt;WirelessGateway&lt;/code&gt;. | 
 **putResourceLogLevelRequest** | [**PutResourceLogLevelRequest**](PutResourceLogLevelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resetAllResourceLogLevels

> Object resetAllResourceLogLevels(opts)



Removes the log-level overrides for all resources; both wireless devices and wireless gateways.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.resetAllResourceLogLevels(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resetResourceLogLevel

> Object resetResourceLogLevel(resourceIdentifier, resourceType, opts)



Removes the log-level override, if any, for a specific resource-ID and resource-type. It can be used for a wireless device or a wireless gateway.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let resourceIdentifier = "resourceIdentifier_example"; // String | 
let resourceType = "resourceType_example"; // String | The type of the resource, which can be <code>WirelessDevice</code> or <code>WirelessGateway</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.resetResourceLogLevel(resourceIdentifier, resourceType, opts, (error, data, response) => {
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
 **resourceIdentifier** | **String**|  | 
 **resourceType** | **String**| The type of the resource, which can be &lt;code&gt;WirelessDevice&lt;/code&gt; or &lt;code&gt;WirelessGateway&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sendDataToMulticastGroup

> SendDataToMulticastGroupResponse sendDataToMulticastGroup(id, sendDataToMulticastGroupRequest, opts)



Sends the specified data to a multicast group.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | 
let sendDataToMulticastGroupRequest = new AwsIoTWireless.SendDataToMulticastGroupRequest(); // SendDataToMulticastGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.sendDataToMulticastGroup(id, sendDataToMulticastGroupRequest, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **sendDataToMulticastGroupRequest** | [**SendDataToMulticastGroupRequest**](SendDataToMulticastGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SendDataToMulticastGroupResponse**](SendDataToMulticastGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendDataToWirelessDevice

> SendDataToWirelessDeviceResponse sendDataToWirelessDevice(id, sendDataToWirelessDeviceRequest, opts)



Sends a decrypted application data frame to a device.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the wireless device to receive the data.
let sendDataToWirelessDeviceRequest = new AwsIoTWireless.SendDataToWirelessDeviceRequest(); // SendDataToWirelessDeviceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.sendDataToWirelessDevice(id, sendDataToWirelessDeviceRequest, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the wireless device to receive the data. | 
 **sendDataToWirelessDeviceRequest** | [**SendDataToWirelessDeviceRequest**](SendDataToWirelessDeviceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SendDataToWirelessDeviceResponse**](SendDataToWirelessDeviceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startBulkAssociateWirelessDeviceWithMulticastGroup

> Object startBulkAssociateWirelessDeviceWithMulticastGroup(id, startBulkDisassociateWirelessDeviceFromMulticastGroupRequest, opts)



Starts a bulk association of all qualifying wireless devices with a multicast group.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | 
let startBulkDisassociateWirelessDeviceFromMulticastGroupRequest = new AwsIoTWireless.StartBulkDisassociateWirelessDeviceFromMulticastGroupRequest(); // StartBulkDisassociateWirelessDeviceFromMulticastGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startBulkAssociateWirelessDeviceWithMulticastGroup(id, startBulkDisassociateWirelessDeviceFromMulticastGroupRequest, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **startBulkDisassociateWirelessDeviceFromMulticastGroupRequest** | [**StartBulkDisassociateWirelessDeviceFromMulticastGroupRequest**](StartBulkDisassociateWirelessDeviceFromMulticastGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startBulkDisassociateWirelessDeviceFromMulticastGroup

> Object startBulkDisassociateWirelessDeviceFromMulticastGroup(id, startBulkDisassociateWirelessDeviceFromMulticastGroupRequest, opts)



Starts a bulk disassociatin of all qualifying wireless devices from a multicast group.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | 
let startBulkDisassociateWirelessDeviceFromMulticastGroupRequest = new AwsIoTWireless.StartBulkDisassociateWirelessDeviceFromMulticastGroupRequest(); // StartBulkDisassociateWirelessDeviceFromMulticastGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startBulkDisassociateWirelessDeviceFromMulticastGroup(id, startBulkDisassociateWirelessDeviceFromMulticastGroupRequest, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **startBulkDisassociateWirelessDeviceFromMulticastGroupRequest** | [**StartBulkDisassociateWirelessDeviceFromMulticastGroupRequest**](StartBulkDisassociateWirelessDeviceFromMulticastGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startFuotaTask

> Object startFuotaTask(id, startFuotaTaskRequest, opts)



Starts a FUOTA task.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | 
let startFuotaTaskRequest = new AwsIoTWireless.StartFuotaTaskRequest(); // StartFuotaTaskRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startFuotaTask(id, startFuotaTaskRequest, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **startFuotaTaskRequest** | [**StartFuotaTaskRequest**](StartFuotaTaskRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startMulticastGroupSession

> Object startMulticastGroupSession(id, startMulticastGroupSessionRequest, opts)



Starts a multicast group session.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | 
let startMulticastGroupSessionRequest = new AwsIoTWireless.StartMulticastGroupSessionRequest(); // StartMulticastGroupSessionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startMulticastGroupSession(id, startMulticastGroupSessionRequest, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **startMulticastGroupSessionRequest** | [**StartMulticastGroupSessionRequest**](StartMulticastGroupSessionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startSingleWirelessDeviceImportTask

> StartSingleWirelessDeviceImportTaskResponse startSingleWirelessDeviceImportTask(startSingleWirelessDeviceImportTaskRequest, opts)



Start import task for a single wireless device.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let startSingleWirelessDeviceImportTaskRequest = new AwsIoTWireless.StartSingleWirelessDeviceImportTaskRequest(); // StartSingleWirelessDeviceImportTaskRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startSingleWirelessDeviceImportTask(startSingleWirelessDeviceImportTaskRequest, opts, (error, data, response) => {
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
 **startSingleWirelessDeviceImportTaskRequest** | [**StartSingleWirelessDeviceImportTaskRequest**](StartSingleWirelessDeviceImportTaskRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartSingleWirelessDeviceImportTaskResponse**](StartSingleWirelessDeviceImportTaskResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startWirelessDeviceImportTask

> StartWirelessDeviceImportTaskResponse startWirelessDeviceImportTask(startWirelessDeviceImportTaskRequest, opts)



Start import task for provisioning Sidewalk devices in bulk using an S3 CSV file.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let startWirelessDeviceImportTaskRequest = new AwsIoTWireless.StartWirelessDeviceImportTaskRequest(); // StartWirelessDeviceImportTaskRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startWirelessDeviceImportTask(startWirelessDeviceImportTaskRequest, opts, (error, data, response) => {
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
 **startWirelessDeviceImportTaskRequest** | [**StartWirelessDeviceImportTaskRequest**](StartWirelessDeviceImportTaskRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartWirelessDeviceImportTaskResponse**](StartWirelessDeviceImportTaskResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



Adds a tag to a resource.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource to add tags to.
let tagResourceRequest = new AwsIoTWireless.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(resourceArn, tagResourceRequest, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The ARN of the resource to add tags to. | 
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## testWirelessDevice

> TestWirelessDeviceResponse testWirelessDevice(id, opts)



Simulates a provisioned device by sending an uplink data payload of &lt;code&gt;Hello&lt;/code&gt;.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the wireless device to test.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.testWirelessDevice(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the wireless device to test. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**TestWirelessDeviceResponse**](TestWirelessDeviceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## untagResource

> Object untagResource(resourceArn, tagKeys, opts)



Removes one or more tags from a resource.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource to remove tags from.
let tagKeys = ["null"]; // [String] | A list of the keys of the tags to remove from the resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(resourceArn, tagKeys, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The ARN of the resource to remove tags from. | 
 **tagKeys** | [**[String]**](String.md)| A list of the keys of the tags to remove from the resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDestination

> Object updateDestination(name, updateDestinationRequest, opts)



Updates properties of a destination.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let name = "name_example"; // String | The new name of the resource.
let updateDestinationRequest = new AwsIoTWireless.UpdateDestinationRequest(); // UpdateDestinationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateDestination(name, updateDestinationRequest, opts, (error, data, response) => {
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
 **name** | **String**| The new name of the resource. | 
 **updateDestinationRequest** | [**UpdateDestinationRequest**](UpdateDestinationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateEventConfigurationByResourceTypes

> Object updateEventConfigurationByResourceTypes(updateEventConfigurationByResourceTypesRequest, opts)



Update the event configuration based on resource types.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let updateEventConfigurationByResourceTypesRequest = new AwsIoTWireless.UpdateEventConfigurationByResourceTypesRequest(); // UpdateEventConfigurationByResourceTypesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateEventConfigurationByResourceTypes(updateEventConfigurationByResourceTypesRequest, opts, (error, data, response) => {
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
 **updateEventConfigurationByResourceTypesRequest** | [**UpdateEventConfigurationByResourceTypesRequest**](UpdateEventConfigurationByResourceTypesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateFuotaTask

> Object updateFuotaTask(id, updateFuotaTaskRequest, opts)



Updates properties of a FUOTA task.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | 
let updateFuotaTaskRequest = new AwsIoTWireless.UpdateFuotaTaskRequest(); // UpdateFuotaTaskRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateFuotaTask(id, updateFuotaTaskRequest, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **updateFuotaTaskRequest** | [**UpdateFuotaTaskRequest**](UpdateFuotaTaskRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateLogLevelsByResourceTypes

> Object updateLogLevelsByResourceTypes(updateLogLevelsByResourceTypesRequest, opts)



Set default log level, or log levels by resource types. This can be for wireless device log options or wireless gateways log options and is used to control the log messages that&#39;ll be displayed in CloudWatch.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let updateLogLevelsByResourceTypesRequest = new AwsIoTWireless.UpdateLogLevelsByResourceTypesRequest(); // UpdateLogLevelsByResourceTypesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateLogLevelsByResourceTypes(updateLogLevelsByResourceTypesRequest, opts, (error, data, response) => {
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
 **updateLogLevelsByResourceTypesRequest** | [**UpdateLogLevelsByResourceTypesRequest**](UpdateLogLevelsByResourceTypesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMulticastGroup

> Object updateMulticastGroup(id, updateMulticastGroupRequest, opts)



Updates properties of a multicast group session.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | 
let updateMulticastGroupRequest = new AwsIoTWireless.UpdateMulticastGroupRequest(); // UpdateMulticastGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateMulticastGroup(id, updateMulticastGroupRequest, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **updateMulticastGroupRequest** | [**UpdateMulticastGroupRequest**](UpdateMulticastGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkAnalyzerConfiguration

> Object updateNetworkAnalyzerConfiguration(configurationName, updateNetworkAnalyzerConfigurationRequest, opts)



Update network analyzer configuration.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let configurationName = "configurationName_example"; // String | 
let updateNetworkAnalyzerConfigurationRequest = new AwsIoTWireless.UpdateNetworkAnalyzerConfigurationRequest(); // UpdateNetworkAnalyzerConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateNetworkAnalyzerConfiguration(configurationName, updateNetworkAnalyzerConfigurationRequest, opts, (error, data, response) => {
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
 **configurationName** | **String**|  | 
 **updateNetworkAnalyzerConfigurationRequest** | [**UpdateNetworkAnalyzerConfigurationRequest**](UpdateNetworkAnalyzerConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePartnerAccount

> Object updatePartnerAccount(partnerAccountId, partnerType, updatePartnerAccountRequest, opts)



Updates properties of a partner account.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let partnerAccountId = "partnerAccountId_example"; // String | The ID of the partner account to update.
let partnerType = "partnerType_example"; // String | The partner type.
let updatePartnerAccountRequest = new AwsIoTWireless.UpdatePartnerAccountRequest(); // UpdatePartnerAccountRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updatePartnerAccount(partnerAccountId, partnerType, updatePartnerAccountRequest, opts, (error, data, response) => {
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
 **partnerAccountId** | **String**| The ID of the partner account to update. | 
 **partnerType** | **String**| The partner type. | 
 **updatePartnerAccountRequest** | [**UpdatePartnerAccountRequest**](UpdatePartnerAccountRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePosition

> Object updatePosition(resourceIdentifier, resourceType, updatePositionRequest, opts)



&lt;p&gt;Update the position information of a resource.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This action is no longer supported. Calls to update the position information should use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_UpdateResourcePosition.html\&quot;&gt;UpdateResourcePosition&lt;/a&gt; API operation instead.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let resourceIdentifier = "resourceIdentifier_example"; // String | Resource identifier of the resource for which position is updated.
let resourceType = "resourceType_example"; // String | Resource type of the resource for which position is updated.
let updatePositionRequest = new AwsIoTWireless.UpdatePositionRequest(); // UpdatePositionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updatePosition(resourceIdentifier, resourceType, updatePositionRequest, opts, (error, data, response) => {
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
 **resourceIdentifier** | **String**| Resource identifier of the resource for which position is updated. | 
 **resourceType** | **String**| Resource type of the resource for which position is updated. | 
 **updatePositionRequest** | [**UpdatePositionRequest**](UpdatePositionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateResourceEventConfiguration

> Object updateResourceEventConfiguration(identifier, identifierType, updateResourceEventConfigurationRequest, opts)



Update the event configuration for a particular resource identifier.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let identifier = "identifier_example"; // String | Resource identifier to opt in for event messaging.
let identifierType = "identifierType_example"; // String | Identifier type of the particular resource identifier for event configuration.
let updateResourceEventConfigurationRequest = new AwsIoTWireless.UpdateResourceEventConfigurationRequest(); // UpdateResourceEventConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'partnerType': "partnerType_example" // String | Partner type of the resource if the identifier type is <code>PartnerAccountId</code> 
};
apiInstance.updateResourceEventConfiguration(identifier, identifierType, updateResourceEventConfigurationRequest, opts, (error, data, response) => {
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
 **identifier** | **String**| Resource identifier to opt in for event messaging. | 
 **identifierType** | **String**| Identifier type of the particular resource identifier for event configuration. | 
 **updateResourceEventConfigurationRequest** | [**UpdateResourceEventConfigurationRequest**](UpdateResourceEventConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **partnerType** | **String**| Partner type of the resource if the identifier type is &lt;code&gt;PartnerAccountId&lt;/code&gt;  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateResourcePosition

> Object updateResourcePosition(resourceIdentifier, resourceType, updateResourcePositionRequest, opts)



Update the position information of a given wireless device or a wireless gateway resource. The position coordinates are based on the &lt;a href&#x3D;\&quot;https://gisgeography.com/wgs84-world-geodetic-system/\&quot;&gt; World Geodetic System (WGS84)&lt;/a&gt;.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let resourceIdentifier = "resourceIdentifier_example"; // String | The identifier of the resource for which position information is updated. It can be the wireless device ID or the wireless gateway ID, depending on the resource type.
let resourceType = "resourceType_example"; // String | The type of resource for which position information is updated, which can be a wireless device or a wireless gateway.
let updateResourcePositionRequest = new AwsIoTWireless.UpdateResourcePositionRequest(); // UpdateResourcePositionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateResourcePosition(resourceIdentifier, resourceType, updateResourcePositionRequest, opts, (error, data, response) => {
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
 **resourceIdentifier** | **String**| The identifier of the resource for which position information is updated. It can be the wireless device ID or the wireless gateway ID, depending on the resource type. | 
 **resourceType** | **String**| The type of resource for which position information is updated, which can be a wireless device or a wireless gateway. | 
 **updateResourcePositionRequest** | [**UpdateResourcePositionRequest**](UpdateResourcePositionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateWirelessDevice

> Object updateWirelessDevice(id, updateWirelessDeviceRequest, opts)



Updates properties of a wireless device.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to update.
let updateWirelessDeviceRequest = new AwsIoTWireless.UpdateWirelessDeviceRequest(); // UpdateWirelessDeviceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateWirelessDevice(id, updateWirelessDeviceRequest, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to update. | 
 **updateWirelessDeviceRequest** | [**UpdateWirelessDeviceRequest**](UpdateWirelessDeviceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateWirelessDeviceImportTask

> Object updateWirelessDeviceImportTask(id, updateWirelessDeviceImportTaskRequest, opts)



Update an import task to add more devices to the task.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The identifier of the import task to be updated.
let updateWirelessDeviceImportTaskRequest = new AwsIoTWireless.UpdateWirelessDeviceImportTaskRequest(); // UpdateWirelessDeviceImportTaskRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateWirelessDeviceImportTask(id, updateWirelessDeviceImportTaskRequest, opts, (error, data, response) => {
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
 **id** | **String**| The identifier of the import task to be updated. | 
 **updateWirelessDeviceImportTaskRequest** | [**UpdateWirelessDeviceImportTaskRequest**](UpdateWirelessDeviceImportTaskRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateWirelessGateway

> Object updateWirelessGateway(id, updateWirelessGatewayRequest, opts)



Updates properties of a wireless gateway.

### Example

```javascript
import AwsIoTWireless from 'aws_io_t_wireless';
let defaultClient = AwsIoTWireless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTWireless.DefaultApi();
let id = "id_example"; // String | The ID of the resource to update.
let updateWirelessGatewayRequest = new AwsIoTWireless.UpdateWirelessGatewayRequest(); // UpdateWirelessGatewayRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateWirelessGateway(id, updateWirelessGatewayRequest, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the resource to update. | 
 **updateWirelessGatewayRequest** | [**UpdateWirelessGatewayRequest**](UpdateWirelessGatewayRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

