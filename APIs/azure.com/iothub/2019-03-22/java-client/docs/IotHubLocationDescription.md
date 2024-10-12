

# IotHubLocationDescription

Public representation of one of the locations where a resource is provisioned.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**location** | **String** | The name of the Azure region |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | The role of the region, can be either primary or secondary. The primary region is where the IoT hub is currently provisioned. The secondary region is the Azure disaster recovery (DR) paired region and also the region where the IoT hub can failover to. |  [optional] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| PRIMARY | &quot;primary&quot; |
| SECONDARY | &quot;secondary&quot; |



