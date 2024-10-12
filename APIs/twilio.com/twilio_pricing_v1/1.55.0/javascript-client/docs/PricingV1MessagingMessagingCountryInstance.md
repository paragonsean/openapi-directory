# TwilioPricing.PricingV1MessagingMessagingCountryInstance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **String** | The name of the country. | [optional] 
**inboundSmsPrices** | [**[PricingV1MessagingMessagingCountryInstanceInboundSmsPricesInner]**](PricingV1MessagingMessagingCountryInstanceInboundSmsPricesInner.md) | The list of [InboundPrice](https://www.twilio.com/docs/sms/api/pricing#inbound-price) records that describe the price to receive an inbound SMS to the different Twilio phone number types supported in this country | [optional] 
**isoCountry** | **String** | The [ISO country code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). | [optional] 
**outboundSmsPrices** | [**[PricingV1MessagingMessagingCountryInstanceOutboundSmsPricesInner]**](PricingV1MessagingMessagingCountryInstanceOutboundSmsPricesInner.md) | The list of [OutboundSMSPrice](https://www.twilio.com/docs/sms/api/pricing#outbound-sms-price) records that represent the price to send a message for each MCC/MNC applicable in this country. | [optional] 
**priceUnit** | **String** | The currency in which prices are measured, specified in [ISO 4127](http://www.iso.org/iso/home/standards/currency_codes.htm) format (e.g. &#x60;usd&#x60;, &#x60;eur&#x60;, &#x60;jpy&#x60;). | [optional] 
**url** | **String** | The absolute URL of the resource. | [optional] 


