# AnchoreEngineApiServer.ImagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addImage**](ImagesApi.md#addImage) | **POST** /images | Submit a new image for analysis by the engine
[**deleteImage**](ImagesApi.md#deleteImage) | **DELETE** /images/{imageDigest} | Delete an image analysis
[**deleteImageByImageId**](ImagesApi.md#deleteImageByImageId) | **DELETE** /images/by_id/{imageId} | Delete image by docker imageId
[**deleteImagesAsync**](ImagesApi.md#deleteImagesAsync) | **DELETE** /images | Bulk mark images for deletion
[**getImage**](ImagesApi.md#getImage) | **GET** /images/{imageDigest} | Get image metadata
[**getImageByImageId**](ImagesApi.md#getImageByImageId) | **GET** /images/by_id/{imageId} | Lookup image by docker imageId
[**getImageContentByType**](ImagesApi.md#getImageContentByType) | **GET** /images/{imageDigest}/content/{ctype} | Get the content of an image by type
[**getImageContentByTypeFiles**](ImagesApi.md#getImageContentByTypeFiles) | **GET** /images/{imageDigest}/content/files | Get the content of an image by type files
[**getImageContentByTypeImageId**](ImagesApi.md#getImageContentByTypeImageId) | **GET** /images/by_id/{imageId}/content/{ctype} | Get the content of an image by type
[**getImageContentByTypeImageIdFiles**](ImagesApi.md#getImageContentByTypeImageIdFiles) | **GET** /images/by_id/{imageId}/content/files | Get the content of an image by type files
[**getImageContentByTypeImageIdJavapackage**](ImagesApi.md#getImageContentByTypeImageIdJavapackage) | **GET** /images/by_id/{imageId}/content/java | Get the content of an image by type java
[**getImageContentByTypeJavapackage**](ImagesApi.md#getImageContentByTypeJavapackage) | **GET** /images/{imageDigest}/content/java | Get the content of an image by type java
[**getImageContentByTypeMalware**](ImagesApi.md#getImageContentByTypeMalware) | **GET** /images/{imageDigest}/content/malware | Get the content of an image by type malware
[**getImageMetadataByType**](ImagesApi.md#getImageMetadataByType) | **GET** /images/{imageDigest}/metadata/{mtype} | Get the metadata of an image by type
[**getImagePolicyCheck**](ImagesApi.md#getImagePolicyCheck) | **GET** /images/{imageDigest}/check | Check policy evaluation status for image
[**getImagePolicyCheckByImageId**](ImagesApi.md#getImagePolicyCheckByImageId) | **GET** /images/by_id/{imageId}/check | Check policy evaluation status for image
[**getImageSbomNative**](ImagesApi.md#getImageSbomNative) | **GET** /images/{imageDigest}/sboms/native | Get image sbom in the native Anchore format
[**getImageVulnerabilitiesByType**](ImagesApi.md#getImageVulnerabilitiesByType) | **GET** /images/{imageDigest}/vuln/{vtype} | Get vulnerabilities by type
[**getImageVulnerabilitiesByTypeImageId**](ImagesApi.md#getImageVulnerabilitiesByTypeImageId) | **GET** /images/by_id/{imageId}/vuln/{vtype} | Get vulnerabilities by type
[**getImageVulnerabilityTypes**](ImagesApi.md#getImageVulnerabilityTypes) | **GET** /images/{imageDigest}/vuln | Get vulnerability types
[**getImageVulnerabilityTypesByImageId**](ImagesApi.md#getImageVulnerabilityTypesByImageId) | **GET** /images/by_id/{imageId}/vuln | Get vulnerability types
[**listImageContent**](ImagesApi.md#listImageContent) | **GET** /images/{imageDigest}/content | List image content types
[**listImageContentByImageid**](ImagesApi.md#listImageContentByImageid) | **GET** /images/by_id/{imageId}/content | List image content types
[**listImageMetadata**](ImagesApi.md#listImageMetadata) | **GET** /images/{imageDigest}/metadata | List image metadata types
[**listImages**](ImagesApi.md#listImages) | **GET** /images | List all visible images



## addImage

> [AnchoreImage] addImage(imageAnalysisRequest, opts)

Submit a new image for analysis by the engine

Creates a new analysis task that is executed asynchronously

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageAnalysisRequest = new AnchoreEngineApiServer.ImageAnalysisRequest(); // ImageAnalysisRequest | 
let opts = {
  'force': true, // Boolean | Override any existing entry in the system
  'autosubscribe': true, // Boolean | Instruct engine to automatically begin watching the added tag for updates from registry
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.addImage(imageAnalysisRequest, opts, (error, data, response) => {
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
 **imageAnalysisRequest** | [**ImageAnalysisRequest**](ImageAnalysisRequest.md)|  | 
 **force** | **Boolean**| Override any existing entry in the system | [optional] 
 **autosubscribe** | **Boolean**| Instruct engine to automatically begin watching the added tag for updates from registry | [optional] 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**[AnchoreImage]**](AnchoreImage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteImage

> DeleteImageResponse deleteImage(imageDigest, opts)

Delete an image analysis

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageDigest = "imageDigest_example"; // String | 
let opts = {
  'force': true, // Boolean | 
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.deleteImage(imageDigest, opts, (error, data, response) => {
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
 **imageDigest** | **String**|  | 
 **force** | **Boolean**|  | [optional] 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**DeleteImageResponse**](DeleteImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteImageByImageId

> DeleteImageResponse deleteImageByImageId(imageId, opts)

Delete image by docker imageId

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageId = "imageId_example"; // String | 
let opts = {
  'force': true, // Boolean | 
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.deleteImageByImageId(imageId, opts, (error, data, response) => {
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
 **imageId** | **String**|  | 
 **force** | **Boolean**|  | [optional] 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**DeleteImageResponse**](DeleteImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteImagesAsync

> [DeleteImageResponse] deleteImagesAsync(imageDigests, opts)

Bulk mark images for deletion

Delete analysis for image digests in the list asynchronously

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageDigests = ["null"]; // [String] | 
let opts = {
  'force': true, // Boolean | 
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.deleteImagesAsync(imageDigests, opts, (error, data, response) => {
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
 **imageDigests** | [**[String]**](String.md)|  | 
 **force** | **Boolean**|  | [optional] 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**[DeleteImageResponse]**](DeleteImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImage

> [AnchoreImage] getImage(imageDigest, opts)

Get image metadata

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageDigest = "imageDigest_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getImage(imageDigest, opts, (error, data, response) => {
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
 **imageDigest** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**[AnchoreImage]**](AnchoreImage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageByImageId

> [AnchoreImage] getImageByImageId(imageId, opts)

Lookup image by docker imageId

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageId = "imageId_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getImageByImageId(imageId, opts, (error, data, response) => {
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
 **imageId** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**[AnchoreImage]**](AnchoreImage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageContentByType

> ContentPackageResponse getImageContentByType(imageDigest, ctype, opts)

Get the content of an image by type

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageDigest = "imageDigest_example"; // String | 
let ctype = "ctype_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getImageContentByType(imageDigest, ctype, opts, (error, data, response) => {
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
 **imageDigest** | **String**|  | 
 **ctype** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**ContentPackageResponse**](ContentPackageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageContentByTypeFiles

> ContentFilesResponse getImageContentByTypeFiles(imageDigest, opts)

Get the content of an image by type files

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageDigest = "imageDigest_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getImageContentByTypeFiles(imageDigest, opts, (error, data, response) => {
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
 **imageDigest** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**ContentFilesResponse**](ContentFilesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageContentByTypeImageId

> ContentPackageResponse getImageContentByTypeImageId(imageId, ctype, opts)

Get the content of an image by type

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageId = "imageId_example"; // String | 
let ctype = "ctype_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getImageContentByTypeImageId(imageId, ctype, opts, (error, data, response) => {
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
 **imageId** | **String**|  | 
 **ctype** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**ContentPackageResponse**](ContentPackageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageContentByTypeImageIdFiles

> ContentFilesResponse getImageContentByTypeImageIdFiles(imageId, opts)

Get the content of an image by type files

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageId = "imageId_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getImageContentByTypeImageIdFiles(imageId, opts, (error, data, response) => {
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
 **imageId** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**ContentFilesResponse**](ContentFilesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageContentByTypeImageIdJavapackage

> ContentJAVAPackageResponse getImageContentByTypeImageIdJavapackage(imageId, opts)

Get the content of an image by type java

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageId = "imageId_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getImageContentByTypeImageIdJavapackage(imageId, opts, (error, data, response) => {
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
 **imageId** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**ContentJAVAPackageResponse**](ContentJAVAPackageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageContentByTypeJavapackage

> ContentJAVAPackageResponse getImageContentByTypeJavapackage(imageDigest, opts)

Get the content of an image by type java

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageDigest = "imageDigest_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getImageContentByTypeJavapackage(imageDigest, opts, (error, data, response) => {
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
 **imageDigest** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**ContentJAVAPackageResponse**](ContentJAVAPackageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageContentByTypeMalware

> ContentMalwareResponse getImageContentByTypeMalware(imageDigest, opts)

Get the content of an image by type malware

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageDigest = "imageDigest_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getImageContentByTypeMalware(imageDigest, opts, (error, data, response) => {
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
 **imageDigest** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**ContentMalwareResponse**](ContentMalwareResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageMetadataByType

> MetadataResponse getImageMetadataByType(imageDigest, mtype, opts)

Get the metadata of an image by type

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageDigest = "imageDigest_example"; // String | 
let mtype = "mtype_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getImageMetadataByType(imageDigest, mtype, opts, (error, data, response) => {
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
 **imageDigest** | **String**|  | 
 **mtype** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**MetadataResponse**](MetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImagePolicyCheck

> [Object] getImagePolicyCheck(imageDigest, tag, opts)

Check policy evaluation status for image

Get the policy evaluation for the given image

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageDigest = "imageDigest_example"; // String | 
let tag = "tag_example"; // String | 
let opts = {
  'policyId': "policyId_example", // String | 
  'detail': true, // Boolean | 
  'history': true, // Boolean | 
  'interactive': true, // Boolean | 
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getImagePolicyCheck(imageDigest, tag, opts, (error, data, response) => {
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
 **imageDigest** | **String**|  | 
 **tag** | **String**|  | 
 **policyId** | **String**|  | [optional] 
 **detail** | **Boolean**|  | [optional] 
 **history** | **Boolean**|  | [optional] 
 **interactive** | **Boolean**|  | [optional] 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

**[Object]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImagePolicyCheckByImageId

> [Object] getImagePolicyCheckByImageId(imageId, tag, opts)

Check policy evaluation status for image

Get the policy evaluation for the given image

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageId = "imageId_example"; // String | 
let tag = "tag_example"; // String | 
let opts = {
  'policyId': "policyId_example", // String | 
  'detail': true, // Boolean | 
  'history': true, // Boolean | 
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getImagePolicyCheckByImageId(imageId, tag, opts, (error, data, response) => {
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
 **imageId** | **String**|  | 
 **tag** | **String**|  | 
 **policyId** | **String**|  | [optional] 
 **detail** | **Boolean**|  | [optional] 
 **history** | **Boolean**|  | [optional] 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

**[Object]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageSbomNative

> File getImageSbomNative(imageDigest, opts)

Get image sbom in the native Anchore format

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageDigest = "imageDigest_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getImageSbomNative(imageDigest, opts, (error, data, response) => {
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
 **imageDigest** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/gzip


## getImageVulnerabilitiesByType

> VulnerabilityResponse getImageVulnerabilitiesByType(imageDigest, vtype, opts)

Get vulnerabilities by type

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageDigest = "imageDigest_example"; // String | 
let vtype = "vtype_example"; // String | 
let opts = {
  'forceRefresh': true, // Boolean | 
  'vendorOnly': true, // Boolean | Filter results to include only vulnerabilities that are not marked as invalid by upstream OS vendor data. When set to true, it will filter out all vulnerabilities where `will_not_fix` is False. If false all vulnerabilities are returned regardless of `will_not_fix`
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getImageVulnerabilitiesByType(imageDigest, vtype, opts, (error, data, response) => {
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
 **imageDigest** | **String**|  | 
 **vtype** | **String**|  | 
 **forceRefresh** | **Boolean**|  | [optional] 
 **vendorOnly** | **Boolean**| Filter results to include only vulnerabilities that are not marked as invalid by upstream OS vendor data. When set to true, it will filter out all vulnerabilities where &#x60;will_not_fix&#x60; is False. If false all vulnerabilities are returned regardless of &#x60;will_not_fix&#x60; | [optional] 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**VulnerabilityResponse**](VulnerabilityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageVulnerabilitiesByTypeImageId

> VulnerabilityResponse getImageVulnerabilitiesByTypeImageId(imageId, vtype, opts)

Get vulnerabilities by type

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageId = "imageId_example"; // String | 
let vtype = "vtype_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getImageVulnerabilitiesByTypeImageId(imageId, vtype, opts, (error, data, response) => {
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
 **imageId** | **String**|  | 
 **vtype** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**VulnerabilityResponse**](VulnerabilityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageVulnerabilityTypes

> [String] getImageVulnerabilityTypes(imageDigest, opts)

Get vulnerability types

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageDigest = "imageDigest_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getImageVulnerabilityTypes(imageDigest, opts, (error, data, response) => {
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
 **imageDigest** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageVulnerabilityTypesByImageId

> [String] getImageVulnerabilityTypesByImageId(imageId, opts)

Get vulnerability types

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageId = "imageId_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getImageVulnerabilityTypesByImageId(imageId, opts, (error, data, response) => {
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
 **imageId** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listImageContent

> [String] listImageContent(imageDigest, opts)

List image content types

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageDigest = "imageDigest_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.listImageContent(imageDigest, opts, (error, data, response) => {
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
 **imageDigest** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listImageContentByImageid

> [String] listImageContentByImageid(imageId, opts)

List image content types

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageId = "imageId_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.listImageContentByImageid(imageId, opts, (error, data, response) => {
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
 **imageId** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listImageMetadata

> [String] listImageMetadata(imageDigest, opts)

List image metadata types

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let imageDigest = "imageDigest_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.listImageMetadata(imageDigest, opts, (error, data, response) => {
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
 **imageDigest** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listImages

> [AnchoreImage] listImages(opts)

List all visible images

List all images visible to the user

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImagesApi();
let opts = {
  'history': true, // Boolean | Include image history in the response
  'fulltag': "fulltag_example", // String | Full docker-pull string to filter results by (e.g. docker.io/library/nginx:latest, or myhost.com:5000/testimages:v1.1.1)
  'imageStatus': "'active'", // String | Filter by image_status value on the record. Default if omitted is 'active'.
  'analysisStatus': "analysisStatus_example", // String | Filter by analysis_status value on the record.
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.listImages(opts, (error, data, response) => {
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
 **history** | **Boolean**| Include image history in the response | [optional] 
 **fulltag** | **String**| Full docker-pull string to filter results by (e.g. docker.io/library/nginx:latest, or myhost.com:5000/testimages:v1.1.1) | [optional] 
 **imageStatus** | **String**| Filter by image_status value on the record. Default if omitted is &#39;active&#39;. | [optional] [default to &#39;active&#39;]
 **analysisStatus** | **String**| Filter by analysis_status value on the record. | [optional] 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**[AnchoreImage]**](AnchoreImage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

