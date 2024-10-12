# RubrikRestApi.VolumeGroupPatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuredSlaDomainId** | **String** | The ID of the SLA Domain policy to assign to the Volume Group. | [optional] 
**forceFull** | **Boolean** | Determines whether the next snapshot of the Volume Group is a full. After the snapshot has completed, this parameter will be reset to the default false value. | [optional] 
**isPaused** | **Boolean** | Indicates whether backup, archival, and replicated is paused for this Volume Group. | [optional] 
**volumeIdsIncludedInSnapshots** | **[String]** | The unique ID of each volume included in the Volume Group. | [optional] 


