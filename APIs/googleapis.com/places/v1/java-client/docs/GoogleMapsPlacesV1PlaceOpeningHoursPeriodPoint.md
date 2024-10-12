

# GoogleMapsPlacesV1PlaceOpeningHoursPeriodPoint

Status changing points.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**date** | [**GoogleTypeDate**](GoogleTypeDate.md) |  |  [optional] |
|**day** | **Integer** | A day of the week, as an integer in the range 0-6. 0 is Sunday, 1 is Monday, etc. |  [optional] |
|**hour** | **Integer** | The hour in 2 digits. Ranges from 00 to 23. |  [optional] |
|**minute** | **Integer** | The minute in 2 digits. Ranges from 00 to 59. |  [optional] |
|**truncated** | **Boolean** | Whether or not this endpoint was truncated. Truncation occurs when the real hours are outside the times we are willing to return hours between, so we truncate the hours back to these boundaries. This ensures that at most 24 * 7 hours from midnight of the day of the request are returned. |  [optional] |



