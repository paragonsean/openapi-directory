

# SasPortalDeviceGrant

Device grant. It is an authorization provided by the Spectrum Access System to a device to transmit using specified operating parameters after a successful heartbeat by the device.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelType** | [**ChannelTypeEnum**](#ChannelTypeEnum) | Type of channel used. |  [optional] |
|**expireTime** | **String** | The expiration time of the grant. |  [optional] |
|**frequencyRange** | [**SasPortalFrequencyRange**](SasPortalFrequencyRange.md) |  |  [optional] |
|**grantId** | **String** | Grant Id. |  [optional] |
|**lastHeartbeatTransmitExpireTime** | **String** | The transmit expiration time of the last heartbeat. |  [optional] |
|**maxEirp** | **Double** | Maximum Equivalent Isotropically Radiated Power (EIRP) permitted by the grant. The maximum EIRP is in units of dBm/MHz. The value of &#x60;maxEirp&#x60; represents the average (RMS) EIRP that would be measured by the procedure defined in FCC part 96.41(e)(3). |  [optional] |
|**moveList** | [**List&lt;SasPortalDpaMoveList&gt;**](SasPortalDpaMoveList.md) | The DPA move lists on which this grant appears. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of the grant. |  [optional] |
|**suspensionReason** | **List&lt;String&gt;** | If the grant is suspended, the reason(s) for suspension. |  [optional] |



## Enum: ChannelTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;CHANNEL_TYPE_UNSPECIFIED&quot; |
| GAA | &quot;CHANNEL_TYPE_GAA&quot; |
| PAL | &quot;CHANNEL_TYPE_PAL&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;GRANT_STATE_UNSPECIFIED&quot; |
| GRANTED | &quot;GRANT_STATE_GRANTED&quot; |
| TERMINATED | &quot;GRANT_STATE_TERMINATED&quot; |
| SUSPENDED | &quot;GRANT_STATE_SUSPENDED&quot; |
| AUTHORIZED | &quot;GRANT_STATE_AUTHORIZED&quot; |
| EXPIRED | &quot;GRANT_STATE_EXPIRED&quot; |



