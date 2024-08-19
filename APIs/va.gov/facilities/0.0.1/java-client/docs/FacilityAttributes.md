

# FacilityAttributes

Details describing a facility.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeStatus** | [**ActiveStatusEnum**](#ActiveStatusEnum) | This field is deprecated and replaced with \&quot;operating_status\&quot;. |  [optional] |
|**address** | [**Addresses**](Addresses.md) |  |  [optional] |
|**classification** | **String** | Subtype of facility which can further be used to describe facility. |  [optional] |
|**detailedServices** | [**List&lt;DetailedService&gt;**](DetailedService.md) |  |  [optional] |
|**facilityType** | [**FacilityTypeEnum**](#FacilityTypeEnum) | One of facility top-level type categories (e.g.) health, benefits, cemetery and vet center. |  |
|**hours** | [**Hours**](Hours.md) |  |  [optional] |
|**lat** | **Float** | Facility latitude. |  |
|**_long** | **Float** | Facility longitude. |  |
|**mobile** | **Boolean** |  |  [optional] |
|**name** | **String** | Name associated with given facility. |  |
|**operatingStatus** | [**OperatingStatus**](OperatingStatus.md) |  |  |
|**operationalHoursSpecialInstructions** | **String** | Additional information about a VA health or Vet Center facility&#39;s operating hours. |  [optional] |
|**phone** | [**Phone**](Phone.md) |  |  [optional] |
|**satisfaction** | [**Satisfaction**](Satisfaction.md) |  |  [optional] |
|**services** | [**Services**](Services.md) |  |  [optional] |
|**timeZone** | **String** | Facility time zone. |  [optional] |
|**visn** | **String** |  |  [optional] |
|**waitTimes** | [**WaitTimes**](WaitTimes.md) |  |  [optional] |
|**website** | **String** | Web address of facility. |  [optional] |



## Enum: ActiveStatusEnum

| Name | Value |
|---- | -----|
| A | &quot;A&quot; |
| T | &quot;T&quot; |



## Enum: FacilityTypeEnum

| Name | Value |
|---- | -----|
| VA_BENEFITS_FACILITY | &quot;va_benefits_facility&quot; |
| VA_CEMETERY | &quot;va_cemetery&quot; |
| VA_HEALTH_FACILITY | &quot;va_health_facility&quot; |
| VET_CENTER | &quot;vet_center&quot; |



