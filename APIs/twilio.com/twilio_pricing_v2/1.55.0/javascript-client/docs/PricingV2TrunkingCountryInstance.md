# TwilioPricing.PricingV2TrunkingCountryInstance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **String** | The name of the country. | [optional] 
**isoCountry** | **String** | The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). | [optional] 
**originatingCallPrices** | [**[PricingV2TrunkingCountryInstanceOriginatingCallPricesInner]**](PricingV2TrunkingCountryInstanceOriginatingCallPricesInner.md) | The list of [OriginatingCallPrice](https://www.twilio.com/docs/voice/pricing#inbound-call-price) records. | [optional] 
**priceUnit** | **String** | The currency in which prices are measured, specified in [ISO 4127](https://www.iso.org/iso/home/standards/currency_codes.htm) format (e.g. &#x60;usd&#x60;, &#x60;eur&#x60;, &#x60;jpy&#x60;). | [optional] 
**terminatingPrefixPrices** | [**[PricingV2TrunkingCountryInstanceTerminatingPrefixPricesInner]**](PricingV2TrunkingCountryInstanceTerminatingPrefixPricesInner.md) | The list of [TerminatingPrefixPrice](https://www.twilio.com/docs/voice/pricing#outbound-prefix-price-with-origin) records. | [optional] 
**url** | **String** | The absolute URL of the resource. | [optional] 


