# RubrikRestApi.VolumeGroupForceFullResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volumeGroupId** | **String** | The ID of the Volume group. | 
**volumeInfos** | [**[ForceFullVolumeInfo]**](ForceFullVolumeInfo.md) | Configuration for each volume that has requested a forced full snapshot. If the configuration is absent, that means either a forced full snapshot has not been requested for the Volume Group, or a backup job has taken the requested full snapshot and cleared the configuration. | [optional] 


