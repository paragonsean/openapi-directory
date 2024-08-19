

# CreateAWebhookRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**secret** | **String** | This is a password you create, that Snyk uses to sign our transports to you, so you be sure the notification is authentic. Your &#x60;secret&#x60; should: Be a random string with high entropy; Not be used for anything else; Only known to Snyk and your webhook transport consuming code; |  [optional] |
|**url** | **String** | Webhooks can only be configured for URLs using the &#x60;https&#x60; protocol. &#x60;http&#x60; is not allowed. |  [optional] |



