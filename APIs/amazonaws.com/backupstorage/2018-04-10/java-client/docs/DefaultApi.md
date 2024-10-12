# DefaultApi

All URIs are relative to *http://backupstorage.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteObject**](DefaultApi.md#deleteObject) | **DELETE** /backup-jobs/{jobId}/object/{objectName} |  |
| [**getChunk**](DefaultApi.md#getChunk) | **GET** /restore-jobs/{jobId}/chunk/{chunkToken} |  |
| [**getObjectMetadata**](DefaultApi.md#getObjectMetadata) | **GET** /restore-jobs/{jobId}/object/{objectToken}/metadata |  |
| [**listChunks**](DefaultApi.md#listChunks) | **GET** /restore-jobs/{jobId}/chunks/{objectToken}/list |  |
| [**listObjects**](DefaultApi.md#listObjects) | **GET** /restore-jobs/{jobId}/objects/list |  |
| [**notifyObjectComplete**](DefaultApi.md#notifyObjectComplete) | **PUT** /backup-jobs/{jobId}/object/{uploadId}/complete#checksum&amp;checksum-algorithm |  |
| [**putChunk**](DefaultApi.md#putChunk) | **PUT** /backup-jobs/{jobId}/chunk/{uploadId}/{chunkIndex}#length&amp;checksum&amp;checksum-algorithm |  |
| [**putObject**](DefaultApi.md#putObject) | **PUT** /backup-jobs/{jobId}/object/{objectName}/put-object |  |
| [**startObject**](DefaultApi.md#startObject) | **PUT** /backup-jobs/{jobId}/object/{objectName} |  |


<a id="deleteObject"></a>
# **deleteObject**
> deleteObject(jobId, objectName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Delete Object from the incremental base Backup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backupstorage.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String jobId = "jobId_example"; // String | Backup job Id for the in-progress backup.
    String objectName = "objectName_example"; // String | The name of the Object.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteObject(jobId, objectName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteObject");
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
| **jobId** | **String**| Backup job Id for the in-progress backup. | |
| **objectName** | **String**| The name of the Object. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ServiceUnavailableException |  -  |
| **481** | ServiceInternalException |  -  |
| **482** | RetryableException |  -  |
| **483** | IllegalArgumentException |  -  |
| **484** | ResourceNotFoundException |  -  |
| **485** | ThrottlingException |  -  |
| **486** | AccessDeniedException |  -  |

<a id="getChunk"></a>
# **getChunk**
> GetChunkOutput getChunk(jobId, chunkToken, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets the specified object&#39;s chunk.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backupstorage.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String jobId = "jobId_example"; // String | Storage job id
    String chunkToken = "chunkToken_example"; // String | Chunk token
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetChunkOutput result = apiInstance.getChunk(jobId, chunkToken, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getChunk");
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
| **jobId** | **String**| Storage job id | |
| **chunkToken** | **String**| Chunk token | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetChunkOutput**](GetChunkOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | IllegalArgumentException |  -  |
| **481** | RetryableException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ServiceInternalException |  -  |
| **484** | ThrottlingException |  -  |
| **485** | KMSInvalidKeyUsageException |  -  |
| **486** | AccessDeniedException |  -  |

<a id="getObjectMetadata"></a>
# **getObjectMetadata**
> GetObjectMetadataOutput getObjectMetadata(jobId, objectToken, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Get metadata associated with an Object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backupstorage.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String jobId = "jobId_example"; // String | Backup job id for the in-progress backup.
    String objectToken = "objectToken_example"; // String | Object token.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetObjectMetadataOutput result = apiInstance.getObjectMetadata(jobId, objectToken, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getObjectMetadata");
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
| **jobId** | **String**| Backup job id for the in-progress backup. | |
| **objectToken** | **String**| Object token. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetObjectMetadataOutput**](GetObjectMetadataOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ServiceUnavailableException |  -  |
| **481** | ServiceInternalException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | RetryableException |  -  |
| **484** | IllegalArgumentException |  -  |
| **485** | ThrottlingException |  -  |
| **486** | KMSInvalidKeyUsageException |  -  |
| **487** | AccessDeniedException |  -  |

<a id="listChunks"></a>
# **listChunks**
> ListChunksOutput listChunks(jobId, objectToken, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2)



List chunks in a given Object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backupstorage.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String jobId = "jobId_example"; // String | Storage job id
    String objectToken = "objectToken_example"; // String | Object token
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer maxResults = 56; // Integer | Maximum number of chunks
    String nextToken = "nextToken_example"; // String | Pagination token
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListChunksOutput result = apiInstance.listChunks(jobId, objectToken, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listChunks");
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
| **jobId** | **String**| Storage job id | |
| **objectToken** | **String**| Object token | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **Integer**| Maximum number of chunks | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListChunksOutput**](ListChunksOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ServiceUnavailableException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | ServiceInternalException |  -  |
| **483** | RetryableException |  -  |
| **484** | IllegalArgumentException |  -  |
| **485** | AccessDeniedException |  -  |

<a id="listObjects"></a>
# **listObjects**
> ListObjectsOutput listObjects(jobId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, startingObjectName, startingObjectPrefix, maxResults, nextToken, createdBefore, createdAfter, maxResults2, nextToken2)



List all Objects in a given Backup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backupstorage.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String jobId = "jobId_example"; // String | Storage job id
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String startingObjectName = "startingObjectName_example"; // String | Optional, specifies the starting Object name to list from. Ignored if NextToken is not NULL
    String startingObjectPrefix = "startingObjectPrefix_example"; // String | Optional, specifies the starting Object prefix to list from. Ignored if NextToken is not NULL
    Integer maxResults = 56; // Integer | Maximum objects count
    String nextToken = "nextToken_example"; // String | Pagination token
    OffsetDateTime createdBefore = OffsetDateTime.now(); // OffsetDateTime | (Optional) Created before filter
    OffsetDateTime createdAfter = OffsetDateTime.now(); // OffsetDateTime | (Optional) Created after filter
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListObjectsOutput result = apiInstance.listObjects(jobId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, startingObjectName, startingObjectPrefix, maxResults, nextToken, createdBefore, createdAfter, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listObjects");
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
| **jobId** | **String**| Storage job id | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **startingObjectName** | **String**| Optional, specifies the starting Object name to list from. Ignored if NextToken is not NULL | [optional] |
| **startingObjectPrefix** | **String**| Optional, specifies the starting Object prefix to list from. Ignored if NextToken is not NULL | [optional] |
| **maxResults** | **Integer**| Maximum objects count | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |
| **createdBefore** | **OffsetDateTime**| (Optional) Created before filter | [optional] |
| **createdAfter** | **OffsetDateTime**| (Optional) Created after filter | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListObjectsOutput**](ListObjectsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ServiceUnavailableException |  -  |
| **481** | ServiceInternalException |  -  |
| **482** | RetryableException |  -  |
| **483** | IllegalArgumentException |  -  |
| **484** | ThrottlingException |  -  |
| **485** | ResourceNotFoundException |  -  |
| **486** | KMSInvalidKeyUsageException |  -  |
| **487** | AccessDeniedException |  -  |

<a id="notifyObjectComplete"></a>
# **notifyObjectComplete**
> NotifyObjectCompleteOutput notifyObjectComplete(jobId, uploadId, checksum, checksumAlgorithm, notifyObjectCompleteRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, metadataString, metadataBlobLength, metadataChecksum, metadataChecksumAlgorithm)



Complete upload

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backupstorage.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String jobId = "jobId_example"; // String | Backup job Id for the in-progress backup
    String uploadId = "uploadId_example"; // String | Upload Id for the in-progress upload
    String checksum = "checksum_example"; // String | Object checksum
    String checksumAlgorithm = "SUMMARY"; // String | Checksum algorithm
    NotifyObjectCompleteRequest notifyObjectCompleteRequest = new NotifyObjectCompleteRequest(); // NotifyObjectCompleteRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String metadataString = "metadataString_example"; // String | Optional metadata associated with an Object. Maximum string length is 256 bytes.
    Integer metadataBlobLength = 56; // Integer | The size of MetadataBlob.
    String metadataChecksum = "metadataChecksum_example"; // String | Checksum of MetadataBlob.
    String metadataChecksumAlgorithm = "SHA256"; // String | Checksum algorithm.
    try {
      NotifyObjectCompleteOutput result = apiInstance.notifyObjectComplete(jobId, uploadId, checksum, checksumAlgorithm, notifyObjectCompleteRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, metadataString, metadataBlobLength, metadataChecksum, metadataChecksumAlgorithm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#notifyObjectComplete");
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
| **jobId** | **String**| Backup job Id for the in-progress backup | |
| **uploadId** | **String**| Upload Id for the in-progress upload | |
| **checksum** | **String**| Object checksum | |
| **checksumAlgorithm** | **String**| Checksum algorithm | [enum: SUMMARY] |
| **notifyObjectCompleteRequest** | [**NotifyObjectCompleteRequest**](NotifyObjectCompleteRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **metadataString** | **String**| Optional metadata associated with an Object. Maximum string length is 256 bytes. | [optional] |
| **metadataBlobLength** | **Integer**| The size of MetadataBlob. | [optional] |
| **metadataChecksum** | **String**| Checksum of MetadataBlob. | [optional] |
| **metadataChecksumAlgorithm** | **String**| Checksum algorithm. | [optional] [enum: SHA256] |

### Return type

[**NotifyObjectCompleteOutput**](NotifyObjectCompleteOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ServiceUnavailableException |  -  |
| **481** | ServiceInternalException |  -  |
| **482** | NotReadableInputStreamException |  -  |
| **483** | RetryableException |  -  |
| **484** | IllegalArgumentException |  -  |
| **485** | ThrottlingException |  -  |
| **486** | KMSInvalidKeyUsageException |  -  |
| **487** | AccessDeniedException |  -  |

<a id="putChunk"></a>
# **putChunk**
> PutChunkOutput putChunk(jobId, uploadId, chunkIndex, length, checksum, checksumAlgorithm, putChunkRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Upload chunk.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backupstorage.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String jobId = "jobId_example"; // String | Backup job Id for the in-progress backup.
    String uploadId = "uploadId_example"; // String | Upload Id for the in-progress upload.
    Integer chunkIndex = 56; // Integer | Describes this chunk's position relative to the other chunks
    Integer length = 56; // Integer | Data length
    String checksum = "checksum_example"; // String | Data checksum
    String checksumAlgorithm = "SHA256"; // String | Checksum algorithm
    PutChunkRequest putChunkRequest = new PutChunkRequest(); // PutChunkRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutChunkOutput result = apiInstance.putChunk(jobId, uploadId, chunkIndex, length, checksum, checksumAlgorithm, putChunkRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putChunk");
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
| **jobId** | **String**| Backup job Id for the in-progress backup. | |
| **uploadId** | **String**| Upload Id for the in-progress upload. | |
| **chunkIndex** | **Integer**| Describes this chunk&#39;s position relative to the other chunks | |
| **length** | **Integer**| Data length | |
| **checksum** | **String**| Data checksum | |
| **checksumAlgorithm** | **String**| Checksum algorithm | [enum: SHA256] |
| **putChunkRequest** | [**PutChunkRequest**](PutChunkRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutChunkOutput**](PutChunkOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ServiceUnavailableException |  -  |
| **481** | ServiceInternalException |  -  |
| **482** | NotReadableInputStreamException |  -  |
| **483** | RetryableException |  -  |
| **484** | IllegalArgumentException |  -  |
| **485** | ThrottlingException |  -  |
| **486** | KMSInvalidKeyUsageException |  -  |
| **487** | AccessDeniedException |  -  |

<a id="putObject"></a>
# **putObject**
> PutObjectOutput putObject(jobId, objectName, putObjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, metadataString, length, checksum, checksumAlgorithm, objectChecksum, objectChecksumAlgorithm, throwOnDuplicate)



Upload object that can store object metadata String and data blob in single API call using inline chunk field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backupstorage.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String jobId = "jobId_example"; // String | Backup job Id for the in-progress backup.
    String objectName = "objectName_example"; // String | The name of the Object to be uploaded.
    PutObjectRequest putObjectRequest = new PutObjectRequest(); // PutObjectRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String metadataString = "metadataString_example"; // String | Store user defined metadata like backup checksum, disk ids, restore metadata etc.
    Integer length = 56; // Integer | Length of the inline chunk data.
    String checksum = "checksum_example"; // String | Inline chunk checksum
    String checksumAlgorithm = "checksumAlgorithm_example"; // String | Inline chunk checksum algorithm
    String objectChecksum = "objectChecksum_example"; // String | object checksum
    String objectChecksumAlgorithm = "SUMMARY"; // String | object checksum algorithm
    Boolean throwOnDuplicate = true; // Boolean | Throw an exception if Object name is already exist.
    try {
      PutObjectOutput result = apiInstance.putObject(jobId, objectName, putObjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, metadataString, length, checksum, checksumAlgorithm, objectChecksum, objectChecksumAlgorithm, throwOnDuplicate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putObject");
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
| **jobId** | **String**| Backup job Id for the in-progress backup. | |
| **objectName** | **String**| The name of the Object to be uploaded. | |
| **putObjectRequest** | [**PutObjectRequest**](PutObjectRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **metadataString** | **String**| Store user defined metadata like backup checksum, disk ids, restore metadata etc. | [optional] |
| **length** | **Integer**| Length of the inline chunk data. | [optional] |
| **checksum** | **String**| Inline chunk checksum | [optional] |
| **checksumAlgorithm** | **String**| Inline chunk checksum algorithm | [optional] |
| **objectChecksum** | **String**| object checksum | [optional] |
| **objectChecksumAlgorithm** | **String**| object checksum algorithm | [optional] [enum: SUMMARY] |
| **throwOnDuplicate** | **Boolean**| Throw an exception if Object name is already exist. | [optional] |

### Return type

[**PutObjectOutput**](PutObjectOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ServiceUnavailableException |  -  |
| **481** | ServiceInternalException |  -  |
| **482** | NotReadableInputStreamException |  -  |
| **483** | RetryableException |  -  |
| **484** | IllegalArgumentException |  -  |
| **485** | ThrottlingException |  -  |
| **486** | KMSInvalidKeyUsageException |  -  |
| **487** | AccessDeniedException |  -  |

<a id="startObject"></a>
# **startObject**
> StartObjectOutput startObject(jobId, objectName, startObjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Start upload containing one or many chunks.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backupstorage.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String jobId = "jobId_example"; // String | Backup job Id for the in-progress backup
    String objectName = "objectName_example"; // String | Name for the object.
    StartObjectRequest startObjectRequest = new StartObjectRequest(); // StartObjectRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartObjectOutput result = apiInstance.startObject(jobId, objectName, startObjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startObject");
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
| **jobId** | **String**| Backup job Id for the in-progress backup | |
| **objectName** | **String**| Name for the object. | |
| **startObjectRequest** | [**StartObjectRequest**](StartObjectRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartObjectOutput**](StartObjectOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ServiceUnavailableException |  -  |
| **481** | ServiceInternalException |  -  |
| **482** | RetryableException |  -  |
| **483** | IllegalArgumentException |  -  |
| **484** | ResourceNotFoundException |  -  |
| **485** | DataAlreadyExistsException |  -  |
| **486** | ThrottlingException |  -  |
| **487** | AccessDeniedException |  -  |

