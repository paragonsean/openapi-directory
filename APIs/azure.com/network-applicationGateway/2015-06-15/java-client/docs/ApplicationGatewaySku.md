

# ApplicationGatewaySku

SKU of application gateway

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacity** | **Integer** | Capacity (instance count) of an application gateway. |  [optional] |
|**name** | [**NameEnum**](#NameEnum) | Name of an application gateway SKU. Possible values are: &#39;Standard_Small&#39;, &#39;Standard_Medium&#39;, &#39;Standard_Large&#39;, &#39;WAF_Medium&#39;, and &#39;WAF_Large&#39;. |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | Tier of an application gateway. |  [optional] |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| SMALL | &quot;Standard_Small&quot; |
| MEDIUM | &quot;Standard_Medium&quot; |
| LARGE | &quot;Standard_Large&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |



