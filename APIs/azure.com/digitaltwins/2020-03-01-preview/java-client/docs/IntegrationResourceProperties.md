

# IntegrationResourceProperties

Properties related to the IoTHub DigitalTwinsInstance Integration Resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdTime** | **OffsetDateTime** | Time when the IoTHub was added to DigitalTwinsInstance. |  [optional] [readonly] |
|**resourceId** | **String** | Fully qualified resource identifier of the DigitalTwins Azure resource. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | DigitalTwinsInstance - IoTHub link state. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| PROVISIONING | &quot;Provisioning&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



