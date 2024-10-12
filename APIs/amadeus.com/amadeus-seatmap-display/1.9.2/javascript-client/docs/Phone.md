# SeatmapDisplay.Phone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresseeName** | **String** | Adressee name (e.g. in case of emergency purpose it corresponds to name of the person to be contacted). | [optional] 
**areaCode** | **String** | Corresponds to a regional code or a city code. The length of the field varies depending on the area. | [optional] 
**category** | **String** | Category of the contact element | [optional] 
**countryCallingCode** | **String** | Country calling code of the phone number, as defined by the International Communication Union. Examples - \&quot;1\&quot; for US, \&quot;371\&quot; for Latvia. | [optional] 
**countryCode** | **String** | Country code of the country (ISO3166-1). E.g. \&quot;US\&quot; for the United States | [optional] 
**deviceType** | [**PhoneDeviceType**](PhoneDeviceType.md) |  | [optional] 
**extension** | **String** | Extension of the phone | [optional] 
**number** | **String** | Phone number. Composed of digits only. The number of digits depends on the country. | [optional] 
**text** | **String** | String containing the full phone number - applicable only when a structured phone (i.e. countryCallingCode + number) is not provided | [optional] 



## Enum: CategoryEnum


* `BUSINESS` (value: `"BUSINESS"`)

* `PERSONAL` (value: `"PERSONAL"`)

* `OTHER` (value: `"OTHER"`)




