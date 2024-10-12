from typing import List, Dict
from aiohttp import web

from openapi_server.models.search import Search
from openapi_server import util


async def search_cse_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, c2coff=None, cr=None, cx=None, date_restrict=None, exact_terms=None, exclude_terms=None, file_type=None, filter=None, gl=None, googlehost=None, high_range=None, hl=None, hq=None, img_color_type=None, img_dominant_color=None, img_size=None, img_type=None, link_site=None, low_range=None, lr=None, num=None, or_terms=None, q=None, related_site=None, rights=None, safe=None, search_type=None, site_search=None, site_search_filter=None, sort=None, start=None) -> web.Response:
    """search_cse_list

    Returns metadata about the search performed, metadata about the engine used for the search, and the search results.

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param c2coff: Enables or disables [Simplified and Traditional Chinese Search](https://developers.google.com/custom-search/docs/json_api_reference#chineseSearch). The default value for this parameter is 0 (zero), meaning that the feature is enabled. Supported values are: * &#x60;1&#x60;: Disabled * &#x60;0&#x60;: Enabled (default)
    :type c2coff: str
    :param cr: Restricts search results to documents originating in a particular country. You may use [Boolean operators](https://developers.google.com/custom-search/docs/json_api_reference#booleanOperators) in the cr parameter&#39;s value. Google Search determines the country of a document by analyzing: * the top-level domain (TLD) of the document&#39;s URL * the geographic location of the Web server&#39;s IP address See the [Country Parameter Values](https://developers.google.com/custom-search/docs/json_api_reference#countryCollections) page for a list of valid values for this parameter.
    :type cr: str
    :param cx: The Programmable Search Engine ID to use for this request.
    :type cx: str
    :param date_restrict: Restricts results to URLs based on date. Supported values include: * &#x60;d[number]&#x60;: requests results from the specified number of past days. * &#x60;w[number]&#x60;: requests results from the specified number of past weeks. * &#x60;m[number]&#x60;: requests results from the specified number of past months. * &#x60;y[number]&#x60;: requests results from the specified number of past years.
    :type date_restrict: str
    :param exact_terms: Identifies a phrase that all documents in the search results must contain.
    :type exact_terms: str
    :param exclude_terms: Identifies a word or phrase that should not appear in any documents in the search results.
    :type exclude_terms: str
    :param file_type: Restricts results to files of a specified extension. A list of file types indexable by Google can be found in Search Console [Help Center](https://support.google.com/webmasters/answer/35287).
    :type file_type: str
    :param filter: Controls turning on or off the duplicate content filter. * See [Automatic Filtering](https://developers.google.com/custom-search/docs/json_api_reference#automaticFiltering) for more information about Google&#39;s search results filters. Note that host crowding filtering applies only to multi-site searches. * By default, Google applies filtering to all search results to improve the quality of those results. Acceptable values are: * &#x60;0&#x60;: Turns off duplicate content filter. * &#x60;1&#x60;: Turns on duplicate content filter.
    :type filter: str
    :param gl: Geolocation of end user. * The &#x60;gl&#x60; parameter value is a two-letter country code. The &#x60;gl&#x60; parameter boosts search results whose country of origin matches the parameter value. See the [Country Codes](https://developers.google.com/custom-search/docs/json_api_reference#countryCodes) page for a list of valid values. * Specifying a &#x60;gl&#x60; parameter value should lead to more relevant results. This is particularly true for international customers and, even more specifically, for customers in English- speaking countries other than the United States.
    :type gl: str
    :param googlehost: **Deprecated**. Use the &#x60;gl&#x60; parameter for a similar effect. The local Google domain (for example, google.com, google.de, or google.fr) to use to perform the search.
    :type googlehost: str
    :param high_range: Specifies the ending value for a search range. * Use &#x60;lowRange&#x60; and &#x60;highRange&#x60; to append an inclusive search range of &#x60;lowRange...highRange&#x60; to the query.
    :type high_range: str
    :param hl: Sets the user interface language. * Explicitly setting this parameter improves the performance and the quality of your search results. * See the [Interface Languages](https://developers.google.com/custom-search/docs/json_api_reference#wsInterfaceLanguages) section of [Internationalizing Queries and Results Presentation](https://developers.google.com/custom-search/docs/json_api_reference#wsInternationalizing) for more information, and [Supported Interface Languages](https://developers.google.com/custom-search/docs/json_api_reference#interfaceLanguages) for a list of supported languages.
    :type hl: str
    :param hq: Appends the specified query terms to the query, as if they were combined with a logical AND operator.
    :type hq: str
    :param img_color_type: Returns black and white, grayscale, transparent, or color images. Acceptable values are: * &#x60;\&quot;color\&quot;&#x60; * &#x60;\&quot;gray\&quot;&#x60; * &#x60;\&quot;mono\&quot;&#x60;: black and white * &#x60;\&quot;trans\&quot;&#x60;: transparent background
    :type img_color_type: str
    :param img_dominant_color: Returns images of a specific dominant color. Acceptable values are: * &#x60;\&quot;black\&quot;&#x60; * &#x60;\&quot;blue\&quot;&#x60; * &#x60;\&quot;brown\&quot;&#x60; * &#x60;\&quot;gray\&quot;&#x60; * &#x60;\&quot;green\&quot;&#x60; * &#x60;\&quot;orange\&quot;&#x60; * &#x60;\&quot;pink\&quot;&#x60; * &#x60;\&quot;purple\&quot;&#x60; * &#x60;\&quot;red\&quot;&#x60; * &#x60;\&quot;teal\&quot;&#x60; * &#x60;\&quot;white\&quot;&#x60; * &#x60;\&quot;yellow\&quot;&#x60;
    :type img_dominant_color: str
    :param img_size: Returns images of a specified size. Acceptable values are: * &#x60;\&quot;huge\&quot;&#x60; * &#x60;\&quot;icon\&quot;&#x60; * &#x60;\&quot;large\&quot;&#x60; * &#x60;\&quot;medium\&quot;&#x60; * &#x60;\&quot;small\&quot;&#x60; * &#x60;\&quot;xlarge\&quot;&#x60; * &#x60;\&quot;xxlarge\&quot;&#x60;
    :type img_size: str
    :param img_type: Returns images of a type. Acceptable values are: * &#x60;\&quot;clipart\&quot;&#x60; * &#x60;\&quot;face\&quot;&#x60; * &#x60;\&quot;lineart\&quot;&#x60; * &#x60;\&quot;stock\&quot;&#x60; * &#x60;\&quot;photo\&quot;&#x60; * &#x60;\&quot;animated\&quot;&#x60;
    :type img_type: str
    :param link_site: Specifies that all search results should contain a link to a particular URL.
    :type link_site: str
    :param low_range: Specifies the starting value for a search range. Use &#x60;lowRange&#x60; and &#x60;highRange&#x60; to append an inclusive search range of &#x60;lowRange...highRange&#x60; to the query.
    :type low_range: str
    :param lr: Restricts the search to documents written in a particular language (e.g., &#x60;lr&#x3D;lang_ja&#x60;). Acceptable values are: * &#x60;\&quot;lang_ar\&quot;&#x60;: Arabic * &#x60;\&quot;lang_bg\&quot;&#x60;: Bulgarian * &#x60;\&quot;lang_ca\&quot;&#x60;: Catalan * &#x60;\&quot;lang_cs\&quot;&#x60;: Czech * &#x60;\&quot;lang_da\&quot;&#x60;: Danish * &#x60;\&quot;lang_de\&quot;&#x60;: German * &#x60;\&quot;lang_el\&quot;&#x60;: Greek * &#x60;\&quot;lang_en\&quot;&#x60;: English * &#x60;\&quot;lang_es\&quot;&#x60;: Spanish * &#x60;\&quot;lang_et\&quot;&#x60;: Estonian * &#x60;\&quot;lang_fi\&quot;&#x60;: Finnish * &#x60;\&quot;lang_fr\&quot;&#x60;: French * &#x60;\&quot;lang_hr\&quot;&#x60;: Croatian * &#x60;\&quot;lang_hu\&quot;&#x60;: Hungarian * &#x60;\&quot;lang_id\&quot;&#x60;: Indonesian * &#x60;\&quot;lang_is\&quot;&#x60;: Icelandic * &#x60;\&quot;lang_it\&quot;&#x60;: Italian * &#x60;\&quot;lang_iw\&quot;&#x60;: Hebrew * &#x60;\&quot;lang_ja\&quot;&#x60;: Japanese * &#x60;\&quot;lang_ko\&quot;&#x60;: Korean * &#x60;\&quot;lang_lt\&quot;&#x60;: Lithuanian * &#x60;\&quot;lang_lv\&quot;&#x60;: Latvian * &#x60;\&quot;lang_nl\&quot;&#x60;: Dutch * &#x60;\&quot;lang_no\&quot;&#x60;: Norwegian * &#x60;\&quot;lang_pl\&quot;&#x60;: Polish * &#x60;\&quot;lang_pt\&quot;&#x60;: Portuguese * &#x60;\&quot;lang_ro\&quot;&#x60;: Romanian * &#x60;\&quot;lang_ru\&quot;&#x60;: Russian * &#x60;\&quot;lang_sk\&quot;&#x60;: Slovak * &#x60;\&quot;lang_sl\&quot;&#x60;: Slovenian * &#x60;\&quot;lang_sr\&quot;&#x60;: Serbian * &#x60;\&quot;lang_sv\&quot;&#x60;: Swedish * &#x60;\&quot;lang_tr\&quot;&#x60;: Turkish * &#x60;\&quot;lang_zh-CN\&quot;&#x60;: Chinese (Simplified) * &#x60;\&quot;lang_zh-TW\&quot;&#x60;: Chinese (Traditional)
    :type lr: str
    :param num: Number of search results to return. * Valid values are integers between 1 and 10, inclusive.
    :type num: int
    :param or_terms: Provides additional search terms to check for in a document, where each document in the search results must contain at least one of the additional search terms.
    :type or_terms: str
    :param q: Query
    :type q: str
    :param related_site: Deprecated.
    :type related_site: str
    :param rights: Filters based on licensing. Supported values include: &#x60;cc_publicdomain&#x60;, &#x60;cc_attribute&#x60;, &#x60;cc_sharealike&#x60;, &#x60;cc_noncommercial&#x60;, &#x60;cc_nonderived&#x60; and combinations of these. See [typical combinations](https://wiki.creativecommons.org/wiki/CC_Search_integration).
    :type rights: str
    :param safe: Search safety level. Acceptable values are: * &#x60;\&quot;active\&quot;&#x60;: Enables SafeSearch filtering. * &#x60;\&quot;off\&quot;&#x60;: Disables SafeSearch filtering. (default)
    :type safe: str
    :param search_type: Specifies the search type: &#x60;image&#x60;. If unspecified, results are limited to webpages. Acceptable values are: * &#x60;\&quot;image\&quot;&#x60;: custom image search.
    :type search_type: str
    :param site_search: Specifies a given site which should always be included or excluded from results (see &#x60;siteSearchFilter&#x60; parameter, below).
    :type site_search: str
    :param site_search_filter: Controls whether to include or exclude results from the site named in the &#x60;siteSearch&#x60; parameter. Acceptable values are: * &#x60;\&quot;e\&quot;&#x60;: exclude * &#x60;\&quot;i\&quot;&#x60;: include
    :type site_search_filter: str
    :param sort: The sort expression to apply to the results. The sort parameter specifies that the results be sorted according to the specified expression i.e. sort by date. [Example: sort&#x3D;date](https://developers.google.com/custom-search/docs/structured_search#sort-by-attribute).
    :type sort: str
    :param start: The index of the first result to return. The default number of results per page is 10, so &#x60;&amp;start&#x3D;11&#x60; would start at the top of the second page of results. **Note**: The JSON API will never return more than 100 results, even if more than 100 documents match the query, so setting the sum of &#x60;start + num&#x60; to a number greater than 100 will produce an error. Also note that the maximum value for &#x60;num&#x60; is 10.
    :type start: int

    """
    return web.Response(status=200)


