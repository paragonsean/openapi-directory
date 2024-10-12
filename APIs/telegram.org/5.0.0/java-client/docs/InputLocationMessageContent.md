

# InputLocationMessageContent

Represents the [content](https://core.telegram.org/bots/api/#inputmessagecontent) of a location message to be sent as the result of an inline query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**heading** | **Integer** | *Optional*. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. |  [optional] |
|**horizontalAccuracy** | **BigDecimal** | *Optional*. The radius of uncertainty for the location, measured in meters; 0-1500 |  [optional] |
|**latitude** | **BigDecimal** | Latitude of the location in degrees |  |
|**livePeriod** | **Integer** | *Optional*. Period in seconds for which the location can be updated, should be between 60 and 86400. |  [optional] |
|**longitude** | **BigDecimal** | Longitude of the location in degrees |  |
|**proximityAlertRadius** | **Integer** | *Optional*. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. |  [optional] |



