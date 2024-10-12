

# AssignmentLockSettings

Defines how resources deployed by a blueprint assignment are locked.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**excludedPrincipals** | **List&lt;String&gt;** | List of AAD principals excluded from blueprint locks. Up to 5 principals are permitted. |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | Lock mode. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| ALL_RESOURCES_READ_ONLY | &quot;AllResourcesReadOnly&quot; |
| ALL_RESOURCES_DO_NOT_DELETE | &quot;AllResourcesDoNotDelete&quot; |



