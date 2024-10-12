

# InlineQueryResultLocation

Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**heading** | **Integer** | *Optional*. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. |  [optional] |
|**horizontalAccuracy** | **BigDecimal** | *Optional*. The radius of uncertainty for the location, measured in meters; 0-1500 |  [optional] |
|**id** | **String** | Unique identifier for this result, 1-64 Bytes |  |
|**inputMessageContent** | [**InputMessageContent**](InputMessageContent.md) |  |  [optional] |
|**latitude** | **BigDecimal** | Location latitude in degrees |  |
|**livePeriod** | **Integer** | *Optional*. Period in seconds for which the location can be updated, should be between 60 and 86400. |  [optional] |
|**longitude** | **BigDecimal** | Location longitude in degrees |  |
|**proximityAlertRadius** | **Integer** | *Optional*. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. |  [optional] |
|**replyMarkup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  |  [optional] |
|**thumbHeight** | **Integer** | *Optional*. Thumbnail height |  [optional] |
|**thumbUrl** | **String** | *Optional*. Url of the thumbnail for the result |  [optional] |
|**thumbWidth** | **Integer** | *Optional*. Thumbnail width |  [optional] |
|**title** | **String** | Location title |  |
|**type** | **String** | Type of the result, must be *location* |  |



