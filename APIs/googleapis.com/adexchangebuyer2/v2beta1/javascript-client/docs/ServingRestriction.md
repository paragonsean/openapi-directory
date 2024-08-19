# AdExchangeBuyerApiIi.ServingRestriction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contexts** | [**[ServingContext]**](ServingContext.md) | The contexts for the restriction. | [optional] 
**disapproval** | [**Disapproval**](Disapproval.md) |  | [optional] 
**disapprovalReasons** | [**[Disapproval]**](Disapproval.md) | Any disapprovals bound to this restriction. Only present if status&#x3D;DISAPPROVED. Can be used to filter the response of the creatives.list method. Deprecated; use disapproval field instead. | [optional] 
**status** | **String** | The status of the creative in this context (for example, it has been explicitly disapproved or is pending review). | [optional] 



## Enum: StatusEnum


* `STATUS_UNSPECIFIED` (value: `"STATUS_UNSPECIFIED"`)

* `DISAPPROVAL` (value: `"DISAPPROVAL"`)

* `PENDING_REVIEW` (value: `"PENDING_REVIEW"`)




