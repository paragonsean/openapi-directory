

# ServerConfigurationResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiTokens** | **List&lt;String&gt;** |  |  [optional] |
|**bounceHookUrl** | **String** |  |  [optional] |
|**clickHookUrl** | **String** |  |  [optional] |
|**color** | [**ColorEnum**](#ColorEnum) |  |  [optional] |
|**deliveryHookUrl** | **String** |  |  [optional] |
|**ID** | **Integer** |  |  [optional] |
|**inboundAddress** | **String** |  |  [optional] |
|**inboundDomain** | **String** |  |  [optional] |
|**inboundHash** | **String** |  |  [optional] |
|**inboundHookUrl** | **String** |  |  [optional] |
|**inboundSpamThreshold** | **Integer** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**openHookUrl** | **String** |  |  [optional] |
|**postFirstOpenOnly** | **Boolean** |  |  [optional] |
|**rawEmailEnabled** | **Boolean** |  |  [optional] |
|**serverLink** | **String** |  |  [optional] |
|**smtpApiActivated** | **Boolean** |  |  [optional] |
|**trackLinks** | [**TrackLinksEnum**](#TrackLinksEnum) |  |  [optional] |
|**trackOpens** | **Boolean** |  |  [optional] |



## Enum: ColorEnum

| Name | Value |
|---- | -----|
| PURPLE | &quot;purple&quot; |
| BLUE | &quot;blue&quot; |
| TURQOISE | &quot;turqoise&quot; |
| GREEN | &quot;green&quot; |
| RED | &quot;red&quot; |
| YELLOW | &quot;yellow&quot; |
| GREY | &quot;grey&quot; |



## Enum: TrackLinksEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| HTML_AND_TEXT | &quot;HtmlAndText&quot; |
| HTML_ONLY | &quot;HtmlOnly&quot; |
| TEXT_ONLY | &quot;TextOnly&quot; |



