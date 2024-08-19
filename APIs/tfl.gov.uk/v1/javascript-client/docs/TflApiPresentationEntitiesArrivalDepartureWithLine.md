# TransportForLondonUnifiedApi.TflApiPresentationEntitiesArrivalDepartureWithLine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cause** | **String** | Reason for cancellation or delay | [optional] 
**departureStatus** | **String** | Status of departure | [optional] 
**destinationName** | **String** | Name of the destination | [optional] 
**destinationNaptanId** | **String** | Naptan Identifier for the prediction&#39;s destination | [optional] 
**estimatedTimeOfArrival** | **Date** | Estimated time of arrival | [optional] 
**estimatedTimeOfDeparture** | **Date** | Estimated time of arrival | [optional] 
**lineId** | **String** | Train operating company name | [optional] 
**lineName** | **String** | Train operating company code | [optional] 
**minutesAndSecondsToArrival** | **String** | Estimated time of arrival | [optional] 
**minutesAndSecondsToDeparture** | **String** | Estimated time of arrival | [optional] 
**naptanId** | **String** | Identifier for the prediction | [optional] 
**platformName** | **String** | Platform name (for bus, this is the stop letter) | [optional] 
**scheduledTimeOfArrival** | **Date** | Estimated time of arrival | [optional] 
**scheduledTimeOfDeparture** | **Date** | Estimated time of arrival | [optional] 
**stationName** | **String** | Station name | [optional] 
**timing** | [**TflApiPresentationEntitiesPredictionTiming**](TflApiPresentationEntitiesPredictionTiming.md) |  | [optional] 



## Enum: DepartureStatusEnum


* `OnTime` (value: `"OnTime"`)

* `Delayed` (value: `"Delayed"`)

* `Cancelled` (value: `"Cancelled"`)

* `NotStoppingAtStation` (value: `"NotStoppingAtStation"`)




