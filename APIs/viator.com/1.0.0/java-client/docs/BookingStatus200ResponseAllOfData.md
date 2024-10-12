

# BookingStatus200ResponseAllOfData

**object** containing booking status and details

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bookingDate** | **String** | **date**: of *this* booking |  [optional] |
|**bookingStatus** | [**BookingStatusItinerary**](BookingStatusItinerary.md) |  |  [optional] |
|**distributorRef** | **String** | **alphanumeric identifer** of the distributor for *this* booking |  [optional] |
|**itemSummaries** | [**List&lt;BookingStatus200ResponseAllOfDataItemSummariesInner&gt;**](BookingStatus200ResponseAllOfDataItemSummariesInner.md) | **array** of item summary objects |  [optional] |
|**itineraryId** | **Integer** | ignore (Viator only) |  [optional] |
|**sortOrder** | **Integer** | **sort order** for *this* response |  [optional] |



