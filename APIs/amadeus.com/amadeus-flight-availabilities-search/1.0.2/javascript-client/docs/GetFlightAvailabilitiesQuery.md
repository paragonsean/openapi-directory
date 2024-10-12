# FlightAvailibilitiesSearch.GetFlightAvailabilitiesQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**originDestinations** | [**[ExtendedOriginDestinationLight]**](ExtendedOriginDestinationLight.md) | Origins and Destinations must be properly ordered in time (chronological order in accordance with the timezone of each location) to describe the journey consistently. Dates and times must not be past nor more than 365 days in the future, according to provider settings.Number of Origins and Destinations must not exceed the limit defined in provider settings. | 
**searchCriteria** | [**ExtendedSearchCriteria**](ExtendedSearchCriteria.md) |  | [optional] 
**sources** | [**[FlightOfferSource]**](FlightOfferSource.md) | Allows enable one or more sources. If present in the list, these sources will be called by the system.  GDS : Full service carriers | 
**travelers** | [**[TravelerInfo]**](TravelerInfo.md) | List of travelers composing the travel | 


