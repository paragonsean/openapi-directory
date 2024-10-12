# FlightAvailibilitiesSearch.FlightAvailability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **String** | duration in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) PnYnMnDTnHnMnS format, e.g. PT2H10M for a duration of 2h10m | [optional] 
**id** | **String** | Id of the flight availability | 
**instantTicketingRequired** | **Boolean** | If true, inform that a ticketing will be required at booking step. | [optional] 
**originDestinationId** | **String** | Id of the originDestination in query | [optional] 
**paymentCardRequired** | **Boolean** | If true, a payment card is mandatory to book this flight offer | [optional] 
**segments** | [**[ExtendedSegment]**](ExtendedSegment.md) |  | 
**source** | [**FlightOfferSource**](FlightOfferSource.md) |  | 
**type** | **String** | the resource name | 


