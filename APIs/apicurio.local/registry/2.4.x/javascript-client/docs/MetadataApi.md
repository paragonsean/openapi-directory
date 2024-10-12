# ApicurioRegistryApiV2.MetadataApi

All URIs are relative to *http://apicurio.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteArtifactVersionMetaData**](MetadataApi.md#deleteArtifactVersionMetaData) | **DELETE** /groups/{groupId}/artifacts/{artifactId}/versions/{version}/meta | Delete artifact version metadata
[**getArtifactMetaData**](MetadataApi.md#getArtifactMetaData) | **GET** /groups/{groupId}/artifacts/{artifactId}/meta | Get artifact metadata
[**getArtifactOwner**](MetadataApi.md#getArtifactOwner) | **GET** /groups/{groupId}/artifacts/{artifactId}/owner | Get artifact owner
[**getArtifactVersionMetaData**](MetadataApi.md#getArtifactVersionMetaData) | **GET** /groups/{groupId}/artifacts/{artifactId}/versions/{version}/meta | Get artifact version metadata
[**getArtifactVersionMetaDataByContent**](MetadataApi.md#getArtifactVersionMetaDataByContent) | **POST** /groups/{groupId}/artifacts/{artifactId}/meta | Get artifact version metadata by content
[**updateArtifactMetaData**](MetadataApi.md#updateArtifactMetaData) | **PUT** /groups/{groupId}/artifacts/{artifactId}/meta | Update artifact metadata
[**updateArtifactOwner**](MetadataApi.md#updateArtifactOwner) | **PUT** /groups/{groupId}/artifacts/{artifactId}/owner | Update artifact owner
[**updateArtifactVersionMetaData**](MetadataApi.md#updateArtifactVersionMetaData) | **PUT** /groups/{groupId}/artifacts/{artifactId}/versions/{version}/meta | Update artifact version metadata



## deleteArtifactVersionMetaData

> deleteArtifactVersionMetaData(groupId, artifactId, version)

Delete artifact version metadata

Deletes the user-editable metadata properties of the artifact version.  Any properties that are not user-editable are preserved.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No version with this &#x60;version&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.MetadataApi();
let groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
let version = "version_example"; // String | The unique identifier of a specific version of the artifact content.
apiInstance.deleteArtifactVersionMetaData(groupId, artifactId, version, (error, data, response) => {
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
 **groupId** | **String**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. | 
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. | 
 **version** | **String**| The unique identifier of a specific version of the artifact content. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getArtifactMetaData

> ArtifactMetaData getArtifactMetaData(groupId, artifactId)

Get artifact metadata

Gets the metadata for an artifact in the registry, based on the latest version. If the latest version of the artifact is marked as &#x60;DISABLED&#x60;, the next available non-disabled version will be used. The returned metadata includes both generated (read-only) and editable metadata (such as name and description).  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists  or all versions are &#x60;DISABLED&#x60; (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.MetadataApi();
let groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
apiInstance.getArtifactMetaData(groupId, artifactId, (error, data, response) => {
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
 **groupId** | **String**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. | 
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. | 

### Return type

[**ArtifactMetaData**](ArtifactMetaData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getArtifactOwner

> ArtifactOwner getArtifactOwner(groupId, artifactId)

Get artifact owner

Gets the owner of an artifact in the registry.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.MetadataApi();
let groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
apiInstance.getArtifactOwner(groupId, artifactId, (error, data, response) => {
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
 **groupId** | **String**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. | 
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. | 

### Return type

[**ArtifactOwner**](ArtifactOwner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getArtifactVersionMetaData

> VersionMetaData getArtifactVersionMetaData(groupId, artifactId, version)

Get artifact version metadata

Retrieves the metadata for a single version of the artifact.  The version metadata is  a subset of the artifact metadata and only includes the metadata that is specific to the version (for example, this doesn&#39;t include &#x60;modifiedOn&#x60;).  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No version with this &#x60;version&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.MetadataApi();
let groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
let version = "version_example"; // String | The unique identifier of a specific version of the artifact content.
apiInstance.getArtifactVersionMetaData(groupId, artifactId, version, (error, data, response) => {
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
 **groupId** | **String**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. | 
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. | 
 **version** | **String**| The unique identifier of a specific version of the artifact content. | 

### Return type

[**VersionMetaData**](VersionMetaData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getArtifactVersionMetaDataByContent

> VersionMetaData getArtifactVersionMetaDataByContent(groupId, artifactId, body, opts)

Get artifact version metadata by content

Gets the metadata for an artifact that matches the raw content.  Searches the registry for a version of the given artifact matching the content provided in the body of the POST.  This operation can fail for the following reasons:  * Provided content (request body) was empty (HTTP error &#x60;400&#x60;) * No artifact with the &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No artifact version matching the provided content exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.MetadataApi();
let groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
let body = {"components":{"schemas":{"Widget":{"description":"A sample data type.","example":{"property-1":"value1","property-2":true},"properties":{"property-1":{"type":"string"},"property-2":{"type":"boolean"}},"title":"Root Type for Widget","type":"object"}}},"info":{"description":"An example API design using OpenAPI.","title":"Empty API","version":"1.0.7"},"openapi":"3.0.2","paths":{"/widgets":{"get":{"responses":{"200":{"content":{"application/json":{"schema":{"items":{"type":"string"},"type":"array"}}},"description":"All widgets"}},"summary":"Get widgets"}}}}; // File | The content of an artifact version.
let opts = {
  'canonical': true // Boolean | Parameter that can be set to `true` to indicate that the server should \"canonicalize\" the content when searching for a matching version.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner.
};
apiInstance.getArtifactVersionMetaDataByContent(groupId, artifactId, body, opts, (error, data, response) => {
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
 **groupId** | **String**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. | 
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. | 
 **body** | **File**| The content of an artifact version. | 
 **canonical** | **Boolean**| Parameter that can be set to &#x60;true&#x60; to indicate that the server should \&quot;canonicalize\&quot; the content when searching for a matching version.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner. | [optional] 

### Return type

[**VersionMetaData**](VersionMetaData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/get.extended+json, application/vnd.get.extended+json
- **Accept**: application/json


## updateArtifactMetaData

> updateArtifactMetaData(groupId, artifactId, editableMetaData)

Update artifact metadata

Updates the editable parts of the artifact&#39;s metadata.  Not all metadata fields can be updated.  For example, &#x60;createdOn&#x60; and &#x60;createdBy&#x60; are both read-only properties.  This operation can fail for the following reasons:  * No artifact with the &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.MetadataApi();
let groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
let editableMetaData = new ApicurioRegistryApiV2.EditableMetaData(); // EditableMetaData | Updated artifact metadata.
apiInstance.updateArtifactMetaData(groupId, artifactId, editableMetaData, (error, data, response) => {
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
 **groupId** | **String**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. | 
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. | 
 **editableMetaData** | [**EditableMetaData**](EditableMetaData.md)| Updated artifact metadata. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateArtifactOwner

> updateArtifactOwner(groupId, artifactId, artifactOwner)

Update artifact owner

Changes the ownership of an artifact.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.MetadataApi();
let groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
let artifactOwner = new ApicurioRegistryApiV2.ArtifactOwner(); // ArtifactOwner | 
apiInstance.updateArtifactOwner(groupId, artifactId, artifactOwner, (error, data, response) => {
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
 **groupId** | **String**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. | 
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. | 
 **artifactOwner** | [**ArtifactOwner**](ArtifactOwner.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateArtifactVersionMetaData

> updateArtifactVersionMetaData(groupId, artifactId, version, editableMetaData)

Update artifact version metadata

Updates the user-editable portion of the artifact version&#39;s metadata.  Only some of  the metadata fields are editable by the user.  For example, &#x60;description&#x60; is editable,  but &#x60;createdOn&#x60; is not.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No version with this &#x60;version&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.MetadataApi();
let groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
let version = "version_example"; // String | The unique identifier of a specific version of the artifact content.
let editableMetaData = new ApicurioRegistryApiV2.EditableMetaData(); // EditableMetaData | 
apiInstance.updateArtifactVersionMetaData(groupId, artifactId, version, editableMetaData, (error, data, response) => {
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
 **groupId** | **String**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. | 
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. | 
 **version** | **String**| The unique identifier of a specific version of the artifact content. | 
 **editableMetaData** | [**EditableMetaData**](EditableMetaData.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

