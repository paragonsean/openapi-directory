# CloudSearchApi.RequestOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debugOptions** | [**DebugOptions**](DebugOptions.md) |  | [optional] 
**languageCode** | **String** | The BCP-47 language code, such as \&quot;en-US\&quot; or \&quot;sr-Latn\&quot;. For more information, see http://www.unicode.org/reports/tr35/#Unicode_locale_identifier. For translations. Set this field using the language set in browser or for the page. In the event that the user&#39;s language preference is known, set this field to the known user language. When specified, the documents in search results are biased towards the specified language. The Suggest API uses this field as a hint to make better third-party autocomplete predictions. | [optional] 
**searchApplicationId** | **String** | The ID generated when you create a search application using the [admin console](https://support.google.com/a/answer/9043922). | [optional] 
**timeZone** | **String** | Current user&#39;s time zone id, such as \&quot;America/Los_Angeles\&quot; or \&quot;Australia/Sydney\&quot;. These IDs are defined by [Unicode Common Locale Data Repository (CLDR)](http://cldr.unicode.org/) project, and currently available in the file [timezone.xml](http://unicode.org/repos/cldr/trunk/common/bcp47/timezone.xml). This field is used to correctly interpret date and time queries. If this field is not specified, the default time zone (UTC) is used. | [optional] 


