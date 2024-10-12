

# CreateEndpointVariantRequest

The Variant properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isDefault** | **Boolean** | Is this the default variant. |  [optional] |
|**trafficPercentile** | **Float** | The amount of traffic variant receives. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the variant. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CONTROL | &quot;Control&quot; |
| TREATMENT | &quot;Treatment&quot; |



