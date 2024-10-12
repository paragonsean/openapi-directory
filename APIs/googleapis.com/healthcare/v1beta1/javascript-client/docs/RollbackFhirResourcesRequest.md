# CloudHealthcareApi.RollbackFhirResourcesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changeType** | **String** | Optional. CREATE/UPDATE/DELETE/ALL for reverting all txns of a certain type. | [optional] 
**excludeRollbacks** | **Boolean** | Optional. Specifies whether to exclude earlier rollbacks. | [optional] 
**filteringFields** | [**RollbackFhirResourceFilteringFields**](RollbackFhirResourceFilteringFields.md) |  | [optional] 
**force** | **Boolean** | Optional. When enabled, changes will be reverted without explicit confirmation | [optional] 
**inputGcsObject** | **String** | Optional. Cloud Storage object containing list of {resourceType}/{resourceId} lines, identifying resources to be reverted | [optional] 
**resultGcsBucket** | **String** | Required. Bucket to deposit result | [optional] 
**rollbackTime** | **String** | Required. Time point to rollback to. | [optional] 
**type** | **[String]** | Optional. If specified, revert only resources of these types | [optional] 



## Enum: ChangeTypeEnum


* `CHANGE_TYPE_UNSPECIFIED` (value: `"CHANGE_TYPE_UNSPECIFIED"`)

* `ALL` (value: `"ALL"`)

* `CREATE` (value: `"CREATE"`)

* `UPDATE` (value: `"UPDATE"`)

* `DELETE` (value: `"DELETE"`)




