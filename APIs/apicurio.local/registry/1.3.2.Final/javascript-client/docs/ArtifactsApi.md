# ApicurioRegistryApi.ArtifactsApi

All URIs are relative to *http://apicurio.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createArtifact**](ArtifactsApi.md#createArtifact) | **POST** /artifacts | Create artifact
[**deleteArtifact**](ArtifactsApi.md#deleteArtifact) | **DELETE** /artifacts/{artifactId} | Delete artifact
[**getArtifactByGlobalId**](ArtifactsApi.md#getArtifactByGlobalId) | **GET** /ids/{globalId} | Get artifact by global ID
[**getLatestArtifact**](ArtifactsApi.md#getLatestArtifact) | **GET** /artifacts/{artifactId} | Get latest artifact
[**listArtifacts**](ArtifactsApi.md#listArtifacts) | **GET** /artifacts | List all artifact IDs
[**searchArtifacts_0**](ArtifactsApi.md#searchArtifacts_0) | **GET** /search/artifacts | Search for artifacts
[**updateArtifact**](ArtifactsApi.md#updateArtifact) | **PUT** /artifacts/{artifactId} | Update artifact
[**updateArtifactState**](ArtifactsApi.md#updateArtifactState) | **PUT** /artifacts/{artifactId}/state | Update artifact state



## createArtifact

> ArtifactMetaData createArtifact(opts)

Create artifact

Creates a new artifact by posting the artifact content.  The body of the request should be the raw content of the artifact.  This is typically in JSON format for *most* of the  supported types, but may be in another format for a few (for example, &#x60;PROTOBUF&#x60;).  The registry attempts to figure out what kind of artifact is being added from the following supported list:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * Protobuf File Descriptor (&#x60;PROTOBUF_FD&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;)  Alternatively, you can specify the artifact type using the &#x60;X-Registry-ArtifactType&#x60;  HTTP request header, or include a hint in the request&#39;s &#x60;Content-Type&#x60;.  For example:  &#x60;&#x60;&#x60; Content-Type: application/json; artifactType&#x3D;AVRO &#x60;&#x60;&#x60;  An artifact is created using the content provided in the body of the request.  This content is created under a unique artifact ID that can be provided in the request using the &#x60;X-Registry-ArtifactId&#x60; request header.  If not provided in the request, the server generates a unique ID for the artifact.  It is typically recommended that callers provide the ID, because this is typically a meaningful identifier,  and for most use cases should be supplied by the caller.  If an artifact with the provided artifact ID already exists, the default behavior is for the server to reject the content with a 409 error.  However, the caller can supply the &#x60;ifExists&#x60; query parameter to alter this default behavior. The &#x60;ifExists&#x60; query parameter can have one of the following values:  * &#x60;FAIL&#x60; (*default*) - server rejects the content with a 409 error * &#x60;UPDATE&#x60; - server updates the existing artifact and returns the new metadata * &#x60;RETURN&#x60; - server does not create or add content to the server, but instead  returns the metadata for the existing artifact * &#x60;RETURN_OR_UPDATE&#x60; - server returns an existing **version** that matches the  provided content if such a version exists, otherwise a new version is created  This operation may fail for one of the following reasons:  * An invalid &#x60;ArtifactType&#x60; was indicated (HTTP error &#x60;400&#x60;) * No &#x60;ArtifactType&#x60; was indicated and the server could not determine one from the content (HTTP error &#x60;400&#x60;) * Provided content (request body) was empty (HTTP error &#x60;400&#x60;) * An artifact with the provided ID already exists (HTTP error &#x60;409&#x60;) * The content violates one of the configured global rules (HTTP error &#x60;409&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.ArtifactsApi();
let opts = {
  'xRegistryArtifactType': "xRegistryArtifactType_example", // String | Specifies the type of the artifact being added. Possible values include:  * Avro (`AVRO`) * Protobuf (`PROTOBUF`) * Protobuf File Descriptor (`PROTOBUF_FD`) * JSON Schema (`JSON`) * Kafka Connect (`KCONNECT`) * OpenAPI (`OPENAPI`) * AsyncAPI (`ASYNCAPI`) * GraphQL (`GRAPHQL`) * Web Services Description Language (`WSDL`) * XML Schema (`XSD`)
  'xRegistryArtifactId': "xRegistryArtifactId_example", // String | A client-provided, globally unique identifier for the new artifact.
  'ifExists': "ifExists_example" // String | Set this option to instruct the server on what to do if the artifact already exists.
};
apiInstance.createArtifact(opts, (error, data, response) => {
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
 **xRegistryArtifactType** | **String**| Specifies the type of the artifact being added. Possible values include:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * Protobuf File Descriptor (&#x60;PROTOBUF_FD&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;) | [optional] 
 **xRegistryArtifactId** | **String**| A client-provided, globally unique identifier for the new artifact. | [optional] 
 **ifExists** | **String**| Set this option to instruct the server on what to do if the artifact already exists. | [optional] 

### Return type

[**ArtifactMetaData**](ArtifactMetaData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteArtifact

> deleteArtifact(artifactId)

Delete artifact

Deletes an artifact completely, resulting in all versions of the artifact also being deleted.  This may fail for one of the following reasons:  * No artifact with the &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.ArtifactsApi();
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
apiInstance.deleteArtifact(artifactId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getArtifactByGlobalId

> getArtifactByGlobalId(globalId)

Get artifact by global ID

Gets the content for an artifact version in the registry using its globally unique identifier.  This operation may fail for one of the following reasons:  * No artifact version with this &#x60;globalId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.ArtifactsApi();
let globalId = 789; // Number | Global identifier for an artifact version.
apiInstance.getArtifactByGlobalId(globalId, (error, data, response) => {
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
 **globalId** | **Number**| Global identifier for an artifact version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/x-protobuf, application/x-protobuffer


## getLatestArtifact

> getLatestArtifact(artifactId)

Get latest artifact

Returns the latest version of the artifact in its raw form.  The &#x60;Content-Type&#x60; of the response depends on the artifact type.  In most cases, this is &#x60;application/json&#x60;, but for some types it may be different (for example, &#x60;PROTOBUF&#x60;). If the latest version of the artifact is marked as &#x60;DISABLED&#x60;, the next available non-disabled version will be used.  This operation may fail for one of the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists or all versions are &#x60;DISABLED&#x60; (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.ArtifactsApi();
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
apiInstance.getLatestArtifact(artifactId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/graphql, application/json, application/x-protobuf, application/x-protobuffer


## listArtifacts

> [String] listArtifacts()

List all artifact IDs

Returns a list of IDs of all artifacts in the registry as a flat list.  Typically the server is configured to limit the number of artifact IDs returned when a large number  of artifacts exist. In this case, the result of this call may be non-deterministic. The  default limit is typically 1000 artifacts.

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.ArtifactsApi();
apiInstance.listArtifacts((error, data, response) => {
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

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchArtifacts_0

> ArtifactSearchResults searchArtifacts_0(offset, limit, opts)

Search for artifacts

Returns a paginated list of all artifacts that match the provided search criteria. 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.ArtifactsApi();
let offset = 0; // Number | The number of artifacts to skip before starting to collect the result set.
let limit = 20; // Number | The number of artifacts to return.
let opts = {
  'search': "search_example", // String | The text to search.
  'over': "over_example", // String | What fields to search.
  'order': "order_example" // String | Sort order, ascending or descending.
};
apiInstance.searchArtifacts_0(offset, limit, opts, (error, data, response) => {
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
 **offset** | **Number**| The number of artifacts to skip before starting to collect the result set. | [default to 0]
 **limit** | **Number**| The number of artifacts to return. | [default to 20]
 **search** | **String**| The text to search. | [optional] 
 **over** | **String**| What fields to search. | [optional] 
 **order** | **String**| Sort order, ascending or descending. | [optional] 

### Return type

[**ArtifactSearchResults**](ArtifactSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateArtifact

> ArtifactMetaData updateArtifact(artifactId, opts)

Update artifact

Updates an artifact by uploading new content.  The body of the request should be the raw content of the artifact.  This is typically in JSON format for *most* of the supported types, but may be in another format for a few (for example, &#x60;PROTOBUF&#x60;).  The registry attempts to figure out what kind of artifact is being added from the following supported list:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * Protobuf File Descriptor (&#x60;PROTOBUF_FD&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;)  Alternatively, you can specify the artifact type using the &#x60;X-Registry-ArtifactType&#x60;  HTTP request header, or include a hint in the request&#39;s &#x60;Content-Type&#x60;.  For example:  &#x60;&#x60;&#x60; Content-Type: application/json; artifactType&#x3D;AVRO &#x60;&#x60;&#x60;  The update could fail for a number of reasons including:  * Provided content (request body) was empty (HTTP error &#x60;400&#x60;) * No artifact with the &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * The new content violates one of the rules configured for the artifact (HTTP error &#x60;409&#x60;) * The provided artifact type is not recognized (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)  When successful, this creates a new version of the artifact, making it the most recent (and therefore official) version of the artifact.

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.ArtifactsApi();
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
let opts = {
  'xRegistryArtifactType': "xRegistryArtifactType_example" // String | Specifies the type of the artifact being added.  Possible values include:  * Avro (`AVRO`) * Protobuf (`PROTOBUF`) * Protobuf File Descriptor (`PROTOBUF_FD`) * JSON Schema (`JSON`) * Kafka Connect (`KCONNECT`) * OpenAPI (`OPENAPI`) * AsyncAPI (`ASYNCAPI`) * GraphQL (`GRAPHQL`) * Web Services Description Language (`WSDL`) * XML Schema (`XSD`)
};
apiInstance.updateArtifact(artifactId, opts, (error, data, response) => {
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
 **xRegistryArtifactType** | **String**| Specifies the type of the artifact being added.  Possible values include:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * Protobuf File Descriptor (&#x60;PROTOBUF_FD&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;) | [optional] 

### Return type

[**ArtifactMetaData**](ArtifactMetaData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateArtifactState

> updateArtifactState(artifactId, updateState)

Update artifact state

Updates the state of the artifact. For example, you can use this to mark the latest version of an artifact as &#x60;DEPRECATED&#x60;. The operation changes the state of the latest version of the artifact, even if this version is &#x60;DISABLED&#x60;. If multiple versions exist, only the most recent is changed.  The following state changes are supported:  * Enabled -&gt; Disabled * Enabled -&gt; Deprecated * Enabled -&gt; Deleted * Disabled -&gt; Enabled * Disabled -&gt; Deleted * Disabled -&gt; Deprecated * Deprecated -&gt; Deleted  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * Artifact cannot transition to the given state (HTTP error &#x60;400&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.ArtifactsApi();
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
let updateState = new ApicurioRegistryApi.UpdateState(); // UpdateState | 
apiInstance.updateArtifactState(artifactId, updateState, (error, data, response) => {
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
 **updateState** | [**UpdateState**](UpdateState.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

