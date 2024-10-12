# GitHubV3RestApi.WebhookConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentType** | **String** | The media type used to serialize the payloads. Supported values include &#x60;json&#x60; and &#x60;form&#x60;. The default is &#x60;form&#x60;. | [optional] 
**insecureSsl** | [**WebhookConfigInsecureSsl**](WebhookConfigInsecureSsl.md) |  | [optional] 
**secret** | **String** | If provided, the &#x60;secret&#x60; will be used as the &#x60;key&#x60; to generate the HMAC hex digest value for [delivery signature headers](https://docs.github.com/enterprise-server@3.2/webhooks/event-payloads/#delivery-headers). | [optional] 
**url** | **String** | The URL to which the payloads will be delivered. | [optional] 


