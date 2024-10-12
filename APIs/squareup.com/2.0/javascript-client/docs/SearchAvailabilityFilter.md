# SquareConnectApi.SearchAvailabilityFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookingId** | **String** | The query expression to search for availabilities for an existing booking by matching the specified &#x60;booking_id&#x60; value. This is commonly used to reschedule an appointment. If this expression is specified, the &#x60;location_id&#x60; and &#x60;segment_filters&#x60; expressions are not allowed. | [optional] 
**locationId** | **String** | The query expression to search for availabilities matching the specified seller location IDs. This query expression is not applicable when &#x60;booking_id&#x60; is present. | [optional] 
**segmentFilters** | [**[SegmentFilter]**](SegmentFilter.md) | The list of segment filters to apply. A query with &#x60;n&#x60; segment filters returns availabilities with &#x60;n&#x60; segments per availability. It is not applicable when &#x60;booking_id&#x60; is present. | [optional] 
**startAtRange** | [**TimeRange**](TimeRange.md) |  | 


