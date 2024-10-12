# CloudIdentityApi.DynamicGroupStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **String** | Status of the dynamic group. | [optional] 
**statusTime** | **String** | The latest time at which the dynamic group is guaranteed to be in the given status. If status is &#x60;UP_TO_DATE&#x60;, the latest time at which the dynamic group was confirmed to be up-to-date. If status is &#x60;UPDATING_MEMBERSHIPS&#x60;, the time at which dynamic group was created. | [optional] 



## Enum: StatusEnum


* `STATUS_UNSPECIFIED` (value: `"STATUS_UNSPECIFIED"`)

* `UP_TO_DATE` (value: `"UP_TO_DATE"`)

* `UPDATING_MEMBERSHIPS` (value: `"UPDATING_MEMBERSHIPS"`)

* `INVALID_QUERY` (value: `"INVALID_QUERY"`)




