

# PubsubEvent

An event indicating a received message or truncation event.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deleted** | **Boolean** | Indicates that this subscription has been deleted. (Note that pull subscribers will always receive NOT_FOUND in response in their pull request on the subscription, rather than seeing this boolean.) |  [optional] |
|**message** | [**PubsubMessage**](PubsubMessage.md) |  |  [optional] |
|**subscription** | **String** | The subscription that received the event. |  [optional] |
|**truncated** | **Boolean** | Indicates that this subscription has been truncated. |  [optional] |



