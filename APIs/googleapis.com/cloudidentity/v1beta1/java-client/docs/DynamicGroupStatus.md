

# DynamicGroupStatus

The current status of a dynamic group along with timestamp.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | Status of the dynamic group. |  [optional] |
|**statusTime** | **String** | The latest time at which the dynamic group is guaranteed to be in the given status. If status is &#x60;UP_TO_DATE&#x60;, the latest time at which the dynamic group was confirmed to be up-to-date. If status is &#x60;UPDATING_MEMBERSHIPS&#x60;, the time at which dynamic group was created. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| UP_TO_DATE | &quot;UP_TO_DATE&quot; |
| UPDATING_MEMBERSHIPS | &quot;UPDATING_MEMBERSHIPS&quot; |
| INVALID_QUERY | &quot;INVALID_QUERY&quot; |



