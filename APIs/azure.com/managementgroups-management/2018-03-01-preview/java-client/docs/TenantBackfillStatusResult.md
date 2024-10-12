

# TenantBackfillStatusResult

The tenant backfill status

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | The status of the Tenant Backfill |  [optional] [readonly] |
|**tenantId** | **String** | The AAD Tenant ID associated with the management group. For example, 00000000-0000-0000-0000-000000000000 |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NOT_STARTED | &quot;NotStarted&quot; |
| NOT_STARTED_BUT_GROUPS_EXIST | &quot;NotStartedButGroupsExist&quot; |
| STARTED | &quot;Started&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| COMPLETED | &quot;Completed&quot; |



