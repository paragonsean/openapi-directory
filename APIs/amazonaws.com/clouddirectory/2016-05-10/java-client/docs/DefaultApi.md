# DefaultApi

All URIs are relative to *http://clouddirectory.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addFacetToObject**](DefaultApi.md#addFacetToObject) | **PUT** /amazonclouddirectory/2017-01-11/object/facets#x-amz-data-partition |  |
| [**applySchema**](DefaultApi.md#applySchema) | **PUT** /amazonclouddirectory/2017-01-11/schema/apply#x-amz-data-partition |  |
| [**attachObject**](DefaultApi.md#attachObject) | **PUT** /amazonclouddirectory/2017-01-11/object/attach#x-amz-data-partition |  |
| [**attachPolicy**](DefaultApi.md#attachPolicy) | **PUT** /amazonclouddirectory/2017-01-11/policy/attach#x-amz-data-partition |  |
| [**attachToIndex**](DefaultApi.md#attachToIndex) | **PUT** /amazonclouddirectory/2017-01-11/index/attach#x-amz-data-partition |  |
| [**attachTypedLink**](DefaultApi.md#attachTypedLink) | **PUT** /amazonclouddirectory/2017-01-11/typedlink/attach#x-amz-data-partition |  |
| [**batchRead**](DefaultApi.md#batchRead) | **POST** /amazonclouddirectory/2017-01-11/batchread#x-amz-data-partition |  |
| [**batchWrite**](DefaultApi.md#batchWrite) | **PUT** /amazonclouddirectory/2017-01-11/batchwrite#x-amz-data-partition |  |
| [**createDirectory**](DefaultApi.md#createDirectory) | **PUT** /amazonclouddirectory/2017-01-11/directory/create#x-amz-data-partition |  |
| [**createFacet**](DefaultApi.md#createFacet) | **PUT** /amazonclouddirectory/2017-01-11/facet/create#x-amz-data-partition |  |
| [**createIndex**](DefaultApi.md#createIndex) | **PUT** /amazonclouddirectory/2017-01-11/index#x-amz-data-partition |  |
| [**createObject**](DefaultApi.md#createObject) | **PUT** /amazonclouddirectory/2017-01-11/object#x-amz-data-partition |  |
| [**createSchema**](DefaultApi.md#createSchema) | **PUT** /amazonclouddirectory/2017-01-11/schema/create |  |
| [**createTypedLinkFacet**](DefaultApi.md#createTypedLinkFacet) | **PUT** /amazonclouddirectory/2017-01-11/typedlink/facet/create#x-amz-data-partition |  |
| [**deleteDirectory**](DefaultApi.md#deleteDirectory) | **PUT** /amazonclouddirectory/2017-01-11/directory#x-amz-data-partition |  |
| [**deleteFacet**](DefaultApi.md#deleteFacet) | **PUT** /amazonclouddirectory/2017-01-11/facet/delete#x-amz-data-partition |  |
| [**deleteObject**](DefaultApi.md#deleteObject) | **PUT** /amazonclouddirectory/2017-01-11/object/delete#x-amz-data-partition |  |
| [**deleteSchema**](DefaultApi.md#deleteSchema) | **PUT** /amazonclouddirectory/2017-01-11/schema#x-amz-data-partition |  |
| [**deleteTypedLinkFacet**](DefaultApi.md#deleteTypedLinkFacet) | **PUT** /amazonclouddirectory/2017-01-11/typedlink/facet/delete#x-amz-data-partition |  |
| [**detachFromIndex**](DefaultApi.md#detachFromIndex) | **PUT** /amazonclouddirectory/2017-01-11/index/detach#x-amz-data-partition |  |
| [**detachObject**](DefaultApi.md#detachObject) | **PUT** /amazonclouddirectory/2017-01-11/object/detach#x-amz-data-partition |  |
| [**detachPolicy**](DefaultApi.md#detachPolicy) | **PUT** /amazonclouddirectory/2017-01-11/policy/detach#x-amz-data-partition |  |
| [**detachTypedLink**](DefaultApi.md#detachTypedLink) | **PUT** /amazonclouddirectory/2017-01-11/typedlink/detach#x-amz-data-partition |  |
| [**disableDirectory**](DefaultApi.md#disableDirectory) | **PUT** /amazonclouddirectory/2017-01-11/directory/disable#x-amz-data-partition |  |
| [**enableDirectory**](DefaultApi.md#enableDirectory) | **PUT** /amazonclouddirectory/2017-01-11/directory/enable#x-amz-data-partition |  |
| [**getAppliedSchemaVersion**](DefaultApi.md#getAppliedSchemaVersion) | **POST** /amazonclouddirectory/2017-01-11/schema/getappliedschema |  |
| [**getDirectory**](DefaultApi.md#getDirectory) | **POST** /amazonclouddirectory/2017-01-11/directory/get#x-amz-data-partition |  |
| [**getFacet**](DefaultApi.md#getFacet) | **POST** /amazonclouddirectory/2017-01-11/facet#x-amz-data-partition |  |
| [**getLinkAttributes**](DefaultApi.md#getLinkAttributes) | **POST** /amazonclouddirectory/2017-01-11/typedlink/attributes/get#x-amz-data-partition |  |
| [**getObjectAttributes**](DefaultApi.md#getObjectAttributes) | **POST** /amazonclouddirectory/2017-01-11/object/attributes/get#x-amz-data-partition |  |
| [**getObjectInformation**](DefaultApi.md#getObjectInformation) | **POST** /amazonclouddirectory/2017-01-11/object/information#x-amz-data-partition |  |
| [**getSchemaAsJson**](DefaultApi.md#getSchemaAsJson) | **POST** /amazonclouddirectory/2017-01-11/schema/json#x-amz-data-partition |  |
| [**getTypedLinkFacetInformation**](DefaultApi.md#getTypedLinkFacetInformation) | **POST** /amazonclouddirectory/2017-01-11/typedlink/facet/get#x-amz-data-partition |  |
| [**listAppliedSchemaArns**](DefaultApi.md#listAppliedSchemaArns) | **POST** /amazonclouddirectory/2017-01-11/schema/applied |  |
| [**listAttachedIndices**](DefaultApi.md#listAttachedIndices) | **POST** /amazonclouddirectory/2017-01-11/object/indices#x-amz-data-partition |  |
| [**listDevelopmentSchemaArns**](DefaultApi.md#listDevelopmentSchemaArns) | **POST** /amazonclouddirectory/2017-01-11/schema/development |  |
| [**listDirectories**](DefaultApi.md#listDirectories) | **POST** /amazonclouddirectory/2017-01-11/directory/list |  |
| [**listFacetAttributes**](DefaultApi.md#listFacetAttributes) | **POST** /amazonclouddirectory/2017-01-11/facet/attributes#x-amz-data-partition |  |
| [**listFacetNames**](DefaultApi.md#listFacetNames) | **POST** /amazonclouddirectory/2017-01-11/facet/list#x-amz-data-partition |  |
| [**listIncomingTypedLinks**](DefaultApi.md#listIncomingTypedLinks) | **POST** /amazonclouddirectory/2017-01-11/typedlink/incoming#x-amz-data-partition |  |
| [**listIndex**](DefaultApi.md#listIndex) | **POST** /amazonclouddirectory/2017-01-11/index/targets#x-amz-data-partition |  |
| [**listObjectAttributes**](DefaultApi.md#listObjectAttributes) | **POST** /amazonclouddirectory/2017-01-11/object/attributes#x-amz-data-partition |  |
| [**listObjectChildren**](DefaultApi.md#listObjectChildren) | **POST** /amazonclouddirectory/2017-01-11/object/children#x-amz-data-partition |  |
| [**listObjectParentPaths**](DefaultApi.md#listObjectParentPaths) | **POST** /amazonclouddirectory/2017-01-11/object/parentpaths#x-amz-data-partition |  |
| [**listObjectParents**](DefaultApi.md#listObjectParents) | **POST** /amazonclouddirectory/2017-01-11/object/parent#x-amz-data-partition |  |
| [**listObjectPolicies**](DefaultApi.md#listObjectPolicies) | **POST** /amazonclouddirectory/2017-01-11/object/policy#x-amz-data-partition |  |
| [**listOutgoingTypedLinks**](DefaultApi.md#listOutgoingTypedLinks) | **POST** /amazonclouddirectory/2017-01-11/typedlink/outgoing#x-amz-data-partition |  |
| [**listPolicyAttachments**](DefaultApi.md#listPolicyAttachments) | **POST** /amazonclouddirectory/2017-01-11/policy/attachment#x-amz-data-partition |  |
| [**listPublishedSchemaArns**](DefaultApi.md#listPublishedSchemaArns) | **POST** /amazonclouddirectory/2017-01-11/schema/published |  |
| [**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /amazonclouddirectory/2017-01-11/tags |  |
| [**listTypedLinkFacetAttributes**](DefaultApi.md#listTypedLinkFacetAttributes) | **POST** /amazonclouddirectory/2017-01-11/typedlink/facet/attributes#x-amz-data-partition |  |
| [**listTypedLinkFacetNames**](DefaultApi.md#listTypedLinkFacetNames) | **POST** /amazonclouddirectory/2017-01-11/typedlink/facet/list#x-amz-data-partition |  |
| [**lookupPolicy**](DefaultApi.md#lookupPolicy) | **POST** /amazonclouddirectory/2017-01-11/policy/lookup#x-amz-data-partition |  |
| [**publishSchema**](DefaultApi.md#publishSchema) | **PUT** /amazonclouddirectory/2017-01-11/schema/publish#x-amz-data-partition |  |
| [**putSchemaFromJson**](DefaultApi.md#putSchemaFromJson) | **PUT** /amazonclouddirectory/2017-01-11/schema/json#x-amz-data-partition |  |
| [**removeFacetFromObject**](DefaultApi.md#removeFacetFromObject) | **PUT** /amazonclouddirectory/2017-01-11/object/facets/delete#x-amz-data-partition |  |
| [**tagResource**](DefaultApi.md#tagResource) | **PUT** /amazonclouddirectory/2017-01-11/tags/add |  |
| [**untagResource**](DefaultApi.md#untagResource) | **PUT** /amazonclouddirectory/2017-01-11/tags/remove |  |
| [**updateFacet**](DefaultApi.md#updateFacet) | **PUT** /amazonclouddirectory/2017-01-11/facet#x-amz-data-partition |  |
| [**updateLinkAttributes**](DefaultApi.md#updateLinkAttributes) | **POST** /amazonclouddirectory/2017-01-11/typedlink/attributes/update#x-amz-data-partition |  |
| [**updateObjectAttributes**](DefaultApi.md#updateObjectAttributes) | **PUT** /amazonclouddirectory/2017-01-11/object/update#x-amz-data-partition |  |
| [**updateSchema**](DefaultApi.md#updateSchema) | **PUT** /amazonclouddirectory/2017-01-11/schema/update#x-amz-data-partition |  |
| [**updateTypedLinkFacet**](DefaultApi.md#updateTypedLinkFacet) | **PUT** /amazonclouddirectory/2017-01-11/typedlink/facet#x-amz-data-partition |  |
| [**upgradeAppliedSchema**](DefaultApi.md#upgradeAppliedSchema) | **PUT** /amazonclouddirectory/2017-01-11/schema/upgradeapplied |  |
| [**upgradePublishedSchema**](DefaultApi.md#upgradePublishedSchema) | **PUT** /amazonclouddirectory/2017-01-11/schema/upgradepublished |  |


<a id="addFacetToObject"></a>
# **addFacetToObject**
> Object addFacetToObject(xAmzDataPartition, addFacetToObjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Adds a new &lt;a&gt;Facet&lt;/a&gt; to an object. An object can have more than one facet applied on it.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.
    AddFacetToObjectRequest addFacetToObjectRequest = new AddFacetToObjectRequest(); // AddFacetToObjectRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.addFacetToObject(xAmzDataPartition, addFacetToObjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addFacetToObject");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **addFacetToObjectRequest** | [**AddFacetToObjectRequest**](AddFacetToObjectRequest.md)|  | |
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
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | FacetValidationException |  -  |

<a id="applySchema"></a>
# **applySchema**
> ApplySchemaResponse applySchema(xAmzDataPartition, applySchemaRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Copies the input published schema, at the specified version, into the &lt;a&gt;Directory&lt;/a&gt; with the same name and version as that of the published schema.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> into which the schema is copied. For more information, see <a>arns</a>.
    ApplySchemaRequest applySchemaRequest = new ApplySchemaRequest(); // ApplySchemaRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ApplySchemaResponse result = apiInstance.applySchema(xAmzDataPartition, applySchemaRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#applySchema");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; into which the schema is copied. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **applySchemaRequest** | [**ApplySchemaRequest**](ApplySchemaRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ApplySchemaResponse**](ApplySchemaResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | InvalidAttachmentException |  -  |

<a id="attachObject"></a>
# **attachObject**
> AttachObjectResponse attachObject(xAmzDataPartition, attachObjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Attaches an existing object to another object. An object can be accessed in two ways:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Using the path&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Using &lt;code&gt;ObjectIdentifier&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where both objects reside. For more information, see <a>arns</a>.
    AttachObjectRequest attachObjectRequest = new AttachObjectRequest(); // AttachObjectRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      AttachObjectResponse result = apiInstance.attachObject(xAmzDataPartition, attachObjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#attachObject");
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
| **xAmzDataPartition** | **String**| Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where both objects reside. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **attachObjectRequest** | [**AttachObjectRequest**](AttachObjectRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**AttachObjectResponse**](AttachObjectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | LinkNameAlreadyInUseException |  -  |
| **489** | InvalidAttachmentException |  -  |
| **490** | ValidationException |  -  |
| **491** | FacetValidationException |  -  |

<a id="attachPolicy"></a>
# **attachPolicy**
> Object attachPolicy(xAmzDataPartition, attachPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Attaches a policy object to a regular object. An object can have a limited number of attached policies.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where both objects reside. For more information, see <a>arns</a>.
    AttachPolicyRequest attachPolicyRequest = new AttachPolicyRequest(); // AttachPolicyRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.attachPolicy(xAmzDataPartition, attachPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#attachPolicy");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where both objects reside. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **attachPolicyRequest** | [**AttachPolicyRequest**](AttachPolicyRequest.md)|  | |
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
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | NotPolicyException |  -  |

<a id="attachToIndex"></a>
# **attachToIndex**
> AttachToIndexResponse attachToIndex(xAmzDataPartition, attachToIndexRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Attaches the specified object to the specified index.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) of the directory where the object and index exist.
    AttachToIndexRequest attachToIndexRequest = new AttachToIndexRequest(); // AttachToIndexRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      AttachToIndexResponse result = apiInstance.attachToIndex(xAmzDataPartition, attachToIndexRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#attachToIndex");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) of the directory where the object and index exist. | |
| **attachToIndexRequest** | [**AttachToIndexRequest**](AttachToIndexRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**AttachToIndexResponse**](AttachToIndexResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | InvalidAttachmentException |  -  |
| **488** | ResourceNotFoundException |  -  |
| **489** | LinkNameAlreadyInUseException |  -  |
| **490** | IndexedAttributeMissingException |  -  |
| **491** | NotIndexException |  -  |

<a id="attachTypedLink"></a>
# **attachTypedLink**
> AttachTypedLinkResponse attachTypedLink(xAmzDataPartition, attachTypedLinkRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Attaches a typed link to a specified source and target object. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) of the directory where you want to attach the typed link.
    AttachTypedLinkRequest attachTypedLinkRequest = new AttachTypedLinkRequest(); // AttachTypedLinkRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      AttachTypedLinkResponse result = apiInstance.attachTypedLink(xAmzDataPartition, attachTypedLinkRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#attachTypedLink");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) of the directory where you want to attach the typed link. | |
| **attachTypedLinkRequest** | [**AttachTypedLinkRequest**](AttachTypedLinkRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**AttachTypedLinkResponse**](AttachTypedLinkResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | InvalidAttachmentException |  -  |
| **489** | ValidationException |  -  |
| **490** | FacetValidationException |  -  |

<a id="batchRead"></a>
# **batchRead**
> BatchReadResponse batchRead(xAmzDataPartition, batchReadRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzConsistencyLevel)



Performs all the read operations in a batch. 

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a>. For more information, see <a>arns</a>.
    BatchReadRequest batchReadRequest = new BatchReadRequest(); // BatchReadRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzConsistencyLevel = "SERIALIZABLE"; // String | Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
    try {
      BatchReadResponse result = apiInstance.batchRead(xAmzDataPartition, batchReadRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzConsistencyLevel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchRead");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **batchReadRequest** | [**BatchReadRequest**](BatchReadRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzConsistencyLevel** | **String**| Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object. | [optional] [enum: SERIALIZABLE, EVENTUAL] |

### Return type

[**BatchReadResponse**](BatchReadResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |

<a id="batchWrite"></a>
# **batchWrite**
> BatchWriteResponse batchWrite(xAmzDataPartition, batchWriteRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Performs all the write operations in a batch. Either all the operations succeed or none.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a>. For more information, see <a>arns</a>.
    BatchWriteRequest batchWriteRequest = new BatchWriteRequest(); // BatchWriteRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      BatchWriteResponse result = apiInstance.batchWrite(xAmzDataPartition, batchWriteRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchWrite");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **batchWriteRequest** | [**BatchWriteRequest**](BatchWriteRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**BatchWriteResponse**](BatchWriteResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | BatchWriteException |  -  |

<a id="createDirectory"></a>
# **createDirectory**
> CreateDirectoryResponse createDirectory(xAmzDataPartition, createDirectoryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a &lt;a&gt;Directory&lt;/a&gt; by copying the published schema into the directory. A directory cannot be created without a schema.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) of the published schema that will be copied into the data <a>Directory</a>. For more information, see <a>arns</a>.
    CreateDirectoryRequest createDirectoryRequest = new CreateDirectoryRequest(); // CreateDirectoryRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateDirectoryResponse result = apiInstance.createDirectory(xAmzDataPartition, createDirectoryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createDirectory");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) of the published schema that will be copied into the data &lt;a&gt;Directory&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **createDirectoryRequest** | [**CreateDirectoryRequest**](CreateDirectoryRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateDirectoryResponse**](CreateDirectoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryAlreadyExistsException |  -  |
| **487** | ResourceNotFoundException |  -  |

<a id="createFacet"></a>
# **createFacet**
> Object createFacet(xAmzDataPartition, createFacetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a new &lt;a&gt;Facet&lt;/a&gt; in a schema. Facet creation is allowed only in development or applied schemas.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The schema ARN in which the new <a>Facet</a> will be created. For more information, see <a>arns</a>.
    CreateFacetRequest createFacetRequest = new CreateFacetRequest(); // CreateFacetRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.createFacet(xAmzDataPartition, createFacetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createFacet");
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
| **xAmzDataPartition** | **String**| The schema ARN in which the new &lt;a&gt;Facet&lt;/a&gt; will be created. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **createFacetRequest** | [**CreateFacetRequest**](CreateFacetRequest.md)|  | |
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
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | FacetAlreadyExistsException |  -  |
| **488** | InvalidRuleException |  -  |
| **489** | FacetValidationException |  -  |

<a id="createIndex"></a>
# **createIndex**
> CreateIndexResponse createIndex(xAmzDataPartition, createIndexRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates an index object. See &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_indexing.html\&quot;&gt;Indexing&lt;/a&gt; for more information.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the directory where the index should be created.
    CreateIndexRequest createIndexRequest = new CreateIndexRequest(); // CreateIndexRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateIndexResponse result = apiInstance.createIndex(xAmzDataPartition, createIndexRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createIndex");
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
| **xAmzDataPartition** | **String**| The ARN of the directory where the index should be created. | |
| **createIndexRequest** | [**CreateIndexRequest**](CreateIndexRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateIndexResponse**](CreateIndexResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | FacetValidationException |  -  |
| **489** | LinkNameAlreadyInUseException |  -  |
| **490** | UnsupportedIndexTypeException |  -  |

<a id="createObject"></a>
# **createObject**
> CreateObjectResponse createObject(xAmzDataPartition, createObjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates an object in a &lt;a&gt;Directory&lt;/a&gt;. Additionally attaches the object to a parent, if a parent reference and &lt;code&gt;LinkName&lt;/code&gt; is specified. An object is simply a collection of &lt;a&gt;Facet&lt;/a&gt; attributes. You can also use this API call to create a policy object, if the facet from which you create the object is a policy facet. 

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> in which the object will be created. For more information, see <a>arns</a>.
    CreateObjectRequest createObjectRequest = new CreateObjectRequest(); // CreateObjectRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateObjectResponse result = apiInstance.createObject(xAmzDataPartition, createObjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createObject");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; in which the object will be created. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **createObjectRequest** | [**CreateObjectRequest**](CreateObjectRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateObjectResponse**](CreateObjectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | FacetValidationException |  -  |
| **489** | LinkNameAlreadyInUseException |  -  |
| **490** | UnsupportedIndexTypeException |  -  |

<a id="createSchema"></a>
# **createSchema**
> CreateSchemaResponse createSchema(createSchemaRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a new schema in a development state. A schema can exist in three phases:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Development:&lt;/i&gt; This is a mutable phase of the schema. All new schemas are in the development phase. Once the schema is finalized, it can be published.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Published:&lt;/i&gt; Published schemas are immutable and have a version associated with them.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Applied:&lt;/i&gt; Applied schemas are mutable in a way that allows you to add new schema facets. You can also add new, nonrequired attributes to existing schema facets. You can apply only published schemas to directories. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateSchemaRequest createSchemaRequest = new CreateSchemaRequest(); // CreateSchemaRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateSchemaResponse result = apiInstance.createSchema(createSchemaRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createSchema");
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
| **createSchemaRequest** | [**CreateSchemaRequest**](CreateSchemaRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateSchemaResponse**](CreateSchemaResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | SchemaAlreadyExistsException |  -  |
| **487** | AccessDeniedException |  -  |

<a id="createTypedLinkFacet"></a>
# **createTypedLinkFacet**
> Object createTypedLinkFacet(xAmzDataPartition, createTypedLinkFacetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a &lt;a&gt;TypedLinkFacet&lt;/a&gt;. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.
    CreateTypedLinkFacetRequest createTypedLinkFacetRequest = new CreateTypedLinkFacetRequest(); // CreateTypedLinkFacetRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.createTypedLinkFacet(xAmzDataPartition, createTypedLinkFacetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createTypedLinkFacet");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the schema. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **createTypedLinkFacetRequest** | [**CreateTypedLinkFacetRequest**](CreateTypedLinkFacetRequest.md)|  | |
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
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | FacetAlreadyExistsException |  -  |
| **488** | InvalidRuleException |  -  |
| **489** | FacetValidationException |  -  |

<a id="deleteDirectory"></a>
# **deleteDirectory**
> DeleteDirectoryResponse deleteDirectory(xAmzDataPartition, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes a directory. Only disabled directories can be deleted. A deleted directory cannot be undone. Exercise extreme caution when deleting directories.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the directory to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteDirectoryResponse result = apiInstance.deleteDirectory(xAmzDataPartition, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteDirectory");
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
| **xAmzDataPartition** | **String**| The ARN of the directory to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteDirectoryResponse**](DeleteDirectoryResponse.md)

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
| **481** | DirectoryNotDisabledException |  -  |
| **482** | InternalServiceException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryDeletedException |  -  |
| **487** | RetryableConflictException |  -  |
| **488** | InvalidArnException |  -  |

<a id="deleteFacet"></a>
# **deleteFacet**
> Object deleteFacet(xAmzDataPartition, deleteFacetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes a given &lt;a&gt;Facet&lt;/a&gt;. All attributes and &lt;a&gt;Rule&lt;/a&gt;s that are associated with the facet will be deleted. Only development schema facets are allowed deletion.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Facet</a>. For more information, see <a>arns</a>.
    DeleteFacetRequest deleteFacetRequest = new DeleteFacetRequest(); // DeleteFacetRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteFacet(xAmzDataPartition, deleteFacetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteFacet");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Facet&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **deleteFacetRequest** | [**DeleteFacetRequest**](DeleteFacetRequest.md)|  | |
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
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | FacetNotFoundException |  -  |
| **488** | FacetInUseException |  -  |

<a id="deleteObject"></a>
# **deleteObject**
> Object deleteObject(xAmzDataPartition, deleteObjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes an object and its associated attributes. Only objects with no children and no parents can be deleted.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.
    DeleteObjectRequest deleteObjectRequest = new DeleteObjectRequest(); // DeleteObjectRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteObject(xAmzDataPartition, deleteObjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **deleteObjectRequest** | [**DeleteObjectRequest**](DeleteObjectRequest.md)|  | |
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
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | ObjectNotDetachedException |  -  |

<a id="deleteSchema"></a>
# **deleteSchema**
> DeleteSchemaResponse deleteSchema(xAmzDataPartition, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes a given schema. Schemas in a development and published state can only be deleted. 

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) of the development schema. For more information, see <a>arns</a>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteSchemaResponse result = apiInstance.deleteSchema(xAmzDataPartition, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteSchema");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) of the development schema. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteSchemaResponse**](DeleteSchemaResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | StillContainsLinksException |  -  |

<a id="deleteTypedLinkFacet"></a>
# **deleteTypedLinkFacet**
> Object deleteTypedLinkFacet(xAmzDataPartition, deleteTypedLinkFacetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes a &lt;a&gt;TypedLinkFacet&lt;/a&gt;. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.
    DeleteTypedLinkFacetRequest deleteTypedLinkFacetRequest = new DeleteTypedLinkFacetRequest(); // DeleteTypedLinkFacetRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteTypedLinkFacet(xAmzDataPartition, deleteTypedLinkFacetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteTypedLinkFacet");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the schema. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **deleteTypedLinkFacetRequest** | [**DeleteTypedLinkFacetRequest**](DeleteTypedLinkFacetRequest.md)|  | |
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
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | FacetNotFoundException |  -  |

<a id="detachFromIndex"></a>
# **detachFromIndex**
> DetachFromIndexResponse detachFromIndex(xAmzDataPartition, attachToIndexRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Detaches the specified object from the specified index.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) of the directory the index and object exist in.
    AttachToIndexRequest attachToIndexRequest = new AttachToIndexRequest(); // AttachToIndexRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DetachFromIndexResponse result = apiInstance.detachFromIndex(xAmzDataPartition, attachToIndexRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#detachFromIndex");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) of the directory the index and object exist in. | |
| **attachToIndexRequest** | [**AttachToIndexRequest**](AttachToIndexRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DetachFromIndexResponse**](DetachFromIndexResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | ObjectAlreadyDetachedException |  -  |
| **489** | NotIndexException |  -  |

<a id="detachObject"></a>
# **detachObject**
> DetachObjectResponse detachObject(xAmzDataPartition, detachObjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Detaches a given object from the parent object. The object that is to be detached from the parent is specified by the link name.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where objects reside. For more information, see <a>arns</a>.
    DetachObjectRequest detachObjectRequest = new DetachObjectRequest(); // DetachObjectRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DetachObjectResponse result = apiInstance.detachObject(xAmzDataPartition, detachObjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#detachObject");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where objects reside. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **detachObjectRequest** | [**DetachObjectRequest**](DetachObjectRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DetachObjectResponse**](DetachObjectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | NotNodeException |  -  |

<a id="detachPolicy"></a>
# **detachPolicy**
> Object detachPolicy(xAmzDataPartition, attachPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Detaches a policy from an object.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where both objects reside. For more information, see <a>arns</a>.
    AttachPolicyRequest attachPolicyRequest = new AttachPolicyRequest(); // AttachPolicyRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.detachPolicy(xAmzDataPartition, attachPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#detachPolicy");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where both objects reside. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **attachPolicyRequest** | [**AttachPolicyRequest**](AttachPolicyRequest.md)|  | |
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
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | NotPolicyException |  -  |

<a id="detachTypedLink"></a>
# **detachTypedLink**
> detachTypedLink(xAmzDataPartition, detachTypedLinkRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Detaches a typed link from a specified source and target object. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) of the directory where you want to detach the typed link.
    DetachTypedLinkRequest detachTypedLinkRequest = new DetachTypedLinkRequest(); // DetachTypedLinkRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.detachTypedLink(xAmzDataPartition, detachTypedLinkRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#detachTypedLink");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) of the directory where you want to detach the typed link. | |
| **detachTypedLinkRequest** | [**DetachTypedLinkRequest**](DetachTypedLinkRequest.md)|  | |
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
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | FacetValidationException |  -  |

<a id="disableDirectory"></a>
# **disableDirectory**
> DisableDirectoryResponse disableDirectory(xAmzDataPartition, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Disables the specified directory. Disabled directories cannot be read or written to. Only enabled directories can be disabled. Disabled directories may be reenabled.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the directory to disable.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DisableDirectoryResponse result = apiInstance.disableDirectory(xAmzDataPartition, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#disableDirectory");
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
| **xAmzDataPartition** | **String**| The ARN of the directory to disable. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DisableDirectoryResponse**](DisableDirectoryResponse.md)

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
| **481** | DirectoryDeletedException |  -  |
| **482** | InternalServiceException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | RetryableConflictException |  -  |
| **487** | InvalidArnException |  -  |

<a id="enableDirectory"></a>
# **enableDirectory**
> EnableDirectoryResponse enableDirectory(xAmzDataPartition, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Enables the specified directory. Only disabled directories can be enabled. Once enabled, the directory can then be read and written to.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the directory to enable.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      EnableDirectoryResponse result = apiInstance.enableDirectory(xAmzDataPartition, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#enableDirectory");
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
| **xAmzDataPartition** | **String**| The ARN of the directory to enable. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**EnableDirectoryResponse**](EnableDirectoryResponse.md)

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
| **481** | DirectoryDeletedException |  -  |
| **482** | InternalServiceException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | RetryableConflictException |  -  |
| **487** | InvalidArnException |  -  |

<a id="getAppliedSchemaVersion"></a>
# **getAppliedSchemaVersion**
> GetAppliedSchemaVersionResponse getAppliedSchemaVersion(getAppliedSchemaVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Returns current applied schema version ARN, including the minor version in use.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    GetAppliedSchemaVersionRequest getAppliedSchemaVersionRequest = new GetAppliedSchemaVersionRequest(); // GetAppliedSchemaVersionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetAppliedSchemaVersionResponse result = apiInstance.getAppliedSchemaVersion(getAppliedSchemaVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAppliedSchemaVersion");
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
| **getAppliedSchemaVersionRequest** | [**GetAppliedSchemaVersionRequest**](GetAppliedSchemaVersionRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetAppliedSchemaVersionResponse**](GetAppliedSchemaVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |

<a id="getDirectory"></a>
# **getDirectory**
> GetDirectoryResponse getDirectory(xAmzDataPartition, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves metadata about a directory.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the directory.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetDirectoryResponse result = apiInstance.getDirectory(xAmzDataPartition, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDirectory");
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
| **xAmzDataPartition** | **String**| The ARN of the directory. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetDirectoryResponse**](GetDirectoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |

<a id="getFacet"></a>
# **getFacet**
> GetFacetResponse getFacet(xAmzDataPartition, getFacetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets details of the &lt;a&gt;Facet&lt;/a&gt;, such as facet name, attributes, &lt;a&gt;Rule&lt;/a&gt;s, or &lt;code&gt;ObjectType&lt;/code&gt;. You can call this on all kinds of schema facets -- published, development, or applied.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Facet</a>. For more information, see <a>arns</a>.
    GetFacetRequest getFacetRequest = new GetFacetRequest(); // GetFacetRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetFacetResponse result = apiInstance.getFacet(xAmzDataPartition, getFacetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFacet");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Facet&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **getFacetRequest** | [**GetFacetRequest**](GetFacetRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetFacetResponse**](GetFacetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | FacetNotFoundException |  -  |

<a id="getLinkAttributes"></a>
# **getLinkAttributes**
> GetLinkAttributesResponse getLinkAttributes(xAmzDataPartition, getLinkAttributesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves attributes that are associated with a typed link.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the Directory where the typed link resides. For more information, see <a>arns</a> or <a href=\"http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\">Typed link</a>.
    GetLinkAttributesRequest getLinkAttributesRequest = new GetLinkAttributesRequest(); // GetLinkAttributesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetLinkAttributesResponse result = apiInstance.getLinkAttributes(xAmzDataPartition, getLinkAttributesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getLinkAttributes");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the Directory where the typed link resides. For more information, see &lt;a&gt;arns&lt;/a&gt; or &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;. | |
| **getLinkAttributesRequest** | [**GetLinkAttributesRequest**](GetLinkAttributesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetLinkAttributesResponse**](GetLinkAttributesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | FacetValidationException |  -  |

<a id="getObjectAttributes"></a>
# **getObjectAttributes**
> GetObjectAttributesResponse getObjectAttributes(xAmzDataPartition, getObjectAttributesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzConsistencyLevel)



Retrieves attributes within a facet that are associated with an object.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides.
    GetObjectAttributesRequest getObjectAttributesRequest = new GetObjectAttributesRequest(); // GetObjectAttributesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzConsistencyLevel = "SERIALIZABLE"; // String | The consistency level at which to retrieve the attributes on an object.
    try {
      GetObjectAttributesResponse result = apiInstance.getObjectAttributes(xAmzDataPartition, getObjectAttributesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzConsistencyLevel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getObjectAttributes");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides. | |
| **getObjectAttributesRequest** | [**GetObjectAttributesRequest**](GetObjectAttributesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzConsistencyLevel** | **String**| The consistency level at which to retrieve the attributes on an object. | [optional] [enum: SERIALIZABLE, EVENTUAL] |

### Return type

[**GetObjectAttributesResponse**](GetObjectAttributesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | FacetValidationException |  -  |

<a id="getObjectInformation"></a>
# **getObjectInformation**
> GetObjectInformationResponse getObjectInformation(xAmzDataPartition, deleteObjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzConsistencyLevel)



Retrieves metadata about an object.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the directory being retrieved.
    DeleteObjectRequest deleteObjectRequest = new DeleteObjectRequest(); // DeleteObjectRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzConsistencyLevel = "SERIALIZABLE"; // String | The consistency level at which to retrieve the object information.
    try {
      GetObjectInformationResponse result = apiInstance.getObjectInformation(xAmzDataPartition, deleteObjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzConsistencyLevel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getObjectInformation");
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
| **xAmzDataPartition** | **String**| The ARN of the directory being retrieved. | |
| **deleteObjectRequest** | [**DeleteObjectRequest**](DeleteObjectRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzConsistencyLevel** | **String**| The consistency level at which to retrieve the object information. | [optional] [enum: SERIALIZABLE, EVENTUAL] |

### Return type

[**GetObjectInformationResponse**](GetObjectInformationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |

<a id="getSchemaAsJson"></a>
# **getSchemaAsJson**
> GetSchemaAsJsonResponse getSchemaAsJson(xAmzDataPartition, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves a JSON representation of the schema. See &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_schemas.html#jsonformat\&quot;&gt;JSON Schema Format&lt;/a&gt; for more information.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the schema to retrieve.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetSchemaAsJsonResponse result = apiInstance.getSchemaAsJson(xAmzDataPartition, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSchemaAsJson");
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
| **xAmzDataPartition** | **String**| The ARN of the schema to retrieve. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetSchemaAsJsonResponse**](GetSchemaAsJsonResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | ValidationException |  -  |

<a id="getTypedLinkFacetInformation"></a>
# **getTypedLinkFacetInformation**
> GetTypedLinkFacetInformationResponse getTypedLinkFacetInformation(xAmzDataPartition, deleteTypedLinkFacetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Returns the identity attribute order for a specific &lt;a&gt;TypedLinkFacet&lt;/a&gt;. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.
    DeleteTypedLinkFacetRequest deleteTypedLinkFacetRequest = new DeleteTypedLinkFacetRequest(); // DeleteTypedLinkFacetRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetTypedLinkFacetInformationResponse result = apiInstance.getTypedLinkFacetInformation(xAmzDataPartition, deleteTypedLinkFacetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getTypedLinkFacetInformation");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the schema. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **deleteTypedLinkFacetRequest** | [**DeleteTypedLinkFacetRequest**](DeleteTypedLinkFacetRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetTypedLinkFacetInformationResponse**](GetTypedLinkFacetInformationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | InvalidNextTokenException |  -  |
| **488** | FacetNotFoundException |  -  |

<a id="listAppliedSchemaArns"></a>
# **listAppliedSchemaArns**
> ListAppliedSchemaArnsResponse listAppliedSchemaArns(listAppliedSchemaArnsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Lists schema major versions applied to a directory. If &lt;code&gt;SchemaArn&lt;/code&gt; is provided, lists the minor version.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ListAppliedSchemaArnsRequest listAppliedSchemaArnsRequest = new ListAppliedSchemaArnsRequest(); // ListAppliedSchemaArnsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListAppliedSchemaArnsResponse result = apiInstance.listAppliedSchemaArns(listAppliedSchemaArnsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAppliedSchemaArns");
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
| **listAppliedSchemaArnsRequest** | [**ListAppliedSchemaArnsRequest**](ListAppliedSchemaArnsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListAppliedSchemaArnsResponse**](ListAppliedSchemaArnsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | InvalidNextTokenException |  -  |

<a id="listAttachedIndices"></a>
# **listAttachedIndices**
> ListAttachedIndicesResponse listAttachedIndices(xAmzDataPartition, listAttachedIndicesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzConsistencyLevel, maxResults, nextToken)



Lists indices attached to the specified object.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the directory.
    ListAttachedIndicesRequest listAttachedIndicesRequest = new ListAttachedIndicesRequest(); // ListAttachedIndicesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzConsistencyLevel = "SERIALIZABLE"; // String | The consistency level to use for this operation.
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListAttachedIndicesResponse result = apiInstance.listAttachedIndices(xAmzDataPartition, listAttachedIndicesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzConsistencyLevel, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAttachedIndices");
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
| **xAmzDataPartition** | **String**| The ARN of the directory. | |
| **listAttachedIndicesRequest** | [**ListAttachedIndicesRequest**](ListAttachedIndicesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzConsistencyLevel** | **String**| The consistency level to use for this operation. | [optional] [enum: SERIALIZABLE, EVENTUAL] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListAttachedIndicesResponse**](ListAttachedIndicesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |

<a id="listDevelopmentSchemaArns"></a>
# **listDevelopmentSchemaArns**
> ListDevelopmentSchemaArnsResponse listDevelopmentSchemaArns(listDevelopmentSchemaArnsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Retrieves each Amazon Resource Name (ARN) of schemas in the development state.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ListDevelopmentSchemaArnsRequest listDevelopmentSchemaArnsRequest = new ListDevelopmentSchemaArnsRequest(); // ListDevelopmentSchemaArnsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListDevelopmentSchemaArnsResponse result = apiInstance.listDevelopmentSchemaArns(listDevelopmentSchemaArnsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listDevelopmentSchemaArns");
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
| **listDevelopmentSchemaArnsRequest** | [**ListDevelopmentSchemaArnsRequest**](ListDevelopmentSchemaArnsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListDevelopmentSchemaArnsResponse**](ListDevelopmentSchemaArnsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | InvalidNextTokenException |  -  |

<a id="listDirectories"></a>
# **listDirectories**
> ListDirectoriesResponse listDirectories(listDirectoriesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Lists directories created within an account.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ListDirectoriesRequest listDirectoriesRequest = new ListDirectoriesRequest(); // ListDirectoriesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListDirectoriesResponse result = apiInstance.listDirectories(listDirectoriesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listDirectories");
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
| **listDirectoriesRequest** | [**ListDirectoriesRequest**](ListDirectoriesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListDirectoriesResponse**](ListDirectoriesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | InvalidNextTokenException |  -  |

<a id="listFacetAttributes"></a>
# **listFacetAttributes**
> ListFacetAttributesResponse listFacetAttributes(xAmzDataPartition, listFacetAttributesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Retrieves attributes attached to the facet.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the schema where the facet resides.
    ListFacetAttributesRequest listFacetAttributesRequest = new ListFacetAttributesRequest(); // ListFacetAttributesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListFacetAttributesResponse result = apiInstance.listFacetAttributes(xAmzDataPartition, listFacetAttributesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listFacetAttributes");
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
| **xAmzDataPartition** | **String**| The ARN of the schema where the facet resides. | |
| **listFacetAttributesRequest** | [**ListFacetAttributesRequest**](ListFacetAttributesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListFacetAttributesResponse**](ListFacetAttributesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | FacetNotFoundException |  -  |
| **488** | InvalidNextTokenException |  -  |

<a id="listFacetNames"></a>
# **listFacetNames**
> ListFacetNamesResponse listFacetNames(xAmzDataPartition, listDevelopmentSchemaArnsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Retrieves the names of facets that exist in a schema.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) to retrieve facet names from.
    ListDevelopmentSchemaArnsRequest listDevelopmentSchemaArnsRequest = new ListDevelopmentSchemaArnsRequest(); // ListDevelopmentSchemaArnsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListFacetNamesResponse result = apiInstance.listFacetNames(xAmzDataPartition, listDevelopmentSchemaArnsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listFacetNames");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) to retrieve facet names from. | |
| **listDevelopmentSchemaArnsRequest** | [**ListDevelopmentSchemaArnsRequest**](ListDevelopmentSchemaArnsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListFacetNamesResponse**](ListFacetNamesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | InvalidNextTokenException |  -  |

<a id="listIncomingTypedLinks"></a>
# **listIncomingTypedLinks**
> ListIncomingTypedLinksResponse listIncomingTypedLinks(xAmzDataPartition, listIncomingTypedLinksRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Returns a paginated list of all the incoming &lt;a&gt;TypedLinkSpecifier&lt;/a&gt; information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) of the directory where you want to list the typed links.
    ListIncomingTypedLinksRequest listIncomingTypedLinksRequest = new ListIncomingTypedLinksRequest(); // ListIncomingTypedLinksRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListIncomingTypedLinksResponse result = apiInstance.listIncomingTypedLinks(xAmzDataPartition, listIncomingTypedLinksRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listIncomingTypedLinks");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) of the directory where you want to list the typed links. | |
| **listIncomingTypedLinksRequest** | [**ListIncomingTypedLinksRequest**](ListIncomingTypedLinksRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListIncomingTypedLinksResponse**](ListIncomingTypedLinksResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | InvalidNextTokenException |  -  |
| **489** | FacetValidationException |  -  |

<a id="listIndex"></a>
# **listIndex**
> ListIndexResponse listIndex(xAmzDataPartition, listIndexRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzConsistencyLevel, maxResults, nextToken)



Lists objects attached to the specified index.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the directory that the index exists in.
    ListIndexRequest listIndexRequest = new ListIndexRequest(); // ListIndexRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzConsistencyLevel = "SERIALIZABLE"; // String | The consistency level to execute the request at.
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListIndexResponse result = apiInstance.listIndex(xAmzDataPartition, listIndexRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzConsistencyLevel, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listIndex");
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
| **xAmzDataPartition** | **String**| The ARN of the directory that the index exists in. | |
| **listIndexRequest** | [**ListIndexRequest**](ListIndexRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzConsistencyLevel** | **String**| The consistency level to execute the request at. | [optional] [enum: SERIALIZABLE, EVENTUAL] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListIndexResponse**](ListIndexResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | FacetValidationException |  -  |
| **484** | ValidationException |  -  |
| **485** | LimitExceededException |  -  |
| **486** | AccessDeniedException |  -  |
| **487** | DirectoryNotEnabledException |  -  |
| **488** | InvalidNextTokenException |  -  |
| **489** | ResourceNotFoundException |  -  |
| **490** | NotIndexException |  -  |

<a id="listObjectAttributes"></a>
# **listObjectAttributes**
> ListObjectAttributesResponse listObjectAttributes(xAmzDataPartition, listObjectAttributesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzConsistencyLevel, maxResults, nextToken)



Lists all attributes that are associated with an object. 

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.
    ListObjectAttributesRequest listObjectAttributesRequest = new ListObjectAttributesRequest(); // ListObjectAttributesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzConsistencyLevel = "SERIALIZABLE"; // String | Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListObjectAttributesResponse result = apiInstance.listObjectAttributes(xAmzDataPartition, listObjectAttributesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzConsistencyLevel, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listObjectAttributes");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **listObjectAttributesRequest** | [**ListObjectAttributesRequest**](ListObjectAttributesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzConsistencyLevel** | **String**| Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object. | [optional] [enum: SERIALIZABLE, EVENTUAL] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListObjectAttributesResponse**](ListObjectAttributesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | InvalidNextTokenException |  -  |
| **489** | FacetValidationException |  -  |

<a id="listObjectChildren"></a>
# **listObjectChildren**
> ListObjectChildrenResponse listObjectChildren(xAmzDataPartition, listObjectChildrenRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzConsistencyLevel, maxResults, nextToken)



Returns a paginated list of child objects that are associated with a given object.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.
    ListObjectChildrenRequest listObjectChildrenRequest = new ListObjectChildrenRequest(); // ListObjectChildrenRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzConsistencyLevel = "SERIALIZABLE"; // String | Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListObjectChildrenResponse result = apiInstance.listObjectChildren(xAmzDataPartition, listObjectChildrenRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzConsistencyLevel, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listObjectChildren");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **listObjectChildrenRequest** | [**ListObjectChildrenRequest**](ListObjectChildrenRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzConsistencyLevel** | **String**| Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object. | [optional] [enum: SERIALIZABLE, EVENTUAL] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListObjectChildrenResponse**](ListObjectChildrenResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | InvalidNextTokenException |  -  |
| **489** | NotNodeException |  -  |

<a id="listObjectParentPaths"></a>
# **listObjectParentPaths**
> ListObjectParentPathsResponse listObjectParentPaths(xAmzDataPartition, listObjectChildrenRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



&lt;p&gt;Retrieves all available parent paths for any object type such as node, leaf node, policy node, and index node objects. For more information about objects, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_key_concepts.html#dirstructure\&quot;&gt;Directory Structure&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Use this API to evaluate all parents for an object. The call returns all objects from the root of the directory up to the requested object. The API returns the number of paths based on user-defined &lt;code&gt;MaxResults&lt;/code&gt;, in case there are multiple paths to the parent. The order of the paths and nodes returned is consistent among multiple API calls unless the objects are deleted or moved. Paths not leading to the directory root are ignored from the target object.&lt;/p&gt;

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the directory to which the parent path applies.
    ListObjectChildrenRequest listObjectChildrenRequest = new ListObjectChildrenRequest(); // ListObjectChildrenRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListObjectParentPathsResponse result = apiInstance.listObjectParentPaths(xAmzDataPartition, listObjectChildrenRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listObjectParentPaths");
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
| **xAmzDataPartition** | **String**| The ARN of the directory to which the parent path applies. | |
| **listObjectChildrenRequest** | [**ListObjectChildrenRequest**](ListObjectChildrenRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListObjectParentPathsResponse**](ListObjectParentPathsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | InvalidNextTokenException |  -  |
| **488** | ResourceNotFoundException |  -  |

<a id="listObjectParents"></a>
# **listObjectParents**
> ListObjectParentsResponse listObjectParents(xAmzDataPartition, listObjectChildrenRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzConsistencyLevel, maxResults, nextToken)



Lists parent objects that are associated with a given object in pagination fashion.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.
    ListObjectChildrenRequest listObjectChildrenRequest = new ListObjectChildrenRequest(); // ListObjectChildrenRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzConsistencyLevel = "SERIALIZABLE"; // String | Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListObjectParentsResponse result = apiInstance.listObjectParents(xAmzDataPartition, listObjectChildrenRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzConsistencyLevel, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listObjectParents");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **listObjectChildrenRequest** | [**ListObjectChildrenRequest**](ListObjectChildrenRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzConsistencyLevel** | **String**| Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object. | [optional] [enum: SERIALIZABLE, EVENTUAL] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListObjectParentsResponse**](ListObjectParentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | InvalidNextTokenException |  -  |
| **489** | CannotListParentOfRootException |  -  |

<a id="listObjectPolicies"></a>
# **listObjectPolicies**
> ListObjectPoliciesResponse listObjectPolicies(xAmzDataPartition, listObjectChildrenRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzConsistencyLevel, maxResults, nextToken)



Returns policies attached to an object in pagination fashion.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where objects reside. For more information, see <a>arns</a>.
    ListObjectChildrenRequest listObjectChildrenRequest = new ListObjectChildrenRequest(); // ListObjectChildrenRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzConsistencyLevel = "SERIALIZABLE"; // String | Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListObjectPoliciesResponse result = apiInstance.listObjectPolicies(xAmzDataPartition, listObjectChildrenRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzConsistencyLevel, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listObjectPolicies");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where objects reside. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **listObjectChildrenRequest** | [**ListObjectChildrenRequest**](ListObjectChildrenRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzConsistencyLevel** | **String**| Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object. | [optional] [enum: SERIALIZABLE, EVENTUAL] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListObjectPoliciesResponse**](ListObjectPoliciesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | InvalidNextTokenException |  -  |

<a id="listOutgoingTypedLinks"></a>
# **listOutgoingTypedLinks**
> ListOutgoingTypedLinksResponse listOutgoingTypedLinks(xAmzDataPartition, listIncomingTypedLinksRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Returns a paginated list of all the outgoing &lt;a&gt;TypedLinkSpecifier&lt;/a&gt; information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) of the directory where you want to list the typed links.
    ListIncomingTypedLinksRequest listIncomingTypedLinksRequest = new ListIncomingTypedLinksRequest(); // ListIncomingTypedLinksRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListOutgoingTypedLinksResponse result = apiInstance.listOutgoingTypedLinks(xAmzDataPartition, listIncomingTypedLinksRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listOutgoingTypedLinks");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) of the directory where you want to list the typed links. | |
| **listIncomingTypedLinksRequest** | [**ListIncomingTypedLinksRequest**](ListIncomingTypedLinksRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListOutgoingTypedLinksResponse**](ListOutgoingTypedLinksResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | InvalidNextTokenException |  -  |
| **489** | FacetValidationException |  -  |

<a id="listPolicyAttachments"></a>
# **listPolicyAttachments**
> ListPolicyAttachmentsResponse listPolicyAttachments(xAmzDataPartition, listPolicyAttachmentsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzConsistencyLevel, maxResults, nextToken)



Returns all of the &lt;code&gt;ObjectIdentifiers&lt;/code&gt; to which a given policy is attached.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where objects reside. For more information, see <a>arns</a>.
    ListPolicyAttachmentsRequest listPolicyAttachmentsRequest = new ListPolicyAttachmentsRequest(); // ListPolicyAttachmentsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzConsistencyLevel = "SERIALIZABLE"; // String | Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListPolicyAttachmentsResponse result = apiInstance.listPolicyAttachments(xAmzDataPartition, listPolicyAttachmentsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzConsistencyLevel, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listPolicyAttachments");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where objects reside. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **listPolicyAttachmentsRequest** | [**ListPolicyAttachmentsRequest**](ListPolicyAttachmentsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzConsistencyLevel** | **String**| Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object. | [optional] [enum: SERIALIZABLE, EVENTUAL] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListPolicyAttachmentsResponse**](ListPolicyAttachmentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | InvalidNextTokenException |  -  |
| **488** | ResourceNotFoundException |  -  |
| **489** | NotPolicyException |  -  |

<a id="listPublishedSchemaArns"></a>
# **listPublishedSchemaArns**
> ListPublishedSchemaArnsResponse listPublishedSchemaArns(listPublishedSchemaArnsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Lists the major version families of each published schema. If a major version ARN is provided as &lt;code&gt;SchemaArn&lt;/code&gt;, the minor version revisions in that family are listed instead.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ListPublishedSchemaArnsRequest listPublishedSchemaArnsRequest = new ListPublishedSchemaArnsRequest(); // ListPublishedSchemaArnsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListPublishedSchemaArnsResponse result = apiInstance.listPublishedSchemaArns(listPublishedSchemaArnsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listPublishedSchemaArns");
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
| **listPublishedSchemaArnsRequest** | [**ListPublishedSchemaArnsRequest**](ListPublishedSchemaArnsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListPublishedSchemaArnsResponse**](ListPublishedSchemaArnsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | InvalidNextTokenException |  -  |

<a id="listTagsForResource"></a>
# **listTagsForResource**
> ListTagsForResourceResponse listTagsForResource(listTagsForResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Returns tags for a resource. Tagging is currently supported only for directories with a limit of 50 tags per directory. All 50 tags are returned for a given directory with this API call.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ListTagsForResourceRequest listTagsForResourceRequest = new ListTagsForResourceRequest(); // ListTagsForResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListTagsForResourceResponse result = apiInstance.listTagsForResource(listTagsForResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTagsForResource");
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
| **listTagsForResourceRequest** | [**ListTagsForResourceRequest**](ListTagsForResourceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | InvalidTaggingRequestException |  -  |

<a id="listTypedLinkFacetAttributes"></a>
# **listTypedLinkFacetAttributes**
> ListTypedLinkFacetAttributesResponse listTypedLinkFacetAttributes(xAmzDataPartition, listTypedLinkFacetAttributesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Returns a paginated list of all attribute definitions for a particular &lt;a&gt;TypedLinkFacet&lt;/a&gt;. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.
    ListTypedLinkFacetAttributesRequest listTypedLinkFacetAttributesRequest = new ListTypedLinkFacetAttributesRequest(); // ListTypedLinkFacetAttributesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListTypedLinkFacetAttributesResponse result = apiInstance.listTypedLinkFacetAttributes(xAmzDataPartition, listTypedLinkFacetAttributesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTypedLinkFacetAttributes");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the schema. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **listTypedLinkFacetAttributesRequest** | [**ListTypedLinkFacetAttributesRequest**](ListTypedLinkFacetAttributesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListTypedLinkFacetAttributesResponse**](ListTypedLinkFacetAttributesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | FacetNotFoundException |  -  |
| **488** | InvalidNextTokenException |  -  |

<a id="listTypedLinkFacetNames"></a>
# **listTypedLinkFacetNames**
> ListTypedLinkFacetNamesResponse listTypedLinkFacetNames(xAmzDataPartition, listDevelopmentSchemaArnsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Returns a paginated list of &lt;code&gt;TypedLink&lt;/code&gt; facet names for a particular schema. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.
    ListDevelopmentSchemaArnsRequest listDevelopmentSchemaArnsRequest = new ListDevelopmentSchemaArnsRequest(); // ListDevelopmentSchemaArnsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListTypedLinkFacetNamesResponse result = apiInstance.listTypedLinkFacetNames(xAmzDataPartition, listDevelopmentSchemaArnsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTypedLinkFacetNames");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the schema. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **listDevelopmentSchemaArnsRequest** | [**ListDevelopmentSchemaArnsRequest**](ListDevelopmentSchemaArnsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListTypedLinkFacetNamesResponse**](ListTypedLinkFacetNamesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | InvalidNextTokenException |  -  |

<a id="lookupPolicy"></a>
# **lookupPolicy**
> LookupPolicyResponse lookupPolicy(xAmzDataPartition, lookupPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Lists all policies from the root of the &lt;a&gt;Directory&lt;/a&gt; to the object specified. If there are no policies present, an empty list is returned. If policies are present, and if some objects don&#39;t have the policies attached, it returns the &lt;code&gt;ObjectIdentifier&lt;/code&gt; for such objects. If policies are present, it returns &lt;code&gt;ObjectIdentifier&lt;/code&gt;, &lt;code&gt;policyId&lt;/code&gt;, and &lt;code&gt;policyType&lt;/code&gt;. Paths that don&#39;t lead to the root from the target object are ignored. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_key_concepts.html#policies\&quot;&gt;Policies&lt;/a&gt;.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a>. For more information, see <a>arns</a>.
    LookupPolicyRequest lookupPolicyRequest = new LookupPolicyRequest(); // LookupPolicyRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      LookupPolicyResponse result = apiInstance.lookupPolicy(xAmzDataPartition, lookupPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#lookupPolicy");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **lookupPolicyRequest** | [**LookupPolicyRequest**](LookupPolicyRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**LookupPolicyResponse**](LookupPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | InvalidNextTokenException |  -  |
| **488** | ResourceNotFoundException |  -  |

<a id="publishSchema"></a>
# **publishSchema**
> PublishSchemaResponse publishSchema(xAmzDataPartition, publishSchemaRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Publishes a development schema with a major version and a recommended minor version.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the development schema. For more information, see <a>arns</a>.
    PublishSchemaRequest publishSchemaRequest = new PublishSchemaRequest(); // PublishSchemaRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PublishSchemaResponse result = apiInstance.publishSchema(xAmzDataPartition, publishSchemaRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#publishSchema");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the development schema. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **publishSchemaRequest** | [**PublishSchemaRequest**](PublishSchemaRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PublishSchemaResponse**](PublishSchemaResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | SchemaAlreadyPublishedException |  -  |

<a id="putSchemaFromJson"></a>
# **putSchemaFromJson**
> PutSchemaFromJsonResponse putSchemaFromJson(xAmzDataPartition, putSchemaFromJsonRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Allows a schema to be updated using JSON upload. Only available for development schemas. See &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_schemas.html#jsonformat\&quot;&gt;JSON Schema Format&lt;/a&gt; for more information.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the schema to update.
    PutSchemaFromJsonRequest putSchemaFromJsonRequest = new PutSchemaFromJsonRequest(); // PutSchemaFromJsonRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutSchemaFromJsonResponse result = apiInstance.putSchemaFromJson(xAmzDataPartition, putSchemaFromJsonRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putSchemaFromJson");
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
| **xAmzDataPartition** | **String**| The ARN of the schema to update. | |
| **putSchemaFromJsonRequest** | [**PutSchemaFromJsonRequest**](PutSchemaFromJsonRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutSchemaFromJsonResponse**](PutSchemaFromJsonResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | InvalidSchemaDocException |  -  |
| **487** | InvalidRuleException |  -  |

<a id="removeFacetFromObject"></a>
# **removeFacetFromObject**
> Object removeFacetFromObject(xAmzDataPartition, removeFacetFromObjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Removes the specified facet from the specified object.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the directory in which the object resides.
    RemoveFacetFromObjectRequest removeFacetFromObjectRequest = new RemoveFacetFromObjectRequest(); // RemoveFacetFromObjectRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.removeFacetFromObject(xAmzDataPartition, removeFacetFromObjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeFacetFromObject");
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
| **xAmzDataPartition** | **String**| The ARN of the directory in which the object resides. | |
| **removeFacetFromObjectRequest** | [**RemoveFacetFromObjectRequest**](RemoveFacetFromObjectRequest.md)|  | |
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
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | FacetValidationException |  -  |

<a id="tagResource"></a>
# **tagResource**
> Object tagResource(tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



An API operation for adding tags to a resource.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    TagResourceRequest tagResourceRequest = new TagResourceRequest(); // TagResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.tagResource(tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagResource");
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
| **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | |
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
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | InvalidTaggingRequestException |  -  |

<a id="untagResource"></a>
# **untagResource**
> Object untagResource(untagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



An API operation for removing tags from a resource.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UntagResourceRequest untagResourceRequest = new UntagResourceRequest(); // UntagResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.untagResource(untagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#untagResource");
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
| **untagResourceRequest** | [**UntagResourceRequest**](UntagResourceRequest.md)|  | |
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
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | InvalidTaggingRequestException |  -  |

<a id="updateFacet"></a>
# **updateFacet**
> Object updateFacet(xAmzDataPartition, updateFacetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Does the following:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Adds new &lt;code&gt;Attributes&lt;/code&gt;, &lt;code&gt;Rules&lt;/code&gt;, or &lt;code&gt;ObjectTypes&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Updates existing &lt;code&gt;Attributes&lt;/code&gt;, &lt;code&gt;Rules&lt;/code&gt;, or &lt;code&gt;ObjectTypes&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Deletes existing &lt;code&gt;Attributes&lt;/code&gt;, &lt;code&gt;Rules&lt;/code&gt;, or &lt;code&gt;ObjectTypes&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Facet</a>. For more information, see <a>arns</a>.
    UpdateFacetRequest updateFacetRequest = new UpdateFacetRequest(); // UpdateFacetRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.updateFacet(xAmzDataPartition, updateFacetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateFacet");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Facet&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **updateFacetRequest** | [**UpdateFacetRequest**](UpdateFacetRequest.md)|  | |
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
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | InvalidFacetUpdateException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | FacetNotFoundException |  -  |
| **489** | InvalidRuleException |  -  |

<a id="updateLinkAttributes"></a>
# **updateLinkAttributes**
> Object updateLinkAttributes(xAmzDataPartition, updateLinkAttributesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates a given typed link’s attributes. Attributes to be updated must not contribute to the typed link’s identity, as defined by its &lt;code&gt;IdentityAttributeOrder&lt;/code&gt;.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the Directory where the updated typed link resides. For more information, see <a>arns</a> or <a href=\"http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\">Typed link</a>.
    UpdateLinkAttributesRequest updateLinkAttributesRequest = new UpdateLinkAttributesRequest(); // UpdateLinkAttributesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.updateLinkAttributes(xAmzDataPartition, updateLinkAttributesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateLinkAttributes");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the Directory where the updated typed link resides. For more information, see &lt;a&gt;arns&lt;/a&gt; or &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;. | |
| **updateLinkAttributesRequest** | [**UpdateLinkAttributesRequest**](UpdateLinkAttributesRequest.md)|  | |
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
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | FacetValidationException |  -  |

<a id="updateObjectAttributes"></a>
# **updateObjectAttributes**
> UpdateObjectAttributesResponse updateObjectAttributes(xAmzDataPartition, updateObjectAttributesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates a given object&#39;s attributes.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.
    UpdateObjectAttributesRequest updateObjectAttributesRequest = new UpdateObjectAttributesRequest(); // UpdateObjectAttributesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateObjectAttributesResponse result = apiInstance.updateObjectAttributes(xAmzDataPartition, updateObjectAttributesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateObjectAttributes");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **updateObjectAttributesRequest** | [**UpdateObjectAttributesRequest**](UpdateObjectAttributesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateObjectAttributesResponse**](UpdateObjectAttributesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | DirectoryNotEnabledException |  -  |
| **487** | ResourceNotFoundException |  -  |
| **488** | LinkNameAlreadyInUseException |  -  |
| **489** | FacetValidationException |  -  |

<a id="updateSchema"></a>
# **updateSchema**
> UpdateSchemaResponse updateSchema(xAmzDataPartition, updateSchemaRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates the schema name with a new name. Only development schema names can be updated.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) of the development schema. For more information, see <a>arns</a>.
    UpdateSchemaRequest updateSchemaRequest = new UpdateSchemaRequest(); // UpdateSchemaRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateSchemaResponse result = apiInstance.updateSchema(xAmzDataPartition, updateSchemaRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateSchema");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) of the development schema. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **updateSchemaRequest** | [**UpdateSchemaRequest**](UpdateSchemaRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateSchemaResponse**](UpdateSchemaResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |

<a id="updateTypedLinkFacet"></a>
# **updateTypedLinkFacet**
> Object updateTypedLinkFacet(xAmzDataPartition, updateTypedLinkFacetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates a &lt;a&gt;TypedLinkFacet&lt;/a&gt;. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.
    UpdateTypedLinkFacetRequest updateTypedLinkFacetRequest = new UpdateTypedLinkFacetRequest(); // UpdateTypedLinkFacetRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.updateTypedLinkFacet(xAmzDataPartition, updateTypedLinkFacetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateTypedLinkFacet");
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
| **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the schema. For more information, see &lt;a&gt;arns&lt;/a&gt;. | |
| **updateTypedLinkFacetRequest** | [**UpdateTypedLinkFacetRequest**](UpdateTypedLinkFacetRequest.md)|  | |
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
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | FacetValidationException |  -  |
| **487** | InvalidFacetUpdateException |  -  |
| **488** | ResourceNotFoundException |  -  |
| **489** | FacetNotFoundException |  -  |
| **490** | InvalidRuleException |  -  |

<a id="upgradeAppliedSchema"></a>
# **upgradeAppliedSchema**
> UpgradeAppliedSchemaResponse upgradeAppliedSchema(upgradeAppliedSchemaRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Upgrades a single directory in-place using the &lt;code&gt;PublishedSchemaArn&lt;/code&gt; with schema updates found in &lt;code&gt;MinorVersion&lt;/code&gt;. Backwards-compatible minor version upgrades are instantaneously available for readers on all objects in the directory. Note: This is a synchronous API call and upgrades only one schema on a given directory per call. To upgrade multiple directories from one schema, you would need to call this API on each directory.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UpgradeAppliedSchemaRequest upgradeAppliedSchemaRequest = new UpgradeAppliedSchemaRequest(); // UpgradeAppliedSchemaRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpgradeAppliedSchemaResponse result = apiInstance.upgradeAppliedSchema(upgradeAppliedSchemaRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#upgradeAppliedSchema");
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
| **upgradeAppliedSchemaRequest** | [**UpgradeAppliedSchemaRequest**](UpgradeAppliedSchemaRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpgradeAppliedSchemaResponse**](UpgradeAppliedSchemaResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | IncompatibleSchemaException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | InvalidAttachmentException |  -  |

<a id="upgradePublishedSchema"></a>
# **upgradePublishedSchema**
> UpgradePublishedSchemaResponse upgradePublishedSchema(upgradePublishedSchemaRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Upgrades a published schema under a new minor version revision using the current contents of &lt;code&gt;DevelopmentSchemaArn&lt;/code&gt;.

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
    defaultClient.setBasePath("http://clouddirectory.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UpgradePublishedSchemaRequest upgradePublishedSchemaRequest = new UpgradePublishedSchemaRequest(); // UpgradePublishedSchemaRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpgradePublishedSchemaResponse result = apiInstance.upgradePublishedSchema(upgradePublishedSchemaRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#upgradePublishedSchema");
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
| **upgradePublishedSchemaRequest** | [**UpgradePublishedSchemaRequest**](UpgradePublishedSchemaRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpgradePublishedSchemaResponse**](UpgradePublishedSchemaResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceException |  -  |
| **481** | InvalidArnException |  -  |
| **482** | RetryableConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | IncompatibleSchemaException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceNotFoundException |  -  |
| **487** | InvalidAttachmentException |  -  |
| **488** | LimitExceededException |  -  |

