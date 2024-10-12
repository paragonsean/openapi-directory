

# Cadence


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addedStage** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**archivedAt** | **OffsetDateTime** | Datetime of when the cadence was archived, if archived |  [optional] |
|**bouncedStage** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**cadenceFrameworkId** | **Integer** | ID of the cadence framework used to create steps for the cadence |  [optional] |
|**cadenceFunction** | **String** | The use case of the cadence. Possible values are:  outbound: Denotes an outbound cadence, typically for sales purposes  inbound: Denotes an inbound sales cadence  event: Denotes a cadence used for an upcoming event  other: Denotes a cadence outside of the standard process  |  [optional] |
|**cadencePriority** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**counts** | [**CadenceCounts**](CadenceCounts.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** | Datetime of when the cadence was created |  [optional] |
|**creator** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**draft** | **Boolean** | Whether this cadence is in draft mode |  [optional] |
|**externalIdentifier** | **String** | Cadence External ID |  [optional] |
|**finishedStage** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**groups** | [**List&lt;EmbeddedResource&gt;**](EmbeddedResource.md) | Groups to which this cadence is assigned, if any |  [optional] |
|**id** | **Integer** | ID of cadence |  [optional] |
|**name** | **String** | Cadence name |  [optional] |
|**optOutLinkIncluded** | **Boolean** | Whether this cadence is configured to include an opt-out link by default |  [optional] |
|**owner** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**removeBouncesEnabled** | **Boolean** | Whether this cadence is configured to automatically remove people who have bounced |  [optional] |
|**removeRepliesEnabled** | **Boolean** | Whether this cadence is configured to automatically remove people who have replied |  [optional] |
|**repliedStage** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**shared** | **Boolean** | Whether this cadence is visible to team members (shared) |  [optional] |
|**tags** | **List&lt;String&gt;** | All tags applied to this cadence |  [optional] |
|**teamCadence** | **Boolean** | Whether this cadence is a team cadence.  A team cadence is created by an admin and can be run by all users |  [optional] |
|**updatedAt** | **OffsetDateTime** | Datetime of when the cadence was last updated |  [optional] |



