

# SqlTriggerGetPropertiesResource


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | Body of the Trigger |  [optional] |
|**id** | **String** | Name of the Cosmos DB SQL trigger |  |
|**triggerOperation** | [**TriggerOperationEnum**](#TriggerOperationEnum) | The operation the trigger is associated with |  [optional] |
|**triggerType** | [**TriggerTypeEnum**](#TriggerTypeEnum) | Type of the Trigger |  [optional] |
|**etag** | **String** | A system generated property representing the resource etag required for optimistic concurrency control. |  [optional] [readonly] |
|**rid** | **String** | A system generated property. A unique identifier. |  [optional] [readonly] |
|**ts** | **Object** | A system generated property that denotes the last updated timestamp of the resource. |  [optional] [readonly] |



## Enum: TriggerOperationEnum

| Name | Value |
|---- | -----|
| ALL | &quot;All&quot; |
| CREATE | &quot;Create&quot; |
| UPDATE | &quot;Update&quot; |
| DELETE | &quot;Delete&quot; |
| REPLACE | &quot;Replace&quot; |



## Enum: TriggerTypeEnum

| Name | Value |
|---- | -----|
| PRE | &quot;Pre&quot; |
| POST | &quot;Post&quot; |



