

# PricingV1VoiceVoiceCountryInstance


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**country** | **String** | The name of the country. |  [optional] |
|**inboundCallPrices** | [**List&lt;PricingV1VoiceVoiceCountryInstanceInboundCallPricesInner&gt;**](PricingV1VoiceVoiceCountryInstanceInboundCallPricesInner.md) | The list of [InboundCallPrice](https://www.twilio.com/docs/voice/pricing#inbound-call-price) records. |  [optional] |
|**isoCountry** | **String** | The [ISO country code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |  [optional] |
|**outboundPrefixPrices** | [**List&lt;PricingV1VoiceVoiceCountryInstanceOutboundPrefixPricesInner&gt;**](PricingV1VoiceVoiceCountryInstanceOutboundPrefixPricesInner.md) | The list of OutboundPrefixPrice records, which include a list of the &#x60;prefixes&#x60;, the &#x60;friendly_name&#x60;, &#x60;base_price&#x60;, and the   &#x60;current_price&#x60; for those prefixes. |  [optional] |
|**priceUnit** | **String** | The currency in which prices are measured, specified in [ISO 4127](http://www.iso.org/iso/home/standards/currency_codes.htm) format (e.g. &#x60;usd&#x60;, &#x60;eur&#x60;, &#x60;jpy&#x60;). |  [optional] |
|**url** | **URI** | The absolute URL of the resource. |  [optional] |



