# MerakiDashboardApi.UpdateNetworkWirelessRfProfileRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apBandSettings** | [**UpdateNetworkWirelessRfProfileRequestApBandSettings**](UpdateNetworkWirelessRfProfileRequestApBandSettings.md) |  | [optional] 
**bandSelectionType** | **String** | Band selection can be set to either &#39;ssid&#39; or &#39;ap&#39;. | [optional] 
**clientBalancingEnabled** | **Boolean** | Steers client to best available access point. Can be either true or false. | [optional] 
**fiveGhzSettings** | [**UpdateNetworkWirelessRfProfileRequestFiveGhzSettings**](UpdateNetworkWirelessRfProfileRequestFiveGhzSettings.md) |  | [optional] 
**minBitrateType** | **String** | Minimum bitrate can be set to either &#39;band&#39; or &#39;ssid&#39;. | [optional] 
**name** | **String** | The name of the new profile. Must be unique. | [optional] 
**twoFourGhzSettings** | [**UpdateNetworkWirelessRfProfileRequestTwoFourGhzSettings**](UpdateNetworkWirelessRfProfileRequestTwoFourGhzSettings.md) |  | [optional] 



## Enum: BandSelectionTypeEnum


* `ap` (value: `"ap"`)

* `ssid` (value: `"ssid"`)





## Enum: MinBitrateTypeEnum


* `band` (value: `"band"`)

* `ssid` (value: `"ssid"`)




