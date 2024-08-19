

# TflApiPresentationEntitiesPrediction

DTO to capture the prediction details

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bearing** | **String** | Bearing (between 0 to 359) |  [optional] |
|**currentLocation** | **String** | The current location of the vehicle. |  [optional] |
|**destinationName** | **String** | Name of the destination |  [optional] |
|**destinationNaptanId** | **String** | Naptan Identifier for the prediction&#39;s destination |  [optional] |
|**direction** | **String** | Direction (unified to inbound/outbound) |  [optional] |
|**expectedArrival** | **OffsetDateTime** | The expected arrival time of the vehicle at the stop/station |  [optional] |
|**id** | **String** | The identitier for the prediction |  [optional] |
|**lineId** | **String** | Unique identifier for the Line |  [optional] |
|**lineName** | **String** | Line Name |  [optional] |
|**modeName** | **String** | The mode name of the station/line the prediction relates to |  [optional] |
|**naptanId** | **String** | Identifier for the prediction |  [optional] |
|**operationType** | **Integer** | The type of the operation (1: is new or has been updated, 2: should be deleted from any client cache) |  [optional] |
|**platformName** | **String** | Platform name (for bus, this is the stop letter) |  [optional] |
|**stationName** | **String** | Station name |  [optional] |
|**timeToLive** | **OffsetDateTime** | The expiry time for the prediction |  [optional] |
|**timeToStation** | **Integer** | Prediction of the Time to station in seconds |  [optional] |
|**timestamp** | **OffsetDateTime** | Timestamp for when the prediction was inserted/modified (source column drives what objects are broadcast on each iteration) |  [optional] |
|**timing** | [**TflApiPresentationEntitiesPredictionTiming**](TflApiPresentationEntitiesPredictionTiming.md) |  |  [optional] |
|**towards** | **String** | Routing information or other descriptive text about the path of the vehicle towards the destination |  [optional] |
|**vehicleId** | **String** | The actual vehicle in transit (for train modes, the leading car of the rolling set) |  [optional] |



