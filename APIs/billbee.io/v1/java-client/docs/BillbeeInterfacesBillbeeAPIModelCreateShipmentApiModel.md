

# BillbeeInterfacesBillbeeAPIModelCreateShipmentApiModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientReference** | **String** | Optional specify a text to be included on the label. Not possible with all carriers |  [optional] |
|**content** | **String** | Optional specify a text describing the content of the shipment. Used for export shipments |  [optional] |
|**customerNumber** | **String** | Not used anymore |  [optional] |
|**dimension** | [**BillbeeInterfacesShippingShipmentDataDimensions**](BillbeeInterfacesShippingShipmentDataDimensions.md) |  |  [optional] |
|**orderCurrencyCode** | **String** | The Currency if the ordersum |  [optional] |
|**orderSum** | **Double** | The value of the shipments content |  [optional] |
|**printerIdForExportDocs** | **Long** | The id of a connected Cloudprinter to sent the export docs to |  [optional] |
|**printerName** | **String** | The name of a connected Cloudprinter to sent the label to |  [optional] |
|**productCode** | **String** | The productcode to be used when creating the shipment. Values depends on the carrier used |  [optional] |
|**providerName** | **String** | The name of the provider as specified in the billbee account |  [optional] |
|**receiverAddress** | [**BillbeeInterfacesBillbeeAPIModelShipmentAddressApiModel**](BillbeeInterfacesBillbeeAPIModelShipmentAddressApiModel.md) |  |  [optional] |
|**services** | [**List&lt;BillbeeInterfacesShippingProductService&gt;**](BillbeeInterfacesShippingProductService.md) | A list of services to be used when creating the shipment |  [optional] |
|**shipDate** | **OffsetDateTime** | Optional overwrite the shipdate to be transferred to the carrier |  [optional] |
|**totalNet** | **Double** | The value of the shipments content (net) |  [optional] |
|**weightInGram** | **Double** | Optional specify the weight in gram of the shipment |  [optional] |
|**shippingCarrier** | [**ShippingCarrierEnum**](#ShippingCarrierEnum) |  |  [optional] |



## Enum: ShippingCarrierEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |
| NUMBER_5 | 5 |
| NUMBER_6 | 6 |
| NUMBER_7 | 7 |
| NUMBER_8 | 8 |
| NUMBER_9 | 9 |
| NUMBER_10 | 10 |
| NUMBER_11 | 11 |
| NUMBER_12 | 12 |
| NUMBER_13 | 13 |
| NUMBER_14 | 14 |
| NUMBER_15 | 15 |
| NUMBER_16 | 16 |
| NUMBER_17 | 17 |
| NUMBER_18 | 18 |



