# RubrikRestApi.HostShareDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **String** | The domain of the SMB share. | [optional] 
**exportPoint** | **String** | The NFS export point or SMB share name for the NAS share. | 
**hostId** | **String** | The host ID of the NAS Share host. | [optional] 
**hostShareParameters** | [**HostShareParameters**](HostShareParameters.md) |  | [optional] 
**hostname** | **String** | The hostname of the NAS host. | 
**id** | **String** | The unique ID of the NAS Share. | 
**primaryClusterId** | **String** | The ID of the primary Rubrik cluster. | 
**shareType** | **String** | The type of NAS share. | 
**status** | **String** | The status of connection between the Rubrik cluster and the NAS Share. Possible responses are Connected and Disconnected. | 
**username** | **String** | The username to access the NAS share. | [optional] 
**vendorType** | [**NasVendorType**](NasVendorType.md) |  | [optional] 



## Enum: ShareTypeEnum


* `NFS` (value: `"NFS"`)

* `SMB` (value: `"SMB"`)




