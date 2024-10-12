# VideosApi

All URIs are relative to *https://api.shutterstock.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVideoCollectionItems**](VideosApi.md#addVideoCollectionItems) | **POST** /v2/videos/collections/{id}/items | Add videos to collections |
| [**createVideoCollection**](VideosApi.md#createVideoCollection) | **POST** /v2/videos/collections | Create video collections |
| [**deleteVideoCollection**](VideosApi.md#deleteVideoCollection) | **DELETE** /v2/videos/collections/{id} | Delete video collections |
| [**deleteVideoCollectionItems**](VideosApi.md#deleteVideoCollectionItems) | **DELETE** /v2/videos/collections/{id}/items | Remove videos from collections |
| [**downloadVideos**](VideosApi.md#downloadVideos) | **POST** /v2/videos/licenses/{id}/downloads | Download videos |
| [**findSimilarVideos**](VideosApi.md#findSimilarVideos) | **GET** /v2/videos/{id}/similar | List similar videos |
| [**getFeaturedVideoCollection**](VideosApi.md#getFeaturedVideoCollection) | **GET** /v2/videos/collections/featured/{id} | Get the details of featured video collections |
| [**getFeaturedVideoCollectionItems**](VideosApi.md#getFeaturedVideoCollectionItems) | **GET** /v2/videos/collections/featured/{id}/items | Get the contents of featured video collections |
| [**getFeaturedVideoCollectionList**](VideosApi.md#getFeaturedVideoCollectionList) | **GET** /v2/videos/collections/featured | List featured video collections |
| [**getUpdatedVideos**](VideosApi.md#getUpdatedVideos) | **GET** /v2/videos/updated | List updated videos |
| [**getVideo**](VideosApi.md#getVideo) | **GET** /v2/videos/{id} | Get details about videos |
| [**getVideoCollection**](VideosApi.md#getVideoCollection) | **GET** /v2/videos/collections/{id} | Get the details of video collections |
| [**getVideoCollectionItems**](VideosApi.md#getVideoCollectionItems) | **GET** /v2/videos/collections/{id}/items | Get the contents of video collections |
| [**getVideoCollectionList**](VideosApi.md#getVideoCollectionList) | **GET** /v2/videos/collections | List video collections |
| [**getVideoLicenseList**](VideosApi.md#getVideoLicenseList) | **GET** /v2/videos/licenses | List video licenses |
| [**getVideoList**](VideosApi.md#getVideoList) | **GET** /v2/videos | List videos |
| [**getVideoSuggestions**](VideosApi.md#getVideoSuggestions) | **GET** /v2/videos/search/suggestions | Get suggestions for a search term |
| [**licenseVideos**](VideosApi.md#licenseVideos) | **POST** /v2/videos/licenses | License videos |
| [**listVideoCategories**](VideosApi.md#listVideoCategories) | **GET** /v2/videos/categories | List video categories |
| [**renameVideoCollection**](VideosApi.md#renameVideoCollection) | **POST** /v2/videos/collections/{id} | Rename video collections |
| [**searchVideos**](VideosApi.md#searchVideos) | **GET** /v2/videos/search | Search for videos |


<a id="addVideoCollectionItems"></a>
# **addVideoCollectionItems**
> addVideoCollectionItems(id, collectionItemRequest)

Add videos to collections

This endpoint adds one or more videos to a collection by video IDs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String id = "17555176"; // String | The ID of the collection to which items should be added
    CollectionItemRequest collectionItemRequest = new CollectionItemRequest(); // CollectionItemRequest | Array of video IDs to add to the collection
    try {
      apiInstance.addVideoCollectionItems(id, collectionItemRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#addVideoCollectionItems");
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
| **id** | **String**| The ID of the collection to which items should be added | |
| **collectionItemRequest** | [**CollectionItemRequest**](CollectionItemRequest.md)| Array of video IDs to add to the collection | |

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully added collection items |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Collection not found |  -  |

<a id="createVideoCollection"></a>
# **createVideoCollection**
> CollectionCreateResponse createVideoCollection(collectionCreateRequest)

Create video collections

This endpoint creates one or more collections (clipboxes). To add videos to collections, use &#x60;POST /v2/videos/collections/{id}/items&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    CollectionCreateRequest collectionCreateRequest = new CollectionCreateRequest(); // CollectionCreateRequest | Collection metadata
    try {
      CollectionCreateResponse result = apiInstance.createVideoCollection(collectionCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#createVideoCollection");
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
| **collectionCreateRequest** | [**CollectionCreateRequest**](CollectionCreateRequest.md)| Collection metadata | |

### Return type

[**CollectionCreateResponse**](CollectionCreateResponse.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successfully created video collection |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="deleteVideoCollection"></a>
# **deleteVideoCollection**
> deleteVideoCollection(id)

Delete video collections

This endpoint deletes a collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String id = "17555176"; // String | The ID of the collection to delete
    try {
      apiInstance.deleteVideoCollection(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#deleteVideoCollection");
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
| **id** | **String**| The ID of the collection to delete | |

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully deleted collection |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Collection not found |  -  |

<a id="deleteVideoCollectionItems"></a>
# **deleteVideoCollectionItems**
> deleteVideoCollectionItems(id, itemId)

Remove videos from collections

This endpoint removes one or more videos from a collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String id = "17555176"; // String | The ID of the Collection from which items will be deleted
    List<String> itemId = Arrays.asList(); // List<String> | One or more video IDs to remove from the collection
    try {
      apiInstance.deleteVideoCollectionItems(id, itemId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#deleteVideoCollectionItems");
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
| **id** | **String**| The ID of the Collection from which items will be deleted | |
| **itemId** | [**List&lt;String&gt;**](String.md)| One or more video IDs to remove from the collection | [optional] |

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully removed collection items |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Collection not found |  -  |

<a id="downloadVideos"></a>
# **downloadVideos**
> Url downloadVideos(id, redownloadVideo)

Download videos

This endpoint redownloads videos that you have already received a license for.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String id = "e123"; // String | The license ID of the item to (re)download. The download links in the response are valid for 8 hours.
    RedownloadVideo redownloadVideo = new RedownloadVideo(); // RedownloadVideo | Information about the videos to redownload
    try {
      Url result = apiInstance.downloadVideos(id, redownloadVideo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#downloadVideos");
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
| **id** | **String**| The license ID of the item to (re)download. The download links in the response are valid for 8 hours. | |
| **redownloadVideo** | [**RedownloadVideo**](RedownloadVideo.md)| Information about the videos to redownload | |

### Return type

[**Url**](Url.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="findSimilarVideos"></a>
# **findSimilarVideos**
> VideoSearchResults findSimilarVideos(id, language, page, perPage, view)

List similar videos

This endpoint searches for videos that are similar to a video that you specify.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String id = "2140697"; // String | The ID of a video for which similar videos should be returned
    Language language = Language.fromValue("ar"); // Language | Language for the keywords and categories in the response
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    String view = "minimal"; // String | Amount of detail to render in the response
    try {
      VideoSearchResults result = apiInstance.findSimilarVideos(id, language, page, perPage, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#findSimilarVideos");
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
| **id** | **String**| The ID of a video for which similar videos should be returned | |
| **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] [enum: ar, bg, bn, cs, da, de, el, en, es, fi, fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, ml, mr, nb, nl, or, pl, pt, ro, ru, sk, sl, sv, ta, te, th, tr, uk, ur, vi, zh, zh-Hant] |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **view** | **String**| Amount of detail to render in the response | [optional] [default to minimal] [enum: minimal, full] |

### Return type

[**VideoSearchResults**](VideoSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getFeaturedVideoCollection"></a>
# **getFeaturedVideoCollection**
> FeaturedCollection getFeaturedVideoCollection(id, embed)

Get the details of featured video collections

This endpoint gets more detailed information about a featured video collection, including its cover video and timestamps for its creation and most recent update. To get the videos, use &#x60;GET /v2/videos/collections/featured/{id}/items&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String id = "136351027"; // String | Collection ID
    String embed = "share_url"; // String | What information to include in the response, such as a URL to the collection
    try {
      FeaturedCollection result = apiInstance.getFeaturedVideoCollection(id, embed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#getFeaturedVideoCollection");
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
| **id** | **String**| Collection ID | |
| **embed** | **String**| What information to include in the response, such as a URL to the collection | [optional] [enum: share_url] |

### Return type

[**FeaturedCollection**](FeaturedCollection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Featured collection not found |  -  |

<a id="getFeaturedVideoCollectionItems"></a>
# **getFeaturedVideoCollectionItems**
> VideoCollectionItemDataList getFeaturedVideoCollectionItems(id, page, perPage)

Get the contents of featured video collections

This endpoint lists the IDs of videos in a featured collection and the date that each was added.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String id = "136351027"; // String | Collection ID
    Integer page = 1; // Integer | Page number
    Integer perPage = 100; // Integer | Number of results per page
    try {
      VideoCollectionItemDataList result = apiInstance.getFeaturedVideoCollectionItems(id, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#getFeaturedVideoCollectionItems");
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
| **id** | **String**| Collection ID | |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 100] |

### Return type

[**VideoCollectionItemDataList**](VideoCollectionItemDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Featured collection not found |  -  |

<a id="getFeaturedVideoCollectionList"></a>
# **getFeaturedVideoCollectionList**
> FeaturedCollectionDataList getFeaturedVideoCollectionList(embed)

List featured video collections

This endpoint lists featured video collections and a name and cover video for each collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String embed = "share_url"; // String | What information to include in the response, such as a URL to the collection
    try {
      FeaturedCollectionDataList result = apiInstance.getFeaturedVideoCollectionList(embed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#getFeaturedVideoCollectionList");
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
| **embed** | **String**| What information to include in the response, such as a URL to the collection | [optional] [enum: share_url] |

### Return type

[**FeaturedCollectionDataList**](FeaturedCollectionDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getUpdatedVideos"></a>
# **getUpdatedVideos**
> UpdatedMediaDataList getUpdatedVideos(startDate, endDate, interval, page, perPage, sort)

List updated videos

This endpoint lists videos that have been updated in the specified time period to update content management systems (CMS) or digital asset management (DAM) systems. In most cases, use the &#x60;interval&#x60; parameter to show videos that were updated recently, but you can also use the &#x60;start_date&#x60; and &#x60;end_date&#x60; parameters to specify a range of no more than three days. Do not use the &#x60;interval&#x60; parameter with either &#x60;start_date&#x60; or &#x60;end_date&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    VideosApi apiInstance = new VideosApi(defaultClient);
    LocalDate startDate = LocalDate.parse("2020-05-29"); // LocalDate | Show videos updated on or after the specified date
    LocalDate endDate = LocalDate.parse("2021-05-29"); // LocalDate | Show videos updated before the specified date
    String interval = "1 HOUR"; // String | Show videos updated in the specified time period, where the time period is an interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows videos that were updated in the hour preceding the request
    Integer page = 1; // Integer | Page number
    Integer perPage = 100; // Integer | Number of results per page
    String sort = "newest"; // String | Sort by oldest or newest videos first
    try {
      UpdatedMediaDataList result = apiInstance.getUpdatedVideos(startDate, endDate, interval, page, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#getUpdatedVideos");
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
| **startDate** | **LocalDate**| Show videos updated on or after the specified date | [optional] |
| **endDate** | **LocalDate**| Show videos updated before the specified date | [optional] |
| **interval** | **String**| Show videos updated in the specified time period, where the time period is an interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows videos that were updated in the hour preceding the request | [optional] [default to 1 HOUR] |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 100] |
| **sort** | **String**| Sort by oldest or newest videos first | [optional] [default to newest] [enum: newest, oldest] |

### Return type

[**UpdatedMediaDataList**](UpdatedMediaDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getVideo"></a>
# **getVideo**
> Video getVideo(id, language, view, searchId)

Get details about videos

This endpoint shows information about a video, including URLs to previews and the sizes that it is available in.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String id = "639703"; // String | Video ID
    Language language = Language.fromValue("ar"); // Language | Language for the keywords and categories in the response
    String view = "minimal"; // String | Amount of detail to render in the response
    String searchId = "00000000-0000-0000-0000-000000000000"; // String | The ID of the search that is related to this request
    try {
      Video result = apiInstance.getVideo(id, language, view, searchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#getVideo");
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
| **id** | **String**| Video ID | |
| **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] [enum: ar, bg, bn, cs, da, de, el, en, es, fi, fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, ml, mr, nb, nl, or, pl, pt, ro, ru, sk, sl, sv, ta, te, th, tr, uk, ur, vi, zh, zh-Hant] |
| **view** | **String**| Amount of detail to render in the response | [optional] [default to full] [enum: minimal, full] |
| **searchId** | **String**| The ID of the search that is related to this request | [optional] |

### Return type

[**Video**](Video.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |

<a id="getVideoCollection"></a>
# **getVideoCollection**
> Collection getVideoCollection(id, embed, shareCode)

Get the details of video collections

This endpoint gets more detailed information about a collection, including the timestamp for its creation and the number of videos in it. To get the videos in collections, use GET /v2/videos/collections/{id}/items.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String id = "17555176"; // String | The ID of the collection to return
    List<String> embed = Arrays.asList(); // List<String> | Which sharing information to include in the response, such as a URL to the collection
    String shareCode = "shareCode_example"; // String | Code to retrieve a shared collection
    try {
      Collection result = apiInstance.getVideoCollection(id, embed, shareCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#getVideoCollection");
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
| **id** | **String**| The ID of the collection to return | |
| **embed** | [**List&lt;String&gt;**](String.md)| Which sharing information to include in the response, such as a URL to the collection | [optional] [enum: share_code, share_url] |
| **shareCode** | **String**| Code to retrieve a shared collection | [optional] |

### Return type

[**Collection**](Collection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Collection not found |  -  |

<a id="getVideoCollectionItems"></a>
# **getVideoCollectionItems**
> CollectionItemDataList getVideoCollectionItems(id, page, perPage, shareCode, sort)

Get the contents of video collections

This endpoint lists the IDs of videos in a collection and the date that each was added.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String id = "17555176"; // String | Collection ID
    Integer page = 1; // Integer | Page number
    Integer perPage = 100; // Integer | Number of results per page
    String shareCode = "shareCode_example"; // String | Code to retrieve the contents of a shared collection
    String sort = "newest"; // String | Sort order
    try {
      CollectionItemDataList result = apiInstance.getVideoCollectionItems(id, page, perPage, shareCode, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#getVideoCollectionItems");
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
| **id** | **String**| Collection ID | |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 100] |
| **shareCode** | **String**| Code to retrieve the contents of a shared collection | [optional] |
| **sort** | **String**| Sort order | [optional] [default to oldest] [enum: newest, oldest] |

### Return type

[**CollectionItemDataList**](CollectionItemDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Collection not found |  -  |

<a id="getVideoCollectionList"></a>
# **getVideoCollectionList**
> CollectionDataList getVideoCollectionList(page, perPage, embed)

List video collections

This endpoint lists your collections of videos and their basic attributes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    Integer page = 1; // Integer | Page number
    Integer perPage = 100; // Integer | Number of results per page
    List<String> embed = Arrays.asList(); // List<String> | Which sharing information to include in the response, such as a URL to the collection
    try {
      CollectionDataList result = apiInstance.getVideoCollectionList(page, perPage, embed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#getVideoCollectionList");
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
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 100] |
| **embed** | [**List&lt;String&gt;**](String.md)| Which sharing information to include in the response, such as a URL to the collection | [optional] [enum: share_code, share_url] |

### Return type

[**CollectionDataList**](CollectionDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getVideoLicenseList"></a>
# **getVideoLicenseList**
> DownloadHistoryDataList getVideoLicenseList(videoId, license, page, perPage, sort, username, startDate, endDate, downloadAvailability, teamHistory)

List video licenses

This endpoint lists existing licenses.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String videoId = "12345678"; // String | Show licenses for the specified video ID
    String license = "standard"; // String | Show videos that are available with the specified license, such as `standard` or `enhanced`; prepending a `-` sign excludes results from that license
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    String sort = "newest"; // String | Sort by oldest or newest videos first
    String username = "aUniqueUsername"; // String | Filter licenses by username of licensee
    OffsetDateTime startDate = OffsetDateTime.parse("2021-03-29T13:25:13.521Z"); // OffsetDateTime | Show licenses created on or after the specified date
    OffsetDateTime endDate = OffsetDateTime.parse("2021-03-29T13:25:13.521Z"); // OffsetDateTime | Show licenses created before the specified date
    String downloadAvailability = "all"; // String | Filter licenses by download availability
    Boolean teamHistory = false; // Boolean | Set to true to see license history for all members of your team.
    try {
      DownloadHistoryDataList result = apiInstance.getVideoLicenseList(videoId, license, page, perPage, sort, username, startDate, endDate, downloadAvailability, teamHistory);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#getVideoLicenseList");
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
| **videoId** | **String**| Show licenses for the specified video ID | [optional] |
| **license** | **String**| Show videos that are available with the specified license, such as &#x60;standard&#x60; or &#x60;enhanced&#x60;; prepending a &#x60;-&#x60; sign excludes results from that license | [optional] |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **sort** | **String**| Sort by oldest or newest videos first | [optional] [default to newest] [enum: newest, oldest] |
| **username** | **String**| Filter licenses by username of licensee | [optional] |
| **startDate** | **OffsetDateTime**| Show licenses created on or after the specified date | [optional] |
| **endDate** | **OffsetDateTime**| Show licenses created before the specified date | [optional] |
| **downloadAvailability** | **String**| Filter licenses by download availability | [optional] [default to all] [enum: all, downloadable, non_downloadable] |
| **teamHistory** | **Boolean**| Set to true to see license history for all members of your team. | [optional] [default to false] |

### Return type

[**DownloadHistoryDataList**](DownloadHistoryDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getVideoList"></a>
# **getVideoList**
> VideoDataList getVideoList(id, view, searchId)

List videos

This endpoint lists information about one or more videos, including the aspect ratio and URLs to previews.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    VideosApi apiInstance = new VideosApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | One or more video IDs
    String view = "minimal"; // String | Amount of detail to render in the response
    String searchId = "00000000-0000-0000-0000-000000000000"; // String | The ID of the search that is related to this request
    try {
      VideoDataList result = apiInstance.getVideoList(id, view, searchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#getVideoList");
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
| **id** | [**List&lt;String&gt;**](String.md)| One or more video IDs | |
| **view** | **String**| Amount of detail to render in the response | [optional] [default to minimal] [enum: minimal, full] |
| **searchId** | **String**| The ID of the search that is related to this request | [optional] |

### Return type

[**VideoDataList**](VideoDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getVideoSuggestions"></a>
# **getVideoSuggestions**
> Suggestions getVideoSuggestions(query, limit)

Get suggestions for a search term

This endpoint provides autocomplete suggestions for partial search terms.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String query = "cats"; // String | Search term for which you want keyword suggestions
    Integer limit = 10; // Integer | Limit the number of the suggestions
    try {
      Suggestions result = apiInstance.getVideoSuggestions(query, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#getVideoSuggestions");
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
| **query** | **String**| Search term for which you want keyword suggestions | |
| **limit** | **Integer**| Limit the number of the suggestions | [optional] [default to 10] |

### Return type

[**Suggestions**](Suggestions.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="licenseVideos"></a>
# **licenseVideos**
> LicenseVideoResultDataList licenseVideos(licenseVideoRequest, subscriptionId, size, searchId)

License videos

This endpoint gets licenses for one or more videos. You must specify the video IDs in the body parameter and the size and subscription ID either in the query parameter or with each video ID in the body parameter. Values in the body parameter override values in the query parameters. The download links in the response are valid for 8 hours.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    LicenseVideoRequest licenseVideoRequest = new LicenseVideoRequest(); // LicenseVideoRequest | List of videos to request licenses for and information about each license transaction; these values override the defaults in the query parameters
    String subscriptionId = "s12345678"; // String | The subscription ID to use for licensing
    String size = "web"; // String | The size of the video to license
    String searchId = "searchId_example"; // String | The Search ID that led to this licensing event
    try {
      LicenseVideoResultDataList result = apiInstance.licenseVideos(licenseVideoRequest, subscriptionId, size, searchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#licenseVideos");
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
| **licenseVideoRequest** | [**LicenseVideoRequest**](LicenseVideoRequest.md)| List of videos to request licenses for and information about each license transaction; these values override the defaults in the query parameters | |
| **subscriptionId** | **String**| The subscription ID to use for licensing | [optional] |
| **size** | **String**| The size of the video to license | [optional] [default to web] [enum: web, sd, hd, 4k] |
| **searchId** | **String**| The Search ID that led to this licensing event | [optional] |

### Return type

[**LicenseVideoResultDataList**](LicenseVideoResultDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="listVideoCategories"></a>
# **listVideoCategories**
> CategoryDataList listVideoCategories(language)

List video categories

This endpoint lists the categories (Shutterstock-assigned genres) that videos can belong to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    VideosApi apiInstance = new VideosApi(defaultClient);
    Language language = Language.fromValue("ar"); // Language | Language for the keywords and categories in the response
    try {
      CategoryDataList result = apiInstance.listVideoCategories(language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#listVideoCategories");
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
| **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] [enum: ar, bg, bn, cs, da, de, el, en, es, fi, fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, ml, mr, nb, nl, or, pl, pt, ro, ru, sk, sl, sv, ta, te, th, tr, uk, ur, vi, zh, zh-Hant] |

### Return type

[**CategoryDataList**](CategoryDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="renameVideoCollection"></a>
# **renameVideoCollection**
> renameVideoCollection(id, collectionUpdateRequest)

Rename video collections

This endpoint sets a new name for a collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String id = "17555176"; // String | The ID of the collection to rename
    CollectionUpdateRequest collectionUpdateRequest = new CollectionUpdateRequest(); // CollectionUpdateRequest | The new name for the collection
    try {
      apiInstance.renameVideoCollection(id, collectionUpdateRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#renameVideoCollection");
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
| **id** | **String**| The ID of the collection to rename | |
| **collectionUpdateRequest** | [**CollectionUpdateRequest**](CollectionUpdateRequest.md)| The new name for the collection | |

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully updated collection |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Collection not found |  -  |

<a id="searchVideos"></a>
# **searchVideos**
> VideoSearchResults searchVideos(addedDate, addedDateStart, addedDateEnd, aspectRatio, category, contributor, contributorCountry, duration, durationFrom, durationTo, fps, fpsFrom, fpsTo, keywordSafeSearch, language, license, model, page, perPage, peopleAge, peopleEthnicity, peopleGender, peopleNumber, peopleModelReleased, query, resolution, safe, sort, view)

Search for videos

This endpoint searches for videos. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in the &#x60;query&#x60; parameter by prefixing the term with NOT.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    VideosApi apiInstance = new VideosApi(defaultClient);
    LocalDate addedDate = LocalDate.parse("2020-05-29"); // LocalDate | Show videos added on the specified date
    LocalDate addedDateStart = LocalDate.parse("2020-05-29"); // LocalDate | Show videos added on or after the specified date
    LocalDate addedDateEnd = LocalDate.parse("2020-05-29"); // LocalDate | Show videos added before the specified date
    String aspectRatio = "43"; // String | Show videos with the specified aspect ratio
    String category = "category_example"; // String | Show videos with the specified Shutterstock-defined category; specify a category name or ID
    List<String> contributor = Arrays.asList(); // List<String> | Show videos with the specified artist names or IDs
    List<String> contributorCountry = Arrays.asList(); // List<String> | Show videos from contributors in one or more specified countries
    Integer duration = 56; // Integer | (Deprecated; use duration_from and duration_to instead) Show videos with the specified duration in seconds
    Integer durationFrom = 60; // Integer | Show videos with the specified duration or longer in seconds
    Integer durationTo = 180; // Integer | Show videos with the specified duration or shorter in seconds
    BigDecimal fps = new BigDecimal(78); // BigDecimal | (Deprecated; use fps_from and fps_to instead) Show videos with the specified frames per second
    BigDecimal fpsFrom = new BigDecimal("24"); // BigDecimal | Show videos with the specified frames per second or more
    BigDecimal fpsTo = new BigDecimal("60"); // BigDecimal | Show videos with the specified frames per second or fewer
    Boolean keywordSafeSearch = true; // Boolean | Hide results with potentially unsafe keywords
    Language language = Language.fromValue("ar"); // Language | Set query and result language (uses Accept-Language header if not set)
    List<String> license = Arrays.asList("commercial"); // List<String> | Show only videos with the specified license or licenses
    List<String> model = Arrays.asList(); // List<String> | Show videos with each of the specified models
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    String peopleAge = "infants"; // String | Show videos that feature people of the specified age range
    List<String> peopleEthnicity = Arrays.asList(); // List<String> | Show videos with people of the specified ethnicities
    String peopleGender = "male"; // String | Show videos with people with the specified gender
    Integer peopleNumber = 2; // Integer | Show videos with the specified number of people
    Boolean peopleModelReleased = true; // Boolean | Show only videos of people with a signed model release
    String query = "dogs running on the beach"; // String | One or more search terms separated by spaces; you can use NOT to filter out videos that match a term
    String resolution = "4k"; // String | Show videos with the specified resolution
    Boolean safe = true; // Boolean | Enable or disable safe search
    String sort = "newest"; // String | Sort by one of these categories
    String view = "minimal"; // String | Amount of detail to render in the response
    try {
      VideoSearchResults result = apiInstance.searchVideos(addedDate, addedDateStart, addedDateEnd, aspectRatio, category, contributor, contributorCountry, duration, durationFrom, durationTo, fps, fpsFrom, fpsTo, keywordSafeSearch, language, license, model, page, perPage, peopleAge, peopleEthnicity, peopleGender, peopleNumber, peopleModelReleased, query, resolution, safe, sort, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#searchVideos");
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
| **addedDate** | **LocalDate**| Show videos added on the specified date | [optional] |
| **addedDateStart** | **LocalDate**| Show videos added on or after the specified date | [optional] |
| **addedDateEnd** | **LocalDate**| Show videos added before the specified date | [optional] |
| **aspectRatio** | **String**| Show videos with the specified aspect ratio | [optional] [enum: 43, 169, nonstandard] |
| **category** | **String**| Show videos with the specified Shutterstock-defined category; specify a category name or ID | [optional] |
| **contributor** | [**List&lt;String&gt;**](String.md)| Show videos with the specified artist names or IDs | [optional] |
| **contributorCountry** | [**List&lt;String&gt;**](String.md)| Show videos from contributors in one or more specified countries | [optional] |
| **duration** | **Integer**| (Deprecated; use duration_from and duration_to instead) Show videos with the specified duration in seconds | [optional] |
| **durationFrom** | **Integer**| Show videos with the specified duration or longer in seconds | [optional] |
| **durationTo** | **Integer**| Show videos with the specified duration or shorter in seconds | [optional] |
| **fps** | **BigDecimal**| (Deprecated; use fps_from and fps_to instead) Show videos with the specified frames per second | [optional] |
| **fpsFrom** | **BigDecimal**| Show videos with the specified frames per second or more | [optional] |
| **fpsTo** | **BigDecimal**| Show videos with the specified frames per second or fewer | [optional] |
| **keywordSafeSearch** | **Boolean**| Hide results with potentially unsafe keywords | [optional] [default to true] |
| **language** | [**Language**](.md)| Set query and result language (uses Accept-Language header if not set) | [optional] [enum: ar, bg, bn, cs, da, de, el, en, es, fi, fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, ml, mr, nb, nl, or, pl, pt, ro, ru, sk, sl, sv, ta, te, th, tr, uk, ur, vi, zh, zh-Hant] |
| **license** | [**List&lt;String&gt;**](String.md)| Show only videos with the specified license or licenses | [optional] [enum: commercial, editorial] |
| **model** | [**List&lt;String&gt;**](String.md)| Show videos with each of the specified models | [optional] |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **peopleAge** | **String**| Show videos that feature people of the specified age range | [optional] [enum: infants, children, teenagers, 20s, 30s, 40s, 50s, 60s, older] |
| **peopleEthnicity** | [**List&lt;String&gt;**](String.md)| Show videos with people of the specified ethnicities | [optional] [enum: african, african_american, black, brazilian, chinese, caucasian, east_asian, hispanic, japanese, middle_eastern, native_american, pacific_islander, south_asian, southeast_asian, other] |
| **peopleGender** | **String**| Show videos with people with the specified gender | [optional] [enum: male, female, both] |
| **peopleNumber** | **Integer**| Show videos with the specified number of people | [optional] |
| **peopleModelReleased** | **Boolean**| Show only videos of people with a signed model release | [optional] |
| **query** | **String**| One or more search terms separated by spaces; you can use NOT to filter out videos that match a term | [optional] |
| **resolution** | **String**| Show videos with the specified resolution | [optional] [enum: 4k, standard_definition, high_definition] |
| **safe** | **Boolean**| Enable or disable safe search | [optional] [default to true] |
| **sort** | **String**| Sort by one of these categories | [optional] [default to popular] [enum: newest, popular, relevance, random] |
| **view** | **String**| Amount of detail to render in the response | [optional] [default to minimal] [enum: minimal, full] |

### Return type

[**VideoSearchResults**](VideoSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |

