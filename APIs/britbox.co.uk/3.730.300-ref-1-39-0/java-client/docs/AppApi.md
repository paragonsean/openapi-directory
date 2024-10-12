# AppApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAppConfig**](AppApi.md#getAppConfig) | **GET** /config |  |
| [**getItvPage**](AppApi.md#getItvPage) | **GET** /itv/page |  |
| [**getPage**](AppApi.md#getPage) | **GET** /page |  |


<a id="getAppConfig"></a>
# **getAppConfig**
> AppConfig getAppConfig(include, system, device, sub, segments, ff, lang)



Get the global configuration for an application. Should be called during app statup.  This includes things like device and playback rules, classifications, sitemap and subscriptions.  You have the option to select specific configuration objects using the &#39;include&#39; parameter, or if unspecified, getting all configuration. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    AppApi apiInstance = new AppApi(defaultClient);
    List<String> include = Arrays.asList(); // List<String> | A comma delimited list of config objects to return. If none specified then all configuration is returned. 
    String system = "system_example"; // String | Classification system to load in case include = classification. 
    String device = "web_browser"; // String | The type of device the content is targeting.
    String sub = "sub_example"; // String | The active subscription code.
    List<String> segments = Arrays.asList(); // List<String> | The list of segments to filter the response by.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      AppConfig result = apiInstance.getAppConfig(include, system, device, sub, segments, ff, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppApi#getAppConfig");
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
| **include** | [**List&lt;String&gt;**](String.md)| A comma delimited list of config objects to return. If none specified then all configuration is returned.  | [optional] [enum: classification, playback, sitemap, navigation, subscription, general, display, i18n, linear] |
| **system** | **String**| Classification system to load in case include &#x3D; classification.  | [optional] |
| **device** | **String**| The type of device the content is targeting. | [optional] [default to web_browser] |
| **sub** | **String**| The active subscription code. | [optional] |
| **segments** | [**List&lt;String&gt;**](String.md)| The list of segments to filter the response by. | [optional] |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**AppConfig**](AppConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of available pages |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getItvPage"></a>
# **getItvPage**
> Page getItvPage(path, listPageSize, listPageSizeLarge, maxListPrefetch, itemDetailExpand, itemDetailSelectSeason, textEntryFormat, maxRating, device, sub, segments, ff, lang)



Returns a page with the specified id.  This is a cut down version for low memory devices.123  If targeting the search page you must url encode the search term as a parameter using the &#x60;q&#x60; key. For example if your browser path looks like &#x60;/search?q&#x3D;the&#x60; then what you pass to this endpoint would look like &#x60;/itv/page?path&#x3D;/search%3Fq%3Dthe&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    AppApi apiInstance = new AppApi(defaultClient);
    String path = "path_example"; // String | The path of the page to load, e.g. '/movies'.
    Integer listPageSize = 12; // Integer | The number of items to load when prefetching and paging each list in the page row.
    Integer listPageSizeLarge = 50; // Integer | The number of items to load when prefetching a continuous scroll list entry in a page.  By default any list page entry with template pattern `/^CS\\d+$/` will be considered a continuous scroll list. 
    Integer maxListPrefetch = 2; // Integer | The maximum number of lists to prefetch in the page.
    String itemDetailExpand = "all"; // String | Only relevant when loading item detail pages as these embed a detailed item in the main page entry.  If no value is specified no item dependencies are expanded.  If 'children' is specified then the list of any direct children will be expanded. For example seasons of a show or episodes of a season.  If 'all' is specified then the parent chain will be expanded along with any child list at each level. For example if an episode is specified then its season will be expanded and that season's episode list. The season will have its show expanded and the show will have its season list expanded.  The 'all' options is useful when you deep link into a show/season/episode for the first time as it provides full context for navigating around the show page. Subsequent navigation around children of the show should only need to request expand of children.  If 'ancestors' is specified then only the parent chain is included  If an expand is specified which is not relevant to the item type, it will be ignored. 
    String itemDetailSelectSeason = "first"; // String | Only relevant when loading show detail pages as these embed a detailed item in the main page entry.  Since the introduction of the D1,2,3 templates this parameter is now somewhat redundant, or less likely to have any effect. While it may still be useful in some cases, most of the time the season selection will be dictated by the configuration of the rows scheduled on the show detail page. This parameter will only take effect if there are rows used to schedule episodes of a season, like D1,2,3, or if no rows have a value set for their `seasonOrder` custom field.  Given a targeted show page, it can be useful to get the details of a child season. This option provides a means to return the `first` or `latest` season of a show embedded in the page.  The `expand` parameter also works here so for example you could land on a show page and request the `item_detail_select_season=latest` along with `item_detail_expand=all`. This would then return the detail of the latest season with its list of child episode summaries, and also expand the detail of the show with its list of seasons summaries. 
    String textEntryFormat = "markdown"; // String | Only relevant to page entries of type `TextEntry`.  Converts the value of a text page entry to the specified format. 
    String maxRating = "maxRating_example"; // String | The maximum rating (inclusive) of items returned, e.g. 'auoflc-pg'.
    String device = "web_browser"; // String | The type of device the content is targeting.
    String sub = "sub_example"; // String | The active subscription code.
    List<String> segments = Arrays.asList(); // List<String> | The list of segments to filter the response by.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      Page result = apiInstance.getItvPage(path, listPageSize, listPageSizeLarge, maxListPrefetch, itemDetailExpand, itemDetailSelectSeason, textEntryFormat, maxRating, device, sub, segments, ff, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppApi#getItvPage");
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
| **path** | **String**| The path of the page to load, e.g. &#39;/movies&#39;. | |
| **listPageSize** | **Integer**| The number of items to load when prefetching and paging each list in the page row. | [optional] [default to 12] |
| **listPageSizeLarge** | **Integer**| The number of items to load when prefetching a continuous scroll list entry in a page.  By default any list page entry with template pattern &#x60;/^CS\\d+$/&#x60; will be considered a continuous scroll list.  | [optional] [default to 50] |
| **maxListPrefetch** | **Integer**| The maximum number of lists to prefetch in the page. | [optional] [default to 2] |
| **itemDetailExpand** | **String**| Only relevant when loading item detail pages as these embed a detailed item in the main page entry.  If no value is specified no item dependencies are expanded.  If &#39;children&#39; is specified then the list of any direct children will be expanded. For example seasons of a show or episodes of a season.  If &#39;all&#39; is specified then the parent chain will be expanded along with any child list at each level. For example if an episode is specified then its season will be expanded and that season&#39;s episode list. The season will have its show expanded and the show will have its season list expanded.  The &#39;all&#39; options is useful when you deep link into a show/season/episode for the first time as it provides full context for navigating around the show page. Subsequent navigation around children of the show should only need to request expand of children.  If &#39;ancestors&#39; is specified then only the parent chain is included  If an expand is specified which is not relevant to the item type, it will be ignored.  | [optional] [enum: all, children, ancestors] |
| **itemDetailSelectSeason** | **String**| Only relevant when loading show detail pages as these embed a detailed item in the main page entry.  Since the introduction of the D1,2,3 templates this parameter is now somewhat redundant, or less likely to have any effect. While it may still be useful in some cases, most of the time the season selection will be dictated by the configuration of the rows scheduled on the show detail page. This parameter will only take effect if there are rows used to schedule episodes of a season, like D1,2,3, or if no rows have a value set for their &#x60;seasonOrder&#x60; custom field.  Given a targeted show page, it can be useful to get the details of a child season. This option provides a means to return the &#x60;first&#x60; or &#x60;latest&#x60; season of a show embedded in the page.  The &#x60;expand&#x60; parameter also works here so for example you could land on a show page and request the &#x60;item_detail_select_season&#x3D;latest&#x60; along with &#x60;item_detail_expand&#x3D;all&#x60;. This would then return the detail of the latest season with its list of child episode summaries, and also expand the detail of the show with its list of seasons summaries.  | [optional] [enum: first, latest] |
| **textEntryFormat** | **String**| Only relevant to page entries of type &#x60;TextEntry&#x60;.  Converts the value of a text page entry to the specified format.  | [optional] [default to markdown] [enum: markdown, html] |
| **maxRating** | **String**| The maximum rating (inclusive) of items returned, e.g. &#39;auoflc-pg&#39;. | [optional] |
| **device** | **String**| The type of device the content is targeting. | [optional] [default to web_browser] |
| **sub** | **String**| The active subscription code. | [optional] |
| **segments** | [**List&lt;String&gt;**](String.md)| The list of segments to filter the response by. | [optional] |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The page requested. |  -  |
| **301** | Returned if feature flag &#x60;cd&#x60; is set and item detail is requested of an item that has Custom Destination set to an External URL. The &#x60;Location&#x60; response header contains the URL.  |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getPage"></a>
# **getPage**
> Page getPage(path, listPageSize, listPageSizeLarge, maxListPrefetch, itemDetailExpand, itemDetailSelectSeason, textEntryFormat, maxRating, device, sub, segments, ff, lang)



Returns a page with the specified id.  If targeting the search page you must url encode the search term as a parameter using the &#x60;q&#x60; key. For example if your browser path looks like &#x60;/search?q&#x3D;the&#x60; then what you pass to this endpoint would look like &#x60;/page?path&#x3D;/search%3Fq%3Dthe&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    AppApi apiInstance = new AppApi(defaultClient);
    String path = "path_example"; // String | The path of the page to load, e.g. '/movies'.
    Integer listPageSize = 12; // Integer | The number of items to load when prefetching and paging each list in the page row.
    Integer listPageSizeLarge = 50; // Integer | The number of items to load when prefetching a continuous scroll list entry in a page.  By default any list page entry with template pattern `/^CS\\d+$/` will be considered a continuous scroll list. 
    Integer maxListPrefetch = 2; // Integer | The maximum number of lists to prefetch in the page.
    String itemDetailExpand = "all"; // String | Only relevant when loading item detail pages as these embed a detailed item in the main page entry.  If no value is specified no item dependencies are expanded.  If 'children' is specified then the list of any direct children will be expanded. For example seasons of a show or episodes of a season.  If 'all' is specified then the parent chain will be expanded along with any child list at each level. For example if an episode is specified then its season will be expanded and that season's episode list. The season will have its show expanded and the show will have its season list expanded.  The 'all' options is useful when you deep link into a show/season/episode for the first time as it provides full context for navigating around the show page. Subsequent navigation around children of the show should only need to request expand of children.  If 'ancestors' is specified then only the parent chain is included  If an expand is specified which is not relevant to the item type, it will be ignored. 
    String itemDetailSelectSeason = "first"; // String | Only relevant when loading show detail pages as these embed a detailed item in the main page entry.  Since the introduction of the D1,2,3 templates this parameter is now somewhat redundant, or less likely to have any effect. While it may still be useful in some cases, most of the time the season selection will be dictated by the configuration of the rows scheduled on the show detail page. This parameter will only take effect if there are rows used to schedule episodes of a season, like D1,2,3, or if no rows have a value set for their `seasonOrder` custom field.  Given a targeted show page, it can be useful to get the details of a child season. This option provides a means to return the `first` or `latest` season of a show embedded in the page.  The `expand` parameter also works here so for example you could land on a show page and request the `item_detail_select_season=latest` along with `item_detail_expand=all`. This would then return the detail of the latest season with its list of child episode summaries, and also expand the detail of the show with its list of seasons summaries. 
    String textEntryFormat = "markdown"; // String | Only relevant to page entries of type `TextEntry`.  Converts the value of a text page entry to the specified format. 
    String maxRating = "maxRating_example"; // String | The maximum rating (inclusive) of items returned, e.g. 'auoflc-pg'.
    String device = "web_browser"; // String | The type of device the content is targeting.
    String sub = "sub_example"; // String | The active subscription code.
    List<String> segments = Arrays.asList(); // List<String> | The list of segments to filter the response by.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      Page result = apiInstance.getPage(path, listPageSize, listPageSizeLarge, maxListPrefetch, itemDetailExpand, itemDetailSelectSeason, textEntryFormat, maxRating, device, sub, segments, ff, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppApi#getPage");
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
| **path** | **String**| The path of the page to load, e.g. &#39;/movies&#39;. | |
| **listPageSize** | **Integer**| The number of items to load when prefetching and paging each list in the page row. | [optional] [default to 12] |
| **listPageSizeLarge** | **Integer**| The number of items to load when prefetching a continuous scroll list entry in a page.  By default any list page entry with template pattern &#x60;/^CS\\d+$/&#x60; will be considered a continuous scroll list.  | [optional] [default to 50] |
| **maxListPrefetch** | **Integer**| The maximum number of lists to prefetch in the page. | [optional] [default to 2] |
| **itemDetailExpand** | **String**| Only relevant when loading item detail pages as these embed a detailed item in the main page entry.  If no value is specified no item dependencies are expanded.  If &#39;children&#39; is specified then the list of any direct children will be expanded. For example seasons of a show or episodes of a season.  If &#39;all&#39; is specified then the parent chain will be expanded along with any child list at each level. For example if an episode is specified then its season will be expanded and that season&#39;s episode list. The season will have its show expanded and the show will have its season list expanded.  The &#39;all&#39; options is useful when you deep link into a show/season/episode for the first time as it provides full context for navigating around the show page. Subsequent navigation around children of the show should only need to request expand of children.  If &#39;ancestors&#39; is specified then only the parent chain is included  If an expand is specified which is not relevant to the item type, it will be ignored.  | [optional] [enum: all, children, ancestors] |
| **itemDetailSelectSeason** | **String**| Only relevant when loading show detail pages as these embed a detailed item in the main page entry.  Since the introduction of the D1,2,3 templates this parameter is now somewhat redundant, or less likely to have any effect. While it may still be useful in some cases, most of the time the season selection will be dictated by the configuration of the rows scheduled on the show detail page. This parameter will only take effect if there are rows used to schedule episodes of a season, like D1,2,3, or if no rows have a value set for their &#x60;seasonOrder&#x60; custom field.  Given a targeted show page, it can be useful to get the details of a child season. This option provides a means to return the &#x60;first&#x60; or &#x60;latest&#x60; season of a show embedded in the page.  The &#x60;expand&#x60; parameter also works here so for example you could land on a show page and request the &#x60;item_detail_select_season&#x3D;latest&#x60; along with &#x60;item_detail_expand&#x3D;all&#x60;. This would then return the detail of the latest season with its list of child episode summaries, and also expand the detail of the show with its list of seasons summaries.  | [optional] [enum: first, latest] |
| **textEntryFormat** | **String**| Only relevant to page entries of type &#x60;TextEntry&#x60;.  Converts the value of a text page entry to the specified format.  | [optional] [default to markdown] [enum: markdown, html] |
| **maxRating** | **String**| The maximum rating (inclusive) of items returned, e.g. &#39;auoflc-pg&#39;. | [optional] |
| **device** | **String**| The type of device the content is targeting. | [optional] [default to web_browser] |
| **sub** | **String**| The active subscription code. | [optional] |
| **segments** | [**List&lt;String&gt;**](String.md)| The list of segments to filter the response by. | [optional] |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The page requested. |  -  |
| **301** | Returned if feature flag &#x60;cd&#x60; is set and item detail is requested of an item that has Custom Destination set to an External URL. The &#x60;Location&#x60; response header contains the URL.  |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

