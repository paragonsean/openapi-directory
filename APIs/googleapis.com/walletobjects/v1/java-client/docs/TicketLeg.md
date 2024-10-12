

# TicketLeg


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arrivalDateTime** | **String** | The date/time of arrival. This is an ISO 8601 extended format date/time, with or without an offset. Time may be specified up to nanosecond precision. Offsets may be specified with seconds precision (even though offset seconds is not part of ISO 8601). For example: &#x60;1985-04-12T23:20:50.52Z&#x60; would be 20 minutes and 50.52 seconds after the 23rd hour of April 12th, 1985 in UTC. &#x60;1985-04-12T19:20:50.52-04:00&#x60; would be 20 minutes and 50.52 seconds after the 19th hour of April 12th, 1985, 4 hours before UTC (same instant in time as the above example). If the event were in New York, this would be the equivalent of Eastern Daylight Time (EDT). Remember that offset varies in regions that observe Daylight Saving Time (or Summer Time), depending on the time of the year. &#x60;1985-04-12T19:20:50.52&#x60; would be 20 minutes and 50.52 seconds after the 19th hour of April 12th, 1985 with no offset information. The portion of the date/time without the offset is considered the \&quot;local date/time\&quot;. This should be the local date/time at the destination station. For example, if the event occurs at the 20th hour of June 5th, 2018 at the destination station, the local date/time portion should be &#x60;2018-06-05T20:00:00&#x60;. If the local date/time at the destination station is 4 hours before UTC, an offset of &#x60;-04:00&#x60; may be appended. Without offset information, some rich features may not be available. |  [optional] |
|**carriage** | **String** | The train or ship name/number that the passsenger needs to board. |  [optional] |
|**departureDateTime** | **String** | The date/time of departure. This is required if there is no validity time interval set on the transit object. This is an ISO 8601 extended format date/time, with or without an offset. Time may be specified up to nanosecond precision. Offsets may be specified with seconds precision (even though offset seconds is not part of ISO 8601). For example: &#x60;1985-04-12T23:20:50.52Z&#x60; would be 20 minutes and 50.52 seconds after the 23rd hour of April 12th, 1985 in UTC. &#x60;1985-04-12T19:20:50.52-04:00&#x60; would be 20 minutes and 50.52 seconds after the 19th hour of April 12th, 1985, 4 hours before UTC (same instant in time as the above example). If the event were in New York, this would be the equivalent of Eastern Daylight Time (EDT). Remember that offset varies in regions that observe Daylight Saving Time (or Summer Time), depending on the time of the year. &#x60;1985-04-12T19:20:50.52&#x60; would be 20 minutes and 50.52 seconds after the 19th hour of April 12th, 1985 with no offset information. The portion of the date/time without the offset is considered the \&quot;local date/time\&quot;. This should be the local date/time at the origin station. For example, if the departure occurs at the 20th hour of June 5th, 2018 at the origin station, the local date/time portion should be &#x60;2018-06-05T20:00:00&#x60;. If the local date/time at the origin station is 4 hours before UTC, an offset of &#x60;-04:00&#x60; may be appended. Without offset information, some rich features may not be available. |  [optional] |
|**destinationName** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**destinationStationCode** | **String** | The destination station code. |  [optional] |
|**fareName** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**originName** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**originStationCode** | **String** | The origin station code. This is required if &#x60;destinationStationCode&#x60; is present or if &#x60;originName&#x60; is not present. |  [optional] |
|**platform** | **String** | The platform or gate where the passenger can board the carriage. |  [optional] |
|**ticketSeat** | [**TicketSeat**](TicketSeat.md) |  |  [optional] |
|**ticketSeats** | [**List&lt;TicketSeat&gt;**](TicketSeat.md) | The reserved seat for the passenger(s). If only one seat is to be specified then use the &#x60;ticketSeat&#x60; field instead. Both &#x60;ticketSeat&#x60; and &#x60;ticketSeats&#x60; may not be set. |  [optional] |
|**transitOperatorName** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**transitTerminusName** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**zone** | **String** | The zone of boarding within the platform. |  [optional] |



