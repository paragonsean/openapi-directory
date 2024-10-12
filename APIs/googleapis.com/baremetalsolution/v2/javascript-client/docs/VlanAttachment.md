# BareMetalSolutionApi.VlanAttachment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Immutable. The identifier of the attachment within vrf. | [optional] 
**interconnectAttachment** | **String** | Optional. The name of the vlan attachment within vrf. This is of the form projects/{project_number}/regions/{region}/interconnectAttachments/{interconnect_attachment} | [optional] 
**pairingKey** | **String** | Input only. Pairing key. | [optional] 
**peerIp** | **String** | The peer IP of the attachment. | [optional] 
**peerVlanId** | **String** | The peer vlan ID of the attachment. | [optional] 
**qosPolicy** | [**QosPolicy**](QosPolicy.md) |  | [optional] 
**routerIp** | **String** | The router IP of the attachment. | [optional] 


