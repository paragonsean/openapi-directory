# ArtifactsApi

All URIs are relative to *http://apicurio.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createArtifact**](ArtifactsApi.md#createArtifact) | **POST** /groups/{groupId}/artifacts | Create artifact |
| [**deleteArtifact**](ArtifactsApi.md#deleteArtifact) | **DELETE** /groups/{groupId}/artifacts/{artifactId} | Delete artifact |
| [**deleteArtifactsInGroup**](ArtifactsApi.md#deleteArtifactsInGroup) | **DELETE** /groups/{groupId}/artifacts | Delete artifacts in group |
| [**getContentByGlobalId**](ArtifactsApi.md#getContentByGlobalId) | **GET** /ids/globalIds/{globalId} | Get artifact by global ID |
| [**getContentByHash**](ArtifactsApi.md#getContentByHash) | **GET** /ids/contentHashes/{contentHash}/ | Get artifact content by SHA-256 hash |
| [**getContentById**](ArtifactsApi.md#getContentById) | **GET** /ids/contentIds/{contentId}/ | Get artifact content by ID |
| [**getLatestArtifact**](ArtifactsApi.md#getLatestArtifact) | **GET** /groups/{groupId}/artifacts/{artifactId} | Get latest artifact |
| [**listArtifactsInGroup**](ArtifactsApi.md#listArtifactsInGroup) | **GET** /groups/{groupId}/artifacts | List artifacts in group |
| [**referencesByContentHash**](ArtifactsApi.md#referencesByContentHash) | **GET** /ids/contentHashes/{contentHash}/references | List artifact references by hash |
| [**referencesByContentId**](ArtifactsApi.md#referencesByContentId) | **GET** /ids/contentIds/{contentId}/references | List artifact references by content ID |
| [**referencesByGlobalId**](ArtifactsApi.md#referencesByGlobalId) | **GET** /ids/globalIds/{globalId}/references | List artifact references by global ID |
| [**searchArtifactsByContent_0**](ArtifactsApi.md#searchArtifactsByContent_0) | **POST** /search/artifacts | Search for artifacts by content |
| [**searchArtifacts_0**](ArtifactsApi.md#searchArtifacts_0) | **GET** /search/artifacts | Search for artifacts |
| [**updateArtifact**](ArtifactsApi.md#updateArtifact) | **PUT** /groups/{groupId}/artifacts/{artifactId} | Update artifact |
| [**updateArtifactState**](ArtifactsApi.md#updateArtifactState) | **PUT** /groups/{groupId}/artifacts/{artifactId}/state | Update artifact state |


<a id="createArtifact"></a>
# **createArtifact**
> ArtifactMetaData createArtifact(groupId, body, xRegistryArtifactType, xRegistryArtifactId, xRegistryVersion, ifExists, canonical, xRegistryDescription, xRegistryDescriptionEncoded, xRegistryName, xRegistryNameEncoded, xRegistryContentHash, xRegistryHashAlgorithm)

Create artifact

Creates a new artifact by posting the artifact content.  The body of the request should be the raw content of the artifact.  This is typically in JSON format for *most* of the  supported types, but may be in another format for a few (for example, &#x60;PROTOBUF&#x60;).  The registry attempts to figure out what kind of artifact is being added from the following supported list:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;)  Alternatively, you can specify the artifact type using the &#x60;X-Registry-ArtifactType&#x60;  HTTP request header, or include a hint in the request&#39;s &#x60;Content-Type&#x60;.  For example:  &#x60;&#x60;&#x60; Content-Type: application/json; artifactType&#x3D;AVRO &#x60;&#x60;&#x60;  An artifact is created using the content provided in the body of the request.  This content is created under a unique artifact ID that can be provided in the request using the &#x60;X-Registry-ArtifactId&#x60; request header.  If not provided in the request, the server generates a unique ID for the artifact.  It is typically recommended that callers provide the ID, because this is typically a meaningful identifier,  and for most use cases should be supplied by the caller.  If an artifact with the provided artifact ID already exists, the default behavior is for the server to reject the content with a 409 error.  However, the caller can supply the &#x60;ifExists&#x60; query parameter to alter this default behavior. The &#x60;ifExists&#x60; query parameter can have one of the following values:  * &#x60;FAIL&#x60; (*default*) - server rejects the content with a 409 error * &#x60;UPDATE&#x60; - server updates the existing artifact and returns the new metadata * &#x60;RETURN&#x60; - server does not create or add content to the server, but instead  returns the metadata for the existing artifact * &#x60;RETURN_OR_UPDATE&#x60; - server returns an existing **version** that matches the  provided content if such a version exists, otherwise a new version is created  This operation may fail for one of the following reasons:  * An invalid &#x60;ArtifactType&#x60; was indicated (HTTP error &#x60;400&#x60;) * No &#x60;ArtifactType&#x60; was indicated and the server could not determine one from the content (HTTP error &#x60;400&#x60;) * Provided content (request body) was empty (HTTP error &#x60;400&#x60;) * An artifact with the provided ID already exists (HTTP error &#x60;409&#x60;) * The content violates one of the configured global rules (HTTP error &#x60;409&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    ArtifactsApi apiInstance = new ArtifactsApi(defaultClient);
    String groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    File body = {"components":{"schemas":{"Widget":{"description":"A sample data type.","example":{"property-1":"value1","property-2":true},"properties":{"property-1":{"type":"string"},"property-2":{"type":"boolean"}},"title":"Root Type for Widget","type":"object"}}},"info":{"description":"An example API design using OpenAPI.","title":"Empty API","version":"1.0.7"},"openapi":"3.0.2","paths":{"/widgets":{"get":{"responses":{"200":{"content":{"application/json":{"schema":{"items":{"type":"string"},"type":"array"}}},"description":"All widgets"}},"summary":"Get widgets"}}}}; // File | The content of the artifact being created. This is often, but not always, JSON data representing one of the supported artifact types:  * Avro (`AVRO`) * Protobuf (`PROTOBUF`) * JSON Schema (`JSON`) * Kafka Connect (`KCONNECT`) * OpenAPI (`OPENAPI`) * AsyncAPI (`ASYNCAPI`) * GraphQL (`GRAPHQL`) * Web Services Description Language (`WSDL`) * XML Schema (`XSD`) 
    String xRegistryArtifactType = "xRegistryArtifactType_example"; // String | Specifies the type of the artifact being added. Possible values include:  * Avro (`AVRO`) * Protobuf (`PROTOBUF`) * JSON Schema (`JSON`) * Kafka Connect (`KCONNECT`) * OpenAPI (`OPENAPI`) * AsyncAPI (`ASYNCAPI`) * GraphQL (`GRAPHQL`) * Web Services Description Language (`WSDL`) * XML Schema (`XSD`)
    String xRegistryArtifactId = "xRegistryArtifactId_example"; // String | A client-provided, globally unique identifier for the new artifact.
    String xRegistryVersion = "xRegistryVersion_example"; // String | Specifies the version number of this initial version of the artifact content.  This would typically be a simple integer or a SemVer value.  If not provided, the server will assign a version number automatically (starting with version `1`).
    IfExists ifExists = IfExists.fromValue("FAIL"); // IfExists | Set this option to instruct the server on what to do if the artifact already exists.
    Boolean canonical = true; // Boolean | Used only when the `ifExists` query parameter is set to `RETURN_OR_UPDATE`, this parameter can be set to `true` to indicate that the server should \"canonicalize\" the content when searching for a matching version.  The canonicalization algorithm is unique to each artifact type, but typically involves removing extra whitespace and formatting the content in a consistent manner.
    String xRegistryDescription = "xRegistryDescription_example"; // String | Specifies the description of artifact being added. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content.
    String xRegistryDescriptionEncoded = "xRegistryDescriptionEncoded_example"; // String | Specifies the description of artifact being added. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content.
    String xRegistryName = "xRegistryName_example"; // String | Specifies the name of artifact being added. Name must be ASCII-only string. If this is not provided, the server will extract the name from the artifact content.
    String xRegistryNameEncoded = "xRegistryNameEncoded_example"; // String | Specifies the name of artifact being added. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content.
    String xRegistryContentHash = "xRegistryContentHash_example"; // String | Specifies the (optional) hash of the artifact to be verified.
    String xRegistryHashAlgorithm = "SHA256"; // String | The algorithm to use when checking the content validity. (available: SHA256, MD5; default: SHA256)
    try {
      ArtifactMetaData result = apiInstance.createArtifact(groupId, body, xRegistryArtifactType, xRegistryArtifactId, xRegistryVersion, ifExists, canonical, xRegistryDescription, xRegistryDescriptionEncoded, xRegistryName, xRegistryNameEncoded, xRegistryContentHash, xRegistryHashAlgorithm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactsApi#createArtifact");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **groupId** | **String**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. | |
| **body** | **File**| The content of the artifact being created. This is often, but not always, JSON data representing one of the supported artifact types:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;)  | |
| **xRegistryArtifactType** | **String**| Specifies the type of the artifact being added. Possible values include:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;) | [optional] |
| **xRegistryArtifactId** | **String**| A client-provided, globally unique identifier for the new artifact. | [optional] |
| **xRegistryVersion** | **String**| Specifies the version number of this initial version of the artifact content.  This would typically be a simple integer or a SemVer value.  If not provided, the server will assign a version number automatically (starting with version &#x60;1&#x60;). | [optional] |
| **ifExists** | [**IfExists**](.md)| Set this option to instruct the server on what to do if the artifact already exists. | [optional] [enum: FAIL, UPDATE, RETURN, RETURN_OR_UPDATE] |
| **canonical** | **Boolean**| Used only when the &#x60;ifExists&#x60; query parameter is set to &#x60;RETURN_OR_UPDATE&#x60;, this parameter can be set to &#x60;true&#x60; to indicate that the server should \&quot;canonicalize\&quot; the content when searching for a matching version.  The canonicalization algorithm is unique to each artifact type, but typically involves removing extra whitespace and formatting the content in a consistent manner. | [optional] |
| **xRegistryDescription** | **String**| Specifies the description of artifact being added. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content. | [optional] |
| **xRegistryDescriptionEncoded** | **String**| Specifies the description of artifact being added. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content. | [optional] |
| **xRegistryName** | **String**| Specifies the name of artifact being added. Name must be ASCII-only string. If this is not provided, the server will extract the name from the artifact content. | [optional] |
| **xRegistryNameEncoded** | **String**| Specifies the name of artifact being added. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content. | [optional] |
| **xRegistryContentHash** | **String**| Specifies the (optional) hash of the artifact to be verified. | [optional] |
| **xRegistryHashAlgorithm** | **String**| The algorithm to use when checking the content validity. (available: SHA256, MD5; default: SHA256) | [optional] [enum: SHA256, MD5] |

### Return type

[**ArtifactMetaData**](ArtifactMetaData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/create.extended+json, application/vnd.create.extended+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Artifact was successfully created. |  -  |
| **400** | Common response for all operations that can return a &#x60;400&#x60; error. |  -  |
| **409** | Common response used when an input conflicts with existing data. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

<a id="deleteArtifact"></a>
# **deleteArtifact**
> deleteArtifact(groupId, artifactId)

Delete artifact

Deletes an artifact completely, resulting in all versions of the artifact also being deleted.  This may fail for one of the following reasons:  * No artifact with the &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    ArtifactsApi apiInstance = new ArtifactsApi(defaultClient);
    String groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    String artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    try {
      apiInstance.deleteArtifact(groupId, artifactId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactsApi#deleteArtifact");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **groupId** | **String**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. | |
| **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Returned when the artifact was successfully deleted. |  -  |
| **404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

<a id="deleteArtifactsInGroup"></a>
# **deleteArtifactsInGroup**
> deleteArtifactsInGroup(groupId)

Delete artifacts in group

Deletes all of the artifacts that exist in a given group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    ArtifactsApi apiInstance = new ArtifactsApi(defaultClient);
    String groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    try {
      apiInstance.deleteArtifactsInGroup(groupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactsApi#deleteArtifactsInGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **groupId** | **String**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | When the delete operation is successful, a simple 204 is returned. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

<a id="getContentByGlobalId"></a>
# **getContentByGlobalId**
> File getContentByGlobalId(globalId, dereference)

Get artifact by global ID

Gets the content for an artifact version in the registry using its globally unique identifier.  This operation may fail for one of the following reasons:  * No artifact version with this &#x60;globalId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    ArtifactsApi apiInstance = new ArtifactsApi(defaultClient);
    Long globalId = 56L; // Long | Global identifier for an artifact version.
    Boolean dereference = true; // Boolean | Allows the user to specify if the content should be dereferenced when being returned
    try {
      File result = apiInstance.getContentByGlobalId(globalId, dereference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactsApi#getContentByGlobalId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **globalId** | **Long**| Global identifier for an artifact version. | |
| **dereference** | **Boolean**| Allows the user to specify if the content should be dereferenced when being returned | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The content of one version of one artifact. |  -  |
| **404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

<a id="getContentByHash"></a>
# **getContentByHash**
> File getContentByHash(contentHash)

Get artifact content by SHA-256 hash

Gets the content for an artifact version in the registry using the  SHA-256 hash of the content.  This content hash may be shared by multiple artifact versions in the case where the artifact versions have identical content.  This operation may fail for one of the following reasons:  * No content with this &#x60;contentHash&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    ArtifactsApi apiInstance = new ArtifactsApi(defaultClient);
    String contentHash = "contentHash_example"; // String | SHA-256 content hash for a single artifact content.
    try {
      File result = apiInstance.getContentByHash(contentHash);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactsApi#getContentByHash");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **contentHash** | **String**| SHA-256 content hash for a single artifact content. | |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The content of one version of one artifact. |  -  |
| **404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

<a id="getContentById"></a>
# **getContentById**
> File getContentById(contentId)

Get artifact content by ID

Gets the content for an artifact version in the registry using the unique content identifier for that content.  This content ID may be shared by multiple artifact versions in the case where the artifact versions are identical.  This operation may fail for one of the following reasons:  * No content with this &#x60;contentId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    ArtifactsApi apiInstance = new ArtifactsApi(defaultClient);
    Long contentId = 56L; // Long | Global identifier for a single artifact content.
    try {
      File result = apiInstance.getContentById(contentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactsApi#getContentById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **contentId** | **Long**| Global identifier for a single artifact content. | |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The content of one version of one artifact. |  -  |
| **404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

<a id="getLatestArtifact"></a>
# **getLatestArtifact**
> File getLatestArtifact(groupId, artifactId, dereference)

Get latest artifact

Returns the latest version of the artifact in its raw form.  The &#x60;Content-Type&#x60; of the response depends on the artifact type.  In most cases, this is &#x60;application/json&#x60;, but  for some types it may be different (for example, &#x60;PROTOBUF&#x60;). If the latest version of the artifact is marked as &#x60;DISABLED&#x60;, the next available non-disabled version will be used.  This operation may fail for one of the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists or all versions are &#x60;DISABLED&#x60; (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    ArtifactsApi apiInstance = new ArtifactsApi(defaultClient);
    String groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    String artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    Boolean dereference = true; // Boolean | Allows the user to specify if the content should be dereferenced when being returned
    try {
      File result = apiInstance.getLatestArtifact(groupId, artifactId, dereference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactsApi#getLatestArtifact");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **groupId** | **String**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. | |
| **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. | |
| **dereference** | **Boolean**| Allows the user to specify if the content should be dereferenced when being returned | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The content of one version of one artifact. |  -  |
| **404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

<a id="listArtifactsInGroup"></a>
# **listArtifactsInGroup**
> ArtifactSearchResults listArtifactsInGroup(groupId, limit, offset, order, orderby)

List artifacts in group

Returns a list of all artifacts in the group.  This list is paged.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    ArtifactsApi apiInstance = new ArtifactsApi(defaultClient);
    String groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    Integer limit = 56; // Integer | The number of artifacts to return.  Defaults to 20.
    Integer offset = 56; // Integer | The number of artifacts to skip before starting the result set.  Defaults to 0.
    SortOrder order = SortOrder.fromValue("asc"); // SortOrder | Sort order, ascending (`asc`) or descending (`desc`).
    SortBy orderby = SortBy.fromValue("name"); // SortBy | The field to sort by.  Can be one of:  * `name` * `createdOn` 
    try {
      ArtifactSearchResults result = apiInstance.listArtifactsInGroup(groupId, limit, offset, order, orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactsApi#listArtifactsInGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **groupId** | **String**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. | |
| **limit** | **Integer**| The number of artifacts to return.  Defaults to 20. | [optional] |
| **offset** | **Integer**| The number of artifacts to skip before starting the result set.  Defaults to 0. | [optional] |
| **order** | [**SortOrder**](.md)| Sort order, ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;). | [optional] [enum: asc, desc] |
| **orderby** | [**SortBy**](.md)| The field to sort by.  Can be one of:  * &#x60;name&#x60; * &#x60;createdOn&#x60;  | [optional] [enum: name, createdOn] |

### Return type

[**ArtifactSearchResults**](ArtifactSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | On a successful response, returns a bounded set of artifacts. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

<a id="referencesByContentHash"></a>
# **referencesByContentHash**
> List&lt;ArtifactReference&gt; referencesByContentHash(contentHash)

List artifact references by hash

Returns a list containing all the artifact references using the artifact content hash.  This operation may fail for one of the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    ArtifactsApi apiInstance = new ArtifactsApi(defaultClient);
    String contentHash = "contentHash_example"; // String | SHA-256 content hash for a single artifact content.
    try {
      List<ArtifactReference> result = apiInstance.referencesByContentHash(contentHash);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactsApi#referencesByContentHash");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **contentHash** | **String**| SHA-256 content hash for a single artifact content. | |

### Return type

[**List&lt;ArtifactReference&gt;**](ArtifactReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list containing all the references for the artifact with the given content hash. |  -  |

<a id="referencesByContentId"></a>
# **referencesByContentId**
> List&lt;ArtifactReference&gt; referencesByContentId(contentId)

List artifact references by content ID

Returns a list containing all the artifact references using the artifact content ID.  This operation may fail for one of the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    ArtifactsApi apiInstance = new ArtifactsApi(defaultClient);
    Long contentId = 56L; // Long | Global identifier for a single artifact content.
    try {
      List<ArtifactReference> result = apiInstance.referencesByContentId(contentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactsApi#referencesByContentId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **contentId** | **Long**| Global identifier for a single artifact content. | |

### Return type

[**List&lt;ArtifactReference&gt;**](ArtifactReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list containing all the references for the artifact with the given content id. |  -  |

<a id="referencesByGlobalId"></a>
# **referencesByGlobalId**
> List&lt;ArtifactReference&gt; referencesByGlobalId(globalId)

List artifact references by global ID

Returns a list containing all the artifact references using the artifact global ID.  This operation may fail for one of the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    ArtifactsApi apiInstance = new ArtifactsApi(defaultClient);
    Long globalId = 56L; // Long | Global identifier for an artifact version.
    try {
      List<ArtifactReference> result = apiInstance.referencesByGlobalId(globalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactsApi#referencesByGlobalId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **globalId** | **Long**| Global identifier for an artifact version. | |

### Return type

[**List&lt;ArtifactReference&gt;**](ArtifactReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list containing all the references for the artifact with the given global id. |  -  |

<a id="searchArtifactsByContent_0"></a>
# **searchArtifactsByContent_0**
> ArtifactSearchResults searchArtifactsByContent_0(body, canonical, artifactType, offset, limit, order, orderby)

Search for artifacts by content

Returns a paginated list of all artifacts with at least one version that matches the posted content. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    ArtifactsApi apiInstance = new ArtifactsApi(defaultClient);
    File body = new File("/path/to/file"); // File | The content to search for.
    Boolean canonical = true; // Boolean | Parameter that can be set to `true` to indicate that the server should \"canonicalize\" the content when searching for matching artifacts.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner.  Must be used along with the `artifactType` query parameter.
    String artifactType = "artifactType_example"; // String | Indicates the type of artifact represented by the content being used for the search.  This is only needed when using the `canonical` query parameter, so that the server knows how to canonicalize the content prior to searching for matching artifacts.
    Integer offset = 0; // Integer | The number of artifacts to skip before starting to collect the result set.  Defaults to 0.
    Integer limit = 20; // Integer | The number of artifacts to return.  Defaults to 20.
    String order = "asc"; // String | Sort order, ascending (`asc`) or descending (`desc`).
    String orderby = "name"; // String | The field to sort by.  Can be one of:  * `name` * `createdOn` 
    try {
      ArtifactSearchResults result = apiInstance.searchArtifactsByContent_0(body, canonical, artifactType, offset, limit, order, orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactsApi#searchArtifactsByContent_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **File**| The content to search for. | |
| **canonical** | **Boolean**| Parameter that can be set to &#x60;true&#x60; to indicate that the server should \&quot;canonicalize\&quot; the content when searching for matching artifacts.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner.  Must be used along with the &#x60;artifactType&#x60; query parameter. | [optional] |
| **artifactType** | **String**| Indicates the type of artifact represented by the content being used for the search.  This is only needed when using the &#x60;canonical&#x60; query parameter, so that the server knows how to canonicalize the content prior to searching for matching artifacts. | [optional] |
| **offset** | **Integer**| The number of artifacts to skip before starting to collect the result set.  Defaults to 0. | [optional] [default to 0] |
| **limit** | **Integer**| The number of artifacts to return.  Defaults to 20. | [optional] [default to 20] |
| **order** | **String**| Sort order, ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;). | [optional] [enum: asc, desc] |
| **orderby** | **String**| The field to sort by.  Can be one of:  * &#x60;name&#x60; * &#x60;createdOn&#x60;  | [optional] [enum: name, createdOn] |

### Return type

[**ArtifactSearchResults**](ArtifactSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | On a successful response, returns a result set of artifacts - one for each artifact in the registry that matches the criteria. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

<a id="searchArtifacts_0"></a>
# **searchArtifacts_0**
> ArtifactSearchResults searchArtifacts_0(name, offset, limit, order, orderby, labels, properties, description, group, globalId, contentId)

Search for artifacts

Returns a paginated list of all artifacts that match the provided filter criteria. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    ArtifactsApi apiInstance = new ArtifactsApi(defaultClient);
    String name = "name_example"; // String | Filter by artifact name.
    Integer offset = 0; // Integer | The number of artifacts to skip before starting to collect the result set.  Defaults to 0.
    Integer limit = 20; // Integer | The number of artifacts to return.  Defaults to 20.
    SortOrder order = SortOrder.fromValue("asc"); // SortOrder | Sort order, ascending (`asc`) or descending (`desc`).
    SortBy orderby = SortBy.fromValue("name"); // SortBy | The field to sort by.  Can be one of:  * `name` * `createdOn` 
    List<String> labels = Arrays.asList(); // List<String> | Filter by label.  Include one or more label to only return artifacts containing all of the specified labels.
    List<String> properties = Arrays.asList(); // List<String> | Filter by one or more name/value property.  Separate each name/value pair using a colon.  For example `properties=foo:bar` will return only artifacts with a custom property named `foo` and value `bar`.
    String description = "description_example"; // String | Filter by description.
    String group = "group_example"; // String | Filter by artifact group.
    Long globalId = 56L; // Long | Filter by globalId.
    Long contentId = 56L; // Long | Filter by contentId.
    try {
      ArtifactSearchResults result = apiInstance.searchArtifacts_0(name, offset, limit, order, orderby, labels, properties, description, group, globalId, contentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactsApi#searchArtifacts_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| Filter by artifact name. | [optional] |
| **offset** | **Integer**| The number of artifacts to skip before starting to collect the result set.  Defaults to 0. | [optional] [default to 0] |
| **limit** | **Integer**| The number of artifacts to return.  Defaults to 20. | [optional] [default to 20] |
| **order** | [**SortOrder**](.md)| Sort order, ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;). | [optional] [enum: asc, desc] |
| **orderby** | [**SortBy**](.md)| The field to sort by.  Can be one of:  * &#x60;name&#x60; * &#x60;createdOn&#x60;  | [optional] [enum: name, createdOn] |
| **labels** | [**List&lt;String&gt;**](String.md)| Filter by label.  Include one or more label to only return artifacts containing all of the specified labels. | [optional] |
| **properties** | [**List&lt;String&gt;**](String.md)| Filter by one or more name/value property.  Separate each name/value pair using a colon.  For example &#x60;properties&#x3D;foo:bar&#x60; will return only artifacts with a custom property named &#x60;foo&#x60; and value &#x60;bar&#x60;. | [optional] |
| **description** | **String**| Filter by description. | [optional] |
| **group** | **String**| Filter by artifact group. | [optional] |
| **globalId** | **Long**| Filter by globalId. | [optional] |
| **contentId** | **Long**| Filter by contentId. | [optional] |

### Return type

[**ArtifactSearchResults**](ArtifactSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | On a successful response, returns a result set of artifacts - one for each artifact in the registry that matches the criteria. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

<a id="updateArtifact"></a>
# **updateArtifact**
> ArtifactMetaData updateArtifact(groupId, artifactId, body, xRegistryVersion, xRegistryName, xRegistryNameEncoded, xRegistryDescription, xRegistryDescriptionEncoded)

Update artifact

Updates an artifact by uploading new content.  The body of the request can be the raw content of the artifact or a JSON object containing both the raw content and a set of references to other artifacts..  This is typically in JSON format for *most* of the supported types, but may be in another format for a few (for example, &#x60;PROTOBUF&#x60;). The type of the content should be compatible with the artifact&#39;s type (it would be an error to update an &#x60;AVRO&#x60; artifact with new &#x60;OPENAPI&#x60; content, for example).  The update could fail for a number of reasons including:  * Provided content (request body) was empty (HTTP error &#x60;400&#x60;) * No artifact with the &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * The new content violates one of the rules configured for the artifact (HTTP error &#x60;409&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)  When successful, this creates a new version of the artifact, making it the most recent (and therefore official) version of the artifact.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    ArtifactsApi apiInstance = new ArtifactsApi(defaultClient);
    String groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    String artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    File body = {"components":{"schemas":{"Widget":{"description":"A sample data type.","example":{"property-1":"value1","property-2":true},"properties":{"property-1":{"type":"string"},"property-2":{"type":"boolean"}},"title":"Root Type for Widget","type":"object"}}},"info":{"description":"An example API design using OpenAPI.","title":"Empty API","version":"1.0.7"},"openapi":"3.0.2","paths":{"/widgets":{"get":{"responses":{"200":{"content":{"application/json":{"schema":{"items":{"type":"string"},"type":"array"}}},"description":"All widgets"}},"summary":"Get widgets"}}}}; // File | The new content of the artifact being updated. This is often, but not always, JSON data representing one of the supported artifact types:  * Avro (`AVRO`) * Protobuf (`PROTOBUF`) * JSON Schema (`JSON`) * Kafka Connect (`KCONNECT`) * OpenAPI (`OPENAPI`) * AsyncAPI (`ASYNCAPI`) * GraphQL (`GRAPHQL`) * Web Services Description Language (`WSDL`) * XML Schema (`XSD`) 
    String xRegistryVersion = "xRegistryVersion_example"; // String | Specifies the version number of this new version of the artifact content.  This would typically be a simple integer or a SemVer value.  If not provided, the server will assign a version number automatically.
    String xRegistryName = "xRegistryName_example"; // String | Specifies the artifact name of this new version of the artifact content. Name must be ASCII-only string. If this is not provided, the server will extract the name from the artifact content.
    String xRegistryNameEncoded = "xRegistryNameEncoded_example"; // String | Specifies the artifact name of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content.
    String xRegistryDescription = "xRegistryDescription_example"; // String | Specifies the artifact description of this new version of the artifact content. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content.
    String xRegistryDescriptionEncoded = "xRegistryDescriptionEncoded_example"; // String | Specifies the artifact description of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content.
    try {
      ArtifactMetaData result = apiInstance.updateArtifact(groupId, artifactId, body, xRegistryVersion, xRegistryName, xRegistryNameEncoded, xRegistryDescription, xRegistryDescriptionEncoded);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactsApi#updateArtifact");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **groupId** | **String**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. | |
| **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. | |
| **body** | **File**| The new content of the artifact being updated. This is often, but not always, JSON data representing one of the supported artifact types:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;)  | |
| **xRegistryVersion** | **String**| Specifies the version number of this new version of the artifact content.  This would typically be a simple integer or a SemVer value.  If not provided, the server will assign a version number automatically. | [optional] |
| **xRegistryName** | **String**| Specifies the artifact name of this new version of the artifact content. Name must be ASCII-only string. If this is not provided, the server will extract the name from the artifact content. | [optional] |
| **xRegistryNameEncoded** | **String**| Specifies the artifact name of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content. | [optional] |
| **xRegistryDescription** | **String**| Specifies the artifact description of this new version of the artifact content. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content. | [optional] |
| **xRegistryDescriptionEncoded** | **String**| Specifies the artifact description of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content. | [optional] |

### Return type

[**ArtifactMetaData**](ArtifactMetaData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/create.extended+json, application/vnd.create.extended+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | When successful, returns the updated artifact metadata. |  -  |
| **404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
| **409** | Common response used when an input conflicts with existing data. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

<a id="updateArtifactState"></a>
# **updateArtifactState**
> updateArtifactState(groupId, artifactId, updateState)

Update artifact state

Updates the state of the artifact.  For example, you can use this to mark the latest version of an artifact as &#x60;DEPRECATED&#x60;. The operation changes the state of the latest version of the artifact, even if this version is &#x60;DISABLED&#x60;. If multiple versions exist, only the most recent is changed.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    ArtifactsApi apiInstance = new ArtifactsApi(defaultClient);
    String groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    String artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    UpdateState updateState = new UpdateState(); // UpdateState | 
    try {
      apiInstance.updateArtifactState(groupId, artifactId, updateState);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactsApi#updateArtifactState");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **groupId** | **String**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. | |
| **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. | |
| **updateState** | [**UpdateState**](UpdateState.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Returned when the operation was successful. |  -  |
| **400** | Common response for all operations that can return a &#x60;400&#x60; error. |  -  |
| **404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

