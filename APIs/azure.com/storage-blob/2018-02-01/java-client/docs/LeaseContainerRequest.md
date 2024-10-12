

# LeaseContainerRequest

Lease Container request schema.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | Specifies the lease action. Can be one of the available actions. |  |
|**breakPeriod** | **Integer** | Optional. For a break action, proposed duration the lease should continue before it is broken, in seconds, between 0 and 60. |  [optional] |
|**leaseDuration** | **Integer** | Required for acquire. Specifies the duration of the lease, in seconds, or negative one (-1) for a lease that never expires. |  [optional] |
|**leaseId** | **String** | Identifies the lease. Can be specified in any valid GUID string format. |  [optional] |
|**proposedLeaseId** | **String** | Optional for acquire, required for change. Proposed lease ID, in a GUID string format. |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| ACQUIRE | &quot;Acquire&quot; |
| RENEW | &quot;Renew&quot; |
| CHANGE | &quot;Change&quot; |
| RELEASE | &quot;Release&quot; |
| BREAK | &quot;Break&quot; |



