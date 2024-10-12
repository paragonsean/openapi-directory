

# GoogleMapsPlacesV1PlaceOpeningHours

Information about business hour of the place.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**openNow** | **Boolean** | Is this place open right now? Always present unless we lack time-of-day or timezone data for these opening hours. |  [optional] |
|**periods** | [**List&lt;GoogleMapsPlacesV1PlaceOpeningHoursPeriod&gt;**](GoogleMapsPlacesV1PlaceOpeningHoursPeriod.md) | The periods that this place is open during the week. The periods are in chronological order, starting with Sunday in the place-local timezone. An empty (but not absent) value indicates a place that is never open, e.g. because it is closed temporarily for renovations. |  [optional] |
|**secondaryHoursType** | [**SecondaryHoursTypeEnum**](#SecondaryHoursTypeEnum) | A type string used to identify the type of secondary hours. |  [optional] |
|**specialDays** | [**List&lt;GoogleMapsPlacesV1PlaceOpeningHoursSpecialDay&gt;**](GoogleMapsPlacesV1PlaceOpeningHoursSpecialDay.md) | Structured information for special days that fall within the period that the returned opening hours cover. Special days are days that could impact the business hours of a place, e.g. Christmas day. Set for current_opening_hours and current_secondary_opening_hours if there are exceptional hours. |  [optional] |
|**weekdayDescriptions** | **List&lt;String&gt;** | Localized strings describing the opening hours of this place, one string for each day of the week. Will be empty if the hours are unknown or could not be converted to localized text. Example: \&quot;Sun: 18:00–06:00\&quot; |  [optional] |



## Enum: SecondaryHoursTypeEnum

| Name | Value |
|---- | -----|
| SECONDARY_HOURS_TYPE_UNSPECIFIED | &quot;SECONDARY_HOURS_TYPE_UNSPECIFIED&quot; |
| DRIVE_THROUGH | &quot;DRIVE_THROUGH&quot; |
| HAPPY_HOUR | &quot;HAPPY_HOUR&quot; |
| DELIVERY | &quot;DELIVERY&quot; |
| TAKEOUT | &quot;TAKEOUT&quot; |
| KITCHEN | &quot;KITCHEN&quot; |
| BREAKFAST | &quot;BREAKFAST&quot; |
| LUNCH | &quot;LUNCH&quot; |
| DINNER | &quot;DINNER&quot; |
| BRUNCH | &quot;BRUNCH&quot; |
| PICKUP | &quot;PICKUP&quot; |
| ACCESS | &quot;ACCESS&quot; |
| SENIOR_HOURS | &quot;SENIOR_HOURS&quot; |
| ONLINE_SERVICE_HOURS | &quot;ONLINE_SERVICE_HOURS&quot; |



