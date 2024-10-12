

# RechnungsdruckWebAppControllersApiShipmentWithLabel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**changeStateToSend** | **Boolean** | Optional parameter to automatically change the orderstate to sent after creating the shipment |  [optional] |
|**clientReference** | **String** | Optional specify a reference text to be included on the label. Works not with all carriers |  [optional] |
|**dimension** | [**BillbeeInterfacesShippingShipmentDataDimensions**](BillbeeInterfacesShippingShipmentDataDimensions.md) |  |  [optional] |
|**orderId** | **Long** | The Billbee internal id of the order to ship |  [optional] |
|**printerName** | **String** | Optional the name of a connected cloudprinter to send the label to |  [optional] |
|**productId** | **Long** | the id of the shipping provider product to be used |  [optional] |
|**providerId** | **Long** | The id of the provider. You can query all providers with the shippingproviders endpoint |  [optional] |
|**shipDate** | **OffsetDateTime** | Optional specify the shipdate to be transmitted to the carrier |  [optional] |
|**weightInGram** | **Integer** | Optional the shipments weight in gram to override the calculated weight |  [optional] |



