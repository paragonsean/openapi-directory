

# DigitalTwinsProperties

The properties of a DigitalTwinsInstance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdTime** | **OffsetDateTime** | Time when DigitalTwinsInstance was created. |  [optional] [readonly] |
|**hostName** | **String** | Api endpoint to work with DigitalTwinsInstance. |  [optional] [readonly] |
|**lastUpdatedTime** | **OffsetDateTime** | Time when DigitalTwinsInstance was created. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| PROVISIONING | &quot;Provisioning&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



