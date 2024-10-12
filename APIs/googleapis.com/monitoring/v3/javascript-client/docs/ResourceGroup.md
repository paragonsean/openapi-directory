# CloudMonitoringApi.ResourceGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groupId** | **String** | The group of resources being monitored. Should be only the [GROUP_ID], and not the full-path projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID]. | [optional] 
**resourceType** | **String** | The resource type of the group members. | [optional] 



## Enum: ResourceTypeEnum


* `RESOURCE_TYPE_UNSPECIFIED` (value: `"RESOURCE_TYPE_UNSPECIFIED"`)

* `INSTANCE` (value: `"INSTANCE"`)

* `AWS_ELB_LOAD_BALANCER` (value: `"AWS_ELB_LOAD_BALANCER"`)




