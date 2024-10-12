

# RollbackFhirResourcesRequest

Request to roll back resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**changeType** | [**ChangeTypeEnum**](#ChangeTypeEnum) | Optional. CREATE/UPDATE/DELETE/ALL for reverting all txns of a certain type. |  [optional] |
|**excludeRollbacks** | **Boolean** | Optional. Specifies whether to exclude earlier rollbacks. |  [optional] |
|**filteringFields** | [**RollbackFhirResourceFilteringFields**](RollbackFhirResourceFilteringFields.md) |  |  [optional] |
|**force** | **Boolean** | Optional. When enabled, changes will be reverted without explicit confirmation |  [optional] |
|**inputGcsObject** | **String** | Optional. Cloud Storage object containing list of {resourceType}/{resourceId} lines, identifying resources to be reverted |  [optional] |
|**resultGcsBucket** | **String** | Required. Bucket to deposit result |  [optional] |
|**rollbackTime** | **String** | Required. Time point to rollback to. |  [optional] |
|**type** | **List&lt;String&gt;** | Optional. If specified, revert only resources of these types |  [optional] |



## Enum: ChangeTypeEnum

| Name | Value |
|---- | -----|
| CHANGE_TYPE_UNSPECIFIED | &quot;CHANGE_TYPE_UNSPECIFIED&quot; |
| ALL | &quot;ALL&quot; |
| CREATE | &quot;CREATE&quot; |
| UPDATE | &quot;UPDATE&quot; |
| DELETE | &quot;DELETE&quot; |



