# ViatorApiDocumentationAmpSpecificationMerchantPartners.SearchFreetextResponseDestinationAllOfData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultCurrencyCode** | **String** | **currency code** for the currency in which pricing is displayed | [optional] 
**destinationId** | **Number** | **unique numeric identifier** of the destination - use this value as the &#x60;destId&#x60; input field for other Viator API services  | [optional] 
**destinationName** | **String** | **natural-language name** of the destination | [optional] 
**destinationType** | [**DestinationType**](DestinationType.md) |  | [optional] 
**destinationUrlName** | **String** | ignore - (Viator only) | [optional] 
**iataCode** | **String** | **IATA airport code** for the destination - a three-letter code defined by the International Air Transport Association (IATA) used to identify many airports around the world - the IATA code is also known as an &#39;IATA location identifier&#39;, &#39;IATA station code&#39; or simply a &#39;location identifier&#39; - the IATA code is &amp;lt;u&amp;gt;not available&amp;lt;/u&amp;gt; for destinations with a destination type of &#x60;&#39;COUNTRY&#39;&#x60; or &#x60;&#39;REGION&#39;&#x60;, as there could be more than one airport within a destination  | [optional] 
**latitude** | **Number** | **latitude component** of the destination&#39;s geolocation | [optional] 
**longitude** | **Number** | **longitude component** of the destination&#39;s geolocation | [optional] 
**lookupId** | **String** | **hierarchy location specifier** for the destination that is a concatenation of all &#x60;parentId&#x60; and &#x60;destinationId&#x60; codes - e.g. &#x60;&#39;8.77.673&#39;&#x60; for Chicago - format: [top level &#x60;parentId&#x60;].[any additional &#x60;parentId&#x60;].[&#x60;destinationId&#x60;]  | [optional] 
**parentId** | **Number** | **unique numeric identifier** of the destination&#39;s parent destination | [optional] 
**selectable** | **Boolean** | ignore - (Viator only) | [optional] 
**sortOrder** | **Number** | **sort order** for this response | [optional] 
**timeZone** | **String** | **time zone** of the destination | [optional] 


