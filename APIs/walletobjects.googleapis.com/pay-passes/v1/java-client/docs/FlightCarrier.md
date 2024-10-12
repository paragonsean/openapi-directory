

# FlightCarrier


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**airlineAllianceLogo** | [**Image**](Image.md) |  |  [optional] |
|**airlineLogo** | [**Image**](Image.md) |  |  [optional] |
|**airlineName** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**carrierIataCode** | **String** | Two character IATA airline code of the marketing carrier (as opposed to operating carrier). Exactly one of this or &#x60;carrierIcaoCode&#x60; needs to be provided for &#x60;carrier&#x60; and &#x60;operatingCarrier&#x60;. eg: \&quot;LX\&quot; for Swiss Air |  [optional] |
|**carrierIcaoCode** | **String** | Three character ICAO airline code of the marketing carrier (as opposed to operating carrier). Exactly one of this or &#x60;carrierIataCode&#x60; needs to be provided for &#x60;carrier&#x60; and &#x60;operatingCarrier&#x60;. eg: \&quot;EZY\&quot; for Easy Jet |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;walletobjects#flightCarrier\&quot;&#x60;. |  [optional] |



