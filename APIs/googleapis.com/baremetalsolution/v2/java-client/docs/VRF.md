

# VRF

A network VRF.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the VRF. |  [optional] |
|**qosPolicy** | [**QosPolicy**](QosPolicy.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The possible state of VRF. |  [optional] |
|**vlanAttachments** | [**List&lt;VlanAttachment&gt;**](VlanAttachment.md) | The list of VLAN attachments for the VRF. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PROVISIONING | &quot;PROVISIONING&quot; |
| PROVISIONED | &quot;PROVISIONED&quot; |



