# DiscoveryresourcesApi

All URIs are relative to *http://channel4.com/pmlsd*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**aToZLandingFeed**](DiscoveryresourcesApi.md#aToZLandingFeed) | **GET** /atoz.atom | A to Z Landing Feed |
| [**aToZLetterFeed**](DiscoveryresourcesApi.md#aToZLetterFeed) | **GET** /atoz/{start_letter}.atom | A to Z Letter Feed |
| [**aToZLetterFeed2**](DiscoveryresourcesApi.md#aToZLetterFeed2) | **GET** /atoz/{start_letter}/page-{pageno}.atom | A to Z Letter Feed(2) |
| [**allProgrammesByTXDate**](DiscoveryresourcesApi.md#allProgrammesByTXDate) | **GET** /categories/{category}.atom | All Programmes by TX Date |
| [**allProgrammesByTXDate2**](DiscoveryresourcesApi.md#allProgrammesByTXDate2) | **GET** /categories/{category}/channel/{channel}.atom | All Programmes by TX Date(2) |
| [**allProgrammesByTXDate3**](DiscoveryresourcesApi.md#allProgrammesByTXDate3) | **GET** /categories/{category}/derived/ad.atom | All Programmes by TX Date(3) |
| [**allProgrammesByTXDate4**](DiscoveryresourcesApi.md#allProgrammesByTXDate4) | **GET** /categories/{category}/page-{pageno}.atom | All Programmes by TX Date(4) |
| [**allProgrammesByTXDate5**](DiscoveryresourcesApi.md#allProgrammesByTXDate5) | **GET** /categories/{category}/channel/{channel}/page-{pageno}.atom | All Programmes by TX Date(5) |
| [**allProgrammesByTXDate6**](DiscoveryresourcesApi.md#allProgrammesByTXDate6) | **GET** /categories/{category}/derived/ad/page-{pageno}.atom | All Programmes by TX Date(6) |
| [**allProgrammesByTitle**](DiscoveryresourcesApi.md#allProgrammesByTitle) | **GET** /categories/{category}/title.atom | All Programmes by Title |
| [**allProgrammesByTitle2**](DiscoveryresourcesApi.md#allProgrammesByTitle2) | **GET** /categories/{category}/channel/{channel}/title.atom | All Programmes by Title(2) |
| [**allProgrammesByTitle3**](DiscoveryresourcesApi.md#allProgrammesByTitle3) | **GET** /categories/{category}/derived/ad/title.atom | All Programmes by Title(3) |
| [**allProgrammesByTitle4**](DiscoveryresourcesApi.md#allProgrammesByTitle4) | **GET** /categories/{category}/title/page-{pageno}.atom | All Programmes by Title(4) |
| [**allProgrammesByTitle5**](DiscoveryresourcesApi.md#allProgrammesByTitle5) | **GET** /categories/{category}/channel/{channel}/title/page-{pageno}.atom | All Programmes by Title(5) |
| [**allProgrammesByTitle6**](DiscoveryresourcesApi.md#allProgrammesByTitle6) | **GET** /categories/{category}/derived/ad/title/page-{pageno}.atom | All Programmes by Title(6) |
| [**call4oDBrowseByDateFeed**](DiscoveryresourcesApi.md#call4oDBrowseByDateFeed) | **GET** /4od/episode-list/date/{yyyy}/{mm}/{dd}.atom | 4oD Browse by Date Feed |
| [**call4oDClipsCatchUpFeed**](DiscoveryresourcesApi.md#call4oDClipsCatchUpFeed) | **GET** /4od/recently-added/videos.atom | 4oD Clips Catch Up Feed |
| [**call4oDMostPopularEpisodesFeed**](DiscoveryresourcesApi.md#call4oDMostPopularEpisodesFeed) | **GET** /4od/episode-list/popular.atom | 4oD Most Popular Episodes Feed |
| [**call4oDPopularAllBrandsFeed**](DiscoveryresourcesApi.md#call4oDPopularAllBrandsFeed) | **GET** /brands/4od/popular.atom | 4oD Popular All Brands Feed |
| [**call4oDPopularAllBrandsFeed2**](DiscoveryresourcesApi.md#call4oDPopularAllBrandsFeed2) | **GET** /brands/4od/popular/page-{pageno}.atom | 4oD Popular All Brands Feed(2) |
| [**call4oDProgrammesByTXDate**](DiscoveryresourcesApi.md#call4oDProgrammesByTXDate) | **GET** /categories/{category}/4od.atom | 4oD Programmes by TX Date |
| [**call4oDProgrammesByTXDate2**](DiscoveryresourcesApi.md#call4oDProgrammesByTXDate2) | **GET** /categories/{category}/channel/{channel}/4od.atom | 4oD Programmes by TX Date(2) |
| [**call4oDProgrammesByTXDate3**](DiscoveryresourcesApi.md#call4oDProgrammesByTXDate3) | **GET** /categories/{category}/derived/ad/4od.atom | 4oD Programmes by TX Date(3) |
| [**call4oDProgrammesByTXDate4**](DiscoveryresourcesApi.md#call4oDProgrammesByTXDate4) | **GET** /categories/{category}/4od/page-{pageno}.atom | 4oD Programmes by TX Date(4) |
| [**call4oDProgrammesByTXDate5**](DiscoveryresourcesApi.md#call4oDProgrammesByTXDate5) | **GET** /categories/{category}/channel/{channel}/4od/page-{pageno}.atom | 4oD Programmes by TX Date(5) |
| [**call4oDProgrammesByTXDate6**](DiscoveryresourcesApi.md#call4oDProgrammesByTXDate6) | **GET** /categories/{category}/derived/ad/4od/page-{pageno}.atom | 4oD Programmes by TX Date(6) |
| [**call4oDProgrammesByTitle**](DiscoveryresourcesApi.md#call4oDProgrammesByTitle) | **GET** /categories/{category}/4od/title.atom | 4oD Programmes by Title |
| [**call4oDProgrammesByTitle2**](DiscoveryresourcesApi.md#call4oDProgrammesByTitle2) | **GET** /categories/{category}/channel/{channel}/4od/title.atom | 4oD Programmes by Title(2) |
| [**call4oDProgrammesByTitle3**](DiscoveryresourcesApi.md#call4oDProgrammesByTitle3) | **GET** /categories/{category}/derived/ad/4od/title.atom | 4oD Programmes by Title(3) |
| [**call4oDProgrammesByTitle4**](DiscoveryresourcesApi.md#call4oDProgrammesByTitle4) | **GET** /categories/{category}/4od/title/page-{pageno}.atom | 4oD Programmes by Title(4) |
| [**call4oDProgrammesByTitle5**](DiscoveryresourcesApi.md#call4oDProgrammesByTitle5) | **GET** /categories/{category}/channel/{channel}/4od/title/page-{pageno}.atom | 4oD Programmes by Title(5) |
| [**call4oDProgrammesByTitle6**](DiscoveryresourcesApi.md#call4oDProgrammesByTitle6) | **GET** /categories/{category}/derived/ad/4od/title/page-{pageno}.atom | 4oD Programmes by Title(6) |
| [**call4oDTitleAllBrandsFeed**](DiscoveryresourcesApi.md#call4oDTitleAllBrandsFeed) | **GET** /brands/4od.atom | 4oD Title All Brands Feed |
| [**call4oDTitleAllBrandsFeed2**](DiscoveryresourcesApi.md#call4oDTitleAllBrandsFeed2) | **GET** /brands/4od/page-{pageno}.atom | 4oD Title All Brands Feed(2) |
| [**categoriesLandingFeed**](DiscoveryresourcesApi.md#categoriesLandingFeed) | **GET** /categories.atom | Categories Landing Feed |
| [**collectionsFeed**](DiscoveryresourcesApi.md#collectionsFeed) | **GET** /collections/{collection_name}/4od.atom | Collections Feed |
| [**collectionsFeed2**](DiscoveryresourcesApi.md#collectionsFeed2) | **GET** /collections/{collection_name}.atom | Collections Feed(2) |
| [**flattenedCollectionFeed**](DiscoveryresourcesApi.md#flattenedCollectionFeed) | **GET** /collections/{collection_name}/flattened/4od.atom | Flattened Collection Feed |
| [**flattenedCollectionFeed2**](DiscoveryresourcesApi.md#flattenedCollectionFeed2) | **GET** /collections/{collection_name}/flattened.atom | Flattened Collection Feed(2) |
| [**mostPopularBrandsFeed**](DiscoveryresourcesApi.md#mostPopularBrandsFeed) | **GET** /categories/{category}/4od/popular.atom | Most Popular Brands Feed |
| [**mostPopularBrandsFeed2**](DiscoveryresourcesApi.md#mostPopularBrandsFeed2) | **GET** /categories/{category}/popular.atom | Most Popular Brands Feed(2) |
| [**mostPopularBrandsFeed3**](DiscoveryresourcesApi.md#mostPopularBrandsFeed3) | **GET** /categories/{category}/channel/{channel}/4od/popular.atom | Most Popular Brands Feed(3) |
| [**mostPopularBrandsFeed4**](DiscoveryresourcesApi.md#mostPopularBrandsFeed4) | **GET** /categories/{category}/derived/ad/4od/popular.atom | Most Popular Brands Feed(4) |
| [**mostPopularBrandsFeed5**](DiscoveryresourcesApi.md#mostPopularBrandsFeed5) | **GET** /categories/{category}/4od/popular/page-{pageno}.atom | Most Popular Brands Feed(5) |
| [**mostPopularBrandsFeed6**](DiscoveryresourcesApi.md#mostPopularBrandsFeed6) | **GET** /categories/{category}/popular/page-{pageno}.atom | Most Popular Brands Feed(6) |
| [**mostPopularBrandsFeed7**](DiscoveryresourcesApi.md#mostPopularBrandsFeed7) | **GET** /categories/{category}/channel/{channel}/4od/popular/page-{pageno}.atom | Most Popular Brands Feed(7) |
| [**mostPopularBrandsFeed8**](DiscoveryresourcesApi.md#mostPopularBrandsFeed8) | **GET** /categories/{category}/derived/ad/4od/popular/page-{pageno}.atom | Most Popular Brands Feed(8) |
| [**popularBrandsFeed**](DiscoveryresourcesApi.md#popularBrandsFeed) | **GET** /brands/popular.atom | Popular Brands Feed |
| [**popularBrandsFeed2**](DiscoveryresourcesApi.md#popularBrandsFeed2) | **GET** /brands/popular/page-{pageno}.atom | Popular Brands Feed(2) |
| [**searchFeed**](DiscoveryresourcesApi.md#searchFeed) | **GET** /search.atom | Search Feed |
| [**searchFeed2**](DiscoveryresourcesApi.md#searchFeed2) | **GET** /search/{q}.atom | Search Feed(2) |
| [**searchFeed3**](DiscoveryresourcesApi.md#searchFeed3) | **GET** /search/page-{pageno}.atom | Search Feed(3) |
| [**searchFeed4**](DiscoveryresourcesApi.md#searchFeed4) | **GET** /search/{q}/page-{pageno}.atom | Search Feed(4) |
| [**tVListingsFeed**](DiscoveryresourcesApi.md#tVListingsFeed) | **GET** /tv-listings/daily/{yyyy}/{mm}/{dd}.atom | TV Listings Feed |
| [**tVListingsFeed2**](DiscoveryresourcesApi.md#tVListingsFeed2) | **GET** /tv-listings/daily/{yyyy}/{mm}/{dd}/{channel}.atom | TV Listings Feed(2) |


<a id="aToZLandingFeed"></a>
# **aToZLandingFeed**
> Atom aToZLandingFeed(platform)

A to Z Landing Feed

Lists Channel 4 programmes alphabetically from A to Z, providing the same    functionality and information as is available in the A to Z section of the    Channel 4 Programmes page, http://www.channel4.com/programmes.    http://api.channel4.com/pmlsd/atoz.atom    http://api.channel4.com/pmlsd/atoz.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.aToZLandingFeed(platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#aToZLandingFeed");
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
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="aToZLetterFeed"></a>
# **aToZLetterFeed**
> Atom aToZLetterFeed(startLetter, platform)

A to Z Letter Feed

Lists Channel 4 programmes whose names begin with the associated letter.    http://api.channel4.com/pmlsd/atoz/start_letter.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/atoz/a.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String startLetter = "startLetter_example"; // String | The letter of the alphabet for which you seek associated Channel 4 programmes
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.aToZLetterFeed(startLetter, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#aToZLetterFeed");
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
| **startLetter** | **String**| The letter of the alphabet for which you seek associated Channel 4 programmes | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="aToZLetterFeed2"></a>
# **aToZLetterFeed2**
> Atom aToZLetterFeed2(startLetter, pageno, platform)

A to Z Letter Feed(2)

Lists Channel 4 programmes whose names begin with the associated letter.    http://api.channel4.com/pmlsd/atoz/start_letter/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/atoz/a.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String startLetter = "startLetter_example"; // String | The letter of the alphabet for which you seek associated Channel 4 programmes
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.aToZLetterFeed2(startLetter, pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#aToZLetterFeed2");
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
| **startLetter** | **String**| The letter of the alphabet for which you seek associated Channel 4 programmes | |
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="allProgrammesByTXDate"></a>
# **allProgrammesByTXDate**
> Atom allProgrammesByTXDate(category, platform)

All Programmes by TX Date

Lists all Channel 4 programmes associated with the specified category (tag).     By default, the programmes are listed in order of Transmission (TX) Date,    with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.allProgrammesByTXDate(category, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#allProgrammesByTXDate");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="allProgrammesByTXDate2"></a>
# **allProgrammesByTXDate2**
> Atom allProgrammesByTXDate2(category, channel, platform)

All Programmes by TX Date(2)

Lists all Channel 4 programmes associated with the specified category (tag).     By default, the programmes are listed in order of Transmission (TX) Date,    with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/channel/[channel].atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String channel = "c4"; // String | The name of the channel for which you seek associated Channel 4oD programmes
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.allProgrammesByTXDate2(category, channel, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#allProgrammesByTXDate2");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **channel** | **String**| The name of the channel for which you seek associated Channel 4oD programmes | [enum: c4, f4, e4, m4, 4m, 4s] |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="allProgrammesByTXDate3"></a>
# **allProgrammesByTXDate3**
> Atom allProgrammesByTXDate3(category, platform)

All Programmes by TX Date(3)

Lists all Channel 4 programmes associated with the specified category (tag).     By default, the programmes are listed in order of Transmission (TX) Date,    with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/derived/ad.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.allProgrammesByTXDate3(category, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#allProgrammesByTXDate3");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="allProgrammesByTXDate4"></a>
# **allProgrammesByTXDate4**
> Atom allProgrammesByTXDate4(category, pageno, platform)

All Programmes by TX Date(4)

Lists all Channel 4 programmes associated with the specified category (tag).     By default, the programmes are listed in order of Transmission (TX) Date,    with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.allProgrammesByTXDate4(category, pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#allProgrammesByTXDate4");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="allProgrammesByTXDate5"></a>
# **allProgrammesByTXDate5**
> Atom allProgrammesByTXDate5(category, channel, pageno, platform)

All Programmes by TX Date(5)

Lists all Channel 4 programmes associated with the specified category (tag).     By default, the programmes are listed in order of Transmission (TX) Date,    with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/channel/[channel]/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String channel = "c4"; // String | The name of the channel for which you seek associated Channel 4oD programmes
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.allProgrammesByTXDate5(category, channel, pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#allProgrammesByTXDate5");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **channel** | **String**| The name of the channel for which you seek associated Channel 4oD programmes | [enum: c4, f4, e4, m4, 4m, 4s] |
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="allProgrammesByTXDate6"></a>
# **allProgrammesByTXDate6**
> Atom allProgrammesByTXDate6(category, pageno, platform)

All Programmes by TX Date(6)

Lists all Channel 4 programmes associated with the specified category (tag).     By default, the programmes are listed in order of Transmission (TX) Date,    with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/derived/ad/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.allProgrammesByTXDate6(category, pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#allProgrammesByTXDate6");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="allProgrammesByTitle"></a>
# **allProgrammesByTitle**
> Atom allProgrammesByTitle(category, platform)

All Programmes by Title

Lists all Channel 4 programmes associated with the specified category (tag),    alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/history/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.allProgrammesByTitle(category, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#allProgrammesByTitle");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="allProgrammesByTitle2"></a>
# **allProgrammesByTitle2**
> Atom allProgrammesByTitle2(category, channel, platform)

All Programmes by Title(2)

Lists all Channel 4 programmes associated with the specified category (tag),    alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/channel/[channel]/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/history/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String channel = "c4"; // String | The name of the channel for which you seek associated Channel 4oD programmes
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.allProgrammesByTitle2(category, channel, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#allProgrammesByTitle2");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **channel** | **String**| The name of the channel for which you seek associated Channel 4oD programmes | [enum: c4, f4, e4, m4, 4m, 4s] |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="allProgrammesByTitle3"></a>
# **allProgrammesByTitle3**
> Atom allProgrammesByTitle3(category, platform)

All Programmes by Title(3)

Lists all Channel 4 programmes associated with the specified category (tag),    alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/derived/ad/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/history/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.allProgrammesByTitle3(category, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#allProgrammesByTitle3");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="allProgrammesByTitle4"></a>
# **allProgrammesByTitle4**
> Atom allProgrammesByTitle4(category, pageno, platform)

All Programmes by Title(4)

Lists all Channel 4 programmes associated with the specified category (tag),    alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/title/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/history/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.allProgrammesByTitle4(category, pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#allProgrammesByTitle4");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="allProgrammesByTitle5"></a>
# **allProgrammesByTitle5**
> Atom allProgrammesByTitle5(category, channel, pageno, platform)

All Programmes by Title(5)

Lists all Channel 4 programmes associated with the specified category (tag),    alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/channel/[channel]/title/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/history/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String channel = "c4"; // String | The name of the channel for which you seek associated Channel 4oD programmes
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.allProgrammesByTitle5(category, channel, pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#allProgrammesByTitle5");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **channel** | **String**| The name of the channel for which you seek associated Channel 4oD programmes | [enum: c4, f4, e4, m4, 4m, 4s] |
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="allProgrammesByTitle6"></a>
# **allProgrammesByTitle6**
> Atom allProgrammesByTitle6(category, pageno, platform)

All Programmes by Title(6)

Lists all Channel 4 programmes associated with the specified category (tag),    alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/derived/ad/title/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/history/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.allProgrammesByTitle6(category, pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#allProgrammesByTitle6");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="call4oDBrowseByDateFeed"></a>
# **call4oDBrowseByDateFeed**
> Atom call4oDBrowseByDateFeed(yyyy, mm, dd, platform)

4oD Browse by Date Feed

Information of daily broadcast content available on 4oD, according to    broadcast date    http://api.channel4.com/pmlsd/4od/episode-list/date/[yyyy]/[mm]/[dd].atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/4od/episode-list/date/2010/11/28.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String yyyy = "yyyy_example"; // String | The date for which you wish to see programming information
    String mm = "mm_example"; // String | The date for which you wish to see programming information
    String dd = "dd_example"; // String | The date for which you wish to see programming information
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.call4oDBrowseByDateFeed(yyyy, mm, dd, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#call4oDBrowseByDateFeed");
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
| **yyyy** | **String**| The date for which you wish to see programming information | |
| **mm** | **String**| The date for which you wish to see programming information | |
| **dd** | **String**| The date for which you wish to see programming information | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="call4oDClipsCatchUpFeed"></a>
# **call4oDClipsCatchUpFeed**
> Atom call4oDClipsCatchUpFeed(platform)

4oD Clips Catch Up Feed

A feed containing metadata about short-form content relating to 4oD Episodes    recently added to 4oD based on linear transmission. The entries for the    Clips Landing Feed contain references to each short-form asset. It will    return up to 20 entries.    http://api.channel4.com/pmlsd/4od/recently-added/videos.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/4od/episode-list/videos.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.call4oDClipsCatchUpFeed(platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#call4oDClipsCatchUpFeed");
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
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="call4oDMostPopularEpisodesFeed"></a>
# **call4oDMostPopularEpisodesFeed**
> Atom call4oDMostPopularEpisodesFeed(platform)

4oD Most Popular Episodes Feed

Information of the most popular content available on 4oD, according to user    data driven.    http://api.channel4.com/pmlsd/4od/episode-list/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/4od/episode-list/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.call4oDMostPopularEpisodesFeed(platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#call4oDMostPopularEpisodesFeed");
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
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="call4oDPopularAllBrandsFeed"></a>
# **call4oDPopularAllBrandsFeed**
> Atom call4oDPopularAllBrandsFeed(platform)

4oD Popular All Brands Feed

Lists all Channel 4 programmes available on 4oD by popularity considering    the data gathered within the last 7 days.    http://api.channel4.com/pmlsd/brands/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/brands/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.call4oDPopularAllBrandsFeed(platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#call4oDPopularAllBrandsFeed");
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
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="call4oDPopularAllBrandsFeed2"></a>
# **call4oDPopularAllBrandsFeed2**
> Atom call4oDPopularAllBrandsFeed2(pageno, platform)

4oD Popular All Brands Feed(2)

Lists all Channel 4 programmes available on 4oD by popularity considering    the data gathered within the last 7 days.    http://api.channel4.com/pmlsd/brands/4od/popular/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/brands/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.call4oDPopularAllBrandsFeed2(pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#call4oDPopularAllBrandsFeed2");
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
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="call4oDProgrammesByTXDate"></a>
# **call4oDProgrammesByTXDate**
> Atom call4oDProgrammesByTXDate(category, platform)

4oD Programmes by TX Date

Lists all Channel 4oD programmes associated with the specified category    (tag).By default, the programmes are listed in order of Transmission (TX)    Date, with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals/4oD.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.call4oDProgrammesByTXDate(category, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#call4oDProgrammesByTXDate");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="call4oDProgrammesByTXDate2"></a>
# **call4oDProgrammesByTXDate2**
> Atom call4oDProgrammesByTXDate2(category, channel, platform)

4oD Programmes by TX Date(2)

Lists all Channel 4oD programmes associated with the specified category    (tag).By default, the programmes are listed in order of Transmission (TX)    Date, with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/channel/[channel]/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals/4oD.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String channel = "c4"; // String | The name of the channel for which you seek associated Channel 4oD programmes
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.call4oDProgrammesByTXDate2(category, channel, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#call4oDProgrammesByTXDate2");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **channel** | **String**| The name of the channel for which you seek associated Channel 4oD programmes | [enum: c4, f4, e4, m4, 4m, 4s] |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="call4oDProgrammesByTXDate3"></a>
# **call4oDProgrammesByTXDate3**
> Atom call4oDProgrammesByTXDate3(category, platform)

4oD Programmes by TX Date(3)

Lists all Channel 4oD programmes associated with the specified category    (tag).By default, the programmes are listed in order of Transmission (TX)    Date, with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/derived/ad/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals/4oD.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.call4oDProgrammesByTXDate3(category, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#call4oDProgrammesByTXDate3");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="call4oDProgrammesByTXDate4"></a>
# **call4oDProgrammesByTXDate4**
> Atom call4oDProgrammesByTXDate4(category, pageno, platform)

4oD Programmes by TX Date(4)

Lists all Channel 4oD programmes associated with the specified category    (tag).By default, the programmes are listed in order of Transmission (TX)    Date, with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/4od/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals/4oD.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.call4oDProgrammesByTXDate4(category, pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#call4oDProgrammesByTXDate4");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="call4oDProgrammesByTXDate5"></a>
# **call4oDProgrammesByTXDate5**
> Atom call4oDProgrammesByTXDate5(category, channel, pageno, platform)

4oD Programmes by TX Date(5)

Lists all Channel 4oD programmes associated with the specified category    (tag).By default, the programmes are listed in order of Transmission (TX)    Date, with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/channel/[channel]/4od/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals/4oD.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String channel = "c4"; // String | The name of the channel for which you seek associated Channel 4oD programmes
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.call4oDProgrammesByTXDate5(category, channel, pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#call4oDProgrammesByTXDate5");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **channel** | **String**| The name of the channel for which you seek associated Channel 4oD programmes | [enum: c4, f4, e4, m4, 4m, 4s] |
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="call4oDProgrammesByTXDate6"></a>
# **call4oDProgrammesByTXDate6**
> Atom call4oDProgrammesByTXDate6(category, pageno, platform)

4oD Programmes by TX Date(6)

Lists all Channel 4oD programmes associated with the specified category    (tag).By default, the programmes are listed in order of Transmission (TX)    Date, with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/derived/ad/4od/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals/4oD.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.call4oDProgrammesByTXDate6(category, pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#call4oDProgrammesByTXDate6");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="call4oDProgrammesByTitle"></a>
# **call4oDProgrammesByTitle**
> Atom call4oDProgrammesByTitle(category, platform)

4oD Programmes by Title

Lists all Channel 4oD programmes associated with the specified category    (tag), alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/4od/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/religion-and-belief/4oD/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.call4oDProgrammesByTitle(category, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#call4oDProgrammesByTitle");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="call4oDProgrammesByTitle2"></a>
# **call4oDProgrammesByTitle2**
> Atom call4oDProgrammesByTitle2(category, channel, platform)

4oD Programmes by Title(2)

Lists all Channel 4oD programmes associated with the specified category    (tag), alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/channel/[channel]/4od/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/religion-and-belief/4oD/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String channel = "c4"; // String | The name of the channel for which you seek associated Channel 4oD programmes
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.call4oDProgrammesByTitle2(category, channel, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#call4oDProgrammesByTitle2");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **channel** | **String**| The name of the channel for which you seek associated Channel 4oD programmes | [enum: c4, f4, e4, m4, 4m, 4s] |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="call4oDProgrammesByTitle3"></a>
# **call4oDProgrammesByTitle3**
> Atom call4oDProgrammesByTitle3(category, platform)

4oD Programmes by Title(3)

Lists all Channel 4oD programmes associated with the specified category    (tag), alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/derived/ad/4od/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/religion-and-belief/4oD/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.call4oDProgrammesByTitle3(category, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#call4oDProgrammesByTitle3");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="call4oDProgrammesByTitle4"></a>
# **call4oDProgrammesByTitle4**
> Atom call4oDProgrammesByTitle4(category, pageno, platform)

4oD Programmes by Title(4)

Lists all Channel 4oD programmes associated with the specified category    (tag), alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/4od/title/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/religion-and-belief/4oD/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.call4oDProgrammesByTitle4(category, pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#call4oDProgrammesByTitle4");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="call4oDProgrammesByTitle5"></a>
# **call4oDProgrammesByTitle5**
> Atom call4oDProgrammesByTitle5(category, channel, pageno, platform)

4oD Programmes by Title(5)

Lists all Channel 4oD programmes associated with the specified category    (tag), alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/channel/[channel]/4od/title/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/religion-and-belief/4oD/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String channel = "c4"; // String | The name of the channel for which you seek associated Channel 4oD programmes
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.call4oDProgrammesByTitle5(category, channel, pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#call4oDProgrammesByTitle5");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **channel** | **String**| The name of the channel for which you seek associated Channel 4oD programmes | [enum: c4, f4, e4, m4, 4m, 4s] |
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="call4oDProgrammesByTitle6"></a>
# **call4oDProgrammesByTitle6**
> Atom call4oDProgrammesByTitle6(category, pageno, platform)

4oD Programmes by Title(6)

Lists all Channel 4oD programmes associated with the specified category    (tag), alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/derived/ad/4od/title/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/religion-and-belief/4oD/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.call4oDProgrammesByTitle6(category, pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#call4oDProgrammesByTitle6");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="call4oDTitleAllBrandsFeed"></a>
# **call4oDTitleAllBrandsFeed**
> Atom call4oDTitleAllBrandsFeed(platform)

4oD Title All Brands Feed

Lists all Channel 4 programmes available on 4oD.  By default, the programmes    are listed by title in alphabetical order (case unsensitive).    http://api.channel4.com/pmlsd/brands/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/brands/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.call4oDTitleAllBrandsFeed(platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#call4oDTitleAllBrandsFeed");
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
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="call4oDTitleAllBrandsFeed2"></a>
# **call4oDTitleAllBrandsFeed2**
> Atom call4oDTitleAllBrandsFeed2(pageno, platform)

4oD Title All Brands Feed(2)

Lists all Channel 4 programmes available on 4oD.  By default, the programmes    are listed by title in alphabetical order (case unsensitive).    http://api.channel4.com/pmlsd/brands/4od/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/brands/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.call4oDTitleAllBrandsFeed2(pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#call4oDTitleAllBrandsFeed2");
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
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="categoriesLandingFeed"></a>
# **categoriesLandingFeed**
> Atom categoriesLandingFeed(platform)

Categories Landing Feed

Lists Channel 4 programmes by category (/ tag).    http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.categoriesLandingFeed(platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#categoriesLandingFeed");
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
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="collectionsFeed"></a>
# **collectionsFeed**
> Atom collectionsFeed(collectionName, platform)

Collections Feed

Collections are editorially controlled groups of brands, series, episodes or    other collections used for promotion and discovery of content. A SIMPLE    collection can contain an assortment of Brands, Series, Episodes or Freeform    items. A GROUP collection contains other collections.    http://api.channel4.com/pmlsd/collections/collection_name/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/collections/4od-home-promo/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String collectionName = "collectionName_example"; // String | Web safe title for the collection.
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.collectionsFeed(collectionName, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#collectionsFeed");
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
| **collectionName** | **String**| Web safe title for the collection. | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="collectionsFeed2"></a>
# **collectionsFeed2**
> Atom collectionsFeed2(collectionName, platform)

Collections Feed(2)

Collections are editorially controlled groups of brands, series, episodes or    other collections used for promotion and discovery of content. A SIMPLE    collection can contain an assortment of Brands, Series, Episodes or Freeform    items. A GROUP collection contains other collections.    http://api.channel4.com/pmlsd/collections/collection_name.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/collections/4od-home-promo/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String collectionName = "collectionName_example"; // String | Web safe title for the collection.
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.collectionsFeed2(collectionName, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#collectionsFeed2");
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
| **collectionName** | **String**| Web safe title for the collection. | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="flattenedCollectionFeed"></a>
# **flattenedCollectionFeed**
> Atom flattenedCollectionFeed(collectionName, platform)

Flattened Collection Feed

The Flattened Collections Feed is only applicable for GROUP collections and    its purpose is mainly return 3 items (BRAND, SERIES or EPSIODE) of each of    the simple collections assigned to the GROUP.    http://api.channel4.com/pmlsd/collections/collection_name/flattened/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/collections/4od-home-promo/flattened/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String collectionName = "collectionName_example"; // String | Web safe title for the collection.
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.flattenedCollectionFeed(collectionName, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#flattenedCollectionFeed");
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
| **collectionName** | **String**| Web safe title for the collection. | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="flattenedCollectionFeed2"></a>
# **flattenedCollectionFeed2**
> Atom flattenedCollectionFeed2(collectionName, platform)

Flattened Collection Feed(2)

The Flattened Collections Feed is only applicable for GROUP collections and    its purpose is mainly return 3 items (BRAND, SERIES or EPSIODE) of each of    the simple collections assigned to the GROUP.    http://api.channel4.com/pmlsd/collections/collection_name/flattened.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/collections/4od-home-promo/flattened/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String collectionName = "collectionName_example"; // String | Web safe title for the collection.
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.flattenedCollectionFeed2(collectionName, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#flattenedCollectionFeed2");
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
| **collectionName** | **String**| Web safe title for the collection. | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="mostPopularBrandsFeed"></a>
# **mostPopularBrandsFeed**
> Atom mostPopularBrandsFeed(category, platform)

Most Popular Brands Feed

Lists all Channel 4oD most popular brands for the given category within the    last 7 days, in order of popularity.    http://api.channel4.com/pmlsd/categories/category/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/comedy/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.mostPopularBrandsFeed(category, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#mostPopularBrandsFeed");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="mostPopularBrandsFeed2"></a>
# **mostPopularBrandsFeed2**
> Atom mostPopularBrandsFeed2(category, platform)

Most Popular Brands Feed(2)

Lists all Channel 4oD most popular brands for the given category within the    last 7 days, in order of popularity.    http://api.channel4.com/pmlsd/categories/category/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/comedy/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.mostPopularBrandsFeed2(category, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#mostPopularBrandsFeed2");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="mostPopularBrandsFeed3"></a>
# **mostPopularBrandsFeed3**
> Atom mostPopularBrandsFeed3(category, channel, platform)

Most Popular Brands Feed(3)

Lists all Channel 4oD most popular brands for the given category within the    last 7 days, in order of popularity.    http://api.channel4.com/pmlsd/categories/category/channel/[channel]/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/comedy/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String channel = "c4"; // String | The name of the channel for which you seek associated Channel 4oD programmes
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.mostPopularBrandsFeed3(category, channel, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#mostPopularBrandsFeed3");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **channel** | **String**| The name of the channel for which you seek associated Channel 4oD programmes | [enum: c4, f4, e4, m4, 4m, 4s] |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="mostPopularBrandsFeed4"></a>
# **mostPopularBrandsFeed4**
> Atom mostPopularBrandsFeed4(category, platform)

Most Popular Brands Feed(4)

Lists all Channel 4oD most popular brands for the given category within the    last 7 days, in order of popularity.    http://api.channel4.com/pmlsd/categories/category/derived/ad/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/comedy/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.mostPopularBrandsFeed4(category, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#mostPopularBrandsFeed4");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="mostPopularBrandsFeed5"></a>
# **mostPopularBrandsFeed5**
> Atom mostPopularBrandsFeed5(category, pageno, platform)

Most Popular Brands Feed(5)

Lists all Channel 4oD most popular brands for the given category within the    last 7 days, in order of popularity.    http://api.channel4.com/pmlsd/categories/category/4od/popular/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/comedy/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.mostPopularBrandsFeed5(category, pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#mostPopularBrandsFeed5");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="mostPopularBrandsFeed6"></a>
# **mostPopularBrandsFeed6**
> Atom mostPopularBrandsFeed6(category, pageno, platform)

Most Popular Brands Feed(6)

Lists all Channel 4oD most popular brands for the given category within the    last 7 days, in order of popularity.    http://api.channel4.com/pmlsd/categories/category/popular/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/comedy/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.mostPopularBrandsFeed6(category, pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#mostPopularBrandsFeed6");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="mostPopularBrandsFeed7"></a>
# **mostPopularBrandsFeed7**
> Atom mostPopularBrandsFeed7(category, channel, pageno, platform)

Most Popular Brands Feed(7)

Lists all Channel 4oD most popular brands for the given category within the    last 7 days, in order of popularity.    http://api.channel4.com/pmlsd/categories/category/channel/[channel]/4od/popular/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/comedy/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    String channel = "c4"; // String | The name of the channel for which you seek associated Channel 4oD programmes
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.mostPopularBrandsFeed7(category, channel, pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#mostPopularBrandsFeed7");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **channel** | **String**| The name of the channel for which you seek associated Channel 4oD programmes | [enum: c4, f4, e4, m4, 4m, 4s] |
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="mostPopularBrandsFeed8"></a>
# **mostPopularBrandsFeed8**
> Atom mostPopularBrandsFeed8(category, pageno, platform)

Most Popular Brands Feed(8)

Lists all Channel 4oD most popular brands for the given category within the    last 7 days, in order of popularity.    http://api.channel4.com/pmlsd/categories/category/derived/ad/4od/popular/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/comedy/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String category = "category_example"; // String | The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey=xxxxxxxxxxxxxxxxxxxxxxxx)
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.mostPopularBrandsFeed8(category, pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#mostPopularBrandsFeed8");
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
| **category** | **String**| The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx) | |
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="popularBrandsFeed"></a>
# **popularBrandsFeed**
> Atom popularBrandsFeed(platform)

Popular Brands Feed

Lists all Channel 4 programmes by popularity considering the data gathered    within the last 7 days.    http://api.channel4.com/pmlsd/brands/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/brands/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.popularBrandsFeed(platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#popularBrandsFeed");
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
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="popularBrandsFeed2"></a>
# **popularBrandsFeed2**
> Atom popularBrandsFeed2(pageno, platform)

Popular Brands Feed(2)

Lists all Channel 4 programmes by popularity considering the data gathered    within the last 7 days.    http://api.channel4.com/pmlsd/brands/popular/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/brands/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.popularBrandsFeed2(pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#popularBrandsFeed2");
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
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="searchFeed"></a>
# **searchFeed**
> Atom searchFeed(q, platform)

Search Feed

Lists all Channel 4 programmes where title (brand name) matching the search    term. Matches are made from the beginning of individual words in the title.    http://api.channel4.com/pmlsd/search.atom?q&#x3D;search-term&amp;apikey&#x3D;xxx    http://api.channel4.com/pmlsd/search.atom?q&#x3D;the+it+crowd&amp;apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String q = "q_example"; // String | The programme name to look for, minimum length: 2 chars.Looking for programme names with special chars might be URL encoded.
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.searchFeed(q, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#searchFeed");
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
| **q** | **String**| The programme name to look for, minimum length: 2 chars.Looking for programme names with special chars might be URL encoded. | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="searchFeed2"></a>
# **searchFeed2**
> Atom searchFeed2(q, platform)

Search Feed(2)

Lists all Channel 4 programmes where title (brand name) matching the search    term. Matches are made from the beginning of individual words in the title.    http://api.channel4.com/pmlsd/search/search-term.atom?apikey&#x3D;xxx    http://api.channel4.com/pmlsd/search.atom?q&#x3D;the+it+crowd&amp;apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String q = "q_example"; // String | The programme name to look for, minimum length: 2 chars.Looking for programme names with special chars might be URL encoded.
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.searchFeed2(q, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#searchFeed2");
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
| **q** | **String**| The programme name to look for, minimum length: 2 chars.Looking for programme names with special chars might be URL encoded. | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="searchFeed3"></a>
# **searchFeed3**
> Atom searchFeed3(q, pageno, platform)

Search Feed(3)

Lists all Channel 4 programmes where title (brand name) matching the search    term. Matches are made from the beginning of individual words in the title.    http://api.channel4.com/pmlsd/search/page-{pageno}.atom?q&#x3D;search-term&amp;apikey&#x3D;xxx    http://api.channel4.com/pmlsd/search.atom?q&#x3D;the+it+crowd&amp;apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String q = "q_example"; // String | The programme name to look for, minimum length: 2 chars.Looking for programme names with special chars might be URL encoded.
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.searchFeed3(q, pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#searchFeed3");
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
| **q** | **String**| The programme name to look for, minimum length: 2 chars.Looking for programme names with special chars might be URL encoded. | |
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="searchFeed4"></a>
# **searchFeed4**
> Atom searchFeed4(q, pageno, platform)

Search Feed(4)

Lists all Channel 4 programmes where title (brand name) matching the search    term. Matches are made from the beginning of individual words in the title.    http://api.channel4.com/pmlsd/search/search-term/page-{pageno}.atom?apikey&#x3D;xxx    http://api.channel4.com/pmlsd/search.atom?q&#x3D;the+it+crowd&amp;apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String q = "q_example"; // String | The programme name to look for, minimum length: 2 chars.Looking for programme names with special chars might be URL encoded.
    Integer pageno = 56; // Integer | Page number of results to return
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.searchFeed4(q, pageno, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#searchFeed4");
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
| **q** | **String**| The programme name to look for, minimum length: 2 chars.Looking for programme names with special chars might be URL encoded. | |
| **pageno** | **Integer**| Page number of results to return | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="tVListingsFeed"></a>
# **tVListingsFeed**
> Atom tVListingsFeed(yyyy, mm, dd, platform)

TV Listings Feed

EPG Information of daily broadcast content aired per channels, according to    broadcast date    http://api.channel4.com/pmlsd/tv-listings/daily/[yyyy]/[mm]/[dd].atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/tv-listings/daily/2010/11/28.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String yyyy = "yyyy_example"; // String | The date for which you wish to see programming information. Note the schedule days start from 6am and run until 6am on the next calendar day.
    String mm = "mm_example"; // String | The date for which you wish to see programming information. Note the schedule days start from 6am and run until 6am on the next calendar day.
    String dd = "dd_example"; // String | The date for which you wish to see programming information. Note the schedule days start from 6am and run until 6am on the next calendar day.
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.tVListingsFeed(yyyy, mm, dd, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#tVListingsFeed");
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
| **yyyy** | **String**| The date for which you wish to see programming information. Note the schedule days start from 6am and run until 6am on the next calendar day. | |
| **mm** | **String**| The date for which you wish to see programming information. Note the schedule days start from 6am and run until 6am on the next calendar day. | |
| **dd** | **String**| The date for which you wish to see programming information. Note the schedule days start from 6am and run until 6am on the next calendar day. | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="tVListingsFeed2"></a>
# **tVListingsFeed2**
> Atom tVListingsFeed2(yyyy, mm, dd, channel, platform)

TV Listings Feed(2)

EPG Information of daily broadcast content aired per channels, according to    broadcast date    http://api.channel4.com/pmlsd/tv-listings/daily/[yyyy]/[mm]/[dd]/[channel].atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/tv-listings/daily/2010/11/28.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DiscoveryresourcesApi apiInstance = new DiscoveryresourcesApi(defaultClient);
    String yyyy = "yyyy_example"; // String | The date for which you wish to see programming information. Note the schedule days start from 6am and run until 6am on the next calendar day.
    String mm = "mm_example"; // String | The date for which you wish to see programming information. Note the schedule days start from 6am and run until 6am on the next calendar day.
    String dd = "dd_example"; // String | The date for which you wish to see programming information. Note the schedule days start from 6am and run until 6am on the next calendar day.
    String channel = "c4"; // String | The EPG for a specific channel (c4, e4, m4, 4m, f4, 4s)
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.tVListingsFeed2(yyyy, mm, dd, channel, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryresourcesApi#tVListingsFeed2");
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
| **yyyy** | **String**| The date for which you wish to see programming information. Note the schedule days start from 6am and run until 6am on the next calendar day. | |
| **mm** | **String**| The date for which you wish to see programming information. Note the schedule days start from 6am and run until 6am on the next calendar day. | |
| **dd** | **String**| The date for which you wish to see programming information. Note the schedule days start from 6am and run until 6am on the next calendar day. | |
| **channel** | **String**| The EPG for a specific channel (c4, e4, m4, 4m, f4, 4s) | [enum: c4, f4, e4, m4, 4m, 4s] |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

