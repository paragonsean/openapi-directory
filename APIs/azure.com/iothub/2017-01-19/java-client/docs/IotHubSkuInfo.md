

# IotHubSkuInfo

Information about the SKU of the IoT hub.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacity** | **Long** | The number of provisioned IoT Hub units. See: https://docs.microsoft.com/azure/azure-subscription-service-limits#iot-hub-limits. |  |
|**name** | [**NameEnum**](#NameEnum) | The name of the SKU. |  |
|**tier** | [**TierEnum**](#TierEnum) | The billing tier for the IoT hub. |  [optional] [readonly] |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| F1 | &quot;F1&quot; |
| S1 | &quot;S1&quot; |
| S2 | &quot;S2&quot; |
| S3 | &quot;S3&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| FREE | &quot;Free&quot; |
| STANDARD | &quot;Standard&quot; |



