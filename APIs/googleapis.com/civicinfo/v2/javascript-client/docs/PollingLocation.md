# GoogleCivicInformationApi.PollingLocation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**SimpleAddressType**](SimpleAddressType.md) |  | [optional] 
**endDate** | **String** | The last date that this early vote site or drop off location may be used. This field is not populated for polling locations. | [optional] 
**latitude** | **Number** | Latitude of the location, in degrees north of the equator. Note this field may not be available for some locations. | [optional] 
**longitude** | **Number** | Longitude of the location, in degrees east of the Prime Meridian. Note this field may not be available for some locations. | [optional] 
**name** | **String** | The name of the early vote site or drop off location. This field is not populated for polling locations. | [optional] 
**notes** | **String** | Notes about this location (e.g. accessibility ramp or entrance to use). | [optional] 
**pollingHours** | **String** | A description of when this location is open. | [optional] 
**sources** | [**[Source]**](Source.md) | A list of sources for this location. If multiple sources are listed the data has been aggregated from those sources. | [optional] 
**startDate** | **String** | The first date that this early vote site or drop off location may be used. This field is not populated for polling locations. | [optional] 
**voterServices** | **String** | The services provided by this early vote site or drop off location. This field is not populated for polling locations. | [optional] 


