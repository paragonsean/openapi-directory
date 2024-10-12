# StorageManagementClient.MigrationResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containerName** | **String** | The name of the container to be migrated. | [optional] [readonly] 
**destinationShareName** | **String** | The name of the destination storage share. | [optional] [readonly] 
**failureReason** | **String** | The migration failure reason. | [optional] [readonly] 
**jobId** | **String** | The migration job ID. | [optional] [readonly] 
**migrationStatus** | [**MigrationState**](MigrationState.md) |  | [optional] 
**sourceShareName** | **String** | The name of the source storage share. | [optional] [readonly] 
**storageAccountName** | **String** | The storage account name. | [optional] [readonly] 
**subEntitiesCompleted** | **Number** | The number of entities which have been migrated. | [optional] [readonly] 
**subEntitiesFailed** | **Number** | The number of entities which failed in migration. | [optional] [readonly] 


