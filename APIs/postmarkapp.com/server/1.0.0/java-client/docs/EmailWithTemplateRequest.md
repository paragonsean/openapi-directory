

# EmailWithTemplateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachments** | [**List&lt;Attachment&gt;**](Attachment.md) |  |  [optional] |
|**bcc** | **String** |  |  [optional] |
|**cc** | **String** |  |  [optional] |
|**from** | **String** |  |  |
|**headers** | [**List&lt;MessageHeader&gt;**](MessageHeader.md) |  |  [optional] |
|**inlineCss** | **Boolean** |  |  [optional] |
|**replyTo** | **String** |  |  [optional] |
|**tag** | **String** |  |  [optional] |
|**templateAlias** | **String** | Required if &#39;TemplateId&#39; is not specified. |  |
|**templateId** | **Integer** | Required if &#39;TemplateAlias&#39; is not specified. |  |
|**templateModel** | **Object** |  |  |
|**to** | **String** |  |  |
|**trackLinks** | [**TrackLinksEnum**](#TrackLinksEnum) | Replace links in content to enable \&quot;click tracking\&quot; stats. Default is &#39;null&#39;, which uses the server&#39;s LinkTracking setting&#39;. |  [optional] |
|**trackOpens** | **Boolean** | Activate open tracking for this email. |  [optional] |



## Enum: TrackLinksEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| HTML_AND_TEXT | &quot;HtmlAndText&quot; |
| HTML_ONLY | &quot;HtmlOnly&quot; |
| TEXT_ONLY | &quot;TextOnly&quot; |



