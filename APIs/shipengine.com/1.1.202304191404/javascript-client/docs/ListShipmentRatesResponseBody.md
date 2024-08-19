# ShipEngineApi.ListShipmentRatesResponseBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **String** | When the rate was created | 
**errors** | [**[Error]**](Error.md) |  | 
**invalidRates** | [**[Rate]**](Rate.md) | An array of invalid shipment rates | [readonly] 
**rateRequestId** | **String** | A string that uniquely identifies the rate request | [readonly] 
**rates** | [**[Rate]**](Rate.md) | An array of shipment rates | [readonly] 
**shipmentId** | **String** | A string that uniquely identifies the shipment | [readonly] 
**status** | [**RateResponseStatus**](RateResponseStatus.md) |  | [readonly] 


