# PostmarkApi.SendEmailRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**[Attachment]**](Attachment.md) |  | [optional] 
**bcc** | **String** | Bcc recipient email address. Multiple addresses are comma seperated. Max 50. | [optional] 
**cc** | **String** | Recipient email address. Multiple addresses are comma seperated. Max 50. | [optional] 
**from** | **String** | The sender email address. Must have a registered and confirmed Sender Signature. | [optional] 
**headers** | [**[MessageHeader]**](MessageHeader.md) |  | [optional] 
**htmlBody** | **String** | If no TextBody specified HTML email message | [optional] 
**replyTo** | **String** | Reply To override email address. Defaults to the Reply To set in the sender signature. | [optional] 
**subject** | **String** | Email Subject | [optional] 
**tag** | **String** | Email tag that allows you to categorize outgoing emails and get detailed statistics. | [optional] 
**textBody** | **String** | If no HtmlBody specified Plain text email message | [optional] 
**to** | **String** | Recipient email address. Multiple addresses are comma seperated. Max 50. | [optional] 
**trackLinks** | **String** | Replace links in content to enable \&quot;click tracking\&quot; stats. Default is &#39;null&#39;, which uses the server&#39;s LinkTracking setting&#39;. | [optional] 
**trackOpens** | **Boolean** | Activate open tracking for this email. | [optional] 



## Enum: TrackLinksEnum


* `None` (value: `"None"`)

* `HtmlAndText` (value: `"HtmlAndText"`)

* `HtmlOnly` (value: `"HtmlOnly"`)

* `TextOnly` (value: `"TextOnly"`)




