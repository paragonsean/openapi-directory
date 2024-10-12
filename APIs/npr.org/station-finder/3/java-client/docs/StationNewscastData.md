

# StationNewscastData

Metadata about the newscast for this station; newscasts are handled internally by other microservices such as the NPR One Listening Service, so this data should typically not be used by consumers

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The ID of the newscast that should be played for this station; this is handled internally by other microservices such as the NPR One Listening Service, so this field should typically not be used by consumers |  |
|**recency** | **Integer** | How often the newscast should be played, in minutes; a value of &#x60;null&#x60; implies no information is available, and sensible defaults should be used |  |



