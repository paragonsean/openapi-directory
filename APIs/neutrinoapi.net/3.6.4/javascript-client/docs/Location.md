# NeutrinoApi.Location

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | The complete address using comma-separated values | 
**addressComponents** | **{String: String}** | The components which make up the address such as road, city, state, etc | 
**city** | **String** | The city of the location | 
**country** | **String** | The country of the location | 
**countryCode** | **String** | The ISO 2-letter country code of the location | 
**countryCode3** | **String** | The ISO 3-letter country code of the location | 
**currencyCode** | **String** | ISO 4217 currency code associated with the country | 
**latitude** | **Number** | The location latitude | 
**locationTags** | **[String]** | Array of strings containing any location tags associated with the address. Tags are additional pieces of metadata about a specific location, there are thousands of different tags. Some examples of tags: shop, office, cafe, bank, pub | 
**locationType** | **String** | The detected location type ordered roughly from most to least precise, possible values are: &lt;br&gt; &lt;ul&gt; &lt;li&gt;address - indicates a precise street address&lt;/li&gt; &lt;li&gt;street - accurate to the street level but may not point to the exact location of the house/building number&lt;/li&gt; &lt;li&gt;city - accurate to the city level, this includes villages, towns, suburbs, etc&lt;/li&gt; &lt;li&gt;postal-code - indicates a postal code area (no house or street information present)&lt;/li&gt; &lt;li&gt;railway - location is part of a rail network such as a station or railway track&lt;/li&gt; &lt;li&gt;natural - indicates a natural feature, for example a mountain peak or a waterway&lt;/li&gt; &lt;li&gt;island - location is an island or archipelago&lt;/li&gt; &lt;li&gt;administrative - indicates an administrative boundary such as a country, state or province&lt;/li&gt; &lt;/ul&gt; | 
**longitude** | **Number** | The location longitude | 
**postalAddress** | **String** | The formatted address using local standards suitable for printing on an envelope | 
**postalCode** | **String** | The postal code for the location | 
**regionCode** | **String** | The ISO 3166-2 region code for the location | 
**state** | **String** | The state of the location | 
**timezone** | [**Timezone**](Timezone.md) |  | 


