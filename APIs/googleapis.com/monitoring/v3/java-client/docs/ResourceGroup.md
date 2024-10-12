

# ResourceGroup

The resource submessage for group checks. It can be used instead of a monitored resource, when multiple resources are being monitored.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**groupId** | **String** | The group of resources being monitored. Should be only the [GROUP_ID], and not the full-path projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID]. |  [optional] |
|**resourceType** | [**ResourceTypeEnum**](#ResourceTypeEnum) | The resource type of the group members. |  [optional] |



## Enum: ResourceTypeEnum

| Name | Value |
|---- | -----|
| RESOURCE_TYPE_UNSPECIFIED | &quot;RESOURCE_TYPE_UNSPECIFIED&quot; |
| INSTANCE | &quot;INSTANCE&quot; |
| AWS_ELB_LOAD_BALANCER | &quot;AWS_ELB_LOAD_BALANCER&quot; |



