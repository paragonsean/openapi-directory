# ShipEngineApi.GetCarrierSettingsResponseBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isPrimaryAccount** | **Boolean** | Indicates if this is the primary UPS account | [optional] 
**nickname** | **String** | nickname | [optional] 
**shouldHideAccountNumberOnArchiveDoc** | **Boolean** | Indicates if the account number should be hidden on the archive documentation | [optional] 
**letterheadImage** | **String** |  | [optional] 
**pickupType** | [**UpsPickupType**](UpsPickupType.md) |  | [optional] 
**signatureImage** | **String** |  | [optional] 
**smartPostEndorsement** | [**AncillaryServiceEndorsement**](AncillaryServiceEndorsement.md) |  | [optional] 
**smartPostHub** | [**SmartPostHub**](SmartPostHub.md) |  | [optional] 
**accountPostalCode** | **String** | account postal code | [optional] 
**invoice** | [**UpsInvoice**](UpsInvoice.md) | The invoice | [optional] 
**mailInnovationsCostCenter** | **String** | mail innovations cost center | [optional] 
**mailInnovationsEndorsement** | [**AncillaryServiceEndorsement**](AncillaryServiceEndorsement.md) |  | [optional] 
**useCarbonNeutralShippingProgram** | **Boolean** | The use carbon neutral shipping program | [optional] 
**useConsolidationServices** | **Boolean** | The use consolidation services | [optional] 
**useGroundFreightPricing** | **Boolean** | The use ground freight pricing | [optional] 
**useNegotiatedRates** | **Boolean** | The use negotiated rates | [optional] 
**useOrderNumberOnMailInnovationsLabels** | **Boolean** | The use order number on mail innovations labels | [optional] 


