# ShipEngineApi.GetShipmentByExternalIdResponseBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advancedOptions** | [**AdvancedShipmentOptions**](AdvancedShipmentOptions.md) | Advanced shipment options.  These are entirely optional. | 
**carrierId** | **String** | The carrier account that is billed for the shipping charges | 
**confirmation** | [**DeliveryConfirmation**](DeliveryConfirmation.md) | The type of delivery confirmation that is required for this shipment. | 
**createdAt** | **Date** | The date and time that the shipment was created in ShipEngine. | [readonly] 
**customs** | [**InternationalShipmentOptions**](InternationalShipmentOptions.md) | Customs information.  This is usually only needed for international shipments.  | 
**externalOrderId** | **String** | ID that the Order Source assigned | [optional] 
**externalShipmentId** | **String** | A unique user-defined key to identify a shipment.  This can be used to retrieve the shipment.  &gt; **Warning:** The &#x60;external_shipment_id&#x60; is limited to 50 characters. Any additional characters will be truncated.  | [optional] 
**insuranceProvider** | [**InsuranceProvider**](InsuranceProvider.md) | The insurance provider to use for any insured packages in the shipment.  | 
**isReturn** | **Boolean** | An optional indicator if the shipment is intended to be a return. Defaults to false if not provided.  | [optional] [default to false]
**items** | [**[ShipmentItem]**](ShipmentItem.md) | Describe the packages included in this shipment as related to potential metadata that was imported from external order sources  | [optional] 
**modifiedAt** | **Date** | The date and time that the shipment was created or last modified. | [readonly] 
**orderSourceCode** | [**OrderSourceName**](OrderSourceName.md) |  | [optional] 
**originType** | [**OriginType**](OriginType.md) | Indicates if the package will be picked up or dropped off by the carrier | [optional] 
**packages** | [**[Package]**](Package.md) | The packages in the shipment.  &gt; **Note:** Some carriers only allow one package per shipment.  If you attempt to create a multi-package shipment for a carrier that doesn&#39;t allow it, an error will be returned.  | 
**returnTo** | [**ShippingAddress**](ShippingAddress.md) | The return address for this shipment.  Defaults to the &#x60;ship_from&#x60; address.  | 
**serviceCode** | **String** | The [carrier service](https://www.shipengine.com/docs/shipping/use-a-carrier-service/) used to ship the package, such as &#x60;fedex_ground&#x60;, &#x60;usps_first_class_mail&#x60;, &#x60;flat_rate_envelope&#x60;, etc.  | 
**shipDate** | **Date** | The date that the shipment was (or will be) shippped.  ShipEngine will take the day of week into consideration. For example, if the carrier does not operate on Sundays, then a package that would have shipped on Sunday will ship on Monday instead.  | 
**shipFrom** | [**ShippingAddress**](ShippingAddress.md) | The shipment&#39;s origin address. If you frequently ship from the same location, consider [creating a warehouse](https://www.shipengine.com/docs/reference/create-warehouse/).  Then you can simply specify the &#x60;warehouse_id&#x60; rather than the complete address each time.  | 
**shipTo** | [**ShippingAddress**](ShippingAddress.md) | The recipient&#39;s mailing address | 
**shipmentId** | **String** | A string that uniquely identifies the shipment | [readonly] 
**shipmentNumber** | **String** | A non-unique user-defined number used to identify a shipment.  If undefined, this will match the external_shipment_id of the shipment.  &gt; **Warning:** The &#x60;shipment_number&#x60; is limited to 50 characters. Any additional characters will be truncated.  | [optional] 
**shipmentStatus** | [**ShipmentStatus**](ShipmentStatus.md) | The current status of the shipment | [readonly] 
**tags** | [**[Tag]**](Tag.md) | Arbitrary tags associated with this shipment.  Tags can be used to categorize shipments, and shipments can be queried by their tags.  | [readonly] 
**taxIdentifiers** | [**[TaxIdentifier]**](TaxIdentifier.md) |  | [optional] 
**totalWeight** | [**Weight**](Weight.md) | The combined weight of all packages in the shipment | [readonly] 
**warehouseId** | **String** | The [warehouse](https://www.shipengine.com/docs/shipping/ship-from-a-warehouse/) that the shipment is being shipped from.  Either &#x60;warehouse_id&#x60; or &#x60;ship_from&#x60; must be specified.  | 


