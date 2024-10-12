# AzureDigitalTwinsManagementClient.DigitalTwinsEndpointResourceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdTime** | **Date** | Time when the Endpoint was added to DigitalTwinsInstance. | [optional] [readonly] 
**endpointType** | **String** | The type of Digital Twins endpoint | 
**provisioningState** | **String** | The provisioning state. | [optional] [readonly] 
**tags** | **{String: String}** | The resource tags. | [optional] 



## Enum: EndpointTypeEnum


* `EventHub` (value: `"EventHub"`)

* `EventGrid` (value: `"EventGrid"`)

* `ServiceBus` (value: `"ServiceBus"`)





## Enum: ProvisioningStateEnum


* `Provisioning` (value: `"Provisioning"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)




