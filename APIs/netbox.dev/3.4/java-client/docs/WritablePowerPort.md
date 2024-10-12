

# WritablePowerPort


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**occupied** | **Boolean** |  |  [optional] [readonly] |
|**allocatedDraw** | **Integer** | Allocated power draw (watts) |  [optional] |
|**cable** | [**NestedCable**](NestedCable.md) |  |  [optional] |
|**cableEnd** | **String** |  |  [optional] [readonly] |
|**connectedEndpoints** | **List&lt;String&gt;** |  Return the appropriate serializer for the type of connected object.  |  [optional] [readonly] |
|**connectedEndpointsReachable** | **Boolean** |  |  [optional] [readonly] |
|**connectedEndpointsType** | **String** |  |  [optional] [readonly] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**device** | **Integer** |  |  |
|**display** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**label** | **String** | Physical label |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**linkPeers** | **List&lt;String&gt;** |  Return the appropriate serializer for the link termination model.  |  [optional] [readonly] |
|**linkPeersType** | **String** |  |  [optional] [readonly] |
|**markConnected** | **Boolean** | Treat as if a cable is connected |  [optional] |
|**maximumDraw** | **Integer** | Maximum power draw (watts) |  [optional] |
|**module** | **Integer** |  |  [optional] |
|**name** | **String** |  |  |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Physical port type |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IEC_60320_C6 | &quot;iec-60320-c6&quot; |
| IEC_60320_C8 | &quot;iec-60320-c8&quot; |
| IEC_60320_C14 | &quot;iec-60320-c14&quot; |
| IEC_60320_C16 | &quot;iec-60320-c16&quot; |
| IEC_60320_C20 | &quot;iec-60320-c20&quot; |
| IEC_60320_C22 | &quot;iec-60320-c22&quot; |
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
| NEMA_1_15P | &quot;nema-1-15p&quot; |
| NEMA_5_15P | &quot;nema-5-15p&quot; |
| NEMA_5_20P | &quot;nema-5-20p&quot; |
| NEMA_5_30P | &quot;nema-5-30p&quot; |
| NEMA_5_50P | &quot;nema-5-50p&quot; |
| NEMA_6_15P | &quot;nema-6-15p&quot; |
| NEMA_6_20P | &quot;nema-6-20p&quot; |
| NEMA_6_30P | &quot;nema-6-30p&quot; |
| NEMA_6_50P | &quot;nema-6-50p&quot; |
| NEMA_10_30P | &quot;nema-10-30p&quot; |
| NEMA_10_50P | &quot;nema-10-50p&quot; |
| NEMA_14_20P | &quot;nema-14-20p&quot; |
| NEMA_14_30P | &quot;nema-14-30p&quot; |
| NEMA_14_50P | &quot;nema-14-50p&quot; |
| NEMA_14_60P | &quot;nema-14-60p&quot; |
| NEMA_15_15P | &quot;nema-15-15p&quot; |
| NEMA_15_20P | &quot;nema-15-20p&quot; |
| NEMA_15_30P | &quot;nema-15-30p&quot; |
| NEMA_15_50P | &quot;nema-15-50p&quot; |
| NEMA_15_60P | &quot;nema-15-60p&quot; |
| NEMA_L1_15P | &quot;nema-l1-15p&quot; |
| NEMA_L5_15P | &quot;nema-l5-15p&quot; |
| NEMA_L5_20P | &quot;nema-l5-20p&quot; |
| NEMA_L5_30P | &quot;nema-l5-30p&quot; |
| NEMA_L5_50P | &quot;nema-l5-50p&quot; |
| NEMA_L6_15P | &quot;nema-l6-15p&quot; |
| NEMA_L6_20P | &quot;nema-l6-20p&quot; |
| NEMA_L6_30P | &quot;nema-l6-30p&quot; |
| NEMA_L6_50P | &quot;nema-l6-50p&quot; |
| NEMA_L10_30P | &quot;nema-l10-30p&quot; |
| NEMA_L14_20P | &quot;nema-l14-20p&quot; |
| NEMA_L14_30P | &quot;nema-l14-30p&quot; |
| NEMA_L14_50P | &quot;nema-l14-50p&quot; |
| NEMA_L14_60P | &quot;nema-l14-60p&quot; |
| NEMA_L15_20P | &quot;nema-l15-20p&quot; |
| NEMA_L15_30P | &quot;nema-l15-30p&quot; |
| NEMA_L15_50P | &quot;nema-l15-50p&quot; |
| NEMA_L15_60P | &quot;nema-l15-60p&quot; |
| NEMA_L21_20P | &quot;nema-l21-20p&quot; |
| NEMA_L21_30P | &quot;nema-l21-30p&quot; |
| NEMA_L22_30P | &quot;nema-l22-30p&quot; |
| CS6361C | &quot;cs6361c&quot; |
| CS6365C | &quot;cs6365c&quot; |
| CS8165C | &quot;cs8165c&quot; |
| CS8265C | &quot;cs8265c&quot; |
| CS8365C | &quot;cs8365c&quot; |
| CS8465C | &quot;cs8465c&quot; |
| ITA_C | &quot;ita-c&quot; |
| ITA_E | &quot;ita-e&quot; |
| ITA_F | &quot;ita-f&quot; |
| ITA_EF | &quot;ita-ef&quot; |
| ITA_G | &quot;ita-g&quot; |
| ITA_H | &quot;ita-h&quot; |
| ITA_I | &quot;ita-i&quot; |
| ITA_J | &quot;ita-j&quot; |
| ITA_K | &quot;ita-k&quot; |
| ITA_L | &quot;ita-l&quot; |
| ITA_M | &quot;ita-m&quot; |
| ITA_N | &quot;ita-n&quot; |
| ITA_O | &quot;ita-o&quot; |
| USB_A | &quot;usb-a&quot; |
| USB_B | &quot;usb-b&quot; |
| USB_C | &quot;usb-c&quot; |
| USB_MINI_A | &quot;usb-mini-a&quot; |
| USB_MINI_B | &quot;usb-mini-b&quot; |
| USB_MICRO_A | &quot;usb-micro-a&quot; |
| USB_MICRO_B | &quot;usb-micro-b&quot; |
| USB_MICRO_AB | &quot;usb-micro-ab&quot; |
| USB_3_B | &quot;usb-3-b&quot; |
| USB_3_MICRO_B | &quot;usb-3-micro-b&quot; |
| DC_TERMINAL | &quot;dc-terminal&quot; |
| SAF_D_GRID | &quot;saf-d-grid&quot; |
| NEUTRIK_POWERCON_20 | &quot;neutrik-powercon-20&quot; |
| NEUTRIK_POWERCON_32 | &quot;neutrik-powercon-32&quot; |
| NEUTRIK_POWERCON_TRUE1 | &quot;neutrik-powercon-true1&quot; |
| NEUTRIK_POWERCON_TRUE1_TOP | &quot;neutrik-powercon-true1-top&quot; |
| UBIQUITI_SMARTPOWER | &quot;ubiquiti-smartpower&quot; |
| HARDWIRED | &quot;hardwired&quot; |
| OTHER | &quot;other&quot; |



