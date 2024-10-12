# VaFacilities.FacilityAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeStatus** | **String** | This field is deprecated and replaced with \&quot;operating_status\&quot;. | [optional] 
**address** | [**Addresses**](Addresses.md) |  | [optional] 
**classification** | **String** | Subtype of facility which can further be used to describe facility. | [optional] 
**detailedServices** | [**[DetailedService]**](DetailedService.md) |  | [optional] 
**facilityType** | **String** | One of facility top-level type categories (e.g.) health, benefits, cemetery and vet center. | 
**hours** | [**Hours**](Hours.md) |  | [optional] 
**lat** | **Number** | Facility latitude. | 
**_long** | **Number** | Facility longitude. | 
**mobile** | **Boolean** |  | [optional] 
**name** | **String** | Name associated with given facility. | 
**operatingStatus** | [**OperatingStatus**](OperatingStatus.md) |  | 
**operationalHoursSpecialInstructions** | **String** | Additional information about a VA health or Vet Center facility&#39;s operating hours. | [optional] 
**phone** | [**Phone**](Phone.md) |  | [optional] 
**satisfaction** | [**Satisfaction**](Satisfaction.md) |  | [optional] 
**services** | [**Services**](Services.md) |  | [optional] 
**timeZone** | **String** | Facility time zone. | [optional] 
**visn** | **String** |  | [optional] 
**waitTimes** | [**WaitTimes**](WaitTimes.md) |  | [optional] 
**website** | **String** | Web address of facility. | [optional] 



## Enum: ActiveStatusEnum


* `A` (value: `"A"`)

* `T` (value: `"T"`)





## Enum: FacilityTypeEnum


* `va_benefits_facility` (value: `"va_benefits_facility"`)

* `va_cemetery` (value: `"va_cemetery"`)

* `va_health_facility` (value: `"va_health_facility"`)

* `vet_center` (value: `"vet_center"`)




