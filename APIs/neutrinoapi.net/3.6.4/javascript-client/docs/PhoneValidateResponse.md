# NeutrinoApi.PhoneValidateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **String** | The phone number country | 
**countryCode** | **String** | The phone number country as an ISO 2-letter country code | 
**countryCode3** | **String** | The phone number country as an ISO 3-letter country code | 
**currencyCode** | **String** | ISO 4217 currency code associated with the country | 
**internationalCallingCode** | **String** | The international calling code | 
**internationalNumber** | **String** | The number represented in full international format (E.164) | 
**isMobile** | **Boolean** | True if this is a mobile number. If the number type is unknown this value will be false | 
**localNumber** | **String** | The number represented in local dialing format | 
**location** | **String** | The phone number location. Could be the city, region or country depending on the type of number | 
**prefixNetwork** | **String** | The network/carrier who owns the prefix (this only works for some countries, use HLR lookup for global network detection) | 
**type** | **String** | The number type based on the number prefix. &lt;br&gt;Possible values are: &lt;br&gt; &lt;ul&gt; &lt;li&gt;mobile&lt;/li&gt; &lt;li&gt;fixed-line&lt;/li&gt; &lt;li&gt;premium-rate&lt;/li&gt; &lt;li&gt;toll-free&lt;/li&gt; &lt;li&gt;voip&lt;/li&gt; &lt;li&gt;unknown (use HLR lookup)&lt;/li&gt; &lt;/ul&gt; | 
**valid** | **Boolean** | Is this a valid phone number | 


