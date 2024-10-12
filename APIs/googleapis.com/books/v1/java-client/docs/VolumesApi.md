# VolumesApi

All URIs are relative to *https://books.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**booksVolumesAssociatedList**](VolumesApi.md#booksVolumesAssociatedList) | **GET** /books/v1/volumes/{volumeId}/associated |  |
| [**booksVolumesGet**](VolumesApi.md#booksVolumesGet) | **GET** /books/v1/volumes/{volumeId} |  |
| [**booksVolumesList**](VolumesApi.md#booksVolumesList) | **GET** /books/v1/volumes |  |
| [**booksVolumesMybooksList**](VolumesApi.md#booksVolumesMybooksList) | **GET** /books/v1/volumes/mybooks |  |
| [**booksVolumesRecommendedList**](VolumesApi.md#booksVolumesRecommendedList) | **GET** /books/v1/volumes/recommended |  |
| [**booksVolumesRecommendedRate**](VolumesApi.md#booksVolumesRecommendedRate) | **POST** /books/v1/volumes/recommended/rate |  |
| [**booksVolumesUseruploadedList**](VolumesApi.md#booksVolumesUseruploadedList) | **GET** /books/v1/volumes/useruploaded |  |


<a id="booksVolumesAssociatedList"></a>
# **booksVolumesAssociatedList**
> Volumes booksVolumesAssociatedList(volumeId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, association, locale, maxAllowedMaturityRating, source)



Return a list of associated books.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://books.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    String volumeId = "volumeId_example"; // String | ID of the source volume.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String association = "ASSOCIATION_UNDEFINED"; // String | Association type.
    String locale = "locale_example"; // String | ISO-639-1 language and ISO-3166-1 country code. Ex: 'en_US'. Used for generating recommendations.
    String maxAllowedMaturityRating = "MAX_ALLOWED_MATURITY_RATING_UNDEFINED"; // String | The maximum allowed maturity rating of returned recommendations. Books with a higher maturity rating are filtered out.
    String source = "source_example"; // String | String to identify the originator of this request.
    try {
      Volumes result = apiInstance.booksVolumesAssociatedList(volumeId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, association, locale, maxAllowedMaturityRating, source);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#booksVolumesAssociatedList");
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
| **volumeId** | **String**| ID of the source volume. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **association** | **String**| Association type. | [optional] [enum: ASSOCIATION_UNDEFINED, end-of-sample, end-of-volume, related-for-play] |
| **locale** | **String**| ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;. Used for generating recommendations. | [optional] |
| **maxAllowedMaturityRating** | **String**| The maximum allowed maturity rating of returned recommendations. Books with a higher maturity rating are filtered out. | [optional] [enum: MAX_ALLOWED_MATURITY_RATING_UNDEFINED, MATURE, not-mature] |
| **source** | **String**| String to identify the originator of this request. | [optional] |

### Return type

[**Volumes**](Volumes.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="booksVolumesGet"></a>
# **booksVolumesGet**
> Volume booksVolumesGet(volumeId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, country, includeNonComicsSeries, partner, projection, source, userLibraryConsistentRead)



Gets volume information for a single volume.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://books.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    String volumeId = "volumeId_example"; // String | ID of volume to retrieve.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String country = "country_example"; // String | ISO-3166-1 code to override the IP-based location.
    Boolean includeNonComicsSeries = true; // Boolean | Set to true to include non-comics series. Defaults to false.
    String partner = "partner_example"; // String | Brand results for partner ID.
    String projection = "PROJECTION_UNDEFINED"; // String | Restrict information returned to a set of selected fields.
    String source = "source_example"; // String | string to identify the originator of this request.
    Boolean userLibraryConsistentRead = true; // Boolean | 
    try {
      Volume result = apiInstance.booksVolumesGet(volumeId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, country, includeNonComicsSeries, partner, projection, source, userLibraryConsistentRead);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#booksVolumesGet");
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
| **volumeId** | **String**| ID of volume to retrieve. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **country** | **String**| ISO-3166-1 code to override the IP-based location. | [optional] |
| **includeNonComicsSeries** | **Boolean**| Set to true to include non-comics series. Defaults to false. | [optional] |
| **partner** | **String**| Brand results for partner ID. | [optional] |
| **projection** | **String**| Restrict information returned to a set of selected fields. | [optional] [enum: PROJECTION_UNDEFINED, FULL, LITE] |
| **source** | **String**| string to identify the originator of this request. | [optional] |
| **userLibraryConsistentRead** | **Boolean**|  | [optional] |

### Return type

[**Volume**](Volume.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="booksVolumesList"></a>
# **booksVolumesList**
> Volumes booksVolumesList(q, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, download, filter, langRestrict, libraryRestrict, maxAllowedMaturityRating, maxResults, orderBy, partner, printType, projection, showPreorders, source, startIndex)



Performs a book search.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://books.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    String q = "q_example"; // String | Full-text search query string.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String download = "DOWNLOAD_UNDEFINED"; // String | Restrict to volumes by download availability.
    String filter = "FILTER_UNDEFINED"; // String | Filter search results.
    String langRestrict = "langRestrict_example"; // String | Restrict results to books with this language code.
    String libraryRestrict = "LIBRARY_RESTRICT_UNDEFINED"; // String | Restrict search to this user's library.
    String maxAllowedMaturityRating = "MAX_ALLOWED_MATURITY_RATING_UNDEFINED"; // String | The maximum allowed maturity rating of returned recommendations. Books with a higher maturity rating are filtered out.
    Integer maxResults = 56; // Integer | Maximum number of results to return.
    String orderBy = "ORDER_BY_UNDEFINED"; // String | Sort search results.
    String partner = "partner_example"; // String | Restrict and brand results for partner ID.
    String printType = "PRINT_TYPE_UNDEFINED"; // String | Restrict to books or magazines.
    String projection = "PROJECTION_UNDEFINED"; // String | Restrict information returned to a set of selected fields.
    Boolean showPreorders = true; // Boolean | Set to true to show books available for preorder. Defaults to false.
    String source = "source_example"; // String | String to identify the originator of this request.
    Integer startIndex = 56; // Integer | Index of the first result to return (starts at 0)
    try {
      Volumes result = apiInstance.booksVolumesList(q, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, download, filter, langRestrict, libraryRestrict, maxAllowedMaturityRating, maxResults, orderBy, partner, printType, projection, showPreorders, source, startIndex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#booksVolumesList");
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
| **q** | **String**| Full-text search query string. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **download** | **String**| Restrict to volumes by download availability. | [optional] [enum: DOWNLOAD_UNDEFINED, EPUB] |
| **filter** | **String**| Filter search results. | [optional] [enum: FILTER_UNDEFINED, ebooks, free-ebooks, full, paid-ebooks, partial] |
| **langRestrict** | **String**| Restrict results to books with this language code. | [optional] |
| **libraryRestrict** | **String**| Restrict search to this user&#39;s library. | [optional] [enum: LIBRARY_RESTRICT_UNDEFINED, my-library, no-restrict] |
| **maxAllowedMaturityRating** | **String**| The maximum allowed maturity rating of returned recommendations. Books with a higher maturity rating are filtered out. | [optional] [enum: MAX_ALLOWED_MATURITY_RATING_UNDEFINED, MATURE, not-mature] |
| **maxResults** | **Integer**| Maximum number of results to return. | [optional] |
| **orderBy** | **String**| Sort search results. | [optional] [enum: ORDER_BY_UNDEFINED, newest, relevance] |
| **partner** | **String**| Restrict and brand results for partner ID. | [optional] |
| **printType** | **String**| Restrict to books or magazines. | [optional] [enum: PRINT_TYPE_UNDEFINED, ALL, BOOKS, MAGAZINES] |
| **projection** | **String**| Restrict information returned to a set of selected fields. | [optional] [enum: PROJECTION_UNDEFINED, FULL, LITE] |
| **showPreorders** | **Boolean**| Set to true to show books available for preorder. Defaults to false. | [optional] |
| **source** | **String**| String to identify the originator of this request. | [optional] |
| **startIndex** | **Integer**| Index of the first result to return (starts at 0) | [optional] |

### Return type

[**Volumes**](Volumes.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="booksVolumesMybooksList"></a>
# **booksVolumesMybooksList**
> Volumes booksVolumesMybooksList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, acquireMethod, country, locale, maxResults, processingState, source, startIndex)



Return a list of books in My Library.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://books.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    List<String> acquireMethod = Arrays.asList(); // List<String> | How the book was acquired
    String country = "country_example"; // String | ISO-3166-1 code to override the IP-based location.
    String locale = "locale_example"; // String | ISO-639-1 language and ISO-3166-1 country code. Ex:'en_US'. Used for generating recommendations.
    Integer maxResults = 56; // Integer | Maximum number of results to return.
    List<String> processingState = Arrays.asList(); // List<String> | The processing state of the user uploaded volumes to be returned. Applicable only if the UPLOADED is specified in the acquireMethod.
    String source = "source_example"; // String | String to identify the originator of this request.
    Integer startIndex = 56; // Integer | Index of the first result to return (starts at 0)
    try {
      Volumes result = apiInstance.booksVolumesMybooksList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, acquireMethod, country, locale, maxResults, processingState, source, startIndex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#booksVolumesMybooksList");
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
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **acquireMethod** | [**List&lt;String&gt;**](String.md)| How the book was acquired | [optional] [enum: ACQUIRE_METHOD_UNDEFINED, FAMILY_SHARED, PREORDERED, PREVIOUSLY_RENTED, PUBLIC_DOMAIN, PURCHASED, RENTED, SAMPLE, UPLOADED] |
| **country** | **String**| ISO-3166-1 code to override the IP-based location. | [optional] |
| **locale** | **String**| ISO-639-1 language and ISO-3166-1 country code. Ex:&#39;en_US&#39;. Used for generating recommendations. | [optional] |
| **maxResults** | **Integer**| Maximum number of results to return. | [optional] |
| **processingState** | [**List&lt;String&gt;**](String.md)| The processing state of the user uploaded volumes to be returned. Applicable only if the UPLOADED is specified in the acquireMethod. | [optional] [enum: PROCESSING_STATE_UNDEFINED, COMPLETED_FAILED, COMPLETED_SUCCESS, RUNNING] |
| **source** | **String**| String to identify the originator of this request. | [optional] |
| **startIndex** | **Integer**| Index of the first result to return (starts at 0) | [optional] |

### Return type

[**Volumes**](Volumes.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="booksVolumesRecommendedList"></a>
# **booksVolumesRecommendedList**
> Volumes booksVolumesRecommendedList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, locale, maxAllowedMaturityRating, source)



Return a list of recommended books for the current user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://books.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String locale = "locale_example"; // String | ISO-639-1 language and ISO-3166-1 country code. Ex: 'en_US'. Used for generating recommendations.
    String maxAllowedMaturityRating = "MAX_ALLOWED_MATURITY_RATING_UNDEFINED"; // String | The maximum allowed maturity rating of returned recommendations. Books with a higher maturity rating are filtered out.
    String source = "source_example"; // String | String to identify the originator of this request.
    try {
      Volumes result = apiInstance.booksVolumesRecommendedList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, locale, maxAllowedMaturityRating, source);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#booksVolumesRecommendedList");
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
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **locale** | **String**| ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;. Used for generating recommendations. | [optional] |
| **maxAllowedMaturityRating** | **String**| The maximum allowed maturity rating of returned recommendations. Books with a higher maturity rating are filtered out. | [optional] [enum: MAX_ALLOWED_MATURITY_RATING_UNDEFINED, MATURE, not-mature] |
| **source** | **String**| String to identify the originator of this request. | [optional] |

### Return type

[**Volumes**](Volumes.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="booksVolumesRecommendedRate"></a>
# **booksVolumesRecommendedRate**
> BooksVolumesRecommendedRateResponse booksVolumesRecommendedRate(rating, volumeId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, locale, source)



Rate a recommended book for the current user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://books.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    String rating = "RATING_UNDEFINED"; // String | Rating to be given to the volume.
    String volumeId = "volumeId_example"; // String | ID of the source volume.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String locale = "locale_example"; // String | ISO-639-1 language and ISO-3166-1 country code. Ex: 'en_US'. Used for generating recommendations.
    String source = "source_example"; // String | String to identify the originator of this request.
    try {
      BooksVolumesRecommendedRateResponse result = apiInstance.booksVolumesRecommendedRate(rating, volumeId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, locale, source);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#booksVolumesRecommendedRate");
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
| **rating** | **String**| Rating to be given to the volume. | [enum: RATING_UNDEFINED, HAVE_IT, NOT_INTERESTED] |
| **volumeId** | **String**| ID of the source volume. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **locale** | **String**| ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;. Used for generating recommendations. | [optional] |
| **source** | **String**| String to identify the originator of this request. | [optional] |

### Return type

[**BooksVolumesRecommendedRateResponse**](BooksVolumesRecommendedRateResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="booksVolumesUseruploadedList"></a>
# **booksVolumesUseruploadedList**
> Volumes booksVolumesUseruploadedList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, locale, maxResults, processingState, source, startIndex, volumeId)



Return a list of books uploaded by the current user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://books.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String locale = "locale_example"; // String | ISO-639-1 language and ISO-3166-1 country code. Ex: 'en_US'. Used for generating recommendations.
    Integer maxResults = 56; // Integer | Maximum number of results to return.
    List<String> processingState = Arrays.asList(); // List<String> | The processing state of the user uploaded volumes to be returned.
    String source = "source_example"; // String | String to identify the originator of this request.
    Integer startIndex = 56; // Integer | Index of the first result to return (starts at 0)
    List<String> volumeId = Arrays.asList(); // List<String> | The ids of the volumes to be returned. If not specified all that match the processingState are returned.
    try {
      Volumes result = apiInstance.booksVolumesUseruploadedList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, locale, maxResults, processingState, source, startIndex, volumeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#booksVolumesUseruploadedList");
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
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **locale** | **String**| ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;. Used for generating recommendations. | [optional] |
| **maxResults** | **Integer**| Maximum number of results to return. | [optional] |
| **processingState** | [**List&lt;String&gt;**](String.md)| The processing state of the user uploaded volumes to be returned. | [optional] [enum: PROCESSING_STATE_UNDEFINED, COMPLETED_FAILED, COMPLETED_SUCCESS, RUNNING] |
| **source** | **String**| String to identify the originator of this request. | [optional] |
| **startIndex** | **Integer**| Index of the first result to return (starts at 0) | [optional] |
| **volumeId** | [**List&lt;String&gt;**](String.md)| The ids of the volumes to be returned. If not specified all that match the processingState are returned. | [optional] |

### Return type

[**Volumes**](Volumes.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

