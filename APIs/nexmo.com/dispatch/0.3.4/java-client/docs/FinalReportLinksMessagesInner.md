

# FinalReportLinksMessagesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channel** | [**ChannelEnum**](#ChannelEnum) |  |  [optional] |
|**href** | **String** | Please note GET is not currently supported |  [optional] |
|**messageUuid** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**usage** | [**MessageStatusUsage**](MessageStatusUsage.md) |  |  [optional] |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| MESSENGER | &quot;messenger&quot; |
| VIBER_SEVICE_MSG | &quot;viber_sevice_msg&quot; |
| SMS | &quot;sms&quot; |
| WHATSAPP | &quot;whatsapp&quot; |
| MMS | &quot;mms&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUBMITTED | &quot;submitted&quot; |
| DELIVERED | &quot;delivered&quot; |
| READ | &quot;read&quot; |
| REJECTED | &quot;rejected&quot; |
| UNDELIVERABLE | &quot;undeliverable&quot; |



