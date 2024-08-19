# PostmarkApi.EmailWithTemplateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**[Attachment]**](Attachment.md) |  | [optional] 
**bcc** | **String** |  | [optional] 
**cc** | **String** |  | [optional] 
**from** | **String** |  | 
**headers** | [**[MessageHeader]**](MessageHeader.md) |  | [optional] 
**inlineCss** | **Boolean** |  | [optional] [default to true]
**replyTo** | **String** |  | [optional] 
**tag** | **String** |  | [optional] 
**templateAlias** | **String** | Required if &#39;TemplateId&#39; is not specified. | 
**templateId** | **Number** | Required if &#39;TemplateAlias&#39; is not specified. | 
**templateModel** | **Object** |  | 
**to** | **String** |  | 
**trackLinks** | **String** | Replace links in content to enable \&quot;click tracking\&quot; stats. Default is &#39;null&#39;, which uses the server&#39;s LinkTracking setting&#39;. | [optional] 
**trackOpens** | **Boolean** | Activate open tracking for this email. | [optional] 



## Enum: TrackLinksEnum


* `None` (value: `"None"`)

* `HtmlAndText` (value: `"HtmlAndText"`)

* `HtmlOnly` (value: `"HtmlOnly"`)

* `TextOnly` (value: `"TextOnly"`)




