# ServiceConsumerManagementApi.TenantResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **String** | Output only. @OutputOnly Identifier of the tenant resource. For cloud projects, it is in the form &#39;projects/{number}&#39;. For example &#39;projects/123456&#39;. | [optional] [readonly] 
**status** | **String** | Status of tenant resource. | [optional] 
**tag** | **String** | Unique per single tenancy unit. | [optional] 



## Enum: StatusEnum


* `STATUS_UNSPECIFIED` (value: `"STATUS_UNSPECIFIED"`)

* `PENDING_CREATE` (value: `"PENDING_CREATE"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `PENDING_DELETE` (value: `"PENDING_DELETE"`)

* `FAILED` (value: `"FAILED"`)

* `DELETED` (value: `"DELETED"`)