async def search_cse_siterestrict_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, c2coff=None, cr=None, cx=None, date_restrict=None, exact_terms=None, exclude_terms=None, file_type=None, filter=None, gl=None, googlehost=None, high_range=None, hl=None, hq=None, img_color_type=None, img_dominant_color=None, img_size=None, img_type=None, link_site=None, low_range=None, lr=None, num=None, or_terms=None, q=None, related_site=None, rights=None, safe=None, search_type=None, site_search=None, site_search_filter=None, sort=None, start=None) -> web.Response:
    """search_cse_siterestrict_list

    Returns metadata about the search performed, metadata about the engine used for the search, and the search results. Uses a small set of url patterns.

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param c2coff: Enables or disables [Simplified and Traditional Chinese Search](https://developers.google.com/custom-search/docs/json_api_reference#chineseSearch). The default value for this parameter is 0 (zero), meaning that the feature is enabled. Supported values are: * &#x60;1&#x60;: Disabled * &#x60;0&#x60;: Enabled (default)
    :type c2coff: str
    :param cr: Restricts search results to documents originating in a particular country. You may use [Boolean operators](https://developers.google.com/custom-search/docs/json_api_reference#booleanOperators) in the cr parameter&#39;s value. Google Search determines the country of a document by analyzing: * the top-level domain (TLD) of the document&#39;s URL * the geographic location of the Web server&#39;s IP address See the [Country Parameter Values](https://developers.google.com/custom-search/docs/json_api_reference#countryCollections) page for a list of valid values for this parameter.
    :type cr: str
    :param cx: The Programmable Search Engine ID to use for this request.
    :type cx: str
    :param date_restrict: Restricts results to URLs based on date. Supported values include: * &#x60;d[number]&#x60;: requests results from the specified number of past days. * &#x60;w[number]&#x60;: requests results from the specified number of past weeks. * &#x60;m[number]&#x60;: requests results from the specified number of past months. * &#x60;y[number]&#x60;: requests results from the specified number of past years.
    :type date_restrict: str
    :param exact_terms: Identifies a phrase that all documents in the search results must contain.
    :type exact_terms: str
    :param exclude_terms: Identifies a word or phrase that should not appear in any documents in the search results.
    :type exclude_terms: str
    :param file_type: Restricts results to files of a specified extension. A list of file types indexable by Google can be found in Search Console [Help Center](https://support.google.com/webmasters/answer/35287).
    :type file_type: str
    :param filter: Controls turning on or off the duplicate content filter. * See [Automatic Filtering](https://developers.google.com/custom-search/docs/json_api_reference#automaticFiltering) for more information about Google&#39;s search results filters. Note that host crowding filtering applies only to multi-site searches. * By default, Google applies filtering to all search results to improve the quality of those results. Acceptable values are: * &#x60;0&#x60;: Turns off duplicate content filter. * &#x60;1&#x60;: Turns on duplicate content filter.
    :type filter: str
    :param gl: Geolocation of end user. * The &#x60;gl&#x60; parameter value is a two-letter country code. The &#x60;gl&#x60; parameter boosts search results whose country of origin matches the parameter value. See the [Country Codes](https://developers.google.com/custom-search/docs/json_api_reference#countryCodes) page for a list of valid values. * Specifying a &#x60;gl&#x60; parameter value should lead to more relevant results. This is particularly true for international customers and, even more specifically, for customers in English- speaking countries other than the United States.
    :type gl: str
    :param googlehost: **Deprecated**. Use the &#x60;gl&#x60; parameter for a similar effect. The local Google domain (for example, google.com, google.de, or google.fr) to use to perform the search.
    :type googlehost: str
    :param high_range: Specifies the ending value for a search range. * Use &#x60;lowRange&#x60; and &#x60;highRange&#x60; to append an inclusive search range of &#x60;lowRange...highRange&#x60; to the query.
    :type high_range: str
    :param hl: Sets the user interface language. * Explicitly setting this parameter improves the performance and the quality of your search results. * See the [Interface Languages](https://developers.google.com/custom-search/docs/json_api_reference#wsInterfaceLanguages) section of [Internationalizing Queries and Results Presentation](https://developers.google.com/custom-search/docs/json_api_reference#wsInternationalizing) for more information, and [Supported Interface Languages](https://developers.google.com/custom-search/docs/json_api_reference#interfaceLanguages) for a list of supported languages.
    :type hl: str
    :param hq: Appends the specified query terms to the query, as if they were combined with a logical AND operator.
    :type hq: str
    :param img_color_type: Returns black and white, grayscale, transparent, or color images. Acceptable values are: * &#x60;\&quot;color\&quot;&#x60; * &#x60;\&quot;gray\&quot;&#x60; * &#x60;\&quot;mono\&quot;&#x60;: black and white * &#x60;\&quot;trans\&quot;&#x60;: transparent background
    :type img_color_type: str
    :param img_dominant_color: Returns images of a specific dominant color. Acceptable values are: * &#x60;\&quot;black\&quot;&#x60; * &#x60;\&quot;blue\&quot;&#x60; * &#x60;\&quot;brown\&quot;&#x60; * &#x60;\&quot;gray\&quot;&#x60; * &#x60;\&quot;green\&quot;&#x60; * &#x60;\&quot;orange\&quot;&#x60; * &#x60;\&quot;pink\&quot;&#x60; * &#x60;\&quot;purple\&quot;&#x60; * &#x60;\&quot;red\&quot;&#x60; * &#x60;\&quot;teal\&quot;&#x60; * &#x60;\&quot;white\&quot;&#x60; * &#x60;\&quot;yellow\&quot;&#x60;
    :type img_dominant_color: str
    :param img_size: Returns images of a specified size. Acceptable values are: * &#x60;\&quot;huge\&quot;&#x60; * &#x60;\&quot;icon\&quot;&#x60; * &#x60;\&quot;large\&quot;&#x60; * &#x60;\&quot;medium\&quot;&#x60; * &#x60;\&quot;small\&quot;&#x60; * &#x60;\&quot;xlarge\&quot;&#x60; * &#x60;\&quot;xxlarge\&quot;&#x60;
    :type img_size: str
    :param img_type: Returns images of a type. Acceptable values are: * &#x60;\&quot;clipart\&quot;&#x60; * &#x60;\&quot;face\&quot;&#x60; * &#x60;\&quot;lineart\&quot;&#x60; * &#x60;\&quot;stock\&quot;&#x60; * &#x60;\&quot;photo\&quot;&#x60; * &#x60;\&quot;animated\&quot;&#x60;
    :type img_type: str
    :param link_site: Specifies that all search results should contain a link to a particular URL.
    :type link_site: str
    :param low_range: Specifies the starting value for a search range. Use &#x60;lowRange&#x60; and &#x60;highRange&#x60; to append an inclusive search range of &#x60;lowRange...highRange&#x60; to the query.
    :type low_range: str
    :param lr: Restricts the search to documents written in a particular language (e.g., &#x60;lr&#x3D;lang_ja&#x60;). Acceptable values are: * &#x60;\&quot;lang_ar\&quot;&#x60;: Arabic * &#x60;\&quot;lang_bg\&quot;&#x60;: Bulgarian * &#x60;\&quot;lang_ca\&quot;&#x60;: Catalan * &#x60;\&quot;lang_cs\&quot;&#x60;: Czech * &#x60;\&quot;lang_da\&quot;&#x60;: Danish * &#x60;\&quot;lang_de\&quot;&#x60;: German * &#x60;\&quot;lang_el\&quot;&#x60;: Greek * &#x60;\&quot;lang_en\&quot;&#x60;: English * &#x60;\&quot;lang_es\&quot;&#x60;: Spanish * &#x60;\&quot;lang_et\&quot;&#x60;: Estonian * &#x60;\&quot;lang_fi\&quot;&#x60;: Finnish * &#x60;\&quot;lang_fr\&quot;&#x60;: French * &#x60;\&quot;lang_hr\&quot;&#x60;: Croatian * &#x60;\&quot;lang_hu\&quot;&#x60;: Hungarian * &#x60;\&quot;lang_id\&quot;&#x60;: Indonesian * &#x60;\&quot;lang_is\&quot;&#x60;: Icelandic * &#x60;\&quot;lang_it\&quot;&#x60;: Italian * &#x60;\&quot;lang_iw\&quot;&#x60;: Hebrew * &#x60;\&quot;lang_ja\&quot;&#x60;: Japanese * &#x60;\&quot;lang_ko\&quot;&#x60;: Korean * &#x60;\&quot;lang_lt\&quot;&#x60;: Lithuanian * &#x60;\&quot;lang_lv\&quot;&#x60;: Latvian * &#x60;\&quot;lang_nl\&quot;&#x60;: Dutch * &#x60;\&quot;lang_no\&quot;&#x60;: Norwegian * &#x60;\&quot;lang_pl\&quot;&#x60;: Polish * &#x60;\&quot;lang_pt\&quot;&#x60;: Portuguese * &#x60;\&quot;lang_ro\&quot;&#x60;: Romanian * &#x60;\&quot;lang_ru\&quot;&#x60;: Russian * &#x60;\&quot;lang_sk\&quot;&#x60;: Slovak * &#x60;\&quot;lang_sl\&quot;&#x60;: Slovenian * &#x60;\&quot;lang_sr\&quot;&#x60;: Serbian * &#x60;\&quot;lang_sv\&quot;&#x60;: Swedish * &#x60;\&quot;lang_tr\&quot;&#x60;: Turkish * &#x60;\&quot;lang_zh-CN\&quot;&#x60;: Chinese (Simplified) * &#x60;\&quot;lang_zh-TW\&quot;&#x60;: Chinese (Traditional)
    :type lr: str
    :param num: Number of search results to return. * Valid values are integers between 1 and 10, inclusive.
    :type num: int
    :param or_terms: Provides additional search terms to check for in a document, where each document in the search results must contain at least one of the additional search terms.
    :type or_terms: str
    :param q: Query
    :type q: str
    :param related_site: Deprecated.
    :type related_site: str
    :param rights: Filters based on licensing. Supported values include: &#x60;cc_publicdomain&#x60;, &#x60;cc_attribute&#x60;, &#x60;cc_sharealike&#x60;, &#x60;cc_noncommercial&#x60;, &#x60;cc_nonderived&#x60; and combinations of these. See [typical combinations](https://wiki.creativecommons.org/wiki/CC_Search_integration).
    :type rights: str
    :param safe: Search safety level. Acceptable values are: * &#x60;\&quot;active\&quot;&#x60;: Enables SafeSearch filtering. * &#x60;\&quot;off\&quot;&#x60;: Disables SafeSearch filtering. (default)
    :type safe: str
    :param search_type: Specifies the search type: &#x60;image&#x60;. If unspecified, results are limited to webpages. Acceptable values are: * &#x60;\&quot;image\&quot;&#x60;: custom image search.
    :type search_type: str
    :param site_search: Specifies a given site which should always be included or excluded from results (see &#x60;siteSearchFilter&#x60; parameter, below).
    :type site_search: str
    :param site_search_filter: Controls whether to include or exclude results from the site named in the &#x60;siteSearch&#x60; parameter. Acceptable values are: * &#x60;\&quot;e\&quot;&#x60;: exclude * &#x60;\&quot;i\&quot;&#x60;: include
    :type site_search_filter: str
    :param sort: The sort expression to apply to the results. The sort parameter specifies that the results be sorted according to the specified expression i.e. sort by date. [Example: sort&#x3D;date](https://developers.google.com/custom-search/docs/structured_search#sort-by-attribute).
    :type sort: str
    :param start: The index of the first result to return. The default number of results per page is 10, so &#x60;&amp;start&#x3D;11&#x60; would start at the top of the second page of results. **Note**: The JSON API will never return more than 100 results, even if more than 100 documents match the query, so setting the sum of &#x60;start + num&#x60; to a number greater than 100 will produce an error. Also note that the maximum value for &#x60;num&#x60; is 10.
    :type start: int

    """
    return web.Response(status=200)
