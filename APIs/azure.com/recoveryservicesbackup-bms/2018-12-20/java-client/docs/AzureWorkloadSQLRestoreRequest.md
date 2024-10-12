

# AzureWorkloadSQLRestoreRequest

AzureWorkload SQL -specific restore. Specifically for full/diff restore

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alternateDirectoryPaths** | [**List&lt;SQLDataDirectoryMapping&gt;**](SQLDataDirectoryMapping.md) | Data directory details |  [optional] |
|**isNonRecoverable** | **Boolean** | SQL specific property where user can chose to set no-recovery when restore operation is tried |  [optional] |
|**shouldUseAlternateTargetLocation** | **Boolean** | Default option set to true. If this is set to false, alternate data directory must be provided |  [optional] |



