# ComputeManagementClient.DedicatedHostGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**DedicatedHostGroupProperties**](DedicatedHostGroupProperties.md) |  | [optional] 
**zones** | **[String]** | Availability Zone to use for this host group. Only single zone is supported. The zone can be assigned only during creation. If not provided, the group supports all zones in the region. If provided, enforces each host in the group to be in the same zone. | [optional] 
**id** | **String** | Resource Id | [optional] [readonly] 
**location** | **String** | Resource location | 
**name** | **String** | Resource name | [optional] [readonly] 
**tags** | **{String: String}** | Resource tags | [optional] 
**type** | **String** | Resource type | [optional] [readonly] 


