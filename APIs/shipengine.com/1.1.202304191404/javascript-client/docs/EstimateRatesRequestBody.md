# ShipEngineApi.EstimateRatesRequestBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressResidentialIndicator** | [**AddressResidentialIndicator**](AddressResidentialIndicator.md) |  | [optional] 
**confirmation** | [**DeliveryConfirmation**](DeliveryConfirmation.md) |  | [optional] 
**dimensions** | [**Dimensions**](Dimensions.md) | The dimensions of the package | [optional] 
**fromCityLocality** | **String** | from postal code | 
**fromCountryCode** | **String** | A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)  | 
**fromPostalCode** | **String** | postal code | 
**fromStateProvince** | **String** | From state province | 
**shipDate** | **Date** | ship date | 
**toCityLocality** | **String** | The city locality the package is being shipped to | 
**toCountryCode** | **String** | A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)  | 
**toPostalCode** | **String** | postal code | 
**toStateProvince** | **String** | To state province | 
**weight** | [**Weight**](Weight.md) | The weight of the package | 


