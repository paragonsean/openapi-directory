# BackupForGkeApi.ClusterResourceRestoreScope

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allGroupKinds** | **Boolean** | Optional. If True, all valid cluster-scoped resources will be restored. Mutually exclusive to any other field in the message. | [optional] 
**excludedGroupKinds** | [**[GroupKind]**](GroupKind.md) | Optional. A list of cluster-scoped resource group kinds to NOT restore from the backup. If specified, all valid cluster-scoped resources will be restored except for those specified in the list. Mutually exclusive to any other field in the message. | [optional] 
**noGroupKinds** | **Boolean** | Optional. If True, no cluster-scoped resources will be restored. This has the same restore scope as if the message is not defined. Mutually exclusive to any other field in the message. | [optional] 
**selectedGroupKinds** | [**[GroupKind]**](GroupKind.md) | Optional. A list of cluster-scoped resource group kinds to restore from the backup. If specified, only the selected resources will be restored. Mutually exclusive to any other field in the message. | [optional] 


