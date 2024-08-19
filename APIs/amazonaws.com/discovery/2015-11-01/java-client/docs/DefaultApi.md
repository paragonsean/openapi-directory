# DefaultApi

All URIs are relative to *http://discovery.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**associateConfigurationItemsToApplication**](DefaultApi.md#associateConfigurationItemsToApplication) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.AssociateConfigurationItemsToApplication |  |
| [**batchDeleteImportData**](DefaultApi.md#batchDeleteImportData) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.BatchDeleteImportData |  |
| [**createApplication**](DefaultApi.md#createApplication) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.CreateApplication |  |
| [**createTags**](DefaultApi.md#createTags) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.CreateTags |  |
| [**deleteApplications**](DefaultApi.md#deleteApplications) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.DeleteApplications |  |
| [**deleteTags**](DefaultApi.md#deleteTags) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.DeleteTags |  |
| [**describeAgents**](DefaultApi.md#describeAgents) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.DescribeAgents |  |
| [**describeConfigurations**](DefaultApi.md#describeConfigurations) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.DescribeConfigurations |  |
| [**describeContinuousExports**](DefaultApi.md#describeContinuousExports) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.DescribeContinuousExports |  |
| [**describeExportConfigurations**](DefaultApi.md#describeExportConfigurations) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.DescribeExportConfigurations |  |
| [**describeExportTasks**](DefaultApi.md#describeExportTasks) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.DescribeExportTasks |  |
| [**describeImportTasks**](DefaultApi.md#describeImportTasks) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.DescribeImportTasks |  |
| [**describeTags**](DefaultApi.md#describeTags) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.DescribeTags |  |
| [**disassociateConfigurationItemsFromApplication**](DefaultApi.md#disassociateConfigurationItemsFromApplication) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.DisassociateConfigurationItemsFromApplication |  |
| [**exportConfigurations**](DefaultApi.md#exportConfigurations) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.ExportConfigurations |  |
| [**getDiscoverySummary**](DefaultApi.md#getDiscoverySummary) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.GetDiscoverySummary |  |
| [**listConfigurations**](DefaultApi.md#listConfigurations) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.ListConfigurations |  |
| [**listServerNeighbors**](DefaultApi.md#listServerNeighbors) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.ListServerNeighbors |  |
| [**startContinuousExport**](DefaultApi.md#startContinuousExport) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.StartContinuousExport |  |
| [**startDataCollectionByAgentIds**](DefaultApi.md#startDataCollectionByAgentIds) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.StartDataCollectionByAgentIds |  |
| [**startExportTask**](DefaultApi.md#startExportTask) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.StartExportTask |  |
| [**startImportTask**](DefaultApi.md#startImportTask) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.StartImportTask |  |
| [**stopContinuousExport**](DefaultApi.md#stopContinuousExport) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.StopContinuousExport |  |
| [**stopDataCollectionByAgentIds**](DefaultApi.md#stopDataCollectionByAgentIds) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.StopDataCollectionByAgentIds |  |
| [**updateApplication**](DefaultApi.md#updateApplication) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.UpdateApplication |  |


<a id="associateConfigurationItemsToApplication"></a>
# **associateConfigurationItemsToApplication**
> Object associateConfigurationItemsToApplication(xAmzTarget, associateConfigurationItemsToApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Associates one or more configuration items with an application.

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.AssociateConfigurationItemsToApplication"; // String | 
    AssociateConfigurationItemsToApplicationRequest associateConfigurationItemsToApplicationRequest = new AssociateConfigurationItemsToApplicationRequest(); // AssociateConfigurationItemsToApplicationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.associateConfigurationItemsToApplication(xAmzTarget, associateConfigurationItemsToApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#associateConfigurationItemsToApplication");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.AssociateConfigurationItemsToApplication] |
| **associateConfigurationItemsToApplicationRequest** | [**AssociateConfigurationItemsToApplicationRequest**](AssociateConfigurationItemsToApplicationRequest.md)|  | |
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
| **480** | AuthorizationErrorException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidParameterValueException |  -  |
| **483** | ServerInternalErrorException |  -  |
| **484** | HomeRegionNotSetException |  -  |

<a id="batchDeleteImportData"></a>
# **batchDeleteImportData**
> BatchDeleteImportDataResponse batchDeleteImportData(xAmzTarget, batchDeleteImportDataRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes one or more import tasks, each identified by their import ID. Each import task has a number of records that can identify servers or applications. &lt;/p&gt; &lt;p&gt;Amazon Web Services Application Discovery Service has built-in matching logic that will identify when discovered servers match existing entries that you&#39;ve previously discovered, the information for the already-existing discovered server is updated. When you delete an import task that contains records that were used to match, the information in those matched records that comes from the deleted records will also be deleted.&lt;/p&gt;

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.BatchDeleteImportData"; // String | 
    BatchDeleteImportDataRequest batchDeleteImportDataRequest = new BatchDeleteImportDataRequest(); // BatchDeleteImportDataRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      BatchDeleteImportDataResponse result = apiInstance.batchDeleteImportData(xAmzTarget, batchDeleteImportDataRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchDeleteImportData");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.BatchDeleteImportData] |
| **batchDeleteImportDataRequest** | [**BatchDeleteImportDataRequest**](BatchDeleteImportDataRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**BatchDeleteImportDataResponse**](BatchDeleteImportDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AuthorizationErrorException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidParameterValueException |  -  |
| **483** | ServerInternalErrorException |  -  |
| **484** | HomeRegionNotSetException |  -  |

<a id="createApplication"></a>
# **createApplication**
> CreateApplicationResponse createApplication(xAmzTarget, createApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates an application with the given name and description.

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.CreateApplication"; // String | 
    CreateApplicationRequest createApplicationRequest = new CreateApplicationRequest(); // CreateApplicationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateApplicationResponse result = apiInstance.createApplication(xAmzTarget, createApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createApplication");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.CreateApplication] |
| **createApplicationRequest** | [**CreateApplicationRequest**](CreateApplicationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateApplicationResponse**](CreateApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AuthorizationErrorException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidParameterValueException |  -  |
| **483** | ServerInternalErrorException |  -  |
| **484** | HomeRegionNotSetException |  -  |

<a id="createTags"></a>
# **createTags**
> Object createTags(xAmzTarget, createTagsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates one or more tags for configuration items. Tags are metadata that help you categorize IT assets. This API accepts a list of multiple configuration items.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Do not store sensitive information (like personal data) in tags.&lt;/p&gt; &lt;/important&gt;

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.CreateTags"; // String | 
    CreateTagsRequest createTagsRequest = new CreateTagsRequest(); // CreateTagsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.createTags(xAmzTarget, createTagsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createTags");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.CreateTags] |
| **createTagsRequest** | [**CreateTagsRequest**](CreateTagsRequest.md)|  | |
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
| **480** | AuthorizationErrorException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InvalidParameterException |  -  |
| **483** | InvalidParameterValueException |  -  |
| **484** | ServerInternalErrorException |  -  |
| **485** | HomeRegionNotSetException |  -  |

<a id="deleteApplications"></a>
# **deleteApplications**
> Object deleteApplications(xAmzTarget, deleteApplicationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes a list of applications and their associations with configuration items.

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.DeleteApplications"; // String | 
    DeleteApplicationsRequest deleteApplicationsRequest = new DeleteApplicationsRequest(); // DeleteApplicationsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteApplications(xAmzTarget, deleteApplicationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteApplications");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.DeleteApplications] |
| **deleteApplicationsRequest** | [**DeleteApplicationsRequest**](DeleteApplicationsRequest.md)|  | |
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
| **480** | AuthorizationErrorException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidParameterValueException |  -  |
| **483** | ServerInternalErrorException |  -  |
| **484** | HomeRegionNotSetException |  -  |

<a id="deleteTags"></a>
# **deleteTags**
> Object deleteTags(xAmzTarget, deleteTagsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes the association between configuration items and one or more tags. This API accepts a list of multiple configuration items.

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.DeleteTags"; // String | 
    DeleteTagsRequest deleteTagsRequest = new DeleteTagsRequest(); // DeleteTagsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteTags(xAmzTarget, deleteTagsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteTags");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.DeleteTags] |
| **deleteTagsRequest** | [**DeleteTagsRequest**](DeleteTagsRequest.md)|  | |
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
| **480** | AuthorizationErrorException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InvalidParameterException |  -  |
| **483** | InvalidParameterValueException |  -  |
| **484** | ServerInternalErrorException |  -  |
| **485** | HomeRegionNotSetException |  -  |

<a id="describeAgents"></a>
# **describeAgents**
> DescribeAgentsResponse describeAgents(xAmzTarget, describeAgentsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Lists agents or collectors as specified by ID or other filters. All agents/collectors associated with your user can be listed if you call &lt;code&gt;DescribeAgents&lt;/code&gt; as is without passing any parameters.

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.DescribeAgents"; // String | 
    DescribeAgentsRequest describeAgentsRequest = new DescribeAgentsRequest(); // DescribeAgentsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeAgentsResponse result = apiInstance.describeAgents(xAmzTarget, describeAgentsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeAgents");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.DescribeAgents] |
| **describeAgentsRequest** | [**DescribeAgentsRequest**](DescribeAgentsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeAgentsResponse**](DescribeAgentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AuthorizationErrorException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidParameterValueException |  -  |
| **483** | ServerInternalErrorException |  -  |
| **484** | HomeRegionNotSetException |  -  |

<a id="describeConfigurations"></a>
# **describeConfigurations**
> DescribeConfigurationsResponse describeConfigurations(xAmzTarget, describeConfigurationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Retrieves attributes for a list of configuration item IDs.&lt;/p&gt; &lt;note&gt; &lt;p&gt;All of the supplied IDs must be for the same asset type from one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;server&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;application&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;process&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;connection&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Output fields are specific to the asset type specified. For example, the output for a &lt;i&gt;server&lt;/i&gt; configuration item includes a list of attributes about the server, such as host name, operating system, number of network cards, etc.&lt;/p&gt; &lt;p&gt;For a complete list of outputs for each asset type, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-api-queries.html#DescribeConfigurations\&quot;&gt;Using the DescribeConfigurations Action&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Application Discovery Service User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.DescribeConfigurations"; // String | 
    DescribeConfigurationsRequest describeConfigurationsRequest = new DescribeConfigurationsRequest(); // DescribeConfigurationsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeConfigurationsResponse result = apiInstance.describeConfigurations(xAmzTarget, describeConfigurationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeConfigurations");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.DescribeConfigurations] |
| **describeConfigurationsRequest** | [**DescribeConfigurationsRequest**](DescribeConfigurationsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeConfigurationsResponse**](DescribeConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AuthorizationErrorException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidParameterValueException |  -  |
| **483** | ServerInternalErrorException |  -  |
| **484** | HomeRegionNotSetException |  -  |

<a id="describeContinuousExports"></a>
# **describeContinuousExports**
> DescribeContinuousExportsResponse describeContinuousExports(xAmzTarget, describeContinuousExportsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Lists exports as specified by ID. All continuous exports associated with your user can be listed if you call &lt;code&gt;DescribeContinuousExports&lt;/code&gt; as is without passing any parameters.

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.DescribeContinuousExports"; // String | 
    DescribeContinuousExportsRequest describeContinuousExportsRequest = new DescribeContinuousExportsRequest(); // DescribeContinuousExportsRequest | 
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
      DescribeContinuousExportsResponse result = apiInstance.describeContinuousExports(xAmzTarget, describeContinuousExportsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeContinuousExports");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.DescribeContinuousExports] |
| **describeContinuousExportsRequest** | [**DescribeContinuousExportsRequest**](DescribeContinuousExportsRequest.md)|  | |
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

[**DescribeContinuousExportsResponse**](DescribeContinuousExportsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AuthorizationErrorException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidParameterValueException |  -  |
| **483** | ServerInternalErrorException |  -  |
| **484** | OperationNotPermittedException |  -  |
| **485** | ResourceNotFoundException |  -  |
| **486** | HomeRegionNotSetException |  -  |

<a id="describeExportConfigurations"></a>
# **describeExportConfigurations**
> DescribeExportConfigurationsResponse describeExportConfigurations(xAmzTarget, describeExportConfigurationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



 &lt;code&gt;DescribeExportConfigurations&lt;/code&gt; is deprecated. Use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeExportTasks.html\&quot;&gt;DescribeExportTasks&lt;/a&gt;, instead.

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.DescribeExportConfigurations"; // String | 
    DescribeExportConfigurationsRequest describeExportConfigurationsRequest = new DescribeExportConfigurationsRequest(); // DescribeExportConfigurationsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeExportConfigurationsResponse result = apiInstance.describeExportConfigurations(xAmzTarget, describeExportConfigurationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeExportConfigurations");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.DescribeExportConfigurations] |
| **describeExportConfigurationsRequest** | [**DescribeExportConfigurationsRequest**](DescribeExportConfigurationsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeExportConfigurationsResponse**](DescribeExportConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AuthorizationErrorException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InvalidParameterException |  -  |
| **483** | InvalidParameterValueException |  -  |
| **484** | ServerInternalErrorException |  -  |
| **485** | HomeRegionNotSetException |  -  |

<a id="describeExportTasks"></a>
# **describeExportTasks**
> DescribeExportTasksResponse describeExportTasks(xAmzTarget, describeExportTasksRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieve status of one or more export tasks. You can retrieve the status of up to 100 export tasks.

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.DescribeExportTasks"; // String | 
    DescribeExportTasksRequest describeExportTasksRequest = new DescribeExportTasksRequest(); // DescribeExportTasksRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeExportTasksResponse result = apiInstance.describeExportTasks(xAmzTarget, describeExportTasksRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeExportTasks");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.DescribeExportTasks] |
| **describeExportTasksRequest** | [**DescribeExportTasksRequest**](DescribeExportTasksRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeExportTasksResponse**](DescribeExportTasksResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AuthorizationErrorException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidParameterValueException |  -  |
| **483** | ServerInternalErrorException |  -  |
| **484** | HomeRegionNotSetException |  -  |

<a id="describeImportTasks"></a>
# **describeImportTasks**
> DescribeImportTasksResponse describeImportTasks(xAmzTarget, describeImportTasksRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Returns an array of import tasks for your account, including status information, times, IDs, the Amazon S3 Object URL for the import file, and more.

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.DescribeImportTasks"; // String | 
    DescribeImportTasksRequest describeImportTasksRequest = new DescribeImportTasksRequest(); // DescribeImportTasksRequest | 
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
      DescribeImportTasksResponse result = apiInstance.describeImportTasks(xAmzTarget, describeImportTasksRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeImportTasks");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.DescribeImportTasks] |
| **describeImportTasksRequest** | [**DescribeImportTasksRequest**](DescribeImportTasksRequest.md)|  | |
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

[**DescribeImportTasksResponse**](DescribeImportTasksResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AuthorizationErrorException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidParameterValueException |  -  |
| **483** | ServerInternalErrorException |  -  |
| **484** | HomeRegionNotSetException |  -  |

<a id="describeTags"></a>
# **describeTags**
> DescribeTagsResponse describeTags(xAmzTarget, describeTagsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Retrieves a list of configuration items that have tags as specified by the key-value pairs, name and value, passed to the optional parameter &lt;code&gt;filters&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;There are three valid tag filter names:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;tagKey&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;tagValue&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;configurationId&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Also, all configuration items associated with your user that have tags can be listed if you call &lt;code&gt;DescribeTags&lt;/code&gt; as is without passing any parameters.&lt;/p&gt;

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.DescribeTags"; // String | 
    DescribeTagsRequest describeTagsRequest = new DescribeTagsRequest(); // DescribeTagsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeTagsResponse result = apiInstance.describeTags(xAmzTarget, describeTagsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeTags");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.DescribeTags] |
| **describeTagsRequest** | [**DescribeTagsRequest**](DescribeTagsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeTagsResponse**](DescribeTagsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AuthorizationErrorException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InvalidParameterException |  -  |
| **483** | InvalidParameterValueException |  -  |
| **484** | ServerInternalErrorException |  -  |
| **485** | HomeRegionNotSetException |  -  |

<a id="disassociateConfigurationItemsFromApplication"></a>
# **disassociateConfigurationItemsFromApplication**
> Object disassociateConfigurationItemsFromApplication(xAmzTarget, disassociateConfigurationItemsFromApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Disassociates one or more configuration items from an application.

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.DisassociateConfigurationItemsFromApplication"; // String | 
    DisassociateConfigurationItemsFromApplicationRequest disassociateConfigurationItemsFromApplicationRequest = new DisassociateConfigurationItemsFromApplicationRequest(); // DisassociateConfigurationItemsFromApplicationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.disassociateConfigurationItemsFromApplication(xAmzTarget, disassociateConfigurationItemsFromApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#disassociateConfigurationItemsFromApplication");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.DisassociateConfigurationItemsFromApplication] |
| **disassociateConfigurationItemsFromApplicationRequest** | [**DisassociateConfigurationItemsFromApplicationRequest**](DisassociateConfigurationItemsFromApplicationRequest.md)|  | |
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
| **480** | AuthorizationErrorException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidParameterValueException |  -  |
| **483** | ServerInternalErrorException |  -  |
| **484** | HomeRegionNotSetException |  -  |

<a id="exportConfigurations"></a>
# **exportConfigurations**
> ExportConfigurationsResponse exportConfigurations(xAmzTarget, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deprecated. Use &lt;code&gt;StartExportTask&lt;/code&gt; instead.&lt;/p&gt; &lt;p&gt;Exports all discovered configuration data to an Amazon S3 bucket or an application that enables you to view and evaluate the data. Data includes tags and tag associations, processes, connections, servers, and system performance. This API returns an export ID that you can query using the &lt;i&gt;DescribeExportConfigurations&lt;/i&gt; API. The system imposes a limit of two configuration exports in six hours.&lt;/p&gt;

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.ExportConfigurations"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ExportConfigurationsResponse result = apiInstance.exportConfigurations(xAmzTarget, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#exportConfigurations");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.ExportConfigurations] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ExportConfigurationsResponse**](ExportConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AuthorizationErrorException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidParameterValueException |  -  |
| **483** | ServerInternalErrorException |  -  |
| **484** | OperationNotPermittedException |  -  |
| **485** | HomeRegionNotSetException |  -  |

<a id="getDiscoverySummary"></a>
# **getDiscoverySummary**
> GetDiscoverySummaryResponse getDiscoverySummary(xAmzTarget, body, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Retrieves a short summary of discovered assets.&lt;/p&gt; &lt;p&gt;This API operation takes no request parameters and is called as is at the command prompt as shown in the example.&lt;/p&gt;

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.GetDiscoverySummary"; // String | 
    Object body = null; // Object | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetDiscoverySummaryResponse result = apiInstance.getDiscoverySummary(xAmzTarget, body, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDiscoverySummary");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.GetDiscoverySummary] |
| **body** | **Object**|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetDiscoverySummaryResponse**](GetDiscoverySummaryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AuthorizationErrorException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidParameterValueException |  -  |
| **483** | ServerInternalErrorException |  -  |
| **484** | HomeRegionNotSetException |  -  |

<a id="listConfigurations"></a>
# **listConfigurations**
> ListConfigurationsResponse listConfigurations(xAmzTarget, listConfigurationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves a list of configuration items as specified by the value passed to the required parameter &lt;code&gt;configurationType&lt;/code&gt;. Optional filtering may be applied to refine search results.

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.ListConfigurations"; // String | 
    ListConfigurationsRequest listConfigurationsRequest = new ListConfigurationsRequest(); // ListConfigurationsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListConfigurationsResponse result = apiInstance.listConfigurations(xAmzTarget, listConfigurationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listConfigurations");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.ListConfigurations] |
| **listConfigurationsRequest** | [**ListConfigurationsRequest**](ListConfigurationsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListConfigurationsResponse**](ListConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AuthorizationErrorException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InvalidParameterException |  -  |
| **483** | InvalidParameterValueException |  -  |
| **484** | ServerInternalErrorException |  -  |
| **485** | HomeRegionNotSetException |  -  |

<a id="listServerNeighbors"></a>
# **listServerNeighbors**
> ListServerNeighborsResponse listServerNeighbors(xAmzTarget, listServerNeighborsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves a list of servers that are one network hop away from a specified server.

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.ListServerNeighbors"; // String | 
    ListServerNeighborsRequest listServerNeighborsRequest = new ListServerNeighborsRequest(); // ListServerNeighborsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListServerNeighborsResponse result = apiInstance.listServerNeighbors(xAmzTarget, listServerNeighborsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listServerNeighbors");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.ListServerNeighbors] |
| **listServerNeighborsRequest** | [**ListServerNeighborsRequest**](ListServerNeighborsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListServerNeighborsResponse**](ListServerNeighborsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AuthorizationErrorException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidParameterValueException |  -  |
| **483** | ServerInternalErrorException |  -  |
| **484** | HomeRegionNotSetException |  -  |

<a id="startContinuousExport"></a>
# **startContinuousExport**
> StartContinuousExportResponse startContinuousExport(xAmzTarget, body, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Start the continuous flow of agent&#39;s discovered data into Amazon Athena.

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.StartContinuousExport"; // String | 
    Object body = null; // Object | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartContinuousExportResponse result = apiInstance.startContinuousExport(xAmzTarget, body, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startContinuousExport");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.StartContinuousExport] |
| **body** | **Object**|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartContinuousExportResponse**](StartContinuousExportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ConflictErrorException |  -  |
| **481** | AuthorizationErrorException |  -  |
| **482** | InvalidParameterException |  -  |
| **483** | InvalidParameterValueException |  -  |
| **484** | ServerInternalErrorException |  -  |
| **485** | OperationNotPermittedException |  -  |
| **486** | ResourceInUseException |  -  |
| **487** | HomeRegionNotSetException |  -  |

<a id="startDataCollectionByAgentIds"></a>
# **startDataCollectionByAgentIds**
> StartDataCollectionByAgentIdsResponse startDataCollectionByAgentIds(xAmzTarget, startDataCollectionByAgentIdsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Instructs the specified agents to start collecting data.

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.StartDataCollectionByAgentIds"; // String | 
    StartDataCollectionByAgentIdsRequest startDataCollectionByAgentIdsRequest = new StartDataCollectionByAgentIdsRequest(); // StartDataCollectionByAgentIdsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartDataCollectionByAgentIdsResponse result = apiInstance.startDataCollectionByAgentIds(xAmzTarget, startDataCollectionByAgentIdsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startDataCollectionByAgentIds");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.StartDataCollectionByAgentIds] |
| **startDataCollectionByAgentIdsRequest** | [**StartDataCollectionByAgentIdsRequest**](StartDataCollectionByAgentIdsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartDataCollectionByAgentIdsResponse**](StartDataCollectionByAgentIdsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AuthorizationErrorException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidParameterValueException |  -  |
| **483** | ServerInternalErrorException |  -  |
| **484** | HomeRegionNotSetException |  -  |

<a id="startExportTask"></a>
# **startExportTask**
> StartExportTaskResponse startExportTask(xAmzTarget, startExportTaskRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Begins the export of a discovered data report to an Amazon S3 bucket managed by Amazon Web Services.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Exports might provide an estimate of fees and savings based on certain information that you provide. Fee estimates do not include any taxes that might apply. Your actual fees and savings depend on a variety of factors, including your actual usage of Amazon Web Services services, which might vary from the estimates provided in this report.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;If you do not specify &lt;code&gt;preferences&lt;/code&gt; or &lt;code&gt;agentIds&lt;/code&gt; in the filter, a summary of all servers, applications, tags, and performance is generated. This data is an aggregation of all server data collected through on-premises tooling, file import, application grouping and applying tags.&lt;/p&gt; &lt;p&gt;If you specify &lt;code&gt;agentIds&lt;/code&gt; in a filter, the task exports up to 72 hours of detailed data collected by the identified Application Discovery Agent, including network, process, and performance details. A time range for exported agent data may be set by using &lt;code&gt;startTime&lt;/code&gt; and &lt;code&gt;endTime&lt;/code&gt;. Export of detailed agent data is limited to five concurrently running exports. Export of detailed agent data is limited to two exports per day.&lt;/p&gt; &lt;p&gt;If you enable &lt;code&gt;ec2RecommendationsPreferences&lt;/code&gt; in &lt;code&gt;preferences&lt;/code&gt; , an Amazon EC2 instance matching the characteristics of each server in Application Discovery Service is generated. Changing the attributes of the &lt;code&gt;ec2RecommendationsPreferences&lt;/code&gt; changes the criteria of the recommendation.&lt;/p&gt;

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.StartExportTask"; // String | 
    StartExportTaskRequest startExportTaskRequest = new StartExportTaskRequest(); // StartExportTaskRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartExportTaskResponse result = apiInstance.startExportTask(xAmzTarget, startExportTaskRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startExportTask");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.StartExportTask] |
| **startExportTaskRequest** | [**StartExportTaskRequest**](StartExportTaskRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartExportTaskResponse**](StartExportTaskResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AuthorizationErrorException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidParameterValueException |  -  |
| **483** | ServerInternalErrorException |  -  |
| **484** | OperationNotPermittedException |  -  |
| **485** | HomeRegionNotSetException |  -  |

<a id="startImportTask"></a>
# **startImportTask**
> StartImportTaskResponse startImportTask(xAmzTarget, startImportTaskRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Starts an import task, which allows you to import details of your on-premises environment directly into Amazon Web Services Migration Hub without having to use the Amazon Web Services Application Discovery Service (Application Discovery Service) tools such as the Amazon Web Services Application Discovery Service Agentless Collector or Application Discovery Agent. This gives you the option to perform migration assessment and planning directly from your imported data, including the ability to group your devices as applications and track their migration status.&lt;/p&gt; &lt;p&gt;To start an import request, do this:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Download the specially formatted comma separated value (CSV) import template, which you can find here: &lt;a href&#x3D;\&quot;https://s3.us-west-2.amazonaws.com/templates-7cffcf56-bd96-4b1c-b45b-a5b42f282e46/import_template.csv\&quot;&gt;https://s3.us-west-2.amazonaws.com/templates-7cffcf56-bd96-4b1c-b45b-a5b42f282e46/import_template.csv&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Fill out the template with your server and application data.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Upload your import file to an Amazon S3 bucket, and make a note of it&#39;s Object URL. Your import file must be in the CSV format.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the console or the &lt;code&gt;StartImportTask&lt;/code&gt; command with the Amazon Web Services CLI or one of the Amazon Web Services SDKs to import the records from your file.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information, including step-by-step procedures, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-import.html\&quot;&gt;Migration Hub Import&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Application Discovery Service User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;There are limits to the number of import tasks you can create (and delete) in an Amazon Web Services account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/application-discovery/latest/userguide/ads_service_limits.html\&quot;&gt;Amazon Web Services Application Discovery Service Limits&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Application Discovery Service User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.StartImportTask"; // String | 
    StartImportTaskRequest startImportTaskRequest = new StartImportTaskRequest(); // StartImportTaskRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartImportTaskResponse result = apiInstance.startImportTask(xAmzTarget, startImportTaskRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startImportTask");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.StartImportTask] |
| **startImportTaskRequest** | [**StartImportTaskRequest**](StartImportTaskRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartImportTaskResponse**](StartImportTaskResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceInUseException |  -  |
| **481** | AuthorizationErrorException |  -  |
| **482** | InvalidParameterException |  -  |
| **483** | InvalidParameterValueException |  -  |
| **484** | ServerInternalErrorException |  -  |
| **485** | HomeRegionNotSetException |  -  |

<a id="stopContinuousExport"></a>
# **stopContinuousExport**
> StopContinuousExportResponse stopContinuousExport(xAmzTarget, stopContinuousExportRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Stop the continuous flow of agent&#39;s discovered data into Amazon Athena.

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.StopContinuousExport"; // String | 
    StopContinuousExportRequest stopContinuousExportRequest = new StopContinuousExportRequest(); // StopContinuousExportRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StopContinuousExportResponse result = apiInstance.stopContinuousExport(xAmzTarget, stopContinuousExportRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#stopContinuousExport");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.StopContinuousExport] |
| **stopContinuousExportRequest** | [**StopContinuousExportRequest**](StopContinuousExportRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StopContinuousExportResponse**](StopContinuousExportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AuthorizationErrorException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidParameterValueException |  -  |
| **483** | ServerInternalErrorException |  -  |
| **484** | OperationNotPermittedException |  -  |
| **485** | ResourceNotFoundException |  -  |
| **486** | ResourceInUseException |  -  |
| **487** | HomeRegionNotSetException |  -  |

<a id="stopDataCollectionByAgentIds"></a>
# **stopDataCollectionByAgentIds**
> StopDataCollectionByAgentIdsResponse stopDataCollectionByAgentIds(xAmzTarget, stopDataCollectionByAgentIdsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Instructs the specified agents to stop collecting data.

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.StopDataCollectionByAgentIds"; // String | 
    StopDataCollectionByAgentIdsRequest stopDataCollectionByAgentIdsRequest = new StopDataCollectionByAgentIdsRequest(); // StopDataCollectionByAgentIdsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StopDataCollectionByAgentIdsResponse result = apiInstance.stopDataCollectionByAgentIds(xAmzTarget, stopDataCollectionByAgentIdsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#stopDataCollectionByAgentIds");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.StopDataCollectionByAgentIds] |
| **stopDataCollectionByAgentIdsRequest** | [**StopDataCollectionByAgentIdsRequest**](StopDataCollectionByAgentIdsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StopDataCollectionByAgentIdsResponse**](StopDataCollectionByAgentIdsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AuthorizationErrorException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidParameterValueException |  -  |
| **483** | ServerInternalErrorException |  -  |
| **484** | HomeRegionNotSetException |  -  |

<a id="updateApplication"></a>
# **updateApplication**
> Object updateApplication(xAmzTarget, updateApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates metadata about an application.

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
    defaultClient.setBasePath("http://discovery.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSPoseidonService_V2015_11_01.UpdateApplication"; // String | 
    UpdateApplicationRequest updateApplicationRequest = new UpdateApplicationRequest(); // UpdateApplicationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.updateApplication(xAmzTarget, updateApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateApplication");
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
| **xAmzTarget** | **String**|  | [enum: AWSPoseidonService_V2015_11_01.UpdateApplication] |
| **updateApplicationRequest** | [**UpdateApplicationRequest**](UpdateApplicationRequest.md)|  | |
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
| **480** | AuthorizationErrorException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidParameterValueException |  -  |
| **483** | ServerInternalErrorException |  -  |
| **484** | HomeRegionNotSetException |  -  |

