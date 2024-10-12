# PlacesApiNew.GoogleMapsPlacesV1PlaceOpeningHours

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openNow** | **Boolean** | Is this place open right now? Always present unless we lack time-of-day or timezone data for these opening hours. | [optional] 
**periods** | [**[GoogleMapsPlacesV1PlaceOpeningHoursPeriod]**](GoogleMapsPlacesV1PlaceOpeningHoursPeriod.md) | The periods that this place is open during the week. The periods are in chronological order, starting with Sunday in the place-local timezone. An empty (but not absent) value indicates a place that is never open, e.g. because it is closed temporarily for renovations. | [optional] 
**secondaryHoursType** | **String** | A type string used to identify the type of secondary hours. | [optional] 
**specialDays** | [**[GoogleMapsPlacesV1PlaceOpeningHoursSpecialDay]**](GoogleMapsPlacesV1PlaceOpeningHoursSpecialDay.md) | Structured information for special days that fall within the period that the returned opening hours cover. Special days are days that could impact the business hours of a place, e.g. Christmas day. Set for current_opening_hours and current_secondary_opening_hours if there are exceptional hours. | [optional] 
**weekdayDescriptions** | **[String]** | Localized strings describing the opening hours of this place, one string for each day of the week. Will be empty if the hours are unknown or could not be converted to localized text. Example: \&quot;Sun: 18:00–06:00\&quot; | [optional] 



## Enum: SecondaryHoursTypeEnum


* `SECONDARY_HOURS_TYPE_UNSPECIFIED` (value: `"SECONDARY_HOURS_TYPE_UNSPECIFIED"`)

* `DRIVE_THROUGH` (value: `"DRIVE_THROUGH"`)

* `HAPPY_HOUR` (value: `"HAPPY_HOUR"`)

* `DELIVERY` (value: `"DELIVERY"`)

* `TAKEOUT` (value: `"TAKEOUT"`)

* `KITCHEN` (value: `"KITCHEN"`)

* `BREAKFAST` (value: `"BREAKFAST"`)

* `LUNCH` (value: `"LUNCH"`)

* `DINNER` (value: `"DINNER"`)

* `BRUNCH` (value: `"BRUNCH"`)

* `PICKUP` (value: `"PICKUP"`)

* `ACCESS` (value: `"ACCESS"`)

* `SENIOR_HOURS` (value: `"SENIOR_HOURS"`)

* `ONLINE_SERVICE_HOURS` (value: `"ONLINE_SERVICE_HOURS"`)




