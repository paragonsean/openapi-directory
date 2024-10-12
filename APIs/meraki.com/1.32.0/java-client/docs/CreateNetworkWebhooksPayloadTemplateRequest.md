

# CreateNetworkWebhooksPayloadTemplateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | The liquid template used for the body of the webhook message. Either &#x60;body&#x60; or &#x60;bodyFile&#x60; must be specified. |  [optional] |
|**bodyFile** | **byte[]** | A file containing liquid template used for the body of the webhook message. Either &#x60;body&#x60; or &#x60;bodyFile&#x60; must be specified. |  [optional] |
|**headers** | [**List&lt;CreateNetworkWebhooksPayloadTemplateRequestHeadersInner&gt;**](CreateNetworkWebhooksPayloadTemplateRequestHeadersInner.md) | The liquid template used with the webhook headers. |  [optional] |
|**headersFile** | **byte[]** | A file containing the liquid template used with the webhook headers. |  [optional] |
|**name** | **String** | The name of the new template |  |



