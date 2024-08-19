

# SqlTriggerResource

Cosmos DB SQL trigger resource object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | Body of the Trigger |  [optional] |
|**id** | **String** | Name of the Cosmos DB SQL trigger |  |
|**triggerOperation** | [**TriggerOperationEnum**](#TriggerOperationEnum) | The operation the trigger is associated with |  [optional] |
|**triggerType** | [**TriggerTypeEnum**](#TriggerTypeEnum) | Type of the Trigger |  [optional] |



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



