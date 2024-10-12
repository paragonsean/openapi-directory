# CampaignManager360Api.ReportDelivery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emailOwner** | **Boolean** | Whether the report should be emailed to the report owner. | [optional] 
**emailOwnerDeliveryType** | **String** | The type of delivery for the owner to receive, if enabled. | [optional] 
**message** | **String** | The message to be sent with each email. | [optional] 
**recipients** | [**[Recipient]**](Recipient.md) | The list of recipients to which to email the report. | [optional] 



## Enum: EmailOwnerDeliveryTypeEnum


* `LINK` (value: `"LINK"`)

* `ATTACHMENT` (value: `"ATTACHMENT"`)




