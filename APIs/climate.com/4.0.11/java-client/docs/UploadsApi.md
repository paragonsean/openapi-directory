# UploadsApi

All URIs are relative to *https://platform.climate.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chunkedUpload**](UploadsApi.md#chunkedUpload) | **PUT** /v4/uploads/{uploadId} | Chunked upload of data |
| [**fetchUploadStatusById**](UploadsApi.md#fetchUploadStatusById) | **GET** /v4/uploads/{uploadId}/status | Retrieve Upload status |
| [**fetchUploadStatuses**](UploadsApi.md#fetchUploadStatuses) | **POST** /v4/uploads/status/query | Retrieve Upload statuses in batch |
| [**postUpload**](UploadsApi.md#postUpload) | **POST** /v4/uploads | Initiate a new upload |


<a id="chunkedUpload"></a>
# **chunkedUpload**
> chunkedUpload(contentRange, uploadId, contentType)

Chunked upload of data

Send chunked data for an **Upload**.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UploadsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    UploadsApi apiInstance = new UploadsApi(defaultClient);
    String contentRange = "contentRange_example"; // String | Byte range `bytes start-end/total` (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes).
    UUID uploadId = UUID.randomUUID(); // UUID | Unique identifier of an Upload.
    String contentType = "contentType_example"; // String | Must be `application/octet-stream`
    try {
      apiInstance.chunkedUpload(contentRange, uploadId, contentType);
    } catch (ApiException e) {
      System.err.println("Exception when calling UploadsApi#chunkedUpload");
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
| **contentRange** | **String**| Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). | |
| **uploadId** | **UUID**| Unique identifier of an Upload. | |
| **contentType** | **String**| Must be &#x60;application/octet-stream&#x60; | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **401** | Unauthorized |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **403** | Forbidden |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **404** | Not Found |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **429** | Too Many Requests |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **500** | Internal Server Error |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **503** | Server Busy |  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

<a id="fetchUploadStatusById"></a>
# **fetchUploadStatusById**
> UploadStatus fetchUploadStatusById(uploadId)

Retrieve Upload status

Check the status of an **Upload** by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UploadsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    UploadsApi apiInstance = new UploadsApi(defaultClient);
    UUID uploadId = UUID.randomUUID(); // UUID | Unique identifier of an Upload.
    try {
      UploadStatus result = apiInstance.fetchUploadStatusById(uploadId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UploadsApi#fetchUploadStatusById");
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
| **uploadId** | **UUID**| Unique identifier of an Upload. | |

### Return type

[**UploadStatus**](UploadStatus.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **401** | Unauthorized |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **403** | Forbidden |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **404** | Not Found |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **429** | Too Many Requests |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **500** | Internal Server Error |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **503** | Server Busy |  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

<a id="fetchUploadStatuses"></a>
# **fetchUploadStatuses**
> UploadStatuses fetchUploadStatuses(uploadStatusQuery)

Retrieve Upload statuses in batch

Check the status of multiple **Uploads** (up to 100 per request).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UploadsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    UploadsApi apiInstance = new UploadsApi(defaultClient);
    UploadStatusQuery uploadStatusQuery = new UploadStatusQuery(); // UploadStatusQuery | 
    try {
      UploadStatuses result = apiInstance.fetchUploadStatuses(uploadStatusQuery);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UploadsApi#fetchUploadStatuses");
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
| **uploadStatusQuery** | [**UploadStatusQuery**](UploadStatusQuery.md)|  | [optional] |

### Return type

[**UploadStatuses**](UploadStatuses.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **401** | Unauthorized |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **403** | Forbidden |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **404** | Not Found |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **429** | Too Many Requests |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **500** | Internal Server Error |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **503** | Server Busy |  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

<a id="postUpload"></a>
# **postUpload**
> UUID postUpload(xRecipientEmail, upload)

Initiate a new upload

Step one in uploading a data product. The method will return an **Upload** ID which the caller will use in subsequent &#x60;PUT&#x60; requests. The following &#x60;contentTypes&#x60; may be uploaded:     &lt;details&gt;&lt;summary&gt;__image/vnd.climate.thermal.geotiff__&lt;/summary&gt;      Allows for the upload of a thermal image. The image is a single band geotiff with 64 bit signed floating point values in degrees Celsius. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt;__image/vnd.climate.ndvi.geotiff__&lt;/summary&gt;      Allows for the upload of a NDVI image. The image is a single band geotiff with 64 bit signed floating point values in the range of -1 to 1 inclusive. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __image/vnd.climate.rgb.geotiff__&lt;/summary&gt;      Allows for the upload of a true color image. The image is a multi band geotiff with 24-bit composite values. Each band is 8 bits with values in the range of 0 to 255. The Coordinate Reference System (CRS) must be UTM with WGS84 datum. The geotiff must contain 3 bands in the order Red, Green, Blue.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __image/vnd.climate.rgb-nir.geotiff__&lt;/summary&gt;      Allows for the upload of a Near Infrared (NIR) image. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt;__image/vnd.climate.rgb-cir.geotiff__&lt;/summary&gt;      Allows for the upload of a Color Infrared (CIR) image. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __application/vnd.climate.rx.planting.shp__&lt;/summary&gt;      Allows for the upload of a planting prescription in shapefile format.  The upload must be an archive in the zip format.  It should contain one and only one of each of the following file types:       * .shp       * .shx       * .dbf      All files with the above suffixes must have the same prefix, ie Back40.shp, Back40.shx and Back40.dbf.      Requires either rx:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __application/vnd.climate.prescription.zones.shp__&lt;/summary&gt;      Allows for the upload of a zones prescription in shapefile format.  The upload must be an archive in the zip format.  It should contain one and only one of each of the following file types:       * .shp       * .shx       * .dbf      All files with the above suffixes must have the same prefix, ie Back40.shp, Back40.shx and Back40.dbf.      The following metadata entries are required:       * fieldId - field identifier for prescription zones.          Requires either rxZones:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __application/vnd.climate.modus.xml__&lt;/summary&gt;      Allows for the upload of a soil sampling file in the modus 1.0 format with some restrictions.  The upload must be a single xml file.      The following elements are required to be present in the modus file.       * EventCode - Max length of 64 bytes       * EventDate - Must be in ISO8601       * SoilSample - Has a maxOccurs of 20k       * Depth - Has a maxOccurs of 50       * LabName - Must be non-empty.       * StartingDepth - 0 to 36 inclusive, default 0       * EndingDepth - 1 - 36 inclusive, default 1       * ColumnDepth       * DepthUnit - must be inches       * Geometry - point in wgs84          Requires the soil:write scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.stand-count.geojson__&lt;/summary&gt;      Allows for the upload of a valid [geojson feature collection](https://tools.ietf.org/html/rfc7946#section-3.3).      Each feature in the collection must contain the following entry in its properties section:       * StandPPA - A count of the number of plants per acre:      Additionally, the type field of each feature&#39;s geometry field must be:       * Point      Requires &#x60;imagery:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.weed-count.geojson__&lt;/summary&gt;      Allows for the upload of a valid [geojson feature collection](https://tools.ietf.org/html/rfc7946#section-3.3).      Each feature in the collection must contain the following entry in its properties section:       * StandPPA - A count of the number of plants per acre:      Additionally, the type field of each feature&#39;s geometry field must be:       * Point      Requires &#x60;imagery:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.as-applied.zip__&lt;/summary&gt;      Allows for the upload of a valid application data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower&#39;s account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires &#x60;asApplied:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.as-planted.zip__&lt;/summary&gt;      Allows for the upload of a valid planting data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower&#39;s account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires &#x60;asPlanted:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.as-harvested.zip__&lt;/summary&gt;      Allows for the upload of a valid harvest data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower&#39;s account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires &#x60;asHarvested:write&#x60; scope.    &lt;/details&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UploadsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    UploadsApi apiInstance = new UploadsApi(defaultClient);
    String xRecipientEmail = "xRecipientEmail_example"; // String | Email address associated with a Climate account, used when to sending to another user.
    Upload upload = new Upload(); // Upload | 
    try {
      UUID result = apiInstance.postUpload(xRecipientEmail, upload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UploadsApi#postUpload");
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
| **xRecipientEmail** | **String**| Email address associated with a Climate account, used when to sending to another user. | [optional] |
| **upload** | [**Upload**](Upload.md)|  | [optional] |

### Return type

[**UUID**](UUID.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Returns a new upload with ID used to PUT file contents. |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **401** | Unauthorized |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **403** | Forbidden |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **429** | Too Many Requests |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **500** | Internal Server Error |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **503** | Server Busy |  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

