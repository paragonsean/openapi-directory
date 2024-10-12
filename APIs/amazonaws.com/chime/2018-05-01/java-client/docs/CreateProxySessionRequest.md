

# CreateProxySessionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**participantPhoneNumbers** | **List&lt;String&gt;** | The participant phone numbers. |  |
|**name** | **String** | The name of the proxy session. |  [optional] |
|**expiryMinutes** | **Integer** | The number of minutes allowed for the proxy session. |  [optional] |
|**capabilities** | **List&lt;Capability&gt;** | The proxy session capabilities. |  |
|**numberSelectionBehavior** | [**NumberSelectionBehaviorEnum**](#NumberSelectionBehaviorEnum) | The preference for proxy phone number reuse, or stickiness, between the same participants across sessions. |  [optional] |
|**geoMatchLevel** | [**GeoMatchLevelEnum**](#GeoMatchLevelEnum) | The preference for matching the country or area code of the proxy phone number with that of the first participant. |  [optional] |
|**geoMatchParams** | [**CreateProxySessionRequestGeoMatchParams**](CreateProxySessionRequestGeoMatchParams.md) |  |  [optional] |



## Enum: NumberSelectionBehaviorEnum

| Name | Value |
|---- | -----|
| PREFER_STICKY | &quot;PreferSticky&quot; |
| AVOID_STICKY | &quot;AvoidSticky&quot; |



## Enum: GeoMatchLevelEnum

| Name | Value |
|---- | -----|
| COUNTRY | &quot;Country&quot; |
| AREA_CODE | &quot;AreaCode&quot; |



