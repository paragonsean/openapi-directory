

# ApiV1StatusesPostRequestInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inReplyToId** | **String** | ID of the status being replied to, if status is a reply |  [optional] |
|**language** | **String** | ISO 639 language code for this status. |  [optional] |
|**mediaIds** | **List&lt;String&gt;** | Array of Attachment ids to be attached as media. If provided, &#x60;status&#x60; becomes optional, and &#x60;poll&#x60; cannot be used. |  [optional] |
|**poll** | **Map&lt;Object&gt;** |  |  [optional] |
|**scheduledAt** | **String** | ISO 8601 Datetime at which to schedule a status. Providing this paramter will cause ScheduledStatus to be returned instead of Status. Must be at least 5 minutes in the future. |  [optional] |
|**sensitive** | **Boolean** | Mark status and attached media as sensitive? |  [optional] |
|**spoilerText** | **String** | Text to be shown as a warning or subject before the actual content. Statuses are generally collapsed behind this field. |  [optional] |
|**status** | **String** | Text content of the status. If &#x60;media_ids&#x60; is provided, this becomes optional. Attaching a &#x60;poll&#x60; is optional while &#x60;status&#x60; is provided. |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) | Visibility of the posted status. Enumerable oneOf public, unlisted, private, direct. |  [optional] |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;public&quot; |
| UNLISTED | &quot;unlisted&quot; |
| PRIVATE | &quot;private&quot; |
| DIRECT | &quot;direct&quot; |



