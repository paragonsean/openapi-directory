# CosmosDb.SqlTriggerGetPropertiesResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **String** | Body of the Trigger | [optional] 
**id** | **String** | Name of the Cosmos DB SQL trigger | 
**triggerOperation** | **String** | The operation the trigger is associated with | [optional] 
**triggerType** | **String** | Type of the Trigger | [optional] 
**etag** | **String** | A system generated property representing the resource etag required for optimistic concurrency control. | [optional] [readonly] 
**rid** | **String** | A system generated property. A unique identifier. | [optional] [readonly] 
**ts** | **Object** | A system generated property that denotes the last updated timestamp of the resource. | [optional] [readonly] 



## Enum: TriggerOperationEnum


* `All` (value: `"All"`)

* `Create` (value: `"Create"`)

* `Update` (value: `"Update"`)

* `Delete` (value: `"Delete"`)

* `Replace` (value: `"Replace"`)





## Enum: TriggerTypeEnum


* `Pre` (value: `"Pre"`)

* `Post` (value: `"Post"`)




