

# WebHook


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **BigDecimal** | The time when this WebHook was created. This does not necessary mean the time when an manifest file was created. |  [optional] |
|**filter** | **List&lt;String&gt;** | An optional list of filter parameters for this webhook. |  [optional] |
|**id** | **String** | The unique identifier for this webhook. Can be used later to unregister the webhook. |  [optional] |
|**subscriptionIds** | **List&lt;String&gt;** | The optional list of userids for which this webhook is subscribed, i.e. presence events for the user are forwarded to the WebHook callback URL. |  [optional] |
|**type** | **String** | The type of a WebHook. This can either be MANUAL or EXTENSION. While manual WebHooks are only temporary and for development only use, permanent ones (EXTENSION) will bemanaged by the system. |  [optional] |
|**url** | **String** | The callback URL of this webhook. |  [optional] |
|**userId** | **String** | The user ID for which this webhook is subscribed, i.e. events for this user are forwarded to the WebHook callback URL. |  [optional] |



