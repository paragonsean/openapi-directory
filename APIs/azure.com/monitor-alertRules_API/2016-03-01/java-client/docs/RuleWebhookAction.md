

# RuleWebhookAction

Specifies the action to post to service when the rule condition is evaluated. The discriminator is always RuleWebhookAction in this case.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | **Map&lt;String, String&gt;** | the dictionary of custom properties to include with the post operation. These data are appended to the webhook payload. |  [optional] |
|**serviceUri** | **String** | the service uri to Post the notification when the alert activates or resolves. |  [optional] |



