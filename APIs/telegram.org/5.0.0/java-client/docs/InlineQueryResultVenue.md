

# InlineQueryResultVenue

Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the venue.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | Address of the venue |  |
|**foursquareId** | **String** | *Optional*. Foursquare identifier of the venue if known |  [optional] |
|**foursquareType** | **String** | *Optional*. Foursquare type of the venue, if known. (For example, “arts\\_entertainment/default”, “arts\\_entertainment/aquarium” or “food/icecream”.) |  [optional] |
|**googlePlaceId** | **String** | *Optional*. Google Places identifier of the venue |  [optional] |
|**googlePlaceType** | **String** | *Optional*. Google Places type of the venue. (See [supported types](https://developers.google.com/places/web-service/supported_types).) |  [optional] |
|**id** | **String** | Unique identifier for this result, 1-64 Bytes |  |
|**inputMessageContent** | [**InputMessageContent**](InputMessageContent.md) |  |  [optional] |
|**latitude** | **BigDecimal** | Latitude of the venue location in degrees |  |
|**longitude** | **BigDecimal** | Longitude of the venue location in degrees |  |
|**replyMarkup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  |  [optional] |
|**thumbHeight** | **Integer** | *Optional*. Thumbnail height |  [optional] |
|**thumbUrl** | **String** | *Optional*. Url of the thumbnail for the result |  [optional] |
|**thumbWidth** | **Integer** | *Optional*. Thumbnail width |  [optional] |
|**title** | **String** | Title of the venue |  |
|**type** | **String** | Type of the result, must be *venue* |  |



