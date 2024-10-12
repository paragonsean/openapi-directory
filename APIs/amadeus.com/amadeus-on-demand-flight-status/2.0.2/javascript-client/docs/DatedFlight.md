# OnDemandFlightStatus.DatedFlight

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flightDesignator** | [**FlightDesignator**](FlightDesignator.md) |  | [optional] 
**flightPoints** | [**[FlightPoint]**](FlightPoint.md) | the flight points of the flight. At least one departure, one arrival  | [optional] 
**legs** | [**[Leg]**](Leg.md) | the list of legs of the datedFlight. - definition of leg: operation of the aircraft between a departure station and the next arrival station (between take off and landing)  | [optional] 
**scheduledDepartureDate** | **Date** | the scheduled departure date | [optional] 
**segments** | [**[Segment]**](Segment.md) | the list of segments of the datedFlight - definition of segment: the commercial unit corresponding to the passenger journey traveling between two points with the same flight (same flight designator)  | [optional] 
**type** | **String** | the resource name | [optional] [readonly] 


