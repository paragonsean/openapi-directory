

# ApplicationGatewaySku

SKU of an application gateway

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacity** | **Integer** | Capacity (instance count) of an application gateway. |  [optional] |
|**name** | [**NameEnum**](#NameEnum) | Name of an application gateway SKU. Possible values are: &#39;Standard_Small&#39;, &#39;Standard_Medium&#39;, &#39;Standard_Large&#39;, &#39;WAF_Medium&#39;, and &#39;WAF_Large&#39;. |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | Tier of an application gateway. Possible values are: &#39;Standard&#39; and &#39;WAF&#39;. |  [optional] |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| STANDARD_SMALL | &quot;Standard_Small&quot; |
| STANDARD_MEDIUM | &quot;Standard_Medium&quot; |
| STANDARD_LARGE | &quot;Standard_Large&quot; |
| WAF_MEDIUM | &quot;WAF_Medium&quot; |
| WAF_LARGE | &quot;WAF_Large&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |
| WAF | &quot;WAF&quot; |



