

# FeaturedTag

Represents a hashtag that is featured on a profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The internal ID of the featured tag in the database. Cast from integer but not guaranteed to be a number |  [optional] |
|**lastStatusAt** | **OffsetDateTime** | The timestamp of the last authored status containing this hashtag. ISO 8601 Datetime. |  [optional] |
|**name** | **String** | The name of the hashtag being featured. |  [optional] |
|**statusesCount** | **Integer** | The number of authored statuses containing this hashtag. |  [optional] |
|**url** | **String** | A link to all statuses by a user that contain this hashtag. |  [optional] |



