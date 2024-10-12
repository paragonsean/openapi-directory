# FulltextAutocompleteApi

All URIs are relative to *http://free.gisgraphy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fulltxtsearch**](FulltextAutocompleteApi.md#fulltxtsearch) | **GET** /fulltext/search | search for places by text around a GPS point |


<a id="fulltxtsearch"></a>
# **fulltxtsearch**
> FulltextResultsDto fulltxtsearch(q, allwordsrequired, spellchecking, lat, lng, radius, suggest, style, country, lang, format, from, to, paramCallback, indent)

search for places by text around a GPS point

The full text service allows you to search for features / places / street and do autocompletion . you can : Specify one or more words search on part of the name (auto completion / suggestion) Search for text or zip code Specify a GPS restriction (promote nearest, not sorted but has an impact on the score), Limit the results to a specific Language, Country, place type, Paginate the results, Specify the output verbosity, Tells if you want the output to be indented, Tells that all words are required or not, The search is case insensitive, use synonyms (Saint/st, ..), separator characters stripping, ...

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FulltextAutocompleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://free.gisgraphy.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FulltextAutocompleteApi apiInstance = new FulltextAutocompleteApi(defaultClient);
    String q = "q_example"; // String | The searched text : The text for the query can be a zip code, a string or one or more strings
    Boolean allwordsrequired = false; // Boolean | Whether the fulltext engine should considers all the words specified as required. Defaults to false (since v 4.0). possible values are true|false (or 'on' when used with the rest service)
    String spellchecking = "spellchecking_example"; // String | The spellchecking (optional) : whether some suggestions should be provided if no results are found
    Double lat = 3.4D; // Double | The latitude (north-south) for the location point to search around. The value is a floating number, between -90 and +90. It uses GPS coordinates
    Double lng = 3.4D; // Double | TThe longitude (east-West) for the location point to search around. The value is a floating number between -180 and +180. It uses GPS coordinates.
    Double radius = 10000.0D; // Double | distance from the location point in meters we'd like to search around. The value is a number > 0 if it is not specify or incorrect.
    Boolean suggest = false; // Boolean | If this parameter is set then it will search in part of the names of the street, place,.... It allow you to do auto completion auto suggestion. See the Gisgraphy leaflet plugin for more details. The JSON format will be forced if this parameter is true. See auto completion / suggestions engine for more details
    String style = "SHORT"; // String | The output style verbosity (optional) : Determines the output verbosity. 4 styles are available
    String country = "country_example"; // String | limit the search to the specified ISO 3166 country code. Default : search in all countries
    String lang = "lang_example"; // String | The language code (optional) : The iso 639 Alpha2 or alpha3 Language Code. Some properties such as the AlternateName AdmNames and countryname belong to a certain language code. The language parameter can limit the output of those fields to a certain language (it only apply when style parameter='style') : If the language code does not exists or is not specified, properties with all the languages are retrieved If it exists, the properties with the specified language code, are retrieved
    String format = "XML"; // String | The output format.
    Integer from = 1; // Integer | The first pagination index. Numbered from 1. If the number is < 1 or not specified, it will be set to the default value : 1
    Integer to = 10; // Integer | The last pagination index. if < 1 or not specified, it will be set to startindex + 10. Max = 10 (can be changed)
    String paramCallback = "paramCallback_example"; // String | The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python)
    Boolean indent = false; // Boolean | indents the results.Default to false. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be 'on' or 'off', so for a simple use : the value of indent can be 'true' or 'on'
    try {
      FulltextResultsDto result = apiInstance.fulltxtsearch(q, allwordsrequired, spellchecking, lat, lng, radius, suggest, style, country, lang, format, from, to, paramCallback, indent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FulltextAutocompleteApi#fulltxtsearch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **q** | **String**| The searched text : The text for the query can be a zip code, a string or one or more strings | |
| **allwordsrequired** | **Boolean**| Whether the fulltext engine should considers all the words specified as required. Defaults to false (since v 4.0). possible values are true|false (or &#39;on&#39; when used with the rest service) | [default to false] |
| **spellchecking** | **String**| The spellchecking (optional) : whether some suggestions should be provided if no results are found | [optional] |
| **lat** | **Double**| The latitude (north-south) for the location point to search around. The value is a floating number, between -90 and +90. It uses GPS coordinates | [optional] |
| **lng** | **Double**| TThe longitude (east-West) for the location point to search around. The value is a floating number between -180 and +180. It uses GPS coordinates. | [optional] |
| **radius** | **Double**| distance from the location point in meters we&#39;d like to search around. The value is a number &gt; 0 if it is not specify or incorrect. | [optional] [default to 10000.0] |
| **suggest** | **Boolean**| If this parameter is set then it will search in part of the names of the street, place,.... It allow you to do auto completion auto suggestion. See the Gisgraphy leaflet plugin for more details. The JSON format will be forced if this parameter is true. See auto completion / suggestions engine for more details | [optional] [default to false] |
| **style** | **String**| The output style verbosity (optional) : Determines the output verbosity. 4 styles are available | [optional] [default to MEDIUM] [enum: SHORT, MEDIUM, LONG, FULL] |
| **country** | **String**| limit the search to the specified ISO 3166 country code. Default : search in all countries | [optional] |
| **lang** | **String**| The language code (optional) : The iso 639 Alpha2 or alpha3 Language Code. Some properties such as the AlternateName AdmNames and countryname belong to a certain language code. The language parameter can limit the output of those fields to a certain language (it only apply when style parameter&#x3D;&#39;style&#39;) : If the language code does not exists or is not specified, properties with all the languages are retrieved If it exists, the properties with the specified language code, are retrieved | [optional] |
| **format** | **String**| The output format. | [optional] [default to XML] [enum: XML, JSON, PHP, RUBY, PYTHON, YAML, ATOM, GEORSS] |
| **from** | **Integer**| The first pagination index. Numbered from 1. If the number is &lt; 1 or not specified, it will be set to the default value : 1 | [optional] [default to 1] |
| **to** | **Integer**| The last pagination index. if &lt; 1 or not specified, it will be set to startindex + 10. Max &#x3D; 10 (can be changed) | [optional] [default to 10] |
| **paramCallback** | **String**| The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python) | [optional] |
| **indent** | **Boolean**| indents the results.Default to false. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be &#39;on&#39; or &#39;off&#39;, so for a simple use : the value of indent can be &#39;true&#39; or &#39;on&#39; | [optional] [default to false] |

### Return type

[**FulltextResultsDto**](FulltextResultsDto.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/php, application/ruby, application/yaml, application/python, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sucessfully processed |  -  |
| **401** | Need auth. The API key parameter is missing or wrong, or doesn&#39;t correspond to any subscriptions |  -  |
| **403** | Unhauthorize (auth will change nothing).Your IP is not allowed. |  -  |
| **412** | Missing parameter. Some parameters required for the webservices ar missing, please consult documentation |  -  |
| **429** | Too many requests. You exceed the authorized rate |  -  |
| **500** | Internal error |  -  |

