# SasPortalApiTesting.SasPortalDeviceGrant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channelType** | **String** | Type of channel used. | [optional] 
**expireTime** | **String** | The expiration time of the grant. | [optional] 
**frequencyRange** | [**SasPortalFrequencyRange**](SasPortalFrequencyRange.md) |  | [optional] 
**grantId** | **String** | Grant Id. | [optional] 
**lastHeartbeatTransmitExpireTime** | **String** | The transmit expiration time of the last heartbeat. | [optional] 
**maxEirp** | **Number** | Maximum Equivalent Isotropically Radiated Power (EIRP) permitted by the grant. The maximum EIRP is in units of dBm/MHz. The value of &#x60;maxEirp&#x60; represents the average (RMS) EIRP that would be measured by the procedure defined in FCC part 96.41(e)(3). | [optional] 
**moveList** | [**[SasPortalDpaMoveList]**](SasPortalDpaMoveList.md) | The DPA move lists on which this grant appears. | [optional] 
**state** | **String** | State of the grant. | [optional] 
**suspensionReason** | **[String]** | If the grant is suspended, the reason(s) for suspension. | [optional] 



## Enum: ChannelTypeEnum


* `UNSPECIFIED` (value: `"CHANNEL_TYPE_UNSPECIFIED"`)

* `GAA` (value: `"CHANNEL_TYPE_GAA"`)

* `PAL` (value: `"CHANNEL_TYPE_PAL"`)





## Enum: StateEnum


* `UNSPECIFIED` (value: `"GRANT_STATE_UNSPECIFIED"`)

* `GRANTED` (value: `"GRANT_STATE_GRANTED"`)

* `TERMINATED` (value: `"GRANT_STATE_TERMINATED"`)

* `SUSPENDED` (value: `"GRANT_STATE_SUSPENDED"`)

* `AUTHORIZED` (value: `"GRANT_STATE_AUTHORIZED"`)

* `EXPIRED` (value: `"GRANT_STATE_EXPIRED"`)




