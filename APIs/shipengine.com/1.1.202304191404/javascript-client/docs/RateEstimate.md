# ShipEngineApi.RateEstimate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrierCode** | **String** | carrier code | [readonly] 
**carrierDeliveryDays** | **String** | The carrier delivery days | [optional] [readonly] 
**carrierFriendlyName** | **String** | carrier friendly name | [readonly] 
**carrierId** | **String** | A string that uniquely identifies the carrier | [readonly] 
**carrierNickname** | **String** | carrier nickname | [readonly] 
**confirmationAmount** | [**MonetaryValue**](MonetaryValue.md) | The confirmation amount | [readonly] 
**deliveryDays** | **Number** | The number of days estimated for delivery, this will show the _actual_ delivery time if for example, the package gets shipped on a Friday  | [optional] [readonly] 
**errorMessages** | **[String]** | The error messages | [readonly] 
**estimatedDeliveryDate** | **Date** | An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string that represents a date, but not a specific time.  The value _may_ contain a time component, but it will be set to &#x60;00:00:00&#x60; UTC by ShipEngine.  | [optional] [readonly] 
**guaranteedService** | **Boolean** | Indicates if the rate is guaranteed. | [readonly] 
**insuranceAmount** | [**MonetaryValue**](MonetaryValue.md) | The insurance amount | [readonly] 
**negotiatedRate** | **Boolean** | Indicates if the rates been negotiated | [readonly] 
**otherAmount** | [**MonetaryValue**](MonetaryValue.md) | Any other charges associated with this rate | [readonly] 
**packageType** | **String** | package type that this rate was estimated for | [readonly] 
**rateType** | [**RateType**](RateType.md) |  | [readonly] 
**serviceCode** | **String** | service code for the rate | [readonly] 
**serviceType** | **String** | service type | [readonly] 
**shipDate** | **Date** | ship date | [optional] [readonly] 
**shippingAmount** | [**MonetaryValue**](MonetaryValue.md) | The shipping amount | [readonly] 
**taxAmount** | [**MonetaryValue**](MonetaryValue.md) | Tariff and additional taxes associated with an international shipment. | [optional] [readonly] 
**trackable** | **Boolean** | Indicates if rate is trackable | [readonly] 
**validationStatus** | [**ValidationStatus**](ValidationStatus.md) |  | [readonly] 
**warningMessages** | **[String]** | The warning messages | [readonly] 
**zone** | **Number** | Certain carriers base [their rates](https://blog.stamps.com/2017/09/08/usps-postal-zones/) off of custom zones that vary depending upon the ship_to and ship_from location  | [readonly] 


