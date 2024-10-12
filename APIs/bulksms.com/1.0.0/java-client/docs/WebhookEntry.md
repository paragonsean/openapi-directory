

# WebhookEntry


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | Indicates whether you want the webhook activated.  If the value is &#x60;true&#x60;, the webhook at the given &#x60;url&#x60; will be invoked with an empty array (&#x60;[]&#x60;) as part of the validation process. If the webhook responds with a &#x60;2xx&#x60; status code, the submission is accepted; if not the webhook is not created (or updated).  If the value is &#x60;false&#x60; the webhook will be inactive, and it will not be invoked when messages are &#x60;SENT&#x60; or &#x60;RECEIVED&#x60;.  The default value is &#x60;true&#x60;.  |  [optional] |
|**contactEmailAddress** | **String** | The email address to which emails will be sent if there are problem with invoking the webhook.  The value must be a valid email address. If this value is &#x60;null&#x60;, no email will be sent.  It is &#x60;null&#x60; by default.  |  [optional] |
|**invokeOption** | [**InvokeOptionEnum**](#InvokeOptionEnum) | Specifies how to invoke your webhook.  If the value is &#x60;ONE&#x60; the array POSTed to your webhook will contain no more than a single message.  Use this option if your webhook logic is unable to handle more than one messages at a time.  If the value is &#x60;MANY&#x60; the array POSTed to your webhook can contain up to 10 messages.  This is the recommended option.  The number of calls made to your webhook would be less and this will speed up your total processing time. If your webhook fails for an invoke that has more than one message, each message in the array will automatically be retried one at a time.   This value defaults to &#x60;ONE&#x60; - but it is recommended that you set this property to &#x60;MANY&#x60;.  |  [optional] |
|**name** | **String** | A text identifier for the webhook. More than one webhook cannot have the same name.  |  |
|**onWebApp** | **Boolean** | Indicates whether you want to show this webhook on the Web App.  Webhooks shown there can be updated by the user that use the public Web site.  The default value is &#x60;true&#x60;.  |  [optional] |
|**triggerScope** | [**TriggerScopeEnum**](#TriggerScopeEnum) | Specifies when the webhook will be triggered.    Please note the values are case sensitive.  If the value is &#x60;SENT&#x60;, the webhook will be called when a status update becomes available for a message you sent (i.e. a mobile terminating (MT) message).  If the value is &#x60;RECEIVED&#x60;, the webhook will be called when a message is received (i.e. a mobile originating (MO) message).  Note that this field forces you to create two separate webhook entries if you want to collect all messages.  However,  you can use the same &#x60;url&#x60; for both webhooks if you want.  |  |
|**url** | **String** | The location of the webhook.  In addition to being a [valid URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Syntax), the url must also start with &#x60;http&#x60; or &#x60;https&#x60;.  |  |



## Enum: InvokeOptionEnum

| Name | Value |
|---- | -----|
| ONE | &quot;ONE&quot; |
| MANY | &quot;MANY&quot; |



## Enum: TriggerScopeEnum

| Name | Value |
|---- | -----|
| SENT | &quot;SENT&quot; |
| RECEIVED | &quot;RECEIVED&quot; |



