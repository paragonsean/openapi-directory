

# NetworkConfig

Network configuration for ManagementServer instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**network** | **String** | Optional. The resource name of the Google Compute Engine VPC network to which the ManagementServer instance is connected. |  [optional] |
|**peeringMode** | [**PeeringModeEnum**](#PeeringModeEnum) | Optional. The network connect mode of the ManagementServer instance. For this version, only PRIVATE_SERVICE_ACCESS is supported. |  [optional] |



## Enum: PeeringModeEnum

| Name | Value |
|---- | -----|
| PEERING_MODE_UNSPECIFIED | &quot;PEERING_MODE_UNSPECIFIED&quot; |
| PRIVATE_SERVICE_ACCESS | &quot;PRIVATE_SERVICE_ACCESS&quot; |



