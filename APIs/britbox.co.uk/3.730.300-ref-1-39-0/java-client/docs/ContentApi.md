# ContentApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAnonNextPlaybackItem**](ContentApi.md#getAnonNextPlaybackItem) | **GET** /items/{itemId}/next |  |
| [**getItem**](ContentApi.md#getItem) | **GET** /items/{id} |  |
| [**getItemChildrenList**](ContentApi.md#getItemChildrenList) | **GET** /items/{id}/children |  |
| [**getItemDownloadables**](ContentApi.md#getItemDownloadables) | **POST** /itv/items/downloadable |  |
| [**getItemRelatedList**](ContentApi.md#getItemRelatedList) | **GET** /items/{id}/related |  |
| [**getItemsMediaClipFiles**](ContentApi.md#getItemsMediaClipFiles) | **POST** /itv/items/clips |  |
| [**getList**](ContentApi.md#getList) | **GET** /lists/{id} |  |
| [**getLists**](ContentApi.md#getLists) | **GET** /lists |  |
| [**getPublicItemMediaFiles**](ContentApi.md#getPublicItemMediaFiles) | **GET** /items/{id}/videos |  |
| [**getSchedules**](ContentApi.md#getSchedules) | **GET** /schedules |  |
| [**plansIdGet**](ContentApi.md#plansIdGet) | **GET** /plans/{id} |  |
| [**search**](ContentApi.md#search) | **GET** /search |  |


<a id="getAnonNextPlaybackItem"></a>
# **getAnonNextPlaybackItem**
> NextPlaybackItem getAnonNextPlaybackItem(itemId, maxRating, expand, device, segments, ff, lang)



Identical to GET /account/profile/items/{itemId}/next route but for users that are not logged in i.e. this endpoint does not require authorisation 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ContentApi apiInstance = new ContentApi(defaultClient);
    String itemId = "itemId_example"; // String | The identifier of the source item to base the next to watch item off. 
    String maxRating = "maxRating_example"; // String | The maximum rating (inclusive) of an item returned, e.g. 'auoflc-pg'.
    String expand = "parent"; // String | If no value is specified no dependencies are expanded.  If 'parent' is specified then only the direct parent will be expanded. For example if an `Episode` then the `Season` would be included.  If 'ancestors' is specified then the full parent chain is expanded. For example if an `Episode` then both the `Season` and `Show` would be included. 
    String device = "web_browser"; // String | The type of device the content is targeting.
    List<String> segments = Arrays.asList(); // List<String> | The list of segments to filter the response by.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      NextPlaybackItem result = apiInstance.getAnonNextPlaybackItem(itemId, maxRating, expand, device, segments, ff, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#getAnonNextPlaybackItem");
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
| **itemId** | **String**| The identifier of the source item to base the next to watch item off.  | |
| **maxRating** | **String**| The maximum rating (inclusive) of an item returned, e.g. &#39;auoflc-pg&#39;. | [optional] |
| **expand** | **String**| If no value is specified no dependencies are expanded.  If &#39;parent&#39; is specified then only the direct parent will be expanded. For example if an &#x60;Episode&#x60; then the &#x60;Season&#x60; would be included.  If &#39;ancestors&#39; is specified then the full parent chain is expanded. For example if an &#x60;Episode&#x60; then both the &#x60;Season&#x60; and &#x60;Show&#x60; would be included.  | [optional] [enum: parent, ancestors] |
| **device** | **String**| The type of device the content is targeting. | [optional] [default to web_browser] |
| **segments** | [**List&lt;String&gt;**](String.md)| The list of segments to filter the response by. | [optional] |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**NextPlaybackItem**](NextPlaybackItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The detail of the next item to play. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getItem"></a>
# **getItem**
> ItemDetail getItem(id, maxRating, expand, selectSeason, useCustomId, device, sub, segments, ff, lang)



Returns the details of an item with the specified id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ContentApi apiInstance = new ContentApi(defaultClient);
    String id = "id_example"; // String | The identifier of the item to load.  The custom identifier of an item can be used here if the `use_custom_id` parameter is true. 
    String maxRating = "maxRating_example"; // String | The maximum rating (inclusive) of items returned, e.g. 'auoflc-pg'.
    String expand = "all"; // String | If no value is specified no dependencies are expanded.  If 'children' is specified then the list of any direct children will be expanded. For example seasons of a show or episodes of a season.  If 'all' is specified then the parent chain will be expanded along with any child list at each level. For example if an episode is specified then its season will be expanded and that season's episode list. The season will have its show expanded and the show will have its season list expanded.  The 'all' options is useful when you deep link into a show/season/episode for the first time as it provides full context for navigating around the show page. Subsequent navigation around children of the show should only need to request expand of children.  If 'ancestors' is specified then only the parent chain is included.  If 'parent' is specified then only the direct parent is included.  If an expand is specified which is not relevant to the item type, it will be ignored. 
    String selectSeason = "first"; // String | Given a provided show id, it can be useful to get the details of a child season. This option provides a means to return the `first` or `latest` season of a show given the show id.  The `expand` parameter also works here so for example you could land on a show page and request the latest season along with `expand=all`. This would then return the detail of the latest season with its list of child episode summaries, and also expand the detail of the show with its list of seasons summaries.  Note the `id` parameter must be a show id for this parameter to work correctly. 
    Boolean useCustomId = true; // Boolean | Set to true when passing a custom Id as the `id` path parameter.
    String device = "web_browser"; // String | The type of device the content is targeting.
    String sub = "sub_example"; // String | The active subscription code.
    List<String> segments = Arrays.asList(); // List<String> | The list of segments to filter the response by.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItemDetail result = apiInstance.getItem(id, maxRating, expand, selectSeason, useCustomId, device, sub, segments, ff, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#getItem");
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
| **id** | **String**| The identifier of the item to load.  The custom identifier of an item can be used here if the &#x60;use_custom_id&#x60; parameter is true.  | |
| **maxRating** | **String**| The maximum rating (inclusive) of items returned, e.g. &#39;auoflc-pg&#39;. | [optional] |
| **expand** | **String**| If no value is specified no dependencies are expanded.  If &#39;children&#39; is specified then the list of any direct children will be expanded. For example seasons of a show or episodes of a season.  If &#39;all&#39; is specified then the parent chain will be expanded along with any child list at each level. For example if an episode is specified then its season will be expanded and that season&#39;s episode list. The season will have its show expanded and the show will have its season list expanded.  The &#39;all&#39; options is useful when you deep link into a show/season/episode for the first time as it provides full context for navigating around the show page. Subsequent navigation around children of the show should only need to request expand of children.  If &#39;ancestors&#39; is specified then only the parent chain is included.  If &#39;parent&#39; is specified then only the direct parent is included.  If an expand is specified which is not relevant to the item type, it will be ignored.  | [optional] [enum: all, children, ancestors, parent] |
| **selectSeason** | **String**| Given a provided show id, it can be useful to get the details of a child season. This option provides a means to return the &#x60;first&#x60; or &#x60;latest&#x60; season of a show given the show id.  The &#x60;expand&#x60; parameter also works here so for example you could land on a show page and request the latest season along with &#x60;expand&#x3D;all&#x60;. This would then return the detail of the latest season with its list of child episode summaries, and also expand the detail of the show with its list of seasons summaries.  Note the &#x60;id&#x60; parameter must be a show id for this parameter to work correctly.  | [optional] [enum: first, latest] |
| **useCustomId** | **Boolean**| Set to true when passing a custom Id as the &#x60;id&#x60; path parameter. | [optional] |
| **device** | **String**| The type of device the content is targeting. | [optional] [default to web_browser] |
| **sub** | **String**| The active subscription code. | [optional] |
| **segments** | [**List&lt;String&gt;**](String.md)| The list of segments to filter the response by. | [optional] |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItemDetail**](ItemDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The item requested |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getItemChildrenList"></a>
# **getItemChildrenList**
> ItemList getItemChildrenList(id, page, pageSize, maxRating, order, device, sub, segments, ff, lang)



Returns the List of child summary items under an item.  If the item is a Season then the children will be episodes and ordered by episode number.  If the item is a Show then the children will be Seasons and ordered by season number.  Returns 404 if no children found. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ContentApi apiInstance = new ContentApi(defaultClient);
    String id = "id_example"; // String | The identifier of the item whose children to load.
    Integer page = 1; // Integer | The page of items to load. Starts from page 1.
    Integer pageSize = 12; // Integer | The number of items to return in a page.
    String maxRating = "maxRating_example"; // String | The maximum rating (inclusive) of items returned, e.g. 'auoflc-pg'.
    String order = "asc"; // String | The list sort order, either 'asc' or 'desc'.
    String device = "web_browser"; // String | The type of device the content is targeting.
    String sub = "sub_example"; // String | The active subscription code.
    List<String> segments = Arrays.asList(); // List<String> | The list of segments to filter the response by.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItemList result = apiInstance.getItemChildrenList(id, page, pageSize, maxRating, order, device, sub, segments, ff, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#getItemChildrenList");
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
| **id** | **String**| The identifier of the item whose children to load. | |
| **page** | **Integer**| The page of items to load. Starts from page 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return in a page. | [optional] [default to 12] |
| **maxRating** | **String**| The maximum rating (inclusive) of items returned, e.g. &#39;auoflc-pg&#39;. | [optional] |
| **order** | **String**| The list sort order, either &#39;asc&#39; or &#39;desc&#39;. | [optional] [default to desc] [enum: asc, desc] |
| **device** | **String**| The type of device the content is targeting. | [optional] [default to web_browser] |
| **sub** | **String**| The active subscription code. | [optional] |
| **segments** | [**List&lt;String&gt;**](String.md)| The list of segments to filter the response by. | [optional] |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItemList**](ItemList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of items requested. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getItemDownloadables"></a>
# **getItemDownloadables**
> ItemDownloadableList getItemDownloadables(itemDownloadableRequest, ff, lang)



Returns the details of an item with the specified id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ContentApi apiInstance = new ContentApi(defaultClient);
    ItemDownloadableRequest itemDownloadableRequest = new ItemDownloadableRequest(); // ItemDownloadableRequest | The item Axis ids joined string with comma.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItemDownloadableList result = apiInstance.getItemDownloadables(itemDownloadableRequest, ff, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#getItemDownloadables");
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
| **itemDownloadableRequest** | [**ItemDownloadableRequest**](ItemDownloadableRequest.md)| The item Axis ids joined string with comma. | |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItemDownloadableList**](ItemDownloadableList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The item requested |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getItemRelatedList"></a>
# **getItemRelatedList**
> ItemList getItemRelatedList(id, page, pageSize, maxRating, device, sub, segments, ff, lang)



Returns the list of items related to the parent item.  Note for now, due to the size of the list being unknown, only a single page will be returned. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ContentApi apiInstance = new ContentApi(defaultClient);
    String id = "id_example"; // String | The identifier of the item to based related items off.
    Integer page = 1; // Integer | The page of items to load. Starts from page 1.
    Integer pageSize = 12; // Integer | The number of items to return in a page.
    String maxRating = "maxRating_example"; // String | The maximum rating (inclusive) of items returned, e.g. 'auoflc-pg'.
    String device = "web_browser"; // String | The type of device the content is targeting.
    String sub = "sub_example"; // String | The active subscription code.
    List<String> segments = Arrays.asList(); // List<String> | The list of segments to filter the response by.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItemList result = apiInstance.getItemRelatedList(id, page, pageSize, maxRating, device, sub, segments, ff, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#getItemRelatedList");
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
| **id** | **String**| The identifier of the item to based related items off. | |
| **page** | **Integer**| The page of items to load. Starts from page 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return in a page. | [optional] [default to 12] |
| **maxRating** | **String**| The maximum rating (inclusive) of items returned, e.g. &#39;auoflc-pg&#39;. | [optional] |
| **device** | **String**| The type of device the content is targeting. | [optional] [default to web_browser] |
| **sub** | **String**| The active subscription code. | [optional] |
| **segments** | [**List&lt;String&gt;**](String.md)| The list of segments to filter the response by. | [optional] |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItemList**](ItemList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of items requested. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getItemsMediaClipFiles"></a>
# **getItemsMediaClipFiles**
> ItemClipFilesList getItemsMediaClipFiles(itemDownloadableRequest, ff, lang)



Get the media clip files associated with items. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ContentApi apiInstance = new ContentApi(defaultClient);
    ItemDownloadableRequest itemDownloadableRequest = new ItemDownloadableRequest(); // ItemDownloadableRequest | The item Axis ids joined string with comma.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItemClipFilesList result = apiInstance.getItemsMediaClipFiles(itemDownloadableRequest, ff, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#getItemsMediaClipFiles");
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
| **itemDownloadableRequest** | [**ItemDownloadableRequest**](ItemDownloadableRequest.md)| The item Axis ids joined string with comma. | |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItemClipFilesList**](ItemClipFilesList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The item id with clip files |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getList"></a>
# **getList**
> ItemList getList(id, page, pageSize, maxRating, order, orderBy, param, itemType, device, sub, segments, ff, lang)



Returns a list of items under the specified item list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ContentApi apiInstance = new ContentApi(defaultClient);
    String id = "id_example"; // String | The identifier of the list to load.
    Integer page = 1; // Integer | The page of items to load. Starts from page 1.
    Integer pageSize = 12; // Integer | The number of items to return in a page.
    String maxRating = "maxRating_example"; // String | The maximum rating (inclusive) of items returned, e.g. 'auoflc-pg'.
    String order = "asc"; // String | The list sort order, either 'asc' or 'desc'.
    String orderBy = "a-z"; // String | What to order by.
    String param = "param_example"; // String | The list parameter in format 'key:value', e.g. 'genre:action'.
    String itemType = "movie"; // String | The item type to filter by. Defaults to unspecified.
    String device = "web_browser"; // String | The type of device the content is targeting.
    String sub = "sub_example"; // String | The active subscription code.
    List<String> segments = Arrays.asList(); // List<String> | The list of segments to filter the response by.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItemList result = apiInstance.getList(id, page, pageSize, maxRating, order, orderBy, param, itemType, device, sub, segments, ff, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#getList");
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
| **id** | **String**| The identifier of the list to load. | |
| **page** | **Integer**| The page of items to load. Starts from page 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return in a page. | [optional] [default to 12] |
| **maxRating** | **String**| The maximum rating (inclusive) of items returned, e.g. &#39;auoflc-pg&#39;. | [optional] |
| **order** | **String**| The list sort order, either &#39;asc&#39; or &#39;desc&#39;. | [optional] [default to desc] [enum: asc, desc] |
| **orderBy** | **String**| What to order by. | [optional] [enum: a-z, release-year, date-added] |
| **param** | **String**| The list parameter in format &#39;key:value&#39;, e.g. &#39;genre:action&#39;. | [optional] |
| **itemType** | **String**| The item type to filter by. Defaults to unspecified. | [optional] [enum: movie, show, season, episode, program, link, trailer, channel, customAsset] |
| **device** | **String**| The type of device the content is targeting. | [optional] [default to web_browser] |
| **sub** | **String**| The active subscription code. | [optional] |
| **segments** | [**List&lt;String&gt;**](String.md)| The list of segments to filter the response by. | [optional] |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItemList**](ItemList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of items requested. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getLists"></a>
# **getLists**
> List&lt;ItemList&gt; getLists(ids, pageSize, maxRating, order, orderBy, itemType, device, sub, segments, ff, lang)



Returns an array of item lists with their first page of content resolved.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ContentApi apiInstance = new ContentApi(defaultClient);
    List<String> ids = Arrays.asList(); // List<String> | A comma delimited list of item list identifiers.  These can be list ids e.g. `14354,65473,3234`  Or more complex sort/filter queries using pipes e.g.  `14354|max_rating=AUOFLC-E|order=asc|order_by=year-added,65473|page_size=30,3234`  _Note the id must always come first for each encoded list query_  List parameters may be provide without the `param=` prefix e.g. `14354|genre:action`  Only the following options can be present.   - `order`   - `order_by`   - `max_rating`   - `page_size`   - `item_type`   - `param` 
    Integer pageSize = 12; // Integer | The number of items to return in a page.
    String maxRating = "maxRating_example"; // String | The maximum rating (inclusive) of items returned, e.g. 'auoflc-pg'.
    String order = "asc"; // String | The list sort order, either 'asc' or 'desc'.
    String orderBy = "a-z"; // String | What to order by.
    String itemType = "movie"; // String | The item type to filter by. Defaults to unspecified.
    String device = "web_browser"; // String | The type of device the content is targeting.
    String sub = "sub_example"; // String | The active subscription code.
    List<String> segments = Arrays.asList(); // List<String> | The list of segments to filter the response by.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      List<ItemList> result = apiInstance.getLists(ids, pageSize, maxRating, order, orderBy, itemType, device, sub, segments, ff, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#getLists");
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
| **ids** | [**List&lt;String&gt;**](String.md)| A comma delimited list of item list identifiers.  These can be list ids e.g. &#x60;14354,65473,3234&#x60;  Or more complex sort/filter queries using pipes e.g.  &#x60;14354|max_rating&#x3D;AUOFLC-E|order&#x3D;asc|order_by&#x3D;year-added,65473|page_size&#x3D;30,3234&#x60;  _Note the id must always come first for each encoded list query_  List parameters may be provide without the &#x60;param&#x3D;&#x60; prefix e.g. &#x60;14354|genre:action&#x60;  Only the following options can be present.   - &#x60;order&#x60;   - &#x60;order_by&#x60;   - &#x60;max_rating&#x60;   - &#x60;page_size&#x60;   - &#x60;item_type&#x60;   - &#x60;param&#x60;  | |
| **pageSize** | **Integer**| The number of items to return in a page. | [optional] [default to 12] |
| **maxRating** | **String**| The maximum rating (inclusive) of items returned, e.g. &#39;auoflc-pg&#39;. | [optional] |
| **order** | **String**| The list sort order, either &#39;asc&#39; or &#39;desc&#39;. | [optional] [default to desc] [enum: asc, desc] |
| **orderBy** | **String**| What to order by. | [optional] [enum: a-z, release-year, date-added] |
| **itemType** | **String**| The item type to filter by. Defaults to unspecified. | [optional] [enum: movie, show, season, episode, program, link, trailer, channel, customAsset] |
| **device** | **String**| The type of device the content is targeting. | [optional] [default to web_browser] |
| **sub** | **String**| The active subscription code. | [optional] |
| **segments** | [**List&lt;String&gt;**](String.md)| The list of segments to filter the response by. | [optional] |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**List&lt;ItemList&gt;**](ItemList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The array of item lists requested. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getPublicItemMediaFiles"></a>
# **getPublicItemMediaFiles**
> List&lt;MediaFile&gt; getPublicItemMediaFiles(id, delivery, resolution, formats, device, sub, segments, ff, lang)



Get the free / public video files associated with an item given maximum resolution, device type and one or more delivery types.  Returns an array of video file objects which each include a url to a video.  The first entry in the array contains what is predicted to be the best match. The remainder of the entries, if any, may contain resolutions below what was requests. For example if you request HD-720 the response may also contain SD entries.  If you specify multiple delivery types, then the response array will insert types in the order you specify them in the query. For example &#x60;stream,progressive&#x60; would return an array with 0 or more stream files followed by 0 or more progressive files.  If no files are found a 404 is returned. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ContentApi apiInstance = new ContentApi(defaultClient);
    String id = "id_example"; // String | The identifier of the item whose video files to load.
    List<String> delivery = Arrays.asList(); // List<String> | The video delivery type you require.
    String resolution = "HD-4K"; // String | The maximum resolution the device to playback the media can present.
    List<String> formats = Arrays.asList(); // List<String> | The set of media file formats that the device supports, in the order of preference.  When provided, Rocket API returns only media files in formats specified in this parameter. For each resolution, only the first media file of matching supported format is returned. Files of different resolutions may be of different supported media file formats.  `external` value is reserved for project customizations where the real MIME type of the file on the specified URL is unknown at the time of ingestion.  When not provided, Rocket API uses the legacy `User-Agent` header-based logic to find matching media files. 
    String device = "web_browser"; // String | The type of device the content is targeting.
    String sub = "sub_example"; // String | The active subscription code.
    List<String> segments = Arrays.asList(); // List<String> | The list of segments to filter the response by.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      List<MediaFile> result = apiInstance.getPublicItemMediaFiles(id, delivery, resolution, formats, device, sub, segments, ff, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#getPublicItemMediaFiles");
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
| **id** | **String**| The identifier of the item whose video files to load. | |
| **delivery** | [**List&lt;String&gt;**](String.md)| The video delivery type you require. | [enum: stream, progressive, download] |
| **resolution** | **String**| The maximum resolution the device to playback the media can present. | [enum: HD-4K, HD-1080, HD-720, SD, External] |
| **formats** | [**List&lt;String&gt;**](String.md)| The set of media file formats that the device supports, in the order of preference.  When provided, Rocket API returns only media files in formats specified in this parameter. For each resolution, only the first media file of matching supported format is returned. Files of different resolutions may be of different supported media file formats.  &#x60;external&#x60; value is reserved for project customizations where the real MIME type of the file on the specified URL is unknown at the time of ingestion.  When not provided, Rocket API uses the legacy &#x60;User-Agent&#x60; header-based logic to find matching media files.  | [optional] [enum: mp4, mpd, hls, external] |
| **device** | **String**| The type of device the content is targeting. | [optional] [default to web_browser] |
| **sub** | **String**| The active subscription code. | [optional] |
| **segments** | [**List&lt;String&gt;**](String.md)| The list of segments to filter the response by. | [optional] |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**List&lt;MediaFile&gt;**](MediaFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of video files available. The first entry containing what is predicted to be the best match.  |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getSchedules"></a>
# **getSchedules**
> List&lt;ItemScheduleList&gt; getSchedules(channels, date, hour, duration, intersect, device, sub, segments, ff, lang)



Returns schedules for a defined set of channels over a requested period.  Schedules are requested in hour blocks and returned grouped by the channel they belong to.  For example, to load 12 hours of schedules for channels &#x60;4343&#x60; and &#x60;5234&#x60;, on 21/2/2017 starting from 08:00.  &#x60;&#x60;&#x60; channels&#x3D;4343,5234 date&#x3D;2017-02-21 hour&#x3D;8 duration&#x3D;12 &#x60;&#x60;&#x60;  Please remember that &#x60;date&#x60; and &#x60;hour&#x60; combined represent a normal datetime,  so they should be converted to UTC on the client - this will help to avoid  issues with EPG schedules near midnight.  If a channel id is passed which doesn&#39;t exist then this endpoint will return an empty schedule list for it. If instead we returned 404, this would invalidate all other channel schedules in the same request which would be unfriendly for clients presenting these channel schedules. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ContentApi apiInstance = new ContentApi(defaultClient);
    List<String> channels = Arrays.asList(); // List<String> | The list of channel ids to get schedules for.
    LocalDate date = LocalDate.now(); // LocalDate | The date to target in ISO format, e.g. `2017-05-23` (converted to UTC - see main description).  The base hour requested will belong to this date. 
    Integer hour = 56; // Integer | The base hour in the day, defined by the `date` parameter, you wish to load schedules for  (converted to UTC - see main description).  From 0 to 23, where 0 is midnight. 
    Integer duration = 56; // Integer | The number of hours of schedules to load from the base `hour` parameter.  This may be negative or positive depending on whether you want to load past or future schedules.  Minimum value is -24, maximum is 24. A value of zero is invalid. 
    Boolean intersect = false; // Boolean | Flag indicating whether schedules should intersect or be contained in the provided interval.  If set to `true`, the result will contain all schedules where either schedule start time or end time touches the provided interval.  If set to `false`, only schedules fully contained in the given period will be returned. 
    String device = "web_browser"; // String | The type of device the content is targeting.
    String sub = "sub_example"; // String | The active subscription code.
    List<String> segments = Arrays.asList(); // List<String> | The list of segments to filter the response by.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      List<ItemScheduleList> result = apiInstance.getSchedules(channels, date, hour, duration, intersect, device, sub, segments, ff, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#getSchedules");
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
| **channels** | [**List&lt;String&gt;**](String.md)| The list of channel ids to get schedules for. | |
| **date** | **LocalDate**| The date to target in ISO format, e.g. &#x60;2017-05-23&#x60; (converted to UTC - see main description).  The base hour requested will belong to this date.  | |
| **hour** | **Integer**| The base hour in the day, defined by the &#x60;date&#x60; parameter, you wish to load schedules for  (converted to UTC - see main description).  From 0 to 23, where 0 is midnight.  | |
| **duration** | **Integer**| The number of hours of schedules to load from the base &#x60;hour&#x60; parameter.  This may be negative or positive depending on whether you want to load past or future schedules.  Minimum value is -24, maximum is 24. A value of zero is invalid.  | |
| **intersect** | **Boolean**| Flag indicating whether schedules should intersect or be contained in the provided interval.  If set to &#x60;true&#x60;, the result will contain all schedules where either schedule start time or end time touches the provided interval.  If set to &#x60;false&#x60;, only schedules fully contained in the given period will be returned.  | [optional] [default to false] |
| **device** | **String**| The type of device the content is targeting. | [optional] [default to web_browser] |
| **sub** | **String**| The active subscription code. | [optional] |
| **segments** | [**List&lt;String&gt;**](String.md)| The list of segments to filter the response by. | [optional] |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**List&lt;ItemScheduleList&gt;**](ItemScheduleList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of schedule lists for each channel requested.  The order of the channels will match the order of channel ids passed during the request.  |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="plansIdGet"></a>
# **plansIdGet**
> Plan plansIdGet(id, device, sub, segments, ff, lang)



Returns the details of a Plan with the specified id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ContentApi apiInstance = new ContentApi(defaultClient);
    String id = "id_example"; // String | The identifier of the Plan to load.
    String device = "web_browser"; // String | The type of device the content is targeting.
    String sub = "sub_example"; // String | The active subscription code.
    List<String> segments = Arrays.asList(); // List<String> | The list of segments to filter the response by.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      Plan result = apiInstance.plansIdGet(id, device, sub, segments, ff, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#plansIdGet");
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
| **id** | **String**| The identifier of the Plan to load. | |
| **device** | **String**| The type of device the content is targeting. | [optional] [default to web_browser] |
| **sub** | **String**| The active subscription code. | [optional] |
| **segments** | [**List&lt;String&gt;**](String.md)| The list of segments to filter the response by. | [optional] |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**Plan**](Plan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Plan requested. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="search"></a>
# **search**
> SearchResults search(term, include, group, maxResults, maxRating, device, sub, segments, ff, lang)



Search the catalog of items and people.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ContentApi apiInstance = new ContentApi(defaultClient);
    String term = "term_example"; // String | The search term to query.
    List<String> include = Arrays.asList(); // List<String> | By default people, movies and tv (shows + programs) will be included in the search results.  If the `cas` feature flag is set, \"other\" items (`customAsset`s) will also be included by default  If you don't want all of these types you can specifiy the specific includes you care about. 
    Boolean group = true; // Boolean | When this option is set, instead of all search result items being returned in a single list, they will instead be returned under two lists. One for movies and another for tv (shows + programs).  if the `cas` feature flag is set, a third `other` list will be included containing `customAsset` results  Default is undefined meaning items will be returned in a single list.  The array of `people` results will always be separate from items. 
    Integer maxResults = 20; // Integer | The maximum number of results to return.
    String maxRating = "maxRating_example"; // String | The maximum rating (inclusive) of items returned, e.g. 'auoflc-pg'.
    String device = "web_browser"; // String | The type of device the content is targeting.
    String sub = "sub_example"; // String | The active subscription code.
    List<String> segments = Arrays.asList(); // List<String> | The list of segments to filter the response by.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      SearchResults result = apiInstance.search(term, include, group, maxResults, maxRating, device, sub, segments, ff, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#search");
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
| **term** | **String**| The search term to query. | |
| **include** | [**List&lt;String&gt;**](String.md)| By default people, movies and tv (shows + programs) will be included in the search results.  If the &#x60;cas&#x60; feature flag is set, \&quot;other\&quot; items (&#x60;customAsset&#x60;s) will also be included by default  If you don&#39;t want all of these types you can specifiy the specific includes you care about.  | [optional] [enum: tv, movies, people, other] |
| **group** | **Boolean**| When this option is set, instead of all search result items being returned in a single list, they will instead be returned under two lists. One for movies and another for tv (shows + programs).  if the &#x60;cas&#x60; feature flag is set, a third &#x60;other&#x60; list will be included containing &#x60;customAsset&#x60; results  Default is undefined meaning items will be returned in a single list.  The array of &#x60;people&#x60; results will always be separate from items.  | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return. | [optional] [default to 20] |
| **maxRating** | **String**| The maximum rating (inclusive) of items returned, e.g. &#39;auoflc-pg&#39;. | [optional] |
| **device** | **String**| The type of device the content is targeting. | [optional] [default to web_browser] |
| **sub** | **String**| The active subscription code. | [optional] |
| **segments** | [**List&lt;String&gt;**](String.md)| The list of segments to filter the response by. | [optional] |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

