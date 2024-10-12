

# GoogleDatastoreAdminV1PrepareStepDetails

Details for the `PREPARE` step.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**concurrencyMode** | [**ConcurrencyModeEnum**](#ConcurrencyModeEnum) | The concurrency mode this database will use when it reaches the &#x60;REDIRECT_WRITES&#x60; step. |  [optional] |



## Enum: ConcurrencyModeEnum

| Name | Value |
|---- | -----|
| CONCURRENCY_MODE_UNSPECIFIED | &quot;CONCURRENCY_MODE_UNSPECIFIED&quot; |
| PESSIMISTIC | &quot;PESSIMISTIC&quot; |
| OPTIMISTIC | &quot;OPTIMISTIC&quot; |
| OPTIMISTIC_WITH_ENTITY_GROUPS | &quot;OPTIMISTIC_WITH_ENTITY_GROUPS&quot; |



