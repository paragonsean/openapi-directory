

# CreateWebhookRequest

Request model for creating a webhook

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventTypeNames** | **List&lt;String&gt;** | List of names of event types |  |
|**isEnabled** | **Boolean** | Is enabled |  [optional] |
|**name** | **String** | Name |  |
|**secret** | **String** | Secret; used for event message signatures |  [optional] |
|**triggerExampleEvent** | **Boolean** | If set to true, an example event is being created |  [optional] |
|**url** | **String** | URL (must begin with the &#x60;HTTPS&#x60; scheme) |  |



