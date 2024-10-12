

# ReportDelivery

The report's email delivery settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**emailOwner** | **Boolean** | Whether the report should be emailed to the report owner. |  [optional] |
|**emailOwnerDeliveryType** | [**EmailOwnerDeliveryTypeEnum**](#EmailOwnerDeliveryTypeEnum) | The type of delivery for the owner to receive, if enabled. |  [optional] |
|**message** | **String** | The message to be sent with each email. |  [optional] |
|**recipients** | [**List&lt;Recipient&gt;**](Recipient.md) | The list of recipients to which to email the report. |  [optional] |



## Enum: EmailOwnerDeliveryTypeEnum

| Name | Value |
|---- | -----|
| LINK | &quot;LINK&quot; |
| ATTACHMENT | &quot;ATTACHMENT&quot; |



