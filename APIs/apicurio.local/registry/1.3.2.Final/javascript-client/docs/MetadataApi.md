# ApicurioRegistryApi.MetadataApi

All URIs are relative to *http://apicurio.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteArtifactVersionMetaData**](MetadataApi.md#deleteArtifactVersionMetaData) | **DELETE** /artifacts/{artifactId}/versions/{version}/meta | Delete artifact version metadata
[**getArtifactMetaData**](MetadataApi.md#getArtifactMetaData) | **GET** /artifacts/{artifactId}/meta | Get artifact metadata
[**getArtifactMetaDataByContent**](MetadataApi.md#getArtifactMetaDataByContent) | **POST** /artifacts/{artifactId}/meta | Get artifact metadata by content
[**getArtifactMetaDataByGlobalId**](MetadataApi.md#getArtifactMetaDataByGlobalId) | **GET** /ids/{globalId}/meta | Get global artifact metadata
[**getArtifactVersionMetaData**](MetadataApi.md#getArtifactVersionMetaData) | **GET** /artifacts/{artifactId}/versions/{version}/meta | Get artifact version metadata
[**updateArtifactMetaData**](MetadataApi.md#updateArtifactMetaData) | **PUT** /artifacts/{artifactId}/meta | Update artifact metadata
[**updateArtifactVersionMetaData**](MetadataApi.md#updateArtifactVersionMetaData) | **PUT** /artifacts/{artifactId}/versions/{version}/meta | Update artifact version metadata



## deleteArtifactVersionMetaData

> deleteArtifactVersionMetaData(version, artifactId)

Delete artifact version metadata

Deletes the user-editable metadata properties of the artifact version.  Any properties that are not user-editable are preserved.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No version with this &#x60;version&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.MetadataApi();
let version = 56; // Number | The unique identifier of a specific version of the artifact content.
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
apiInstance.deleteArtifactVersionMetaData(version, artifactId, (error, data, response) => {
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
 **version** | **Number**| The unique identifier of a specific version of the artifact content. | 
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getArtifactMetaData

> ArtifactMetaData getArtifactMetaData(artifactId)

Get artifact metadata

Gets the metadata for an artifact in the registry, based on the latest version. If the latest version of the artifact is marked as &#x60;DISABLED&#x60;, the next available non-disabled version will be used. The returned metadata includes both generated (read-only) and editable metadata (such as name and description).  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists or all versions are &#x60;DISABLED&#x60; (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.MetadataApi();
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
apiInstance.getArtifactMetaData(artifactId, (error, data, response) => {
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
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | 

### Return type

[**ArtifactMetaData**](ArtifactMetaData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getArtifactMetaDataByContent

> ArtifactMetaData getArtifactMetaDataByContent(artifactId)

Get artifact metadata by content

Gets the metadata for an artifact that matches the raw content.  Searches the registry for a version of the given artifact matching the content provided in the body of the POST.  This operation can fail for the following reasons:  * Provided content (request body) was empty (HTTP error &#x60;400&#x60;) * No artifact with the &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No artifact version matching the provided content exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.MetadataApi();
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
apiInstance.getArtifactMetaDataByContent(artifactId, (error, data, response) => {
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
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | 

### Return type

[**ArtifactMetaData**](ArtifactMetaData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getArtifactMetaDataByGlobalId

> ArtifactMetaData getArtifactMetaDataByGlobalId(globalId)

Get global artifact metadata

Gets the metadata for an artifact version in the registry using its globally unique identifier.  The returned metadata includes both generated (read-only) and editable metadata (such as name and description).  This operation may fail for one of the following reasons:  * No artifact version with this &#x60;globalId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.MetadataApi();
let globalId = 789; // Number | Global identifier for an artifact version.
apiInstance.getArtifactMetaDataByGlobalId(globalId, (error, data, response) => {
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
 **globalId** | **Number**| Global identifier for an artifact version. | 

### Return type

[**ArtifactMetaData**](ArtifactMetaData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getArtifactVersionMetaData

> VersionMetaData getArtifactVersionMetaData(version, artifactId)

Get artifact version metadata

Retrieves the metadata for a single version of the artifact.  The version metadata is  a subset of the artifact metadata and only includes the metadata that is specific to the version (for example, this doesn&#39;t include &#x60;modifiedOn&#x60;).  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No version with this &#x60;version&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.MetadataApi();
let version = 56; // Number | The unique identifier of a specific version of the artifact content.
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
apiInstance.getArtifactVersionMetaData(version, artifactId, (error, data, response) => {
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
 **version** | **Number**| The unique identifier of a specific version of the artifact content. | 
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | 

### Return type

[**VersionMetaData**](VersionMetaData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateArtifactMetaData

> updateArtifactMetaData(artifactId, editableMetaData)

Update artifact metadata

Updates the editable parts of the artifact&#39;s metadata.  Not all metadata fields can be updated.  For example, &#x60;createdOn&#x60; and &#x60;createdBy&#x60; are both read-only properties.  This operation can fail for the following reasons:  * No artifact with the &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.MetadataApi();
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
let editableMetaData = new ApicurioRegistryApi.EditableMetaData(); // EditableMetaData | Updated artifact metadata.
apiInstance.updateArtifactMetaData(artifactId, editableMetaData, (error, data, response) => {
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
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | 
 **editableMetaData** | [**EditableMetaData**](EditableMetaData.md)| Updated artifact metadata. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateArtifactVersionMetaData

> updateArtifactVersionMetaData(version, artifactId, editableMetaData)

Update artifact version metadata

Updates the user-editable portion of the artifact version&#39;s metadata.  Only some of  the metadata fields are editable by the user.  For example, &#x60;description&#x60; is editable,  but &#x60;createdOn&#x60; is not.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No version with this &#x60;version&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.MetadataApi();
let version = 56; // Number | The unique identifier of a specific version of the artifact content.
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
let editableMetaData = new ApicurioRegistryApi.EditableMetaData(); // EditableMetaData | 
apiInstance.updateArtifactVersionMetaData(version, artifactId, editableMetaData, (error, data, response) => {
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
 **version** | **Number**| The unique identifier of a specific version of the artifact content. | 
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | 
 **editableMetaData** | [**EditableMetaData**](EditableMetaData.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

