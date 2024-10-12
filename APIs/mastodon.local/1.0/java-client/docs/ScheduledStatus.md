

# ScheduledStatus

Represents a status that will be published at a future scheduled date.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | ID of the scheduled status in the database. Cast from an integer, but not guaranteed to be a number. |  |
|**mediaAttachments** | [**List&lt;Attachment&gt;**](Attachment.md) | Array of attachements |  |
|**params** | [**StatusParams**](StatusParams.md) |  |  |
|**scheduledAt** | **OffsetDateTime** | ID of the status in the database. ISO 8601 Datetime. |  |



