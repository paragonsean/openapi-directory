# ManagementGroups.TenantBackfillStatusResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **String** | The status of the Tenant Backfill | [optional] [readonly] 
**tenantId** | **String** | The AAD Tenant ID associated with the management group. For example, 00000000-0000-0000-0000-000000000000 | [optional] [readonly] 



## Enum: StatusEnum


* `NotStarted` (value: `"NotStarted"`)

* `NotStartedButGroupsExist` (value: `"NotStartedButGroupsExist"`)

* `Started` (value: `"Started"`)

* `Failed` (value: `"Failed"`)

* `Cancelled` (value: `"Cancelled"`)

* `Completed` (value: `"Completed"`)




