

# UpdateNetworkWirelessRfProfileRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apBandSettings** | [**UpdateNetworkWirelessRfProfileRequestApBandSettings**](UpdateNetworkWirelessRfProfileRequestApBandSettings.md) |  |  [optional] |
|**bandSelectionType** | [**BandSelectionTypeEnum**](#BandSelectionTypeEnum) | Band selection can be set to either &#39;ssid&#39; or &#39;ap&#39;. |  [optional] |
|**clientBalancingEnabled** | **Boolean** | Steers client to best available access point. Can be either true or false. |  [optional] |
|**fiveGhzSettings** | [**UpdateNetworkWirelessRfProfileRequestFiveGhzSettings**](UpdateNetworkWirelessRfProfileRequestFiveGhzSettings.md) |  |  [optional] |
|**minBitrateType** | [**MinBitrateTypeEnum**](#MinBitrateTypeEnum) | Minimum bitrate can be set to either &#39;band&#39; or &#39;ssid&#39;. |  [optional] |
|**name** | **String** | The name of the new profile. Must be unique. |  [optional] |
|**perSsidSettings** | [**CreateNetworkWirelessRfProfileRequestPerSsidSettings**](CreateNetworkWirelessRfProfileRequestPerSsidSettings.md) |  |  [optional] |
|**transmission** | [**CreateNetworkWirelessRfProfileRequestTransmission**](CreateNetworkWirelessRfProfileRequestTransmission.md) |  |  [optional] |
|**twoFourGhzSettings** | [**UpdateNetworkWirelessRfProfileRequestTwoFourGhzSettings**](UpdateNetworkWirelessRfProfileRequestTwoFourGhzSettings.md) |  |  [optional] |



## Enum: BandSelectionTypeEnum

| Name | Value |
|---- | -----|
| AP | &quot;ap&quot; |
| SSID | &quot;ssid&quot; |



## Enum: MinBitrateTypeEnum

| Name | Value |
|---- | -----|
| BAND | &quot;band&quot; |
| SSID | &quot;ssid&quot; |



