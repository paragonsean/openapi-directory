# ComputeManagementClient.ProximityPlacementGroupProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availabilitySets** | [**[SubResourceWithColocationStatus]**](SubResourceWithColocationStatus.md) | A list of references to all availability sets in the proximity placement group. | [optional] [readonly] 
**colocationStatus** | [**InstanceViewStatus**](InstanceViewStatus.md) |  | [optional] 
**proximityPlacementGroupType** | **String** | Specifies the type of the proximity placement group. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; **Standard** : Co-locate resources within an Azure region or Availability Zone. &lt;br&gt;&lt;br&gt; **Ultra** : For future use. | [optional] 
**virtualMachineScaleSets** | [**[SubResourceWithColocationStatus]**](SubResourceWithColocationStatus.md) | A list of references to all virtual machine scale sets in the proximity placement group. | [optional] [readonly] 
**virtualMachines** | [**[SubResourceWithColocationStatus]**](SubResourceWithColocationStatus.md) | A list of references to all virtual machines in the proximity placement group. | [optional] [readonly] 



## Enum: ProximityPlacementGroupTypeEnum


* `Standard` (value: `"Standard"`)

* `Ultra` (value: `"Ultra"`)




