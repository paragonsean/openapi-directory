

# AzureSku

Azure SKU definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacity** | **Integer** | The number of instances of the cluster. |  [optional] |
|**name** | [**NameEnum**](#NameEnum) | SKU name. |  |
|**tier** | [**TierEnum**](#TierEnum) | SKU tier. |  |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| STANDARD_DS13_V2_1_TB_PS | &quot;Standard_DS13_v2+1TB_PS&quot; |
| STANDARD_DS13_V2_2_TB_PS | &quot;Standard_DS13_v2+2TB_PS&quot; |
| STANDARD_DS14_V2_3_TB_PS | &quot;Standard_DS14_v2+3TB_PS&quot; |
| STANDARD_DS14_V2_4_TB_PS | &quot;Standard_DS14_v2+4TB_PS&quot; |
| STANDARD_D13_V2 | &quot;Standard_D13_v2&quot; |
| STANDARD_D14_V2 | &quot;Standard_D14_v2&quot; |
| STANDARD_L8S | &quot;Standard_L8s&quot; |
| STANDARD_L16S | &quot;Standard_L16s&quot; |
| STANDARD_D11_V2 | &quot;Standard_D11_v2&quot; |
| STANDARD_D12_V2 | &quot;Standard_D12_v2&quot; |
| STANDARD_L4S | &quot;Standard_L4s&quot; |
| DEV_NO_SLA__STANDARD_D11_V2 | &quot;Dev(No SLA)_Standard_D11_v2&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;Basic&quot; |
| STANDARD | &quot;Standard&quot; |



