# PlaceKitApiReference.ReverseRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **String** | GPS coordinates latitude and longitude.\\ Used to improve relevancy of results around the given area.  | [optional] 
**countries** | **[String]** | Array of [two-letter ISO 3166-1 alpha-2 country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).\\ Limit the results to given countries.\\ Select only one country for the best results.  | [optional] 
**countryByIP** | **Boolean** | Automatically select the country to search in via the user IP&#39;s detected location.\\ Returned results will be coming from the user&#39;s country&#39;s IP.\\ If set to &#x60;true&#x60;, the parameter &#x60;countries&#x60; acts as a fallback.  | [optional] [default to true]
**language** | **String** | [Two-letter ISO 639-1 language code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).\\ Default results are in their original language.\\ By setting this parameter, you can change the language of the results, if the translation is available.\\ Contact us if you need other languages.  | [optional] 
**maxResults** | **Number** | Maximum number of results to return. | [optional] [default to 5]
**types** | [**[Types]**](Types.md) | Select the types of record to return.\\ Prepend with &#x60;-&#x60; to omit a type.\\ Returns all types by default.  | [optional] 



## Enum: LanguageEnum


* `en` (value: `"en"`)

* `fr` (value: `"fr"`)




