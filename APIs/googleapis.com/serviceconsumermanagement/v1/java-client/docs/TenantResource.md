

# TenantResource

Resource constituting the TenancyUnit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**resource** | **String** | Output only. @OutputOnly Identifier of the tenant resource. For cloud projects, it is in the form &#39;projects/{number}&#39;. For example &#39;projects/123456&#39;. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of tenant resource. |  [optional] |
|**tag** | **String** | Unique per single tenancy unit. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| PENDING_CREATE | &quot;PENDING_CREATE&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| PENDING_DELETE | &quot;PENDING_DELETE&quot; |
| FAILED | &quot;FAILED&quot; |
| DELETED | &quot;DELETED&quot; |



