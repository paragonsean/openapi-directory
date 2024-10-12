# SasPortalApi.SasPortalDevice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeConfig** | [**SasPortalDeviceConfig**](SasPortalDeviceConfig.md) |  | [optional] 
**currentChannels** | [**[SasPortalChannelWithScore]**](SasPortalChannelWithScore.md) | Output only. Current channels with scores. | [optional] [readonly] 
**deviceMetadata** | [**SasPortalDeviceMetadata**](SasPortalDeviceMetadata.md) |  | [optional] 
**displayName** | **String** | Device display name. | [optional] 
**fccId** | **String** | The FCC identifier of the device. Refer to https://www.fcc.gov/oet/ea/fccid for FccID format. Accept underscores and periods because some test-SAS customers use them. | [optional] 
**grantRangeAllowlists** | [**[SasPortalFrequencyRange]**](SasPortalFrequencyRange.md) | Only ranges that are within the allowlists are available for new grants. | [optional] 
**grants** | [**[SasPortalDeviceGrant]**](SasPortalDeviceGrant.md) | Output only. Grants held by the device. | [optional] 
**name** | **String** | Output only. The resource path name. | [optional] 
**preloadedConfig** | [**SasPortalDeviceConfig**](SasPortalDeviceConfig.md) |  | [optional] 
**serialNumber** | **String** | A serial number assigned to the device by the device manufacturer. | [optional] 
**state** | **String** | Output only. Device state. | [optional] 



## Enum: StateEnum


* `DEVICE_STATE_UNSPECIFIED` (value: `"DEVICE_STATE_UNSPECIFIED"`)

* `RESERVED` (value: `"RESERVED"`)

* `REGISTERED` (value: `"REGISTERED"`)

* `DEREGISTERED` (value: `"DEREGISTERED"`)




