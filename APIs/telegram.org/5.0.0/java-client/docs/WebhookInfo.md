

# WebhookInfo

Contains information about the current status of a webhook.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedUpdates** | **List&lt;String&gt;** | *Optional*. A list of update types the bot is subscribed to. Defaults to all update types |  [optional] |
|**hasCustomCertificate** | **Boolean** | True, if a custom certificate was provided for webhook certificate checks |  |
|**ipAddress** | **String** | *Optional*. Currently used webhook IP address |  [optional] |
|**lastErrorDate** | **Integer** | *Optional*. Unix time for the most recent error that happened when trying to deliver an update via webhook |  [optional] |
|**lastErrorMessage** | **String** | *Optional*. Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook |  [optional] |
|**maxConnections** | **Integer** | *Optional*. Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery |  [optional] |
|**pendingUpdateCount** | **Integer** | Number of updates awaiting delivery |  |
|**url** | **String** | Webhook URL, may be empty if webhook is not set up |  |



