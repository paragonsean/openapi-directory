

# TopicTypeProperties

Properties of a topic type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of the topic type. |  [optional] |
|**displayName** | **String** | Display Name for the topic type. |  [optional] |
|**provider** | **String** | Namespace of the provider of the topic type. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the topic type |  [optional] |
|**resourceRegionType** | [**ResourceRegionTypeEnum**](#ResourceRegionTypeEnum) | Region type of the resource. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| CANCELED | &quot;Canceled&quot; |
| FAILED | &quot;Failed&quot; |



## Enum: ResourceRegionTypeEnum

| Name | Value |
|---- | -----|
| REGIONAL_RESOURCE | &quot;RegionalResource&quot; |
| GLOBAL_RESOURCE | &quot;GlobalResource&quot; |



