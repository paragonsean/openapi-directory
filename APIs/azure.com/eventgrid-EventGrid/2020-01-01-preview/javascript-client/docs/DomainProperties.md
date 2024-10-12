# EventGridManagementClient.DomainProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **String** | Endpoint for the domain. | [optional] [readonly] 
**inputSchema** | **String** | This determines the format that Event Grid should expect for incoming events published to the domain. | [optional] [default to &#39;EventGridSchema&#39;]
**inputSchemaMapping** | [**InputSchemaMapping**](InputSchemaMapping.md) |  | [optional] 
**metricResourceId** | **String** | Metric resource id for the domain. | [optional] [readonly] 
**provisioningState** | **String** | Provisioning state of the domain. | [optional] [readonly] 



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




