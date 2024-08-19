

# ServingRestriction

Output only. A representation of the status of an ad in a specific context. A context here relates to where something ultimately serves (for example, a user or publisher geo, a platform, an HTTPS versus HTTP request, or the type of auction).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contexts** | [**List&lt;ServingContext&gt;**](ServingContext.md) | The contexts for the restriction. |  [optional] |
|**disapproval** | [**Disapproval**](Disapproval.md) |  |  [optional] |
|**disapprovalReasons** | [**List&lt;Disapproval&gt;**](Disapproval.md) | Any disapprovals bound to this restriction. Only present if status&#x3D;DISAPPROVED. Can be used to filter the response of the creatives.list method. Deprecated; use disapproval field instead. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the creative in this context (for example, it has been explicitly disapproved or is pending review). |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| DISAPPROVAL | &quot;DISAPPROVAL&quot; |
| PENDING_REVIEW | &quot;PENDING_REVIEW&quot; |



