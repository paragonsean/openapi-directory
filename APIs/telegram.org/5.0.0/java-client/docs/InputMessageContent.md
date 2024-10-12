

# InputMessageContent

This object represents the content of a message to be sent as a result of an inline query. Telegram clients currently support the following 4 types:

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disableWebPagePreview** | **Boolean** | *Optional*. Disables link previews for links in the sent message |  [optional] |
|**entities** | [**List&lt;MessageEntity&gt;**](MessageEntity.md) | *Optional*. List of special entities that appear in message text, which can be specified instead of *parse\\_mode* |  [optional] |
|**messageText** | **String** | Text of the message to be sent, 1-4096 characters |  |
|**parseMode** | **String** | *Optional*. Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. |  [optional] |
|**heading** | **Integer** | *Optional*. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. |  [optional] |
|**horizontalAccuracy** | **BigDecimal** | *Optional*. The radius of uncertainty for the location, measured in meters; 0-1500 |  [optional] |
|**latitude** | **BigDecimal** | Latitude of the venue in degrees |  |
|**livePeriod** | **Integer** | *Optional*. Period in seconds for which the location can be updated, should be between 60 and 86400. |  [optional] |
|**longitude** | **BigDecimal** | Longitude of the venue in degrees |  |
|**proximityAlertRadius** | **Integer** | *Optional*. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. |  [optional] |
|**address** | **String** | Address of the venue |  |
|**foursquareId** | **String** | *Optional*. Foursquare identifier of the venue, if known |  [optional] |
|**foursquareType** | **String** | *Optional*. Foursquare type of the venue, if known. (For example, “arts\\_entertainment/default”, “arts\\_entertainment/aquarium” or “food/icecream”.) |  [optional] |
|**googlePlaceId** | **String** | *Optional*. Google Places identifier of the venue |  [optional] |
|**googlePlaceType** | **String** | *Optional*. Google Places type of the venue. (See [supported types](https://developers.google.com/places/web-service/supported_types).) |  [optional] |
|**title** | **String** | Name of the venue |  |
|**firstName** | **String** | Contact&#39;s first name |  |
|**lastName** | **String** | *Optional*. Contact&#39;s last name |  [optional] |
|**phoneNumber** | **String** | Contact&#39;s phone number |  |
|**vcard** | **String** | *Optional*. Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard), 0-2048 bytes |  [optional] |



