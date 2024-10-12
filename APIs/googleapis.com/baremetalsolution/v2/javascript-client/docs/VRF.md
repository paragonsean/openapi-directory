# BareMetalSolutionApi.VRF

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the VRF. | [optional] 
**qosPolicy** | [**QosPolicy**](QosPolicy.md) |  | [optional] 
**state** | **String** | The possible state of VRF. | [optional] 
**vlanAttachments** | [**[VlanAttachment]**](VlanAttachment.md) | The list of VLAN attachments for the VRF. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PROVISIONING` (value: `"PROVISIONING"`)

* `PROVISIONED` (value: `"PROVISIONED"`)




