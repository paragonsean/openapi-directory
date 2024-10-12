

# UpdateWebhookRequest

Request model for updating a webhook

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventTypeNames** | **List&lt;String&gt;** | List of names of event types |  [optional] |
|**isEnabled** | **Boolean** | Is enabled |  [optional] |
|**name** | **String** | Name |  [optional] |
|**secret** | **String** | Secret; used for event message signatures |  [optional] |
|**triggerExampleEvent** | **Boolean** | If set to true, an example event is being created |  [optional] |
|**url** | **String** | URL (must begin with the &#x60;HTTPS&#x60; scheme) |  [optional] |



