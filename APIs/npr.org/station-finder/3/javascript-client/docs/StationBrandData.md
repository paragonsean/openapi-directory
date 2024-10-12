# NprStationFinderService.StationBrandData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**band** | **String** | The subsection of the radio spectrum -- &#39;AM&#39; or &#39;FM&#39; -- where this station can be heard | [optional] [default to &#39;FM&#39;]
**call** | **String** | The three-to-four-letter identifying code for this station. Please use this with caution; most stations prefer to be identified by their &#x60;name&#x60; in client applications instead of &#x60;call&#x60;. | [optional] 
**frequency** | **String** | Where on the radio dial the station can be heard. If the &#x60;band&#x60; is AM, the frequency will be between 540 and 1600. If the &#x60;band&#x60; is FM, the frequency will be between 87.8 and 108.0. | [optional] 
**marketCity** | **String** | The city that the station is most closely associated with. This may or may not be the city the station is licensed in and it may or may not be the city that the station or the station&#39;s antenna is located in. | 
**marketState** | **String** | The state that the station is most closely associated with. This may or may not be the state the station is licensed in and it may or may not be the state that the station or the station&#39;s antenna is located in. | 
**name** | **String** | The display name for the station. In most cases, this will be the same as &#x60;call&#x60; letters combined with band. When returning networks, it will return the network name (e.g. Minnesota Public Radio). | 
**tagline** | **String** | A short text-logo for the station | [default to &#39;&#39;]



## Enum: BandEnum


* `FM` (value: `"FM"`)

* `AM` (value: `"AM"`)




