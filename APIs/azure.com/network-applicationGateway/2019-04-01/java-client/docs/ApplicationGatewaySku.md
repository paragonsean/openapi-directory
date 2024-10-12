

# ApplicationGatewaySku

SKU of an application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacity** | **Integer** | Capacity (instance count) of an application gateway. |  [optional] |
|**name** | [**NameEnum**](#NameEnum) | Name of an application gateway SKU. |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | Tier of an application gateway. |  [optional] |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| STANDARD_SMALL | &quot;Standard_Small&quot; |
| STANDARD_MEDIUM | &quot;Standard_Medium&quot; |
| STANDARD_LARGE | &quot;Standard_Large&quot; |
| WAF_MEDIUM | &quot;WAF_Medium&quot; |
| WAF_LARGE | &quot;WAF_Large&quot; |
| STANDARD_V2 | &quot;Standard_v2&quot; |
| WAF_V2 | &quot;WAF_v2&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |
| WAF | &quot;WAF&quot; |
| STANDARD_V2 | &quot;Standard_v2&quot; |
| WAF_V2 | &quot;WAF_v2&quot; |



