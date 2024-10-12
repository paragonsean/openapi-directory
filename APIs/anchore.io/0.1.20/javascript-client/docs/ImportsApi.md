# AnchoreEngineApiServer.ImportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOperation**](ImportsApi.md#createOperation) | **POST** /imports/images | Begin the import of an image analyzed by Syft into the system
[**getOperation**](ImportsApi.md#getOperation) | **GET** /imports/images/{operation_id} | Get detail on a single import
[**importImageConfig**](ImportsApi.md#importImageConfig) | **POST** /imports/images/{operation_id}/image_config | Import a docker or OCI image config to associate with the image
[**importImageDockerfile**](ImportsApi.md#importImageDockerfile) | **POST** /imports/images/{operation_id}/dockerfile | Begin the import of an image analyzed by Syft into the system
[**importImageManifest**](ImportsApi.md#importImageManifest) | **POST** /imports/images/{operation_id}/manifest | Import a docker or OCI distribution manifest to associate with the image
[**importImagePackages**](ImportsApi.md#importImagePackages) | **POST** /imports/images/{operation_id}/packages | Begin the import of an image analyzed by Syft into the system
[**importImageParentManifest**](ImportsApi.md#importImageParentManifest) | **POST** /imports/images/{operation_id}/parent_manifest | Import a docker or OCI distribution manifest list to associate with the image
[**invalidateOperation**](ImportsApi.md#invalidateOperation) | **DELETE** /imports/images/{operation_id} | Invalidate operation ID so it can be garbage collected
[**listImportDockerfiles**](ImportsApi.md#listImportDockerfiles) | **GET** /imports/images/{operation_id}/dockerfile | List uploaded dockerfiles
[**listImportImageConfigs**](ImportsApi.md#listImportImageConfigs) | **GET** /imports/images/{operation_id}/image_config | List uploaded image configs
[**listImportImageManifests**](ImportsApi.md#listImportImageManifests) | **GET** /imports/images/{operation_id}/manifest | List uploaded image manifests
[**listImportPackages**](ImportsApi.md#listImportPackages) | **GET** /imports/images/{operation_id}/packages | List uploaded package manifests
[**listImportParentManifests**](ImportsApi.md#listImportParentManifests) | **GET** /imports/images/{operation_id}/parent_manifest | List uploaded parent manifests (manifest lists for a tag)
[**listOperations**](ImportsApi.md#listOperations) | **GET** /imports/images | Lists in-progress imports



## createOperation

> ImageImportOperation createOperation()

Begin the import of an image analyzed by Syft into the system

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImportsApi();
apiInstance.createOperation((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ImageImportOperation**](ImageImportOperation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOperation

> ImageImportOperation getOperation(operationId)

Get detail on a single import

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImportsApi();
let operationId = "operationId_example"; // String | 
apiInstance.getOperation(operationId, (error, data, response) => {
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
 **operationId** | **String**|  | 

### Return type

[**ImageImportOperation**](ImageImportOperation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importImageConfig

> ImageImportContentResponse importImageConfig(operationId, body)

Import a docker or OCI image config to associate with the image

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImportsApi();
let operationId = "operationId_example"; // String | 
let body = {key: null}; // Object | 
apiInstance.importImageConfig(operationId, body, (error, data, response) => {
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
 **operationId** | **String**|  | 
 **body** | **Object**|  | 

### Return type

[**ImageImportContentResponse**](ImageImportContentResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## importImageDockerfile

> ImageImportContentResponse importImageDockerfile(operationId, body)

Begin the import of an image analyzed by Syft into the system

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImportsApi();
let operationId = "operationId_example"; // String | 
let body = "body_example"; // String | 
apiInstance.importImageDockerfile(operationId, body, (error, data, response) => {
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
 **operationId** | **String**|  | 
 **body** | **String**|  | 

### Return type

[**ImageImportContentResponse**](ImageImportContentResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain; utf-8
- **Accept**: application/json


## importImageManifest

> ImageImportContentResponse importImageManifest(operationId, body)

Import a docker or OCI distribution manifest to associate with the image

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImportsApi();
let operationId = "operationId_example"; // String | 
let body = {key: null}; // Object | 
apiInstance.importImageManifest(operationId, body, (error, data, response) => {
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
 **operationId** | **String**|  | 
 **body** | **Object**|  | 

### Return type

[**ImageImportContentResponse**](ImageImportContentResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.docker.distribution.manifest.v1+json, application/vnd.docker.distribution.manifest.v1+prettyjws, application/vnd.docker.distribution.manifest.v2+json, application/vnd.oci.image.manifest.v1+json
- **Accept**: application/json


## importImagePackages

> ImageImportContentResponse importImagePackages(operationId, imagePackageManifest)

Begin the import of an image analyzed by Syft into the system

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImportsApi();
let operationId = "operationId_example"; // String | 
let imagePackageManifest = new AnchoreEngineApiServer.ImagePackageManifest(); // ImagePackageManifest | 
apiInstance.importImagePackages(operationId, imagePackageManifest, (error, data, response) => {
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
 **operationId** | **String**|  | 
 **imagePackageManifest** | [**ImagePackageManifest**](ImagePackageManifest.md)|  | 

### Return type

[**ImageImportContentResponse**](ImageImportContentResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## importImageParentManifest

> ImageImportContentResponse importImageParentManifest(operationId, body)

Import a docker or OCI distribution manifest list to associate with the image

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImportsApi();
let operationId = "operationId_example"; // String | 
let body = {key: null}; // Object | 
apiInstance.importImageParentManifest(operationId, body, (error, data, response) => {
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
 **operationId** | **String**|  | 
 **body** | **Object**|  | 

### Return type

[**ImageImportContentResponse**](ImageImportContentResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.docker.distribution.manifest.list.v2+json, application/vnd.oci.image.index.v1+json
- **Accept**: application/json


## invalidateOperation

> ImageImportOperation invalidateOperation(operationId)

Invalidate operation ID so it can be garbage collected

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImportsApi();
let operationId = "operationId_example"; // String | 
apiInstance.invalidateOperation(operationId, (error, data, response) => {
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
 **operationId** | **String**|  | 

### Return type

[**ImageImportOperation**](ImageImportOperation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listImportDockerfiles

> [String] listImportDockerfiles(operationId)

List uploaded dockerfiles

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImportsApi();
let operationId = "operationId_example"; // String | 
apiInstance.listImportDockerfiles(operationId, (error, data, response) => {
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
 **operationId** | **String**|  | 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listImportImageConfigs

> [String] listImportImageConfigs(operationId)

List uploaded image configs

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImportsApi();
let operationId = "operationId_example"; // String | 
apiInstance.listImportImageConfigs(operationId, (error, data, response) => {
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
 **operationId** | **String**|  | 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listImportImageManifests

> [String] listImportImageManifests(operationId)

List uploaded image manifests

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImportsApi();
let operationId = "operationId_example"; // String | 
apiInstance.listImportImageManifests(operationId, (error, data, response) => {
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
 **operationId** | **String**|  | 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listImportPackages

> [String] listImportPackages(operationId)

List uploaded package manifests

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImportsApi();
let operationId = "operationId_example"; // String | 
apiInstance.listImportPackages(operationId, (error, data, response) => {
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
 **operationId** | **String**|  | 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listImportParentManifests

> [String] listImportParentManifests(operationId)

List uploaded parent manifests (manifest lists for a tag)

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImportsApi();
let operationId = "operationId_example"; // String | 
apiInstance.listImportParentManifests(operationId, (error, data, response) => {
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
 **operationId** | **String**|  | 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listOperations

> [ImageImportOperation] listOperations()

Lists in-progress imports

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImportsApi();
apiInstance.listOperations((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[ImageImportOperation]**](ImageImportOperation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

