

# DigitalTwinsEndpointResourceProperties

Properties related to Digital Twins Endpoint

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdTime** | **OffsetDateTime** | Time when the Endpoint was added to DigitalTwinsInstance. |  [optional] [readonly] |
|**endpointType** | [**EndpointTypeEnum**](#EndpointTypeEnum) | The type of Digital Twins endpoint |  |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state. |  [optional] [readonly] |
|**tags** | **Map&lt;String, String&gt;** | The resource tags. |  [optional] |



## Enum: EndpointTypeEnum

| Name | Value |
|---- | -----|
| EVENT_HUB | &quot;EventHub&quot; |
| EVENT_GRID | &quot;EventGrid&quot; |
| SERVICE_BUS | &quot;ServiceBus&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| PROVISIONING | &quot;Provisioning&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



