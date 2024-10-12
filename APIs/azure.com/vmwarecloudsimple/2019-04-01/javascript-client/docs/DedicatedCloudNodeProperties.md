# VMwareCloudSimple.DedicatedCloudNodeProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availabilityZoneId** | **String** | Availability Zone id, e.g. \&quot;az1\&quot; | 
**availabilityZoneName** | **String** | Availability Zone name, e.g. \&quot;Availability Zone 1\&quot; | [optional] [readonly] 
**cloudRackName** | **String** | VMWare Cloud Rack Name | [optional] [readonly] 
**created** | **Object** | date time the resource was created | [optional] [readonly] 
**nodesCount** | **Number** | count of nodes to create | 
**placementGroupId** | **String** | Placement Group id, e.g. \&quot;n1\&quot; | 
**placementGroupName** | **String** | Placement Name, e.g. \&quot;Placement Group 1\&quot; | [optional] [readonly] 
**privateCloudId** | **String** | Private Cloud Id | [optional] [readonly] 
**privateCloudName** | **String** | Resource Pool Name | [optional] [readonly] 
**provisioningState** | **String** | The provisioning status of the resource | [optional] [readonly] 
**purchaseId** | **String** | purchase id | 
**skuDescription** | [**SkuDescription**](SkuDescription.md) |  | [optional] 
**status** | **String** | Node status, indicates is private cloud set up on this node or not | [optional] [readonly] 
**vmwareClusterName** | **String** | VMWare Cluster Name | [optional] [readonly] 



## Enum: StatusEnum


* `unused` (value: `"unused"`)

* `used` (value: `"used"`)




