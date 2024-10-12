# AudioApi

All URIs are relative to *https://api.shutterstock.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addTrackCollectionItems**](AudioApi.md#addTrackCollectionItems) | **POST** /v2/audio/collections/{id}/items | Add audio tracks to collections |
| [**createTrackCollection**](AudioApi.md#createTrackCollection) | **POST** /v2/audio/collections | Create audio collections |
| [**deleteTrackCollection**](AudioApi.md#deleteTrackCollection) | **DELETE** /v2/audio/collections/{id} | Delete audio collections |
| [**deleteTrackCollectionItems**](AudioApi.md#deleteTrackCollectionItems) | **DELETE** /v2/audio/collections/{id}/items | Remove audio tracks from collections |
| [**downloadTracks**](AudioApi.md#downloadTracks) | **POST** /v2/audio/licenses/{id}/downloads | Download audio tracks |
| [**getTrack**](AudioApi.md#getTrack) | **GET** /v2/audio/{id} | Get details about audio tracks |
| [**getTrackCollection**](AudioApi.md#getTrackCollection) | **GET** /v2/audio/collections/{id} | Get the details of audio collections |
| [**getTrackCollectionItems**](AudioApi.md#getTrackCollectionItems) | **GET** /v2/audio/collections/{id}/items | Get the contents of audio collections |
| [**getTrackCollectionList**](AudioApi.md#getTrackCollectionList) | **GET** /v2/audio/collections | List audio collections |
| [**getTrackLicenseList**](AudioApi.md#getTrackLicenseList) | **GET** /v2/audio/licenses | List audio licenses |
| [**getTrackList**](AudioApi.md#getTrackList) | **GET** /v2/audio | List audio tracks |
| [**licenseTrack**](AudioApi.md#licenseTrack) | **POST** /v2/audio/licenses | License audio tracks |
| [**listGenres**](AudioApi.md#listGenres) | **GET** /v2/audio/genres | List audio genres |
| [**listInstruments**](AudioApi.md#listInstruments) | **GET** /v2/audio/instruments | List audio instruments |
| [**listMoods**](AudioApi.md#listMoods) | **GET** /v2/audio/moods | List audio moods |
| [**renameTrackCollection**](AudioApi.md#renameTrackCollection) | **POST** /v2/audio/collections/{id} | Rename audio collections |
| [**searchTracks**](AudioApi.md#searchTracks) | **GET** /v2/audio/search | Search for tracks |


<a id="addTrackCollectionItems"></a>
# **addTrackCollectionItems**
> addTrackCollectionItems(id, collectionItemRequest)

Add audio tracks to collections

This endpoint adds one or more tracks to a collection by track IDs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AudioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    AudioApi apiInstance = new AudioApi(defaultClient);
    String id = "48433115"; // String | Collection ID
    CollectionItemRequest collectionItemRequest = new CollectionItemRequest(); // CollectionItemRequest | List of items to add to collection
    try {
      apiInstance.addTrackCollectionItems(id, collectionItemRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudioApi#addTrackCollectionItems");
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
| **collectionItemRequest** | [**CollectionItemRequest**](CollectionItemRequest.md)| List of items to add to collection | |

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

<a id="createTrackCollection"></a>
# **createTrackCollection**
> CollectionCreateResponse createTrackCollection(collectionCreateRequest)

Create audio collections

This endpoint creates one or more collections (soundboxes). To add tracks, use &#x60;POST /v2/audio/collections/{id}/items&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AudioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    AudioApi apiInstance = new AudioApi(defaultClient);
    CollectionCreateRequest collectionCreateRequest = new CollectionCreateRequest(); // CollectionCreateRequest | Collection metadata
    try {
      CollectionCreateResponse result = apiInstance.createTrackCollection(collectionCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudioApi#createTrackCollection");
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
| **201** | Successfully created audio collection |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="deleteTrackCollection"></a>
# **deleteTrackCollection**
> deleteTrackCollection(id)

Delete audio collections

This endpoint deletes a collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AudioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    AudioApi apiInstance = new AudioApi(defaultClient);
    String id = "48433111"; // String | Collection ID
    try {
      apiInstance.deleteTrackCollection(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudioApi#deleteTrackCollection");
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

<a id="deleteTrackCollectionItems"></a>
# **deleteTrackCollectionItems**
> deleteTrackCollectionItems(id, itemId)

Remove audio tracks from collections

This endpoint removes one or more tracks from a collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AudioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    AudioApi apiInstance = new AudioApi(defaultClient);
    String id = "48433119"; // String | Collection ID
    List<String> itemId = Arrays.asList(); // List<String> | One or more item IDs to remove from the collection
    try {
      apiInstance.deleteTrackCollectionItems(id, itemId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudioApi#deleteTrackCollectionItems");
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
| **itemId** | [**List&lt;String&gt;**](String.md)| One or more item IDs to remove from the collection | [optional] |

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

<a id="downloadTracks"></a>
# **downloadTracks**
> AudioUrl downloadTracks(id)

Download audio tracks

This endpoint redownloads tracks that you have already received a license for. The download links in the response are valid for 8 hours.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AudioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    AudioApi apiInstance = new AudioApi(defaultClient);
    String id = "e123"; // String | License ID
    try {
      AudioUrl result = apiInstance.downloadTracks(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudioApi#downloadTracks");
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
| **id** | **String**| License ID | |

### Return type

[**AudioUrl**](AudioUrl.md)

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

<a id="getTrack"></a>
# **getTrack**
> Audio getTrack(id, view, searchId)

Get details about audio tracks

This endpoint shows information about a track, including its genres, instruments, and other attributes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AudioApi;

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

    AudioApi apiInstance = new AudioApi(defaultClient);
    Integer id = 442583; // Integer | Audio track ID
    String view = "minimal"; // String | Amount of detail to render in the response
    String searchId = "00000000-0000-0000-0000-000000000000"; // String | The ID of the search that is related to this request
    try {
      Audio result = apiInstance.getTrack(id, view, searchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudioApi#getTrack");
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
| **id** | **Integer**| Audio track ID | |
| **view** | **String**| Amount of detail to render in the response | [optional] [default to full] [enum: minimal, full] |
| **searchId** | **String**| The ID of the search that is related to this request | [optional] |

### Return type

[**Audio**](Audio.md)

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

<a id="getTrackCollection"></a>
# **getTrackCollection**
> Collection getTrackCollection(id, embed, shareCode)

Get the details of audio collections

This endpoint gets more detailed information about a collection, including the number of items in it and when it was last updated. To get the tracks in collections, use &#x60;GET /v2/audio/collections/{id}/items&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AudioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    AudioApi apiInstance = new AudioApi(defaultClient);
    String id = "48433107"; // String | Collection ID
    List<String> embed = Arrays.asList(); // List<String> | Which sharing information to include in the response, such as a URL to the collection
    String shareCode = "shareCode_example"; // String | Code to retrieve a shared collection
    try {
      Collection result = apiInstance.getTrackCollection(id, embed, shareCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudioApi#getTrackCollection");
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

<a id="getTrackCollectionItems"></a>
# **getTrackCollectionItems**
> CollectionItemDataList getTrackCollectionItems(id, page, perPage, shareCode, sort)

Get the contents of audio collections

This endpoint lists the IDs of tracks in a collection and the date that each was added.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AudioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    AudioApi apiInstance = new AudioApi(defaultClient);
    String id = "126351027"; // String | Collection ID
    Integer page = 1; // Integer | Page number
    Integer perPage = 100; // Integer | Number of results per page
    String shareCode = "shareCode_example"; // String | Code to retrieve the contents of a shared collection
    String sort = "newest"; // String | Sort order
    try {
      CollectionItemDataList result = apiInstance.getTrackCollectionItems(id, page, perPage, shareCode, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudioApi#getTrackCollectionItems");
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

<a id="getTrackCollectionList"></a>
# **getTrackCollectionList**
> CollectionDataList getTrackCollectionList(page, perPage, embed)

List audio collections

This endpoint lists your collections of audio tracks and their basic attributes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AudioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    AudioApi apiInstance = new AudioApi(defaultClient);
    Integer page = 1; // Integer | Page number
    Integer perPage = 100; // Integer | Number of results per page
    List<String> embed = Arrays.asList(); // List<String> | Which sharing information to include in the response, such as a URL to the collection
    try {
      CollectionDataList result = apiInstance.getTrackCollectionList(page, perPage, embed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudioApi#getTrackCollectionList");
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

<a id="getTrackLicenseList"></a>
# **getTrackLicenseList**
> DownloadHistoryDataList getTrackLicenseList(audioId, license, page, perPage, sort, username, startDate, endDate, downloadAvailability, teamHistory)

List audio licenses

This endpoint lists existing licenses. You can filter the results according to the track ID to see if you have an existing license for a specific track.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AudioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    AudioApi apiInstance = new AudioApi(defaultClient);
    String audioId = "1"; // String | Show licenses for the specified track ID
    String license = "48433107"; // String | Restrict results by license. Prepending a `-` sign will exclude results by license
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    String sort = "newest"; // String | Sort order
    String username = "aUniqueUsername"; // String | Filter licenses by username of licensee
    OffsetDateTime startDate = OffsetDateTime.parse("2021-03-29T13:25:13.521Z"); // OffsetDateTime | Show licenses created on or after the specified date
    OffsetDateTime endDate = OffsetDateTime.parse("2021-03-29T13:25:13.521Z"); // OffsetDateTime | Show licenses created before the specified date
    String downloadAvailability = "all"; // String | Filter licenses by download availability
    Boolean teamHistory = false; // Boolean | Set to true to see license history for all members of your team.
    try {
      DownloadHistoryDataList result = apiInstance.getTrackLicenseList(audioId, license, page, perPage, sort, username, startDate, endDate, downloadAvailability, teamHistory);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudioApi#getTrackLicenseList");
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
| **audioId** | **String**| Show licenses for the specified track ID | [optional] |
| **license** | **String**| Restrict results by license. Prepending a &#x60;-&#x60; sign will exclude results by license | [optional] |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **sort** | **String**| Sort order | [optional] [default to newest] [enum: newest, oldest] |
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

<a id="getTrackList"></a>
# **getTrackList**
> AudioDataList getTrackList(id, view, searchId)

List audio tracks

This endpoint lists information about one or more audio tracks, including the description and publication date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AudioApi;

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

    AudioApi apiInstance = new AudioApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | One or more audio IDs
    String view = "minimal"; // String | Amount of detail to render in the response
    String searchId = "00000000-0000-0000-0000-000000000000"; // String | The ID of the search that is related to this request
    try {
      AudioDataList result = apiInstance.getTrackList(id, view, searchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudioApi#getTrackList");
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
| **id** | [**List&lt;String&gt;**](String.md)| One or more audio IDs | |
| **view** | **String**| Amount of detail to render in the response | [optional] [default to minimal] [enum: minimal, full] |
| **searchId** | **String**| The ID of the search that is related to this request | [optional] |

### Return type

[**AudioDataList**](AudioDataList.md)

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

<a id="licenseTrack"></a>
# **licenseTrack**
> LicenseAudioResultDataList licenseTrack(licenseAudioRequest, license, searchId)

License audio tracks

This endpoint gets licenses for one or more tracks. The download links in the response are valid for 8 hours.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AudioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    AudioApi apiInstance = new AudioApi(defaultClient);
    LicenseAudioRequest licenseAudioRequest = new LicenseAudioRequest(); // LicenseAudioRequest | Tracks to license
    String license = "audio_platform"; // String | License type
    String searchId = "p5S6QwRikdFJTHXwsoiqTg"; // String | The ID of the search that led to licensing this track
    try {
      LicenseAudioResultDataList result = apiInstance.licenseTrack(licenseAudioRequest, license, searchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudioApi#licenseTrack");
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
| **licenseAudioRequest** | [**LicenseAudioRequest**](LicenseAudioRequest.md)| Tracks to license | |
| **license** | **String**| License type | [optional] [enum: audio_platform, premier_music_basic, premier_music_extended, premier_music_pro, premier_music_comp, asset_all_music] |
| **searchId** | **String**| The ID of the search that led to licensing this track | [optional] |

### Return type

[**LicenseAudioResultDataList**](LicenseAudioResultDataList.md)

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

<a id="listGenres"></a>
# **listGenres**
> GenreList listGenres(language)

List audio genres

This endpoint returns a list of all audio genres.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AudioApi;

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

    AudioApi apiInstance = new AudioApi(defaultClient);
    String language = "language_example"; // String | Which language the genres will be returned
    try {
      GenreList result = apiInstance.listGenres(language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudioApi#listGenres");
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
| **language** | **String**| Which language the genres will be returned | [optional] |

### Return type

[**GenreList**](GenreList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listInstruments"></a>
# **listInstruments**
> InstrumentList listInstruments(language)

List audio instruments

This endpoint returns a list of all audio instruments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AudioApi;

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

    AudioApi apiInstance = new AudioApi(defaultClient);
    String language = "language_example"; // String | Which language the instruments will be returned in
    try {
      InstrumentList result = apiInstance.listInstruments(language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudioApi#listInstruments");
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
| **language** | **String**| Which language the instruments will be returned in | [optional] |

### Return type

[**InstrumentList**](InstrumentList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listMoods"></a>
# **listMoods**
> MoodList listMoods(language)

List audio moods

This endpoint returns a list of all audio moods.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AudioApi;

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

    AudioApi apiInstance = new AudioApi(defaultClient);
    String language = "language_example"; // String | Which language the moods will be returned in
    try {
      MoodList result = apiInstance.listMoods(language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudioApi#listMoods");
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
| **language** | **String**| Which language the moods will be returned in | [optional] |

### Return type

[**MoodList**](MoodList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="renameTrackCollection"></a>
# **renameTrackCollection**
> renameTrackCollection(id, collectionUpdateRequest)

Rename audio collections

This endpoint sets a new name for a collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AudioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    AudioApi apiInstance = new AudioApi(defaultClient);
    String id = "48433107"; // String | Collection ID
    CollectionUpdateRequest collectionUpdateRequest = new CollectionUpdateRequest(); // CollectionUpdateRequest | Collection changes
    try {
      apiInstance.renameTrackCollection(id, collectionUpdateRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudioApi#renameTrackCollection");
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
| **collectionUpdateRequest** | [**CollectionUpdateRequest**](CollectionUpdateRequest.md)| Collection changes | |

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

<a id="searchTracks"></a>
# **searchTracks**
> AudioSearchResults searchTracks(artists, bpm, bpmFrom, bpmTo, duration, durationFrom, durationTo, genre, isInstrumental, instruments, moods, page, perPage, query, sort, sortOrder, vocalDescription, view, fields, library, language)

Search for tracks

This endpoint searches for tracks. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AudioApi;

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

    AudioApi apiInstance = new AudioApi(defaultClient);
    List<String> artists = Arrays.asList(); // List<String> | Show tracks with one of the specified artist names or IDs
    Integer bpm = 56; // Integer | (Deprecated; use bpm_from and bpm_to instead) Show tracks with the specified beats per minute
    Integer bpmFrom = 80; // Integer | Show tracks with the specified beats per minute or faster
    Integer bpmTo = 120; // Integer | Show tracks with the specified beats per minute or slower
    Integer duration = 180; // Integer | Show tracks with the specified duration in seconds
    Integer durationFrom = 30; // Integer | Show tracks with the specified duration or longer in seconds
    Integer durationTo = 180; // Integer | Show tracks with the specified duration or shorter in seconds
    List<String> genre = Arrays.asList(); // List<String> | Show tracks with each of the specified genres; to get the list of genres, use `GET /v2/audio/genres`
    Boolean isInstrumental = true; // Boolean | Show instrumental music only
    List<String> instruments = Arrays.asList(); // List<String> | Show tracks with each of the specified instruments; to get the list of instruments, use `GET /v2/audio/instruments`
    List<String> moods = Arrays.asList(); // List<String> | Show tracks with each of the specified moods; to get the list of moods, use `GET /v2/audio/moods`
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    String query = "drum"; // String | One or more search terms separated by spaces
    String sort = "score"; // String | Sort by
    String sortOrder = "asc"; // String | Sort order
    String vocalDescription = "female"; // String | Show tracks with the specified vocal description (male, female)
    String view = "minimal"; // String | Amount of detail to render in the response
    String fields = "fields_example"; // String | Fields to display in the response; see the documentation for the fields parameter in the overview section
    String library = "shutterstock"; // String | Which library to search
    String language = "language_example"; // String | Which language to search in
    try {
      AudioSearchResults result = apiInstance.searchTracks(artists, bpm, bpmFrom, bpmTo, duration, durationFrom, durationTo, genre, isInstrumental, instruments, moods, page, perPage, query, sort, sortOrder, vocalDescription, view, fields, library, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudioApi#searchTracks");
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
| **artists** | [**List&lt;String&gt;**](String.md)| Show tracks with one of the specified artist names or IDs | [optional] |
| **bpm** | **Integer**| (Deprecated; use bpm_from and bpm_to instead) Show tracks with the specified beats per minute | [optional] |
| **bpmFrom** | **Integer**| Show tracks with the specified beats per minute or faster | [optional] |
| **bpmTo** | **Integer**| Show tracks with the specified beats per minute or slower | [optional] |
| **duration** | **Integer**| Show tracks with the specified duration in seconds | [optional] |
| **durationFrom** | **Integer**| Show tracks with the specified duration or longer in seconds | [optional] |
| **durationTo** | **Integer**| Show tracks with the specified duration or shorter in seconds | [optional] |
| **genre** | [**List&lt;String&gt;**](String.md)| Show tracks with each of the specified genres; to get the list of genres, use &#x60;GET /v2/audio/genres&#x60; | [optional] |
| **isInstrumental** | **Boolean**| Show instrumental music only | [optional] |
| **instruments** | [**List&lt;String&gt;**](String.md)| Show tracks with each of the specified instruments; to get the list of instruments, use &#x60;GET /v2/audio/instruments&#x60; | [optional] |
| **moods** | [**List&lt;String&gt;**](String.md)| Show tracks with each of the specified moods; to get the list of moods, use &#x60;GET /v2/audio/moods&#x60; | [optional] |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **query** | **String**| One or more search terms separated by spaces | [optional] |
| **sort** | **String**| Sort by | [optional] [enum: score, ranking_all, artist, title, bpm, freshness, duration] |
| **sortOrder** | **String**| Sort order | [optional] [default to desc] [enum: asc, desc] |
| **vocalDescription** | **String**| Show tracks with the specified vocal description (male, female) | [optional] |
| **view** | **String**| Amount of detail to render in the response | [optional] [default to minimal] [enum: minimal, full] |
| **fields** | **String**| Fields to display in the response; see the documentation for the fields parameter in the overview section | [optional] |
| **library** | **String**| Which library to search | [optional] [default to premier] [enum: shutterstock, premier] |
| **language** | **String**| Which language to search in | [optional] |

### Return type

[**AudioSearchResults**](AudioSearchResults.md)

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

