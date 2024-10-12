

# CreateNetworkWirelessRfProfileRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apBandSettings** | [**CreateNetworkWirelessRfProfileRequestApBandSettings**](CreateNetworkWirelessRfProfileRequestApBandSettings.md) |  |  [optional] |
|**bandSelectionType** | [**BandSelectionTypeEnum**](#BandSelectionTypeEnum) | Band selection can be set to either &#39;ssid&#39; or &#39;ap&#39;. This param is required on creation. |  |
|**clientBalancingEnabled** | **Boolean** | Steers client to best available access point. Can be either true or false. Defaults to true. |  [optional] |
|**fiveGhzSettings** | [**CreateNetworkWirelessRfProfileRequestFiveGhzSettings**](CreateNetworkWirelessRfProfileRequestFiveGhzSettings.md) |  |  [optional] |
|**minBitrateType** | [**MinBitrateTypeEnum**](#MinBitrateTypeEnum) | Minimum bitrate can be set to either &#39;band&#39; or &#39;ssid&#39;. Defaults to band. |  [optional] |
|**name** | **String** | The name of the new profile. Must be unique. This param is required on creation. |  |
|**twoFourGhzSettings** | [**CreateNetworkWirelessRfProfileRequestTwoFourGhzSettings**](CreateNetworkWirelessRfProfileRequestTwoFourGhzSettings.md) |  |  [optional] |



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



