

# BulkexportsV1ExportConfiguration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | If true, Twilio will automatically generate every day&#39;s file when the day is over. |  [optional] |
|**resourceType** | **String** | The type of communication – Messages, Calls, Conferences, and Participants |  [optional] |
|**url** | **URI** | The URL of this resource. |  [optional] |
|**webhookMethod** | **String** | Sets whether Twilio should call a webhook URL when the automatic generation is complete, using GET or POST. The actual destination is set in the webhook_url |  [optional] |
|**webhookUrl** | **URI** | Stores the URL destination for the method specified in webhook_method. |  [optional] |



