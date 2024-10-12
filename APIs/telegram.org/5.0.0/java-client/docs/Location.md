

# Location

This object represents a point on the map.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**heading** | **Integer** | *Optional*. The direction in which user is moving, in degrees; 1-360. For active live locations only. |  [optional] |
|**horizontalAccuracy** | **BigDecimal** | *Optional*. The radius of uncertainty for the location, measured in meters; 0-1500 |  [optional] |
|**latitude** | **BigDecimal** | Latitude as defined by sender |  |
|**livePeriod** | **Integer** | *Optional*. Time relative to the message sending date, during which the location can be updated, in seconds. For active live locations only. |  [optional] |
|**longitude** | **BigDecimal** | Longitude as defined by sender |  |
|**proximityAlertRadius** | **Integer** | *Optional*. Maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only. |  [optional] |



