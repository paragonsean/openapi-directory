# CustomSearchApi.CseApi

All URIs are relative to *https://customsearch.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchCseList**](CseApi.md#searchCseList) | **GET** /customsearch/v1 | 
[**searchCseSiterestrictList**](CseApi.md#searchCseSiterestrictList) | **GET** /customsearch/v1/siterestrict | 



## searchCseList

> Search searchCseList(opts)



Returns metadata about the search performed, metadata about the engine used for the search, and the search results.

### Example

```javascript
import CustomSearchApi from 'custom_search_api';

let apiInstance = new CustomSearchApi.CseApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'c2coff': "c2coff_example", // String | Enables or disables [Simplified and Traditional Chinese Search](https://developers.google.com/custom-search/docs/json_api_reference#chineseSearch). The default value for this parameter is 0 (zero), meaning that the feature is enabled. Supported values are: * `1`: Disabled * `0`: Enabled (default)
  'cr': "cr_example", // String | Restricts search results to documents originating in a particular country. You may use [Boolean operators](https://developers.google.com/custom-search/docs/json_api_reference#booleanOperators) in the cr parameter's value. Google Search determines the country of a document by analyzing: * the top-level domain (TLD) of the document's URL * the geographic location of the Web server's IP address See the [Country Parameter Values](https://developers.google.com/custom-search/docs/json_api_reference#countryCollections) page for a list of valid values for this parameter.
  'cx': "cx_example", // String | The Programmable Search Engine ID to use for this request.
  'dateRestrict': "dateRestrict_example", // String | Restricts results to URLs based on date. Supported values include: * `d[number]`: requests results from the specified number of past days. * `w[number]`: requests results from the specified number of past weeks. * `m[number]`: requests results from the specified number of past months. * `y[number]`: requests results from the specified number of past years.
  'exactTerms': "exactTerms_example", // String | Identifies a phrase that all documents in the search results must contain.
  'excludeTerms': "excludeTerms_example", // String | Identifies a word or phrase that should not appear in any documents in the search results.
  'fileType': "fileType_example", // String | Restricts results to files of a specified extension. A list of file types indexable by Google can be found in Search Console [Help Center](https://support.google.com/webmasters/answer/35287).
  'filter': "filter_example", // String | Controls turning on or off the duplicate content filter. * See [Automatic Filtering](https://developers.google.com/custom-search/docs/json_api_reference#automaticFiltering) for more information about Google's search results filters. Note that host crowding filtering applies only to multi-site searches. * By default, Google applies filtering to all search results to improve the quality of those results. Acceptable values are: * `0`: Turns off duplicate content filter. * `1`: Turns on duplicate content filter.
  'gl': "gl_example", // String | Geolocation of end user. * The `gl` parameter value is a two-letter country code. The `gl` parameter boosts search results whose country of origin matches the parameter value. See the [Country Codes](https://developers.google.com/custom-search/docs/json_api_reference#countryCodes) page for a list of valid values. * Specifying a `gl` parameter value should lead to more relevant results. This is particularly true for international customers and, even more specifically, for customers in English- speaking countries other than the United States.
  'googlehost': "googlehost_example", // String | **Deprecated**. Use the `gl` parameter for a similar effect. The local Google domain (for example, google.com, google.de, or google.fr) to use to perform the search.
  'highRange': "highRange_example", // String | Specifies the ending value for a search range. * Use `lowRange` and `highRange` to append an inclusive search range of `lowRange...highRange` to the query.
  'hl': "hl_example", // String | Sets the user interface language. * Explicitly setting this parameter improves the performance and the quality of your search results. * See the [Interface Languages](https://developers.google.com/custom-search/docs/json_api_reference#wsInterfaceLanguages) section of [Internationalizing Queries and Results Presentation](https://developers.google.com/custom-search/docs/json_api_reference#wsInternationalizing) for more information, and [Supported Interface Languages](https://developers.google.com/custom-search/docs/json_api_reference#interfaceLanguages) for a list of supported languages.
  'hq': "hq_example", // String | Appends the specified query terms to the query, as if they were combined with a logical AND operator.
  'imgColorType': "imgColorType_example", // String | Returns black and white, grayscale, transparent, or color images. Acceptable values are: * `\"color\"` * `\"gray\"` * `\"mono\"`: black and white * `\"trans\"`: transparent background
  'imgDominantColor': "imgDominantColor_example", // String | Returns images of a specific dominant color. Acceptable values are: * `\"black\"` * `\"blue\"` * `\"brown\"` * `\"gray\"` * `\"green\"` * `\"orange\"` * `\"pink\"` * `\"purple\"` * `\"red\"` * `\"teal\"` * `\"white\"` * `\"yellow\"`
  'imgSize': "imgSize_example", // String | Returns images of a specified size. Acceptable values are: * `\"huge\"` * `\"icon\"` * `\"large\"` * `\"medium\"` * `\"small\"` * `\"xlarge\"` * `\"xxlarge\"`
  'imgType': "imgType_example", // String | Returns images of a type. Acceptable values are: * `\"clipart\"` * `\"face\"` * `\"lineart\"` * `\"stock\"` * `\"photo\"` * `\"animated\"`
  'linkSite': "linkSite_example", // String | Specifies that all search results should contain a link to a particular URL.
  'lowRange': "lowRange_example", // String | Specifies the starting value for a search range. Use `lowRange` and `highRange` to append an inclusive search range of `lowRange...highRange` to the query.
  'lr': "lr_example", // String | Restricts the search to documents written in a particular language (e.g., `lr=lang_ja`). Acceptable values are: * `\"lang_ar\"`: Arabic * `\"lang_bg\"`: Bulgarian * `\"lang_ca\"`: Catalan * `\"lang_cs\"`: Czech * `\"lang_da\"`: Danish * `\"lang_de\"`: German * `\"lang_el\"`: Greek * `\"lang_en\"`: English * `\"lang_es\"`: Spanish * `\"lang_et\"`: Estonian * `\"lang_fi\"`: Finnish * `\"lang_fr\"`: French * `\"lang_hr\"`: Croatian * `\"lang_hu\"`: Hungarian * `\"lang_id\"`: Indonesian * `\"lang_is\"`: Icelandic * `\"lang_it\"`: Italian * `\"lang_iw\"`: Hebrew * `\"lang_ja\"`: Japanese * `\"lang_ko\"`: Korean * `\"lang_lt\"`: Lithuanian * `\"lang_lv\"`: Latvian * `\"lang_nl\"`: Dutch * `\"lang_no\"`: Norwegian * `\"lang_pl\"`: Polish * `\"lang_pt\"`: Portuguese * `\"lang_ro\"`: Romanian * `\"lang_ru\"`: Russian * `\"lang_sk\"`: Slovak * `\"lang_sl\"`: Slovenian * `\"lang_sr\"`: Serbian * `\"lang_sv\"`: Swedish * `\"lang_tr\"`: Turkish * `\"lang_zh-CN\"`: Chinese (Simplified) * `\"lang_zh-TW\"`: Chinese (Traditional)
  'num': 56, // Number | Number of search results to return. * Valid values are integers between 1 and 10, inclusive.
  'orTerms': "orTerms_example", // String | Provides additional search terms to check for in a document, where each document in the search results must contain at least one of the additional search terms.
  'q': "q_example", // String | Query
  'relatedSite': "relatedSite_example", // String | Deprecated.
  'rights': "rights_example", // String | Filters based on licensing. Supported values include: `cc_publicdomain`, `cc_attribute`, `cc_sharealike`, `cc_noncommercial`, `cc_nonderived` and combinations of these. See [typical combinations](https://wiki.creativecommons.org/wiki/CC_Search_integration).
  'safe': "safe_example", // String | Search safety level. Acceptable values are: * `\"active\"`: Enables SafeSearch filtering. * `\"off\"`: Disables SafeSearch filtering. (default)
  'searchType': "searchType_example", // String | Specifies the search type: `image`. If unspecified, results are limited to webpages. Acceptable values are: * `\"image\"`: custom image search.
  'siteSearch': "siteSearch_example", // String | Specifies a given site which should always be included or excluded from results (see `siteSearchFilter` parameter, below).
  'siteSearchFilter': "siteSearchFilter_example", // String | Controls whether to include or exclude results from the site named in the `siteSearch` parameter. Acceptable values are: * `\"e\"`: exclude * `\"i\"`: include
  'sort': "sort_example", // String | The sort expression to apply to the results. The sort parameter specifies that the results be sorted according to the specified expression i.e. sort by date. [Example: sort=date](https://developers.google.com/custom-search/docs/structured_search#sort-by-attribute).
  'start': 56 // Number | The index of the first result to return. The default number of results per page is 10, so `&start=11` would start at the top of the second page of results. **Note**: The JSON API will never return more than 100 results, even if more than 100 documents match the query, so setting the sum of `start + num` to a number greater than 100 will produce an error. Also note that the maximum value for `num` is 10.
};
apiInstance.searchCseList(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **c2coff** | **String**| Enables or disables [Simplified and Traditional Chinese Search](https://developers.google.com/custom-search/docs/json_api_reference#chineseSearch). The default value for this parameter is 0 (zero), meaning that the feature is enabled. Supported values are: * &#x60;1&#x60;: Disabled * &#x60;0&#x60;: Enabled (default) | [optional] 
 **cr** | **String**| Restricts search results to documents originating in a particular country. You may use [Boolean operators](https://developers.google.com/custom-search/docs/json_api_reference#booleanOperators) in the cr parameter&#39;s value. Google Search determines the country of a document by analyzing: * the top-level domain (TLD) of the document&#39;s URL * the geographic location of the Web server&#39;s IP address See the [Country Parameter Values](https://developers.google.com/custom-search/docs/json_api_reference#countryCollections) page for a list of valid values for this parameter. | [optional] 
 **cx** | **String**| The Programmable Search Engine ID to use for this request. | [optional] 
 **dateRestrict** | **String**| Restricts results to URLs based on date. Supported values include: * &#x60;d[number]&#x60;: requests results from the specified number of past days. * &#x60;w[number]&#x60;: requests results from the specified number of past weeks. * &#x60;m[number]&#x60;: requests results from the specified number of past months. * &#x60;y[number]&#x60;: requests results from the specified number of past years. | [optional] 
 **exactTerms** | **String**| Identifies a phrase that all documents in the search results must contain. | [optional] 
 **excludeTerms** | **String**| Identifies a word or phrase that should not appear in any documents in the search results. | [optional] 
 **fileType** | **String**| Restricts results to files of a specified extension. A list of file types indexable by Google can be found in Search Console [Help Center](https://support.google.com/webmasters/answer/35287). | [optional] 
 **filter** | **String**| Controls turning on or off the duplicate content filter. * See [Automatic Filtering](https://developers.google.com/custom-search/docs/json_api_reference#automaticFiltering) for more information about Google&#39;s search results filters. Note that host crowding filtering applies only to multi-site searches. * By default, Google applies filtering to all search results to improve the quality of those results. Acceptable values are: * &#x60;0&#x60;: Turns off duplicate content filter. * &#x60;1&#x60;: Turns on duplicate content filter. | [optional] 
 **gl** | **String**| Geolocation of end user. * The &#x60;gl&#x60; parameter value is a two-letter country code. The &#x60;gl&#x60; parameter boosts search results whose country of origin matches the parameter value. See the [Country Codes](https://developers.google.com/custom-search/docs/json_api_reference#countryCodes) page for a list of valid values. * Specifying a &#x60;gl&#x60; parameter value should lead to more relevant results. This is particularly true for international customers and, even more specifically, for customers in English- speaking countries other than the United States. | [optional] 
 **googlehost** | **String**| **Deprecated**. Use the &#x60;gl&#x60; parameter for a similar effect. The local Google domain (for example, google.com, google.de, or google.fr) to use to perform the search. | [optional] 
 **highRange** | **String**| Specifies the ending value for a search range. * Use &#x60;lowRange&#x60; and &#x60;highRange&#x60; to append an inclusive search range of &#x60;lowRange...highRange&#x60; to the query. | [optional] 
 **hl** | **String**| Sets the user interface language. * Explicitly setting this parameter improves the performance and the quality of your search results. * See the [Interface Languages](https://developers.google.com/custom-search/docs/json_api_reference#wsInterfaceLanguages) section of [Internationalizing Queries and Results Presentation](https://developers.google.com/custom-search/docs/json_api_reference#wsInternationalizing) for more information, and [Supported Interface Languages](https://developers.google.com/custom-search/docs/json_api_reference#interfaceLanguages) for a list of supported languages. | [optional] 
 **hq** | **String**| Appends the specified query terms to the query, as if they were combined with a logical AND operator. | [optional] 
 **imgColorType** | **String**| Returns black and white, grayscale, transparent, or color images. Acceptable values are: * &#x60;\&quot;color\&quot;&#x60; * &#x60;\&quot;gray\&quot;&#x60; * &#x60;\&quot;mono\&quot;&#x60;: black and white * &#x60;\&quot;trans\&quot;&#x60;: transparent background | [optional] 
 **imgDominantColor** | **String**| Returns images of a specific dominant color. Acceptable values are: * &#x60;\&quot;black\&quot;&#x60; * &#x60;\&quot;blue\&quot;&#x60; * &#x60;\&quot;brown\&quot;&#x60; * &#x60;\&quot;gray\&quot;&#x60; * &#x60;\&quot;green\&quot;&#x60; * &#x60;\&quot;orange\&quot;&#x60; * &#x60;\&quot;pink\&quot;&#x60; * &#x60;\&quot;purple\&quot;&#x60; * &#x60;\&quot;red\&quot;&#x60; * &#x60;\&quot;teal\&quot;&#x60; * &#x60;\&quot;white\&quot;&#x60; * &#x60;\&quot;yellow\&quot;&#x60; | [optional] 
 **imgSize** | **String**| Returns images of a specified size. Acceptable values are: * &#x60;\&quot;huge\&quot;&#x60; * &#x60;\&quot;icon\&quot;&#x60; * &#x60;\&quot;large\&quot;&#x60; * &#x60;\&quot;medium\&quot;&#x60; * &#x60;\&quot;small\&quot;&#x60; * &#x60;\&quot;xlarge\&quot;&#x60; * &#x60;\&quot;xxlarge\&quot;&#x60; | [optional] 
 **imgType** | **String**| Returns images of a type. Acceptable values are: * &#x60;\&quot;clipart\&quot;&#x60; * &#x60;\&quot;face\&quot;&#x60; * &#x60;\&quot;lineart\&quot;&#x60; * &#x60;\&quot;stock\&quot;&#x60; * &#x60;\&quot;photo\&quot;&#x60; * &#x60;\&quot;animated\&quot;&#x60; | [optional] 
 **linkSite** | **String**| Specifies that all search results should contain a link to a particular URL. | [optional] 
 **lowRange** | **String**| Specifies the starting value for a search range. Use &#x60;lowRange&#x60; and &#x60;highRange&#x60; to append an inclusive search range of &#x60;lowRange...highRange&#x60; to the query. | [optional] 
 **lr** | **String**| Restricts the search to documents written in a particular language (e.g., &#x60;lr&#x3D;lang_ja&#x60;). Acceptable values are: * &#x60;\&quot;lang_ar\&quot;&#x60;: Arabic * &#x60;\&quot;lang_bg\&quot;&#x60;: Bulgarian * &#x60;\&quot;lang_ca\&quot;&#x60;: Catalan * &#x60;\&quot;lang_cs\&quot;&#x60;: Czech * &#x60;\&quot;lang_da\&quot;&#x60;: Danish * &#x60;\&quot;lang_de\&quot;&#x60;: German * &#x60;\&quot;lang_el\&quot;&#x60;: Greek * &#x60;\&quot;lang_en\&quot;&#x60;: English * &#x60;\&quot;lang_es\&quot;&#x60;: Spanish * &#x60;\&quot;lang_et\&quot;&#x60;: Estonian * &#x60;\&quot;lang_fi\&quot;&#x60;: Finnish * &#x60;\&quot;lang_fr\&quot;&#x60;: French * &#x60;\&quot;lang_hr\&quot;&#x60;: Croatian * &#x60;\&quot;lang_hu\&quot;&#x60;: Hungarian * &#x60;\&quot;lang_id\&quot;&#x60;: Indonesian * &#x60;\&quot;lang_is\&quot;&#x60;: Icelandic * &#x60;\&quot;lang_it\&quot;&#x60;: Italian * &#x60;\&quot;lang_iw\&quot;&#x60;: Hebrew * &#x60;\&quot;lang_ja\&quot;&#x60;: Japanese * &#x60;\&quot;lang_ko\&quot;&#x60;: Korean * &#x60;\&quot;lang_lt\&quot;&#x60;: Lithuanian * &#x60;\&quot;lang_lv\&quot;&#x60;: Latvian * &#x60;\&quot;lang_nl\&quot;&#x60;: Dutch * &#x60;\&quot;lang_no\&quot;&#x60;: Norwegian * &#x60;\&quot;lang_pl\&quot;&#x60;: Polish * &#x60;\&quot;lang_pt\&quot;&#x60;: Portuguese * &#x60;\&quot;lang_ro\&quot;&#x60;: Romanian * &#x60;\&quot;lang_ru\&quot;&#x60;: Russian * &#x60;\&quot;lang_sk\&quot;&#x60;: Slovak * &#x60;\&quot;lang_sl\&quot;&#x60;: Slovenian * &#x60;\&quot;lang_sr\&quot;&#x60;: Serbian * &#x60;\&quot;lang_sv\&quot;&#x60;: Swedish * &#x60;\&quot;lang_tr\&quot;&#x60;: Turkish * &#x60;\&quot;lang_zh-CN\&quot;&#x60;: Chinese (Simplified) * &#x60;\&quot;lang_zh-TW\&quot;&#x60;: Chinese (Traditional) | [optional] 
 **num** | **Number**| Number of search results to return. * Valid values are integers between 1 and 10, inclusive. | [optional] 
 **orTerms** | **String**| Provides additional search terms to check for in a document, where each document in the search results must contain at least one of the additional search terms. | [optional] 
 **q** | **String**| Query | [optional] 
 **relatedSite** | **String**| Deprecated. | [optional] 
 **rights** | **String**| Filters based on licensing. Supported values include: &#x60;cc_publicdomain&#x60;, &#x60;cc_attribute&#x60;, &#x60;cc_sharealike&#x60;, &#x60;cc_noncommercial&#x60;, &#x60;cc_nonderived&#x60; and combinations of these. See [typical combinations](https://wiki.creativecommons.org/wiki/CC_Search_integration). | [optional] 
 **safe** | **String**| Search safety level. Acceptable values are: * &#x60;\&quot;active\&quot;&#x60;: Enables SafeSearch filtering. * &#x60;\&quot;off\&quot;&#x60;: Disables SafeSearch filtering. (default) | [optional] 
 **searchType** | **String**| Specifies the search type: &#x60;image&#x60;. If unspecified, results are limited to webpages. Acceptable values are: * &#x60;\&quot;image\&quot;&#x60;: custom image search. | [optional] 
 **siteSearch** | **String**| Specifies a given site which should always be included or excluded from results (see &#x60;siteSearchFilter&#x60; parameter, below). | [optional] 
 **siteSearchFilter** | **String**| Controls whether to include or exclude results from the site named in the &#x60;siteSearch&#x60; parameter. Acceptable values are: * &#x60;\&quot;e\&quot;&#x60;: exclude * &#x60;\&quot;i\&quot;&#x60;: include | [optional] 
 **sort** | **String**| The sort expression to apply to the results. The sort parameter specifies that the results be sorted according to the specified expression i.e. sort by date. [Example: sort&#x3D;date](https://developers.google.com/custom-search/docs/structured_search#sort-by-attribute). | [optional] 
 **start** | **Number**| The index of the first result to return. The default number of results per page is 10, so &#x60;&amp;start&#x3D;11&#x60; would start at the top of the second page of results. **Note**: The JSON API will never return more than 100 results, even if more than 100 documents match the query, so setting the sum of &#x60;start + num&#x60; to a number greater than 100 will produce an error. Also note that the maximum value for &#x60;num&#x60; is 10. | [optional] 

### Return type

[**Search**](Search.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchCseSiterestrictList

> Search searchCseSiterestrictList(opts)



Returns metadata about the search performed, metadata about the engine used for the search, and the search results. Uses a small set of url patterns.

### Example

```javascript
import CustomSearchApi from 'custom_search_api';

let apiInstance = new CustomSearchApi.CseApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'c2coff': "c2coff_example", // String | Enables or disables [Simplified and Traditional Chinese Search](https://developers.google.com/custom-search/docs/json_api_reference#chineseSearch). The default value for this parameter is 0 (zero), meaning that the feature is enabled. Supported values are: * `1`: Disabled * `0`: Enabled (default)
  'cr': "cr_example", // String | Restricts search results to documents originating in a particular country. You may use [Boolean operators](https://developers.google.com/custom-search/docs/json_api_reference#booleanOperators) in the cr parameter's value. Google Search determines the country of a document by analyzing: * the top-level domain (TLD) of the document's URL * the geographic location of the Web server's IP address See the [Country Parameter Values](https://developers.google.com/custom-search/docs/json_api_reference#countryCollections) page for a list of valid values for this parameter.
  'cx': "cx_example", // String | The Programmable Search Engine ID to use for this request.
  'dateRestrict': "dateRestrict_example", // String | Restricts results to URLs based on date. Supported values include: * `d[number]`: requests results from the specified number of past days. * `w[number]`: requests results from the specified number of past weeks. * `m[number]`: requests results from the specified number of past months. * `y[number]`: requests results from the specified number of past years.
  'exactTerms': "exactTerms_example", // String | Identifies a phrase that all documents in the search results must contain.
  'excludeTerms': "excludeTerms_example", // String | Identifies a word or phrase that should not appear in any documents in the search results.
  'fileType': "fileType_example", // String | Restricts results to files of a specified extension. A list of file types indexable by Google can be found in Search Console [Help Center](https://support.google.com/webmasters/answer/35287).
  'filter': "filter_example", // String | Controls turning on or off the duplicate content filter. * See [Automatic Filtering](https://developers.google.com/custom-search/docs/json_api_reference#automaticFiltering) for more information about Google's search results filters. Note that host crowding filtering applies only to multi-site searches. * By default, Google applies filtering to all search results to improve the quality of those results. Acceptable values are: * `0`: Turns off duplicate content filter. * `1`: Turns on duplicate content filter.
  'gl': "gl_example", // String | Geolocation of end user. * The `gl` parameter value is a two-letter country code. The `gl` parameter boosts search results whose country of origin matches the parameter value. See the [Country Codes](https://developers.google.com/custom-search/docs/json_api_reference#countryCodes) page for a list of valid values. * Specifying a `gl` parameter value should lead to more relevant results. This is particularly true for international customers and, even more specifically, for customers in English- speaking countries other than the United States.
  'googlehost': "googlehost_example", // String | **Deprecated**. Use the `gl` parameter for a similar effect. The local Google domain (for example, google.com, google.de, or google.fr) to use to perform the search.
  'highRange': "highRange_example", // String | Specifies the ending value for a search range. * Use `lowRange` and `highRange` to append an inclusive search range of `lowRange...highRange` to the query.
  'hl': "hl_example", // String | Sets the user interface language. * Explicitly setting this parameter improves the performance and the quality of your search results. * See the [Interface Languages](https://developers.google.com/custom-search/docs/json_api_reference#wsInterfaceLanguages) section of [Internationalizing Queries and Results Presentation](https://developers.google.com/custom-search/docs/json_api_reference#wsInternationalizing) for more information, and [Supported Interface Languages](https://developers.google.com/custom-search/docs/json_api_reference#interfaceLanguages) for a list of supported languages.
  'hq': "hq_example", // String | Appends the specified query terms to the query, as if they were combined with a logical AND operator.
  'imgColorType': "imgColorType_example", // String | Returns black and white, grayscale, transparent, or color images. Acceptable values are: * `\"color\"` * `\"gray\"` * `\"mono\"`: black and white * `\"trans\"`: transparent background
  'imgDominantColor': "imgDominantColor_example", // String | Returns images of a specific dominant color. Acceptable values are: * `\"black\"` * `\"blue\"` * `\"brown\"` * `\"gray\"` * `\"green\"` * `\"orange\"` * `\"pink\"` * `\"purple\"` * `\"red\"` * `\"teal\"` * `\"white\"` * `\"yellow\"`
  'imgSize': "imgSize_example", // String | Returns images of a specified size. Acceptable values are: * `\"huge\"` * `\"icon\"` * `\"large\"` * `\"medium\"` * `\"small\"` * `\"xlarge\"` * `\"xxlarge\"`
  'imgType': "imgType_example", // String | Returns images of a type. Acceptable values are: * `\"clipart\"` * `\"face\"` * `\"lineart\"` * `\"stock\"` * `\"photo\"` * `\"animated\"`
  'linkSite': "linkSite_example", // String | Specifies that all search results should contain a link to a particular URL.
  'lowRange': "lowRange_example", // String | Specifies the starting value for a search range. Use `lowRange` and `highRange` to append an inclusive search range of `lowRange...highRange` to the query.
  'lr': "lr_example", // String | Restricts the search to documents written in a particular language (e.g., `lr=lang_ja`). Acceptable values are: * `\"lang_ar\"`: Arabic * `\"lang_bg\"`: Bulgarian * `\"lang_ca\"`: Catalan * `\"lang_cs\"`: Czech * `\"lang_da\"`: Danish * `\"lang_de\"`: German * `\"lang_el\"`: Greek * `\"lang_en\"`: English * `\"lang_es\"`: Spanish * `\"lang_et\"`: Estonian * `\"lang_fi\"`: Finnish * `\"lang_fr\"`: French * `\"lang_hr\"`: Croatian * `\"lang_hu\"`: Hungarian * `\"lang_id\"`: Indonesian * `\"lang_is\"`: Icelandic * `\"lang_it\"`: Italian * `\"lang_iw\"`: Hebrew * `\"lang_ja\"`: Japanese * `\"lang_ko\"`: Korean * `\"lang_lt\"`: Lithuanian * `\"lang_lv\"`: Latvian * `\"lang_nl\"`: Dutch * `\"lang_no\"`: Norwegian * `\"lang_pl\"`: Polish * `\"lang_pt\"`: Portuguese * `\"lang_ro\"`: Romanian * `\"lang_ru\"`: Russian * `\"lang_sk\"`: Slovak * `\"lang_sl\"`: Slovenian * `\"lang_sr\"`: Serbian * `\"lang_sv\"`: Swedish * `\"lang_tr\"`: Turkish * `\"lang_zh-CN\"`: Chinese (Simplified) * `\"lang_zh-TW\"`: Chinese (Traditional)
  'num': 56, // Number | Number of search results to return. * Valid values are integers between 1 and 10, inclusive.
  'orTerms': "orTerms_example", // String | Provides additional search terms to check for in a document, where each document in the search results must contain at least one of the additional search terms.
  'q': "q_example", // String | Query
  'relatedSite': "relatedSite_example", // String | Deprecated.
  'rights': "rights_example", // String | Filters based on licensing. Supported values include: `cc_publicdomain`, `cc_attribute`, `cc_sharealike`, `cc_noncommercial`, `cc_nonderived` and combinations of these. See [typical combinations](https://wiki.creativecommons.org/wiki/CC_Search_integration).
  'safe': "safe_example", // String | Search safety level. Acceptable values are: * `\"active\"`: Enables SafeSearch filtering. * `\"off\"`: Disables SafeSearch filtering. (default)
  'searchType': "searchType_example", // String | Specifies the search type: `image`. If unspecified, results are limited to webpages. Acceptable values are: * `\"image\"`: custom image search.
  'siteSearch': "siteSearch_example", // String | Specifies a given site which should always be included or excluded from results (see `siteSearchFilter` parameter, below).
  'siteSearchFilter': "siteSearchFilter_example", // String | Controls whether to include or exclude results from the site named in the `siteSearch` parameter. Acceptable values are: * `\"e\"`: exclude * `\"i\"`: include
  'sort': "sort_example", // String | The sort expression to apply to the results. The sort parameter specifies that the results be sorted according to the specified expression i.e. sort by date. [Example: sort=date](https://developers.google.com/custom-search/docs/structured_search#sort-by-attribute).
  'start': 56 // Number | The index of the first result to return. The default number of results per page is 10, so `&start=11` would start at the top of the second page of results. **Note**: The JSON API will never return more than 100 results, even if more than 100 documents match the query, so setting the sum of `start + num` to a number greater than 100 will produce an error. Also note that the maximum value for `num` is 10.
};
apiInstance.searchCseSiterestrictList(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **c2coff** | **String**| Enables or disables [Simplified and Traditional Chinese Search](https://developers.google.com/custom-search/docs/json_api_reference#chineseSearch). The default value for this parameter is 0 (zero), meaning that the feature is enabled. Supported values are: * &#x60;1&#x60;: Disabled * &#x60;0&#x60;: Enabled (default) | [optional] 
 **cr** | **String**| Restricts search results to documents originating in a particular country. You may use [Boolean operators](https://developers.google.com/custom-search/docs/json_api_reference#booleanOperators) in the cr parameter&#39;s value. Google Search determines the country of a document by analyzing: * the top-level domain (TLD) of the document&#39;s URL * the geographic location of the Web server&#39;s IP address See the [Country Parameter Values](https://developers.google.com/custom-search/docs/json_api_reference#countryCollections) page for a list of valid values for this parameter. | [optional] 
 **cx** | **String**| The Programmable Search Engine ID to use for this request. | [optional] 
 **dateRestrict** | **String**| Restricts results to URLs based on date. Supported values include: * &#x60;d[number]&#x60;: requests results from the specified number of past days. * &#x60;w[number]&#x60;: requests results from the specified number of past weeks. * &#x60;m[number]&#x60;: requests results from the specified number of past months. * &#x60;y[number]&#x60;: requests results from the specified number of past years. | [optional] 
 **exactTerms** | **String**| Identifies a phrase that all documents in the search results must contain. | [optional] 
 **excludeTerms** | **String**| Identifies a word or phrase that should not appear in any documents in the search results. | [optional] 
 **fileType** | **String**| Restricts results to files of a specified extension. A list of file types indexable by Google can be found in Search Console [Help Center](https://support.google.com/webmasters/answer/35287). | [optional] 
 **filter** | **String**| Controls turning on or off the duplicate content filter. * See [Automatic Filtering](https://developers.google.com/custom-search/docs/json_api_reference#automaticFiltering) for more information about Google&#39;s search results filters. Note that host crowding filtering applies only to multi-site searches. * By default, Google applies filtering to all search results to improve the quality of those results. Acceptable values are: * &#x60;0&#x60;: Turns off duplicate content filter. * &#x60;1&#x60;: Turns on duplicate content filter. | [optional] 
 **gl** | **String**| Geolocation of end user. * The &#x60;gl&#x60; parameter value is a two-letter country code. The &#x60;gl&#x60; parameter boosts search results whose country of origin matches the parameter value. See the [Country Codes](https://developers.google.com/custom-search/docs/json_api_reference#countryCodes) page for a list of valid values. * Specifying a &#x60;gl&#x60; parameter value should lead to more relevant results. This is particularly true for international customers and, even more specifically, for customers in English- speaking countries other than the United States. | [optional] 
 **googlehost** | **String**| **Deprecated**. Use the &#x60;gl&#x60; parameter for a similar effect. The local Google domain (for example, google.com, google.de, or google.fr) to use to perform the search. | [optional] 
 **highRange** | **String**| Specifies the ending value for a search range. * Use &#x60;lowRange&#x60; and &#x60;highRange&#x60; to append an inclusive search range of &#x60;lowRange...highRange&#x60; to the query. | [optional] 
 **hl** | **String**| Sets the user interface language. * Explicitly setting this parameter improves the performance and the quality of your search results. * See the [Interface Languages](https://developers.google.com/custom-search/docs/json_api_reference#wsInterfaceLanguages) section of [Internationalizing Queries and Results Presentation](https://developers.google.com/custom-search/docs/json_api_reference#wsInternationalizing) for more information, and [Supported Interface Languages](https://developers.google.com/custom-search/docs/json_api_reference#interfaceLanguages) for a list of supported languages. | [optional] 
 **hq** | **String**| Appends the specified query terms to the query, as if they were combined with a logical AND operator. | [optional] 
 **imgColorType** | **String**| Returns black and white, grayscale, transparent, or color images. Acceptable values are: * &#x60;\&quot;color\&quot;&#x60; * &#x60;\&quot;gray\&quot;&#x60; * &#x60;\&quot;mono\&quot;&#x60;: black and white * &#x60;\&quot;trans\&quot;&#x60;: transparent background | [optional] 
 **imgDominantColor** | **String**| Returns images of a specific dominant color. Acceptable values are: * &#x60;\&quot;black\&quot;&#x60; * &#x60;\&quot;blue\&quot;&#x60; * &#x60;\&quot;brown\&quot;&#x60; * &#x60;\&quot;gray\&quot;&#x60; * &#x60;\&quot;green\&quot;&#x60; * &#x60;\&quot;orange\&quot;&#x60; * &#x60;\&quot;pink\&quot;&#x60; * &#x60;\&quot;purple\&quot;&#x60; * &#x60;\&quot;red\&quot;&#x60; * &#x60;\&quot;teal\&quot;&#x60; * &#x60;\&quot;white\&quot;&#x60; * &#x60;\&quot;yellow\&quot;&#x60; | [optional] 
 **imgSize** | **String**| Returns images of a specified size. Acceptable values are: * &#x60;\&quot;huge\&quot;&#x60; * &#x60;\&quot;icon\&quot;&#x60; * &#x60;\&quot;large\&quot;&#x60; * &#x60;\&quot;medium\&quot;&#x60; * &#x60;\&quot;small\&quot;&#x60; * &#x60;\&quot;xlarge\&quot;&#x60; * &#x60;\&quot;xxlarge\&quot;&#x60; | [optional] 
 **imgType** | **String**| Returns images of a type. Acceptable values are: * &#x60;\&quot;clipart\&quot;&#x60; * &#x60;\&quot;face\&quot;&#x60; * &#x60;\&quot;lineart\&quot;&#x60; * &#x60;\&quot;stock\&quot;&#x60; * &#x60;\&quot;photo\&quot;&#x60; * &#x60;\&quot;animated\&quot;&#x60; | [optional] 
 **linkSite** | **String**| Specifies that all search results should contain a link to a particular URL. | [optional] 
 **lowRange** | **String**| Specifies the starting value for a search range. Use &#x60;lowRange&#x60; and &#x60;highRange&#x60; to append an inclusive search range of &#x60;lowRange...highRange&#x60; to the query. | [optional] 
 **lr** | **String**| Restricts the search to documents written in a particular language (e.g., &#x60;lr&#x3D;lang_ja&#x60;). Acceptable values are: * &#x60;\&quot;lang_ar\&quot;&#x60;: Arabic * &#x60;\&quot;lang_bg\&quot;&#x60;: Bulgarian * &#x60;\&quot;lang_ca\&quot;&#x60;: Catalan * &#x60;\&quot;lang_cs\&quot;&#x60;: Czech * &#x60;\&quot;lang_da\&quot;&#x60;: Danish * &#x60;\&quot;lang_de\&quot;&#x60;: German * &#x60;\&quot;lang_el\&quot;&#x60;: Greek * &#x60;\&quot;lang_en\&quot;&#x60;: English * &#x60;\&quot;lang_es\&quot;&#x60;: Spanish * &#x60;\&quot;lang_et\&quot;&#x60;: Estonian * &#x60;\&quot;lang_fi\&quot;&#x60;: Finnish * &#x60;\&quot;lang_fr\&quot;&#x60;: French * &#x60;\&quot;lang_hr\&quot;&#x60;: Croatian * &#x60;\&quot;lang_hu\&quot;&#x60;: Hungarian * &#x60;\&quot;lang_id\&quot;&#x60;: Indonesian * &#x60;\&quot;lang_is\&quot;&#x60;: Icelandic * &#x60;\&quot;lang_it\&quot;&#x60;: Italian * &#x60;\&quot;lang_iw\&quot;&#x60;: Hebrew * &#x60;\&quot;lang_ja\&quot;&#x60;: Japanese * &#x60;\&quot;lang_ko\&quot;&#x60;: Korean * &#x60;\&quot;lang_lt\&quot;&#x60;: Lithuanian * &#x60;\&quot;lang_lv\&quot;&#x60;: Latvian * &#x60;\&quot;lang_nl\&quot;&#x60;: Dutch * &#x60;\&quot;lang_no\&quot;&#x60;: Norwegian * &#x60;\&quot;lang_pl\&quot;&#x60;: Polish * &#x60;\&quot;lang_pt\&quot;&#x60;: Portuguese * &#x60;\&quot;lang_ro\&quot;&#x60;: Romanian * &#x60;\&quot;lang_ru\&quot;&#x60;: Russian * &#x60;\&quot;lang_sk\&quot;&#x60;: Slovak * &#x60;\&quot;lang_sl\&quot;&#x60;: Slovenian * &#x60;\&quot;lang_sr\&quot;&#x60;: Serbian * &#x60;\&quot;lang_sv\&quot;&#x60;: Swedish * &#x60;\&quot;lang_tr\&quot;&#x60;: Turkish * &#x60;\&quot;lang_zh-CN\&quot;&#x60;: Chinese (Simplified) * &#x60;\&quot;lang_zh-TW\&quot;&#x60;: Chinese (Traditional) | [optional] 
 **num** | **Number**| Number of search results to return. * Valid values are integers between 1 and 10, inclusive. | [optional] 
 **orTerms** | **String**| Provides additional search terms to check for in a document, where each document in the search results must contain at least one of the additional search terms. | [optional] 
 **q** | **String**| Query | [optional] 
 **relatedSite** | **String**| Deprecated. | [optional] 
 **rights** | **String**| Filters based on licensing. Supported values include: &#x60;cc_publicdomain&#x60;, &#x60;cc_attribute&#x60;, &#x60;cc_sharealike&#x60;, &#x60;cc_noncommercial&#x60;, &#x60;cc_nonderived&#x60; and combinations of these. See [typical combinations](https://wiki.creativecommons.org/wiki/CC_Search_integration). | [optional] 
 **safe** | **String**| Search safety level. Acceptable values are: * &#x60;\&quot;active\&quot;&#x60;: Enables SafeSearch filtering. * &#x60;\&quot;off\&quot;&#x60;: Disables SafeSearch filtering. (default) | [optional] 
 **searchType** | **String**| Specifies the search type: &#x60;image&#x60;. If unspecified, results are limited to webpages. Acceptable values are: * &#x60;\&quot;image\&quot;&#x60;: custom image search. | [optional] 
 **siteSearch** | **String**| Specifies a given site which should always be included or excluded from results (see &#x60;siteSearchFilter&#x60; parameter, below). | [optional] 
 **siteSearchFilter** | **String**| Controls whether to include or exclude results from the site named in the &#x60;siteSearch&#x60; parameter. Acceptable values are: * &#x60;\&quot;e\&quot;&#x60;: exclude * &#x60;\&quot;i\&quot;&#x60;: include | [optional] 
 **sort** | **String**| The sort expression to apply to the results. The sort parameter specifies that the results be sorted according to the specified expression i.e. sort by date. [Example: sort&#x3D;date](https://developers.google.com/custom-search/docs/structured_search#sort-by-attribute). | [optional] 
 **start** | **Number**| The index of the first result to return. The default number of results per page is 10, so &#x60;&amp;start&#x3D;11&#x60; would start at the top of the second page of results. **Note**: The JSON API will never return more than 100 results, even if more than 100 documents match the query, so setting the sum of &#x60;start + num&#x60; to a number greater than 100 will produce an error. Also note that the maximum value for &#x60;num&#x60; is 10. | [optional] 

### Return type

[**Search**](Search.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

