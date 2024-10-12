# EventGridManagementClient.TopicProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowTrafficFromAllIPs** | **Boolean** | This determines if IP filtering rules ought to be evaluated or not. By default it will not evaluate and will allow traffic from all IPs. | [optional] 
**endpoint** | **String** | Endpoint for the topic. | [optional] [readonly] 
**inboundIpRules** | [**[InboundIpRule]**](InboundIpRule.md) | This determines the IP filtering rules that ought to be applied when events are received on this topic. | [optional] 
**inputSchema** | **String** | This determines the format that Event Grid should expect for incoming events published to the topic. | [optional] [default to &#39;EventGridSchema&#39;]
**inputSchemaMapping** | [**InputSchemaMapping**](InputSchemaMapping.md) |  | [optional] 
**metricResourceId** | **String** | Metric resource id for the topic. | [optional] [readonly] 
**provisioningState** | **String** | Provisioning state of the topic. | [optional] [readonly] 



## Enum: InputSchemaEnum


* `EventGridSchema` (value: `"EventGridSchema"`)

* `CustomEventSchema` (value: `"CustomEventSchema"`)

* `CloudEventSchemaV1_0` (value: `"CloudEventSchemaV1_0"`)





## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Canceled` (value: `"Canceled"`)

* `Failed` (value: `"Failed"`)




