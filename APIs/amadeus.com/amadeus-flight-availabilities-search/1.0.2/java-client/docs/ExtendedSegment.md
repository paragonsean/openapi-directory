

# ExtendedSegment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blacklistedInEU** | **Boolean** | When the flight has a marketing or/and operating airline that is identified as blacklisted by the European Commission.   To improve travel safety, the European Commission regularly updates the list of the banned carriers from operating in Europe. It allows any Travel Agency located in the European Union to easily identify and hide any travel recommendation based on some unsafe airlines.  The [list of the banned airlines](https://ec.europa.eu/transport/sites/transport/files/air-safety-list_en.pdf) is published in the Official Journal of the European Union, where they are included as annexes A and B to the Commission Regulation. The blacklist of an airline can concern all its flights or some specific aircraft types pertaining to the airline     |  [optional] |
|**co2Emissions** | [**List&lt;Co2Emission&gt;**](Co2Emission.md) | Co2 informations |  [optional] |
|**id** | **String** | Id of the segment |  [optional] |
|**numberOfStops** | **Integer** | Number of stops |  [optional] |
|**aircraft** | [**AircraftEquipment**](AircraftEquipment.md) |  |  [optional] |
|**arrival** | [**FlightEndPoint**](FlightEndPoint.md) |  |  [optional] |
|**carrierCode** | **String** | providing the airline / carrier code |  [optional] |
|**departure** | [**FlightEndPoint**](FlightEndPoint.md) |  |  [optional] |
|**duration** | **String** | stop duration in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) PnYnMnDTnHnMnS format, e.g. PT2H10M |  [optional] |
|**number** | **String** | the flight number as assigned by the carrier |  [optional] |
|**operating** | [**OperatingFlight**](OperatingFlight.md) |  |  [optional] |
|**stops** | [**List&lt;FlightStop&gt;**](FlightStop.md) | information regarding the different stops composing the flight segment. E.g. technical stop, change of gauge... |  [optional] |
|**availabilityClasses** | [**List&lt;AvailabilityClass&gt;**](AvailabilityClass.md) | List of booking classes for the segment |  [optional] |
|**closedStatus** | [**ClosedStatusEnum**](#ClosedStatusEnum) | Status of the segment when it is closed. |  [optional] |



## Enum: ClosedStatusEnum

| Name | Value |
|---- | -----|
| CANCELLED | &quot;CANCELLED&quot; |
| DEPARTED | &quot;DEPARTED&quot; |
| NOT_AVAILABLE | &quot;NOT_AVAILABLE&quot; |



