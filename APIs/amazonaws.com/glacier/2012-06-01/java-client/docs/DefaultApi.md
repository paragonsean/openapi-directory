# DefaultApi

All URIs are relative to *http://glacier.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**abortMultipartUpload**](DefaultApi.md#abortMultipartUpload) | **DELETE** /{accountId}/vaults/{vaultName}/multipart-uploads/{uploadId} |  |
| [**abortVaultLock**](DefaultApi.md#abortVaultLock) | **DELETE** /{accountId}/vaults/{vaultName}/lock-policy |  |
| [**addTagsToVault**](DefaultApi.md#addTagsToVault) | **POST** /{accountId}/vaults/{vaultName}/tags#operation&#x3D;add |  |
| [**completeMultipartUpload**](DefaultApi.md#completeMultipartUpload) | **POST** /{accountId}/vaults/{vaultName}/multipart-uploads/{uploadId} |  |
| [**completeVaultLock**](DefaultApi.md#completeVaultLock) | **POST** /{accountId}/vaults/{vaultName}/lock-policy/{lockId} |  |
| [**createVault**](DefaultApi.md#createVault) | **PUT** /{accountId}/vaults/{vaultName} |  |
| [**deleteArchive**](DefaultApi.md#deleteArchive) | **DELETE** /{accountId}/vaults/{vaultName}/archives/{archiveId} |  |
| [**deleteVault**](DefaultApi.md#deleteVault) | **DELETE** /{accountId}/vaults/{vaultName} |  |
| [**deleteVaultAccessPolicy**](DefaultApi.md#deleteVaultAccessPolicy) | **DELETE** /{accountId}/vaults/{vaultName}/access-policy |  |
| [**deleteVaultNotifications**](DefaultApi.md#deleteVaultNotifications) | **DELETE** /{accountId}/vaults/{vaultName}/notification-configuration |  |
| [**describeJob**](DefaultApi.md#describeJob) | **GET** /{accountId}/vaults/{vaultName}/jobs/{jobId} |  |
| [**describeVault**](DefaultApi.md#describeVault) | **GET** /{accountId}/vaults/{vaultName} |  |
| [**getDataRetrievalPolicy**](DefaultApi.md#getDataRetrievalPolicy) | **GET** /{accountId}/policies/data-retrieval |  |
| [**getJobOutput**](DefaultApi.md#getJobOutput) | **GET** /{accountId}/vaults/{vaultName}/jobs/{jobId}/output |  |
| [**getVaultAccessPolicy**](DefaultApi.md#getVaultAccessPolicy) | **GET** /{accountId}/vaults/{vaultName}/access-policy |  |
| [**getVaultLock**](DefaultApi.md#getVaultLock) | **GET** /{accountId}/vaults/{vaultName}/lock-policy |  |
| [**getVaultNotifications**](DefaultApi.md#getVaultNotifications) | **GET** /{accountId}/vaults/{vaultName}/notification-configuration |  |
| [**initiateJob**](DefaultApi.md#initiateJob) | **POST** /{accountId}/vaults/{vaultName}/jobs |  |
| [**initiateMultipartUpload**](DefaultApi.md#initiateMultipartUpload) | **POST** /{accountId}/vaults/{vaultName}/multipart-uploads |  |
| [**initiateVaultLock**](DefaultApi.md#initiateVaultLock) | **POST** /{accountId}/vaults/{vaultName}/lock-policy |  |
| [**listJobs**](DefaultApi.md#listJobs) | **GET** /{accountId}/vaults/{vaultName}/jobs |  |
| [**listMultipartUploads**](DefaultApi.md#listMultipartUploads) | **GET** /{accountId}/vaults/{vaultName}/multipart-uploads |  |
| [**listParts**](DefaultApi.md#listParts) | **GET** /{accountId}/vaults/{vaultName}/multipart-uploads/{uploadId} |  |
| [**listProvisionedCapacity**](DefaultApi.md#listProvisionedCapacity) | **GET** /{accountId}/provisioned-capacity |  |
| [**listTagsForVault**](DefaultApi.md#listTagsForVault) | **GET** /{accountId}/vaults/{vaultName}/tags |  |
| [**listVaults**](DefaultApi.md#listVaults) | **GET** /{accountId}/vaults |  |
| [**purchaseProvisionedCapacity**](DefaultApi.md#purchaseProvisionedCapacity) | **POST** /{accountId}/provisioned-capacity |  |
| [**removeTagsFromVault**](DefaultApi.md#removeTagsFromVault) | **POST** /{accountId}/vaults/{vaultName}/tags#operation&#x3D;remove |  |
| [**setDataRetrievalPolicy**](DefaultApi.md#setDataRetrievalPolicy) | **PUT** /{accountId}/policies/data-retrieval |  |
| [**setVaultAccessPolicy**](DefaultApi.md#setVaultAccessPolicy) | **PUT** /{accountId}/vaults/{vaultName}/access-policy |  |
| [**setVaultNotifications**](DefaultApi.md#setVaultNotifications) | **PUT** /{accountId}/vaults/{vaultName}/notification-configuration |  |
| [**uploadArchive**](DefaultApi.md#uploadArchive) | **POST** /{accountId}/vaults/{vaultName}/archives |  |
| [**uploadMultipartPart**](DefaultApi.md#uploadMultipartPart) | **PUT** /{accountId}/vaults/{vaultName}/multipart-uploads/{uploadId} |  |


<a id="abortMultipartUpload"></a>
# **abortMultipartUpload**
> abortMultipartUpload(accountId, vaultName, uploadId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This operation aborts a multipart upload identified by the upload ID.&lt;/p&gt; &lt;p&gt;After the Abort Multipart Upload request succeeds, you cannot upload any more parts to the multipart upload or complete the multipart upload. Aborting a completed upload fails. However, aborting an already-aborted upload will succeed, for a short time. For more information about uploading a part and completing a multipart upload, see &lt;a&gt;UploadMultipartPart&lt;/a&gt; and &lt;a&gt;CompleteMultipartUpload&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation is idempotent.&lt;/p&gt; &lt;p&gt;An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don&#39;t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\&quot;&gt;Access Control Using AWS Identity and Access Management (IAM)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; For conceptual information and underlying REST API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html\&quot;&gt;Working with Archives in Amazon S3 Glacier&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-abort-upload.html\&quot;&gt;Abort Multipart Upload&lt;/a&gt; in the &lt;i&gt;Amazon Glacier Developer Guide&lt;/i&gt;. &lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String uploadId = "uploadId_example"; // String | The upload ID of the multipart upload to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.abortMultipartUpload(accountId, vaultName, uploadId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#abortMultipartUpload");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID. | |
| **vaultName** | **String**| The name of the vault. | |
| **uploadId** | **String**| The upload ID of the multipart upload to delete. | |
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
| **204** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="abortVaultLock"></a>
# **abortVaultLock**
> abortVaultLock(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This operation aborts the vault locking process if the vault lock is not in the &lt;code&gt;Locked&lt;/code&gt; state. If the vault lock is in the &lt;code&gt;Locked&lt;/code&gt; state when this operation is requested, the operation returns an &lt;code&gt;AccessDeniedException&lt;/code&gt; error. Aborting the vault locking process removes the vault lock policy from the specified vault. &lt;/p&gt; &lt;p&gt;A vault lock is put into the &lt;code&gt;InProgress&lt;/code&gt; state by calling &lt;a&gt;InitiateVaultLock&lt;/a&gt;. A vault lock is put into the &lt;code&gt;Locked&lt;/code&gt; state by calling &lt;a&gt;CompleteVaultLock&lt;/a&gt;. You can get the state of a vault lock by calling &lt;a&gt;GetVaultLock&lt;/a&gt;. For more information about the vault locking process, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html\&quot;&gt;Amazon Glacier Vault Lock&lt;/a&gt;. For more information about vault lock policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock-policy.html\&quot;&gt;Amazon Glacier Access Control with Vault Lock Policies&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;This operation is idempotent. You can successfully invoke this operation multiple times, if the vault lock is in the &lt;code&gt;InProgress&lt;/code&gt; state or if there is no policy associated with the vault.&lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.abortVaultLock(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#abortVaultLock");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (&#39;-&#39;) in the ID. | |
| **vaultName** | **String**| The name of the vault. | |
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
| **204** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="addTagsToVault"></a>
# **addTagsToVault**
> addTagsToVault(accountId, vaultName, operation, addTagsToVaultRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



This operation adds the specified tags to a vault. Each tag is composed of a key and a value. Each vault can have up to 10 tags. If your request would cause the tag limit for the vault to be exceeded, the operation throws the &lt;code&gt;LimitExceededException&lt;/code&gt; error. If a tag already exists on the vault under a specified key, the existing key value will be overwritten. For more information about tags, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/tagging.html\&quot;&gt;Tagging Amazon S3 Glacier Resources&lt;/a&gt;. 

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String operation = "add"; // String | 
    AddTagsToVaultRequest addTagsToVaultRequest = new AddTagsToVaultRequest(); // AddTagsToVaultRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.addTagsToVault(accountId, vaultName, operation, addTagsToVaultRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addTagsToVault");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID. | |
| **vaultName** | **String**| The name of the vault. | |
| **operation** | **String**|  | [enum: add] |
| **addTagsToVaultRequest** | [**AddTagsToVaultRequest**](AddTagsToVaultRequest.md)|  | |
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

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | InvalidParameterValueException |  -  |
| **481** | MissingParameterValueException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | LimitExceededException |  -  |
| **484** | ServiceUnavailableException |  -  |

<a id="completeMultipartUpload"></a>
# **completeMultipartUpload**
> Object completeMultipartUpload(accountId, vaultName, uploadId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzArchiveSize, xAmzSha256TreeHash)



&lt;p&gt;You call this operation to inform Amazon S3 Glacier (Glacier) that all the archive parts have been uploaded and that Glacier can now assemble the archive from the uploaded parts. After assembling and saving the archive to the vault, Glacier returns the URI path of the newly created archive resource. Using the URI path, you can then access the archive. After you upload an archive, you should save the archive ID returned to retrieve the archive at a later point. You can also get the vault inventory to obtain a list of archive IDs in a vault. For more information, see &lt;a&gt;InitiateJob&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;In the request, you must include the computed SHA256 tree hash of the entire archive you have uploaded. For information about computing a SHA256 tree hash, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html\&quot;&gt;Computing Checksums&lt;/a&gt;. On the server side, Glacier also constructs the SHA256 tree hash of the assembled archive. If the values match, Glacier saves the archive to the vault; otherwise, it returns an error, and the operation fails. The &lt;a&gt;ListParts&lt;/a&gt; operation returns a list of parts uploaded for a specific multipart upload. It includes checksum information for each uploaded part that can be used to debug a bad checksum issue.&lt;/p&gt; &lt;p&gt;Additionally, Glacier also checks for any missing content ranges when assembling the archive, if missing content ranges are found, Glacier returns an error and the operation fails.&lt;/p&gt; &lt;p&gt;Complete Multipart Upload is an idempotent operation. After your first successful complete multipart upload, if you call the operation again within a short period, the operation will succeed and return the same archive ID. This is useful in the event you experience a network issue that causes an aborted connection or receive a 500 server error, in which case you can repeat your Complete Multipart Upload request and get the same archive ID without creating duplicate archives. Note, however, that after the multipart upload completes, you cannot call the List Parts operation and the multipart upload will not appear in List Multipart Uploads response, even if idempotent complete is possible.&lt;/p&gt; &lt;p&gt;An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don&#39;t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\&quot;&gt;Access Control Using AWS Identity and Access Management (IAM)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; For conceptual information and underlying REST API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-archive-mpu.html\&quot;&gt;Uploading Large Archives in Parts (Multipart Upload)&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-complete-upload.html\&quot;&gt;Complete Multipart Upload&lt;/a&gt; in the &lt;i&gt;Amazon Glacier Developer Guide&lt;/i&gt;. &lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String uploadId = "uploadId_example"; // String | The upload ID of the multipart upload.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzArchiveSize = "xAmzArchiveSize_example"; // String | The total size, in bytes, of the entire archive. This value should be the sum of all the sizes of the individual parts that you uploaded.
    String xAmzSha256TreeHash = "xAmzSha256TreeHash_example"; // String | The SHA256 tree hash of the entire archive. It is the tree hash of SHA256 tree hash of the individual parts. If the value you specify in the request does not match the SHA256 tree hash of the final assembled archive as computed by Amazon S3 Glacier (Glacier), Glacier returns an error and the request fails.
    try {
      Object result = apiInstance.completeMultipartUpload(accountId, vaultName, uploadId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzArchiveSize, xAmzSha256TreeHash);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#completeMultipartUpload");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID. | |
| **vaultName** | **String**| The name of the vault. | |
| **uploadId** | **String**| The upload ID of the multipart upload. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzArchiveSize** | **String**| The total size, in bytes, of the entire archive. This value should be the sum of all the sizes of the individual parts that you uploaded. | [optional] |
| **xAmzSha256TreeHash** | **String**| The SHA256 tree hash of the entire archive. It is the tree hash of SHA256 tree hash of the individual parts. If the value you specify in the request does not match the SHA256 tree hash of the final assembled archive as computed by Amazon S3 Glacier (Glacier), Glacier returns an error and the request fails. | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="completeVaultLock"></a>
# **completeVaultLock**
> completeVaultLock(accountId, vaultName, lockId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This operation completes the vault locking process by transitioning the vault lock from the &lt;code&gt;InProgress&lt;/code&gt; state to the &lt;code&gt;Locked&lt;/code&gt; state, which causes the vault lock policy to become unchangeable. A vault lock is put into the &lt;code&gt;InProgress&lt;/code&gt; state by calling &lt;a&gt;InitiateVaultLock&lt;/a&gt;. You can obtain the state of the vault lock by calling &lt;a&gt;GetVaultLock&lt;/a&gt;. For more information about the vault locking process, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html\&quot;&gt;Amazon Glacier Vault Lock&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;This operation is idempotent. This request is always successful if the vault lock is in the &lt;code&gt;Locked&lt;/code&gt; state and the provided lock ID matches the lock ID originally used to lock the vault.&lt;/p&gt; &lt;p&gt;If an invalid lock ID is passed in the request when the vault lock is in the &lt;code&gt;Locked&lt;/code&gt; state, the operation returns an &lt;code&gt;AccessDeniedException&lt;/code&gt; error. If an invalid lock ID is passed in the request when the vault lock is in the &lt;code&gt;InProgress&lt;/code&gt; state, the operation throws an &lt;code&gt;InvalidParameter&lt;/code&gt; error.&lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String lockId = "lockId_example"; // String | The <code>lockId</code> value is the lock ID obtained from a <a>InitiateVaultLock</a> request.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.completeVaultLock(accountId, vaultName, lockId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#completeVaultLock");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (&#39;-&#39;) in the ID. | |
| **vaultName** | **String**| The name of the vault. | |
| **lockId** | **String**| The &lt;code&gt;lockId&lt;/code&gt; value is the lock ID obtained from a &lt;a&gt;InitiateVaultLock&lt;/a&gt; request. | |
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
| **204** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="createVault"></a>
# **createVault**
> Object createVault(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This operation creates a new vault with the specified name. The name of the vault must be unique within a region for an AWS account. You can create up to 1,000 vaults per account. If you need to create more vaults, contact Amazon S3 Glacier.&lt;/p&gt; &lt;p&gt;You must use the following guidelines when naming a vault.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Names can be between 1 and 255 characters long.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Allowed characters are a-z, A-Z, 0-9, &#39;_&#39; (underscore), &#39;-&#39; (hyphen), and &#39;.&#39; (period).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation is idempotent.&lt;/p&gt; &lt;p&gt;An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don&#39;t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\&quot;&gt;Access Control Using AWS Identity and Access Management (IAM)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; For conceptual information and underlying REST API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/creating-vaults.html\&quot;&gt;Creating a Vault in Amazon Glacier&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-put.html\&quot;&gt;Create Vault &lt;/a&gt; in the &lt;i&gt;Amazon Glacier Developer Guide&lt;/i&gt;. &lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.createVault(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createVault");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (&#39;-&#39;) in the ID. | |
| **vaultName** | **String**| The name of the vault. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | InvalidParameterValueException |  -  |
| **481** | MissingParameterValueException |  -  |
| **482** | ServiceUnavailableException |  -  |
| **483** | LimitExceededException |  -  |

<a id="deleteArchive"></a>
# **deleteArchive**
> deleteArchive(accountId, vaultName, archiveId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This operation deletes an archive from a vault. Subsequent requests to initiate a retrieval of this archive will fail. Archive retrievals that are in progress for this archive ID may or may not succeed according to the following scenarios:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the archive retrieval job is actively preparing the data for download when Amazon S3 Glacier receives the delete archive request, the archival retrieval operation might fail.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the archive retrieval job has successfully prepared the archive for download when Amazon S3 Glacier receives the delete archive request, you will be able to download the output.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation is idempotent. Attempting to delete an already-deleted archive does not result in an error.&lt;/p&gt; &lt;p&gt;An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don&#39;t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\&quot;&gt;Access Control Using AWS Identity and Access Management (IAM)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; For conceptual information and underlying REST API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-an-archive.html\&quot;&gt;Deleting an Archive in Amazon Glacier&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-delete.html\&quot;&gt;Delete Archive&lt;/a&gt; in the &lt;i&gt;Amazon Glacier Developer Guide&lt;/i&gt;. &lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String archiveId = "archiveId_example"; // String | The ID of the archive to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteArchive(accountId, vaultName, archiveId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteArchive");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID. | |
| **vaultName** | **String**| The name of the vault. | |
| **archiveId** | **String**| The ID of the archive to delete. | |
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
| **204** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="deleteVault"></a>
# **deleteVault**
> deleteVault(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This operation deletes a vault. Amazon S3 Glacier will delete a vault only if there are no archives in the vault as of the last inventory and there have been no writes to the vault since the last inventory. If either of these conditions is not satisfied, the vault deletion fails (that is, the vault is not removed) and Amazon S3 Glacier returns an error. You can use &lt;a&gt;DescribeVault&lt;/a&gt; to return the number of archives in a vault, and you can use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html\&quot;&gt;Initiate a Job (POST jobs)&lt;/a&gt; to initiate a new inventory retrieval for a vault. The inventory contains the archive IDs you use to delete archives using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-delete.html\&quot;&gt;Delete Archive (DELETE archive)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation is idempotent.&lt;/p&gt; &lt;p&gt;An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don&#39;t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\&quot;&gt;Access Control Using AWS Identity and Access Management (IAM)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; For conceptual information and underlying REST API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-vaults.html\&quot;&gt;Deleting a Vault in Amazon Glacier&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-delete.html\&quot;&gt;Delete Vault &lt;/a&gt; in the &lt;i&gt;Amazon S3 Glacier Developer Guide&lt;/i&gt;. &lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteVault(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteVault");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID. | |
| **vaultName** | **String**| The name of the vault. | |
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
| **204** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="deleteVaultAccessPolicy"></a>
# **deleteVaultAccessPolicy**
> deleteVaultAccessPolicy(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This operation deletes the access policy associated with the specified vault. The operation is eventually consistent; that is, it might take some time for Amazon S3 Glacier to completely remove the access policy, and you might still see the effect of the policy for a short time after you send the delete request.&lt;/p&gt; &lt;p&gt;This operation is idempotent. You can invoke delete multiple times, even if there is no policy associated with the vault. For more information about vault access policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html\&quot;&gt;Amazon Glacier Access Control with Vault Access Policies&lt;/a&gt;. &lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteVaultAccessPolicy(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteVaultAccessPolicy");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID.  | |
| **vaultName** | **String**| The name of the vault. | |
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
| **204** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="deleteVaultNotifications"></a>
# **deleteVaultNotifications**
> deleteVaultNotifications(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This operation deletes the notification configuration set for a vault. The operation is eventually consistent; that is, it might take some time for Amazon S3 Glacier to completely disable the notifications and you might still receive some notifications for a short time after you send the delete request.&lt;/p&gt; &lt;p&gt;An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don&#39;t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\&quot;&gt;Access Control Using AWS Identity and Access Management (IAM)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; For conceptual information and underlying REST API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications.html\&quot;&gt;Configuring Vault Notifications in Amazon S3 Glacier&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-notifications-delete.html\&quot;&gt;Delete Vault Notification Configuration &lt;/a&gt; in the Amazon S3 Glacier Developer Guide. &lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteVaultNotifications(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteVaultNotifications");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID.  | |
| **vaultName** | **String**| The name of the vault. | |
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
| **204** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="describeJob"></a>
# **describeJob**
> GlacierJobDescription describeJob(accountId, vaultName, jobId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This operation returns information about a job you previously initiated, including the job initiation date, the user who initiated the job, the job status code/message and the Amazon SNS topic to notify after Amazon S3 Glacier (Glacier) completes the job. For more information about initiating a job, see &lt;a&gt;InitiateJob&lt;/a&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation enables you to check the status of your job. However, it is strongly recommended that you set up an Amazon SNS topic and specify it in your initiate job request so that Glacier can notify the topic after it completes the job.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;A job ID will not expire for at least 24 hours after Glacier completes the job.&lt;/p&gt; &lt;p&gt;An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don&#39;t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\&quot;&gt;Access Control Using AWS Identity and Access Management (IAM)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; For more information about using this operation, see the documentation for the underlying REST API &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-describe-job-get.html\&quot;&gt;Describe Job&lt;/a&gt; in the &lt;i&gt;Amazon Glacier Developer Guide&lt;/i&gt;. &lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String jobId = "jobId_example"; // String | The ID of the job to describe.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GlacierJobDescription result = apiInstance.describeJob(accountId, vaultName, jobId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeJob");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID.  | |
| **vaultName** | **String**| The name of the vault. | |
| **jobId** | **String**| The ID of the job to describe. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GlacierJobDescription**](GlacierJobDescription.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="describeVault"></a>
# **describeVault**
> DescribeVaultOutput describeVault(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This operation returns information about a vault, including the vault&#39;s Amazon Resource Name (ARN), the date the vault was created, the number of archives it contains, and the total size of all the archives in the vault. The number of archives and their total size are as of the last inventory generation. This means that if you add or remove an archive from a vault, and then immediately use Describe Vault, the change in contents will not be immediately reflected. If you want to retrieve the latest inventory of the vault, use &lt;a&gt;InitiateJob&lt;/a&gt;. Amazon S3 Glacier generates vault inventories approximately daily. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-inventory.html\&quot;&gt;Downloading a Vault Inventory in Amazon S3 Glacier&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don&#39;t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\&quot;&gt;Access Control Using AWS Identity and Access Management (IAM)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For conceptual information and underlying REST API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/retrieving-vault-info.html\&quot;&gt;Retrieving Vault Metadata in Amazon S3 Glacier&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-get.html\&quot;&gt;Describe Vault &lt;/a&gt; in the &lt;i&gt;Amazon Glacier Developer Guide&lt;/i&gt;. &lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeVaultOutput result = apiInstance.describeVault(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeVault");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID.  | |
| **vaultName** | **String**| The name of the vault. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeVaultOutput**](DescribeVaultOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="getDataRetrievalPolicy"></a>
# **getDataRetrievalPolicy**
> GetDataRetrievalPolicyOutput getDataRetrievalPolicy(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



This operation returns the current data retrieval policy for the account and region specified in the GET request. For more information about data retrieval policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/data-retrieval-policy.html\&quot;&gt;Amazon Glacier Data Retrieval Policies&lt;/a&gt;.

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetDataRetrievalPolicyOutput result = apiInstance.getDataRetrievalPolicy(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDataRetrievalPolicy");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (&#39;-&#39;) in the ID.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetDataRetrievalPolicyOutput**](GetDataRetrievalPolicyOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterValueException |  -  |
| **481** | MissingParameterValueException |  -  |
| **482** | ServiceUnavailableException |  -  |

<a id="getJobOutput"></a>
# **getJobOutput**
> GetJobOutputOutput getJobOutput(accountId, vaultName, jobId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, range)



&lt;p&gt;This operation downloads the output of the job you initiated using &lt;a&gt;InitiateJob&lt;/a&gt;. Depending on the job type you specified when you initiated the job, the output will be either the content of an archive or a vault inventory.&lt;/p&gt; &lt;p&gt;You can download all the job output or download a portion of the output by specifying a byte range. In the case of an archive retrieval job, depending on the byte range you specify, Amazon S3 Glacier (Glacier) returns the checksum for the portion of the data. You can compute the checksum on the client and verify that the values match to ensure the portion you downloaded is the correct data.&lt;/p&gt; &lt;p&gt;A job ID will not expire for at least 24 hours after Glacier completes the job. That a byte range. For both archive and inventory retrieval jobs, you should verify the downloaded size against the size returned in the headers from the &lt;b&gt;Get Job Output&lt;/b&gt; response.&lt;/p&gt; &lt;p&gt;For archive retrieval jobs, you should also verify that the size is what you expected. If you download a portion of the output, the expected size is based on the range of bytes you specified. For example, if you specify a range of &lt;code&gt;bytes&#x3D;0-1048575&lt;/code&gt;, you should verify your download size is 1,048,576 bytes. If you download an entire archive, the expected size is the size of the archive when you uploaded it to Amazon S3 Glacier The expected size is also returned in the headers from the &lt;b&gt;Get Job Output&lt;/b&gt; response.&lt;/p&gt; &lt;p&gt;In the case of an archive retrieval job, depending on the byte range you specify, Glacier returns the checksum for the portion of the data. To ensure the portion you downloaded is the correct data, compute the checksum on the client, verify that the values match, and verify that the size is what you expected.&lt;/p&gt; &lt;p&gt;A job ID does not expire for at least 24 hours after Glacier completes the job. That is, you can download the job output within the 24 hours period after Amazon Glacier completes the job.&lt;/p&gt; &lt;p&gt;An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don&#39;t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\&quot;&gt;Access Control Using AWS Identity and Access Management (IAM)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For conceptual information and the underlying REST API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-inventory.html\&quot;&gt;Downloading a Vault Inventory&lt;/a&gt;, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/downloading-an-archive.html\&quot;&gt;Downloading an Archive&lt;/a&gt;, and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-job-output-get.html\&quot;&gt;Get Job Output &lt;/a&gt; &lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String jobId = "jobId_example"; // String | The job ID whose data is downloaded.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String range = "range_example"; // String | <p>The range of bytes to retrieve from the output. For example, if you want to download the first 1,048,576 bytes, specify the range as <code>bytes=0-1048575</code>. By default, this operation downloads the entire output.</p> <p>If the job output is large, then you can use a range to retrieve a portion of the output. This allows you to download the entire output in smaller chunks of bytes. For example, suppose you have 1 GB of job output you want to download and you decide to download 128 MB chunks of data at a time, which is a total of eight Get Job Output requests. You use the following process to download the job output:</p> <ol> <li> <p>Download a 128 MB chunk of output by specifying the appropriate byte range. Verify that all 128 MB of data was received.</p> </li> <li> <p>Along with the data, the response includes a SHA256 tree hash of the payload. You compute the checksum of the payload on the client and compare it with the checksum you received in the response to ensure you received all the expected data.</p> </li> <li> <p>Repeat steps 1 and 2 for all the eight 128 MB chunks of output data, each time specifying the appropriate byte range.</p> </li> <li> <p>After downloading all the parts of the job output, you have a list of eight checksum values. Compute the tree hash of these values to find the checksum of the entire output. Using the <a>DescribeJob</a> API, obtain job information of the job that provided you the output. The response includes the checksum of the entire archive stored in Amazon S3 Glacier. You compare this value with the checksum you computed to ensure you have downloaded the entire archive content with no errors.</p> <p/> </li> </ol>
    try {
      GetJobOutputOutput result = apiInstance.getJobOutput(accountId, vaultName, jobId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, range);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getJobOutput");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID. | |
| **vaultName** | **String**| The name of the vault. | |
| **jobId** | **String**| The job ID whose data is downloaded. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **range** | **String**| &lt;p&gt;The range of bytes to retrieve from the output. For example, if you want to download the first 1,048,576 bytes, specify the range as &lt;code&gt;bytes&#x3D;0-1048575&lt;/code&gt;. By default, this operation downloads the entire output.&lt;/p&gt; &lt;p&gt;If the job output is large, then you can use a range to retrieve a portion of the output. This allows you to download the entire output in smaller chunks of bytes. For example, suppose you have 1 GB of job output you want to download and you decide to download 128 MB chunks of data at a time, which is a total of eight Get Job Output requests. You use the following process to download the job output:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Download a 128 MB chunk of output by specifying the appropriate byte range. Verify that all 128 MB of data was received.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Along with the data, the response includes a SHA256 tree hash of the payload. You compute the checksum of the payload on the client and compare it with the checksum you received in the response to ensure you received all the expected data.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Repeat steps 1 and 2 for all the eight 128 MB chunks of output data, each time specifying the appropriate byte range.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;After downloading all the parts of the job output, you have a list of eight checksum values. Compute the tree hash of these values to find the checksum of the entire output. Using the &lt;a&gt;DescribeJob&lt;/a&gt; API, obtain job information of the job that provided you the output. The response includes the checksum of the entire archive stored in Amazon S3 Glacier. You compare this value with the checksum you computed to ensure you have downloaded the entire archive content with no errors.&lt;/p&gt; &lt;p/&gt; &lt;/li&gt; &lt;/ol&gt; | [optional] |

### Return type

[**GetJobOutputOutput**](GetJobOutputOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="getVaultAccessPolicy"></a>
# **getVaultAccessPolicy**
> GetVaultAccessPolicyOutput getVaultAccessPolicy(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



This operation retrieves the &lt;code&gt;access-policy&lt;/code&gt; subresource set on the vault; for more information on setting this subresource, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-SetVaultAccessPolicy.html\&quot;&gt;Set Vault Access Policy (PUT access-policy)&lt;/a&gt;. If there is no access policy set on the vault, the operation returns a &lt;code&gt;404 Not found&lt;/code&gt; error. For more information about vault access policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html\&quot;&gt;Amazon Glacier Access Control with Vault Access Policies&lt;/a&gt;.

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetVaultAccessPolicyOutput result = apiInstance.getVaultAccessPolicy(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getVaultAccessPolicy");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID. | |
| **vaultName** | **String**| The name of the vault. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetVaultAccessPolicyOutput**](GetVaultAccessPolicyOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="getVaultLock"></a>
# **getVaultLock**
> GetVaultLockOutput getVaultLock(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This operation retrieves the following attributes from the &lt;code&gt;lock-policy&lt;/code&gt; subresource set on the specified vault: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The vault lock policy set on the vault.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The state of the vault lock, which is either &lt;code&gt;InProgess&lt;/code&gt; or &lt;code&gt;Locked&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When the lock ID expires. The lock ID is used to complete the vault locking process.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When the vault lock was initiated and put into the &lt;code&gt;InProgress&lt;/code&gt; state.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;A vault lock is put into the &lt;code&gt;InProgress&lt;/code&gt; state by calling &lt;a&gt;InitiateVaultLock&lt;/a&gt;. A vault lock is put into the &lt;code&gt;Locked&lt;/code&gt; state by calling &lt;a&gt;CompleteVaultLock&lt;/a&gt;. You can abort the vault locking process by calling &lt;a&gt;AbortVaultLock&lt;/a&gt;. For more information about the vault locking process, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html\&quot;&gt;Amazon Glacier Vault Lock&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;If there is no vault lock policy set on the vault, the operation returns a &lt;code&gt;404 Not found&lt;/code&gt; error. For more information about vault lock policies, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock-policy.html\&quot;&gt;Amazon Glacier Access Control with Vault Lock Policies&lt;/a&gt;. &lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetVaultLockOutput result = apiInstance.getVaultLock(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getVaultLock");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID. | |
| **vaultName** | **String**| The name of the vault. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetVaultLockOutput**](GetVaultLockOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="getVaultNotifications"></a>
# **getVaultNotifications**
> GetVaultNotificationsOutput getVaultNotifications(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This operation retrieves the &lt;code&gt;notification-configuration&lt;/code&gt; subresource of the specified vault.&lt;/p&gt; &lt;p&gt;For information about setting a notification configuration on a vault, see &lt;a&gt;SetVaultNotifications&lt;/a&gt;. If a notification configuration for a vault is not set, the operation returns a &lt;code&gt;404 Not Found&lt;/code&gt; error. For more information about vault notifications, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications.html\&quot;&gt;Configuring Vault Notifications in Amazon S3 Glacier&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don&#39;t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\&quot;&gt;Access Control Using AWS Identity and Access Management (IAM)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For conceptual information and underlying REST API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications.html\&quot;&gt;Configuring Vault Notifications in Amazon S3 Glacier&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-notifications-get.html\&quot;&gt;Get Vault Notification Configuration &lt;/a&gt; in the &lt;i&gt;Amazon Glacier Developer Guide&lt;/i&gt;. &lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetVaultNotificationsOutput result = apiInstance.getVaultNotifications(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getVaultNotifications");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID. | |
| **vaultName** | **String**| The name of the vault. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetVaultNotificationsOutput**](GetVaultNotificationsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="initiateJob"></a>
# **initiateJob**
> Object initiateJob(accountId, vaultName, initiateJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



This operation initiates a job of the specified type, which can be a select, an archival retrieval, or a vault retrieval. For more information about using this operation, see the documentation for the underlying REST API &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html\&quot;&gt;Initiate a Job&lt;/a&gt;. 

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    InitiateJobRequest initiateJobRequest = new InitiateJobRequest(); // InitiateJobRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.initiateJob(accountId, vaultName, initiateJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#initiateJob");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID. | |
| **vaultName** | **String**| The name of the vault. | |
| **initiateJobRequest** | [**InitiateJobRequest**](InitiateJobRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | PolicyEnforcedException |  -  |
| **482** | InvalidParameterValueException |  -  |
| **483** | MissingParameterValueException |  -  |
| **484** | InsufficientCapacityException |  -  |
| **485** | ServiceUnavailableException |  -  |

<a id="initiateMultipartUpload"></a>
# **initiateMultipartUpload**
> Object initiateMultipartUpload(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzArchiveDescription, xAmzPartSize)



&lt;p&gt;This operation initiates a multipart upload. Amazon S3 Glacier creates a multipart upload resource and returns its ID in the response. The multipart upload ID is used in subsequent requests to upload parts of an archive (see &lt;a&gt;UploadMultipartPart&lt;/a&gt;).&lt;/p&gt; &lt;p&gt;When you initiate a multipart upload, you specify the part size in number of bytes. The part size must be a megabyte (1024 KB) multiplied by a power of 2-for example, 1048576 (1 MB), 2097152 (2 MB), 4194304 (4 MB), 8388608 (8 MB), and so on. The minimum allowable part size is 1 MB, and the maximum is 4 GB.&lt;/p&gt; &lt;p&gt;Every part you upload to this resource (see &lt;a&gt;UploadMultipartPart&lt;/a&gt;), except the last one, must have the same size. The last one can be the same size or smaller. For example, suppose you want to upload a 16.2 MB file. If you initiate the multipart upload with a part size of 4 MB, you will upload four parts of 4 MB each and one part of 0.2 MB. &lt;/p&gt; &lt;note&gt; &lt;p&gt;You don&#39;t need to know the size of the archive when you start a multipart upload because Amazon S3 Glacier does not require you to specify the overall archive size.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;After you complete the multipart upload, Amazon S3 Glacier (Glacier) removes the multipart upload resource referenced by the ID. Glacier also removes the multipart upload resource if you cancel the multipart upload or it may be removed if there is no activity for a period of 24 hours.&lt;/p&gt; &lt;p&gt;An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don&#39;t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\&quot;&gt;Access Control Using AWS Identity and Access Management (IAM)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For conceptual information and underlying REST API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-archive-mpu.html\&quot;&gt;Uploading Large Archives in Parts (Multipart Upload)&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-initiate-upload.html\&quot;&gt;Initiate Multipart Upload&lt;/a&gt; in the &lt;i&gt;Amazon Glacier Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzArchiveDescription = "xAmzArchiveDescription_example"; // String | <p>The archive description that you are uploading in parts.</p> <p>The part size must be a megabyte (1024 KB) multiplied by a power of 2, for example 1048576 (1 MB), 2097152 (2 MB), 4194304 (4 MB), 8388608 (8 MB), and so on. The minimum allowable part size is 1 MB, and the maximum is 4 GB (4096 MB).</p>
    String xAmzPartSize = "xAmzPartSize_example"; // String | The size of each part except the last, in bytes. The last part can be smaller than this part size.
    try {
      Object result = apiInstance.initiateMultipartUpload(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzArchiveDescription, xAmzPartSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#initiateMultipartUpload");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID.  | |
| **vaultName** | **String**| The name of the vault. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzArchiveDescription** | **String**| &lt;p&gt;The archive description that you are uploading in parts.&lt;/p&gt; &lt;p&gt;The part size must be a megabyte (1024 KB) multiplied by a power of 2, for example 1048576 (1 MB), 2097152 (2 MB), 4194304 (4 MB), 8388608 (8 MB), and so on. The minimum allowable part size is 1 MB, and the maximum is 4 GB (4096 MB).&lt;/p&gt; | [optional] |
| **xAmzPartSize** | **String**| The size of each part except the last, in bytes. The last part can be smaller than this part size. | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="initiateVaultLock"></a>
# **initiateVaultLock**
> Object initiateVaultLock(accountId, vaultName, initiateVaultLockRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This operation initiates the vault locking process by doing the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Installing a vault lock policy on the specified vault.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Setting the lock state of vault lock to &lt;code&gt;InProgress&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Returning a lock ID, which is used to complete the vault locking process.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can set one vault lock policy for each vault and this policy can be up to 20 KB in size. For more information about vault lock policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock-policy.html\&quot;&gt;Amazon Glacier Access Control with Vault Lock Policies&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;You must complete the vault locking process within 24 hours after the vault lock enters the &lt;code&gt;InProgress&lt;/code&gt; state. After the 24 hour window ends, the lock ID expires, the vault automatically exits the &lt;code&gt;InProgress&lt;/code&gt; state, and the vault lock policy is removed from the vault. You call &lt;a&gt;CompleteVaultLock&lt;/a&gt; to complete the vault locking process by setting the state of the vault lock to &lt;code&gt;Locked&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;After a vault lock is in the &lt;code&gt;Locked&lt;/code&gt; state, you cannot initiate a new vault lock for the vault.&lt;/p&gt; &lt;p&gt;You can abort the vault locking process by calling &lt;a&gt;AbortVaultLock&lt;/a&gt;. You can get the state of the vault lock by calling &lt;a&gt;GetVaultLock&lt;/a&gt;. For more information about the vault locking process, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html\&quot;&gt;Amazon Glacier Vault Lock&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If this operation is called when the vault lock is in the &lt;code&gt;InProgress&lt;/code&gt; state, the operation returns an &lt;code&gt;AccessDeniedException&lt;/code&gt; error. When the vault lock is in the &lt;code&gt;InProgress&lt;/code&gt; state you must call &lt;a&gt;AbortVaultLock&lt;/a&gt; before you can initiate a new vault lock policy. &lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    InitiateVaultLockRequest initiateVaultLockRequest = new InitiateVaultLockRequest(); // InitiateVaultLockRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.initiateVaultLock(accountId, vaultName, initiateVaultLockRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#initiateVaultLock");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (&#39;-&#39;) in the ID. | |
| **vaultName** | **String**| The name of the vault. | |
| **initiateVaultLockRequest** | [**InitiateVaultLockRequest**](InitiateVaultLockRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="listJobs"></a>
# **listJobs**
> ListJobsOutput listJobs(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, marker, statuscode, completed)



&lt;p&gt;This operation lists jobs for a vault, including jobs that are in-progress and jobs that have recently finished. The List Job operation returns a list of these jobs sorted by job initiation time.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Glacier retains recently completed jobs for a period before deleting them; however, it eventually removes completed jobs. The output of completed jobs can be retrieved. Retaining completed jobs for a period of time after they have completed enables you to get a job output in the event you miss the job completion notification or your first attempt to download it fails. For example, suppose you start an archive retrieval job to download an archive. After the job completes, you start to download the archive but encounter a network error. In this scenario, you can retry and download the archive while the job exists.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The List Jobs operation supports pagination. You should always check the response &lt;code&gt;Marker&lt;/code&gt; field. If there are no more jobs to list, the &lt;code&gt;Marker&lt;/code&gt; field is set to &lt;code&gt;null&lt;/code&gt;. If there are more jobs to list, the &lt;code&gt;Marker&lt;/code&gt; field is set to a non-null value, which you can use to continue the pagination of the list. To return a list of jobs that begins at a specific job, set the marker request parameter to the &lt;code&gt;Marker&lt;/code&gt; value for that job that you obtained from a previous List Jobs request.&lt;/p&gt; &lt;p&gt;You can set a maximum limit for the number of jobs returned in the response by specifying the &lt;code&gt;limit&lt;/code&gt; parameter in the request. The default limit is 50. The number of jobs returned might be fewer than the limit, but the number of returned jobs never exceeds the limit.&lt;/p&gt; &lt;p&gt;Additionally, you can filter the jobs list returned by specifying the optional &lt;code&gt;statuscode&lt;/code&gt; parameter or &lt;code&gt;completed&lt;/code&gt; parameter, or both. Using the &lt;code&gt;statuscode&lt;/code&gt; parameter, you can specify to return only jobs that match either the &lt;code&gt;InProgress&lt;/code&gt;, &lt;code&gt;Succeeded&lt;/code&gt;, or &lt;code&gt;Failed&lt;/code&gt; status. Using the &lt;code&gt;completed&lt;/code&gt; parameter, you can specify to return only jobs that were completed (&lt;code&gt;true&lt;/code&gt;) or jobs that were not completed (&lt;code&gt;false&lt;/code&gt;).&lt;/p&gt; &lt;p&gt;For more information about using this operation, see the documentation for the underlying REST API &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-jobs-get.html\&quot;&gt;List Jobs&lt;/a&gt;. &lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String limit = "limit_example"; // String | The maximum number of jobs to be returned. The default limit is 50. The number of jobs returned might be fewer than the specified limit, but the number of returned jobs never exceeds the limit.
    String marker = "marker_example"; // String | An opaque string used for pagination. This value specifies the job at which the listing of jobs should begin. Get the marker value from a previous List Jobs response. You only need to include the marker if you are continuing the pagination of results started in a previous List Jobs request.
    String statuscode = "statuscode_example"; // String | The type of job status to return. You can specify the following values: <code>InProgress</code>, <code>Succeeded</code>, or <code>Failed</code>.
    String completed = "completed_example"; // String | The state of the jobs to return. You can specify <code>true</code> or <code>false</code>.
    try {
      ListJobsOutput result = apiInstance.listJobs(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, marker, statuscode, completed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listJobs");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID.  | |
| **vaultName** | **String**| The name of the vault. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **limit** | **String**| The maximum number of jobs to be returned. The default limit is 50. The number of jobs returned might be fewer than the specified limit, but the number of returned jobs never exceeds the limit. | [optional] |
| **marker** | **String**| An opaque string used for pagination. This value specifies the job at which the listing of jobs should begin. Get the marker value from a previous List Jobs response. You only need to include the marker if you are continuing the pagination of results started in a previous List Jobs request. | [optional] |
| **statuscode** | **String**| The type of job status to return. You can specify the following values: &lt;code&gt;InProgress&lt;/code&gt;, &lt;code&gt;Succeeded&lt;/code&gt;, or &lt;code&gt;Failed&lt;/code&gt;. | [optional] |
| **completed** | **String**| The state of the jobs to return. You can specify &lt;code&gt;true&lt;/code&gt; or &lt;code&gt;false&lt;/code&gt;. | [optional] |

### Return type

[**ListJobsOutput**](ListJobsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="listMultipartUploads"></a>
# **listMultipartUploads**
> ListMultipartUploadsOutput listMultipartUploads(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, limit)



&lt;p&gt;This operation lists in-progress multipart uploads for the specified vault. An in-progress multipart upload is a multipart upload that has been initiated by an &lt;a&gt;InitiateMultipartUpload&lt;/a&gt; request, but has not yet been completed or aborted. The list returned in the List Multipart Upload response has no guaranteed order. &lt;/p&gt; &lt;p&gt;The List Multipart Uploads operation supports pagination. By default, this operation returns up to 50 multipart uploads in the response. You should always check the response for a &lt;code&gt;marker&lt;/code&gt; at which to continue the list; if there are no more items the &lt;code&gt;marker&lt;/code&gt; is &lt;code&gt;null&lt;/code&gt;. To return a list of multipart uploads that begins at a specific upload, set the &lt;code&gt;marker&lt;/code&gt; request parameter to the value you obtained from a previous List Multipart Upload request. You can also limit the number of uploads returned in the response by specifying the &lt;code&gt;limit&lt;/code&gt; parameter in the request.&lt;/p&gt; &lt;p&gt;Note the difference between this operation and listing parts (&lt;a&gt;ListParts&lt;/a&gt;). The List Multipart Uploads operation lists all multipart uploads for a vault and does not require a multipart upload ID. The List Parts operation requires a multipart upload ID since parts are associated with a single upload.&lt;/p&gt; &lt;p&gt;An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don&#39;t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\&quot;&gt;Access Control Using AWS Identity and Access Management (IAM)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For conceptual information and the underlying REST API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html\&quot;&gt;Working with Archives in Amazon S3 Glacier&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-list-uploads.html\&quot;&gt;List Multipart Uploads &lt;/a&gt; in the &lt;i&gt;Amazon Glacier Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String marker = "marker_example"; // String | An opaque string used for pagination. This value specifies the upload at which the listing of uploads should begin. Get the marker value from a previous List Uploads response. You need only include the marker if you are continuing the pagination of results started in a previous List Uploads request.
    String limit = "limit_example"; // String | Specifies the maximum number of uploads returned in the response body. If this value is not specified, the List Uploads operation returns up to 50 uploads.
    try {
      ListMultipartUploadsOutput result = apiInstance.listMultipartUploads(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listMultipartUploads");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID.  | |
| **vaultName** | **String**| The name of the vault. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| An opaque string used for pagination. This value specifies the upload at which the listing of uploads should begin. Get the marker value from a previous List Uploads response. You need only include the marker if you are continuing the pagination of results started in a previous List Uploads request. | [optional] |
| **limit** | **String**| Specifies the maximum number of uploads returned in the response body. If this value is not specified, the List Uploads operation returns up to 50 uploads. | [optional] |

### Return type

[**ListMultipartUploadsOutput**](ListMultipartUploadsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="listParts"></a>
# **listParts**
> ListPartsOutput listParts(accountId, vaultName, uploadId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, limit)



&lt;p&gt;This operation lists the parts of an archive that have been uploaded in a specific multipart upload. You can make this request at any time during an in-progress multipart upload before you complete the upload (see &lt;a&gt;CompleteMultipartUpload&lt;/a&gt;. List Parts returns an error for completed uploads. The list returned in the List Parts response is sorted by part range. &lt;/p&gt; &lt;p&gt;The List Parts operation supports pagination. By default, this operation returns up to 50 uploaded parts in the response. You should always check the response for a &lt;code&gt;marker&lt;/code&gt; at which to continue the list; if there are no more items the &lt;code&gt;marker&lt;/code&gt; is &lt;code&gt;null&lt;/code&gt;. To return a list of parts that begins at a specific part, set the &lt;code&gt;marker&lt;/code&gt; request parameter to the value you obtained from a previous List Parts request. You can also limit the number of parts returned in the response by specifying the &lt;code&gt;limit&lt;/code&gt; parameter in the request. &lt;/p&gt; &lt;p&gt;An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don&#39;t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\&quot;&gt;Access Control Using AWS Identity and Access Management (IAM)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For conceptual information and the underlying REST API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html\&quot;&gt;Working with Archives in Amazon S3 Glacier&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-list-parts.html\&quot;&gt;List Parts&lt;/a&gt; in the &lt;i&gt;Amazon Glacier Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String uploadId = "uploadId_example"; // String | The upload ID of the multipart upload.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String marker = "marker_example"; // String | An opaque string used for pagination. This value specifies the part at which the listing of parts should begin. Get the marker value from the response of a previous List Parts response. You need only include the marker if you are continuing the pagination of results started in a previous List Parts request.
    String limit = "limit_example"; // String | The maximum number of parts to be returned. The default limit is 50. The number of parts returned might be fewer than the specified limit, but the number of returned parts never exceeds the limit.
    try {
      ListPartsOutput result = apiInstance.listParts(accountId, vaultName, uploadId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listParts");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID.  | |
| **vaultName** | **String**| The name of the vault. | |
| **uploadId** | **String**| The upload ID of the multipart upload. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| An opaque string used for pagination. This value specifies the part at which the listing of parts should begin. Get the marker value from the response of a previous List Parts response. You need only include the marker if you are continuing the pagination of results started in a previous List Parts request. | [optional] |
| **limit** | **String**| The maximum number of parts to be returned. The default limit is 50. The number of parts returned might be fewer than the specified limit, but the number of returned parts never exceeds the limit. | [optional] |

### Return type

[**ListPartsOutput**](ListPartsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="listProvisionedCapacity"></a>
# **listProvisionedCapacity**
> ListProvisionedCapacityOutput listProvisionedCapacity(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



This operation lists the provisioned capacity units for the specified AWS account.

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '-' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, don't include any hyphens ('-') in the ID. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListProvisionedCapacityOutput result = apiInstance.listProvisionedCapacity(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listProvisionedCapacity");
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
| **accountId** | **String**| The AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;-&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, don&#39;t include any hyphens (&#39;-&#39;) in the ID.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListProvisionedCapacityOutput**](ListProvisionedCapacityOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterValueException |  -  |
| **481** | MissingParameterValueException |  -  |
| **482** | ServiceUnavailableException |  -  |

<a id="listTagsForVault"></a>
# **listTagsForVault**
> ListTagsForVaultOutput listTagsForVault(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



This operation lists all the tags attached to a vault. The operation returns an empty map if there are no tags. For more information about tags, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/tagging.html\&quot;&gt;Tagging Amazon S3 Glacier Resources&lt;/a&gt;.

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListTagsForVaultOutput result = apiInstance.listTagsForVault(accountId, vaultName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTagsForVault");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID. | |
| **vaultName** | **String**| The name of the vault. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListTagsForVaultOutput**](ListTagsForVaultOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterValueException |  -  |
| **481** | MissingParameterValueException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="listVaults"></a>
# **listVaults**
> ListVaultsOutput listVaults(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, limit)



&lt;p&gt;This operation lists all vaults owned by the calling user&#39;s account. The list returned in the response is ASCII-sorted by vault name.&lt;/p&gt; &lt;p&gt;By default, this operation returns up to 10 items. If there are more vaults to list, the response &lt;code&gt;marker&lt;/code&gt; field contains the vault Amazon Resource Name (ARN) at which to continue the list with a new List Vaults request; otherwise, the &lt;code&gt;marker&lt;/code&gt; field is &lt;code&gt;null&lt;/code&gt;. To return a list of vaults that begins at a specific vault, set the &lt;code&gt;marker&lt;/code&gt; request parameter to the vault ARN you obtained from a previous List Vaults request. You can also limit the number of vaults returned in the response by specifying the &lt;code&gt;limit&lt;/code&gt; parameter in the request. &lt;/p&gt; &lt;p&gt;An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don&#39;t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\&quot;&gt;Access Control Using AWS Identity and Access Management (IAM)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For conceptual information and underlying REST API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/retrieving-vault-info.html\&quot;&gt;Retrieving Vault Metadata in Amazon S3 Glacier&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vaults-get.html\&quot;&gt;List Vaults &lt;/a&gt; in the &lt;i&gt;Amazon Glacier Developer Guide&lt;/i&gt;. &lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String marker = "marker_example"; // String | A string used for pagination. The marker specifies the vault ARN after which the listing of vaults should begin.
    String limit = "limit_example"; // String | The maximum number of vaults to be returned. The default limit is 10. The number of vaults returned might be fewer than the specified limit, but the number of returned vaults never exceeds the limit.
    try {
      ListVaultsOutput result = apiInstance.listVaults(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listVaults");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (&#39;-&#39;) in the ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| A string used for pagination. The marker specifies the vault ARN after which the listing of vaults should begin. | [optional] |
| **limit** | **String**| The maximum number of vaults to be returned. The default limit is 10. The number of vaults returned might be fewer than the specified limit, but the number of returned vaults never exceeds the limit. | [optional] |

### Return type

[**ListVaultsOutput**](ListVaultsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="purchaseProvisionedCapacity"></a>
# **purchaseProvisionedCapacity**
> Object purchaseProvisionedCapacity(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



This operation purchases a provisioned capacity unit for an AWS account. 

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '-' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, don't include any hyphens ('-') in the ID. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.purchaseProvisionedCapacity(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#purchaseProvisionedCapacity");
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
| **accountId** | **String**| The AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;-&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, don&#39;t include any hyphens (&#39;-&#39;) in the ID.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | InvalidParameterValueException |  -  |
| **481** | MissingParameterValueException |  -  |
| **482** | LimitExceededException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="removeTagsFromVault"></a>
# **removeTagsFromVault**
> removeTagsFromVault(accountId, vaultName, operation, removeTagsFromVaultRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



This operation removes one or more tags from the set of tags attached to a vault. For more information about tags, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/tagging.html\&quot;&gt;Tagging Amazon S3 Glacier Resources&lt;/a&gt;. This operation is idempotent. The operation will be successful, even if there are no tags attached to the vault. 

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String operation = "remove"; // String | 
    RemoveTagsFromVaultRequest removeTagsFromVaultRequest = new RemoveTagsFromVaultRequest(); // RemoveTagsFromVaultRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.removeTagsFromVault(accountId, vaultName, operation, removeTagsFromVaultRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeTagsFromVault");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID. | |
| **vaultName** | **String**| The name of the vault. | |
| **operation** | **String**|  | [enum: remove] |
| **removeTagsFromVaultRequest** | [**RemoveTagsFromVaultRequest**](RemoveTagsFromVaultRequest.md)|  | |
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

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | InvalidParameterValueException |  -  |
| **481** | MissingParameterValueException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="setDataRetrievalPolicy"></a>
# **setDataRetrievalPolicy**
> setDataRetrievalPolicy(accountId, setDataRetrievalPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This operation sets and then enacts a data retrieval policy in the region specified in the PUT request. You can set one policy per region for an AWS account. The policy is enacted within a few minutes of a successful PUT operation.&lt;/p&gt; &lt;p&gt;The set policy operation does not affect retrieval jobs that were in progress before the policy was enacted. For more information about data retrieval policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/data-retrieval-policy.html\&quot;&gt;Amazon Glacier Data Retrieval Policies&lt;/a&gt;. &lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.
    SetDataRetrievalPolicyRequest setDataRetrievalPolicyRequest = new SetDataRetrievalPolicyRequest(); // SetDataRetrievalPolicyRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.setDataRetrievalPolicy(accountId, setDataRetrievalPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#setDataRetrievalPolicy");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (&#39;-&#39;) in the ID. | |
| **setDataRetrievalPolicyRequest** | [**SetDataRetrievalPolicyRequest**](SetDataRetrievalPolicyRequest.md)|  | |
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

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | InvalidParameterValueException |  -  |
| **481** | MissingParameterValueException |  -  |
| **482** | ServiceUnavailableException |  -  |

<a id="setVaultAccessPolicy"></a>
# **setVaultAccessPolicy**
> setVaultAccessPolicy(accountId, vaultName, setVaultAccessPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



This operation configures an access policy for a vault and will overwrite an existing policy. To configure a vault access policy, send a PUT request to the &lt;code&gt;access-policy&lt;/code&gt; subresource of the vault. An access policy is specific to a vault and is also called a vault subresource. You can set one access policy per vault and the policy can be up to 20 KB in size. For more information about vault access policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html\&quot;&gt;Amazon Glacier Access Control with Vault Access Policies&lt;/a&gt;. 

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    SetVaultAccessPolicyRequest setVaultAccessPolicyRequest = new SetVaultAccessPolicyRequest(); // SetVaultAccessPolicyRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.setVaultAccessPolicy(accountId, vaultName, setVaultAccessPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#setVaultAccessPolicy");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID. | |
| **vaultName** | **String**| The name of the vault. | |
| **setVaultAccessPolicyRequest** | [**SetVaultAccessPolicyRequest**](SetVaultAccessPolicyRequest.md)|  | |
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

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="setVaultNotifications"></a>
# **setVaultNotifications**
> setVaultNotifications(accountId, vaultName, setVaultNotificationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This operation configures notifications that will be sent when specific events happen to a vault. By default, you don&#39;t get any notifications.&lt;/p&gt; &lt;p&gt;To configure vault notifications, send a PUT request to the &lt;code&gt;notification-configuration&lt;/code&gt; subresource of the vault. The request should include a JSON document that provides an Amazon SNS topic and specific events for which you want Amazon S3 Glacier to send notifications to the topic.&lt;/p&gt; &lt;p&gt;Amazon SNS topics must grant permission to the vault to be allowed to publish notifications to the topic. You can configure a vault to publish a notification for the following vault events:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;ArchiveRetrievalCompleted&lt;/b&gt; This event occurs when a job that was initiated for an archive retrieval is completed (&lt;a&gt;InitiateJob&lt;/a&gt;). The status of the completed job can be \&quot;Succeeded\&quot; or \&quot;Failed\&quot;. The notification sent to the SNS topic is the same output as returned from &lt;a&gt;DescribeJob&lt;/a&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;InventoryRetrievalCompleted&lt;/b&gt; This event occurs when a job that was initiated for an inventory retrieval is completed (&lt;a&gt;InitiateJob&lt;/a&gt;). The status of the completed job can be \&quot;Succeeded\&quot; or \&quot;Failed\&quot;. The notification sent to the SNS topic is the same output as returned from &lt;a&gt;DescribeJob&lt;/a&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don&#39;t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\&quot;&gt;Access Control Using AWS Identity and Access Management (IAM)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For conceptual information and underlying REST API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications.html\&quot;&gt;Configuring Vault Notifications in Amazon S3 Glacier&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-notifications-put.html\&quot;&gt;Set Vault Notification Configuration &lt;/a&gt; in the &lt;i&gt;Amazon Glacier Developer Guide&lt;/i&gt;. &lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    SetVaultNotificationsRequest setVaultNotificationsRequest = new SetVaultNotificationsRequest(); // SetVaultNotificationsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.setVaultNotifications(accountId, vaultName, setVaultNotificationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#setVaultNotifications");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID. | |
| **vaultName** | **String**| The name of the vault. | |
| **setVaultNotificationsRequest** | [**SetVaultNotificationsRequest**](SetVaultNotificationsRequest.md)|  | |
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

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="uploadArchive"></a>
# **uploadArchive**
> Object uploadArchive(vaultName, accountId, uploadMultipartPartRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzArchiveDescription, xAmzSha256TreeHash)



&lt;p&gt;This operation adds an archive to a vault. This is a synchronous operation, and for a successful upload, your data is durably persisted. Amazon S3 Glacier returns the archive ID in the &lt;code&gt;x-amz-archive-id&lt;/code&gt; header of the response. &lt;/p&gt; &lt;p&gt;You must use the archive ID to access your data in Amazon S3 Glacier. After you upload an archive, you should save the archive ID returned so that you can retrieve or delete the archive later. Besides saving the archive ID, you can also index it and give it a friendly name to allow for better searching. You can also use the optional archive description field to specify how the archive is referred to in an external index of archives, such as you might create in Amazon DynamoDB. You can also get the vault inventory to obtain a list of archive IDs in a vault. For more information, see &lt;a&gt;InitiateJob&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;You must provide a SHA256 tree hash of the data you are uploading. For information about computing a SHA256 tree hash, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html\&quot;&gt;Computing Checksums&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;You can optionally specify an archive description of up to 1,024 printable ASCII characters. You can get the archive description when you either retrieve the archive or get the vault inventory. For more information, see &lt;a&gt;InitiateJob&lt;/a&gt;. Amazon Glacier does not interpret the description in any way. An archive description does not need to be unique. You cannot use the description to retrieve or sort the archive list. &lt;/p&gt; &lt;p&gt;Archives are immutable. After you upload an archive, you cannot edit the archive or its description.&lt;/p&gt; &lt;p&gt;An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don&#39;t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\&quot;&gt;Access Control Using AWS Identity and Access Management (IAM)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; For conceptual information and underlying REST API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-an-archive.html\&quot;&gt;Uploading an Archive in Amazon Glacier&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-post.html\&quot;&gt;Upload Archive&lt;/a&gt; in the &lt;i&gt;Amazon Glacier Developer Guide&lt;/i&gt;. &lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 
    UploadMultipartPartRequest uploadMultipartPartRequest = new UploadMultipartPartRequest(); // UploadMultipartPartRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzArchiveDescription = "xAmzArchiveDescription_example"; // String | The optional description of the archive you are uploading.
    String xAmzSha256TreeHash = "xAmzSha256TreeHash_example"; // String | The SHA256 tree hash of the data being uploaded.
    try {
      Object result = apiInstance.uploadArchive(vaultName, accountId, uploadMultipartPartRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzArchiveDescription, xAmzSha256TreeHash);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#uploadArchive");
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
| **vaultName** | **String**| The name of the vault. | |
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID.  | |
| **uploadMultipartPartRequest** | [**UploadMultipartPartRequest**](UploadMultipartPartRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzArchiveDescription** | **String**| The optional description of the archive you are uploading. | [optional] |
| **xAmzSha256TreeHash** | **String**| The SHA256 tree hash of the data being uploaded. | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | RequestTimeoutException |  -  |
| **484** | ServiceUnavailableException |  -  |

<a id="uploadMultipartPart"></a>
# **uploadMultipartPart**
> Object uploadMultipartPart(accountId, vaultName, uploadId, uploadMultipartPartRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzSha256TreeHash, contentRange)



&lt;p&gt;This operation uploads a part of an archive. You can upload archive parts in any order. You can also upload them in parallel. You can upload up to 10,000 parts for a multipart upload.&lt;/p&gt; &lt;p&gt;Amazon Glacier rejects your upload part request if any of the following conditions is true:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;SHA256 tree hash does not match&lt;/b&gt;To ensure that part data is not corrupted in transmission, you compute a SHA256 tree hash of the part and include it in your request. Upon receiving the part data, Amazon S3 Glacier also computes a SHA256 tree hash. If these hash values don&#39;t match, the operation fails. For information about computing a SHA256 tree hash, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html\&quot;&gt;Computing Checksums&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Part size does not match&lt;/b&gt;The size of each part except the last must match the size specified in the corresponding &lt;a&gt;InitiateMultipartUpload&lt;/a&gt; request. The size of the last part must be the same size as, or smaller than, the specified size.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you upload a part whose size is smaller than the part size you specified in your initiate multipart upload request and that part is not the last part, then the upload part request will succeed. However, the subsequent Complete Multipart Upload request will fail.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Range does not align&lt;/b&gt;The byte range value in the request does not align with the part size specified in the corresponding initiate request. For example, if you specify a part size of 4194304 bytes (4 MB), then 0 to 4194303 bytes (4 MB - 1) and 4194304 (4 MB) to 8388607 (8 MB - 1) are valid part ranges. However, if you set a range value of 2 MB to 6 MB, the range does not align with the part size and the upload will fail. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation is idempotent. If you upload the same part multiple times, the data included in the most recent request overwrites the previously uploaded data.&lt;/p&gt; &lt;p&gt;An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don&#39;t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\&quot;&gt;Access Control Using AWS Identity and Access Management (IAM)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; For conceptual information and underlying REST API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-archive-mpu.html\&quot;&gt;Uploading Large Archives in Parts (Multipart Upload)&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/api-upload-part.html\&quot;&gt;Upload Part &lt;/a&gt; in the &lt;i&gt;Amazon Glacier Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("http://glacier.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String uploadId = "uploadId_example"; // String | The upload ID of the multipart upload.
    UploadMultipartPartRequest uploadMultipartPartRequest = new UploadMultipartPartRequest(); // UploadMultipartPartRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzSha256TreeHash = "xAmzSha256TreeHash_example"; // String | The SHA256 tree hash of the data being uploaded.
    String contentRange = "contentRange_example"; // String | Identifies the range of bytes in the assembled archive that will be uploaded in this part. Amazon S3 Glacier uses this information to assemble the archive in the proper sequence. The format of this header follows RFC 2616. An example header is Content-Range:bytes 0-4194303/_*.
    try {
      Object result = apiInstance.uploadMultipartPart(accountId, vaultName, uploadId, uploadMultipartPartRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzSha256TreeHash, contentRange);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#uploadMultipartPart");
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
| **accountId** | **String**| The &lt;code&gt;AccountId&lt;/code&gt; value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single &#39;&lt;code&gt;-&lt;/code&gt;&#39; (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (&#39;-&#39;) in the ID.  | |
| **vaultName** | **String**| The name of the vault. | |
| **uploadId** | **String**| The upload ID of the multipart upload. | |
| **uploadMultipartPartRequest** | [**UploadMultipartPartRequest**](UploadMultipartPartRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzSha256TreeHash** | **String**| The SHA256 tree hash of the data being uploaded. | [optional] |
| **contentRange** | **String**| Identifies the range of bytes in the assembled archive that will be uploaded in this part. Amazon S3 Glacier uses this information to assemble the archive in the proper sequence. The format of this header follows RFC 2616. An example header is Content-Range:bytes 0-4194303/_*. | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidParameterValueException |  -  |
| **482** | MissingParameterValueException |  -  |
| **483** | RequestTimeoutException |  -  |
| **484** | ServiceUnavailableException |  -  |

