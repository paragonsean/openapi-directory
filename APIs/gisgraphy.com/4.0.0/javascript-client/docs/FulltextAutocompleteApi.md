# GisgraphyWebservices.FulltextAutocompleteApi

All URIs are relative to *http://free.gisgraphy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fulltxtsearch**](FulltextAutocompleteApi.md#fulltxtsearch) | **GET** /fulltext/search | search for places by text around a GPS point



## fulltxtsearch

> FulltextResultsDto fulltxtsearch(q, allwordsrequired, opts)

search for places by text around a GPS point

The full text service allows you to search for features / places / street and do autocompletion . you can : Specify one or more words search on part of the name (auto completion / suggestion) Search for text or zip code Specify a GPS restriction (promote nearest, not sorted but has an impact on the score), Limit the results to a specific Language, Country, place type, Paginate the results, Specify the output verbosity, Tells if you want the output to be indented, Tells that all words are required or not, The search is case insensitive, use synonyms (Saint/st, ..), separator characters stripping, ...

### Example

```javascript
import GisgraphyWebservices from 'gisgraphy_webservices';
let defaultClient = GisgraphyWebservices.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GisgraphyWebservices.FulltextAutocompleteApi();
let q = "q_example"; // String | The searched text : The text for the query can be a zip code, a string or one or more strings
let allwordsrequired = false; // Boolean | Whether the fulltext engine should considers all the words specified as required. Defaults to false (since v 4.0). possible values are true|false (or 'on' when used with the rest service)
let opts = {
  'spellchecking': "spellchecking_example", // String | The spellchecking (optional) : whether some suggestions should be provided if no results are found
  'lat': 3.4, // Number | The latitude (north-south) for the location point to search around. The value is a floating number, between -90 and +90. It uses GPS coordinates
  'lng': 3.4, // Number | TThe longitude (east-West) for the location point to search around. The value is a floating number between -180 and +180. It uses GPS coordinates.
  'radius': 10000.0, // Number | distance from the location point in meters we'd like to search around. The value is a number > 0 if it is not specify or incorrect.
  'suggest': false, // Boolean | If this parameter is set then it will search in part of the names of the street, place,.... It allow you to do auto completion auto suggestion. See the Gisgraphy leaflet plugin for more details. The JSON format will be forced if this parameter is true. See auto completion / suggestions engine for more details
  'style': "'MEDIUM'", // String | The output style verbosity (optional) : Determines the output verbosity. 4 styles are available
  'country': "country_example", // String | limit the search to the specified ISO 3166 country code. Default : search in all countries
  'lang': "lang_example", // String | The language code (optional) : The iso 639 Alpha2 or alpha3 Language Code. Some properties such as the AlternateName AdmNames and countryname belong to a certain language code. The language parameter can limit the output of those fields to a certain language (it only apply when style parameter='style') : If the language code does not exists or is not specified, properties with all the languages are retrieved If it exists, the properties with the specified language code, are retrieved
  'format': "'XML'", // String | The output format.
  'from': 1, // Number | The first pagination index. Numbered from 1. If the number is < 1 or not specified, it will be set to the default value : 1
  'to': 10, // Number | The last pagination index. if < 1 or not specified, it will be set to startindex + 10. Max = 10 (can be changed)
  'callback': "callback_example", // String | The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python)
  'indent': false // Boolean | indents the results.Default to false. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be 'on' or 'off', so for a simple use : the value of indent can be 'true' or 'on'
};
apiInstance.fulltxtsearch(q, allwordsrequired, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **String**| The searched text : The text for the query can be a zip code, a string or one or more strings | 
 **allwordsrequired** | **Boolean**| Whether the fulltext engine should considers all the words specified as required. Defaults to false (since v 4.0). possible values are true|false (or &#39;on&#39; when used with the rest service) | [default to false]
 **spellchecking** | **String**| The spellchecking (optional) : whether some suggestions should be provided if no results are found | [optional] 
 **lat** | **Number**| The latitude (north-south) for the location point to search around. The value is a floating number, between -90 and +90. It uses GPS coordinates | [optional] 
 **lng** | **Number**| TThe longitude (east-West) for the location point to search around. The value is a floating number between -180 and +180. It uses GPS coordinates. | [optional] 
 **radius** | **Number**| distance from the location point in meters we&#39;d like to search around. The value is a number &gt; 0 if it is not specify or incorrect. | [optional] [default to 10000.0]
 **suggest** | **Boolean**| If this parameter is set then it will search in part of the names of the street, place,.... It allow you to do auto completion auto suggestion. See the Gisgraphy leaflet plugin for more details. The JSON format will be forced if this parameter is true. See auto completion / suggestions engine for more details | [optional] [default to false]
 **style** | **String**| The output style verbosity (optional) : Determines the output verbosity. 4 styles are available | [optional] [default to &#39;MEDIUM&#39;]
 **country** | **String**| limit the search to the specified ISO 3166 country code. Default : search in all countries | [optional] 
 **lang** | **String**| The language code (optional) : The iso 639 Alpha2 or alpha3 Language Code. Some properties such as the AlternateName AdmNames and countryname belong to a certain language code. The language parameter can limit the output of those fields to a certain language (it only apply when style parameter&#x3D;&#39;style&#39;) : If the language code does not exists or is not specified, properties with all the languages are retrieved If it exists, the properties with the specified language code, are retrieved | [optional] 
 **format** | **String**| The output format. | [optional] [default to &#39;XML&#39;]
 **from** | **Number**| The first pagination index. Numbered from 1. If the number is &lt; 1 or not specified, it will be set to the default value : 1 | [optional] [default to 1]
 **to** | **Number**| The last pagination index. if &lt; 1 or not specified, it will be set to startindex + 10. Max &#x3D; 10 (can be changed) | [optional] [default to 10]
 **callback** | **String**| The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python) | [optional] 
 **indent** | **Boolean**| indents the results.Default to false. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be &#39;on&#39; or &#39;off&#39;, so for a simple use : the value of indent can be &#39;true&#39; or &#39;on&#39; | [optional] [default to false]

### Return type

[**FulltextResultsDto**](FulltextResultsDto.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, application/php, application/ruby, application/yaml, application/python, text/plain

