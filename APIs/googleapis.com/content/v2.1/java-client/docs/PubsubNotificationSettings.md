

# PubsubNotificationSettings

Settings for Pub/Sub notifications, all methods require that the caller is a direct user of the merchant center account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cloudTopicName** | **String** | Cloud pub/sub topic to which notifications are sent (read-only). |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;&#x60;content#pubsubNotificationSettings&#x60;\&quot; |  [optional] |
|**registeredEvents** | **List&lt;String&gt;** | List of event types. Acceptable values are: - \&quot;&#x60;orderPendingShipment&#x60;\&quot;  |  [optional] |



