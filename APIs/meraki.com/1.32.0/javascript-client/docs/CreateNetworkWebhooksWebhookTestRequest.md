# MerakiDashboardApi.CreateNetworkWebhooksWebhookTestRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertTypeId** | **String** | The type of alert which the test webhook will send. Optional. Defaults to power_supply_down. | [optional] [default to &#39;power_supply_down&#39;]
**payloadTemplateId** | **String** | The ID of the payload template of the test webhook. Defaults to the HTTP server&#39;s template ID if one exists for the given URL, or Generic template ID otherwise | [optional] 
**payloadTemplateName** | **String** | The name of the payload template. | [optional] 
**sharedSecret** | **String** | The shared secret the test webhook will send. Optional. Defaults to an empty string. | [optional] [default to &#39;&#39;]
**url** | **String** | The URL where the test webhook will be sent | 


