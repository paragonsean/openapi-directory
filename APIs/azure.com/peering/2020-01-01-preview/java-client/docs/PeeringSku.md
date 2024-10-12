

# PeeringSku

The SKU that defines the tier and kind of the peering.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**family** | [**FamilyEnum**](#FamilyEnum) | The family of the peering SKU. |  [optional] |
|**name** | **String** | The name of the peering SKU. |  [optional] |
|**size** | [**SizeEnum**](#SizeEnum) | The size of the peering SKU. |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | The tier of the peering SKU. |  [optional] |



## Enum: FamilyEnum

| Name | Value |
|---- | -----|
| DIRECT | &quot;Direct&quot; |
| EXCHANGE | &quot;Exchange&quot; |



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



