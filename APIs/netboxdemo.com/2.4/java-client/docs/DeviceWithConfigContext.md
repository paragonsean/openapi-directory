

# DeviceWithConfigContext


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetTag** | **String** | A unique tag used to identify this device |  [optional] |
|**cluster** | [**NestedCluster**](NestedCluster.md) |  |  [optional] |
|**comments** | **String** |  |  [optional] |
|**configContext** | **String** |  |  [optional] [readonly] |
|**created** | **LocalDate** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**deviceRole** | [**NestedDeviceRole**](NestedDeviceRole.md) |  |  |
|**deviceType** | [**NestedDeviceType**](NestedDeviceType.md) |  |  |
|**displayName** | **String** |  |  [optional] [readonly] |
|**face** | [**Face**](Face.md) |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**localContextData** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**parentDevice** | **String** |  |  [optional] [readonly] |
|**platform** | [**NestedPlatform**](NestedPlatform.md) |  |  [optional] |
|**position** | **Integer** | The lowest-numbered unit occupied by the device |  [optional] |
|**primaryIp** | [**DeviceIPAddress**](DeviceIPAddress.md) |  |  [optional] |
|**primaryIp4** | [**DeviceIPAddress**](DeviceIPAddress.md) |  |  [optional] |
|**primaryIp6** | [**DeviceIPAddress**](DeviceIPAddress.md) |  |  [optional] |
|**rack** | [**NestedRack**](NestedRack.md) |  |  [optional] |
|**serial** | **String** |  |  [optional] |
|**site** | [**NestedSite**](NestedSite.md) |  |  |
|**status** | [**Status**](Status.md) |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**tenant** | [**NestedTenant**](NestedTenant.md) |  |  [optional] |
|**vcPosition** | **Integer** |  |  [optional] |
|**vcPriority** | **Integer** |  |  [optional] |
|**virtualChassis** | [**DeviceVirtualChassis**](DeviceVirtualChassis.md) |  |  [optional] |



