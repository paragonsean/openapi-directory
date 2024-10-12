# MicrosoftNetApp.VolumeProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationToken** | **String** | A unique file path for the volume. Used when creating mount targets | 
**exportPolicy** | [**VolumePatchPropertiesExportPolicy**](VolumePatchPropertiesExportPolicy.md) |  | [optional] 
**fileSystemId** | **String** | Unique FileSystem Identifier. | [optional] [readonly] 
**provisioningState** | **String** | Azure lifecycle management | [optional] [readonly] 
**serviceLevel** | **String** | The service level of the file system | [default to &#39;Premium&#39;]
**subnetId** | **String** | The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes | [optional] 
**usageThreshold** | **Number** | Maximum storage quota allowed for a file system in bytes. This is a soft quota used for alerting only. Minimum size is 100 GiB. Upper limit is 100TiB. | [optional] [default to 107374182400]



## Enum: ServiceLevelEnum


* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)

* `Ultra` (value: `"Ultra"`)




