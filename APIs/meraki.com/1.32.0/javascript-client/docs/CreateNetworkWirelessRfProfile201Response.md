# MerakiDashboardApi.CreateNetworkWirelessRfProfile201Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apBandSettings** | [**CreateNetworkWirelessRfProfile201ResponseApBandSettings**](CreateNetworkWirelessRfProfile201ResponseApBandSettings.md) |  | [optional] 
**bandSelectionType** | **String** | Band selection can be set to either &#39;ssid&#39; or &#39;ap&#39;. This param is required on creation. | [optional] 
**clientBalancingEnabled** | **Boolean** | Steers client to best available access point. Can be either true or false. Defaults to true. | [optional] 
**fiveGhzSettings** | [**CreateNetworkWirelessRfProfileRequestFiveGhzSettings**](CreateNetworkWirelessRfProfileRequestFiveGhzSettings.md) |  | [optional] 
**id** | **String** | The name of the new profile. Must be unique. | [optional] 
**minBitrateType** | **String** | Minimum bitrate can be set to either &#39;band&#39; or &#39;ssid&#39;. Defaults to band. | [optional] 
**name** | **String** | The name of the new profile. Must be unique. This param is required on creation. | [optional] 
**networkId** | **String** | The network ID of the RF Profile | [optional] 
**perSsidSettings** | [**CreateNetworkWirelessRfProfile201ResponsePerSsidSettings**](CreateNetworkWirelessRfProfile201ResponsePerSsidSettings.md) |  | [optional] 
**transmission** | [**CreateNetworkWirelessRfProfileRequestTransmission**](CreateNetworkWirelessRfProfileRequestTransmission.md) |  | [optional] 
**twoFourGhzSettings** | [**CreateNetworkWirelessRfProfileRequestTwoFourGhzSettings**](CreateNetworkWirelessRfProfileRequestTwoFourGhzSettings.md) |  | [optional] 


