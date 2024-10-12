# ShipEngineApi.Carrier

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountNumber** | **String** | The account number that the carrier is connected to. | [optional] [readonly] 
**balance** | **Number** | Current available balance | [optional] [readonly] 
**carrierCode** | **String** | A string that uniquely identifies the carrier. | [optional] 
**carrierId** | **String** | A string that uniquely identifies the carrier. | [optional] [readonly] 
**friendlyName** | **String** | Screen readable name | [optional] [readonly] 
**hasMultiPackageSupportingServices** | **Boolean** | Carrier supports multiple packages per shipment | [optional] [readonly] 
**nickname** | **String** | Nickname given to the account when initially setting up the carrier. | [optional] [readonly] 
**options** | [**[CarrierAdvancedOption]**](CarrierAdvancedOption.md) | A list of options that are available to that carrier | [optional] [readonly] 
**packages** | [**[PackageType]**](PackageType.md) | A list of package types that are supported by the carrier | [optional] [readonly] 
**primary** | **Boolean** | Is this the primary carrier that is used by default when no carrier is specified in label/shipment creation | [optional] [readonly] 
**requiresFundedAmount** | **Boolean** | Indicates whether the carrier requires funding to use its services | [optional] [readonly] 
**services** | [**[Service]**](Service.md) | A list of services that are offered by the carrier | [optional] [readonly] 
**supportsLabelMessages** | **Boolean** | The carrier supports adding custom label messages to an order. | [optional] [readonly] 


