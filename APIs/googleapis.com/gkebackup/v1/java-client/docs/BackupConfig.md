

# BackupConfig

BackupConfig defines the configuration of Backups created via this BackupPlan.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allNamespaces** | **Boolean** | If True, include all namespaced resources |  [optional] |
|**encryptionKey** | [**EncryptionKey**](EncryptionKey.md) |  |  [optional] |
|**includeSecrets** | **Boolean** | Optional. This flag specifies whether Kubernetes Secret resources should be included when they fall into the scope of Backups. Default: False |  [optional] |
|**includeVolumeData** | **Boolean** | Optional. This flag specifies whether volume data should be backed up when PVCs are included in the scope of a Backup. Default: False |  [optional] |
|**selectedApplications** | [**NamespacedNames**](NamespacedNames.md) |  |  [optional] |
|**selectedNamespaces** | [**Namespaces**](Namespaces.md) |  |  [optional] |



