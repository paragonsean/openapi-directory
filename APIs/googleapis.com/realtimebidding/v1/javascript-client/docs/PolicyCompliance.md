# RealTimeBiddingApi.PolicyCompliance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **String** | Serving status for the given transaction type (for example, open auction, deals) or region (for example, China, Russia). Can be used to filter the response of the creatives.list method. | [optional] 
**topics** | [**[PolicyTopicEntry]**](PolicyTopicEntry.md) | Topics related to the policy compliance for this transaction type (for example, open auction, deals) or region (for example, China, Russia). Topics may be present only if status is DISAPPROVED. | [optional] 



## Enum: StatusEnum


* `STATUS_UNSPECIFIED` (value: `"STATUS_UNSPECIFIED"`)

* `PENDING_REVIEW` (value: `"PENDING_REVIEW"`)

* `DISAPPROVED` (value: `"DISAPPROVED"`)

* `APPROVED` (value: `"APPROVED"`)

* `CERTIFICATE_REQUIRED` (value: `"CERTIFICATE_REQUIRED"`)




