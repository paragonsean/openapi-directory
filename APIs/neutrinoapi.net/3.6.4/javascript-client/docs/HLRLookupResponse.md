# NeutrinoApi.HLRLookupResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **String** | The phone number country | 
**countryCode** | **String** | The number location as an ISO 2-letter country code | 
**countryCode3** | **String** | The number location as an ISO 3-letter country code | 
**currencyCode** | **String** | ISO 4217 currency code associated with the country | 
**currentNetwork** | **String** | The currently used network/carrier name | 
**hlrStatus** | **String** | The HLR lookup status, possible values are: &lt;br&gt; &lt;ul&gt; &lt;li&gt;ok - the HLR lookup was successful and the device is connected&lt;/li&gt; &lt;li&gt;absent - the number was once registered but the device has been switched off or out of network range for some time&lt;/li&gt; &lt;li&gt;unknown - the number is not known by the mobile network&lt;/li&gt; &lt;li&gt;invalid - the number is not a valid mobile MSISDN number&lt;/li&gt; &lt;li&gt;fixed-line - the number is a registered fixed-line not mobile&lt;/li&gt; &lt;li&gt;voip - the number has been detected as a VOIP line&lt;/li&gt; &lt;li&gt;failed - the HLR lookup has failed, we could not determine the real status of this number&lt;/li&gt; &lt;/ul&gt; | 
**hlrValid** | **Boolean** | Was the HLR lookup successful. If true then this is a working and registered cell-phone or mobile device (SMS and phone calls will be delivered) | 
**imsi** | **String** | The mobile IMSI number (International Mobile Subscriber Identity) | 
**internationalCallingCode** | **String** | The international calling code | 
**internationalNumber** | **String** | The number represented in full international format | 
**isMobile** | **Boolean** | True if this is a mobile number (only true with 100% certainty, if the number type is unknown this value will be false) | 
**isPorted** | **Boolean** | Has this number been ported to another network | 
**isRoaming** | **Boolean** | Is this number currently roaming from its origin country | 
**localNumber** | **String** | The number represented in local dialing format | 
**location** | **String** | The number location. Could be a city, region or country depending on the type of number | 
**mcc** | **String** | The mobile MCC number (Mobile Country Code) | 
**mnc** | **String** | The mobile MNC number (Mobile Network Code) | 
**msc** | **String** | The mobile MSC number (Mobile Switching Center) | 
**msin** | **String** | The mobile MSIN number (Mobile Subscription Identification Number) | 
**numberType** | **String** | The number type, possible values are: &lt;br&gt; &lt;ul&gt; &lt;li&gt;mobile&lt;/li&gt; &lt;li&gt;fixed-line&lt;/li&gt; &lt;li&gt;premium-rate&lt;/li&gt; &lt;li&gt;toll-free&lt;/li&gt; &lt;li&gt;voip&lt;/li&gt; &lt;li&gt;unknown&lt;/li&gt; &lt;/ul&gt; | 
**numberValid** | **Boolean** | True if this a valid phone number | 
**originNetwork** | **String** | The origin network/carrier name | 
**portedNetwork** | **String** | The ported to network/carrier name (only set if the number has been ported) | 
**roamingCountryCode** | **String** | If the number is currently roaming, the ISO 2-letter country code of the roaming in country | 


