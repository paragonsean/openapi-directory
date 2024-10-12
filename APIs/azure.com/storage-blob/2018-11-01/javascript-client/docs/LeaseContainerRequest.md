# StorageManagementClient.LeaseContainerRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | Specifies the lease action. Can be one of the available actions. | 
**breakPeriod** | **Number** | Optional. For a break action, proposed duration the lease should continue before it is broken, in seconds, between 0 and 60. | [optional] 
**leaseDuration** | **Number** | Required for acquire. Specifies the duration of the lease, in seconds, or negative one (-1) for a lease that never expires. | [optional] 
**leaseId** | **String** | Identifies the lease. Can be specified in any valid GUID string format. | [optional] 
**proposedLeaseId** | **String** | Optional for acquire, required for change. Proposed lease ID, in a GUID string format. | [optional] 



## Enum: ActionEnum


* `Acquire` (value: `"Acquire"`)

* `Renew` (value: `"Renew"`)

* `Change` (value: `"Change"`)

* `Release` (value: `"Release"`)

* `Break` (value: `"Break"`)




