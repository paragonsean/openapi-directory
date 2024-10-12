

# V3StoppingPattern


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**departures** | [**List&lt;V3PatternDeparture&gt;**](V3PatternDeparture.md) | Timetabled and real-time service departures |  [optional] |
|**directions** | [**Map&lt;String, V3Direction&gt;**](V3Direction.md) | Directions of travel of route |  [optional] |
|**disruptions** | [**List&lt;V3Disruption&gt;**](V3Disruption.md) | Disruption information applicable to relevant routes or stops |  [optional] |
|**routes** | **Map&lt;String, Object&gt;** | Train lines, tram routes, bus routes, regional coach routes, Night Bus routes |  [optional] |
|**runs** | [**Map&lt;String, V3Run&gt;**](V3Run.md) | Individual trips/services of a route |  [optional] |
|**status** | [**V3Status**](V3Status.md) |  |  [optional] |
|**stops** | [**Map&lt;String, V3StoppingPatternStop&gt;**](V3StoppingPatternStop.md) | A train station, tram stop, bus stop, regional coach stop or Night Bus stop |  [optional] |



