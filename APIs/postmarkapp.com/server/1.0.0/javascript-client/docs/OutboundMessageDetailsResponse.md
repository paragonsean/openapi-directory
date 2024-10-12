# PostmarkApi.OutboundMessageDetailsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**[Attachment]**](Attachment.md) |  | [optional] 
**bcc** | [**[EmailNameAddressPair]**](EmailNameAddressPair.md) |  | [optional] 
**body** | **String** |  | [optional] 
**cc** | [**[EmailNameAddressPair]**](EmailNameAddressPair.md) |  | [optional] 
**from** | **String** |  | [optional] 
**htmlBody** | **String** |  | [optional] 
**messageEvents** | [**[MessageEventDetails]**](MessageEventDetails.md) |  | [optional] 
**messageID** | **String** |  | [optional] 
**receivedAt** | **Date** |  | [optional] 
**recipients** | **[String]** |  | [optional] 
**status** | **String** |  | [optional] 
**subject** | **String** |  | [optional] 
**tag** | **String** |  | [optional] 
**textBody** | **String** |  | [optional] 
**to** | [**[EmailNameAddressPair]**](EmailNameAddressPair.md) |  | [optional] 
**trackLinks** | **String** |  | [optional] 
**trackOpens** | **Boolean** |  | [optional] 



## Enum: TrackLinksEnum


* `None` (value: `"None"`)

* `HtmlAndText` (value: `"HtmlAndText"`)

* `HtmlOnly` (value: `"HtmlOnly"`)

* `TextOnly` (value: `"TextOnly"`)




