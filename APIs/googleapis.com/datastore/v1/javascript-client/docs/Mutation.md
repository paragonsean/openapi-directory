# CloudDatastoreApi.Mutation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseVersion** | **String** | The version of the entity that this mutation is being applied to. If this does not match the current version on the server, the mutation conflicts. | [optional] 
**_delete** | [**Key**](Key.md) |  | [optional] 
**insert** | [**Entity**](Entity.md) |  | [optional] 
**update** | [**Entity**](Entity.md) |  | [optional] 
**updateTime** | **String** | The update time of the entity that this mutation is being applied to. If this does not match the current update time on the server, the mutation conflicts. | [optional] 
**upsert** | [**Entity**](Entity.md) |  | [optional] 


