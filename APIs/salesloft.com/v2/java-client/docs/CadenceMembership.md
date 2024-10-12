

# CadenceMembership


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addedAt** | **OffsetDateTime** | Datetime of when the person was last added to this cadence |  [optional] |
|**cadence** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**counts** | [**CadenceMembershipCounts**](CadenceMembershipCounts.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** | Datetime of when the person was first added to this cadence |  [optional] |
|**currentState** | **String** | The current state of the person on the cadence. Possible values are:  processing: The person is being processed on a cadence. Cadence-related changes cannot be made at this time  staged: The person is waiting for the first step in the cadence to occur  active: The cadence has begun processing this person and is still in the process, but idle  scheduled: The cadence has begun processing this person and is still in the process, with an activity scheduled to occur  completed: The cadence has been completed for this person  removed: The person was manually or automatically removed from the cadence  removed_no_action: The person was removed from the cadence before any action occurred  reassigned: The person&#39;s cadence execution was transferred to a different user, ending this user&#39;s interaction  |  [optional] |
|**currentlyOnCadence** | **Boolean** | Whether the person is currently on the cadence |  [optional] |
|**id** | **Integer** | Cadence membership ID |  [optional] |
|**latestAction** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**person** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**personDeleted** | **Boolean** | Whether the associated person has since been deleted |  [optional] |
|**updatedAt** | **OffsetDateTime** | Datetime of when the record was last updated |  [optional] |
|**user** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |



