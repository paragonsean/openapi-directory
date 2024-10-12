# BillbeeApi.BillbeeInterfacesBillbeeAPIModelCreateShipmentApiModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientReference** | **String** | Optional specify a text to be included on the label. Not possible with all carriers | [optional] 
**content** | **String** | Optional specify a text describing the content of the shipment. Used for export shipments | [optional] 
**customerNumber** | **String** | Not used anymore | [optional] 
**dimension** | [**BillbeeInterfacesShippingShipmentDataDimensions**](BillbeeInterfacesShippingShipmentDataDimensions.md) |  | [optional] 
**orderCurrencyCode** | **String** | The Currency if the ordersum | [optional] 
**orderSum** | **Number** | The value of the shipments content | [optional] 
**printerIdForExportDocs** | **Number** | The id of a connected Cloudprinter to sent the export docs to | [optional] 
**printerName** | **String** | The name of a connected Cloudprinter to sent the label to | [optional] 
**productCode** | **String** | The productcode to be used when creating the shipment. Values depends on the carrier used | [optional] 
**providerName** | **String** | The name of the provider as specified in the billbee account | [optional] 
**receiverAddress** | [**BillbeeInterfacesBillbeeAPIModelShipmentAddressApiModel**](BillbeeInterfacesBillbeeAPIModelShipmentAddressApiModel.md) |  | [optional] 
**services** | [**[BillbeeInterfacesShippingProductService]**](BillbeeInterfacesShippingProductService.md) | A list of services to be used when creating the shipment | [optional] 
**shipDate** | **Date** | Optional overwrite the shipdate to be transferred to the carrier | [optional] 
**totalNet** | **Number** | The value of the shipments content (net) | [optional] 
**weightInGram** | **Number** | Optional specify the weight in gram of the shipment | [optional] 
**shippingCarrier** | **Number** |  | [optional] 



## Enum: ShippingCarrierEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)

* `5` (value: `5`)

* `6` (value: `6`)

* `7` (value: `7`)

* `8` (value: `8`)

* `9` (value: `9`)

* `10` (value: `10`)

* `11` (value: `11`)

* `12` (value: `12`)

* `13` (value: `13`)

* `14` (value: `14`)

* `15` (value: `15`)

* `16` (value: `16`)

* `17` (value: `17`)

* `18` (value: `18`)




