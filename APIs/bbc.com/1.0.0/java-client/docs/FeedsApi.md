# FeedsApi

All URIs are relative to *https://programmes.api.bbc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listAvailability**](FeedsApi.md#listAvailability) | **GET** /availabilities | Discover details of on-demand availability for programmes and their versions |
| [**listBroadcasts**](FeedsApi.md#listBroadcasts) | **GET** /broadcasts | Build schedules and find metadata for TV and radio broadcasts |
| [**listGroups**](FeedsApi.md#listGroups) | **GET** /groups | Find metadata for curated groups: seasons, collections, galleries or franchises |
| [**listImages**](FeedsApi.md#listImages) | **GET** /images | Find metadata for images |
| [**listItems**](FeedsApi.md#listItems) | **GET** /items | Look inside programmes to find segments: chapters, tracks and more |
| [**listMasterbrands**](FeedsApi.md#listMasterbrands) | **GET** /master_brands | List all Master Brands |
| [**listPeople**](FeedsApi.md#listPeople) | **GET** /people | Find the people behind and in programmes: cast, crew, guests and more |
| [**listPips**](FeedsApi.md#listPips) | **GET** /pips | Look inside pips entities |
| [**listProgrammeDetails**](FeedsApi.md#listProgrammeDetails) | **GET** /programme_details | Exposes programme information for a single pid |
| [**listProgrammes**](FeedsApi.md#listProgrammes) | **GET** /programmes | Start here for programmes metadata: Brands, Series, Episodes and Clips |
| [**listPromotions**](FeedsApi.md#listPromotions) | **GET** /promotions | Discover metadata for content promotions |
| [**listSchedules**](FeedsApi.md#listSchedules) | **GET** /schedules | Build schedules and find metadata for TV and radio broadcasts and webcasts |
| [**listServices**](FeedsApi.md#listServices) | **GET** /services | Information about the linear services used for broadcast transmissions |
| [**listVersions**](FeedsApi.md#listVersions) | **GET** /versions | Metadata on editorial programme versions: original, signed, audio-described, etc |


<a id="listAvailability"></a>
# **listAvailability**
> Nitro listAvailability(sort, sortDirection, availability, descendantsOf, mediaSet, page, pageSize, territory, debug)

Discover details of on-demand availability for programmes and their versions

Discover details of on-demand availability for programmes and their versions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    String sort = "scheduled_start"; // String | Sorts: * scheduled_start: sort chronologically by scheduled start time/date, ascending 
    String sortDirection = "ascending"; // String | Sort direction
    List<String> availability = Arrays.asList(); // List<String> | filter for subset of availabilities
    List<String> descendantsOf = Arrays.asList(); // List<String> | filter for subset of availabilities that have PID as ancestor
    List<String> mediaSet = Arrays.asList(); // List<String> | filter for subset of availabilities with media set
    Integer page = 1; // Integer | which page of results to return
    Integer pageSize = 10; // Integer | number of results in each page
    List<String> territory = Arrays.asList(); // List<String> | filter for availabilities in given territory
    Boolean debug = true; // Boolean | Turn on debug information (undocumented)
    try {
      Nitro result = apiInstance.listAvailability(sort, sortDirection, availability, descendantsOf, mediaSet, page, pageSize, territory, debug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#listAvailability");
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
| **sort** | **String**| Sorts: * scheduled_start: sort chronologically by scheduled start time/date, ascending  | [optional] [enum: scheduled_start] |
| **sortDirection** | **String**| Sort direction | [optional] [enum: ascending, descending] |
| **availability** | [**List&lt;String&gt;**](String.md)| filter for subset of availabilities | [optional] [enum: available] |
| **descendantsOf** | [**List&lt;String&gt;**](String.md)| filter for subset of availabilities that have PID as ancestor | [optional] |
| **mediaSet** | [**List&lt;String&gt;**](String.md)| filter for subset of availabilities with media set | [optional] |
| **page** | **Integer**| which page of results to return | [optional] [default to 1] |
| **pageSize** | **Integer**| number of results in each page | [optional] [default to 10] |
| **territory** | [**List&lt;String&gt;**](String.md)| filter for availabilities in given territory | [optional] [enum: uk, nonuk, world] |
| **debug** | **Boolean**| Turn on debug information (undocumented) | [optional] |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |
| **0** | Unexpected error |  -  |

<a id="listBroadcasts"></a>
# **listBroadcasts**
> Nitro listBroadcasts(sort, sortDirection, mixin, authority, descendantsOf, endFrom, endTo, format, genre, id, item, page, pageSize, people, pid, q, scheduleDay, scheduleDayFrom, scheduleDayTo, serviceMasterBrand, sid, startFrom, startTo, version)

Build schedules and find metadata for TV and radio broadcasts

Fetch metadata about linear Broadcasts and Services, allowing the generation of Television and Radio schedules and other datasets for broadcast items. Use /schedules instead of this feed as it is more efficient. Broadcasts will be deprecated in the future.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    String sort = "start_date"; // String | Sorts: * start_date: sort chronologically by scheduled start time/date, ascending 
    String sortDirection = "ascending"; // String | Sort direction
    List<String> mixin = Arrays.asList(); // List<String> | Mixins: * titles: return ancestor programme titles 
    List<String> authority = Arrays.asList(); // List<String> | filter for subset of broadcasts that have given authority
    List<String> descendantsOf = Arrays.asList(); // List<String> | filter for subset of broadcasts that are descendants of the given programme PID
    OffsetDateTime endFrom = OffsetDateTime.now(); // OffsetDateTime | filter for subset of broadcasts that end on or later than the specified datetime
    OffsetDateTime endTo = OffsetDateTime.now(); // OffsetDateTime | filter for subset of broadcasts that end on or earlier than the specified datetime
    List<String> format = Arrays.asList(); // List<String> | filter for subset of broadcasts that are classified in the given format ID
    List<String> genre = Arrays.asList(); // List<String> | filter for subset of broadcasts that are classified in the given genre ID
    List<String> id = Arrays.asList(); // List<String> | filter for subset of broadcasts that have given identifier
    List<String> item = Arrays.asList(); // List<String> | filter for subset of broadcasts with the given item performed on it
    Integer page = 1; // Integer | which page of results to return
    Integer pageSize = 10; // Integer | number of results in each page
    String people = "people_example"; // String | filter for subset of broadcasts that have given contributor
    List<String> pid = Arrays.asList(); // List<String> | filter for subset of broadcasts having given PID
    String q = "q_example"; // String | filter for subset of broadcasts matching supplied keyword/phrase (boolean operators permitted)
    LocalDate scheduleDay = LocalDate.now(); // LocalDate | filter for subset of broadcasts that start on the specified day (BBC time)
    LocalDate scheduleDayFrom = LocalDate.now(); // LocalDate | filter for subset of broadcasts that start on or after the specified day (BBC time)
    LocalDate scheduleDayTo = LocalDate.now(); // LocalDate | filter for subset of broadcasts that start on or before the specified day (BBC time)
    List<String> serviceMasterBrand = Arrays.asList(); // List<String> | filter for subset of broadcasts with given service master brand
    List<String> sid = Arrays.asList(); // List<String> | filter for subset of broadcasts that are on the specified linear service
    OffsetDateTime startFrom = OffsetDateTime.now(); // OffsetDateTime | filter for subset of broadcasts that start on or later than the specified datetime
    OffsetDateTime startTo = OffsetDateTime.now(); // OffsetDateTime | filter for subset of broadcasts that start on or earlier than the specified datetime
    List<String> version = Arrays.asList(); // List<String> | filter for subset of broadcasts with given PID as their parent version
    try {
      Nitro result = apiInstance.listBroadcasts(sort, sortDirection, mixin, authority, descendantsOf, endFrom, endTo, format, genre, id, item, page, pageSize, people, pid, q, scheduleDay, scheduleDayFrom, scheduleDayTo, serviceMasterBrand, sid, startFrom, startTo, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#listBroadcasts");
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
| **sort** | **String**| Sorts: * start_date: sort chronologically by scheduled start time/date, ascending  | [optional] [enum: start_date] |
| **sortDirection** | **String**| Sort direction | [optional] [enum: ascending, descending] |
| **mixin** | [**List&lt;String&gt;**](String.md)| Mixins: * titles: return ancestor programme titles  | [optional] [enum: titles] |
| **authority** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts that have given authority | [optional] |
| **descendantsOf** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts that are descendants of the given programme PID | [optional] |
| **endFrom** | **OffsetDateTime**| filter for subset of broadcasts that end on or later than the specified datetime | [optional] |
| **endTo** | **OffsetDateTime**| filter for subset of broadcasts that end on or earlier than the specified datetime | [optional] |
| **format** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts that are classified in the given format ID | [optional] |
| **genre** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts that are classified in the given genre ID | [optional] |
| **id** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts that have given identifier | [optional] |
| **item** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts with the given item performed on it | [optional] |
| **page** | **Integer**| which page of results to return | [optional] [default to 1] |
| **pageSize** | **Integer**| number of results in each page | [optional] [default to 10] |
| **people** | **String**| filter for subset of broadcasts that have given contributor | [optional] |
| **pid** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts having given PID | [optional] |
| **q** | **String**| filter for subset of broadcasts matching supplied keyword/phrase (boolean operators permitted) | [optional] |
| **scheduleDay** | **LocalDate**| filter for subset of broadcasts that start on the specified day (BBC time) | [optional] |
| **scheduleDayFrom** | **LocalDate**| filter for subset of broadcasts that start on or after the specified day (BBC time) | [optional] |
| **scheduleDayTo** | **LocalDate**| filter for subset of broadcasts that start on or before the specified day (BBC time) | [optional] |
| **serviceMasterBrand** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts with given service master brand | [optional] |
| **sid** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts that are on the specified linear service | [optional] |
| **startFrom** | **OffsetDateTime**| filter for subset of broadcasts that start on or later than the specified datetime | [optional] |
| **startTo** | **OffsetDateTime**| filter for subset of broadcasts that start on or earlier than the specified datetime | [optional] |
| **version** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts with given PID as their parent version | [optional] |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |
| **0** | Unexpected error |  -  |

<a id="listGroups"></a>
# **listGroups**
> Nitro listGroups(sort, sortDirection, mixin, forDescendantsOf, forProgramme, group, groupType, member, page, pageSize, partnerId, partnerPid, pid, q, embargoed)

Find metadata for curated groups: seasons, collections, galleries or franchises

Long-lived curated collections of programmes and more, including Collections, Seasons, Franchises and Galleries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    String sort = "pid"; // String | Sorts: * pid: sort alphabetically by PID 
    String sortDirection = "descending"; // String | Sort direction
    List<String> mixin = Arrays.asList(); // List<String> | Mixins: * alternate_images: mixin to return the alternate images for a group * group_for: mixin to return links to programme entities that group belongs to * images: mixin to add image information for a group * related_links: mixin to return related links for the group 
    String forDescendantsOf = "forDescendantsOf_example"; // String | filter for groups related to given programme or its descendants
    String forProgramme = "forProgramme_example"; // String | filter for subset of groups directly related to a given programme
    String group = "group_example"; // String | filter for subset of groups which belong to the given group pid
    List<String> groupType = Arrays.asList(); // List<String> | filter for subset of groups that have the given group type
    String member = "member_example"; // String | filter for subset of groups which contain an entity with the given pid as a member
    Integer page = 1; // Integer | which page of results to return
    Integer pageSize = 10; // Integer | number of results in each page
    List<String> partnerId = Arrays.asList(); // List<String> | filter for groups by partner ID
    List<String> partnerPid = Arrays.asList(""s0000001""); // List<String> | filter for groups by partner PID
    List<String> pid = Arrays.asList(); // List<String> | filter for subset of seasons, collections, galleries or franchises having given PID
    String q = "q_example"; // String | filter for subset of groups matching supplied keyword/phrase (boolean operators permitted)
    String embargoed = "include"; // String | Control return of embargoed items (undocumented)
    try {
      Nitro result = apiInstance.listGroups(sort, sortDirection, mixin, forDescendantsOf, forProgramme, group, groupType, member, page, pageSize, partnerId, partnerPid, pid, q, embargoed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#listGroups");
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
| **sort** | **String**| Sorts: * pid: sort alphabetically by PID  | [optional] [enum: pid] |
| **sortDirection** | **String**| Sort direction | [optional] [enum: descending] |
| **mixin** | [**List&lt;String&gt;**](String.md)| Mixins: * alternate_images: mixin to return the alternate images for a group * group_for: mixin to return links to programme entities that group belongs to * images: mixin to add image information for a group * related_links: mixin to return related links for the group  | [optional] [enum: alternate_images, group_for, images, related_links] |
| **forDescendantsOf** | **String**| filter for groups related to given programme or its descendants | [optional] |
| **forProgramme** | **String**| filter for subset of groups directly related to a given programme | [optional] |
| **group** | **String**| filter for subset of groups which belong to the given group pid | [optional] |
| **groupType** | [**List&lt;String&gt;**](String.md)| filter for subset of groups that have the given group type | [optional] [enum: collection, franchise, gallery, season] |
| **member** | **String**| filter for subset of groups which contain an entity with the given pid as a member | [optional] |
| **page** | **Integer**| which page of results to return | [optional] [default to 1] |
| **pageSize** | **Integer**| number of results in each page | [optional] [default to 10] |
| **partnerId** | [**List&lt;String&gt;**](String.md)| filter for groups by partner ID | [optional] |
| **partnerPid** | [**List&lt;String&gt;**](String.md)| filter for groups by partner PID | [optional] |
| **pid** | [**List&lt;String&gt;**](String.md)| filter for subset of seasons, collections, galleries or franchises having given PID | [optional] |
| **q** | **String**| filter for subset of groups matching supplied keyword/phrase (boolean operators permitted) | [optional] |
| **embargoed** | **String**| Control return of embargoed items (undocumented) | [optional] [enum: include, exclude, only] |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |
| **0** | Unexpected error |  -  |

<a id="listImages"></a>
# **listImages**
> Nitro listImages(sort, sortDirection, group, imageType, isAlternateImageFor, isImageFor, page, pageSize, partnerId, partnerPid, pid, q, embargoed)

Find metadata for images

Find metadata for images, particularly those in galleries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    String sort = "group_position"; // String | Sorts: * group_position: sort numerically by position, ascending only * pid: sort alphabetically by PID 
    String sortDirection = "ascending"; // String | Sort direction
    String group = "group_example"; // String | filter for images belonging to the given group (i.e. Gallery)
    List<String> imageType = Arrays.asList(); // List<String> | filter for images by type
    String isAlternateImageFor = "isAlternateImageFor_example"; // String | filter for alternate images by entity PID
    String isImageFor = "isImageFor_example"; // String | filter for images by entity PID
    Integer page = 1; // Integer | which page of results to return
    Integer pageSize = 10; // Integer | number of results in each page
    List<String> partnerId = Arrays.asList(); // List<String> | filter for images by partner ID
    List<String> partnerPid = Arrays.asList(""s0000001""); // List<String> | filter for images by partner PID
    List<String> pid = Arrays.asList(); // List<String> | filter for subset of images having given PID
    String q = "q_example"; // String | filter for subset of images matching supplied keyword/phrase (boolean operators permitted)
    String embargoed = "include"; // String | Control return of embargoed items (undocumented)
    try {
      Nitro result = apiInstance.listImages(sort, sortDirection, group, imageType, isAlternateImageFor, isImageFor, page, pageSize, partnerId, partnerPid, pid, q, embargoed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#listImages");
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
| **sort** | **String**| Sorts: * group_position: sort numerically by position, ascending only * pid: sort alphabetically by PID  | [optional] [enum: group_position, pid] |
| **sortDirection** | **String**| Sort direction | [optional] [enum: ascending, descending] |
| **group** | **String**| filter for images belonging to the given group (i.e. Gallery) | [optional] |
| **imageType** | [**List&lt;String&gt;**](String.md)| filter for images by type | [optional] [enum: standard, podcast, store, portrait, letterbox] |
| **isAlternateImageFor** | **String**| filter for alternate images by entity PID | [optional] |
| **isImageFor** | **String**| filter for images by entity PID | [optional] |
| **page** | **Integer**| which page of results to return | [optional] [default to 1] |
| **pageSize** | **Integer**| number of results in each page | [optional] [default to 10] |
| **partnerId** | [**List&lt;String&gt;**](String.md)| filter for images by partner ID | [optional] |
| **partnerPid** | [**List&lt;String&gt;**](String.md)| filter for images by partner PID | [optional] |
| **pid** | [**List&lt;String&gt;**](String.md)| filter for subset of images having given PID | [optional] |
| **q** | **String**| filter for subset of images matching supplied keyword/phrase (boolean operators permitted) | [optional] |
| **embargoed** | **String**| Control return of embargoed items (undocumented) | [optional] [enum: include, exclude, only] |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |
| **0** | Unexpected error |  -  |

<a id="listItems"></a>
# **listItems**
> Nitro listItems(sort, sortDirection, mixin, authority, id, idType, itemType, page, pageSize, partnerId, partnerPid, people, pid, programme, q, segmentEvent)

Look inside programmes to find segments: chapters, tracks and more

Look inside programmes to find segments: chapters, tracks and more

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    String sort = "pid"; // String | Sorts: * pid: sort by pid, descending 
    String sortDirection = "descending"; // String | Sort direction
    List<String> mixin = Arrays.asList(); // List<String> | Mixins: * contributions: mixin to return information about contributors to items * images: mixin to add image information for an item * offset: mixin to return programme segment offsets, works in conjunction with programme filter * play_event: mixin to return programme segment events, works in conjunction with programme or segment_event filters 
    String authority = "authority_example"; // String | filter for subset of items that have an ID issued by the given authority
    List<String> id = Arrays.asList(); // List<String> | filter for subset of items having given ID
    String idType = "idType_example"; // String | filter for subset of items that have given an ID of the given type
    List<String> itemType = Arrays.asList(); // List<String> | filter for specific type(s) of items
    Integer page = 1; // Integer | which page of results to return
    Integer pageSize = 10; // Integer | number of results in each page
    List<String> partnerId = Arrays.asList(); // List<String> | filter for items by partner ID
    List<String> partnerPid = Arrays.asList(""s0000001""); // List<String> | filter for items by partner PID
    String people = "people_example"; // String | filter for subset of items that have specified person involved
    List<String> pid = Arrays.asList(); // List<String> | filter for subset of items matching one of the given PIDs
    String programme = "programme_example"; // String | filter for subset of items that are part of the given programme
    String q = "q_example"; // String | filter for subset of items matching supplied keyword/phrase (boolean operators permitted)
    String segmentEvent = "segmentEvent_example"; // String | filter for item with the given segment_event
    try {
      Nitro result = apiInstance.listItems(sort, sortDirection, mixin, authority, id, idType, itemType, page, pageSize, partnerId, partnerPid, people, pid, programme, q, segmentEvent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#listItems");
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
| **sort** | **String**| Sorts: * pid: sort by pid, descending  | [optional] [enum: pid] |
| **sortDirection** | **String**| Sort direction | [optional] [enum: descending] |
| **mixin** | [**List&lt;String&gt;**](String.md)| Mixins: * contributions: mixin to return information about contributors to items * images: mixin to add image information for an item * offset: mixin to return programme segment offsets, works in conjunction with programme filter * play_event: mixin to return programme segment events, works in conjunction with programme or segment_event filters  | [optional] [enum: contributions, images, offset, play_event] |
| **authority** | **String**| filter for subset of items that have an ID issued by the given authority | [optional] |
| **id** | [**List&lt;String&gt;**](String.md)| filter for subset of items having given ID | [optional] |
| **idType** | **String**| filter for subset of items that have given an ID of the given type | [optional] |
| **itemType** | [**List&lt;String&gt;**](String.md)| filter for specific type(s) of items | [optional] [enum: chapter, highlight, music, speech, other] |
| **page** | **Integer**| which page of results to return | [optional] [default to 1] |
| **pageSize** | **Integer**| number of results in each page | [optional] [default to 10] |
| **partnerId** | [**List&lt;String&gt;**](String.md)| filter for items by partner ID | [optional] |
| **partnerPid** | [**List&lt;String&gt;**](String.md)| filter for items by partner PID | [optional] |
| **people** | **String**| filter for subset of items that have specified person involved | [optional] |
| **pid** | [**List&lt;String&gt;**](String.md)| filter for subset of items matching one of the given PIDs | [optional] |
| **programme** | **String**| filter for subset of items that are part of the given programme | [optional] |
| **q** | **String**| filter for subset of items matching supplied keyword/phrase (boolean operators permitted) | [optional] |
| **segmentEvent** | **String**| filter for item with the given segment_event | [optional] |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |
| **0** | Unexpected error |  -  |

<a id="listMasterbrands"></a>
# **listMasterbrands**
> Nitro listMasterbrands(sort, sortDirection, mixin, mid, page, pageSize, partnerId, partnerPid, q)

List all Master Brands

List all Master Brands

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    String sort = "mid"; // String | Sorts: * mid: sort by mid, ascending 
    String sortDirection = "ascending"; // String | Sort direction
    List<String> mixin = Arrays.asList(); // List<String> | Mixins: * images: mixin to add image information for a masterbrand 
    List<String> mid = Arrays.asList(); // List<String> | filter for subset of masterbrands that have given identifier
    Integer page = 1; // Integer | which page of results to return
    Integer pageSize = 10; // Integer | number of results in each page
    List<String> partnerId = Arrays.asList(); // List<String> | filter for masterbrands by partner ID
    List<String> partnerPid = Arrays.asList(""s0000001""); // List<String> | filter for masterbrands by partner PID
    String q = "q_example"; // String | filter for subset of masterbrands matching supplied keyword/phrase (boolean operators permitted)
    try {
      Nitro result = apiInstance.listMasterbrands(sort, sortDirection, mixin, mid, page, pageSize, partnerId, partnerPid, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#listMasterbrands");
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
| **sort** | **String**| Sorts: * mid: sort by mid, ascending  | [optional] [enum: mid] |
| **sortDirection** | **String**| Sort direction | [optional] [enum: ascending] |
| **mixin** | [**List&lt;String&gt;**](String.md)| Mixins: * images: mixin to add image information for a masterbrand  | [optional] [enum: images] |
| **mid** | [**List&lt;String&gt;**](String.md)| filter for subset of masterbrands that have given identifier | [optional] |
| **page** | **Integer**| which page of results to return | [optional] [default to 1] |
| **pageSize** | **Integer**| number of results in each page | [optional] [default to 10] |
| **partnerId** | [**List&lt;String&gt;**](String.md)| filter for masterbrands by partner ID | [optional] |
| **partnerPid** | [**List&lt;String&gt;**](String.md)| filter for masterbrands by partner PID | [optional] |
| **q** | **String**| filter for subset of masterbrands matching supplied keyword/phrase (boolean operators permitted) | [optional] |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |
| **0** | Unexpected error |  -  |

<a id="listPeople"></a>
# **listPeople**
> Nitro listPeople(authority, hasExternalId, id, idType, page, pageSize, partnerId, partnerPid, pid, programme, q)

Find the people behind and in programmes: cast, crew, guests and more

The People feed allows you to search for the people and groups that contribute to programmes. This is the starting point for cast and crew credits, as well as finding contributors using external IDs (such as Wikipedia URLs)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    String authority = "authority_example"; // String | filter for subset of people that have an ID issued by the given authority
    List<String> hasExternalId = Arrays.asList(); // List<String> | filter for people who have an external identifier
    List<String> id = Arrays.asList(); // List<String> | filter for subset of people having given ID
    String idType = "idType_example"; // String | filter for subset of people that have given an ID of the given type
    Integer page = 1; // Integer | which page of results to return
    Integer pageSize = 10; // Integer | number of results in each page
    List<String> partnerId = Arrays.asList(); // List<String> | filter for people by partner ID
    List<String> partnerPid = Arrays.asList(""s0000001""); // List<String> | filter for people by partner PID
    List<String> pid = Arrays.asList(); // List<String> | filter for subset of people having given PID
    String programme = "programme_example"; // String | filter for subset of people that have contributed to the given programme pid
    String q = "q_example"; // String | filter for subset of people matching supplied keyword/phrase (boolean operators permitted)
    try {
      Nitro result = apiInstance.listPeople(authority, hasExternalId, id, idType, page, pageSize, partnerId, partnerPid, pid, programme, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#listPeople");
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
| **authority** | **String**| filter for subset of people that have an ID issued by the given authority | [optional] |
| **hasExternalId** | [**List&lt;String&gt;**](String.md)| filter for people who have an external identifier | [optional] [enum: true, false] |
| **id** | [**List&lt;String&gt;**](String.md)| filter for subset of people having given ID | [optional] |
| **idType** | **String**| filter for subset of people that have given an ID of the given type | [optional] |
| **page** | **Integer**| which page of results to return | [optional] [default to 1] |
| **pageSize** | **Integer**| number of results in each page | [optional] [default to 10] |
| **partnerId** | [**List&lt;String&gt;**](String.md)| filter for people by partner ID | [optional] |
| **partnerPid** | [**List&lt;String&gt;**](String.md)| filter for people by partner PID | [optional] |
| **pid** | [**List&lt;String&gt;**](String.md)| filter for subset of people having given PID | [optional] |
| **programme** | **String**| filter for subset of people that have contributed to the given programme pid | [optional] |
| **q** | **String**| filter for subset of people matching supplied keyword/phrase (boolean operators permitted) | [optional] |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |
| **0** | Unexpected error |  -  |

<a id="listPips"></a>
# **listPips**
> Nitro listPips(page, pageSize, q)

Look inside pips entities

Look inside pips entities

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    Integer page = 1; // Integer | which page of results to return
    Integer pageSize = 10; // Integer | number of results in each page
    String q = "q_example"; // String | filter for subset of programmes matching supplied keyword/phrase (boolean operators permitted)
    try {
      Nitro result = apiInstance.listPips(page, pageSize, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#listPips");
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
| **page** | **Integer**| which page of results to return | [optional] [default to 1] |
| **pageSize** | **Integer**| number of results in each page | [optional] [default to 10] |
| **q** | **String**| filter for subset of programmes matching supplied keyword/phrase (boolean operators permitted) | [optional] |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |
| **0** | Unexpected error |  -  |

<a id="listProgrammeDetails"></a>
# **listProgrammeDetails**
> Nitro listProgrammeDetails(page, pageSize, partnerPid, pid)

Exposes programme information for a single pid

Exposes programme information for a single pid

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    Integer page = 1; // Integer | which page of results to return
    Integer pageSize = 10; // Integer | number of results in each page
    String partnerPid = "partnerPid_example"; // String | Filter for programme information by partner PID
    String pid = "pid_example"; // String | Filter for programme information for the provided PID
    try {
      Nitro result = apiInstance.listProgrammeDetails(page, pageSize, partnerPid, pid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#listProgrammeDetails");
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
| **page** | **Integer**| which page of results to return | [optional] [default to 1] |
| **pageSize** | **Integer**| number of results in each page | [optional] [default to 10] |
| **partnerPid** | **String**| Filter for programme information by partner PID | [optional] |
| **pid** | **String**| Filter for programme information for the provided PID | [optional] |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |
| **0** | Unexpected error |  -  |

<a id="listProgrammes"></a>
# **listProgrammes**
> Nitro listProgrammes(sort, sortDirection, mixin, audioDescribed, availability, availabilityEntityType, availabilityFrom, availabilityType, childrenOf, descendantsOf, duration, entityType, format, genre, group, initialLetter, initialLetterEnd, initialLetterStart, initialLetterStrict, item, masterBrand, mediaSet, mediaType, page, pageSize, partnerId, partnerPid, paymentType, people, pid, promotedFor, q, signed, tagName, tagScheme, tleo, version, embargoed)

Start here for programmes metadata: Brands, Series, Episodes and Clips

Fetch metadata about Programmes (brands, series, episodes, clips). By applying different filter restrictions this feed can be used in many ways, for example to retrieve all series belonging to a brand, all the episodes and/or clips for a specific series, or any TLEO objects for a masterbrand. Other filters permit restricting to specific formats and/or genres, and you can request specific versions (for example Signed or Audio-Described). Parameters may be combined in any way suitable for your application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    String sort = "group_position"; // String | Sorts: * group_position: sort numerically by position in group, ascending * pid: sort alphabetically by PID, descending * position: sort numerically by position, ascending * promotion: sort by promotion rank, ascending * release_date: sort chronologically by release date, descending * relevance: sort by weighting of search term (use with q parameter) * scheduled_start: sort chronologically by scheduled start time/date, ascending * strict_title: sort alphabetically by title, ascending * title: sort by title librarian style (ignoring leading 'The', 'A', etc), ascending * tree: sort by root pid and then preorder tree sort. Requires entities to have release date. 
    String sortDirection = "ascending"; // String | Sort direction
    List<String> mixin = Arrays.asList(); // List<String> | Mixins: * alternate_images: mixin to return the alternate images for a programme * ancestor_titles: mixin to return ancestor programme titles * availability: mixin to return programme availability information * available_simulcasts: mixin to return information about programmes that are currently available as simulcasts * available_versions: mixin to return information about programmes that are currently available on demand * available_webcasts: mixin to return information about programmes that are currently available as webcasts * contributions: mixin to return information about contributors to a programme * duration: mixin to return original version duration in programme concept entities * genre_groupings: mixin to return list of genre groupings * genre_groups: mixin to return list of genre groups * images: mixin to add image information for a programme * is_embeddable: mixin to add embeddable information for a programme * previous_next: mixin to return the programmes which appear before and after a programme (as determined by the sort applied in the request) * programme_type: mixin to return the programme type * related_links: mixin to return information about related links to a programme * titles: mixin to return ancestor programme titles * versions_availability: mixin to return information about programmes that are currently available 
    List<String> audioDescribed = Arrays.asList(); // List<String> | filter for subset of programmes that are audio-described
    List<String> availability = Arrays.asList(); // List<String> | filter for subset of programmes that have availability
    List<String> availabilityEntityType = Arrays.asList(); // List<String> | additional filter when availability=available
    OffsetDateTime availabilityFrom = OffsetDateTime.now(); // OffsetDateTime | filter for subset of programmes that are available after or at the specified datetime
    List<String> availabilityType = Arrays.asList(); // List<String> | filter for a subset of programmes that are available for a given type
    List<String> childrenOf = Arrays.asList(); // List<String> | filter for subset of programmes that have PID as immediate parent
    List<String> descendantsOf = Arrays.asList(); // List<String> | filter for subset of programmes that have PID as ancestor
    List<String> duration = Arrays.asList(); // List<String> | filter for subset of programmes that have given duration
    List<String> entityType = Arrays.asList(); // List<String> | filter for subset of programmes that have given entity type
    List<String> format = Arrays.asList(); // List<String> | filter for subset of programmes with format
    List<String> genre = Arrays.asList(); // List<String> | filter for subset of programmes with genre
    String group = "group_example"; // String | filter for subset of programmes which belong to the given group pid
    String initialLetter = "initialLetter_example"; // String | filter for subset of programmes with title beginning with initial letter librarian style (ignoring leading 'The', 'An' (Welsh), etc) 0-9 a-z
    String initialLetterEnd = "initialLetterEnd_example"; // String | Programmes with (librarian) titles whose initial letter is equal/before given letter. Use with initial_letter_start for a range
    String initialLetterStart = "initialLetterStart_example"; // String | Programmes with (librarian) titles whose initial letter is equal/after given letter. Use with initial_letter_end for range.
    List<String> initialLetterStrict = Arrays.asList(); // List<String> | filter for subset of programmes with title beginning with initial letter
    List<String> item = Arrays.asList(); // List<String> | filter for subset of programmes with linked to versions which have the given item pids
    List<String> masterBrand = Arrays.asList(); // List<String> | filter for subset of programmes with master_brand
    String mediaSet = "mediaSet_example"; // String | filter for subset of programmes with media set
    List<String> mediaType = Arrays.asList(); // List<String> | filter for subset of programmes with media type
    Integer page = 1; // Integer | which page of results to return
    Integer pageSize = 10; // Integer | number of results in each page
    List<String> partnerId = Arrays.asList(); // List<String> | filter for programmes by partner ID
    List<String> partnerPid = Arrays.asList(""s0000001""); // List<String> | filter for programmes by partner PID
    List<String> paymentType = Arrays.asList(); // List<String> | filter for a subset of programmes that are of the given payment_type
    String people = "people_example"; // String | filter for subset of programmes with contributions by given people PID
    List<String> pid = Arrays.asList(); // List<String> | filter for subset of programmes having given PID
    String promotedFor = "promotedFor_example"; // String | filter for subset of programmes which are promoted for given service
    String q = "q_example"; // String | filter for subset of programmes matching supplied keyword/phrase (boolean operators permitted)
    List<String> signed = Arrays.asList(); // List<String> | filter for subset of programmes that are signed
    String tagName = "tagName_example"; // String | filter for subset of programmes with tag
    String tagScheme = "tagScheme_example"; // String | filter for subset of programmes with a tag
    List<String> tleo = Arrays.asList(); // List<String> | filter for subset of programmes that are TLEOs
    List<String> version = Arrays.asList(); // List<String> | filter for subset of programmes with given PID as one of their versions
    String embargoed = "include"; // String | Control return of embargoed items (undocumented)
    try {
      Nitro result = apiInstance.listProgrammes(sort, sortDirection, mixin, audioDescribed, availability, availabilityEntityType, availabilityFrom, availabilityType, childrenOf, descendantsOf, duration, entityType, format, genre, group, initialLetter, initialLetterEnd, initialLetterStart, initialLetterStrict, item, masterBrand, mediaSet, mediaType, page, pageSize, partnerId, partnerPid, paymentType, people, pid, promotedFor, q, signed, tagName, tagScheme, tleo, version, embargoed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#listProgrammes");
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
| **sort** | **String**| Sorts: * group_position: sort numerically by position in group, ascending * pid: sort alphabetically by PID, descending * position: sort numerically by position, ascending * promotion: sort by promotion rank, ascending * release_date: sort chronologically by release date, descending * relevance: sort by weighting of search term (use with q parameter) * scheduled_start: sort chronologically by scheduled start time/date, ascending * strict_title: sort alphabetically by title, ascending * title: sort by title librarian style (ignoring leading &#39;The&#39;, &#39;A&#39;, etc), ascending * tree: sort by root pid and then preorder tree sort. Requires entities to have release date.  | [optional] [enum: group_position, pid, position, promotion, release_date, relevance, scheduled_start, strict_title, title, tree] |
| **sortDirection** | **String**| Sort direction | [optional] [enum: ascending, descending] |
| **mixin** | [**List&lt;String&gt;**](String.md)| Mixins: * alternate_images: mixin to return the alternate images for a programme * ancestor_titles: mixin to return ancestor programme titles * availability: mixin to return programme availability information * available_simulcasts: mixin to return information about programmes that are currently available as simulcasts * available_versions: mixin to return information about programmes that are currently available on demand * available_webcasts: mixin to return information about programmes that are currently available as webcasts * contributions: mixin to return information about contributors to a programme * duration: mixin to return original version duration in programme concept entities * genre_groupings: mixin to return list of genre groupings * genre_groups: mixin to return list of genre groups * images: mixin to add image information for a programme * is_embeddable: mixin to add embeddable information for a programme * previous_next: mixin to return the programmes which appear before and after a programme (as determined by the sort applied in the request) * programme_type: mixin to return the programme type * related_links: mixin to return information about related links to a programme * titles: mixin to return ancestor programme titles * versions_availability: mixin to return information about programmes that are currently available  | [optional] [enum: alternate_images, ancestor_titles, availability, available_simulcasts, available_versions, available_webcasts, contributions, duration, genre_groupings, genre_groups, images, is_embeddable, previous_next, programme_type, related_links, titles, versions_availability] |
| **audioDescribed** | [**List&lt;String&gt;**](String.md)| filter for subset of programmes that are audio-described | [optional] [enum: true, false] |
| **availability** | [**List&lt;String&gt;**](String.md)| filter for subset of programmes that have availability | [optional] [enum: available, pending] |
| **availabilityEntityType** | [**List&lt;String&gt;**](String.md)| additional filter when availability&#x3D;available | [optional] [enum: episode, clip] |
| **availabilityFrom** | **OffsetDateTime**| filter for subset of programmes that are available after or at the specified datetime | [optional] |
| **availabilityType** | [**List&lt;String&gt;**](String.md)| filter for a subset of programmes that are available for a given type | [optional] [enum: ondemand, webcast, simulcast] |
| **childrenOf** | [**List&lt;String&gt;**](String.md)| filter for subset of programmes that have PID as immediate parent | [optional] |
| **descendantsOf** | [**List&lt;String&gt;**](String.md)| filter for subset of programmes that have PID as ancestor | [optional] |
| **duration** | [**List&lt;String&gt;**](String.md)| filter for subset of programmes that have given duration | [optional] [enum: short, medium, long] |
| **entityType** | [**List&lt;String&gt;**](String.md)| filter for subset of programmes that have given entity type | [optional] [enum: brand, series, episode, clip] |
| **format** | [**List&lt;String&gt;**](String.md)| filter for subset of programmes with format | [optional] |
| **genre** | [**List&lt;String&gt;**](String.md)| filter for subset of programmes with genre | [optional] |
| **group** | **String**| filter for subset of programmes which belong to the given group pid | [optional] |
| **initialLetter** | **String**| filter for subset of programmes with title beginning with initial letter librarian style (ignoring leading &#39;The&#39;, &#39;An&#39; (Welsh), etc) 0-9 a-z | [optional] |
| **initialLetterEnd** | **String**| Programmes with (librarian) titles whose initial letter is equal/before given letter. Use with initial_letter_start for a range | [optional] |
| **initialLetterStart** | **String**| Programmes with (librarian) titles whose initial letter is equal/after given letter. Use with initial_letter_end for range. | [optional] |
| **initialLetterStrict** | [**List&lt;String&gt;**](String.md)| filter for subset of programmes with title beginning with initial letter | [optional] |
| **item** | [**List&lt;String&gt;**](String.md)| filter for subset of programmes with linked to versions which have the given item pids | [optional] |
| **masterBrand** | [**List&lt;String&gt;**](String.md)| filter for subset of programmes with master_brand | [optional] |
| **mediaSet** | **String**| filter for subset of programmes with media set | [optional] |
| **mediaType** | [**List&lt;String&gt;**](String.md)| filter for subset of programmes with media type | [optional] [enum: audio, audio_video] |
| **page** | **Integer**| which page of results to return | [optional] [default to 1] |
| **pageSize** | **Integer**| number of results in each page | [optional] [default to 10] |
| **partnerId** | [**List&lt;String&gt;**](String.md)| filter for programmes by partner ID | [optional] |
| **partnerPid** | [**List&lt;String&gt;**](String.md)| filter for programmes by partner PID | [optional] |
| **paymentType** | [**List&lt;String&gt;**](String.md)| filter for a subset of programmes that are of the given payment_type | [optional] [enum: free, bbcstore, uscansvod] |
| **people** | **String**| filter for subset of programmes with contributions by given people PID | [optional] |
| **pid** | [**List&lt;String&gt;**](String.md)| filter for subset of programmes having given PID | [optional] |
| **promotedFor** | **String**| filter for subset of programmes which are promoted for given service | [optional] |
| **q** | **String**| filter for subset of programmes matching supplied keyword/phrase (boolean operators permitted) | [optional] |
| **signed** | [**List&lt;String&gt;**](String.md)| filter for subset of programmes that are signed | [optional] [enum: exclusive, inclusive, exclude] |
| **tagName** | **String**| filter for subset of programmes with tag | [optional] |
| **tagScheme** | **String**| filter for subset of programmes with a tag | [optional] |
| **tleo** | [**List&lt;String&gt;**](String.md)| filter for subset of programmes that are TLEOs | [optional] [enum: true, false] |
| **version** | [**List&lt;String&gt;**](String.md)| filter for subset of programmes with given PID as one of their versions | [optional] |
| **embargoed** | **String**| Control return of embargoed items (undocumented) | [optional] [enum: include, exclude, only] |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |
| **0** | Unexpected error |  -  |

<a id="listPromotions"></a>
# **listPromotions**
> Nitro listPromotions(mixin, context, page, pageSize, partnerId, partnerPid, pid, promotedBy, promotedFor, q, status)

Discover metadata for content promotions

Details of short-term editorially curated \&quot;promotions\&quot;, for instance those programmes featured on iPlayer today

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    List<String> mixin = Arrays.asList(); // List<String> | Mixins: * related_links: mixin to return information about related links to a promotion 
    String context = "context_example"; // String | filter for subset of promotions belonging to a given context
    Integer page = 1; // Integer | which page of results to return
    Integer pageSize = 10; // Integer | number of results in each page
    List<String> partnerId = Arrays.asList(); // List<String> | filter for promotions by partner ID
    List<String> partnerPid = Arrays.asList(""s0000001""); // List<String> | filter for promotions by partner PID
    List<String> pid = Arrays.asList(); // List<String> | filter for subset of promotions having given PID
    List<String> promotedBy = Arrays.asList(); // List<String> | filter for subset of promotions having given promoted by
    List<String> promotedFor = Arrays.asList(); // List<String> | filter for subset of promotions having given promoted for
    String q = "q_example"; // String | filter for subset of promotions matching supplied keyword/phrase (boolean operators permitted)
    List<String> status = Arrays.asList(); // List<String> | filter for subset of promotions with status
    try {
      Nitro result = apiInstance.listPromotions(mixin, context, page, pageSize, partnerId, partnerPid, pid, promotedBy, promotedFor, q, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#listPromotions");
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
| **mixin** | [**List&lt;String&gt;**](String.md)| Mixins: * related_links: mixin to return information about related links to a promotion  | [optional] [enum: related_links] |
| **context** | **String**| filter for subset of promotions belonging to a given context | [optional] |
| **page** | **Integer**| which page of results to return | [optional] [default to 1] |
| **pageSize** | **Integer**| number of results in each page | [optional] [default to 10] |
| **partnerId** | [**List&lt;String&gt;**](String.md)| filter for promotions by partner ID | [optional] |
| **partnerPid** | [**List&lt;String&gt;**](String.md)| filter for promotions by partner PID | [optional] |
| **pid** | [**List&lt;String&gt;**](String.md)| filter for subset of promotions having given PID | [optional] |
| **promotedBy** | [**List&lt;String&gt;**](String.md)| filter for subset of promotions having given promoted by | [optional] |
| **promotedFor** | [**List&lt;String&gt;**](String.md)| filter for subset of promotions having given promoted for | [optional] |
| **q** | **String**| filter for subset of promotions matching supplied keyword/phrase (boolean operators permitted) | [optional] |
| **status** | [**List&lt;String&gt;**](String.md)| filter for subset of promotions with status | [optional] [enum: current] |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |
| **0** | Unexpected error |  -  |

<a id="listSchedules"></a>
# **listSchedules**
> Nitro listSchedules(sort, sortDirection, mixin, authority, descendantsOf, endFrom, endTo, format, genre, group, id, idType, item, page, pageSize, partnerId, partnerPid, people, pid, q, repeat, scheduleDay, scheduleDayFrom, scheduleDayTo, serviceMasterBrand, sid, startFrom, startTo, version)

Build schedules and find metadata for TV and radio broadcasts and webcasts

Dates, Times, Schedules: when and where are programmes being shown?

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    String sort = "start_date"; // String | Sorts: * start_date: sort chronologically by scheduled start time/date, ascending 
    String sortDirection = "ascending"; // String | Sort direction
    List<String> mixin = Arrays.asList(); // List<String> | Mixins: * ancestor_titles: return ancestor programme titles * images: mixin to add image information for broadcasts and webcasts * titles: return ancestor programme titles 
    List<String> authority = Arrays.asList(); // List<String> | filter for subset of broadcasts and webcasts that have given authority
    List<String> descendantsOf = Arrays.asList(); // List<String> | filter for subset of broadcasts and webcasts that are descendants of the given programme PID
    OffsetDateTime endFrom = OffsetDateTime.now(); // OffsetDateTime | filter for subset of broadcasts and webcasts that end on or later than the specified datetime
    OffsetDateTime endTo = OffsetDateTime.now(); // OffsetDateTime | filter for subset of broadcasts and webcasts that end on or earlier than the specified datetime
    List<String> format = Arrays.asList(); // List<String> | filter for subset of broadcasts and webcasts that are classified in the given format ID
    List<String> genre = Arrays.asList(); // List<String> | filter for subset of broadcasts and webcasts that are classified in the given genre ID
    String group = "group_example"; // String | filter for subset of broadcasts and webcasts that have programmes in the given group
    List<String> id = Arrays.asList(); // List<String> | filter for subset of broadcasts and webcasts that have given identifier
    List<String> idType = Arrays.asList(); // List<String> | filter for subset of broadcasts and webcasts that have given id type
    List<String> item = Arrays.asList(); // List<String> | filter for subset of broadcasts and webcasts with the given item performed on it
    Integer page = 1; // Integer | which page of results to return
    Integer pageSize = 10; // Integer | number of results in each page
    List<String> partnerId = Arrays.asList(); // List<String> | filter for broadcasts and webcasts by partner ID
    List<String> partnerPid = Arrays.asList(""s0000001""); // List<String> | filter for broadcasts and webcasts by partner PID
    String people = "people_example"; // String | filter for subset of broadcasts and webcasts that have given contributor
    List<String> pid = Arrays.asList(); // List<String> | filter for subset of broadcasts and webcasts having given PID
    String q = "q_example"; // String | filter for subset of broadcasts and webcasts matching supplied keyword/phrase (boolean operators permitted)
    Boolean repeat = true; // Boolean | filter to show either only repeats or non-repeats
    LocalDate scheduleDay = LocalDate.now(); // LocalDate | filter for subset of broadcasts and webcasts that start on the specified day (BBC time)
    LocalDate scheduleDayFrom = LocalDate.now(); // LocalDate | filter for subset of broadcasts and webcasts that start on or after the specified day (BBC time)
    LocalDate scheduleDayTo = LocalDate.now(); // LocalDate | filter for subset of broadcasts and webcasts that start on or before the specified day (BBC time)
    List<String> serviceMasterBrand = Arrays.asList(); // List<String> | filter for subset of broadcasts and webcasts with given service master brand
    List<String> sid = Arrays.asList(); // List<String> | filter for subset of broadcasts and webcasts that are on the specified linear service
    OffsetDateTime startFrom = OffsetDateTime.now(); // OffsetDateTime | filter for subset of broadcasts and webcasts that start on or later than the specified datetime
    OffsetDateTime startTo = OffsetDateTime.now(); // OffsetDateTime | filter for subset of broadcasts and webcasts that start on or earlier than the specified datetime
    List<String> version = Arrays.asList(); // List<String> | filter for subset of broadcasts and webcasts with given PID as their parent version
    try {
      Nitro result = apiInstance.listSchedules(sort, sortDirection, mixin, authority, descendantsOf, endFrom, endTo, format, genre, group, id, idType, item, page, pageSize, partnerId, partnerPid, people, pid, q, repeat, scheduleDay, scheduleDayFrom, scheduleDayTo, serviceMasterBrand, sid, startFrom, startTo, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#listSchedules");
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
| **sort** | **String**| Sorts: * start_date: sort chronologically by scheduled start time/date, ascending  | [optional] [enum: start_date] |
| **sortDirection** | **String**| Sort direction | [optional] [enum: ascending, descending] |
| **mixin** | [**List&lt;String&gt;**](String.md)| Mixins: * ancestor_titles: return ancestor programme titles * images: mixin to add image information for broadcasts and webcasts * titles: return ancestor programme titles  | [optional] [enum: ancestor_titles, images, titles] |
| **authority** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts and webcasts that have given authority | [optional] |
| **descendantsOf** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts and webcasts that are descendants of the given programme PID | [optional] |
| **endFrom** | **OffsetDateTime**| filter for subset of broadcasts and webcasts that end on or later than the specified datetime | [optional] |
| **endTo** | **OffsetDateTime**| filter for subset of broadcasts and webcasts that end on or earlier than the specified datetime | [optional] |
| **format** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts and webcasts that are classified in the given format ID | [optional] |
| **genre** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts and webcasts that are classified in the given genre ID | [optional] |
| **group** | **String**| filter for subset of broadcasts and webcasts that have programmes in the given group | [optional] |
| **id** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts and webcasts that have given identifier | [optional] |
| **idType** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts and webcasts that have given id type | [optional] |
| **item** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts and webcasts with the given item performed on it | [optional] |
| **page** | **Integer**| which page of results to return | [optional] [default to 1] |
| **pageSize** | **Integer**| number of results in each page | [optional] [default to 10] |
| **partnerId** | [**List&lt;String&gt;**](String.md)| filter for broadcasts and webcasts by partner ID | [optional] |
| **partnerPid** | [**List&lt;String&gt;**](String.md)| filter for broadcasts and webcasts by partner PID | [optional] |
| **people** | **String**| filter for subset of broadcasts and webcasts that have given contributor | [optional] |
| **pid** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts and webcasts having given PID | [optional] |
| **q** | **String**| filter for subset of broadcasts and webcasts matching supplied keyword/phrase (boolean operators permitted) | [optional] |
| **repeat** | **Boolean**| filter to show either only repeats or non-repeats | [optional] |
| **scheduleDay** | **LocalDate**| filter for subset of broadcasts and webcasts that start on the specified day (BBC time) | [optional] |
| **scheduleDayFrom** | **LocalDate**| filter for subset of broadcasts and webcasts that start on or after the specified day (BBC time) | [optional] |
| **scheduleDayTo** | **LocalDate**| filter for subset of broadcasts and webcasts that start on or before the specified day (BBC time) | [optional] |
| **serviceMasterBrand** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts and webcasts with given service master brand | [optional] |
| **sid** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts and webcasts that are on the specified linear service | [optional] |
| **startFrom** | **OffsetDateTime**| filter for subset of broadcasts and webcasts that start on or later than the specified datetime | [optional] |
| **startTo** | **OffsetDateTime**| filter for subset of broadcasts and webcasts that start on or earlier than the specified datetime | [optional] |
| **version** | [**List&lt;String&gt;**](String.md)| filter for subset of broadcasts and webcasts with given PID as their parent version | [optional] |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |
| **0** | Unexpected error |  -  |

<a id="listServices"></a>
# **listServices**
> Nitro listServices(endFrom, endTo, mid, page, pageSize, partnerId, partnerPid, q, serviceType, sid, startFrom, startTo)

Information about the linear services used for broadcast transmissions

The services feed exposes the linear broadcast \&quot;services\&quot; from PIPs. These are the actual services which broadcast programmes (eg bbc_one_oxford is the service for BBC One in Oxford).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    OffsetDateTime endFrom = OffsetDateTime.now(); // OffsetDateTime | Return services that end on or later than the specified datetime
    OffsetDateTime endTo = OffsetDateTime.now(); // OffsetDateTime | filter for subset of broadcasts that end on or earlier than the specified datetime
    List<String> mid = Arrays.asList(); // List<String> | filter for services by masterbrand MID
    Integer page = 1; // Integer | which page of results to return
    Integer pageSize = 10; // Integer | number of results in each page
    List<String> partnerId = Arrays.asList(); // List<String> | filter for services by partner ID
    List<String> partnerPid = Arrays.asList(""s0000001""); // List<String> | filter for services by partner PID
    String q = "q_example"; // String | filter for subset of services matching supplied keyword/phrase (boolean operators permitted)
    List<String> serviceType = Arrays.asList(); // List<String> | filter for specified type of linear services
    List<String> sid = Arrays.asList(); // List<String> | filter for specified linear service
    OffsetDateTime startFrom = OffsetDateTime.now(); // OffsetDateTime | Return services that start on or later than the specified datetime
    OffsetDateTime startTo = OffsetDateTime.now(); // OffsetDateTime | Return services that start earlier than the specified datetime
    try {
      Nitro result = apiInstance.listServices(endFrom, endTo, mid, page, pageSize, partnerId, partnerPid, q, serviceType, sid, startFrom, startTo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#listServices");
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
| **endFrom** | **OffsetDateTime**| Return services that end on or later than the specified datetime | [optional] |
| **endTo** | **OffsetDateTime**| filter for subset of broadcasts that end on or earlier than the specified datetime | [optional] |
| **mid** | [**List&lt;String&gt;**](String.md)| filter for services by masterbrand MID | [optional] |
| **page** | **Integer**| which page of results to return | [optional] [default to 1] |
| **pageSize** | **Integer**| number of results in each page | [optional] [default to 10] |
| **partnerId** | [**List&lt;String&gt;**](String.md)| filter for services by partner ID | [optional] |
| **partnerPid** | [**List&lt;String&gt;**](String.md)| filter for services by partner PID | [optional] |
| **q** | **String**| filter for subset of services matching supplied keyword/phrase (boolean operators permitted) | [optional] |
| **serviceType** | [**List&lt;String&gt;**](String.md)| filter for specified type of linear services | [optional] [enum: Interactive, Local Radio, Master Brand Only, National Radio, On Demand, Regional Radio, Simulcast, TV, Web Only, Webcast] |
| **sid** | [**List&lt;String&gt;**](String.md)| filter for specified linear service | [optional] |
| **startFrom** | **OffsetDateTime**| Return services that start on or later than the specified datetime | [optional] |
| **startTo** | **OffsetDateTime**| Return services that start earlier than the specified datetime | [optional] |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |
| **0** | Unexpected error |  -  |

<a id="listVersions"></a>
# **listVersions**
> Nitro listVersions(availability, descendantsOf, mediaSet, page, pageSize, partnerId, partnerPid, paymentType, pid, embargoed)

Metadata on editorial programme versions: original, signed, audio-described, etc

The versions feed exposes editorial \&quot;Versions\&quot; of programmes. These are concepts used to capture different presentations of an overall programme: for example, versions of a programme may include one with sign language, one with audio description, one edited for content and more. Versions are also important to understand for broadcasts: a linear broadcast or an ondemand is always of a specific version, not merely of a programme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    List<String> availability = Arrays.asList(); // List<String> | filter for subset of versions that have availability
    List<String> descendantsOf = Arrays.asList(); // List<String> | filter for subset of versions having given programme PID
    List<String> mediaSet = Arrays.asList(); // List<String> | filter for subset of versions with availability in the given media set
    Integer page = 1; // Integer | which page of results to return
    Integer pageSize = 10; // Integer | number of results in each page
    List<String> partnerId = Arrays.asList(); // List<String> | filter for versions by partner ID
    List<String> partnerPid = Arrays.asList(""s0000001""); // List<String> | filter for versions by partner PID
    List<String> paymentType = Arrays.asList(); // List<String> | filter for a subset of versions that are of the given payment_type
    List<String> pid = Arrays.asList(); // List<String> | filter for subset of versions having given PID
    String embargoed = "include"; // String | Control return of embargoed items (undocumented)
    try {
      Nitro result = apiInstance.listVersions(availability, descendantsOf, mediaSet, page, pageSize, partnerId, partnerPid, paymentType, pid, embargoed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#listVersions");
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
| **availability** | [**List&lt;String&gt;**](String.md)| filter for subset of versions that have availability | [optional] [enum: available] |
| **descendantsOf** | [**List&lt;String&gt;**](String.md)| filter for subset of versions having given programme PID | [optional] |
| **mediaSet** | [**List&lt;String&gt;**](String.md)| filter for subset of versions with availability in the given media set | [optional] |
| **page** | **Integer**| which page of results to return | [optional] [default to 1] |
| **pageSize** | **Integer**| number of results in each page | [optional] [default to 10] |
| **partnerId** | [**List&lt;String&gt;**](String.md)| filter for versions by partner ID | [optional] |
| **partnerPid** | [**List&lt;String&gt;**](String.md)| filter for versions by partner PID | [optional] |
| **paymentType** | [**List&lt;String&gt;**](String.md)| filter for a subset of versions that are of the given payment_type | [optional] [enum: free, bbcstore, uscansvod] |
| **pid** | [**List&lt;String&gt;**](String.md)| filter for subset of versions having given PID | [optional] |
| **embargoed** | **String**| Control return of embargoed items (undocumented) | [optional] [enum: include, exclude, only] |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |
| **0** | Unexpected error |  -  |

