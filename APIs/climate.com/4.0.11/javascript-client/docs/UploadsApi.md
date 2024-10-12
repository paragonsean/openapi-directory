# ClimateFieldViewPlatformApis.UploadsApi

All URIs are relative to *https://platform.climate.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chunkedUpload**](UploadsApi.md#chunkedUpload) | **PUT** /v4/uploads/{uploadId} | Chunked upload of data
[**fetchUploadStatusById**](UploadsApi.md#fetchUploadStatusById) | **GET** /v4/uploads/{uploadId}/status | Retrieve Upload status
[**fetchUploadStatuses**](UploadsApi.md#fetchUploadStatuses) | **POST** /v4/uploads/status/query | Retrieve Upload statuses in batch
[**postUpload**](UploadsApi.md#postUpload) | **POST** /v4/uploads | Initiate a new upload



## chunkedUpload

> chunkedUpload(contentRange, uploadId, contentType)

Chunked upload of data

Send chunked data for an **Upload**.

### Example

```javascript
import ClimateFieldViewPlatformApis from 'climate_field_view_platform_apis';
let defaultClient = ClimateFieldViewPlatformApis.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2_authorization_code
let oauth2_authorization_code = defaultClient.authentications['oauth2_authorization_code'];
oauth2_authorization_code.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ClimateFieldViewPlatformApis.UploadsApi();
let contentRange = "contentRange_example"; // String | Byte range `bytes start-end/total` (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes).
let uploadId = "uploadId_example"; // String | Unique identifier of an Upload.
let contentType = "contentType_example"; // String | Must be `application/octet-stream`
apiInstance.chunkedUpload(contentRange, uploadId, contentType, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentRange** | **String**| Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). | 
 **uploadId** | **String**| Unique identifier of an Upload. | 
 **contentType** | **String**| Must be &#x60;application/octet-stream&#x60; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchUploadStatusById

> UploadStatus fetchUploadStatusById(uploadId)

Retrieve Upload status

Check the status of an **Upload** by ID.

### Example

```javascript
import ClimateFieldViewPlatformApis from 'climate_field_view_platform_apis';
let defaultClient = ClimateFieldViewPlatformApis.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2_authorization_code
let oauth2_authorization_code = defaultClient.authentications['oauth2_authorization_code'];
oauth2_authorization_code.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ClimateFieldViewPlatformApis.UploadsApi();
let uploadId = "uploadId_example"; // String | Unique identifier of an Upload.
apiInstance.fetchUploadStatusById(uploadId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uploadId** | **String**| Unique identifier of an Upload. | 

### Return type

[**UploadStatus**](UploadStatus.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchUploadStatuses

> UploadStatuses fetchUploadStatuses(opts)

Retrieve Upload statuses in batch

Check the status of multiple **Uploads** (up to 100 per request).

### Example

```javascript
import ClimateFieldViewPlatformApis from 'climate_field_view_platform_apis';
let defaultClient = ClimateFieldViewPlatformApis.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2_authorization_code
let oauth2_authorization_code = defaultClient.authentications['oauth2_authorization_code'];
oauth2_authorization_code.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ClimateFieldViewPlatformApis.UploadsApi();
let opts = {
  'uploadStatusQuery': new ClimateFieldViewPlatformApis.UploadStatusQuery() // UploadStatusQuery | 
};
apiInstance.fetchUploadStatuses(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uploadStatusQuery** | [**UploadStatusQuery**](UploadStatusQuery.md)|  | [optional] 

### Return type

[**UploadStatuses**](UploadStatuses.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postUpload

> String postUpload(opts)

Initiate a new upload

Step one in uploading a data product. The method will return an **Upload** ID which the caller will use in subsequent &#x60;PUT&#x60; requests. The following &#x60;contentTypes&#x60; may be uploaded:     &lt;details&gt;&lt;summary&gt;__image/vnd.climate.thermal.geotiff__&lt;/summary&gt;      Allows for the upload of a thermal image. The image is a single band geotiff with 64 bit signed floating point values in degrees Celsius. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt;__image/vnd.climate.ndvi.geotiff__&lt;/summary&gt;      Allows for the upload of a NDVI image. The image is a single band geotiff with 64 bit signed floating point values in the range of -1 to 1 inclusive. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __image/vnd.climate.rgb.geotiff__&lt;/summary&gt;      Allows for the upload of a true color image. The image is a multi band geotiff with 24-bit composite values. Each band is 8 bits with values in the range of 0 to 255. The Coordinate Reference System (CRS) must be UTM with WGS84 datum. The geotiff must contain 3 bands in the order Red, Green, Blue.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __image/vnd.climate.rgb-nir.geotiff__&lt;/summary&gt;      Allows for the upload of a Near Infrared (NIR) image. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt;__image/vnd.climate.rgb-cir.geotiff__&lt;/summary&gt;      Allows for the upload of a Color Infrared (CIR) image. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __application/vnd.climate.rx.planting.shp__&lt;/summary&gt;      Allows for the upload of a planting prescription in shapefile format.  The upload must be an archive in the zip format.  It should contain one and only one of each of the following file types:       * .shp       * .shx       * .dbf      All files with the above suffixes must have the same prefix, ie Back40.shp, Back40.shx and Back40.dbf.      Requires either rx:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __application/vnd.climate.prescription.zones.shp__&lt;/summary&gt;      Allows for the upload of a zones prescription in shapefile format.  The upload must be an archive in the zip format.  It should contain one and only one of each of the following file types:       * .shp       * .shx       * .dbf      All files with the above suffixes must have the same prefix, ie Back40.shp, Back40.shx and Back40.dbf.      The following metadata entries are required:       * fieldId - field identifier for prescription zones.          Requires either rxZones:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __application/vnd.climate.modus.xml__&lt;/summary&gt;      Allows for the upload of a soil sampling file in the modus 1.0 format with some restrictions.  The upload must be a single xml file.      The following elements are required to be present in the modus file.       * EventCode - Max length of 64 bytes       * EventDate - Must be in ISO8601       * SoilSample - Has a maxOccurs of 20k       * Depth - Has a maxOccurs of 50       * LabName - Must be non-empty.       * StartingDepth - 0 to 36 inclusive, default 0       * EndingDepth - 1 - 36 inclusive, default 1       * ColumnDepth       * DepthUnit - must be inches       * Geometry - point in wgs84          Requires the soil:write scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.stand-count.geojson__&lt;/summary&gt;      Allows for the upload of a valid [geojson feature collection](https://tools.ietf.org/html/rfc7946#section-3.3).      Each feature in the collection must contain the following entry in its properties section:       * StandPPA - A count of the number of plants per acre:      Additionally, the type field of each feature&#39;s geometry field must be:       * Point      Requires &#x60;imagery:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.weed-count.geojson__&lt;/summary&gt;      Allows for the upload of a valid [geojson feature collection](https://tools.ietf.org/html/rfc7946#section-3.3).      Each feature in the collection must contain the following entry in its properties section:       * StandPPA - A count of the number of plants per acre:      Additionally, the type field of each feature&#39;s geometry field must be:       * Point      Requires &#x60;imagery:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.as-applied.zip__&lt;/summary&gt;      Allows for the upload of a valid application data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower&#39;s account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires &#x60;asApplied:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.as-planted.zip__&lt;/summary&gt;      Allows for the upload of a valid planting data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower&#39;s account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires &#x60;asPlanted:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.as-harvested.zip__&lt;/summary&gt;      Allows for the upload of a valid harvest data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower&#39;s account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires &#x60;asHarvested:write&#x60; scope.    &lt;/details&gt;

### Example

```javascript
import ClimateFieldViewPlatformApis from 'climate_field_view_platform_apis';
let defaultClient = ClimateFieldViewPlatformApis.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2_authorization_code
let oauth2_authorization_code = defaultClient.authentications['oauth2_authorization_code'];
oauth2_authorization_code.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ClimateFieldViewPlatformApis.UploadsApi();
let opts = {
  'xRecipientEmail': "xRecipientEmail_example", // String | Email address associated with a Climate account, used when to sending to another user.
  'upload': new ClimateFieldViewPlatformApis.Upload() // Upload | 
};
apiInstance.postUpload(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xRecipientEmail** | **String**| Email address associated with a Climate account, used when to sending to another user. | [optional] 
 **upload** | [**Upload**](Upload.md)|  | [optional] 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

