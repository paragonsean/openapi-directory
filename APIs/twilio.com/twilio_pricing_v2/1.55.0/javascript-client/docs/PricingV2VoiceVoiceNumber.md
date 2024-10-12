# TwilioPricing.PricingV2VoiceVoiceNumber

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **String** | The name of the country. | [optional] 
**destinationNumber** | **String** | The destination phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number. | [optional] 
**inboundCallPrice** | [**PricingV2VoiceVoiceNumberInboundCallPrice**](PricingV2VoiceVoiceNumberInboundCallPrice.md) |  | [optional] 
**isoCountry** | **String** | The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) | [optional] 
**originationNumber** | **String** | The origination phone number in [[E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number. | [optional] 
**outboundCallPrices** | [**[PricingV2VoiceVoiceNumberOutboundCallPricesInner]**](PricingV2VoiceVoiceNumberOutboundCallPricesInner.md) | The list of [OutboundCallPriceWithOrigin](https://www.twilio.com/docs/voice/pricing#outbound-call-price-with-origin) records. | [optional] 
**priceUnit** | **String** | The currency in which prices are measured, specified in [ISO 4127](https://www.iso.org/iso/home/standards/currency_codes.htm) format (e.g. &#x60;usd&#x60;, &#x60;eur&#x60;, &#x60;jpy&#x60;). | [optional] 
**url** | **String** | The absolute URL of the resource. | [optional] 


