# LayersApi

All URIs are relative to *https://books.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**booksLayersAnnotationDataGet**](LayersApi.md#booksLayersAnnotationDataGet) | **GET** /books/v1/volumes/{volumeId}/layers/{layerId}/data/{annotationDataId} |  |
| [**booksLayersAnnotationDataList**](LayersApi.md#booksLayersAnnotationDataList) | **GET** /books/v1/volumes/{volumeId}/layers/{layerId}/data |  |
| [**booksLayersGet**](LayersApi.md#booksLayersGet) | **GET** /books/v1/volumes/{volumeId}/layersummary/{summaryId} |  |
| [**booksLayersList**](LayersApi.md#booksLayersList) | **GET** /books/v1/volumes/{volumeId}/layersummary |  |
| [**booksLayersVolumeAnnotationsGet**](LayersApi.md#booksLayersVolumeAnnotationsGet) | **GET** /books/v1/volumes/{volumeId}/layers/{layerId}/annotations/{annotationId} |  |
| [**booksLayersVolumeAnnotationsList**](LayersApi.md#booksLayersVolumeAnnotationsList) | **GET** /books/v1/volumes/{volumeId}/layers/{layerId} |  |


<a id="booksLayersAnnotationDataGet"></a>
# **booksLayersAnnotationDataGet**
> DictionaryAnnotationdata booksLayersAnnotationDataGet(volumeId, layerId, annotationDataId, contentVersion, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, allowWebDefinitions, h, locale, scale, source, w)



Gets the annotation data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LayersApi;

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

    LayersApi apiInstance = new LayersApi(defaultClient);
    String volumeId = "volumeId_example"; // String | The volume to retrieve annotations for.
    String layerId = "layerId_example"; // String | The ID for the layer to get the annotations.
    String annotationDataId = "annotationDataId_example"; // String | The ID of the annotation data to retrieve.
    String contentVersion = "contentVersion_example"; // String | The content version for the volume you are trying to retrieve.
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
    Boolean allowWebDefinitions = true; // Boolean | For the dictionary layer. Whether or not to allow web definitions.
    Integer h = 56; // Integer | The requested pixel height for any images. If height is provided width must also be provided.
    String locale = "locale_example"; // String | The locale information for the data. ISO-639-1 language and ISO-3166-1 country code. Ex: 'en_US'.
    Integer scale = 56; // Integer | The requested scale for the image.
    String source = "source_example"; // String | String to identify the originator of this request.
    Integer w = 56; // Integer | The requested pixel width for any images. If width is provided height must also be provided.
    try {
      DictionaryAnnotationdata result = apiInstance.booksLayersAnnotationDataGet(volumeId, layerId, annotationDataId, contentVersion, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, allowWebDefinitions, h, locale, scale, source, w);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LayersApi#booksLayersAnnotationDataGet");
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
| **volumeId** | **String**| The volume to retrieve annotations for. | |
| **layerId** | **String**| The ID for the layer to get the annotations. | |
| **annotationDataId** | **String**| The ID of the annotation data to retrieve. | |
| **contentVersion** | **String**| The content version for the volume you are trying to retrieve. | |
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
| **allowWebDefinitions** | **Boolean**| For the dictionary layer. Whether or not to allow web definitions. | [optional] |
| **h** | **Integer**| The requested pixel height for any images. If height is provided width must also be provided. | [optional] |
| **locale** | **String**| The locale information for the data. ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;. | [optional] |
| **scale** | **Integer**| The requested scale for the image. | [optional] |
| **source** | **String**| String to identify the originator of this request. | [optional] |
| **w** | **Integer**| The requested pixel width for any images. If width is provided height must also be provided. | [optional] |

### Return type

[**DictionaryAnnotationdata**](DictionaryAnnotationdata.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="booksLayersAnnotationDataList"></a>
# **booksLayersAnnotationDataList**
> Annotationsdata booksLayersAnnotationDataList(volumeId, layerId, contentVersion, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, annotationDataId, h, locale, maxResults, pageToken, scale, source, updatedMax, updatedMin, w)



Gets the annotation data for a volume and layer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LayersApi;

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

    LayersApi apiInstance = new LayersApi(defaultClient);
    String volumeId = "volumeId_example"; // String | The volume to retrieve annotation data for.
    String layerId = "layerId_example"; // String | The ID for the layer to get the annotation data.
    String contentVersion = "contentVersion_example"; // String | The content version for the requested volume.
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
    List<String> annotationDataId = Arrays.asList(); // List<String> | The list of Annotation Data Ids to retrieve. Pagination is ignored if this is set.
    Integer h = 56; // Integer | The requested pixel height for any images. If height is provided width must also be provided.
    String locale = "locale_example"; // String | The locale information for the data. ISO-639-1 language and ISO-3166-1 country code. Ex: 'en_US'.
    Integer maxResults = 56; // Integer | Maximum number of results to return
    String pageToken = "pageToken_example"; // String | The value of the nextToken from the previous page.
    Integer scale = 56; // Integer | The requested scale for the image.
    String source = "source_example"; // String | String to identify the originator of this request.
    String updatedMax = "updatedMax_example"; // String | RFC 3339 timestamp to restrict to items updated prior to this timestamp (exclusive).
    String updatedMin = "updatedMin_example"; // String | RFC 3339 timestamp to restrict to items updated since this timestamp (inclusive).
    Integer w = 56; // Integer | The requested pixel width for any images. If width is provided height must also be provided.
    try {
      Annotationsdata result = apiInstance.booksLayersAnnotationDataList(volumeId, layerId, contentVersion, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, annotationDataId, h, locale, maxResults, pageToken, scale, source, updatedMax, updatedMin, w);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LayersApi#booksLayersAnnotationDataList");
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
| **volumeId** | **String**| The volume to retrieve annotation data for. | |
| **layerId** | **String**| The ID for the layer to get the annotation data. | |
| **contentVersion** | **String**| The content version for the requested volume. | |
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
| **annotationDataId** | [**List&lt;String&gt;**](String.md)| The list of Annotation Data Ids to retrieve. Pagination is ignored if this is set. | [optional] |
| **h** | **Integer**| The requested pixel height for any images. If height is provided width must also be provided. | [optional] |
| **locale** | **String**| The locale information for the data. ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;. | [optional] |
| **maxResults** | **Integer**| Maximum number of results to return | [optional] |
| **pageToken** | **String**| The value of the nextToken from the previous page. | [optional] |
| **scale** | **Integer**| The requested scale for the image. | [optional] |
| **source** | **String**| String to identify the originator of this request. | [optional] |
| **updatedMax** | **String**| RFC 3339 timestamp to restrict to items updated prior to this timestamp (exclusive). | [optional] |
| **updatedMin** | **String**| RFC 3339 timestamp to restrict to items updated since this timestamp (inclusive). | [optional] |
| **w** | **Integer**| The requested pixel width for any images. If width is provided height must also be provided. | [optional] |

### Return type

[**Annotationsdata**](Annotationsdata.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="booksLayersGet"></a>
# **booksLayersGet**
> Layersummary booksLayersGet(volumeId, summaryId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, contentVersion, source)



Gets the layer summary for a volume.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LayersApi;

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

    LayersApi apiInstance = new LayersApi(defaultClient);
    String volumeId = "volumeId_example"; // String | The volume to retrieve layers for.
    String summaryId = "summaryId_example"; // String | The ID for the layer to get the summary for.
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
    String contentVersion = "contentVersion_example"; // String | The content version for the requested volume.
    String source = "source_example"; // String | String to identify the originator of this request.
    try {
      Layersummary result = apiInstance.booksLayersGet(volumeId, summaryId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, contentVersion, source);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LayersApi#booksLayersGet");
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
| **volumeId** | **String**| The volume to retrieve layers for. | |
| **summaryId** | **String**| The ID for the layer to get the summary for. | |
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
| **contentVersion** | **String**| The content version for the requested volume. | [optional] |
| **source** | **String**| String to identify the originator of this request. | [optional] |

### Return type

[**Layersummary**](Layersummary.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="booksLayersList"></a>
# **booksLayersList**
> Layersummaries booksLayersList(volumeId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, contentVersion, maxResults, pageToken, source)



List the layer summaries for a volume.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LayersApi;

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

    LayersApi apiInstance = new LayersApi(defaultClient);
    String volumeId = "volumeId_example"; // String | The volume to retrieve layers for.
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
    String contentVersion = "contentVersion_example"; // String | The content version for the requested volume.
    Integer maxResults = 56; // Integer | Maximum number of results to return
    String pageToken = "pageToken_example"; // String | The value of the nextToken from the previous page.
    String source = "source_example"; // String | String to identify the originator of this request.
    try {
      Layersummaries result = apiInstance.booksLayersList(volumeId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, contentVersion, maxResults, pageToken, source);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LayersApi#booksLayersList");
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
| **volumeId** | **String**| The volume to retrieve layers for. | |
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
| **contentVersion** | **String**| The content version for the requested volume. | [optional] |
| **maxResults** | **Integer**| Maximum number of results to return | [optional] |
| **pageToken** | **String**| The value of the nextToken from the previous page. | [optional] |
| **source** | **String**| String to identify the originator of this request. | [optional] |

### Return type

[**Layersummaries**](Layersummaries.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="booksLayersVolumeAnnotationsGet"></a>
# **booksLayersVolumeAnnotationsGet**
> Volumeannotation booksLayersVolumeAnnotationsGet(volumeId, layerId, annotationId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, locale, source)



Gets the volume annotation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LayersApi;

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

    LayersApi apiInstance = new LayersApi(defaultClient);
    String volumeId = "volumeId_example"; // String | The volume to retrieve annotations for.
    String layerId = "layerId_example"; // String | The ID for the layer to get the annotations.
    String annotationId = "annotationId_example"; // String | The ID of the volume annotation to retrieve.
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
    String locale = "locale_example"; // String | The locale information for the data. ISO-639-1 language and ISO-3166-1 country code. Ex: 'en_US'.
    String source = "source_example"; // String | String to identify the originator of this request.
    try {
      Volumeannotation result = apiInstance.booksLayersVolumeAnnotationsGet(volumeId, layerId, annotationId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, locale, source);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LayersApi#booksLayersVolumeAnnotationsGet");
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
| **volumeId** | **String**| The volume to retrieve annotations for. | |
| **layerId** | **String**| The ID for the layer to get the annotations. | |
| **annotationId** | **String**| The ID of the volume annotation to retrieve. | |
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
| **locale** | **String**| The locale information for the data. ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;. | [optional] |
| **source** | **String**| String to identify the originator of this request. | [optional] |

### Return type

[**Volumeannotation**](Volumeannotation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="booksLayersVolumeAnnotationsList"></a>
# **booksLayersVolumeAnnotationsList**
> Volumeannotations booksLayersVolumeAnnotationsList(volumeId, layerId, contentVersion, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, endOffset, endPosition, locale, maxResults, pageToken, showDeleted, source, startOffset, startPosition, updatedMax, updatedMin, volumeAnnotationsVersion)



Gets the volume annotations for a volume and layer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LayersApi;

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

    LayersApi apiInstance = new LayersApi(defaultClient);
    String volumeId = "volumeId_example"; // String | The volume to retrieve annotations for.
    String layerId = "layerId_example"; // String | The ID for the layer to get the annotations.
    String contentVersion = "contentVersion_example"; // String | The content version for the requested volume.
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
    String endOffset = "endOffset_example"; // String | The end offset to end retrieving data from.
    String endPosition = "endPosition_example"; // String | The end position to end retrieving data from.
    String locale = "locale_example"; // String | The locale information for the data. ISO-639-1 language and ISO-3166-1 country code. Ex: 'en_US'.
    Integer maxResults = 56; // Integer | Maximum number of results to return
    String pageToken = "pageToken_example"; // String | The value of the nextToken from the previous page.
    Boolean showDeleted = true; // Boolean | Set to true to return deleted annotations. updatedMin must be in the request to use this. Defaults to false.
    String source = "source_example"; // String | String to identify the originator of this request.
    String startOffset = "startOffset_example"; // String | The start offset to start retrieving data from.
    String startPosition = "startPosition_example"; // String | The start position to start retrieving data from.
    String updatedMax = "updatedMax_example"; // String | RFC 3339 timestamp to restrict to items updated prior to this timestamp (exclusive).
    String updatedMin = "updatedMin_example"; // String | RFC 3339 timestamp to restrict to items updated since this timestamp (inclusive).
    String volumeAnnotationsVersion = "volumeAnnotationsVersion_example"; // String | The version of the volume annotations that you are requesting.
    try {
      Volumeannotations result = apiInstance.booksLayersVolumeAnnotationsList(volumeId, layerId, contentVersion, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, endOffset, endPosition, locale, maxResults, pageToken, showDeleted, source, startOffset, startPosition, updatedMax, updatedMin, volumeAnnotationsVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LayersApi#booksLayersVolumeAnnotationsList");
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
| **volumeId** | **String**| The volume to retrieve annotations for. | |
| **layerId** | **String**| The ID for the layer to get the annotations. | |
| **contentVersion** | **String**| The content version for the requested volume. | |
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
| **endOffset** | **String**| The end offset to end retrieving data from. | [optional] |
| **endPosition** | **String**| The end position to end retrieving data from. | [optional] |
| **locale** | **String**| The locale information for the data. ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;. | [optional] |
| **maxResults** | **Integer**| Maximum number of results to return | [optional] |
| **pageToken** | **String**| The value of the nextToken from the previous page. | [optional] |
| **showDeleted** | **Boolean**| Set to true to return deleted annotations. updatedMin must be in the request to use this. Defaults to false. | [optional] |
| **source** | **String**| String to identify the originator of this request. | [optional] |
| **startOffset** | **String**| The start offset to start retrieving data from. | [optional] |
| **startPosition** | **String**| The start position to start retrieving data from. | [optional] |
| **updatedMax** | **String**| RFC 3339 timestamp to restrict to items updated prior to this timestamp (exclusive). | [optional] |
| **updatedMin** | **String**| RFC 3339 timestamp to restrict to items updated since this timestamp (inclusive). | [optional] |
| **volumeAnnotationsVersion** | **String**| The version of the volume annotations that you are requesting. | [optional] |

### Return type

[**Volumeannotations**](Volumeannotations.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

