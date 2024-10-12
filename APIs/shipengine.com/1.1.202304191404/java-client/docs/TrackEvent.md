

# TrackEvent

A track event

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**carrierDetailCode** | **String** | Carrier detail code |  [readonly] |
|**carrierOccurredAt** | **OffsetDateTime** | Carrier timestamp for the event, it is assumed to be the local time of where the event occurred. |  [optional] |
|**carrierStatusCode** | **String** | Carrier status code |  [readonly] |
|**carrierStatusDescription** | **String** | carrier status description |  [readonly] |
|**cityLocality** | **String** | City locality |  [readonly] |
|**companyName** | **String** | Company Name |  [optional] [readonly] |
|**countryCode** | **String** | A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)  |  [optional] |
|**description** | **String** | Event description |  [optional] [readonly] |
|**eventCode** | **String** | Event Code |  [optional] |
|**latitude** | **Double** | Latitude coordinate of tracking event. |  [optional] |
|**longitude** | **Double** | Longitude coordinate of tracking event. |  [optional] |
|**occurredAt** | **OffsetDateTime** | Timestamp for carrier event |  |
|**postalCode** | **String** | Postal code |  [readonly] |
|**signer** | **String** | Signer information |  [optional] [readonly] |
|**stateProvince** | **String** | State province |  [readonly] |
|**statusCode** | **StatusCode** |  |  |
|**statusDescription** | **String** | Event Status Description |  [readonly] |



