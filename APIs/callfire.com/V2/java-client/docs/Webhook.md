

# Webhook

Webhook is a user-defined callback, which can be maintained via API. CallFire will send POST request to a client's endpoint defined in webhook once one of assigned events is triggered. See [webhooks guide](https://developers.callfire.com/webhooks-guide.html) for more information about CallFire Webhooks API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callback** | **String** | URL that webhook will send POST to on resource event trigger |  [optional] |
|**createdAt** | **Long** | A time when the given resource was created, formatted in unix time milliseconds (read only). Example: 1473781817000 |  [optional] [readonly] |
|**enabled** | **Boolean** | A parameter which allows the webhook to send requests to unknown ssl endpoints (ssl certificate verification is disabled) |  [optional] |
|**events** | **Set&lt;String&gt;** | Comma separated list of events on resource that will trigger callbacks (ex: STARTED, STOPPED, FINISHED, etc...).  |  [optional] |
|**expiresAt** | **Long** | ~ |  [optional] |
|**fields** | **String** | A limit callback response to a particular fields |  [optional] |
|**id** | **Long** | An id of a webhook |  [optional] |
|**name** | **String** | A name of a webhook |  [optional] |
|**nonStrictSsl** | **Boolean** | A parameter which allows the webhook to send requests to unknown ssl endpoints (ssl certificate verification is disabled) |  [optional] |
|**resource** | **String** | A resource name that webhook is watching events on. Use GET /webhooks/resources to determine resources and events available (ex: InboundCall, OutboundCall, InboundText, OutboundText, CallBroadcast, TextBroadcast, etc...) |  [optional] |
|**secret** | **String** | Webhook secret token which is used as a signing key to HmacSHA1 hash of json payload which is returned in &#39;X-CallFire-Signature&#39; header. This header can be used to verify callback POST is coming from CallFire. See [security guide](https://developers.callfire.com/security-guide.html) |  [optional] |
|**singleUse** | **Boolean** | If true is set then webhook triggers only once. Afterwards the webhook will be deleted |  [optional] |
|**updatedAt** | **Long** | A time when the given resource was updated, formatted in unix time milliseconds (read only). Example: 1473781817000 |  [optional] [readonly] |



