# MerakiDashboardApi.CreateNetworkWebhooksPayloadTemplateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **String** | The liquid template used for the body of the webhook message. Either &#x60;body&#x60; or &#x60;bodyFile&#x60; must be specified. | [optional] 
**bodyFile** | **Blob** | A file containing liquid template used for the body of the webhook message. Either &#x60;body&#x60; or &#x60;bodyFile&#x60; must be specified. | [optional] 
**headers** | [**[CreateNetworkWebhooksPayloadTemplateRequestHeadersInner]**](CreateNetworkWebhooksPayloadTemplateRequestHeadersInner.md) | The liquid template used with the webhook headers. | [optional] 
**headersFile** | **Blob** | A file containing the liquid template used with the webhook headers. | [optional] 
**name** | **String** | The name of the new template | 


