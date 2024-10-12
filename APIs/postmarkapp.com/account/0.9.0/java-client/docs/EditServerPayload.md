

# EditServerPayload



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bounceHookUrl** | **String** |  |  [optional] |
|**clickHookUrl** | **String** |  |  [optional] |
|**color** | **String** |  |  [optional] |
|**deliveryHookUrl** | **String** |  |  [optional] |
|**inboundDomain** | **String** |  |  [optional] |
|**inboundHookUrl** | **String** |  |  [optional] |
|**inboundSpamThreshold** | **Integer** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**openHookUrl** | **String** |  |  [optional] |
|**postFirstOpenOnly** | **Boolean** |  |  [optional] |
|**rawEmailEnabled** | **Boolean** |  |  [optional] |
|**smtpApiActivated** | **Boolean** |  |  [optional] |
|**trackLinks** | [**TrackLinksEnum**](#TrackLinksEnum) |  |  [optional] |
|**trackOpens** | **Boolean** |  |  [optional] |



## Enum: TrackLinksEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| HTML_AND_TEXT_TRACKING | &quot;HtmlAndTextTracking&quot; |
| HTML_ONLY_TRACKING | &quot;HtmlOnlyTracking&quot; |
| TEXT_ONLY_TRACKING | &quot;TextOnlyTracking&quot; |



