

# Airport

Array of all available airports or one airport matching the request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**airportCode** | **String** | 3-letter IATA airport code, e.g. “TXL”. |  [optional] |
|**cityCode** | **String** | 3-letter IATA city code, e.g. “BER”. |  [optional] |
|**countryCode** | **String** | 2-letter ISO 3166-1 country code, e.g. “DE”. |  [optional] |
|**locationType** | **String** |  “Airport”, “RailwayStation” or “BusStation”. |  [optional] |
|**names** | [**AirportNames**](AirportNames.md) |  |  [optional] |
|**position** | [**AirportPosition**](AirportPosition.md) |  |  [optional] |
|**timeZoneId** | **String** | Time zone name airport is in |  [optional] |
|**utcOffset** | **Float** | Hour offset of airport to UTC time zone |  [optional] |



