

# IotHubProperties

The properties of an IoT hub.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationPolicies** | [**List&lt;SharedAccessSignatureAuthorizationRule&gt;**](SharedAccessSignatureAuthorizationRule.md) | The shared access policies you can use to secure a connection to the IoT hub. |  [optional] |
|**cloudToDevice** | [**CloudToDeviceProperties**](CloudToDeviceProperties.md) |  |  [optional] |
|**comments** | **String** | IoT hub comments. |  [optional] |
|**deviceStreams** | [**IotHubPropertiesDeviceStreams**](IotHubPropertiesDeviceStreams.md) |  |  [optional] |
|**enableFileUploadNotifications** | **Boolean** | If True, file upload notifications are enabled. |  [optional] |
|**eventHubEndpoints** | [**Map&lt;String, EventHubProperties&gt;**](EventHubProperties.md) | The Event Hub-compatible endpoint properties. The only possible keys to this dictionary is events. This key has to be present in the dictionary while making create or update calls for the IoT hub. |  [optional] |
|**features** | [**FeaturesEnum**](#FeaturesEnum) | The capabilities and features enabled for the IoT hub. |  [optional] |
|**hostName** | **String** | The name of the host. |  [optional] [readonly] |
|**ipFilterRules** | [**List&lt;IpFilterRule&gt;**](IpFilterRule.md) | The IP filter rules. |  [optional] |
|**locations** | [**List&lt;IotHubLocationDescription&gt;**](IotHubLocationDescription.md) | Primary and secondary location for iot hub |  [optional] [readonly] |
|**messagingEndpoints** | [**Map&lt;String, MessagingEndpointProperties&gt;**](MessagingEndpointProperties.md) | The messaging endpoint properties for the file upload notification queue. |  [optional] |
|**provisioningState** | **String** | The provisioning state. |  [optional] [readonly] |
|**routing** | [**RoutingProperties**](RoutingProperties.md) |  |  [optional] |
|**state** | **String** | The hub state. |  [optional] [readonly] |
|**storageEndpoints** | [**Map&lt;String, StorageEndpointProperties&gt;**](StorageEndpointProperties.md) | The list of Azure Storage endpoints where you can upload files. Currently you can configure only one Azure Storage account and that MUST have its key as $default. Specifying more than one storage account causes an error to be thrown. Not specifying a value for this property when the enableFileUploadNotifications property is set to True, causes an error to be thrown. |  [optional] |



## Enum: FeaturesEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| DEVICE_MANAGEMENT | &quot;DeviceManagement&quot; |



