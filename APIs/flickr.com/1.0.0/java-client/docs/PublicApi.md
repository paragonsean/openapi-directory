# PublicApi

All URIs are relative to *https://api.flickr.com/services*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**echo**](PublicApi.md#echo) | **GET** /rest?method&#x3D;flickr.test.echo |  |
| [**getAccessToken**](PublicApi.md#getAccessToken) | **GET** /oauth/access_token |  |
| [**getAlbumByID**](PublicApi.md#getAlbumByID) | **GET** /rest?method&#x3D;flickr.photosets.getPhotos |  |
| [**getAlbumContextByID**](PublicApi.md#getAlbumContextByID) | **GET** /rest?method&#x3D;flickr.photosets.getContext |  |
| [**getAlbumsByPersonID**](PublicApi.md#getAlbumsByPersonID) | **GET** /rest?method&#x3D;flickr.photosets.getList |  |
| [**getFavoritesByPersonID**](PublicApi.md#getFavoritesByPersonID) | **GET** /rest?method&#x3D;flickr.favorites.getList |  |
| [**getFavoritesContextByID**](PublicApi.md#getFavoritesContextByID) | **GET** /rest?method&#x3D;flickr.favorites.getContext |  |
| [**getGalleryPhotosByID**](PublicApi.md#getGalleryPhotosByID) | **GET** /rest?method&#x3D;flickr.galleries.getPhotos |  |
| [**getGroupByID**](PublicApi.md#getGroupByID) | **GET** /rest?method&#x3D;flickr.groups.getInfo |  |
| [**getGroupDiscussionsByID**](PublicApi.md#getGroupDiscussionsByID) | **GET** /rest?method&#x3D;flickr.groups.discuss.topics.getList |  |
| [**getGroupPhotosByID**](PublicApi.md#getGroupPhotosByID) | **GET** /rest?method&#x3D;flickr.groups.pools.getPhotos |  |
| [**getGroupTopicByID**](PublicApi.md#getGroupTopicByID) | **GET** /rest?method&#x3D;flickr.groups.discuss.topics.getInfo |  |
| [**getGroupTopicRepliesByID**](PublicApi.md#getGroupTopicRepliesByID) | **GET** /rest?method&#x3D;flickr.groups.discuss.replies.getInfo |  |
| [**getLicenseByID**](PublicApi.md#getLicenseByID) | **GET** /rest?method&#x3D;flickr.photos.licenses.getInfo |  |
| [**getMediaByPersonID**](PublicApi.md#getMediaByPersonID) | **GET** /rest?method&#x3D;flickr.people.getPhotos |  |
| [**getMediaBySearch**](PublicApi.md#getMediaBySearch) | **GET** /rest?method&#x3D;flickr.photos.search |  |
| [**getPersonByID**](PublicApi.md#getPersonByID) | **GET** /rest?method&#x3D;flickr.people.getInfo |  |
| [**getPhotoByID**](PublicApi.md#getPhotoByID) | **GET** /rest?method&#x3D;flickr.photos.getInfo |  |
| [**getPhotoExifByID**](PublicApi.md#getPhotoExifByID) | **GET** /rest?method&#x3D;flickr.photos.getExif |  |
| [**getPhotoSizesByID**](PublicApi.md#getPhotoSizesByID) | **GET** /rest?method&#x3D;flickr.photos.getSizes |  |
| [**getPhotolistContextByID**](PublicApi.md#getPhotolistContextByID) | **GET** /rest?method&#x3D;flickr.photolist.getContext |  |
| [**getPhotostreamContextByID**](PublicApi.md#getPhotostreamContextByID) | **GET** /rest?method&#x3D;flickr.photos.getContext |  |
| [**getRequestToken**](PublicApi.md#getRequestToken) | **GET** /oauth/request_token |  |
| [**restmethodflickrGroupsPoolsGetContextGet**](PublicApi.md#restmethodflickrGroupsPoolsGetContextGet) | **GET** /rest?method&#x3D;flickr.groups.pools.getContext |  |
| [**uploadPhoto**](PublicApi.md#uploadPhoto) | **POST** /upload |  |


<a id="echo"></a>
# **echo**
> Echo200Response echo(apiKey, echo)



Echos the input parameters back in the response

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String echo = "echo_example"; // String | 
    try {
      Echo200Response result = apiInstance.echo(apiKey, echo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#echo");
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
| **apiKey** | **String**|  | |
| **echo** | **String**|  | [optional] |

### Return type

[**Echo200Response**](Echo200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getAccessToken"></a>
# **getAccessToken**
> String getAccessToken(oauthConsumerKey, oauthNonce, oauthTimestamp, oauthSignatureMethod, oauthVersion, oauthSignature, oauthVerifier, oauthToken)



Returns an access token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String oauthConsumerKey = "oauthConsumerKey_example"; // String | 
    String oauthNonce = "oauthNonce_example"; // String | 
    String oauthTimestamp = "oauthTimestamp_example"; // String | 
    String oauthSignatureMethod = "oauthSignatureMethod_example"; // String | 
    String oauthVersion = "oauthVersion_example"; // String | 
    String oauthSignature = "oauthSignature_example"; // String | 
    String oauthVerifier = "oauthVerifier_example"; // String | 
    String oauthToken = "oauthToken_example"; // String | 
    try {
      String result = apiInstance.getAccessToken(oauthConsumerKey, oauthNonce, oauthTimestamp, oauthSignatureMethod, oauthVersion, oauthSignature, oauthVerifier, oauthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getAccessToken");
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
| **oauthConsumerKey** | **String**|  | |
| **oauthNonce** | **String**|  | |
| **oauthTimestamp** | **String**|  | |
| **oauthSignatureMethod** | **String**|  | |
| **oauthVersion** | **String**|  | |
| **oauthSignature** | **String**|  | |
| **oauthVerifier** | **String**|  | |
| **oauthToken** | **String**|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getAlbumByID"></a>
# **getAlbumByID**
> GetAlbumByID200Response getAlbumByID(apiKey, photosetId)



Returns a list of photos in an album.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String photosetId = "photosetId_example"; // String | 
    try {
      GetAlbumByID200Response result = apiInstance.getAlbumByID(apiKey, photosetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getAlbumByID");
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
| **apiKey** | **String**|  | |
| **photosetId** | **String**|  | |

### Return type

[**GetAlbumByID200Response**](GetAlbumByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getAlbumContextByID"></a>
# **getAlbumContextByID**
> GetFavoritesContextByID200Response getAlbumContextByID(apiKey, photoId, photosetId)



Returns next and previous photos for a photo in a set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String photoId = "photoId_example"; // String | 
    String photosetId = "photosetId_example"; // String | 
    try {
      GetFavoritesContextByID200Response result = apiInstance.getAlbumContextByID(apiKey, photoId, photosetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getAlbumContextByID");
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
| **apiKey** | **String**|  | |
| **photoId** | **String**|  | |
| **photosetId** | **String**|  | [optional] |

### Return type

[**GetFavoritesContextByID200Response**](GetFavoritesContextByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getAlbumsByPersonID"></a>
# **getAlbumsByPersonID**
> GetAlbumsByPersonID200Response getAlbumsByPersonID(apiKey, userId, page, perPage)



Returns the albums belonging to the specified user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String userId = "userId_example"; // String | 
    BigDecimal page = new BigDecimal(78); // BigDecimal | 
    BigDecimal perPage = new BigDecimal(78); // BigDecimal | 
    try {
      GetAlbumsByPersonID200Response result = apiInstance.getAlbumsByPersonID(apiKey, userId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getAlbumsByPersonID");
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
| **apiKey** | **String**|  | |
| **userId** | **String**|  | |
| **page** | **BigDecimal**|  | [optional] |
| **perPage** | **BigDecimal**|  | [optional] |

### Return type

[**GetAlbumsByPersonID200Response**](GetAlbumsByPersonID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getFavoritesByPersonID"></a>
# **getFavoritesByPersonID**
> GetFavoritesByPersonID200Response getFavoritesByPersonID(apiKey, userId, minFaveDate, maxFaveDate, page, perPage)



Returns a list of the user&#39;s favorite photos. Only photos which the calling user has permission to see are returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String userId = "userId_example"; // String | 
    BigDecimal minFaveDate = new BigDecimal(78); // BigDecimal | 
    BigDecimal maxFaveDate = new BigDecimal(78); // BigDecimal | 
    BigDecimal page = new BigDecimal(78); // BigDecimal | 
    BigDecimal perPage = new BigDecimal(78); // BigDecimal | 
    try {
      GetFavoritesByPersonID200Response result = apiInstance.getFavoritesByPersonID(apiKey, userId, minFaveDate, maxFaveDate, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getFavoritesByPersonID");
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
| **apiKey** | **String**|  | |
| **userId** | **String**|  | |
| **minFaveDate** | **BigDecimal**|  | [optional] |
| **maxFaveDate** | **BigDecimal**|  | [optional] |
| **page** | **BigDecimal**|  | [optional] |
| **perPage** | **BigDecimal**|  | [optional] |

### Return type

[**GetFavoritesByPersonID200Response**](GetFavoritesByPersonID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getFavoritesContextByID"></a>
# **getFavoritesContextByID**
> GetFavoritesContextByID200Response getFavoritesContextByID(apiKey, photoId, userId)



Returns next and previous favorites for a photo in a user&#39;s favorites

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String photoId = "photoId_example"; // String | 
    String userId = "userId_example"; // String | 
    try {
      GetFavoritesContextByID200Response result = apiInstance.getFavoritesContextByID(apiKey, photoId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getFavoritesContextByID");
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
| **apiKey** | **String**|  | |
| **photoId** | **String**|  | |
| **userId** | **String**|  | [optional] |

### Return type

[**GetFavoritesContextByID200Response**](GetFavoritesContextByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getGalleryPhotosByID"></a>
# **getGalleryPhotosByID**
> GetGalleryPhotosByID200Response getGalleryPhotosByID(apiKey, galleryId)



Returns a list of photos in a gallery.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String galleryId = "galleryId_example"; // String | 
    try {
      GetGalleryPhotosByID200Response result = apiInstance.getGalleryPhotosByID(apiKey, galleryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getGalleryPhotosByID");
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
| **apiKey** | **String**|  | |
| **galleryId** | **String**|  | |

### Return type

[**GetGalleryPhotosByID200Response**](GetGalleryPhotosByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getGroupByID"></a>
# **getGroupByID**
> GetGroupByID200Response getGroupByID(apiKey, groupId, groupPathAlias, lang)



Get information about a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String groupId = "groupId_example"; // String | 
    String groupPathAlias = "groupPathAlias_example"; // String | 
    String lang = "lang_example"; // String | 
    try {
      GetGroupByID200Response result = apiInstance.getGroupByID(apiKey, groupId, groupPathAlias, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getGroupByID");
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
| **apiKey** | **String**|  | |
| **groupId** | **String**|  | [optional] |
| **groupPathAlias** | **String**|  | [optional] |
| **lang** | **String**|  | [optional] |

### Return type

[**GetGroupByID200Response**](GetGroupByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getGroupDiscussionsByID"></a>
# **getGroupDiscussionsByID**
> GetGroupDiscussionsByID200Response getGroupDiscussionsByID(apiKey, groupId, page, perPage)



Get a list of discussion topics in a group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String groupId = "groupId_example"; // String | 
    BigDecimal page = new BigDecimal(78); // BigDecimal | 
    BigDecimal perPage = new BigDecimal(78); // BigDecimal | 
    try {
      GetGroupDiscussionsByID200Response result = apiInstance.getGroupDiscussionsByID(apiKey, groupId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getGroupDiscussionsByID");
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
| **apiKey** | **String**|  | |
| **groupId** | **String**|  | [optional] |
| **page** | **BigDecimal**|  | [optional] |
| **perPage** | **BigDecimal**|  | [optional] |

### Return type

[**GetGroupDiscussionsByID200Response**](GetGroupDiscussionsByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getGroupPhotosByID"></a>
# **getGroupPhotosByID**
> GetGalleryPhotosByID200Response getGroupPhotosByID(apiKey, groupId)



Returns a list of pool photos for a given group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String groupId = "groupId_example"; // String | 
    try {
      GetGalleryPhotosByID200Response result = apiInstance.getGroupPhotosByID(apiKey, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getGroupPhotosByID");
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
| **apiKey** | **String**|  | |
| **groupId** | **String**|  | [optional] |

### Return type

[**GetGalleryPhotosByID200Response**](GetGalleryPhotosByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getGroupTopicByID"></a>
# **getGroupTopicByID**
> GetGroupTopicByID200Response getGroupTopicByID(apiKey, topicId, groupId)



Get information about a group discussion topic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String topicId = "topicId_example"; // String | 
    String groupId = "groupId_example"; // String | 
    try {
      GetGroupTopicByID200Response result = apiInstance.getGroupTopicByID(apiKey, topicId, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getGroupTopicByID");
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
| **apiKey** | **String**|  | |
| **topicId** | **String**|  | |
| **groupId** | **String**|  | [optional] |

### Return type

[**GetGroupTopicByID200Response**](GetGroupTopicByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getGroupTopicRepliesByID"></a>
# **getGroupTopicRepliesByID**
> GetGroupTopicRepliesByID200Response getGroupTopicRepliesByID(apiKey, topicId, replyId, groupId)



Get information on a group topic reply

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String topicId = "topicId_example"; // String | 
    String replyId = "replyId_example"; // String | 
    String groupId = "groupId_example"; // String | 
    try {
      GetGroupTopicRepliesByID200Response result = apiInstance.getGroupTopicRepliesByID(apiKey, topicId, replyId, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getGroupTopicRepliesByID");
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
| **apiKey** | **String**|  | |
| **topicId** | **String**|  | |
| **replyId** | **String**|  | |
| **groupId** | **String**|  | [optional] |

### Return type

[**GetGroupTopicRepliesByID200Response**](GetGroupTopicRepliesByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getLicenseByID"></a>
# **getLicenseByID**
> GetLicenseByID200Response getLicenseByID(apiKey)



Fetches a list of available photo licenses for Flickr

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    try {
      GetLicenseByID200Response result = apiInstance.getLicenseByID(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getLicenseByID");
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
| **apiKey** | **String**|  | |

### Return type

[**GetLicenseByID200Response**](GetLicenseByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getMediaByPersonID"></a>
# **getMediaByPersonID**
> GetFavoritesByPersonID200Response getMediaByPersonID(apiKey, userId, safeSearch, minUploadDate, maxUploadDate, minTakenDate, maxTakenDate, contentType, privacyFilter, page, perPage)



Return photos from the given user&#39;s photostream

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String userId = "userId_example"; // String | 
    BigDecimal safeSearch = new BigDecimal(78); // BigDecimal | 
    BigDecimal minUploadDate = new BigDecimal(78); // BigDecimal | 
    BigDecimal maxUploadDate = new BigDecimal(78); // BigDecimal | 
    BigDecimal minTakenDate = new BigDecimal(78); // BigDecimal | 
    BigDecimal maxTakenDate = new BigDecimal(78); // BigDecimal | 
    BigDecimal contentType = new BigDecimal(78); // BigDecimal | 
    BigDecimal privacyFilter = new BigDecimal(78); // BigDecimal | 
    BigDecimal page = new BigDecimal(78); // BigDecimal | 
    BigDecimal perPage = new BigDecimal(78); // BigDecimal | 
    try {
      GetFavoritesByPersonID200Response result = apiInstance.getMediaByPersonID(apiKey, userId, safeSearch, minUploadDate, maxUploadDate, minTakenDate, maxTakenDate, contentType, privacyFilter, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getMediaByPersonID");
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
| **apiKey** | **String**|  | |
| **userId** | **String**|  | |
| **safeSearch** | **BigDecimal**|  | [optional] |
| **minUploadDate** | **BigDecimal**|  | [optional] |
| **maxUploadDate** | **BigDecimal**|  | [optional] |
| **minTakenDate** | **BigDecimal**|  | [optional] |
| **maxTakenDate** | **BigDecimal**|  | [optional] |
| **contentType** | **BigDecimal**|  | [optional] |
| **privacyFilter** | **BigDecimal**|  | [optional] |
| **page** | **BigDecimal**|  | [optional] |
| **perPage** | **BigDecimal**|  | [optional] |

### Return type

[**GetFavoritesByPersonID200Response**](GetFavoritesByPersonID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getMediaBySearch"></a>
# **getMediaBySearch**
> GetFavoritesByPersonID200Response getMediaBySearch(apiKey, text, tags, userId, minUploadDate, maxUploadDate, minTakenDate, maxTakenDate, license, sort, privacyFilter, bbox, accuracy, safeSearch, contentType, machineTags, machineTagMode, groupId, contacts, woeId, placeId, media, hasGeo, geoContext, lat, lon, radius, radiusUnits, isCommons, inGallery, isGetty, perPage, page)



Return a list of photos matching some criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String text = "text_example"; // String | A free text search. Photos who's title, description or tags contain the text will be returned. You can exclude results that match a term by prepending it with a - character.
    String tags = "tags_example"; // String | A comma-delimited list of tags. Photos with one or more of the tags listed will be returned. You can exclude results that match a term by prepending it with a - character.
    String userId = "userId_example"; // String | The NSID of the user who's photo to search. If this parameter isn't passed then everybody's public photos will be searched. A value of \"me\" will search against the calling user's photos for authenticated calls.
    String minUploadDate = "minUploadDate_example"; // String | Minimum upload date. Photos with an upload date greater than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime.
    String maxUploadDate = "maxUploadDate_example"; // String | Maximum upload date. Photos with an upload date less than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime.
    String minTakenDate = "minTakenDate_example"; // String | Minimum taken date. Photos with an taken date greater than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp.
    String maxTakenDate = "maxTakenDate_example"; // String | Maximum taken date. Photos with an taken date less than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp.
    String license = "license_example"; // String | The license id for photos (for possible values see the flickr.photos.licenses.getInfo method). Multiple licenses may be comma-separated.
    String sort = "sort_example"; // String | The order in which to sort returned photos. Deafults to date-posted-desc (unless you are doing a radial geo query, in which case the default sorting is by ascending distance from the point specified). The possible values are:   date-posted-asc,   date-posted-desc,   date-taken-asc,   date-taken-desc,   interestingness-desc,   interestingness-asc, and   relevance. 
    BigDecimal privacyFilter = new BigDecimal(78); // BigDecimal | Return photos only matching a certain privacy level. This only applies when making an authenticated call to view photos you own. Valid values are:,   1: public photos,   2: private photos visible to friends,   3: private photos visible to family,   4: private photos visible to friends & family,   5: completely private photos 
    String bbox = "bbox_example"; // String | A comma-delimited list of 4 values defining the Bounding Box of the area that will be searched.
    String accuracy = "accuracy_example"; // String | Recorded accuracy level of the location information. Current range is 1-16:   World level is 1   Country is ~3   Region is ~6   City is ~11   Street is ~16 
    BigDecimal safeSearch = new BigDecimal(78); // BigDecimal | Safe search setting:   1: for safe,   2: for moderate,   3: for restricted 
    BigDecimal contentType = new BigDecimal(78); // BigDecimal | Content Type setting:   1: photos only.   2: screenshots only.   3: 'other' only.   4: photos and screenshots.   5: screenshots and 'other'.   6: photos and 'other'.   7: photos, screenshots, and 'other' (all). 
    String machineTags = "machineTags_example"; // String | Aside from passing in a fully formed machine tag, there is a special syntax for searching on specific properties : Find photos using the 'dc' namespace : \"machine_tags\" => \"dc:\" Find photos with a title in the 'dc' namespace : \"machine_tags\" => \"dc:title=\" Find photos titled \"mr. camera\" in the 'dc' namespace : \"machine_tags\" => \"dc:title=\\\"mr. camera\\\" Find photos whose value is \"mr. camera\" : \"machine_tags\" => \"*:*=\\\"mr. camera\\\"\" Find photos that have a title, in any namespace : \"machine_tags\" => \"*:title=\" Find photos that have a title, in any namespace, whose value is \"mr. camera\" : \"machine_tags\" => \"*:title=\\\"mr. camera\\\"\" Find photos, in the 'dc' namespace whose value is \"mr. camera\" : \"machine_tags\" => \"dc:*=\\\"mr. camera\\\"\" Multiple machine tags may be queried by passing a comma-separated list. The number of machine tags you can pass in a single query depends on the tag mode (AND or OR) that you are querying with. \"AND\" queries are limited to (16) machine tags. \"OR\" queries are limited to (8). 
    String machineTagMode = "machineTagMode_example"; // String | Either 'any' for an OR combination of tags, or 'all' for an AND combination. Defaults to 'any' if not specified.
    String groupId = "groupId_example"; // String | The id of a group who's pool to search. If specified, only matching photos posted to the group's pool will be returned.
    String contacts = "contacts_example"; // String | Search your contacts. Either 'all' or 'ff' for just friends and family. (Experimental)
    String woeId = "woeId_example"; // String | A 32-bit identifier that uniquely represents spatial entities. (not used if bbox argument is present).
    String placeId = "placeId_example"; // String | A Flickr place id. (not used if bbox argument is present). Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \"parameterless searches\" for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future). 
    String media = "media_example"; // String | Filter results by media type. Possible values are all (default), photos or videos
    String hasGeo = "hasGeo_example"; // String | Any photo that has been geotagged, or if the value is \"0\" any photo that has not been geotagged. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \"parameterless searches\" for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future). 
    String geoContext = "geoContext_example"; // String | Geo context is a numeric value representing the photo's geotagginess beyond latitude and longitude. For example, you may wish to search for photos that were taken \"indoors\" or \"outdoors\". The current list of context IDs is: 0, not defined. 1, indoors. 2, outdoors. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \"parameterless searches\" for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future). 
    String lat = "lat_example"; // String | A valid latitude, in decimal format, for doing radial geo queries. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \"parameterless searches\" for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future). 
    String lon = "lon_example"; // String | A valid longitude, in decimal format, for doing radial geo queries. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \"parameterless searches\" for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future). 
    BigDecimal radius = new BigDecimal(78); // BigDecimal | A valid radius used for geo queries, greater than zero and less than 20 miles (or 32 kilometers), for use with point-based geo queries. The default value is 5 (km).
    String radiusUnits = "radiusUnits_example"; // String | The unit of measure when doing radial geo queries. Valid options are \"mi\" (miles) and \"km\" (kilometers). The default is \"km\".
    Boolean isCommons = true; // Boolean | Limit the scope of the search to only photos that are part of the Flickr Commons project. Default is false.
    Boolean inGallery = true; // Boolean | Limit the scope of the search to only photos that are in a gallery? Default is false, search all photos.
    Boolean isGetty = true; // Boolean | Limit the scope of the search to only photos that are for sale on Getty. Default is false.
    BigDecimal perPage = new BigDecimal(78); // BigDecimal | Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.
    BigDecimal page = new BigDecimal(78); // BigDecimal | The page of results to return. If this argument is omitted, it defaults to 1.
    try {
      GetFavoritesByPersonID200Response result = apiInstance.getMediaBySearch(apiKey, text, tags, userId, minUploadDate, maxUploadDate, minTakenDate, maxTakenDate, license, sort, privacyFilter, bbox, accuracy, safeSearch, contentType, machineTags, machineTagMode, groupId, contacts, woeId, placeId, media, hasGeo, geoContext, lat, lon, radius, radiusUnits, isCommons, inGallery, isGetty, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getMediaBySearch");
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
| **apiKey** | **String**|  | |
| **text** | **String**| A free text search. Photos who&#39;s title, description or tags contain the text will be returned. You can exclude results that match a term by prepending it with a - character. | [optional] |
| **tags** | **String**| A comma-delimited list of tags. Photos with one or more of the tags listed will be returned. You can exclude results that match a term by prepending it with a - character. | [optional] |
| **userId** | **String**| The NSID of the user who&#39;s photo to search. If this parameter isn&#39;t passed then everybody&#39;s public photos will be searched. A value of \&quot;me\&quot; will search against the calling user&#39;s photos for authenticated calls. | [optional] |
| **minUploadDate** | **String**| Minimum upload date. Photos with an upload date greater than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime. | [optional] |
| **maxUploadDate** | **String**| Maximum upload date. Photos with an upload date less than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime. | [optional] |
| **minTakenDate** | **String**| Minimum taken date. Photos with an taken date greater than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp. | [optional] |
| **maxTakenDate** | **String**| Maximum taken date. Photos with an taken date less than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp. | [optional] |
| **license** | **String**| The license id for photos (for possible values see the flickr.photos.licenses.getInfo method). Multiple licenses may be comma-separated. | [optional] |
| **sort** | **String**| The order in which to sort returned photos. Deafults to date-posted-desc (unless you are doing a radial geo query, in which case the default sorting is by ascending distance from the point specified). The possible values are:   date-posted-asc,   date-posted-desc,   date-taken-asc,   date-taken-desc,   interestingness-desc,   interestingness-asc, and   relevance.  | [optional] |
| **privacyFilter** | **BigDecimal**| Return photos only matching a certain privacy level. This only applies when making an authenticated call to view photos you own. Valid values are:,   1: public photos,   2: private photos visible to friends,   3: private photos visible to family,   4: private photos visible to friends &amp; family,   5: completely private photos  | [optional] |
| **bbox** | **String**| A comma-delimited list of 4 values defining the Bounding Box of the area that will be searched. | [optional] |
| **accuracy** | **String**| Recorded accuracy level of the location information. Current range is 1-16:   World level is 1   Country is ~3   Region is ~6   City is ~11   Street is ~16  | [optional] |
| **safeSearch** | **BigDecimal**| Safe search setting:   1: for safe,   2: for moderate,   3: for restricted  | [optional] |
| **contentType** | **BigDecimal**| Content Type setting:   1: photos only.   2: screenshots only.   3: &#39;other&#39; only.   4: photos and screenshots.   5: screenshots and &#39;other&#39;.   6: photos and &#39;other&#39;.   7: photos, screenshots, and &#39;other&#39; (all).  | [optional] |
| **machineTags** | **String**| Aside from passing in a fully formed machine tag, there is a special syntax for searching on specific properties : Find photos using the &#39;dc&#39; namespace : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;dc:\&quot; Find photos with a title in the &#39;dc&#39; namespace : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;dc:title&#x3D;\&quot; Find photos titled \&quot;mr. camera\&quot; in the &#39;dc&#39; namespace : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;dc:title&#x3D;\\\&quot;mr. camera\\\&quot; Find photos whose value is \&quot;mr. camera\&quot; : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;*:*&#x3D;\\\&quot;mr. camera\\\&quot;\&quot; Find photos that have a title, in any namespace : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;*:title&#x3D;\&quot; Find photos that have a title, in any namespace, whose value is \&quot;mr. camera\&quot; : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;*:title&#x3D;\\\&quot;mr. camera\\\&quot;\&quot; Find photos, in the &#39;dc&#39; namespace whose value is \&quot;mr. camera\&quot; : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;dc:*&#x3D;\\\&quot;mr. camera\\\&quot;\&quot; Multiple machine tags may be queried by passing a comma-separated list. The number of machine tags you can pass in a single query depends on the tag mode (AND or OR) that you are querying with. \&quot;AND\&quot; queries are limited to (16) machine tags. \&quot;OR\&quot; queries are limited to (8).  | [optional] |
| **machineTagMode** | **String**| Either &#39;any&#39; for an OR combination of tags, or &#39;all&#39; for an AND combination. Defaults to &#39;any&#39; if not specified. | [optional] |
| **groupId** | **String**| The id of a group who&#39;s pool to search. If specified, only matching photos posted to the group&#39;s pool will be returned. | [optional] |
| **contacts** | **String**| Search your contacts. Either &#39;all&#39; or &#39;ff&#39; for just friends and family. (Experimental) | [optional] |
| **woeId** | **String**| A 32-bit identifier that uniquely represents spatial entities. (not used if bbox argument is present). | [optional] |
| **placeId** | **String**| A Flickr place id. (not used if bbox argument is present). Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \&quot;parameterless searches\&quot; for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future).  | [optional] |
| **media** | **String**| Filter results by media type. Possible values are all (default), photos or videos | [optional] |
| **hasGeo** | **String**| Any photo that has been geotagged, or if the value is \&quot;0\&quot; any photo that has not been geotagged. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \&quot;parameterless searches\&quot; for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future).  | [optional] |
| **geoContext** | **String**| Geo context is a numeric value representing the photo&#39;s geotagginess beyond latitude and longitude. For example, you may wish to search for photos that were taken \&quot;indoors\&quot; or \&quot;outdoors\&quot;. The current list of context IDs is: 0, not defined. 1, indoors. 2, outdoors. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \&quot;parameterless searches\&quot; for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future).  | [optional] |
| **lat** | **String**| A valid latitude, in decimal format, for doing radial geo queries. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \&quot;parameterless searches\&quot; for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future).  | [optional] |
| **lon** | **String**| A valid longitude, in decimal format, for doing radial geo queries. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \&quot;parameterless searches\&quot; for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future).  | [optional] |
| **radius** | **BigDecimal**| A valid radius used for geo queries, greater than zero and less than 20 miles (or 32 kilometers), for use with point-based geo queries. The default value is 5 (km). | [optional] |
| **radiusUnits** | **String**| The unit of measure when doing radial geo queries. Valid options are \&quot;mi\&quot; (miles) and \&quot;km\&quot; (kilometers). The default is \&quot;km\&quot;. | [optional] |
| **isCommons** | **Boolean**| Limit the scope of the search to only photos that are part of the Flickr Commons project. Default is false. | [optional] |
| **inGallery** | **Boolean**| Limit the scope of the search to only photos that are in a gallery? Default is false, search all photos. | [optional] |
| **isGetty** | **Boolean**| Limit the scope of the search to only photos that are for sale on Getty. Default is false. | [optional] |
| **perPage** | **BigDecimal**| Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500. | [optional] |
| **page** | **BigDecimal**| The page of results to return. If this argument is omitted, it defaults to 1. | [optional] |

### Return type

[**GetFavoritesByPersonID200Response**](GetFavoritesByPersonID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getPersonByID"></a>
# **getPersonByID**
> GetPersonByID200Response getPersonByID(apiKey, userId)



Returns a person

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String userId = "userId_example"; // String | 
    try {
      GetPersonByID200Response result = apiInstance.getPersonByID(apiKey, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getPersonByID");
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
| **apiKey** | **String**|  | |
| **userId** | **String**|  | [optional] |

### Return type

[**GetPersonByID200Response**](GetPersonByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getPhotoByID"></a>
# **getPhotoByID**
> GetPhotoByID200Response getPhotoByID(apiKey, photoId)



Returns a photo

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String photoId = "photoId_example"; // String | 
    try {
      GetPhotoByID200Response result = apiInstance.getPhotoByID(apiKey, photoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getPhotoByID");
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
| **apiKey** | **String**|  | |
| **photoId** | **String**|  | |

### Return type

[**GetPhotoByID200Response**](GetPhotoByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a photo |  -  |

<a id="getPhotoExifByID"></a>
# **getPhotoExifByID**
> GetPhotoExifByID200Response getPhotoExifByID(apiKey, photoId, secret)



Retrieves a list of EXIF/TIFF/GPS tags for a given photo. The calling user must have permission to view the photo.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String photoId = "photoId_example"; // String | 
    String secret = "secret_example"; // String | 
    try {
      GetPhotoExifByID200Response result = apiInstance.getPhotoExifByID(apiKey, photoId, secret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getPhotoExifByID");
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
| **apiKey** | **String**|  | |
| **photoId** | **String**|  | |
| **secret** | **String**|  | [optional] |

### Return type

[**GetPhotoExifByID200Response**](GetPhotoExifByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getPhotoSizesByID"></a>
# **getPhotoSizesByID**
> GetPhotoSizesByID200Response getPhotoSizesByID(apiKey, photoId)



Returns photo sizes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String photoId = "photoId_example"; // String | 
    try {
      GetPhotoSizesByID200Response result = apiInstance.getPhotoSizesByID(apiKey, photoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getPhotoSizesByID");
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
| **apiKey** | **String**|  | |
| **photoId** | **String**|  | |

### Return type

[**GetPhotoSizesByID200Response**](GetPhotoSizesByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Photo sizes |  -  |

<a id="getPhotolistContextByID"></a>
# **getPhotolistContextByID**
> GetFavoritesContextByID200Response getPhotolistContextByID(apiKey, photoId, photolistId)



Returns next and previous photos in a photo list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String photoId = "photoId_example"; // String | 
    String photolistId = "photolistId_example"; // String | 
    try {
      GetFavoritesContextByID200Response result = apiInstance.getPhotolistContextByID(apiKey, photoId, photolistId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getPhotolistContextByID");
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
| **apiKey** | **String**|  | |
| **photoId** | **String**|  | |
| **photolistId** | **String**|  | |

### Return type

[**GetFavoritesContextByID200Response**](GetFavoritesContextByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getPhotostreamContextByID"></a>
# **getPhotostreamContextByID**
> GetFavoritesContextByID200Response getPhotostreamContextByID(apiKey, photoId)



Returns next and previous photos for a photo in a photostream

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String photoId = "photoId_example"; // String | 
    try {
      GetFavoritesContextByID200Response result = apiInstance.getPhotostreamContextByID(apiKey, photoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getPhotostreamContextByID");
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
| **apiKey** | **String**|  | |
| **photoId** | **String**|  | |

### Return type

[**GetFavoritesContextByID200Response**](GetFavoritesContextByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getRequestToken"></a>
# **getRequestToken**
> String getRequestToken(oauthConsumerKey, oauthNonce, oauthTimestamp, oauthSignatureMethod, oauthVersion, oauthSignature, oauthCallback)



Returns an oauth token and oauth token secret

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String oauthConsumerKey = "oauthConsumerKey_example"; // String | 
    String oauthNonce = "oauthNonce_example"; // String | 
    String oauthTimestamp = "oauthTimestamp_example"; // String | 
    String oauthSignatureMethod = "oauthSignatureMethod_example"; // String | 
    String oauthVersion = "oauthVersion_example"; // String | 
    String oauthSignature = "oauthSignature_example"; // String | 
    String oauthCallback = "oauthCallback_example"; // String | 
    try {
      String result = apiInstance.getRequestToken(oauthConsumerKey, oauthNonce, oauthTimestamp, oauthSignatureMethod, oauthVersion, oauthSignature, oauthCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#getRequestToken");
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
| **oauthConsumerKey** | **String**|  | |
| **oauthNonce** | **String**|  | |
| **oauthTimestamp** | **String**|  | |
| **oauthSignatureMethod** | **String**|  | |
| **oauthVersion** | **String**|  | |
| **oauthSignature** | **String**|  | |
| **oauthCallback** | **String**|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="restmethodflickrGroupsPoolsGetContextGet"></a>
# **restmethodflickrGroupsPoolsGetContextGet**
> GetFavoritesContextByID200Response restmethodflickrGroupsPoolsGetContextGet(apiKey, photoId, groupId)



Returns next and previous photos for a photo in a group pool

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String photoId = "photoId_example"; // String | 
    String groupId = "groupId_example"; // String | 
    try {
      GetFavoritesContextByID200Response result = apiInstance.restmethodflickrGroupsPoolsGetContextGet(apiKey, photoId, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#restmethodflickrGroupsPoolsGetContextGet");
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
| **apiKey** | **String**|  | |
| **photoId** | **String**|  | |
| **groupId** | **String**|  | [optional] |

### Return type

[**GetFavoritesContextByID200Response**](GetFavoritesContextByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="uploadPhoto"></a>
# **uploadPhoto**
> Object uploadPhoto(apiKey, photo, contentType, description, hidden, isFamily, isFriend, isPublic, safetyLevel, tags, title)



Uploads a new photo to Flickr

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flickr.com/services");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    File photo = new File("/path/to/file"); // File | 
    String contentType = "1"; // String | 
    String description = "description_example"; // String | 
    String hidden = "1"; // String | 
    String isFamily = "0"; // String | 
    String isFriend = "0"; // String | 
    String isPublic = "0"; // String | 
    String safetyLevel = "1"; // String | 
    String tags = "tags_example"; // String | 
    String title = "title_example"; // String | 
    try {
      Object result = apiInstance.uploadPhoto(apiKey, photo, contentType, description, hidden, isFamily, isFriend, isPublic, safetyLevel, tags, title);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#uploadPhoto");
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
| **apiKey** | **String**|  | |
| **photo** | **File**|  | |
| **contentType** | **String**|  | [optional] [enum: 1, 2, 3] |
| **description** | **String**|  | [optional] |
| **hidden** | **String**|  | [optional] [enum: 1, 2] |
| **isFamily** | **String**|  | [optional] [enum: 0, 1] |
| **isFriend** | **String**|  | [optional] [enum: 0, 1] |
| **isPublic** | **String**|  | [optional] [enum: 0, 1] |
| **safetyLevel** | **String**|  | [optional] [enum: 1, 2, 3] |
| **tags** | **String**|  | [optional] |
| **title** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

