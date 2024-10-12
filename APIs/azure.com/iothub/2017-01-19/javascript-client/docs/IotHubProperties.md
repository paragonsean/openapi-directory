# IotHubClient.IotHubProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizationPolicies** | [**[SharedAccessSignatureAuthorizationRule]**](SharedAccessSignatureAuthorizationRule.md) | The shared access policies you can use to secure a connection to the IoT hub. | [optional] 
**cloudToDevice** | [**CloudToDeviceProperties**](CloudToDeviceProperties.md) |  | [optional] 
**comments** | **String** | Comments. | [optional] 
**enableFileUploadNotifications** | **Boolean** | If True, file upload notifications are enabled. | [optional] 
**eventHubEndpoints** | [**{String: EventHubProperties}**](EventHubProperties.md) | The Event Hub-compatible endpoint properties. The possible keys to this dictionary are events and operationsMonitoringEvents. Both of these keys have to be present in the dictionary while making create or update calls for the IoT hub. | [optional] 
**features** | **String** | The capabilities and features enabled for the IoT hub. | [optional] 
**hostName** | **String** | The name of the host. | [optional] [readonly] 
**ipFilterRules** | [**[IpFilterRule]**](IpFilterRule.md) | The IP filter rules. | [optional] 
**messagingEndpoints** | [**{String: MessagingEndpointProperties}**](MessagingEndpointProperties.md) | The messaging endpoint properties for the file upload notification queue. | [optional] 
**operationsMonitoringProperties** | [**OperationsMonitoringProperties**](OperationsMonitoringProperties.md) |  | [optional] 
**provisioningState** | **String** | The provisioning state. | [optional] [readonly] 
**routing** | [**RoutingProperties**](RoutingProperties.md) |  | [optional] 
**storageEndpoints** | [**{String: StorageEndpointProperties}**](StorageEndpointProperties.md) | The list of Azure Storage endpoints where you can upload files. Currently you can configure only one Azure Storage account and that MUST have its key as $default. Specifying more than one storage account causes an error to be thrown. Not specifying a value for this property when the enableFileUploadNotifications property is set to True, causes an error to be thrown. | [optional] 



## Enum: FeaturesEnum


* `None` (value: `"None"`)

* `DeviceManagement` (value: `"DeviceManagement"`)




