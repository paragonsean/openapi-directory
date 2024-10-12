# BrandedFaresUpsell.ExtendedPricingOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corporateCodes** | **[String]** | Allow Corporate negotiated fares using one or more corporate number (corporate code). | [optional] 
**fareType** | **[String]** | type of fare of the flight-offer | [optional] 
**includedCheckedBagsOnly** | **Boolean** | If true, returns the flight-offers with included checked bags only | [optional] 
**minimumDelayBeforeTicketing** | **String** | Required delay before being able to ticket. This option ensures that the system will only search for flight-offers which can still be ticketed the last day after this delay. If booked on the same day as the search (with respect to provider timezone), such flight-offers are guaranteed to be thereafter valid for ticketing at least during this delay (last day included). This option has no effect on flight-offers for which the last ticketing date does not make sense. Overrides the default settings. Max 365D | [optional] 
**noPenaltyFare** | **Boolean** | If true, returns the flight-offers with no penalty fares only | [optional] 
**noRestrictionFare** | **Boolean** | If true, returns the flight-offers with no restriction fares only | [optional] 
**refundableFare** | **Boolean** | If true, returns the flight-offers with refundable fares only | [optional] 



## Enum: [FareTypeEnum]


* `PUBLISHED` (value: `"PUBLISHED"`)

* `NEGOTIATED` (value: `"NEGOTIATED"`)

* `CORPORATE` (value: `"CORPORATE"`)




