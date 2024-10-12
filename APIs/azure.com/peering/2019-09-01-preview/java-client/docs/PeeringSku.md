

# PeeringSku

The SKU that defines the tier and kind of the peering.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**family** | [**FamilyEnum**](#FamilyEnum) | The family of the peering SKU. |  [optional] |
|**name** | [**NameEnum**](#NameEnum) | The name of the peering SKU. |  [optional] |
|**size** | [**SizeEnum**](#SizeEnum) | The size of the peering SKU. |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | The tier of the peering SKU. |  [optional] |



## Enum: FamilyEnum

| Name | Value |
|---- | -----|
| DIRECT | &quot;Direct&quot; |
| EXCHANGE | &quot;Exchange&quot; |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| BASIC_EXCHANGE_FREE | &quot;Basic_Exchange_Free&quot; |
| BASIC_DIRECT_FREE | &quot;Basic_Direct_Free&quot; |
| PREMIUM_EXCHANGE_METERED | &quot;Premium_Exchange_Metered&quot; |
| PREMIUM_DIRECT_FREE | &quot;Premium_Direct_Free&quot; |
| PREMIUM_DIRECT_METERED | &quot;Premium_Direct_Metered&quot; |
| PREMIUM_DIRECT_UNLIMITED | &quot;Premium_Direct_Unlimited&quot; |



## Enum: SizeEnum

| Name | Value |
|---- | -----|
| FREE | &quot;Free&quot; |
| METERED | &quot;Metered&quot; |
| UNLIMITED | &quot;Unlimited&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;Basic&quot; |
| PREMIUM | &quot;Premium&quot; |



