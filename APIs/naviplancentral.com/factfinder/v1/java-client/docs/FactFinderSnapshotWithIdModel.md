

# FactFinderSnapshotWithIdModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** |  |  [optional] |
|**factFinderData** | [**IFactFinderSnapshotDomainObject**](IFactFinderSnapshotDomainObject.md) |  |  [optional] |
|**factFinderId** | **Integer** |  |  [optional] |
|**factFinderStatus** | [**FactFinderStatusEnum**](#FactFinderStatusEnum) |  |  [optional] |
|**snapshotId** | **Integer** |  |  [optional] |



## Enum: FactFinderStatusEnum

| Name | Value |
|---- | -----|
| NEW | &quot;New&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| CLIENT_SUBMITTED | &quot;ClientSubmitted&quot; |
| ADVISOR_ACCEPTED | &quot;AdvisorAccepted&quot; |
| CANCELED | &quot;Canceled&quot; |
| DRAFT | &quot;Draft&quot; |
| DELETED | &quot;Deleted&quot; |



