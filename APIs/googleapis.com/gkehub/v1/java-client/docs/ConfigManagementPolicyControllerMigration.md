

# ConfigManagementPolicyControllerMigration

State for the migration of PolicyController from ACM -> PoCo Hub.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**copyTime** | **String** | Last time this membership spec was copied to PoCo feature. |  [optional] |
|**stage** | [**StageEnum**](#StageEnum) | Stage of the migration. |  [optional] |



## Enum: StageEnum

| Name | Value |
|---- | -----|
| STAGE_UNSPECIFIED | &quot;STAGE_UNSPECIFIED&quot; |
| ACM_MANAGED | &quot;ACM_MANAGED&quot; |
| POCO_MANAGED | &quot;POCO_MANAGED&quot; |



