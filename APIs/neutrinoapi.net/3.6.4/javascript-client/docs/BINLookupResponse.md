# NeutrinoApi.BINLookupResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binNumber** | **String** | The BIN or IIN number | 
**cardBrand** | **String** | The card brand (e.g. Visa or Mastercard) | 
**cardCategory** | **String** | The card category. There are many different card categories the most common card categories are: CLASSIC, BUSINESS, CORPORATE, PLATINUM, PREPAID | 
**cardType** | **String** | The card type, will always be one of: DEBIT, CREDIT, CHARGE CARD | 
**country** | **String** | The full country name of the issuer | 
**countryCode** | **String** | The ISO 2-letter country code of the issuer | 
**countryCode3** | **String** | The ISO 3-letter country code of the issuer | 
**currencyCode** | **String** | ISO 4217 currency code associated with the country of the issuer | 
**ipBlocklisted** | **Boolean** | True if the customers IP is listed on one of our blocklists, see the &lt;a href&#x3D;\&quot;http://www.neutrinoapi.com/api/ip-blocklist/\&quot;&gt;IP Blocklist API&lt;/a&gt; | 
**ipBlocklists** | **[String]** | An array of strings indicating which blocklists this IP is listed on | 
**ipCity** | **String** | The city of the customers IP (if detectable) | 
**ipCountry** | **String** | The country of the customers IP | 
**ipCountryCode** | **String** | The ISO 2-letter country code of the customers IP | 
**ipCountryCode3** | **String** | The ISO 3-letter country code of the customers IP | 
**ipMatchesBin** | **Boolean** | True if the customers IP country matches the BIN country | 
**ipRegion** | **String** | The region of the customers IP (if detectable) | 
**isCommercial** | **Boolean** | Is this a commercial/business use card | 
**isPrepaid** | **Boolean** | Is this a prepaid or prepaid reloadable card | 
**issuer** | **String** | The card issuer | 
**issuerPhone** | **String** | The card issuers phone number | 
**issuerWebsite** | **String** | The card issuers website | 
**valid** | **Boolean** | Is this a valid BIN or IIN number | 


