

# PartitionJsonldGet

The Partition resource is a collection of siloed monitor and alert environments in the user account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atContext** | [**AlertLogJsonldGetContext**](AlertLogJsonldGetContext.md) |  |  [optional] |
|**atId** | **String** |  |  [optional] [readonly] |
|**atType** | **String** |  |  [optional] [readonly] |
|**alertServices** | **List&lt;String&gt;** | The alert services that are related to this resource. |  [optional] |
|**createdAt** | **OffsetDateTime** | When the resource instance was created. This date-time is in the UTC timezone. |  [optional] [readonly] |
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**id** | **UUID** | The unique identifier of the resource instance. |  [optional] [readonly] |
|**monitors** | **List&lt;String&gt;** | The monitors that are associated with this partition. |  [optional] |
|**partitionName** | **String** | The name of the partition. Max 255 characters. |  |
|**partitionNotes** | **String** | Notes about the partition. Max 10,000 characters. Formatting using Markdown is allowed. HTML will be removed. |  [optional] |
|**resourceOwner** | **String** | The name of the person who owns this resource. |  [optional] |
|**teamInvitations** | **List&lt;String&gt;** | The team invitations that are related to this resource. |  [optional] |
|**teamMembers** | **List&lt;String&gt;** | The team members of this resource. |  [optional] |



