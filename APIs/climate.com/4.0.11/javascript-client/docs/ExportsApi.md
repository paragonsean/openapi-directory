# ClimateFieldViewPlatformApis.ExportsApi

All URIs are relative to *https://platform.climate.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchExportContentsById**](ExportsApi.md#fetchExportContentsById) | **GET** /v4/exports/{exportId}/contents | Retrieve the binary contents of a processed export request.
[**fetchExportStatusById**](ExportsApi.md#fetchExportStatusById) | **GET** /v4/exports/{exportId}/status | Retrieve the status of an Export.
[**postExport**](ExportsApi.md#postExport) | **POST** /v4/exports | Initiate a new export request.



## fetchExportContentsById

> fetchExportContentsById(accept, exportId, range)

Retrieve the binary contents of a processed export request.

Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;).

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

let apiInstance = new ClimateFieldViewPlatformApis.ExportsApi();
let accept = "accept_example"; // String | Must be either \\*_/_* or application/octet-stream,application/json
let exportId = "exportId_example"; // String | Unique identifier of an Export.
let range = "range_example"; // String | Byte range `bytes=start-end` (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes=0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB.
apiInstance.fetchExportContentsById(accept, exportId, range, (error, data, response) => {
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
 **accept** | **String**| Must be either \\*_/_* or application/octet-stream,application/json | 
 **exportId** | **String**| Unique identifier of an Export. | 
 **range** | **String**| Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json


## fetchExportStatusById

> ExportStatus fetchExportStatusById(exportId)

Retrieve the status of an Export.

Check the status of an **Export** by ID.

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

let apiInstance = new ClimateFieldViewPlatformApis.ExportsApi();
let exportId = "exportId_example"; // String | Unique identifier of an Export.
apiInstance.fetchExportStatusById(exportId, (error, data, response) => {
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
 **exportId** | **String**| Unique identifier of an Export. | 

### Return type

[**ExportStatus**](ExportStatus.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postExport

> CreatedExport postExport(opts)

Initiate a new export request.

Step one in requesting a data product. The method will return an **Export** ID which the caller will use in subsequent &#x60;GET&#x60; requests. The following &#x60;contentTypes&#x60; may be requested:   * __application/vnd.climate.acrsi.geojson__ (Beta)      Exports the planting activities accessible by the authenticated user and optionally filtered by resource owner      as a [GeoJSON Feature Collection](https://tools.ietf.org/html/rfc7946#page-12).       The export request definition must contain the following properties:        * plantingStartDate        * plantingEndDate        * resourceOwnerId       Requires &#x60;exports:read&#x60; and &#x60;plantingActivitySummary:read&#x60; scope.      * __application/vnd.climate.harvest.geojson__      Exports the harvesting activities accessible by the authenticated user and optionally filtered by resource owner      as a [GeoJSON Feature Collection](https://tools.ietf.org/html/rfc7946#page-12).       The export request definition must contain the following properties:        * harvestStartDate        * harvestEndDate        * resourceOwnerId       Requires &#x60;exports:read&#x60; and &#x60;plantingActivitySummary:read&#x60; scope.

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

let apiInstance = new ClimateFieldViewPlatformApis.ExportsApi();
let opts = {
  '_export': new ClimateFieldViewPlatformApis.Export() // Export | 
};
apiInstance.postExport(opts, (error, data, response) => {
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
 **_export** | [**Export**](Export.md)|  | [optional] 

### Return type

[**CreatedExport**](CreatedExport.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

