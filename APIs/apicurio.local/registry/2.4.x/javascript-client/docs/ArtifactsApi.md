# ApicurioRegistryApiV2.ArtifactsApi

All URIs are relative to *http://apicurio.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createArtifact**](ArtifactsApi.md#createArtifact) | **POST** /groups/{groupId}/artifacts | Create artifact
[**deleteArtifact**](ArtifactsApi.md#deleteArtifact) | **DELETE** /groups/{groupId}/artifacts/{artifactId} | Delete artifact
[**deleteArtifactsInGroup**](ArtifactsApi.md#deleteArtifactsInGroup) | **DELETE** /groups/{groupId}/artifacts | Delete artifacts in group
[**getContentByGlobalId**](ArtifactsApi.md#getContentByGlobalId) | **GET** /ids/globalIds/{globalId} | Get artifact by global ID
[**getContentByHash**](ArtifactsApi.md#getContentByHash) | **GET** /ids/contentHashes/{contentHash}/ | Get artifact content by SHA-256 hash
[**getContentById**](ArtifactsApi.md#getContentById) | **GET** /ids/contentIds/{contentId}/ | Get artifact content by ID
[**getLatestArtifact**](ArtifactsApi.md#getLatestArtifact) | **GET** /groups/{groupId}/artifacts/{artifactId} | Get latest artifact
[**listArtifactsInGroup**](ArtifactsApi.md#listArtifactsInGroup) | **GET** /groups/{groupId}/artifacts | List artifacts in group
[**referencesByContentHash**](ArtifactsApi.md#referencesByContentHash) | **GET** /ids/contentHashes/{contentHash}/references | List artifact references by hash
[**referencesByContentId**](ArtifactsApi.md#referencesByContentId) | **GET** /ids/contentIds/{contentId}/references | List artifact references by content ID
[**referencesByGlobalId**](ArtifactsApi.md#referencesByGlobalId) | **GET** /ids/globalIds/{globalId}/references | List artifact references by global ID
[**searchArtifactsByContent_0**](ArtifactsApi.md#searchArtifactsByContent_0) | **POST** /search/artifacts | Search for artifacts by content
[**searchArtifacts_0**](ArtifactsApi.md#searchArtifacts_0) | **GET** /search/artifacts | Search for artifacts
[**updateArtifact**](ArtifactsApi.md#updateArtifact) | **PUT** /groups/{groupId}/artifacts/{artifactId} | Update artifact
[**updateArtifactState**](ArtifactsApi.md#updateArtifactState) | **PUT** /groups/{groupId}/artifacts/{artifactId}/state | Update artifact state



## createArtifact

> ArtifactMetaData createArtifact(groupId, body, opts)

Create artifact

Creates a new artifact by posting the artifact content.  The body of the request should be the raw content of the artifact.  This is typically in JSON format for *most* of the  supported types, but may be in another format for a few (for example, &#x60;PROTOBUF&#x60;).  The registry attempts to figure out what kind of artifact is being added from the following supported list:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;)  Alternatively, you can specify the artifact type using the &#x60;X-Registry-ArtifactType&#x60;  HTTP request header, or include a hint in the request&#39;s &#x60;Content-Type&#x60;.  For example:  &#x60;&#x60;&#x60; Content-Type: application/json; artifactType&#x3D;AVRO &#x60;&#x60;&#x60;  An artifact is created using the content provided in the body of the request.  This content is created under a unique artifact ID that can be provided in the request using the &#x60;X-Registry-ArtifactId&#x60; request header.  If not provided in the request, the server generates a unique ID for the artifact.  It is typically recommended that callers provide the ID, because this is typically a meaningful identifier,  and for most use cases should be supplied by the caller.  If an artifact with the provided artifact ID already exists, the default behavior is for the server to reject the content with a 409 error.  However, the caller can supply the &#x60;ifExists&#x60; query parameter to alter this default behavior. The &#x60;ifExists&#x60; query parameter can have one of the following values:  * &#x60;FAIL&#x60; (*default*) - server rejects the content with a 409 error * &#x60;UPDATE&#x60; - server updates the existing artifact and returns the new metadata * &#x60;RETURN&#x60; - server does not create or add content to the server, but instead  returns the metadata for the existing artifact * &#x60;RETURN_OR_UPDATE&#x60; - server returns an existing **version** that matches the  provided content if such a version exists, otherwise a new version is created  This operation may fail for one of the following reasons:  * An invalid &#x60;ArtifactType&#x60; was indicated (HTTP error &#x60;400&#x60;) * No &#x60;ArtifactType&#x60; was indicated and the server could not determine one from the content (HTTP error &#x60;400&#x60;) * Provided content (request body) was empty (HTTP error &#x60;400&#x60;) * An artifact with the provided ID already exists (HTTP error &#x60;409&#x60;) * The content violates one of the configured global rules (HTTP error &#x60;409&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.ArtifactsApi();
let groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
let body = {"components":{"schemas":{"Widget":{"description":"A sample data type.","example":{"property-1":"value1","property-2":true},"properties":{"property-1":{"type":"string"},"property-2":{"type":"boolean"}},"title":"Root Type for Widget","type":"object"}}},"info":{"description":"An example API design using OpenAPI.","title":"Empty API","version":"1.0.7"},"openapi":"3.0.2","paths":{"/widgets":{"get":{"responses":{"200":{"content":{"application/json":{"schema":{"items":{"type":"string"},"type":"array"}}},"description":"All widgets"}},"summary":"Get widgets"}}}}; // File | The content of the artifact being created. This is often, but not always, JSON data representing one of the supported artifact types:  * Avro (`AVRO`) * Protobuf (`PROTOBUF`) * JSON Schema (`JSON`) * Kafka Connect (`KCONNECT`) * OpenAPI (`OPENAPI`) * AsyncAPI (`ASYNCAPI`) * GraphQL (`GRAPHQL`) * Web Services Description Language (`WSDL`) * XML Schema (`XSD`) 
let opts = {
  'xRegistryArtifactType': "xRegistryArtifactType_example", // String | Specifies the type of the artifact being added. Possible values include:  * Avro (`AVRO`) * Protobuf (`PROTOBUF`) * JSON Schema (`JSON`) * Kafka Connect (`KCONNECT`) * OpenAPI (`OPENAPI`) * AsyncAPI (`ASYNCAPI`) * GraphQL (`GRAPHQL`) * Web Services Description Language (`WSDL`) * XML Schema (`XSD`)
  'xRegistryArtifactId': "xRegistryArtifactId_example", // String | A client-provided, globally unique identifier for the new artifact.
  'xRegistryVersion': "xRegistryVersion_example", // String | Specifies the version number of this initial version of the artifact content.  This would typically be a simple integer or a SemVer value.  If not provided, the server will assign a version number automatically (starting with version `1`).
  'ifExists': new ApicurioRegistryApiV2.IfExists(), // IfExists | Set this option to instruct the server on what to do if the artifact already exists.
  'canonical': true, // Boolean | Used only when the `ifExists` query parameter is set to `RETURN_OR_UPDATE`, this parameter can be set to `true` to indicate that the server should \"canonicalize\" the content when searching for a matching version.  The canonicalization algorithm is unique to each artifact type, but typically involves removing extra whitespace and formatting the content in a consistent manner.
  'xRegistryDescription': "xRegistryDescription_example", // String | Specifies the description of artifact being added. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content.
  'xRegistryDescriptionEncoded': "xRegistryDescriptionEncoded_example", // String | Specifies the description of artifact being added. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content.
  'xRegistryName': "xRegistryName_example", // String | Specifies the name of artifact being added. Name must be ASCII-only string. If this is not provided, the server will extract the name from the artifact content.
  'xRegistryNameEncoded': "xRegistryNameEncoded_example", // String | Specifies the name of artifact being added. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content.
  'xRegistryContentHash': "xRegistryContentHash_example", // String | Specifies the (optional) hash of the artifact to be verified.
  'xRegistryHashAlgorithm': "xRegistryHashAlgorithm_example" // String | The algorithm to use when checking the content validity. (available: SHA256, MD5; default: SHA256)
};
apiInstance.createArtifact(groupId, body, opts, (error, data, response) => {
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
 **body** | **File**| The content of the artifact being created. This is often, but not always, JSON data representing one of the supported artifact types:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;)  | 
 **xRegistryArtifactType** | **String**| Specifies the type of the artifact being added. Possible values include:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;) | [optional] 
 **xRegistryArtifactId** | **String**| A client-provided, globally unique identifier for the new artifact. | [optional] 
 **xRegistryVersion** | **String**| Specifies the version number of this initial version of the artifact content.  This would typically be a simple integer or a SemVer value.  If not provided, the server will assign a version number automatically (starting with version &#x60;1&#x60;). | [optional] 
 **ifExists** | [**IfExists**](.md)| Set this option to instruct the server on what to do if the artifact already exists. | [optional] 
 **canonical** | **Boolean**| Used only when the &#x60;ifExists&#x60; query parameter is set to &#x60;RETURN_OR_UPDATE&#x60;, this parameter can be set to &#x60;true&#x60; to indicate that the server should \&quot;canonicalize\&quot; the content when searching for a matching version.  The canonicalization algorithm is unique to each artifact type, but typically involves removing extra whitespace and formatting the content in a consistent manner. | [optional] 
 **xRegistryDescription** | **String**| Specifies the description of artifact being added. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content. | [optional] 
 **xRegistryDescriptionEncoded** | **String**| Specifies the description of artifact being added. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content. | [optional] 
 **xRegistryName** | **String**| Specifies the name of artifact being added. Name must be ASCII-only string. If this is not provided, the server will extract the name from the artifact content. | [optional] 
 **xRegistryNameEncoded** | **String**| Specifies the name of artifact being added. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content. | [optional] 
 **xRegistryContentHash** | **String**| Specifies the (optional) hash of the artifact to be verified. | [optional] 
 **xRegistryHashAlgorithm** | **String**| The algorithm to use when checking the content validity. (available: SHA256, MD5; default: SHA256) | [optional] 

### Return type

[**ArtifactMetaData**](ArtifactMetaData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/create.extended+json, application/vnd.create.extended+json
- **Accept**: application/json


## deleteArtifact

> deleteArtifact(groupId, artifactId)

Delete artifact

Deletes an artifact completely, resulting in all versions of the artifact also being deleted.  This may fail for one of the following reasons:  * No artifact with the &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.ArtifactsApi();
let groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
apiInstance.deleteArtifact(groupId, artifactId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteArtifactsInGroup

> deleteArtifactsInGroup(groupId)

Delete artifacts in group

Deletes all of the artifacts that exist in a given group.

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.ArtifactsApi();
let groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
apiInstance.deleteArtifactsInGroup(groupId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContentByGlobalId

> File getContentByGlobalId(globalId, opts)

Get artifact by global ID

Gets the content for an artifact version in the registry using its globally unique identifier.  This operation may fail for one of the following reasons:  * No artifact version with this &#x60;globalId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.ArtifactsApi();
let globalId = 789; // Number | Global identifier for an artifact version.
let opts = {
  'dereference': true // Boolean | Allows the user to specify if the content should be dereferenced when being returned
};
apiInstance.getContentByGlobalId(globalId, opts, (error, data, response) => {
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
 **dereference** | **Boolean**| Allows the user to specify if the content should be dereferenced when being returned | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## getContentByHash

> File getContentByHash(contentHash)

Get artifact content by SHA-256 hash

Gets the content for an artifact version in the registry using the  SHA-256 hash of the content.  This content hash may be shared by multiple artifact versions in the case where the artifact versions have identical content.  This operation may fail for one of the following reasons:  * No content with this &#x60;contentHash&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.ArtifactsApi();
let contentHash = "contentHash_example"; // String | SHA-256 content hash for a single artifact content.
apiInstance.getContentByHash(contentHash, (error, data, response) => {
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
 **contentHash** | **String**| SHA-256 content hash for a single artifact content. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## getContentById

> File getContentById(contentId)

Get artifact content by ID

Gets the content for an artifact version in the registry using the unique content identifier for that content.  This content ID may be shared by multiple artifact versions in the case where the artifact versions are identical.  This operation may fail for one of the following reasons:  * No content with this &#x60;contentId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.ArtifactsApi();
let contentId = 789; // Number | Global identifier for a single artifact content.
apiInstance.getContentById(contentId, (error, data, response) => {
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
 **contentId** | **Number**| Global identifier for a single artifact content. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## getLatestArtifact

> File getLatestArtifact(groupId, artifactId, opts)

Get latest artifact

Returns the latest version of the artifact in its raw form.  The &#x60;Content-Type&#x60; of the response depends on the artifact type.  In most cases, this is &#x60;application/json&#x60;, but  for some types it may be different (for example, &#x60;PROTOBUF&#x60;). If the latest version of the artifact is marked as &#x60;DISABLED&#x60;, the next available non-disabled version will be used.  This operation may fail for one of the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists or all versions are &#x60;DISABLED&#x60; (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.ArtifactsApi();
let groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
let opts = {
  'dereference': true // Boolean | Allows the user to specify if the content should be dereferenced when being returned
};
apiInstance.getLatestArtifact(groupId, artifactId, opts, (error, data, response) => {
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
 **dereference** | **Boolean**| Allows the user to specify if the content should be dereferenced when being returned | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## listArtifactsInGroup

> ArtifactSearchResults listArtifactsInGroup(groupId, opts)

List artifacts in group

Returns a list of all artifacts in the group.  This list is paged.

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.ArtifactsApi();
let groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
let opts = {
  'limit': 56, // Number | The number of artifacts to return.  Defaults to 20.
  'offset': 56, // Number | The number of artifacts to skip before starting the result set.  Defaults to 0.
  'order': new ApicurioRegistryApiV2.SortOrder(), // SortOrder | Sort order, ascending (`asc`) or descending (`desc`).
  'orderby': new ApicurioRegistryApiV2.SortBy() // SortBy | The field to sort by.  Can be one of:  * `name` * `createdOn` 
};
apiInstance.listArtifactsInGroup(groupId, opts, (error, data, response) => {
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
 **limit** | **Number**| The number of artifacts to return.  Defaults to 20. | [optional] 
 **offset** | **Number**| The number of artifacts to skip before starting the result set.  Defaults to 0. | [optional] 
 **order** | [**SortOrder**](.md)| Sort order, ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;). | [optional] 
 **orderby** | [**SortBy**](.md)| The field to sort by.  Can be one of:  * &#x60;name&#x60; * &#x60;createdOn&#x60;  | [optional] 

### Return type

[**ArtifactSearchResults**](ArtifactSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## referencesByContentHash

> [ArtifactReference] referencesByContentHash(contentHash)

List artifact references by hash

Returns a list containing all the artifact references using the artifact content hash.  This operation may fail for one of the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.ArtifactsApi();
let contentHash = "contentHash_example"; // String | SHA-256 content hash for a single artifact content.
apiInstance.referencesByContentHash(contentHash, (error, data, response) => {
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
 **contentHash** | **String**| SHA-256 content hash for a single artifact content. | 

### Return type

[**[ArtifactReference]**](ArtifactReference.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## referencesByContentId

> [ArtifactReference] referencesByContentId(contentId)

List artifact references by content ID

Returns a list containing all the artifact references using the artifact content ID.  This operation may fail for one of the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;)

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.ArtifactsApi();
let contentId = 789; // Number | Global identifier for a single artifact content.
apiInstance.referencesByContentId(contentId, (error, data, response) => {
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
 **contentId** | **Number**| Global identifier for a single artifact content. | 

### Return type

[**[ArtifactReference]**](ArtifactReference.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## referencesByGlobalId

> [ArtifactReference] referencesByGlobalId(globalId)

List artifact references by global ID

Returns a list containing all the artifact references using the artifact global ID.  This operation may fail for one of the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;)

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.ArtifactsApi();
let globalId = 789; // Number | Global identifier for an artifact version.
apiInstance.referencesByGlobalId(globalId, (error, data, response) => {
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

[**[ArtifactReference]**](ArtifactReference.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchArtifactsByContent_0

> ArtifactSearchResults searchArtifactsByContent_0(body, opts)

Search for artifacts by content

Returns a paginated list of all artifacts with at least one version that matches the posted content. 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.ArtifactsApi();
let body = "/path/to/file"; // File | The content to search for.
let opts = {
  'canonical': true, // Boolean | Parameter that can be set to `true` to indicate that the server should \"canonicalize\" the content when searching for matching artifacts.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner.  Must be used along with the `artifactType` query parameter.
  'artifactType': "artifactType_example", // String | Indicates the type of artifact represented by the content being used for the search.  This is only needed when using the `canonical` query parameter, so that the server knows how to canonicalize the content prior to searching for matching artifacts.
  'offset': 0, // Number | The number of artifacts to skip before starting to collect the result set.  Defaults to 0.
  'limit': 20, // Number | The number of artifacts to return.  Defaults to 20.
  'order': "order_example", // String | Sort order, ascending (`asc`) or descending (`desc`).
  'orderby': "orderby_example" // String | The field to sort by.  Can be one of:  * `name` * `createdOn` 
};
apiInstance.searchArtifactsByContent_0(body, opts, (error, data, response) => {
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
 **body** | **File**| The content to search for. | 
 **canonical** | **Boolean**| Parameter that can be set to &#x60;true&#x60; to indicate that the server should \&quot;canonicalize\&quot; the content when searching for matching artifacts.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner.  Must be used along with the &#x60;artifactType&#x60; query parameter. | [optional] 
 **artifactType** | **String**| Indicates the type of artifact represented by the content being used for the search.  This is only needed when using the &#x60;canonical&#x60; query parameter, so that the server knows how to canonicalize the content prior to searching for matching artifacts. | [optional] 
 **offset** | **Number**| The number of artifacts to skip before starting to collect the result set.  Defaults to 0. | [optional] [default to 0]
 **limit** | **Number**| The number of artifacts to return.  Defaults to 20. | [optional] [default to 20]
 **order** | **String**| Sort order, ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;). | [optional] 
 **orderby** | **String**| The field to sort by.  Can be one of:  * &#x60;name&#x60; * &#x60;createdOn&#x60;  | [optional] 

### Return type

[**ArtifactSearchResults**](ArtifactSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchArtifacts_0

> ArtifactSearchResults searchArtifacts_0(opts)

Search for artifacts

Returns a paginated list of all artifacts that match the provided filter criteria. 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.ArtifactsApi();
let opts = {
  'name': "name_example", // String | Filter by artifact name.
  'offset': 0, // Number | The number of artifacts to skip before starting to collect the result set.  Defaults to 0.
  'limit': 20, // Number | The number of artifacts to return.  Defaults to 20.
  'order': new ApicurioRegistryApiV2.SortOrder(), // SortOrder | Sort order, ascending (`asc`) or descending (`desc`).
  'orderby': new ApicurioRegistryApiV2.SortBy(), // SortBy | The field to sort by.  Can be one of:  * `name` * `createdOn` 
  'labels': ["null"], // [String] | Filter by label.  Include one or more label to only return artifacts containing all of the specified labels.
  'properties': ["null"], // [String] | Filter by one or more name/value property.  Separate each name/value pair using a colon.  For example `properties=foo:bar` will return only artifacts with a custom property named `foo` and value `bar`.
  'description': "description_example", // String | Filter by description.
  'group': "group_example", // String | Filter by artifact group.
  'globalId': 789, // Number | Filter by globalId.
  'contentId': 789 // Number | Filter by contentId.
};
apiInstance.searchArtifacts_0(opts, (error, data, response) => {
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
 **name** | **String**| Filter by artifact name. | [optional] 
 **offset** | **Number**| The number of artifacts to skip before starting to collect the result set.  Defaults to 0. | [optional] [default to 0]
 **limit** | **Number**| The number of artifacts to return.  Defaults to 20. | [optional] [default to 20]
 **order** | [**SortOrder**](.md)| Sort order, ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;). | [optional] 
 **orderby** | [**SortBy**](.md)| The field to sort by.  Can be one of:  * &#x60;name&#x60; * &#x60;createdOn&#x60;  | [optional] 
 **labels** | [**[String]**](String.md)| Filter by label.  Include one or more label to only return artifacts containing all of the specified labels. | [optional] 
 **properties** | [**[String]**](String.md)| Filter by one or more name/value property.  Separate each name/value pair using a colon.  For example &#x60;properties&#x3D;foo:bar&#x60; will return only artifacts with a custom property named &#x60;foo&#x60; and value &#x60;bar&#x60;. | [optional] 
 **description** | **String**| Filter by description. | [optional] 
 **group** | **String**| Filter by artifact group. | [optional] 
 **globalId** | **Number**| Filter by globalId. | [optional] 
 **contentId** | **Number**| Filter by contentId. | [optional] 

### Return type

[**ArtifactSearchResults**](ArtifactSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateArtifact

> ArtifactMetaData updateArtifact(groupId, artifactId, body, opts)

Update artifact

Updates an artifact by uploading new content.  The body of the request can be the raw content of the artifact or a JSON object containing both the raw content and a set of references to other artifacts..  This is typically in JSON format for *most* of the supported types, but may be in another format for a few (for example, &#x60;PROTOBUF&#x60;). The type of the content should be compatible with the artifact&#39;s type (it would be an error to update an &#x60;AVRO&#x60; artifact with new &#x60;OPENAPI&#x60; content, for example).  The update could fail for a number of reasons including:  * Provided content (request body) was empty (HTTP error &#x60;400&#x60;) * No artifact with the &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * The new content violates one of the rules configured for the artifact (HTTP error &#x60;409&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)  When successful, this creates a new version of the artifact, making it the most recent (and therefore official) version of the artifact.

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.ArtifactsApi();
let groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
let body = {"components":{"schemas":{"Widget":{"description":"A sample data type.","example":{"property-1":"value1","property-2":true},"properties":{"property-1":{"type":"string"},"property-2":{"type":"boolean"}},"title":"Root Type for Widget","type":"object"}}},"info":{"description":"An example API design using OpenAPI.","title":"Empty API","version":"1.0.7"},"openapi":"3.0.2","paths":{"/widgets":{"get":{"responses":{"200":{"content":{"application/json":{"schema":{"items":{"type":"string"},"type":"array"}}},"description":"All widgets"}},"summary":"Get widgets"}}}}; // File | The new content of the artifact being updated. This is often, but not always, JSON data representing one of the supported artifact types:  * Avro (`AVRO`) * Protobuf (`PROTOBUF`) * JSON Schema (`JSON`) * Kafka Connect (`KCONNECT`) * OpenAPI (`OPENAPI`) * AsyncAPI (`ASYNCAPI`) * GraphQL (`GRAPHQL`) * Web Services Description Language (`WSDL`) * XML Schema (`XSD`) 
let opts = {
  'xRegistryVersion': "xRegistryVersion_example", // String | Specifies the version number of this new version of the artifact content.  This would typically be a simple integer or a SemVer value.  If not provided, the server will assign a version number automatically.
  'xRegistryName': "xRegistryName_example", // String | Specifies the artifact name of this new version of the artifact content. Name must be ASCII-only string. If this is not provided, the server will extract the name from the artifact content.
  'xRegistryNameEncoded': "xRegistryNameEncoded_example", // String | Specifies the artifact name of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content.
  'xRegistryDescription': "xRegistryDescription_example", // String | Specifies the artifact description of this new version of the artifact content. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content.
  'xRegistryDescriptionEncoded': "xRegistryDescriptionEncoded_example" // String | Specifies the artifact description of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content.
};
apiInstance.updateArtifact(groupId, artifactId, body, opts, (error, data, response) => {
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
 **body** | **File**| The new content of the artifact being updated. This is often, but not always, JSON data representing one of the supported artifact types:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;)  | 
 **xRegistryVersion** | **String**| Specifies the version number of this new version of the artifact content.  This would typically be a simple integer or a SemVer value.  If not provided, the server will assign a version number automatically. | [optional] 
 **xRegistryName** | **String**| Specifies the artifact name of this new version of the artifact content. Name must be ASCII-only string. If this is not provided, the server will extract the name from the artifact content. | [optional] 
 **xRegistryNameEncoded** | **String**| Specifies the artifact name of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content. | [optional] 
 **xRegistryDescription** | **String**| Specifies the artifact description of this new version of the artifact content. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content. | [optional] 
 **xRegistryDescriptionEncoded** | **String**| Specifies the artifact description of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content. | [optional] 

### Return type

[**ArtifactMetaData**](ArtifactMetaData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/create.extended+json, application/vnd.create.extended+json
- **Accept**: application/json


## updateArtifactState

> updateArtifactState(groupId, artifactId, updateState)

Update artifact state

Updates the state of the artifact.  For example, you can use this to mark the latest version of an artifact as &#x60;DEPRECATED&#x60;. The operation changes the state of the latest version of the artifact, even if this version is &#x60;DISABLED&#x60;. If multiple versions exist, only the most recent is changed.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.ArtifactsApi();
let groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
let updateState = new ApicurioRegistryApiV2.UpdateState(); // UpdateState | 
apiInstance.updateArtifactState(groupId, artifactId, updateState, (error, data, response) => {
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
 **updateState** | [**UpdateState**](UpdateState.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

