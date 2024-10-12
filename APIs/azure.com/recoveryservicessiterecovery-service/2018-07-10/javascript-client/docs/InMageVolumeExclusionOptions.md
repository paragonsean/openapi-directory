# SiteRecoveryManagementClient.InMageVolumeExclusionOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**onlyExcludeIfSingleVolume** | **String** | The value indicating whether to exclude multi volume disk or not. If a disk has multiple volumes and one of the volume has label matching with VolumeLabel this disk will be excluded from replication if OnlyExcludeIfSingleVolume is false. | [optional] 
**volumeLabel** | **String** | The volume label. The disk having any volume with this label will be excluded from replication. | [optional] 


