

# Sku

The sku determines the type of environment, either standard (S1 or S2) or long-term (L1). For standard environments the sku determines the capacity of the environment, the ingress rate, and the billing rate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacity** | **Integer** | The capacity of the sku. For standard environments, this value can be changed to support scale out of environments after they have been created. |  |
|**name** | [**NameEnum**](#NameEnum) | The name of this SKU. |  |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| S1 | &quot;S1&quot; |
| S2 | &quot;S2&quot; |
| P1 | &quot;P1&quot; |
| L1 | &quot;L1&quot; |



