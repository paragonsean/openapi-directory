# Stoplight.VersionsApi

All URIs are relative to *https://api.stoplight.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gETVersionsVersionIdExportFormat**](VersionsApi.md#gETVersionsVersionIdExportFormat) | **GET** /versions/{versionId}/export/{format} | Export
[**pOSTVersionsVersionIdPublish**](VersionsApi.md#pOSTVersionsVersionIdPublish) | **POST** /versions/{versionId}/publish | Publish
[**pUTVersionsVersionIdImport**](VersionsApi.md#pUTVersionsVersionIdImport) | **PUT** /versions/{versionId}/import | Import
[**pUTVersionsVersionIdUnpublish**](VersionsApi.md#pUTVersionsVersionIdUnpublish) | **PUT** /versions/{versionId}/unpublish | Unpublish



## gETVersionsVersionIdExportFormat

> gETVersionsVersionIdExportFormat(versionId, format)

Export

Export a version to your choice of API specification.  ### Allowed Formats:  - oas.json - oas.yaml - raml08.yaml - raml10.yaml - stoplight.json - stoplight.yaml  The stoplight format actually returns OAS (Swagger 2) with x-stoplight annotations. If you are exporting with the intent on importing back into Stoplight, this export format preserves the most information.  ### Example URL:  &#x60;https://api.stoplight.io/v1/versions/123/export/oas.json&#x60;

### Example

```javascript
import Stoplight from 'stoplight';

let apiInstance = new Stoplight.VersionsApi();
let versionId = "''"; // String | This is the unique identifier for the version.
let format = "'oas.json'"; // String | The specification / format that you want to export.
apiInstance.gETVersionsVersionIdExportFormat(versionId, format, (error, data, response) => {
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
 **versionId** | **String**| This is the unique identifier for the version. | [default to &#39;&#39;]
 **format** | **String**| The specification / format that you want to export. | [default to &#39;oas.json&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/yaml


## pOSTVersionsVersionIdPublish

> POSTVersionsVersionIdPublish200Response pOSTVersionsVersionIdPublish(versionId)

Publish

Re-publish an API version in Stoplight. This will re-publish the given API version, with whatever publish settings have already been setup in the app.  This will only work with APIs that have previously been published at least once.  This works well with the #endpoint:957qEfc97BB5XGAeZ endpoint to augment your continuous integration processes, and automatically re-publish your documentation when certain events happen. Once such scenario is:  1. Swagger is generated from your codebase, and pushed up to Github. 2. A simple script that you write sends a request to the Stoplight API to import the new specification, passing in the URL to the swagger file on Github. 3. After the import succeeds, and your API in Stoplight is up to date, the script sends a request to the Stoplight API (this endpoint) to re-publish your documentation.

### Example

```javascript
import Stoplight from 'stoplight';
let defaultClient = Stoplight.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Stoplight.VersionsApi();
let versionId = "versionId_example"; // String | This is the unique identifier for the version.
apiInstance.pOSTVersionsVersionIdPublish(versionId, (error, data, response) => {
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
 **versionId** | **String**| This is the unique identifier for the version. | 

### Return type

[**POSTVersionsVersionIdPublish200Response**](POSTVersionsVersionIdPublish200Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pUTVersionsVersionIdImport

> PUTVersionsVersionIdImport200Response pUTVersionsVersionIdImport(versionId, opts)

Import

Import the given specification into an existing version.   **Warning, this is a destructive action! Any resources present in both the existing version, and the specification being imported, will be overwritten.**  This endpoint is particularly useful when you manage a specification file (Swagger or RAML) outside of Stoplight, and want to keep your Stoplight API version up to date as that specification changes.  By default, a \&quot;merge\&quot; is performed when importing. If a resource exists in the specification that you are importing, and in the Stoplight API, the resource will be overwritten. If a resource exists in the Stoplight API, but not in the spefication that you are importing, the resource will be left alone (and not deleted).  You can include an optional &#x60;options&#x60; property in the request body, to indicate if you would like to perform more of a replacement (instead of a merge). The options are documented in full in the response definition below these notes.  Take this request + request body for example:  &#x60;PUT https://api.stoplight.io/v1/versions/123/import&#x60; &#x60;&#x60;&#x60;json {   \&quot;url\&quot;: \&quot;http://petstore.swagger.io/v2/swagger.json\&quot;,   \&quot;options\&quot;: {     \&quot;removeExtraEndpoints\&quot;: true,     \&quot;removeExtraSchemas\&quot;: true   } } &#x60;&#x60;&#x60;  This request will grab the swagger specification described at &#x60;http://petstore.swagger.io/v2/swagger.json&#x60;, and import it into the Stoplight API version with id &#x60;123&#x60;. Additionally, it will delete any existing endpoints or models that are not described in the petstore swagger being imported.  Instead of a URL, you can provide the actual specification to be imported, either as a string (in the case of YAML) or an object (in the case of JSON). That request would look something like this:  &#x60;PUT https://api.stoplight.io/v1/versions/123/import&#x60; &#x60;&#x60;&#x60;json {   \&quot;specData\&quot;: {     \&quot;swagger\&quot;: \&quot;2.0\&quot;,     \&quot;info\&quot;: {}     ... rest of spec   } } &#x60;&#x60;&#x60;

### Example

```javascript
import Stoplight from 'stoplight';
let defaultClient = Stoplight.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Stoplight.VersionsApi();
let versionId = "versionId_example"; // String | This is the unique identifier for the version.
let opts = {
  'pUTVersionsVersionIdImportRequest': new Stoplight.PUTVersionsVersionIdImportRequest() // PUTVersionsVersionIdImportRequest | 
};
apiInstance.pUTVersionsVersionIdImport(versionId, opts, (error, data, response) => {
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
 **versionId** | **String**| This is the unique identifier for the version. | 
 **pUTVersionsVersionIdImportRequest** | [**PUTVersionsVersionIdImportRequest**](PUTVersionsVersionIdImportRequest.md)|  | [optional] 

### Return type

[**PUTVersionsVersionIdImport200Response**](PUTVersionsVersionIdImport200Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pUTVersionsVersionIdUnpublish

> PUTVersionsVersionIdUnpublish200Response pUTVersionsVersionIdUnpublish(versionId)

Unpublish

Unpublish the documentation associated with the given API version.

### Example

```javascript
import Stoplight from 'stoplight';
let defaultClient = Stoplight.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Stoplight.VersionsApi();
let versionId = "versionId_example"; // String | This is the unique identifier for the version.
apiInstance.pUTVersionsVersionIdUnpublish(versionId, (error, data, response) => {
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
 **versionId** | **String**| This is the unique identifier for the version. | 

### Return type

[**PUTVersionsVersionIdUnpublish200Response**](PUTVersionsVersionIdUnpublish200Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

