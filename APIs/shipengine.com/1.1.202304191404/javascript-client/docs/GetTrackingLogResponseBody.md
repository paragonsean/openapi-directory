# ShipEngineApi.GetTrackingLogResponseBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actualDeliveryDate** | **Date** | An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string that represents a date and time.  | [optional] 
**carrierCode** | **String** | A [shipping carrier](https://www.shipengine.com/docs/carriers/setup/), such as &#x60;fedex&#x60;, &#x60;dhl_express&#x60;, &#x60;stamps_com&#x60;, etc.  | 
**carrierDetailCode** | **String** | Carrier detail code | [readonly] 
**carrierId** | **String** | A string that uniquely identifies a ShipEngine resource, such as a carrier, label, shipment, etc. | 
**carrierStatusCode** | **String** | Carrier status code | [readonly] 
**carrierStatusDescription** | **String** | carrier status description | [optional] [readonly] 
**estimatedDeliveryDate** | **Date** | An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string that represents a date and time.  | 
**events** | [**[TrackEvent]**](TrackEvent.md) | The events that have occured during the lifetime of this tracking number. | [readonly] 
**exceptionDescription** | **String** | Exception description | [optional] [readonly] 
**shipDate** | **Date** | An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string that represents a date and time.  | [optional] 
**statusCode** | [**StatusCode**](StatusCode.md) |  | 
**statusDescription** | **String** | Status description | [optional] [readonly] 
**trackingNumber** | **String** | A tracking number for a package. The format depends on the carrier. | 
**trackingUrl** | **String** | Carrier Tracking Url, if available | [readonly] 


