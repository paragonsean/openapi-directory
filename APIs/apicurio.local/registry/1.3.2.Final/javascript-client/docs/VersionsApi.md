# ApicurioRegistryApi.VersionsApi

All URIs are relative to *http://apicurio.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createArtifactVersion**](VersionsApi.md#createArtifactVersion) | **POST** /artifacts/{artifactId}/versions | Create artifact version
[**getArtifactVersion**](VersionsApi.md#getArtifactVersion) | **GET** /artifacts/{artifactId}/versions/{version} | Get artifact version
[**listArtifactVersions**](VersionsApi.md#listArtifactVersions) | **GET** /artifacts/{artifactId}/versions | List artifact versions
[**searchVersions_0**](VersionsApi.md#searchVersions_0) | **GET** /search/artifacts/{artifactId}/versions | Search artifact versions
[**updateArtifactVersionState**](VersionsApi.md#updateArtifactVersionState) | **PUT** /artifacts/{artifactId}/versions/{version}/state | Update artifact version state



## createArtifactVersion

> VersionMetaData createArtifactVersion(artifactId, opts)

Create artifact version

Creates a new version of the artifact by uploading new content.  The configured rules for the artifact are applied, and if they all pass, the new content is added as the most recent  version of the artifact.  If any of the rules fail, an error is returned.  The body of the request should be the raw content of the new artifact version.  This  is typically in JSON format for *most* of the supported types, but may be in another  format for a few (for example, &#x60;PROTOBUF&#x60;).  The registry attempts to figure out what kind of artifact is being added from the following supported list:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * Protobuf File Descriptor (&#x60;PROTOBUF_FD&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;)  Alternatively, you can explicitly specify the artifact type using the &#x60;X-Registry-ArtifactType&#x60;  HTTP request header, or by including a hint in the request&#39;s &#x60;Content-Type&#x60;.  For example:  &#x60;&#x60;&#x60; Content-Type: application/json; artifactType&#x3D;AVRO &#x60;&#x60;&#x60;  This operation can fail for the following reasons:  * Provided content (request body) was empty (HTTP error &#x60;400&#x60;) * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * The new content violates one of the rules configured for the artifact (HTTP error &#x60;409&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.VersionsApi();
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
let opts = {
  'xRegistryArtifactType': "xRegistryArtifactType_example" // String | This header parameter can be used to indicate the type of the artifact being added. Possible values include:  * Avro (`AVRO`)    * Protobuf (`PROTOBUF`)   * Protobuf File Descriptor (`PROTOBUF_FD`)    * JSON Schema (`JSON`)    * Kafka Connect (`KCONNECT`)    * OpenAPI (`OPENAPI`)    * AsyncAPI (`ASYNCAPI`)   * GraphQL (`GRAPHQL`)    * Web Services Description Language (`WSDL`)    * XML Schema (`XSD`)
};
apiInstance.createArtifactVersion(artifactId, opts, (error, data, response) => {
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
 **xRegistryArtifactType** | **String**| This header parameter can be used to indicate the type of the artifact being added. Possible values include:  * Avro (&#x60;AVRO&#x60;)    * Protobuf (&#x60;PROTOBUF&#x60;)   * Protobuf File Descriptor (&#x60;PROTOBUF_FD&#x60;)    * JSON Schema (&#x60;JSON&#x60;)    * Kafka Connect (&#x60;KCONNECT&#x60;)    * OpenAPI (&#x60;OPENAPI&#x60;)    * AsyncAPI (&#x60;ASYNCAPI&#x60;)   * GraphQL (&#x60;GRAPHQL&#x60;)    * Web Services Description Language (&#x60;WSDL&#x60;)    * XML Schema (&#x60;XSD&#x60;) | [optional] 

### Return type

[**VersionMetaData**](VersionMetaData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getArtifactVersion

> getArtifactVersion(version, artifactId)

Get artifact version

Retrieves a single version of the artifact content.  Both the &#x60;artifactId&#x60; and the unique &#x60;version&#x60; number must be provided.  The &#x60;Content-Type&#x60; of the response depends  on the artifact type.  In most cases, this is &#x60;application/json&#x60;, but for some types  it may be different (for example, &#x60;PROTOBUF&#x60;).  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No version with this &#x60;version&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.VersionsApi();
let version = 56; // Number | The unique identifier of a specific version of the artifact content.
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
apiInstance.getArtifactVersion(version, artifactId, (error, data, response) => {
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
- **Accept**: application/graphql, application/json, application/x-protobuf, application/x-protobuffer


## listArtifactVersions

> [Number] listArtifactVersions(artifactId)

List artifact versions

Returns a list of all version numbers for the artifact.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.VersionsApi();
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
apiInstance.listArtifactVersions(artifactId, (error, data, response) => {
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

**[Number]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchVersions_0

> VersionSearchResults searchVersions_0(artifactId, offset, limit)

Search artifact versions

Searches for versions of a specific artifact.  This is typically used to get a listing of all versions of an artifact (for example, in a user interface).

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.VersionsApi();
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
let offset = 56; // Number | The number of versions to skip before starting to collect the result set.
let limit = 56; // Number | The number of versions to return.
apiInstance.searchVersions_0(artifactId, offset, limit, (error, data, response) => {
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
 **offset** | **Number**| The number of versions to skip before starting to collect the result set. | 
 **limit** | **Number**| The number of versions to return. | 

### Return type

[**VersionSearchResults**](VersionSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateArtifactVersionState

> updateArtifactVersionState(version, artifactId, updateState)

Update artifact version state

Updates the state of a specific version of an artifact.  For example, you can use  this operation to disable a specific version.  The following state changes are supported:  * Enabled -&gt; Disabled * Enabled -&gt; Deprecated * Enabled -&gt; Deleted * Disabled -&gt; Enabled * Disabled -&gt; Deleted * Disabled -&gt; Deprecated * Deprecated -&gt; Deleted  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No version with this &#x60;version&#x60; exists (HTTP error &#x60;404&#x60;) * Artifact version cannot transition to the given state (HTTP error &#x60;400&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.VersionsApi();
let version = 56; // Number | The unique identifier of a specific version of the artifact content.
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
let updateState = new ApicurioRegistryApi.UpdateState(); // UpdateState | 
apiInstance.updateArtifactVersionState(version, artifactId, updateState, (error, data, response) => {
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
 **updateState** | [**UpdateState**](UpdateState.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

