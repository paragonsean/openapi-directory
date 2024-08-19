

# OutboundMessageDetailsResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachments** | [**List&lt;Attachment&gt;**](Attachment.md) |  |  [optional] |
|**bcc** | [**List&lt;EmailNameAddressPair&gt;**](EmailNameAddressPair.md) |  |  [optional] |
|**body** | **String** |  |  [optional] |
|**cc** | [**List&lt;EmailNameAddressPair&gt;**](EmailNameAddressPair.md) |  |  [optional] |
|**from** | **String** |  |  [optional] |
|**htmlBody** | **String** |  |  [optional] |
|**messageEvents** | [**List&lt;MessageEventDetails&gt;**](MessageEventDetails.md) |  |  [optional] |
|**messageID** | **String** |  |  [optional] |
|**receivedAt** | **OffsetDateTime** |  |  [optional] |
|**recipients** | **List&lt;String&gt;** |  |  [optional] |
|**status** | **String** |  |  [optional] |
|**subject** | **String** |  |  [optional] |
|**tag** | **String** |  |  [optional] |
|**textBody** | **String** |  |  [optional] |
|**to** | [**List&lt;EmailNameAddressPair&gt;**](EmailNameAddressPair.md) |  |  [optional] |
|**trackLinks** | [**TrackLinksEnum**](#TrackLinksEnum) |  |  [optional] |
|**trackOpens** | **Boolean** |  |  [optional] |



## Enum: TrackLinksEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| HTML_AND_TEXT | &quot;HtmlAndText&quot; |
| HTML_ONLY | &quot;HtmlOnly&quot; |
| TEXT_ONLY | &quot;TextOnly&quot; |



