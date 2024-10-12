# AmazonChime.CreateProxySessionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participantPhoneNumbers** | **[String]** | The participant phone numbers. | 
**name** | **String** | The name of the proxy session. | [optional] 
**expiryMinutes** | **Number** | The number of minutes allowed for the proxy session. | [optional] 
**capabilities** | [**[Capability]**](Capability.md) | The proxy session capabilities. | 
**numberSelectionBehavior** | **String** | The preference for proxy phone number reuse, or stickiness, between the same participants across sessions. | [optional] 
**geoMatchLevel** | **String** | The preference for matching the country or area code of the proxy phone number with that of the first participant. | [optional] 
**geoMatchParams** | [**CreateProxySessionRequestGeoMatchParams**](CreateProxySessionRequestGeoMatchParams.md) |  | [optional] 



## Enum: NumberSelectionBehaviorEnum


* `PreferSticky` (value: `"PreferSticky"`)

* `AvoidSticky` (value: `"AvoidSticky"`)





## Enum: GeoMatchLevelEnum


* `Country` (value: `"Country"`)

* `AreaCode` (value: `"AreaCode"`)




