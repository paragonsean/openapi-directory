# PostmarkApi.EditServerConfigurationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounceHookUrl** | **String** |  | [optional] 
**clickHookUrl** | **String** | Webhook url allowing real-time notification when tracked links are clicked. | [optional] 
**color** | **String** |  | [optional] 
**deliveryHookUrl** | **String** |  | [optional] 
**inboundDomain** | **String** |  | [optional] 
**inboundHookUrl** | **String** |  | [optional] 
**inboundSpamThreshold** | **Number** |  | [optional] 
**name** | **String** |  | [optional] 
**openHookUrl** | **String** |  | [optional] 
**postFirstOpenOnly** | **Boolean** |  | [optional] 
**rawEmailEnabled** | **Boolean** |  | [optional] 
**smtpApiActivated** | **Boolean** |  | [optional] 
**trackLinks** | **String** |  | [optional] 
**trackOpens** | **Boolean** |  | [optional] 



## Enum: ColorEnum


* `purple` (value: `"purple"`)

* `blue` (value: `"blue"`)

* `turqoise` (value: `"turqoise"`)

* `green` (value: `"green"`)

* `red` (value: `"red"`)

* `yellow` (value: `"yellow"`)

* `grey` (value: `"grey"`)





## Enum: TrackLinksEnum


* `None` (value: `"None"`)

* `HtmlAndText` (value: `"HtmlAndText"`)

* `HtmlOnly` (value: `"HtmlOnly"`)

* `TextOnly` (value: `"TextOnly"`)




