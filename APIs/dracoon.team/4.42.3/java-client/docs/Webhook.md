

# Webhook

Webhook information

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | Creation date |  |
|**createdBy** | [**UserInfo**](UserInfo.md) |  |  [optional] |
|**eventTypeNames** | **List&lt;String&gt;** | List of names of event types |  |
|**expireAt** | **OffsetDateTime** | Expiration date / time |  |
|**failStatus** | **Integer** | Last HTTP status code when a webhook is disabled due to delivery failures |  [optional] |
|**id** | **Long** | ID |  |
|**isEnabled** | **Boolean** | Is enabled |  |
|**name** | **String** | Name |  |
|**secret** | **String** | Secret; used for event message signatures |  [optional] |
|**updatedAt** | **OffsetDateTime** | Modification date |  |
|**updatedBy** | [**UserInfo**](UserInfo.md) |  |  [optional] |
|**url** | **String** | URL |  |



