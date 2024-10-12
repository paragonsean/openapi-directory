

# PolicyCompliance

Policy compliance of the creative for a transaction type or a region.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | Serving status for the given transaction type (for example, open auction, deals) or region (for example, China, Russia). Can be used to filter the response of the creatives.list method. |  [optional] |
|**topics** | [**List&lt;PolicyTopicEntry&gt;**](PolicyTopicEntry.md) | Topics related to the policy compliance for this transaction type (for example, open auction, deals) or region (for example, China, Russia). Topics may be present only if status is DISAPPROVED. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| PENDING_REVIEW | &quot;PENDING_REVIEW&quot; |
| DISAPPROVED | &quot;DISAPPROVED&quot; |
| APPROVED | &quot;APPROVED&quot; |
| CERTIFICATE_REQUIRED | &quot;CERTIFICATE_REQUIRED&quot; |



