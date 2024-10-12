# MetadataApi

All URIs are relative to *http://apicurio.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteArtifactVersionMetaData**](MetadataApi.md#deleteArtifactVersionMetaData) | **DELETE** /artifacts/{artifactId}/versions/{version}/meta | Delete artifact version metadata |
| [**getArtifactMetaData**](MetadataApi.md#getArtifactMetaData) | **GET** /artifacts/{artifactId}/meta | Get artifact metadata |
| [**getArtifactMetaDataByContent**](MetadataApi.md#getArtifactMetaDataByContent) | **POST** /artifacts/{artifactId}/meta | Get artifact metadata by content |
| [**getArtifactMetaDataByGlobalId**](MetadataApi.md#getArtifactMetaDataByGlobalId) | **GET** /ids/{globalId}/meta | Get global artifact metadata |
| [**getArtifactVersionMetaData**](MetadataApi.md#getArtifactVersionMetaData) | **GET** /artifacts/{artifactId}/versions/{version}/meta | Get artifact version metadata |
| [**updateArtifactMetaData**](MetadataApi.md#updateArtifactMetaData) | **PUT** /artifacts/{artifactId}/meta | Update artifact metadata |
| [**updateArtifactVersionMetaData**](MetadataApi.md#updateArtifactVersionMetaData) | **PUT** /artifacts/{artifactId}/versions/{version}/meta | Update artifact version metadata |


<a id="deleteArtifactVersionMetaData"></a>
# **deleteArtifactVersionMetaData**
> deleteArtifactVersionMetaData(version, artifactId)

Delete artifact version metadata

Deletes the user-editable metadata properties of the artifact version.  Any properties that are not user-editable are preserved.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No version with this &#x60;version&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    Integer version = 56; // Integer | The unique identifier of a specific version of the artifact content.
    String artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
    try {
      apiInstance.deleteArtifactVersionMetaData(version, artifactId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#deleteArtifactVersionMetaData");
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
| **version** | **Integer**| The unique identifier of a specific version of the artifact content. | |
| **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | |

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
| **204** | The artifact version&#39;s user-editable metadata was successfully deleted. |  -  |
| **404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

<a id="getArtifactMetaData"></a>
# **getArtifactMetaData**
> ArtifactMetaData getArtifactMetaData(artifactId)

Get artifact metadata

Gets the metadata for an artifact in the registry, based on the latest version. If the latest version of the artifact is marked as &#x60;DISABLED&#x60;, the next available non-disabled version will be used. The returned metadata includes both generated (read-only) and editable metadata (such as name and description).  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists or all versions are &#x60;DISABLED&#x60; (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
    try {
      ArtifactMetaData result = apiInstance.getArtifactMetaData(artifactId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#getArtifactMetaData");
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
| **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | |

### Return type

[**ArtifactMetaData**](ArtifactMetaData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The artifact&#39;s metadata. |  -  |
| **404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

<a id="getArtifactMetaDataByContent"></a>
# **getArtifactMetaDataByContent**
> ArtifactMetaData getArtifactMetaDataByContent(artifactId)

Get artifact metadata by content

Gets the metadata for an artifact that matches the raw content.  Searches the registry for a version of the given artifact matching the content provided in the body of the POST.  This operation can fail for the following reasons:  * Provided content (request body) was empty (HTTP error &#x60;400&#x60;) * No artifact with the &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No artifact version matching the provided content exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
    try {
      ArtifactMetaData result = apiInstance.getArtifactMetaDataByContent(artifactId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#getArtifactMetaDataByContent");
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
| **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | |

### Return type

[**ArtifactMetaData**](ArtifactMetaData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The metadata of the artifact version matching the provided content. |  -  |
| **404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

<a id="getArtifactMetaDataByGlobalId"></a>
# **getArtifactMetaDataByGlobalId**
> ArtifactMetaData getArtifactMetaDataByGlobalId(globalId)

Get global artifact metadata

Gets the metadata for an artifact version in the registry using its globally unique identifier.  The returned metadata includes both generated (read-only) and editable metadata (such as name and description).  This operation may fail for one of the following reasons:  * No artifact version with this &#x60;globalId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    Long globalId = 56L; // Long | Global identifier for an artifact version.
    try {
      ArtifactMetaData result = apiInstance.getArtifactMetaDataByGlobalId(globalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#getArtifactMetaDataByGlobalId");
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

[**ArtifactMetaData**](ArtifactMetaData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The artifact&#39;s metadata. |  -  |
| **404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

<a id="getArtifactVersionMetaData"></a>
# **getArtifactVersionMetaData**
> VersionMetaData getArtifactVersionMetaData(version, artifactId)

Get artifact version metadata

Retrieves the metadata for a single version of the artifact.  The version metadata is  a subset of the artifact metadata and only includes the metadata that is specific to the version (for example, this doesn&#39;t include &#x60;modifiedOn&#x60;).  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No version with this &#x60;version&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    Integer version = 56; // Integer | The unique identifier of a specific version of the artifact content.
    String artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
    try {
      VersionMetaData result = apiInstance.getArtifactVersionMetaData(version, artifactId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#getArtifactVersionMetaData");
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
| **version** | **Integer**| The unique identifier of a specific version of the artifact content. | |
| **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | |

### Return type

[**VersionMetaData**](VersionMetaData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The artifact version&#39;s metadata. |  -  |
| **404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

<a id="updateArtifactMetaData"></a>
# **updateArtifactMetaData**
> updateArtifactMetaData(artifactId, editableMetaData)

Update artifact metadata

Updates the editable parts of the artifact&#39;s metadata.  Not all metadata fields can be updated.  For example, &#x60;createdOn&#x60; and &#x60;createdBy&#x60; are both read-only properties.  This operation can fail for the following reasons:  * No artifact with the &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
    EditableMetaData editableMetaData = new EditableMetaData(); // EditableMetaData | Updated artifact metadata.
    try {
      apiInstance.updateArtifactMetaData(artifactId, editableMetaData);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#updateArtifactMetaData");
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
| **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | |
| **editableMetaData** | [**EditableMetaData**](EditableMetaData.md)| Updated artifact metadata. | |

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
| **204** | The artifact&#39;s metadata was updated. |  -  |
| **404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

<a id="updateArtifactVersionMetaData"></a>
# **updateArtifactVersionMetaData**
> updateArtifactVersionMetaData(version, artifactId, editableMetaData)

Update artifact version metadata

Updates the user-editable portion of the artifact version&#39;s metadata.  Only some of  the metadata fields are editable by the user.  For example, &#x60;description&#x60; is editable,  but &#x60;createdOn&#x60; is not.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No version with this &#x60;version&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    Integer version = 56; // Integer | The unique identifier of a specific version of the artifact content.
    String artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
    EditableMetaData editableMetaData = new EditableMetaData(); // EditableMetaData | 
    try {
      apiInstance.updateArtifactVersionMetaData(version, artifactId, editableMetaData);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#updateArtifactVersionMetaData");
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
| **version** | **Integer**| The unique identifier of a specific version of the artifact content. | |
| **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | |
| **editableMetaData** | [**EditableMetaData**](EditableMetaData.md)|  | |

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
| **204** | The artifact version&#39;s metadata was successfully updated. |  -  |
| **404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

