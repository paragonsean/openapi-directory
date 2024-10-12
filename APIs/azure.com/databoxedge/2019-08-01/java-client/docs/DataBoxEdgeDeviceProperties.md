

# DataBoxEdgeDeviceProperties

The properties of the Data Box Edge/Gateway device.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configuredRoleTypes** | [**List&lt;ConfiguredRoleTypesEnum&gt;**](#List&lt;ConfiguredRoleTypesEnum&gt;) | Type of compute roles configured. |  [optional] [readonly] |
|**culture** | **String** | The Data Box Edge/Gateway device culture. |  [optional] [readonly] |
|**dataBoxEdgeDeviceStatus** | [**DataBoxEdgeDeviceStatusEnum**](#DataBoxEdgeDeviceStatusEnum) | The status of the Data Box Edge/Gateway device. |  [optional] |
|**description** | **String** | The Description of the Data Box Edge/Gateway device. |  [optional] |
|**deviceHcsVersion** | **String** | The device software version number of the device (eg: 1.2.18105.6). |  [optional] [readonly] |
|**deviceLocalCapacity** | **Long** | The Data Box Edge/Gateway device local capacity in MB. |  [optional] [readonly] |
|**deviceModel** | **String** | The Data Box Edge/Gateway device model. |  [optional] [readonly] |
|**deviceSoftwareVersion** | **String** | The Data Box Edge/Gateway device software version. |  [optional] [readonly] |
|**deviceType** | [**DeviceTypeEnum**](#DeviceTypeEnum) | The type of the Data Box Edge/Gateway device. |  [optional] [readonly] |
|**friendlyName** | **String** | The Data Box Edge/Gateway device name. |  [optional] |
|**modelDescription** | **String** | The description of the Data Box Edge/Gateway device model. |  [optional] |
|**nodeCount** | **Integer** | The number of nodes in the cluster. |  [optional] [readonly] |
|**serialNumber** | **String** | The Serial Number of Data Box Edge/Gateway device. |  [optional] [readonly] |
|**timeZone** | **String** | The Data Box Edge/Gateway device timezone. |  [optional] [readonly] |



## Enum: List&lt;ConfiguredRoleTypesEnum&gt;

| Name | Value |
|---- | -----|
| IOT | &quot;IOT&quot; |
| ASA | &quot;ASA&quot; |
| FUNCTIONS | &quot;Functions&quot; |
| COGNITIVE | &quot;Cognitive&quot; |



## Enum: DataBoxEdgeDeviceStatusEnum

| Name | Value |
|---- | -----|
| READY_TO_SETUP | &quot;ReadyToSetup&quot; |
| ONLINE | &quot;Online&quot; |
| OFFLINE | &quot;Offline&quot; |
| NEEDS_ATTENTION | &quot;NeedsAttention&quot; |
| DISCONNECTED | &quot;Disconnected&quot; |
| PARTIALLY_DISCONNECTED | &quot;PartiallyDisconnected&quot; |
| MAINTENANCE | &quot;Maintenance&quot; |



## Enum: DeviceTypeEnum

| Name | Value |
|---- | -----|
| DATA_BOX_EDGE_DEVICE | &quot;DataBoxEdgeDevice&quot; |



