

# WritablePowerOutlet


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cable** | [**NestedCable**](NestedCable.md) |  |  [optional] |
|**connectedEndpoint** | **Map&lt;String, String&gt;** |  Return the appropriate serializer for the type of connected object.  |  [optional] [readonly] |
|**connectedEndpointType** | **String** |  |  [optional] [readonly] |
|**connectionStatus** | **Boolean** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**device** | **Integer** |  |  |
|**feedLeg** | [**FeedLegEnum**](#FeedLegEnum) | Phase (for three-phase feeds) |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**name** | **String** |  |  |
|**powerPort** | **Integer** |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Physical port type |  [optional] |



## Enum: FeedLegEnum

| Name | Value |
|---- | -----|
| A | &quot;A&quot; |
| B | &quot;B&quot; |
| C | &quot;C&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IEC_60320_C5 | &quot;iec-60320-c5&quot; |
| IEC_60320_C7 | &quot;iec-60320-c7&quot; |
| IEC_60320_C13 | &quot;iec-60320-c13&quot; |
| IEC_60320_C15 | &quot;iec-60320-c15&quot; |
| IEC_60320_C19 | &quot;iec-60320-c19&quot; |
| IEC_60309_P_N_E_4H | &quot;iec-60309-p-n-e-4h&quot; |
| IEC_60309_P_N_E_6H | &quot;iec-60309-p-n-e-6h&quot; |
| IEC_60309_P_N_E_9H | &quot;iec-60309-p-n-e-9h&quot; |
| IEC_60309_2P_E_4H | &quot;iec-60309-2p-e-4h&quot; |
| IEC_60309_2P_E_6H | &quot;iec-60309-2p-e-6h&quot; |
| IEC_60309_2P_E_9H | &quot;iec-60309-2p-e-9h&quot; |
| IEC_60309_3P_E_4H | &quot;iec-60309-3p-e-4h&quot; |
| IEC_60309_3P_E_6H | &quot;iec-60309-3p-e-6h&quot; |
| IEC_60309_3P_E_9H | &quot;iec-60309-3p-e-9h&quot; |
| IEC_60309_3P_N_E_4H | &quot;iec-60309-3p-n-e-4h&quot; |
| IEC_60309_3P_N_E_6H | &quot;iec-60309-3p-n-e-6h&quot; |
| IEC_60309_3P_N_E_9H | &quot;iec-60309-3p-n-e-9h&quot; |
| NEMA_1_15R | &quot;nema-1-15r&quot; |
| NEMA_5_15R | &quot;nema-5-15r&quot; |
| NEMA_5_20R | &quot;nema-5-20r&quot; |
| NEMA_5_30R | &quot;nema-5-30r&quot; |
| NEMA_5_50R | &quot;nema-5-50r&quot; |
| NEMA_6_15R | &quot;nema-6-15r&quot; |
| NEMA_6_20R | &quot;nema-6-20r&quot; |
| NEMA_6_30R | &quot;nema-6-30r&quot; |
| NEMA_6_50R | &quot;nema-6-50r&quot; |
| NEMA_10_30R | &quot;nema-10-30r&quot; |
| NEMA_10_50R | &quot;nema-10-50r&quot; |
| NEMA_14_20R | &quot;nema-14-20r&quot; |
| NEMA_14_30R | &quot;nema-14-30r&quot; |
| NEMA_14_50R | &quot;nema-14-50r&quot; |
| NEMA_14_60R | &quot;nema-14-60r&quot; |
| NEMA_L1_15R | &quot;nema-l1-15r&quot; |
| NEMA_L5_15R | &quot;nema-l5-15r&quot; |
| NEMA_L5_20R | &quot;nema-l5-20r&quot; |
| NEMA_L5_30R | &quot;nema-l5-30r&quot; |
| NEMA_L5_50R | &quot;nema-l5-50r&quot; |
| NEMA_L6_15R | &quot;nema-l6-15r&quot; |
| NEMA_L6_20R | &quot;nema-l6-20r&quot; |
| NEMA_L6_30R | &quot;nema-l6-30r&quot; |
| NEMA_L6_50R | &quot;nema-l6-50r&quot; |
| NEMA_L10_30R | &quot;nema-l10-30r&quot; |
| NEMA_L14_20R | &quot;nema-l14-20r&quot; |
| NEMA_L14_30R | &quot;nema-l14-30r&quot; |
| NEMA_L14_50R | &quot;nema-l14-50r&quot; |
| NEMA_L14_60R | &quot;nema-l14-60r&quot; |
| NEMA_L21_20R | &quot;nema-l21-20r&quot; |
| NEMA_L21_30R | &quot;nema-l21-30r&quot; |
| CS6360_C | &quot;CS6360C&quot; |
| CS6364_C | &quot;CS6364C&quot; |
| CS8164_C | &quot;CS8164C&quot; |
| CS8264_C | &quot;CS8264C&quot; |
| CS8364_C | &quot;CS8364C&quot; |
| CS8464_C | &quot;CS8464C&quot; |
| ITA_E | &quot;ita-e&quot; |
| ITA_F | &quot;ita-f&quot; |
| ITA_G | &quot;ita-g&quot; |
| ITA_H | &quot;ita-h&quot; |
| ITA_I | &quot;ita-i&quot; |
| ITA_J | &quot;ita-j&quot; |
| ITA_K | &quot;ita-k&quot; |
| ITA_L | &quot;ita-l&quot; |
| ITA_M | &quot;ita-m&quot; |
| ITA_N | &quot;ita-n&quot; |
| ITA_O | &quot;ita-o&quot; |
| HDOT_CX | &quot;hdot-cx&quot; |



