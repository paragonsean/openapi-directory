# ShipEngineApi.AdvancedShipmentOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billToAccount** | **String** | This field is used to [bill shipping costs to a third party](https://www.shipengine.com/docs/shipping/bill-to-third-party/).  This field must be used in conjunction with the &#x60;bill_to_country_code&#x60;, &#x60;bill_to_party&#x60;, and &#x60;bill_to_postal_code&#x60; fields.  | [optional] 
**billToCountryCode** | **String** | The two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the third-party that is responsible for shipping costs.  | [optional] 
**billToParty** | [**BillToParty**](BillToParty.md) | Indicates whether to bill shipping costs to the recipient or to a third-party.  When billing to a third-party, the &#x60;bill_to_account&#x60;, &#x60;bill_to_country_code&#x60;, and &#x60;bill_to_postal_code&#x60; fields must also be set.  | [optional] 
**billToPostalCode** | **String** | The postal code of the third-party that is responsible for shipping costs.  | [optional] 
**collectOnDelivery** | [**CollectOnDelivery**](CollectOnDelivery.md) |  | [optional] 
**containsAlcohol** | **Boolean** | Indicates that the shipment contains alcohol. | [optional] [default to false]
**customField1** | **String** | An arbitrary field that can be used to store information about the shipment.  | [optional] 
**customField2** | **String** | An arbitrary field that can be used to store information about the shipment.  | [optional] 
**customField3** | **String** | An arbitrary field that can be used to store information about the shipment.  | [optional] 
**deliveredDutyPaid** | **Boolean** | Indicates that the shipper is paying the international delivery duties for this shipment.  This option is supported by UPS, FedEx, and DHL Express.  | [optional] [default to false]
**dryIce** | **Boolean** | Indicates if the shipment contain dry ice | [optional] [default to false]
**dryIceWeight** | [**Weight**](Weight.md) | The weight of the dry ice in the shipment | [optional] 
**fedexFreight** | [**AdvancedShipmentOptionsFedexFreight**](AdvancedShipmentOptionsFedexFreight.md) |  | [optional] 
**freightClass** | **String** | The National Motor Freight Traffic Association [freight class](http://www.nmfta.org/pages/nmfc?AspxAutoDetectCookieSupport&#x3D;1), such as \&quot;77.5\&quot;, \&quot;110\&quot;, or \&quot;250\&quot;.  | [optional] 
**nonMachinable** | **Boolean** | Indicates that the package cannot be processed automatically because it is too large or irregularly shaped. This is primarily for USPS shipments.  See [Section 1.2 of the USPS parcel standards](https://pe.usps.com/text/dmm300/101.htm#ep1047495) for details.  | [optional] [default to false]
**originType** | [**OriginType**](OriginType.md) |  | [optional] 
**saturdayDelivery** | **Boolean** | Enables Saturday delivery, if supported by the carrier. | [optional] [default to false]
**shipperRelease** | **Boolean** |  | [optional] 
**thirdPartyConsignee** | **Boolean** | Third Party Consignee option is a value-added service that allows the shipper to supply goods without commercial invoices being attached | [optional] [default to false]
**useUpsGroundFreightPricing** | **Boolean** | Whether to use [UPS Ground Freight pricing](https://www.shipengine.com/docs/shipping/ups-ground-freight/).  If enabled, then a &#x60;freight_class&#x60; must also be specified.  | [optional] 


