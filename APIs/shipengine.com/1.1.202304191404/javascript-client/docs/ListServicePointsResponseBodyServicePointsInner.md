# ShipEngineApi.ListServicePointsResponseBodyServicePointsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressLine1** | **String** |  | [optional] 
**carrierCode** | **String** |  | [optional] 
**cityLocality** | **String** |  | [optional] 
**companyName** | **String** |  | [optional] 
**countryCode** | **String** |  | [optional] 
**distanceInMeters** | **Number** |  | [optional] 
**features** | **[String]** |  | [optional] 
**hoursOfOperation** | [**GetServicePointByIdResponseBodyServicePointHoursOfOperation**](GetServicePointByIdResponseBodyServicePointHoursOfOperation.md) |  | [optional] 
**lat** | **Number** |  | [optional] 
**_long** | **Number** |  | [optional] 
**phoneNumber** | **String** |  | [optional] 
**postalCode** | **String** |  | [optional] 
**serviceCodes** | **[String]** |  | [optional] 
**servicePointId** | **String** |  | [optional] 
**stateProvince** | **String** |  | [optional] 
**type** | **String** |  | [optional] [default to &#39;pudo&#39;]



## Enum: [FeaturesEnum]


* `drop_off_point` (value: `"drop_off_point"`)

* `pickup_point` (value: `"pickup_point"`)

* `print_services` (value: `"print_services"`)

* `after_hours_locker` (value: `"after_hours_locker"`)

* `after_hours_dropbox` (value: `"after_hours_dropbox"`)





## Enum: TypeEnum


* `pudo` (value: `"pudo"`)

* `locker` (value: `"locker"`)




