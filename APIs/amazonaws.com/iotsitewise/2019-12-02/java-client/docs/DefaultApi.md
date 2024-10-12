# DefaultApi

All URIs are relative to *http://iotsitewise.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**associateAssets**](DefaultApi.md#associateAssets) | **POST** /assets/{assetId}/associate |  |
| [**associateTimeSeriesToAssetProperty**](DefaultApi.md#associateTimeSeriesToAssetProperty) | **POST** /timeseries/associate/#alias&amp;assetId&amp;propertyId |  |
| [**batchAssociateProjectAssets**](DefaultApi.md#batchAssociateProjectAssets) | **POST** /projects/{projectId}/assets/associate |  |
| [**batchDisassociateProjectAssets**](DefaultApi.md#batchDisassociateProjectAssets) | **POST** /projects/{projectId}/assets/disassociate |  |
| [**batchGetAssetPropertyAggregates**](DefaultApi.md#batchGetAssetPropertyAggregates) | **POST** /properties/batch/aggregates |  |
| [**batchGetAssetPropertyValue**](DefaultApi.md#batchGetAssetPropertyValue) | **POST** /properties/batch/latest |  |
| [**batchGetAssetPropertyValueHistory**](DefaultApi.md#batchGetAssetPropertyValueHistory) | **POST** /properties/batch/history |  |
| [**batchPutAssetPropertyValue**](DefaultApi.md#batchPutAssetPropertyValue) | **POST** /properties |  |
| [**createAccessPolicy**](DefaultApi.md#createAccessPolicy) | **POST** /access-policies |  |
| [**createAsset**](DefaultApi.md#createAsset) | **POST** /assets |  |
| [**createAssetModel**](DefaultApi.md#createAssetModel) | **POST** /asset-models |  |
| [**createBulkImportJob**](DefaultApi.md#createBulkImportJob) | **POST** /jobs |  |
| [**createDashboard**](DefaultApi.md#createDashboard) | **POST** /dashboards |  |
| [**createGateway**](DefaultApi.md#createGateway) | **POST** /20200301/gateways |  |
| [**createPortal**](DefaultApi.md#createPortal) | **POST** /portals |  |
| [**createProject**](DefaultApi.md#createProject) | **POST** /projects |  |
| [**deleteAccessPolicy**](DefaultApi.md#deleteAccessPolicy) | **DELETE** /access-policies/{accessPolicyId} |  |
| [**deleteAsset**](DefaultApi.md#deleteAsset) | **DELETE** /assets/{assetId} |  |
| [**deleteAssetModel**](DefaultApi.md#deleteAssetModel) | **DELETE** /asset-models/{assetModelId} |  |
| [**deleteDashboard**](DefaultApi.md#deleteDashboard) | **DELETE** /dashboards/{dashboardId} |  |
| [**deleteGateway**](DefaultApi.md#deleteGateway) | **DELETE** /20200301/gateways/{gatewayId} |  |
| [**deletePortal**](DefaultApi.md#deletePortal) | **DELETE** /portals/{portalId} |  |
| [**deleteProject**](DefaultApi.md#deleteProject) | **DELETE** /projects/{projectId} |  |
| [**deleteTimeSeries**](DefaultApi.md#deleteTimeSeries) | **POST** /timeseries/delete/ |  |
| [**describeAccessPolicy**](DefaultApi.md#describeAccessPolicy) | **GET** /access-policies/{accessPolicyId} |  |
| [**describeAsset**](DefaultApi.md#describeAsset) | **GET** /assets/{assetId} |  |
| [**describeAssetModel**](DefaultApi.md#describeAssetModel) | **GET** /asset-models/{assetModelId} |  |
| [**describeAssetProperty**](DefaultApi.md#describeAssetProperty) | **GET** /assets/{assetId}/properties/{propertyId} |  |
| [**describeBulkImportJob**](DefaultApi.md#describeBulkImportJob) | **GET** /jobs/{jobId} |  |
| [**describeDashboard**](DefaultApi.md#describeDashboard) | **GET** /dashboards/{dashboardId} |  |
| [**describeDefaultEncryptionConfiguration**](DefaultApi.md#describeDefaultEncryptionConfiguration) | **GET** /configuration/account/encryption |  |
| [**describeGateway**](DefaultApi.md#describeGateway) | **GET** /20200301/gateways/{gatewayId} |  |
| [**describeGatewayCapabilityConfiguration**](DefaultApi.md#describeGatewayCapabilityConfiguration) | **GET** /20200301/gateways/{gatewayId}/capability/{capabilityNamespace} |  |
| [**describeLoggingOptions**](DefaultApi.md#describeLoggingOptions) | **GET** /logging |  |
| [**describePortal**](DefaultApi.md#describePortal) | **GET** /portals/{portalId} |  |
| [**describeProject**](DefaultApi.md#describeProject) | **GET** /projects/{projectId} |  |
| [**describeStorageConfiguration**](DefaultApi.md#describeStorageConfiguration) | **GET** /configuration/account/storage |  |
| [**describeTimeSeries**](DefaultApi.md#describeTimeSeries) | **GET** /timeseries/describe/ |  |
| [**disassociateAssets**](DefaultApi.md#disassociateAssets) | **POST** /assets/{assetId}/disassociate |  |
| [**disassociateTimeSeriesFromAssetProperty**](DefaultApi.md#disassociateTimeSeriesFromAssetProperty) | **POST** /timeseries/disassociate/#alias&amp;assetId&amp;propertyId |  |
| [**getAssetPropertyAggregates**](DefaultApi.md#getAssetPropertyAggregates) | **GET** /properties/aggregates#aggregateTypes&amp;resolution&amp;startDate&amp;endDate |  |
| [**getAssetPropertyValue**](DefaultApi.md#getAssetPropertyValue) | **GET** /properties/latest |  |
| [**getAssetPropertyValueHistory**](DefaultApi.md#getAssetPropertyValueHistory) | **GET** /properties/history |  |
| [**getInterpolatedAssetPropertyValues**](DefaultApi.md#getInterpolatedAssetPropertyValues) | **GET** /properties/interpolated#startTimeInSeconds&amp;endTimeInSeconds&amp;quality&amp;intervalInSeconds&amp;type |  |
| [**listAccessPolicies**](DefaultApi.md#listAccessPolicies) | **GET** /access-policies |  |
| [**listAssetModelProperties**](DefaultApi.md#listAssetModelProperties) | **GET** /asset-models/{assetModelId}/properties |  |
| [**listAssetModels**](DefaultApi.md#listAssetModels) | **GET** /asset-models |  |
| [**listAssetProperties**](DefaultApi.md#listAssetProperties) | **GET** /assets/{assetId}/properties |  |
| [**listAssetRelationships**](DefaultApi.md#listAssetRelationships) | **GET** /assets/{assetId}/assetRelationships#traversalType |  |
| [**listAssets**](DefaultApi.md#listAssets) | **GET** /assets |  |
| [**listAssociatedAssets**](DefaultApi.md#listAssociatedAssets) | **GET** /assets/{assetId}/hierarchies |  |
| [**listBulkImportJobs**](DefaultApi.md#listBulkImportJobs) | **GET** /jobs |  |
| [**listDashboards**](DefaultApi.md#listDashboards) | **GET** /dashboards#projectId |  |
| [**listGateways**](DefaultApi.md#listGateways) | **GET** /20200301/gateways |  |
| [**listPortals**](DefaultApi.md#listPortals) | **GET** /portals |  |
| [**listProjectAssets**](DefaultApi.md#listProjectAssets) | **GET** /projects/{projectId}/assets |  |
| [**listProjects**](DefaultApi.md#listProjects) | **GET** /projects#portalId |  |
| [**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags#resourceArn |  |
| [**listTimeSeries**](DefaultApi.md#listTimeSeries) | **GET** /timeseries/ |  |
| [**putDefaultEncryptionConfiguration**](DefaultApi.md#putDefaultEncryptionConfiguration) | **POST** /configuration/account/encryption |  |
| [**putLoggingOptions**](DefaultApi.md#putLoggingOptions) | **PUT** /logging |  |
| [**putStorageConfiguration**](DefaultApi.md#putStorageConfiguration) | **POST** /configuration/account/storage |  |
| [**tagResource**](DefaultApi.md#tagResource) | **POST** /tags#resourceArn |  |
| [**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags#resourceArn&amp;tagKeys |  |
| [**updateAccessPolicy**](DefaultApi.md#updateAccessPolicy) | **PUT** /access-policies/{accessPolicyId} |  |
| [**updateAsset**](DefaultApi.md#updateAsset) | **PUT** /assets/{assetId} |  |
| [**updateAssetModel**](DefaultApi.md#updateAssetModel) | **PUT** /asset-models/{assetModelId} |  |
| [**updateAssetProperty**](DefaultApi.md#updateAssetProperty) | **PUT** /assets/{assetId}/properties/{propertyId} |  |
| [**updateDashboard**](DefaultApi.md#updateDashboard) | **PUT** /dashboards/{dashboardId} |  |
| [**updateGateway**](DefaultApi.md#updateGateway) | **PUT** /20200301/gateways/{gatewayId} |  |
| [**updateGatewayCapabilityConfiguration**](DefaultApi.md#updateGatewayCapabilityConfiguration) | **POST** /20200301/gateways/{gatewayId}/capability |  |
| [**updatePortal**](DefaultApi.md#updatePortal) | **PUT** /portals/{portalId} |  |
| [**updateProject**](DefaultApi.md#updateProject) | **PUT** /projects/{projectId} |  |


<a id="associateAssets"></a>
# **associateAssets**
> associateAssets(assetId, associateAssetsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Associates a child asset with the given parent asset through a hierarchy defined in the parent asset&#39;s model. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/add-associated-assets.html\&quot;&gt;Associating assets&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String assetId = "assetId_example"; // String | The ID of the parent asset.
    AssociateAssetsRequest associateAssetsRequest = new AssociateAssetsRequest(); // AssociateAssetsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.associateAssets(assetId, associateAssetsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#associateAssets");
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
| **assetId** | **String**| The ID of the parent asset. | |
| **associateAssetsRequest** | [**AssociateAssetsRequest**](AssociateAssetsRequest.md)|  | |
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
| **480** | InvalidRequestException |  -  |
| **481** | ResourceAlreadyExistsException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | ThrottlingException |  -  |
| **486** | ConflictingOperationException |  -  |

<a id="associateTimeSeriesToAssetProperty"></a>
# **associateTimeSeriesToAssetProperty**
> associateTimeSeriesToAssetProperty(alias, assetId, propertyId, associateTimeSeriesToAssetPropertyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Associates a time series (data stream) with an asset property.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String alias = "alias_example"; // String | The alias that identifies the time series.
    String assetId = "assetId_example"; // String | The ID of the asset in which the asset property was created.
    String propertyId = "propertyId_example"; // String | The ID of the asset property.
    AssociateTimeSeriesToAssetPropertyRequest associateTimeSeriesToAssetPropertyRequest = new AssociateTimeSeriesToAssetPropertyRequest(); // AssociateTimeSeriesToAssetPropertyRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.associateTimeSeriesToAssetProperty(alias, assetId, propertyId, associateTimeSeriesToAssetPropertyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#associateTimeSeriesToAssetProperty");
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
| **alias** | **String**| The alias that identifies the time series. | |
| **assetId** | **String**| The ID of the asset in which the asset property was created. | |
| **propertyId** | **String**| The ID of the asset property. | |
| **associateTimeSeriesToAssetPropertyRequest** | [**AssociateTimeSeriesToAssetPropertyRequest**](AssociateTimeSeriesToAssetPropertyRequest.md)|  | |
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
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ConflictingOperationException |  -  |

<a id="batchAssociateProjectAssets"></a>
# **batchAssociateProjectAssets**
> BatchAssociateProjectAssetsResponse batchAssociateProjectAssets(projectId, batchAssociateProjectAssetsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Associates a group (batch) of assets with an IoT SiteWise Monitor project.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectId = "projectId_example"; // String | The ID of the project to which to associate the assets.
    BatchAssociateProjectAssetsRequest batchAssociateProjectAssetsRequest = new BatchAssociateProjectAssetsRequest(); // BatchAssociateProjectAssetsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      BatchAssociateProjectAssetsResponse result = apiInstance.batchAssociateProjectAssets(projectId, batchAssociateProjectAssetsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchAssociateProjectAssets");
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
| **projectId** | **String**| The ID of the project to which to associate the assets. | |
| **batchAssociateProjectAssetsRequest** | [**BatchAssociateProjectAssetsRequest**](BatchAssociateProjectAssetsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**BatchAssociateProjectAssetsResponse**](BatchAssociateProjectAssetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | LimitExceededException |  -  |

<a id="batchDisassociateProjectAssets"></a>
# **batchDisassociateProjectAssets**
> BatchDisassociateProjectAssetsResponse batchDisassociateProjectAssets(projectId, batchDisassociateProjectAssetsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Disassociates a group (batch) of assets from an IoT SiteWise Monitor project.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectId = "projectId_example"; // String | The ID of the project from which to disassociate the assets.
    BatchDisassociateProjectAssetsRequest batchDisassociateProjectAssetsRequest = new BatchDisassociateProjectAssetsRequest(); // BatchDisassociateProjectAssetsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      BatchDisassociateProjectAssetsResponse result = apiInstance.batchDisassociateProjectAssets(projectId, batchDisassociateProjectAssetsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchDisassociateProjectAssets");
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
| **projectId** | **String**| The ID of the project from which to disassociate the assets. | |
| **batchDisassociateProjectAssetsRequest** | [**BatchDisassociateProjectAssetsRequest**](BatchDisassociateProjectAssetsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**BatchDisassociateProjectAssetsResponse**](BatchDisassociateProjectAssetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |

<a id="batchGetAssetPropertyAggregates"></a>
# **batchGetAssetPropertyAggregates**
> BatchGetAssetPropertyAggregatesResponse batchGetAssetPropertyAggregates(batchGetAssetPropertyAggregatesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Gets aggregated values (for example, average, minimum, and maximum) for one or more asset properties. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#aggregates\&quot;&gt;Querying aggregates&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    BatchGetAssetPropertyAggregatesRequest batchGetAssetPropertyAggregatesRequest = new BatchGetAssetPropertyAggregatesRequest(); // BatchGetAssetPropertyAggregatesRequest | 
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
      BatchGetAssetPropertyAggregatesResponse result = apiInstance.batchGetAssetPropertyAggregates(batchGetAssetPropertyAggregatesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchGetAssetPropertyAggregates");
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
| **batchGetAssetPropertyAggregatesRequest** | [**BatchGetAssetPropertyAggregatesRequest**](BatchGetAssetPropertyAggregatesRequest.md)|  | |
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

[**BatchGetAssetPropertyAggregatesResponse**](BatchGetAssetPropertyAggregatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="batchGetAssetPropertyValue"></a>
# **batchGetAssetPropertyValue**
> BatchGetAssetPropertyValueResponse batchGetAssetPropertyValue(batchGetAssetPropertyValueRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken)



Gets the current value for one or more asset properties. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#current-values\&quot;&gt;Querying current values&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    BatchGetAssetPropertyValueRequest batchGetAssetPropertyValueRequest = new BatchGetAssetPropertyValueRequest(); // BatchGetAssetPropertyValueRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      BatchGetAssetPropertyValueResponse result = apiInstance.batchGetAssetPropertyValue(batchGetAssetPropertyValueRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchGetAssetPropertyValue");
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
| **batchGetAssetPropertyValueRequest** | [**BatchGetAssetPropertyValueRequest**](BatchGetAssetPropertyValueRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**BatchGetAssetPropertyValueResponse**](BatchGetAssetPropertyValueResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="batchGetAssetPropertyValueHistory"></a>
# **batchGetAssetPropertyValueHistory**
> BatchGetAssetPropertyValueHistoryResponse batchGetAssetPropertyValueHistory(batchGetAssetPropertyValueHistoryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Gets the historical values for one or more asset properties. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#historical-values\&quot;&gt;Querying historical values&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    BatchGetAssetPropertyValueHistoryRequest batchGetAssetPropertyValueHistoryRequest = new BatchGetAssetPropertyValueHistoryRequest(); // BatchGetAssetPropertyValueHistoryRequest | 
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
      BatchGetAssetPropertyValueHistoryResponse result = apiInstance.batchGetAssetPropertyValueHistory(batchGetAssetPropertyValueHistoryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchGetAssetPropertyValueHistory");
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
| **batchGetAssetPropertyValueHistoryRequest** | [**BatchGetAssetPropertyValueHistoryRequest**](BatchGetAssetPropertyValueHistoryRequest.md)|  | |
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

[**BatchGetAssetPropertyValueHistoryResponse**](BatchGetAssetPropertyValueHistoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="batchPutAssetPropertyValue"></a>
# **batchPutAssetPropertyValue**
> BatchPutAssetPropertyValueResponse batchPutAssetPropertyValue(batchPutAssetPropertyValueRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Sends a list of asset property values to IoT SiteWise. Each value is a timestamp-quality-value (TQV) data point. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ingest-api.html\&quot;&gt;Ingesting data using the API&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To identify an asset property, you must specify one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; of an asset property.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;propertyAlias&lt;/code&gt;, which is a data stream alias (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). To define an asset property&#39;s alias, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\&quot;&gt;UpdateAssetProperty&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;important&gt; &lt;p&gt;With respect to Unix epoch time, IoT SiteWise accepts only TQVs that have a timestamp of no more than 7 days in the past and no more than 10 minutes in the future. IoT SiteWise rejects timestamps outside of the inclusive range of [-7 days, +10 minutes] and returns a &lt;code&gt;TimestampOutOfRangeException&lt;/code&gt; error.&lt;/p&gt; &lt;p&gt;For each asset property, IoT SiteWise overwrites TQVs with duplicate timestamps unless the newer TQV has a different quality. For example, if you store a TQV &lt;code&gt;{T1, GOOD, V1}&lt;/code&gt;, then storing &lt;code&gt;{T1, GOOD, V2}&lt;/code&gt; replaces the existing TQV.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;IoT SiteWise authorizes access to each &lt;code&gt;BatchPutAssetPropertyValue&lt;/code&gt; entry individually. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-batchputassetpropertyvalue-action\&quot;&gt;BatchPutAssetPropertyValue authorization&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    BatchPutAssetPropertyValueRequest batchPutAssetPropertyValueRequest = new BatchPutAssetPropertyValueRequest(); // BatchPutAssetPropertyValueRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      BatchPutAssetPropertyValueResponse result = apiInstance.batchPutAssetPropertyValue(batchPutAssetPropertyValueRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchPutAssetPropertyValue");
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
| **batchPutAssetPropertyValueRequest** | [**BatchPutAssetPropertyValueRequest**](BatchPutAssetPropertyValueRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**BatchPutAssetPropertyValueResponse**](BatchPutAssetPropertyValueResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ConflictingOperationException |  -  |

<a id="createAccessPolicy"></a>
# **createAccessPolicy**
> CreateAccessPolicyResponse createAccessPolicy(createAccessPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates an access policy that grants the specified identity (IAM Identity Center user, IAM Identity Center group, or IAM user) access to the specified IoT SiteWise Monitor portal or project resource.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateAccessPolicyRequest createAccessPolicyRequest = new CreateAccessPolicyRequest(); // CreateAccessPolicyRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateAccessPolicyResponse result = apiInstance.createAccessPolicy(createAccessPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAccessPolicy");
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
| **createAccessPolicyRequest** | [**CreateAccessPolicyRequest**](CreateAccessPolicyRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateAccessPolicyResponse**](CreateAccessPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | LimitExceededException |  -  |

<a id="createAsset"></a>
# **createAsset**
> CreateAssetResponse createAsset(createAssetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates an asset from an existing asset model. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-assets.html\&quot;&gt;Creating assets&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateAssetRequest createAssetRequest = new CreateAssetRequest(); // CreateAssetRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateAssetResponse result = apiInstance.createAsset(createAssetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAsset");
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
| **createAssetRequest** | [**CreateAssetRequest**](CreateAssetRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateAssetResponse**](CreateAssetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceAlreadyExistsException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | ThrottlingException |  -  |
| **485** | LimitExceededException |  -  |
| **486** | ConflictingOperationException |  -  |

<a id="createAssetModel"></a>
# **createAssetModel**
> CreateAssetModelResponse createAssetModel(createAssetModelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates an asset model from specified property and hierarchy definitions. You create assets from asset models. With asset models, you can easily create assets of the same type that have standardized definitions. Each asset created from a model inherits the asset model&#39;s property and hierarchy definitions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/define-models.html\&quot;&gt;Defining asset models&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateAssetModelRequest createAssetModelRequest = new CreateAssetModelRequest(); // CreateAssetModelRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateAssetModelResponse result = apiInstance.createAssetModel(createAssetModelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAssetModel");
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
| **createAssetModelRequest** | [**CreateAssetModelRequest**](CreateAssetModelRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateAssetModelResponse**](CreateAssetModelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceAlreadyExistsException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | ThrottlingException |  -  |
| **485** | LimitExceededException |  -  |
| **486** | ConflictingOperationException |  -  |

<a id="createBulkImportJob"></a>
# **createBulkImportJob**
> CreateBulkImportJobResponse createBulkImportJob(createBulkImportJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Defines a job to ingest data to IoT SiteWise from Amazon S3. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/CreateBulkImportJob.html\&quot;&gt;Create a bulk import job (CLI)&lt;/a&gt; in the &lt;i&gt;Amazon Simple Storage Service User Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;You must enable IoT SiteWise to export data to Amazon S3 before you create a bulk import job. For more information about how to configure storage settings, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PutStorageConfiguration.html\&quot;&gt;PutStorageConfiguration&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt;

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateBulkImportJobRequest createBulkImportJobRequest = new CreateBulkImportJobRequest(); // CreateBulkImportJobRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateBulkImportJobResponse result = apiInstance.createBulkImportJob(createBulkImportJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createBulkImportJob");
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
| **createBulkImportJobRequest** | [**CreateBulkImportJobRequest**](CreateBulkImportJobRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateBulkImportJobResponse**](CreateBulkImportJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceAlreadyExistsException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | ThrottlingException |  -  |
| **485** | LimitExceededException |  -  |
| **486** | ConflictingOperationException |  -  |

<a id="createDashboard"></a>
# **createDashboard**
> CreateDashboardResponse createDashboard(createDashboardRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a dashboard in an IoT SiteWise Monitor project.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateDashboardRequest createDashboardRequest = new CreateDashboardRequest(); // CreateDashboardRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateDashboardResponse result = apiInstance.createDashboard(createDashboardRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createDashboard");
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
| **createDashboardRequest** | [**CreateDashboardRequest**](CreateDashboardRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateDashboardResponse**](CreateDashboardResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | LimitExceededException |  -  |

<a id="createGateway"></a>
# **createGateway**
> CreateGatewayResponse createGateway(createGatewayRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a gateway, which is a virtual or edge device that delivers industrial data streams from local servers to IoT SiteWise. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateway-connector.html\&quot;&gt;Ingesting data using a gateway&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateGatewayRequest createGatewayRequest = new CreateGatewayRequest(); // CreateGatewayRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateGatewayResponse result = apiInstance.createGateway(createGatewayRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createGateway");
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
| **createGatewayRequest** | [**CreateGatewayRequest**](CreateGatewayRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateGatewayResponse**](CreateGatewayResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceAlreadyExistsException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | LimitExceededException |  -  |

<a id="createPortal"></a>
# **createPortal**
> CreatePortalResponse createPortal(createPortalRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a portal, which can contain projects and dashboards. IoT SiteWise Monitor uses IAM Identity Center or IAM to authenticate portal users and manage user permissions.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before you can sign in to a new portal, you must add at least one identity to that portal. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/administer-portals.html#portal-change-admins\&quot;&gt;Adding or removing portal administrators&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreatePortalRequest createPortalRequest = new CreatePortalRequest(); // CreatePortalRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreatePortalResponse result = apiInstance.createPortal(createPortalRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createPortal");
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
| **createPortalRequest** | [**CreatePortalRequest**](CreatePortalRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreatePortalResponse**](CreatePortalResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | LimitExceededException |  -  |

<a id="createProject"></a>
# **createProject**
> CreateProjectResponse createProject(createProjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a project in the specified portal.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Make sure that the project name and description don&#39;t contain confidential information.&lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateProjectRequest createProjectRequest = new CreateProjectRequest(); // CreateProjectRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateProjectResponse result = apiInstance.createProject(createProjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createProject");
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
| **createProjectRequest** | [**CreateProjectRequest**](CreateProjectRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateProjectResponse**](CreateProjectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | LimitExceededException |  -  |

<a id="deleteAccessPolicy"></a>
# **deleteAccessPolicy**
> Object deleteAccessPolicy(accessPolicyId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, clientToken)



Deletes an access policy that grants the specified identity access to the specified IoT SiteWise Monitor resource. You can use this operation to revoke access to an IoT SiteWise Monitor resource.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accessPolicyId = "accessPolicyId_example"; // String | The ID of the access policy to be deleted.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String clientToken = "clientToken_example"; // String | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
    try {
      Object result = apiInstance.deleteAccessPolicy(accessPolicyId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, clientToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteAccessPolicy");
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
| **accessPolicyId** | **String**| The ID of the access policy to be deleted. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **clientToken** | **String**| A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. | [optional] |

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
| **204** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |

<a id="deleteAsset"></a>
# **deleteAsset**
> DeleteAssetResponse deleteAsset(assetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, clientToken)



&lt;p&gt;Deletes an asset. This action can&#39;t be undone. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-assets-and-models.html\&quot;&gt;Deleting assets and models&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t delete an asset that&#39;s associated to another asset. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DisassociateAssets.html\&quot;&gt;DisassociateAssets&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String assetId = "assetId_example"; // String | The ID of the asset to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String clientToken = "clientToken_example"; // String | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
    try {
      DeleteAssetResponse result = apiInstance.deleteAsset(assetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, clientToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteAsset");
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
| **assetId** | **String**| The ID of the asset to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **clientToken** | **String**| A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. | [optional] |

### Return type

[**DeleteAssetResponse**](DeleteAssetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ConflictingOperationException |  -  |

<a id="deleteAssetModel"></a>
# **deleteAssetModel**
> DeleteAssetModelResponse deleteAssetModel(assetModelId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, clientToken)



Deletes an asset model. This action can&#39;t be undone. You must delete all assets created from an asset model before you can delete the model. Also, you can&#39;t delete an asset model if a parent asset model exists that contains a property formula expression that depends on the asset model that you want to delete. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-assets-and-models.html\&quot;&gt;Deleting assets and models&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String assetModelId = "assetModelId_example"; // String | The ID of the asset model to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String clientToken = "clientToken_example"; // String | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
    try {
      DeleteAssetModelResponse result = apiInstance.deleteAssetModel(assetModelId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, clientToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteAssetModel");
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
| **assetModelId** | **String**| The ID of the asset model to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **clientToken** | **String**| A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. | [optional] |

### Return type

[**DeleteAssetModelResponse**](DeleteAssetModelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ConflictingOperationException |  -  |

<a id="deleteDashboard"></a>
# **deleteDashboard**
> Object deleteDashboard(dashboardId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, clientToken)



Deletes a dashboard from IoT SiteWise Monitor.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String dashboardId = "dashboardId_example"; // String | The ID of the dashboard to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String clientToken = "clientToken_example"; // String | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
    try {
      Object result = apiInstance.deleteDashboard(dashboardId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, clientToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteDashboard");
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
| **dashboardId** | **String**| The ID of the dashboard to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **clientToken** | **String**| A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. | [optional] |

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
| **204** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |

<a id="deleteGateway"></a>
# **deleteGateway**
> deleteGateway(gatewayId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes a gateway from IoT SiteWise. When you delete a gateway, some of the gateway&#39;s files remain in your gateway&#39;s file system.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String gatewayId = "gatewayId_example"; // String | The ID of the gateway to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteGateway(gatewayId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteGateway");
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
| **gatewayId** | **String**| The ID of the gateway to delete. | |
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
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |

<a id="deletePortal"></a>
# **deletePortal**
> DeletePortalResponse deletePortal(portalId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, clientToken)



Deletes a portal from IoT SiteWise Monitor.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String portalId = "portalId_example"; // String | The ID of the portal to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String clientToken = "clientToken_example"; // String | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
    try {
      DeletePortalResponse result = apiInstance.deletePortal(portalId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, clientToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deletePortal");
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
| **portalId** | **String**| The ID of the portal to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **clientToken** | **String**| A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. | [optional] |

### Return type

[**DeletePortalResponse**](DeletePortalResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ConflictingOperationException |  -  |

<a id="deleteProject"></a>
# **deleteProject**
> Object deleteProject(projectId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, clientToken)



Deletes a project from IoT SiteWise Monitor.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectId = "projectId_example"; // String | The ID of the project.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String clientToken = "clientToken_example"; // String | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
    try {
      Object result = apiInstance.deleteProject(projectId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, clientToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteProject");
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
| **projectId** | **String**| The ID of the project. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **clientToken** | **String**| A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. | [optional] |

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
| **204** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |

<a id="deleteTimeSeries"></a>
# **deleteTimeSeries**
> deleteTimeSeries(associateTimeSeriesToAssetPropertyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, alias, assetId, propertyId)



&lt;p&gt;Deletes a time series (data stream). If you delete a time series that&#39;s associated with an asset property, the asset property still exists, but the time series will no longer be associated with this asset property.&lt;/p&gt; &lt;p&gt;To identify a time series, do one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the time series isn&#39;t associated with an asset property, specify the &lt;code&gt;alias&lt;/code&gt; of the time series.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the time series is associated with an asset property, specify one of the following: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;alias&lt;/code&gt; of the time series.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; that identifies the asset property.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt;

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    AssociateTimeSeriesToAssetPropertyRequest associateTimeSeriesToAssetPropertyRequest = new AssociateTimeSeriesToAssetPropertyRequest(); // AssociateTimeSeriesToAssetPropertyRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String alias = "alias_example"; // String | The alias that identifies the time series.
    String assetId = "assetId_example"; // String | The ID of the asset in which the asset property was created.
    String propertyId = "propertyId_example"; // String | The ID of the asset property.
    try {
      apiInstance.deleteTimeSeries(associateTimeSeriesToAssetPropertyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, alias, assetId, propertyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteTimeSeries");
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
| **associateTimeSeriesToAssetPropertyRequest** | [**AssociateTimeSeriesToAssetPropertyRequest**](AssociateTimeSeriesToAssetPropertyRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **alias** | **String**| The alias that identifies the time series. | [optional] |
| **assetId** | **String**| The ID of the asset in which the asset property was created. | [optional] |
| **propertyId** | **String**| The ID of the asset property. | [optional] |

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
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ConflictingOperationException |  -  |

<a id="describeAccessPolicy"></a>
# **describeAccessPolicy**
> DescribeAccessPolicyResponse describeAccessPolicy(accessPolicyId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Describes an access policy, which specifies an identity&#39;s access to an IoT SiteWise Monitor portal or project.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accessPolicyId = "accessPolicyId_example"; // String | The ID of the access policy.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeAccessPolicyResponse result = apiInstance.describeAccessPolicy(accessPolicyId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeAccessPolicy");
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
| **accessPolicyId** | **String**| The ID of the access policy. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeAccessPolicyResponse**](DescribeAccessPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |

<a id="describeAsset"></a>
# **describeAsset**
> DescribeAssetResponse describeAsset(assetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, excludeProperties)



Retrieves information about an asset.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String assetId = "assetId_example"; // String | The ID of the asset.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Boolean excludeProperties = true; // Boolean |  Whether or not to exclude asset properties from the response. 
    try {
      DescribeAssetResponse result = apiInstance.describeAsset(assetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, excludeProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeAsset");
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
| **assetId** | **String**| The ID of the asset. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **excludeProperties** | **Boolean**|  Whether or not to exclude asset properties from the response.  | [optional] |

### Return type

[**DescribeAssetResponse**](DescribeAssetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |

<a id="describeAssetModel"></a>
# **describeAssetModel**
> DescribeAssetModelResponse describeAssetModel(assetModelId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, excludeProperties)



Retrieves information about an asset model.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String assetModelId = "assetModelId_example"; // String | The ID of the asset model.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Boolean excludeProperties = true; // Boolean |  Whether or not to exclude asset model properties from the response. 
    try {
      DescribeAssetModelResponse result = apiInstance.describeAssetModel(assetModelId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, excludeProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeAssetModel");
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
| **assetModelId** | **String**| The ID of the asset model. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **excludeProperties** | **Boolean**|  Whether or not to exclude asset model properties from the response.  | [optional] |

### Return type

[**DescribeAssetModelResponse**](DescribeAssetModelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |

<a id="describeAssetProperty"></a>
# **describeAssetProperty**
> DescribeAssetPropertyResponse describeAssetProperty(assetId, propertyId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Retrieves information about an asset property.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When you call this operation for an attribute property, this response includes the default attribute value that you define in the asset model. If you update the default value in the model, this operation&#39;s response includes the new default value.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation doesn&#39;t return the value of the asset property. To get the value of an asset property, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetAssetPropertyValue.html\&quot;&gt;GetAssetPropertyValue&lt;/a&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String assetId = "assetId_example"; // String | The ID of the asset.
    String propertyId = "propertyId_example"; // String | The ID of the asset property.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeAssetPropertyResponse result = apiInstance.describeAssetProperty(assetId, propertyId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeAssetProperty");
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
| **assetId** | **String**| The ID of the asset. | |
| **propertyId** | **String**| The ID of the asset property. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeAssetPropertyResponse**](DescribeAssetPropertyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |

<a id="describeBulkImportJob"></a>
# **describeBulkImportJob**
> DescribeBulkImportJobResponse describeBulkImportJob(jobId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves information about a bulk import job request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/DescribeBulkImportJob.html\&quot;&gt;Describe a bulk import job (CLI)&lt;/a&gt; in the &lt;i&gt;Amazon Simple Storage Service User Guide&lt;/i&gt;.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String jobId = "jobId_example"; // String | The ID of the job.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeBulkImportJobResponse result = apiInstance.describeBulkImportJob(jobId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeBulkImportJob");
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
| **jobId** | **String**| The ID of the job. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeBulkImportJobResponse**](DescribeBulkImportJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |

<a id="describeDashboard"></a>
# **describeDashboard**
> DescribeDashboardResponse describeDashboard(dashboardId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves information about a dashboard.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String dashboardId = "dashboardId_example"; // String | The ID of the dashboard.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeDashboardResponse result = apiInstance.describeDashboard(dashboardId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeDashboard");
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
| **dashboardId** | **String**| The ID of the dashboard. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeDashboardResponse**](DescribeDashboardResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |

<a id="describeDefaultEncryptionConfiguration"></a>
# **describeDefaultEncryptionConfiguration**
> DescribeDefaultEncryptionConfigurationResponse describeDefaultEncryptionConfiguration(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves information about the default encryption configuration for the Amazon Web Services account in the default or specified Region. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html\&quot;&gt;Key management&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeDefaultEncryptionConfigurationResponse result = apiInstance.describeDefaultEncryptionConfiguration(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeDefaultEncryptionConfiguration");
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
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeDefaultEncryptionConfigurationResponse**](DescribeDefaultEncryptionConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ThrottlingException |  -  |

<a id="describeGateway"></a>
# **describeGateway**
> DescribeGatewayResponse describeGateway(gatewayId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves information about a gateway.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String gatewayId = "gatewayId_example"; // String | The ID of the gateway device.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeGatewayResponse result = apiInstance.describeGateway(gatewayId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeGateway");
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
| **gatewayId** | **String**| The ID of the gateway device. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeGatewayResponse**](DescribeGatewayResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |

<a id="describeGatewayCapabilityConfiguration"></a>
# **describeGatewayCapabilityConfiguration**
> DescribeGatewayCapabilityConfigurationResponse describeGatewayCapabilityConfiguration(gatewayId, capabilityNamespace, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves information about a gateway capability configuration. Each gateway capability defines data sources for a gateway. A capability configuration can contain multiple data source configurations. If you define OPC-UA sources for a gateway in the IoT SiteWise console, all of your OPC-UA sources are stored in one capability configuration. To list all capability configurations for a gateway, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGateway.html\&quot;&gt;DescribeGateway&lt;/a&gt;.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String gatewayId = "gatewayId_example"; // String | The ID of the gateway that defines the capability configuration.
    String capabilityNamespace = "capabilityNamespace_example"; // String | The namespace of the capability configuration. For example, if you configure OPC-UA sources from the IoT SiteWise console, your OPC-UA capability configuration has the namespace <code>iotsitewise:opcuacollector:version</code>, where <code>version</code> is a number such as <code>1</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeGatewayCapabilityConfigurationResponse result = apiInstance.describeGatewayCapabilityConfiguration(gatewayId, capabilityNamespace, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeGatewayCapabilityConfiguration");
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
| **gatewayId** | **String**| The ID of the gateway that defines the capability configuration. | |
| **capabilityNamespace** | **String**| The namespace of the capability configuration. For example, if you configure OPC-UA sources from the IoT SiteWise console, your OPC-UA capability configuration has the namespace &lt;code&gt;iotsitewise:opcuacollector:version&lt;/code&gt;, where &lt;code&gt;version&lt;/code&gt; is a number such as &lt;code&gt;1&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeGatewayCapabilityConfigurationResponse**](DescribeGatewayCapabilityConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |

<a id="describeLoggingOptions"></a>
# **describeLoggingOptions**
> DescribeLoggingOptionsResponse describeLoggingOptions(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves the current IoT SiteWise logging options.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeLoggingOptionsResponse result = apiInstance.describeLoggingOptions(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeLoggingOptions");
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
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeLoggingOptionsResponse**](DescribeLoggingOptionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ThrottlingException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ResourceNotFoundException |  -  |

<a id="describePortal"></a>
# **describePortal**
> DescribePortalResponse describePortal(portalId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves information about a portal.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String portalId = "portalId_example"; // String | The ID of the portal.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribePortalResponse result = apiInstance.describePortal(portalId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describePortal");
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
| **portalId** | **String**| The ID of the portal. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribePortalResponse**](DescribePortalResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |

<a id="describeProject"></a>
# **describeProject**
> DescribeProjectResponse describeProject(projectId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves information about a project.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectId = "projectId_example"; // String | The ID of the project.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeProjectResponse result = apiInstance.describeProject(projectId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeProject");
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
| **projectId** | **String**| The ID of the project. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeProjectResponse**](DescribeProjectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |

<a id="describeStorageConfiguration"></a>
# **describeStorageConfiguration**
> DescribeStorageConfigurationResponse describeStorageConfiguration(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves information about the storage configuration for IoT SiteWise.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeStorageConfigurationResponse result = apiInstance.describeStorageConfiguration(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeStorageConfiguration");
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
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeStorageConfigurationResponse**](DescribeStorageConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | ConflictingOperationException |  -  |

<a id="describeTimeSeries"></a>
# **describeTimeSeries**
> DescribeTimeSeriesResponse describeTimeSeries(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, alias, assetId, propertyId)



&lt;p&gt;Retrieves information about a time series (data stream).&lt;/p&gt; &lt;p&gt;To identify a time series, do one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the time series isn&#39;t associated with an asset property, specify the &lt;code&gt;alias&lt;/code&gt; of the time series.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the time series is associated with an asset property, specify one of the following: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;alias&lt;/code&gt; of the time series.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; that identifies the asset property.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt;

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String alias = "alias_example"; // String | The alias that identifies the time series.
    String assetId = "assetId_example"; // String | The ID of the asset in which the asset property was created.
    String propertyId = "propertyId_example"; // String | The ID of the asset property.
    try {
      DescribeTimeSeriesResponse result = apiInstance.describeTimeSeries(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, alias, assetId, propertyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeTimeSeries");
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
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **alias** | **String**| The alias that identifies the time series. | [optional] |
| **assetId** | **String**| The ID of the asset in which the asset property was created. | [optional] |
| **propertyId** | **String**| The ID of the asset property. | [optional] |

### Return type

[**DescribeTimeSeriesResponse**](DescribeTimeSeriesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |

<a id="disassociateAssets"></a>
# **disassociateAssets**
> disassociateAssets(assetId, disassociateAssetsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Disassociates a child asset from the given parent asset through a hierarchy defined in the parent asset&#39;s model.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String assetId = "assetId_example"; // String | The ID of the parent asset from which to disassociate the child asset.
    DisassociateAssetsRequest disassociateAssetsRequest = new DisassociateAssetsRequest(); // DisassociateAssetsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.disassociateAssets(assetId, disassociateAssetsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#disassociateAssets");
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
| **assetId** | **String**| The ID of the parent asset from which to disassociate the child asset. | |
| **disassociateAssetsRequest** | [**DisassociateAssetsRequest**](DisassociateAssetsRequest.md)|  | |
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
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ConflictingOperationException |  -  |

<a id="disassociateTimeSeriesFromAssetProperty"></a>
# **disassociateTimeSeriesFromAssetProperty**
> disassociateTimeSeriesFromAssetProperty(alias, assetId, propertyId, associateTimeSeriesToAssetPropertyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Disassociates a time series (data stream) from an asset property.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String alias = "alias_example"; // String | The alias that identifies the time series.
    String assetId = "assetId_example"; // String | The ID of the asset in which the asset property was created.
    String propertyId = "propertyId_example"; // String | The ID of the asset property.
    AssociateTimeSeriesToAssetPropertyRequest associateTimeSeriesToAssetPropertyRequest = new AssociateTimeSeriesToAssetPropertyRequest(); // AssociateTimeSeriesToAssetPropertyRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.disassociateTimeSeriesFromAssetProperty(alias, assetId, propertyId, associateTimeSeriesToAssetPropertyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#disassociateTimeSeriesFromAssetProperty");
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
| **alias** | **String**| The alias that identifies the time series. | |
| **assetId** | **String**| The ID of the asset in which the asset property was created. | |
| **propertyId** | **String**| The ID of the asset property. | |
| **associateTimeSeriesToAssetPropertyRequest** | [**AssociateTimeSeriesToAssetPropertyRequest**](AssociateTimeSeriesToAssetPropertyRequest.md)|  | |
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
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ConflictingOperationException |  -  |

<a id="getAssetPropertyAggregates"></a>
# **getAssetPropertyAggregates**
> GetAssetPropertyAggregatesResponse getAssetPropertyAggregates(aggregateTypes, resolution, startDate, endDate, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, assetId, propertyId, propertyAlias, qualities, timeOrdering, nextToken, maxResults)



&lt;p&gt;Gets aggregated values for an asset property. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#aggregates\&quot;&gt;Querying aggregates&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To identify an asset property, you must specify one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; of an asset property.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;propertyAlias&lt;/code&gt;, which is a data stream alias (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). To define an asset property&#39;s alias, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\&quot;&gt;UpdateAssetProperty&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    List<AggregateType> aggregateTypes = Arrays.asList(); // List<AggregateType> | The data aggregating function.
    String resolution = "resolution_example"; // String | The time interval over which to aggregate data.
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String assetId = "assetId_example"; // String | The ID of the asset.
    String propertyId = "propertyId_example"; // String | The ID of the asset property.
    String propertyAlias = "propertyAlias_example"; // String | The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.
    List<Quality> qualities = Arrays.asList(); // List<Quality> | The quality by which to filter asset data.
    String timeOrdering = "ASCENDING"; // String | <p>The chronological sorting order of the requested information.</p> <p>Default: <code>ASCENDING</code> </p>
    String nextToken = "nextToken_example"; // String | The token to be used for the next set of paginated results.
    Integer maxResults = 56; // Integer | <p>The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.</p> <ul> <li> <p>The size of the result set is equal to 1 MB.</p> </li> <li> <p>The number of data points in the result set is equal to the value of <code>maxResults</code>. The maximum value of <code>maxResults</code> is 250.</p> </li> </ul>
    try {
      GetAssetPropertyAggregatesResponse result = apiInstance.getAssetPropertyAggregates(aggregateTypes, resolution, startDate, endDate, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, assetId, propertyId, propertyAlias, qualities, timeOrdering, nextToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAssetPropertyAggregates");
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
| **aggregateTypes** | [**List&lt;AggregateType&gt;**](AggregateType.md)| The data aggregating function. | |
| **resolution** | **String**| The time interval over which to aggregate data. | |
| **startDate** | **OffsetDateTime**| The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time. | |
| **endDate** | **OffsetDateTime**| The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **assetId** | **String**| The ID of the asset. | [optional] |
| **propertyId** | **String**| The ID of the asset property. | [optional] |
| **propertyAlias** | **String**| The alias that identifies the property, such as an OPC-UA server data stream path (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\&quot;&gt;Mapping industrial data streams to asset properties&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;. | [optional] |
| **qualities** | [**List&lt;Quality&gt;**](Quality.md)| The quality by which to filter asset data. | [optional] |
| **timeOrdering** | **String**| &lt;p&gt;The chronological sorting order of the requested information.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;ASCENDING&lt;/code&gt; &lt;/p&gt; | [optional] [enum: ASCENDING, DESCENDING] |
| **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] |
| **maxResults** | **Integer**| &lt;p&gt;The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The size of the result set is equal to 1 MB.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The number of data points in the result set is equal to the value of &lt;code&gt;maxResults&lt;/code&gt;. The maximum value of &lt;code&gt;maxResults&lt;/code&gt; is 250.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |

### Return type

[**GetAssetPropertyAggregatesResponse**](GetAssetPropertyAggregatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ServiceUnavailableException |  -  |

<a id="getAssetPropertyValue"></a>
# **getAssetPropertyValue**
> GetAssetPropertyValueResponse getAssetPropertyValue(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, assetId, propertyId, propertyAlias)



&lt;p&gt;Gets an asset property&#39;s current value. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#current-values\&quot;&gt;Querying current values&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To identify an asset property, you must specify one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; of an asset property.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;propertyAlias&lt;/code&gt;, which is a data stream alias (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). To define an asset property&#39;s alias, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\&quot;&gt;UpdateAssetProperty&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String assetId = "assetId_example"; // String | The ID of the asset.
    String propertyId = "propertyId_example"; // String | The ID of the asset property.
    String propertyAlias = "propertyAlias_example"; // String | The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.
    try {
      GetAssetPropertyValueResponse result = apiInstance.getAssetPropertyValue(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, assetId, propertyId, propertyAlias);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAssetPropertyValue");
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
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **assetId** | **String**| The ID of the asset. | [optional] |
| **propertyId** | **String**| The ID of the asset property. | [optional] |
| **propertyAlias** | **String**| The alias that identifies the property, such as an OPC-UA server data stream path (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\&quot;&gt;Mapping industrial data streams to asset properties&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;. | [optional] |

### Return type

[**GetAssetPropertyValueResponse**](GetAssetPropertyValueResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ServiceUnavailableException |  -  |

<a id="getAssetPropertyValueHistory"></a>
# **getAssetPropertyValueHistory**
> GetAssetPropertyValueHistoryResponse getAssetPropertyValueHistory(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, assetId, propertyId, propertyAlias, startDate, endDate, qualities, timeOrdering, nextToken, maxResults)



&lt;p&gt;Gets the history of an asset property&#39;s values. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#historical-values\&quot;&gt;Querying historical values&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To identify an asset property, you must specify one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; of an asset property.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;propertyAlias&lt;/code&gt;, which is a data stream alias (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). To define an asset property&#39;s alias, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\&quot;&gt;UpdateAssetProperty&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String assetId = "assetId_example"; // String | The ID of the asset.
    String propertyId = "propertyId_example"; // String | The ID of the asset property.
    String propertyAlias = "propertyAlias_example"; // String | The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.
    List<Quality> qualities = Arrays.asList(); // List<Quality> | The quality by which to filter asset data.
    String timeOrdering = "ASCENDING"; // String | <p>The chronological sorting order of the requested information.</p> <p>Default: <code>ASCENDING</code> </p>
    String nextToken = "nextToken_example"; // String | The token to be used for the next set of paginated results.
    Integer maxResults = 56; // Integer | <p>The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.</p> <ul> <li> <p>The size of the result set is equal to 4 MB.</p> </li> <li> <p>The number of data points in the result set is equal to the value of <code>maxResults</code>. The maximum value of <code>maxResults</code> is 20000.</p> </li> </ul>
    try {
      GetAssetPropertyValueHistoryResponse result = apiInstance.getAssetPropertyValueHistory(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, assetId, propertyId, propertyAlias, startDate, endDate, qualities, timeOrdering, nextToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAssetPropertyValueHistory");
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
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **assetId** | **String**| The ID of the asset. | [optional] |
| **propertyId** | **String**| The ID of the asset property. | [optional] |
| **propertyAlias** | **String**| The alias that identifies the property, such as an OPC-UA server data stream path (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\&quot;&gt;Mapping industrial data streams to asset properties&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;. | [optional] |
| **startDate** | **OffsetDateTime**| The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time. | [optional] |
| **endDate** | **OffsetDateTime**| The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time. | [optional] |
| **qualities** | [**List&lt;Quality&gt;**](Quality.md)| The quality by which to filter asset data. | [optional] |
| **timeOrdering** | **String**| &lt;p&gt;The chronological sorting order of the requested information.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;ASCENDING&lt;/code&gt; &lt;/p&gt; | [optional] [enum: ASCENDING, DESCENDING] |
| **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] |
| **maxResults** | **Integer**| &lt;p&gt;The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The size of the result set is equal to 4 MB.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The number of data points in the result set is equal to the value of &lt;code&gt;maxResults&lt;/code&gt;. The maximum value of &lt;code&gt;maxResults&lt;/code&gt; is 20000.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |

### Return type

[**GetAssetPropertyValueHistoryResponse**](GetAssetPropertyValueHistoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ServiceUnavailableException |  -  |

<a id="getInterpolatedAssetPropertyValues"></a>
# **getInterpolatedAssetPropertyValues**
> GetInterpolatedAssetPropertyValuesResponse getInterpolatedAssetPropertyValues(startTimeInSeconds, endTimeInSeconds, quality, intervalInSeconds, type, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, assetId, propertyId, propertyAlias, startTimeOffsetInNanos, endTimeOffsetInNanos, nextToken, maxResults, intervalWindowInSeconds)



&lt;p&gt;Get interpolated values for an asset property for a specified time interval, during a period of time. If your time series is missing data points during the specified time interval, you can use interpolation to estimate the missing data.&lt;/p&gt; &lt;p&gt;For example, you can use this operation to return the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days.&lt;/p&gt; &lt;p&gt;To identify an asset property, you must specify one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; of an asset property.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;propertyAlias&lt;/code&gt;, which is a data stream alias (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). To define an asset property&#39;s alias, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\&quot;&gt;UpdateAssetProperty&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer startTimeInSeconds = 56; // Integer | The exclusive start of the range from which to interpolate data, expressed in seconds in Unix epoch time.
    Integer endTimeInSeconds = 56; // Integer | The inclusive end of the range from which to interpolate data, expressed in seconds in Unix epoch time.
    String quality = "GOOD"; // String | The quality of the asset property value. You can use this parameter as a filter to choose only the asset property values that have a specific quality.
    Integer intervalInSeconds = 56; // Integer | The time interval in seconds over which to interpolate data. Each interval starts when the previous one ends.
    String type = "type_example"; // String | <p>The interpolation type.</p> <p>Valid values: <code>LINEAR_INTERPOLATION | LOCF_INTERPOLATION</code> </p> <ul> <li> <p> <code>LINEAR_INTERPOLATION</code> – Estimates missing data using <a href=\"https://en.wikipedia.org/wiki/Linear_interpolation\">linear interpolation</a>.</p> <p>For example, you can use this operation to return the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days. If the interpolation starts July 1, 2021, at 9 AM, IoT SiteWise returns the first interpolated value on July 2, 2021, at 9 AM, the second interpolated value on July 3, 2021, at 9 AM, and so on.</p> </li> <li> <p> <code>LOCF_INTERPOLATION</code> – Estimates missing data using last observation carried forward interpolation</p> <p>If no data point is found for an interval, IoT SiteWise returns the last observed data point for the previous interval and carries forward this interpolated value until a new data point is found.</p> <p>For example, you can get the state of an on-off valve every 24 hours over a duration of 7 days. If the interpolation starts July 1, 2021, at 9 AM, IoT SiteWise returns the last observed data point between July 1, 2021, at 9 AM and July 2, 2021, at 9 AM as the first interpolated value. If a data point isn't found after 9 AM on July 2, 2021, IoT SiteWise uses the same interpolated value for the rest of the days.</p> </li> </ul>
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String assetId = "assetId_example"; // String | The ID of the asset.
    String propertyId = "propertyId_example"; // String | The ID of the asset property.
    String propertyAlias = "propertyAlias_example"; // String | The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.
    Integer startTimeOffsetInNanos = 56; // Integer | The nanosecond offset converted from <code>startTimeInSeconds</code>.
    Integer endTimeOffsetInNanos = 56; // Integer | The nanosecond offset converted from <code>endTimeInSeconds</code>.
    String nextToken = "nextToken_example"; // String | The token to be used for the next set of paginated results.
    Integer maxResults = 56; // Integer | The maximum number of results to return for each paginated request. If not specified, the default value is 10.
    Integer intervalWindowInSeconds = 56; // Integer | <p>The query interval for the window, in seconds. IoT SiteWise computes each interpolated value by using data points from the timestamp of each interval, minus the window to the timestamp of each interval plus the window. If not specified, the window ranges between the start time minus the interval and the end time plus the interval.</p> <note> <ul> <li> <p>If you specify a value for the <code>intervalWindowInSeconds</code> parameter, the value for the <code>type</code> parameter must be <code>LINEAR_INTERPOLATION</code>.</p> </li> <li> <p>If a data point isn't found during the specified query window, IoT SiteWise won't return an interpolated value for the interval. This indicates that there's a gap in the ingested data points.</p> </li> </ul> </note> <p>For example, you can get the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days. If the interpolation starts on July 1, 2021, at 9 AM with a window of 2 hours, IoT SiteWise uses the data points from 7 AM (9 AM minus 2 hours) to 11 AM (9 AM plus 2 hours) on July 2, 2021 to compute the first interpolated value. Next, IoT SiteWise uses the data points from 7 AM (9 AM minus 2 hours) to 11 AM (9 AM plus 2 hours) on July 3, 2021 to compute the second interpolated value, and so on. </p>
    try {
      GetInterpolatedAssetPropertyValuesResponse result = apiInstance.getInterpolatedAssetPropertyValues(startTimeInSeconds, endTimeInSeconds, quality, intervalInSeconds, type, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, assetId, propertyId, propertyAlias, startTimeOffsetInNanos, endTimeOffsetInNanos, nextToken, maxResults, intervalWindowInSeconds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getInterpolatedAssetPropertyValues");
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
| **startTimeInSeconds** | **Integer**| The exclusive start of the range from which to interpolate data, expressed in seconds in Unix epoch time. | |
| **endTimeInSeconds** | **Integer**| The inclusive end of the range from which to interpolate data, expressed in seconds in Unix epoch time. | |
| **quality** | **String**| The quality of the asset property value. You can use this parameter as a filter to choose only the asset property values that have a specific quality. | [enum: GOOD, BAD, UNCERTAIN] |
| **intervalInSeconds** | **Integer**| The time interval in seconds over which to interpolate data. Each interval starts when the previous one ends. | |
| **type** | **String**| &lt;p&gt;The interpolation type.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;LINEAR_INTERPOLATION | LOCF_INTERPOLATION&lt;/code&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LINEAR_INTERPOLATION&lt;/code&gt; – Estimates missing data using &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/Linear_interpolation\&quot;&gt;linear interpolation&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For example, you can use this operation to return the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days. If the interpolation starts July 1, 2021, at 9 AM, IoT SiteWise returns the first interpolated value on July 2, 2021, at 9 AM, the second interpolated value on July 3, 2021, at 9 AM, and so on.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LOCF_INTERPOLATION&lt;/code&gt; – Estimates missing data using last observation carried forward interpolation&lt;/p&gt; &lt;p&gt;If no data point is found for an interval, IoT SiteWise returns the last observed data point for the previous interval and carries forward this interpolated value until a new data point is found.&lt;/p&gt; &lt;p&gt;For example, you can get the state of an on-off valve every 24 hours over a duration of 7 days. If the interpolation starts July 1, 2021, at 9 AM, IoT SiteWise returns the last observed data point between July 1, 2021, at 9 AM and July 2, 2021, at 9 AM as the first interpolated value. If a data point isn&#39;t found after 9 AM on July 2, 2021, IoT SiteWise uses the same interpolated value for the rest of the days.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **assetId** | **String**| The ID of the asset. | [optional] |
| **propertyId** | **String**| The ID of the asset property. | [optional] |
| **propertyAlias** | **String**| The alias that identifies the property, such as an OPC-UA server data stream path (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\&quot;&gt;Mapping industrial data streams to asset properties&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;. | [optional] |
| **startTimeOffsetInNanos** | **Integer**| The nanosecond offset converted from &lt;code&gt;startTimeInSeconds&lt;/code&gt;. | [optional] |
| **endTimeOffsetInNanos** | **Integer**| The nanosecond offset converted from &lt;code&gt;endTimeInSeconds&lt;/code&gt;. | [optional] |
| **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return for each paginated request. If not specified, the default value is 10. | [optional] |
| **intervalWindowInSeconds** | **Integer**| &lt;p&gt;The query interval for the window, in seconds. IoT SiteWise computes each interpolated value by using data points from the timestamp of each interval, minus the window to the timestamp of each interval plus the window. If not specified, the window ranges between the start time minus the interval and the end time plus the interval.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you specify a value for the &lt;code&gt;intervalWindowInSeconds&lt;/code&gt; parameter, the value for the &lt;code&gt;type&lt;/code&gt; parameter must be &lt;code&gt;LINEAR_INTERPOLATION&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If a data point isn&#39;t found during the specified query window, IoT SiteWise won&#39;t return an interpolated value for the interval. This indicates that there&#39;s a gap in the ingested data points.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p&gt;For example, you can get the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days. If the interpolation starts on July 1, 2021, at 9 AM with a window of 2 hours, IoT SiteWise uses the data points from 7 AM (9 AM minus 2 hours) to 11 AM (9 AM plus 2 hours) on July 2, 2021 to compute the first interpolated value. Next, IoT SiteWise uses the data points from 7 AM (9 AM minus 2 hours) to 11 AM (9 AM plus 2 hours) on July 3, 2021 to compute the second interpolated value, and so on. &lt;/p&gt; | [optional] |

### Return type

[**GetInterpolatedAssetPropertyValuesResponse**](GetInterpolatedAssetPropertyValuesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ServiceUnavailableException |  -  |

<a id="listAccessPolicies"></a>
# **listAccessPolicies**
> ListAccessPoliciesResponse listAccessPolicies(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, identityType, identityId, resourceType, resourceId, iamArn, nextToken, maxResults)



Retrieves a paginated list of access policies for an identity (an IAM Identity Center user, an IAM Identity Center group, or an IAM user) or an IoT SiteWise Monitor resource (a portal or project).

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String identityType = "USER"; // String | The type of identity (IAM Identity Center user, IAM Identity Center group, or IAM user). This parameter is required if you specify <code>identityId</code>.
    String identityId = "identityId_example"; // String | The ID of the identity. This parameter is required if you specify <code>USER</code> or <code>GROUP</code> for <code>identityType</code>.
    String resourceType = "PORTAL"; // String | The type of resource (portal or project). This parameter is required if you specify <code>resourceId</code>.
    String resourceId = "resourceId_example"; // String | The ID of the resource. This parameter is required if you specify <code>resourceType</code>.
    String iamArn = "iamArn_example"; // String | The ARN of the IAM user. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html\">IAM ARNs</a> in the <i>IAM User Guide</i>. This parameter is required if you specify <code>IAM</code> for <code>identityType</code>.
    String nextToken = "nextToken_example"; // String | The token to be used for the next set of paginated results.
    Integer maxResults = 56; // Integer | <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
    try {
      ListAccessPoliciesResponse result = apiInstance.listAccessPolicies(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, identityType, identityId, resourceType, resourceId, iamArn, nextToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAccessPolicies");
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
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **identityType** | **String**| The type of identity (IAM Identity Center user, IAM Identity Center group, or IAM user). This parameter is required if you specify &lt;code&gt;identityId&lt;/code&gt;. | [optional] [enum: USER, GROUP, IAM] |
| **identityId** | **String**| The ID of the identity. This parameter is required if you specify &lt;code&gt;USER&lt;/code&gt; or &lt;code&gt;GROUP&lt;/code&gt; for &lt;code&gt;identityType&lt;/code&gt;. | [optional] |
| **resourceType** | **String**| The type of resource (portal or project). This parameter is required if you specify &lt;code&gt;resourceId&lt;/code&gt;. | [optional] [enum: PORTAL, PROJECT] |
| **resourceId** | **String**| The ID of the resource. This parameter is required if you specify &lt;code&gt;resourceType&lt;/code&gt;. | [optional] |
| **iamArn** | **String**| The ARN of the IAM user. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html\&quot;&gt;IAM ARNs&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. This parameter is required if you specify &lt;code&gt;IAM&lt;/code&gt; for &lt;code&gt;identityType&lt;/code&gt;. | [optional] |
| **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] |
| **maxResults** | **Integer**| &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt; | [optional] |

### Return type

[**ListAccessPoliciesResponse**](ListAccessPoliciesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ThrottlingException |  -  |

<a id="listAssetModelProperties"></a>
# **listAssetModelProperties**
> ListAssetModelPropertiesResponse listAssetModelProperties(assetModelId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, filter)



Retrieves a paginated list of properties associated with an asset model. If you update properties associated with the model before you finish listing all the properties, you need to start all over again.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String assetModelId = "assetModelId_example"; // String | The ID of the asset model.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | The token to be used for the next set of paginated results.
    Integer maxResults = 56; // Integer | The maximum number of results to return for each paginated request. If not specified, the default value is 50.
    String filter = "ALL"; // String | <p> Filters the requested list of asset model properties. You can choose one of the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all asset model properties for a given asset model ID. </p> </li> <li> <p> <code>BASE</code> – The list includes only base asset model properties for a given asset model ID. </p> </li> </ul> <p>Default: <code>BASE</code> </p>
    try {
      ListAssetModelPropertiesResponse result = apiInstance.listAssetModelProperties(assetModelId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAssetModelProperties");
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
| **assetModelId** | **String**| The ID of the asset model. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return for each paginated request. If not specified, the default value is 50. | [optional] |
| **filter** | **String**| &lt;p&gt; Filters the requested list of asset model properties. You can choose one of the following options:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ALL&lt;/code&gt; – The list includes all asset model properties for a given asset model ID. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;BASE&lt;/code&gt; – The list includes only base asset model properties for a given asset model ID. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: &lt;code&gt;BASE&lt;/code&gt; &lt;/p&gt; | [optional] [enum: ALL, BASE] |

### Return type

[**ListAssetModelPropertiesResponse**](ListAssetModelPropertiesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |

<a id="listAssetModels"></a>
# **listAssetModels**
> ListAssetModelsResponse listAssetModels(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults)



Retrieves a paginated list of summaries of all asset models.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | The token to be used for the next set of paginated results.
    Integer maxResults = 56; // Integer | <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
    try {
      ListAssetModelsResponse result = apiInstance.listAssetModels(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAssetModels");
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
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] |
| **maxResults** | **Integer**| &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt; | [optional] |

### Return type

[**ListAssetModelsResponse**](ListAssetModelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ThrottlingException |  -  |

<a id="listAssetProperties"></a>
# **listAssetProperties**
> ListAssetPropertiesResponse listAssetProperties(assetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, filter)



Retrieves a paginated list of properties associated with an asset. If you update properties associated with the model before you finish listing all the properties, you need to start all over again.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String assetId = "assetId_example"; // String | The ID of the asset.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | The token to be used for the next set of paginated results.
    Integer maxResults = 56; // Integer | The maximum number of results to return for each paginated request. If not specified, the default value is 50.
    String filter = "ALL"; // String | <p> Filters the requested list of asset properties. You can choose one of the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all asset properties for a given asset model ID. </p> </li> <li> <p> <code>BASE</code> – The list includes only base asset properties for a given asset model ID. </p> </li> </ul> <p>Default: <code>BASE</code> </p>
    try {
      ListAssetPropertiesResponse result = apiInstance.listAssetProperties(assetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAssetProperties");
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
| **assetId** | **String**| The ID of the asset. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return for each paginated request. If not specified, the default value is 50. | [optional] |
| **filter** | **String**| &lt;p&gt; Filters the requested list of asset properties. You can choose one of the following options:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ALL&lt;/code&gt; – The list includes all asset properties for a given asset model ID. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;BASE&lt;/code&gt; – The list includes only base asset properties for a given asset model ID. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: &lt;code&gt;BASE&lt;/code&gt; &lt;/p&gt; | [optional] [enum: ALL, BASE] |

### Return type

[**ListAssetPropertiesResponse**](ListAssetPropertiesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |

<a id="listAssetRelationships"></a>
# **listAssetRelationships**
> ListAssetRelationshipsResponse listAssetRelationships(assetId, traversalType, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults)



Retrieves a paginated list of asset relationships for an asset. You can use this operation to identify an asset&#39;s root asset and all associated assets between that asset and its root.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String assetId = "assetId_example"; // String | The ID of the asset.
    String traversalType = "PATH_TO_ROOT"; // String | <p>The type of traversal to use to identify asset relationships. Choose the following option:</p> <ul> <li> <p> <code>PATH_TO_ROOT</code> – Identify the asset's parent assets up to the root asset. The asset that you specify in <code>assetId</code> is the first result in the list of <code>assetRelationshipSummaries</code>, and the root asset is the last result.</p> </li> </ul>
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | The token to be used for the next set of paginated results.
    Integer maxResults = 56; // Integer | The maximum number of results to return for each paginated request.
    try {
      ListAssetRelationshipsResponse result = apiInstance.listAssetRelationships(assetId, traversalType, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAssetRelationships");
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
| **assetId** | **String**| The ID of the asset. | |
| **traversalType** | **String**| &lt;p&gt;The type of traversal to use to identify asset relationships. Choose the following option:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PATH_TO_ROOT&lt;/code&gt; – Identify the asset&#39;s parent assets up to the root asset. The asset that you specify in &lt;code&gt;assetId&lt;/code&gt; is the first result in the list of &lt;code&gt;assetRelationshipSummaries&lt;/code&gt;, and the root asset is the last result.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [enum: PATH_TO_ROOT] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return for each paginated request. | [optional] |

### Return type

[**ListAssetRelationshipsResponse**](ListAssetRelationshipsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |

<a id="listAssets"></a>
# **listAssets**
> ListAssetsResponse listAssets(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, assetModelId, filter)



&lt;p&gt;Retrieves a paginated list of asset summaries.&lt;/p&gt; &lt;p&gt;You can use this operation to do the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;List assets based on a specific asset model.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;List top-level assets.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can&#39;t use this operation to list all assets. To retrieve summaries for all of your assets, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssetModels.html\&quot;&gt;ListAssetModels&lt;/a&gt; to get all of your asset model IDs. Then, use ListAssets to get all assets for each asset model.&lt;/p&gt;

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | The token to be used for the next set of paginated results.
    Integer maxResults = 56; // Integer | <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
    String assetModelId = "assetModelId_example"; // String | The ID of the asset model by which to filter the list of assets. This parameter is required if you choose <code>ALL</code> for <code>filter</code>.
    String filter = "ALL"; // String | <p>The filter for the requested list of assets. Choose one of the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all assets for a given asset model ID. The <code>assetModelId</code> parameter is required if you filter by <code>ALL</code>.</p> </li> <li> <p> <code>TOP_LEVEL</code> – The list includes only top-level assets in the asset hierarchy tree.</p> </li> </ul> <p>Default: <code>ALL</code> </p>
    try {
      ListAssetsResponse result = apiInstance.listAssets(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, assetModelId, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAssets");
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
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] |
| **maxResults** | **Integer**| &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt; | [optional] |
| **assetModelId** | **String**| The ID of the asset model by which to filter the list of assets. This parameter is required if you choose &lt;code&gt;ALL&lt;/code&gt; for &lt;code&gt;filter&lt;/code&gt;. | [optional] |
| **filter** | **String**| &lt;p&gt;The filter for the requested list of assets. Choose one of the following options:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ALL&lt;/code&gt; – The list includes all assets for a given asset model ID. The &lt;code&gt;assetModelId&lt;/code&gt; parameter is required if you filter by &lt;code&gt;ALL&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TOP_LEVEL&lt;/code&gt; – The list includes only top-level assets in the asset hierarchy tree.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: &lt;code&gt;ALL&lt;/code&gt; &lt;/p&gt; | [optional] [enum: ALL, TOP_LEVEL] |

### Return type

[**ListAssetsResponse**](ListAssetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |

<a id="listAssociatedAssets"></a>
# **listAssociatedAssets**
> ListAssociatedAssetsResponse listAssociatedAssets(assetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, hierarchyId, traversalDirection, nextToken, maxResults)



&lt;p&gt;Retrieves a paginated list of associated assets.&lt;/p&gt; &lt;p&gt;You can use this operation to do the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;List child assets associated to a parent asset by a hierarchy that you specify.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;List an asset&#39;s parent asset.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String assetId = "assetId_example"; // String | The ID of the asset to query.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String hierarchyId = "hierarchyId_example"; // String | <p>The ID of the hierarchy by which child assets are associated to the asset. To find a hierarchy ID, use the <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAsset.html\">DescribeAsset</a> or <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModel.html\">DescribeAssetModel</a> operations. This parameter is required if you choose <code>CHILD</code> for <code>traversalDirection</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html\">Asset hierarchies</a> in the <i>IoT SiteWise User Guide</i>.</p>
    String traversalDirection = "PARENT"; // String | <p>The direction to list associated assets. Choose one of the following options:</p> <ul> <li> <p> <code>CHILD</code> – The list includes all child assets associated to the asset. The <code>hierarchyId</code> parameter is required if you choose <code>CHILD</code>.</p> </li> <li> <p> <code>PARENT</code> – The list includes the asset's parent asset.</p> </li> </ul> <p>Default: <code>CHILD</code> </p>
    String nextToken = "nextToken_example"; // String | The token to be used for the next set of paginated results.
    Integer maxResults = 56; // Integer | <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
    try {
      ListAssociatedAssetsResponse result = apiInstance.listAssociatedAssets(assetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, hierarchyId, traversalDirection, nextToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAssociatedAssets");
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
| **assetId** | **String**| The ID of the asset to query. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **hierarchyId** | **String**| &lt;p&gt;The ID of the hierarchy by which child assets are associated to the asset. To find a hierarchy ID, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAsset.html\&quot;&gt;DescribeAsset&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModel.html\&quot;&gt;DescribeAssetModel&lt;/a&gt; operations. This parameter is required if you choose &lt;code&gt;CHILD&lt;/code&gt; for &lt;code&gt;traversalDirection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html\&quot;&gt;Asset hierarchies&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; | [optional] |
| **traversalDirection** | **String**| &lt;p&gt;The direction to list associated assets. Choose one of the following options:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CHILD&lt;/code&gt; – The list includes all child assets associated to the asset. The &lt;code&gt;hierarchyId&lt;/code&gt; parameter is required if you choose &lt;code&gt;CHILD&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PARENT&lt;/code&gt; – The list includes the asset&#39;s parent asset.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: &lt;code&gt;CHILD&lt;/code&gt; &lt;/p&gt; | [optional] [enum: PARENT, CHILD] |
| **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] |
| **maxResults** | **Integer**| &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt; | [optional] |

### Return type

[**ListAssociatedAssetsResponse**](ListAssociatedAssetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |

<a id="listBulkImportJobs"></a>
# **listBulkImportJobs**
> ListBulkImportJobsResponse listBulkImportJobs(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, filter)



Retrieves a paginated list of bulk import job requests. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ListBulkImportJobs.html\&quot;&gt;List bulk import jobs (CLI)&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | The token to be used for the next set of paginated results.
    Integer maxResults = 56; // Integer | The maximum number of results to return for each paginated request.
    String filter = "ALL"; // String | You can use a filter to select the bulk import jobs that you want to retrieve.
    try {
      ListBulkImportJobsResponse result = apiInstance.listBulkImportJobs(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listBulkImportJobs");
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
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return for each paginated request. | [optional] |
| **filter** | **String**| You can use a filter to select the bulk import jobs that you want to retrieve. | [optional] [enum: ALL, PENDING, RUNNING, CANCELLED, FAILED, COMPLETED_WITH_FAILURES, COMPLETED] |

### Return type

[**ListBulkImportJobsResponse**](ListBulkImportJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ThrottlingException |  -  |

<a id="listDashboards"></a>
# **listDashboards**
> ListDashboardsResponse listDashboards(projectId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults)



Retrieves a paginated list of dashboards for an IoT SiteWise Monitor project.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectId = "projectId_example"; // String | The ID of the project.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | The token to be used for the next set of paginated results.
    Integer maxResults = 56; // Integer | <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
    try {
      ListDashboardsResponse result = apiInstance.listDashboards(projectId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listDashboards");
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
| **projectId** | **String**| The ID of the project. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] |
| **maxResults** | **Integer**| &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt; | [optional] |

### Return type

[**ListDashboardsResponse**](ListDashboardsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ThrottlingException |  -  |

<a id="listGateways"></a>
# **listGateways**
> ListGatewaysResponse listGateways(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults)



Retrieves a paginated list of gateways.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | The token to be used for the next set of paginated results.
    Integer maxResults = 56; // Integer | <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
    try {
      ListGatewaysResponse result = apiInstance.listGateways(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listGateways");
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
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] |
| **maxResults** | **Integer**| &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt; | [optional] |

### Return type

[**ListGatewaysResponse**](ListGatewaysResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ThrottlingException |  -  |

<a id="listPortals"></a>
# **listPortals**
> ListPortalsResponse listPortals(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults)



Retrieves a paginated list of IoT SiteWise Monitor portals.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | The token to be used for the next set of paginated results.
    Integer maxResults = 56; // Integer | <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
    try {
      ListPortalsResponse result = apiInstance.listPortals(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listPortals");
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
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] |
| **maxResults** | **Integer**| &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt; | [optional] |

### Return type

[**ListPortalsResponse**](ListPortalsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ThrottlingException |  -  |

<a id="listProjectAssets"></a>
# **listProjectAssets**
> ListProjectAssetsResponse listProjectAssets(projectId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults)



Retrieves a paginated list of assets associated with an IoT SiteWise Monitor project.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectId = "projectId_example"; // String | The ID of the project.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | The token to be used for the next set of paginated results.
    Integer maxResults = 56; // Integer | <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
    try {
      ListProjectAssetsResponse result = apiInstance.listProjectAssets(projectId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listProjectAssets");
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
| **projectId** | **String**| The ID of the project. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] |
| **maxResults** | **Integer**| &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt; | [optional] |

### Return type

[**ListProjectAssetsResponse**](ListProjectAssetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ThrottlingException |  -  |

<a id="listProjects"></a>
# **listProjects**
> ListProjectsResponse listProjects(portalId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults)



Retrieves a paginated list of projects for an IoT SiteWise Monitor portal.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String portalId = "portalId_example"; // String | The ID of the portal.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | The token to be used for the next set of paginated results.
    Integer maxResults = 56; // Integer | <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
    try {
      ListProjectsResponse result = apiInstance.listProjects(portalId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listProjects");
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
| **portalId** | **String**| The ID of the portal. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] |
| **maxResults** | **Integer**| &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt; | [optional] |

### Return type

[**ListProjectsResponse**](ListProjectsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ThrottlingException |  -  |

<a id="listTagsForResource"></a>
# **listTagsForResource**
> ListTagsForResourceResponse listTagsForResource(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves the list of tags for an IoT SiteWise resource.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the resource.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListTagsForResourceResponse result = apiInstance.listTagsForResource(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
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
| **resourceArn** | **String**| The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the resource. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ConflictingOperationException |  -  |
| **485** | LimitExceededException |  -  |
| **486** | UnauthorizedException |  -  |

<a id="listTimeSeries"></a>
# **listTimeSeries**
> ListTimeSeriesResponse listTimeSeries(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, assetId, aliasPrefix, timeSeriesType)



Retrieves a paginated list of time series (data streams).

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | The token to be used for the next set of paginated results.
    Integer maxResults = 56; // Integer | The maximum number of results to return for each paginated request.
    String assetId = "assetId_example"; // String | The ID of the asset in which the asset property was created.
    String aliasPrefix = "aliasPrefix_example"; // String | The alias prefix of the time series.
    String timeSeriesType = "ASSOCIATED"; // String | <p>The type of the time series. The time series type can be one of the following values:</p> <ul> <li> <p> <code>ASSOCIATED</code> – The time series is associated with an asset property.</p> </li> <li> <p> <code>DISASSOCIATED</code> – The time series isn't associated with any asset property.</p> </li> </ul>
    try {
      ListTimeSeriesResponse result = apiInstance.listTimeSeries(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, assetId, aliasPrefix, timeSeriesType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTimeSeries");
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
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return for each paginated request. | [optional] |
| **assetId** | **String**| The ID of the asset in which the asset property was created. | [optional] |
| **aliasPrefix** | **String**| The alias prefix of the time series. | [optional] |
| **timeSeriesType** | **String**| &lt;p&gt;The type of the time series. The time series type can be one of the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ASSOCIATED&lt;/code&gt; – The time series is associated with an asset property.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DISASSOCIATED&lt;/code&gt; – The time series isn&#39;t associated with any asset property.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] [enum: ASSOCIATED, DISASSOCIATED] |

### Return type

[**ListTimeSeriesResponse**](ListTimeSeriesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |

<a id="putDefaultEncryptionConfiguration"></a>
# **putDefaultEncryptionConfiguration**
> PutDefaultEncryptionConfigurationResponse putDefaultEncryptionConfiguration(putDefaultEncryptionConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Sets the default encryption configuration for the Amazon Web Services account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html\&quot;&gt;Key management&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    PutDefaultEncryptionConfigurationRequest putDefaultEncryptionConfigurationRequest = new PutDefaultEncryptionConfigurationRequest(); // PutDefaultEncryptionConfigurationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutDefaultEncryptionConfigurationResponse result = apiInstance.putDefaultEncryptionConfiguration(putDefaultEncryptionConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putDefaultEncryptionConfiguration");
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
| **putDefaultEncryptionConfigurationRequest** | [**PutDefaultEncryptionConfigurationRequest**](PutDefaultEncryptionConfigurationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutDefaultEncryptionConfigurationResponse**](PutDefaultEncryptionConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | LimitExceededException |  -  |
| **484** | ConflictingOperationException |  -  |

<a id="putLoggingOptions"></a>
# **putLoggingOptions**
> Object putLoggingOptions(putLoggingOptionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Sets logging options for IoT SiteWise.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    PutLoggingOptionsRequest putLoggingOptionsRequest = new PutLoggingOptionsRequest(); // PutLoggingOptionsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.putLoggingOptions(putLoggingOptionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putLoggingOptions");
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
| **putLoggingOptionsRequest** | [**PutLoggingOptionsRequest**](PutLoggingOptionsRequest.md)|  | |
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
| **480** | InvalidRequestException |  -  |
| **481** | ThrottlingException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ConflictingOperationException |  -  |
| **484** | ResourceNotFoundException |  -  |

<a id="putStorageConfiguration"></a>
# **putStorageConfiguration**
> PutStorageConfigurationResponse putStorageConfiguration(putStorageConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Configures storage settings for IoT SiteWise.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    PutStorageConfigurationRequest putStorageConfigurationRequest = new PutStorageConfigurationRequest(); // PutStorageConfigurationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutStorageConfigurationResponse result = apiInstance.putStorageConfiguration(putStorageConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putStorageConfiguration");
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
| **putStorageConfigurationRequest** | [**PutStorageConfigurationRequest**](PutStorageConfigurationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutStorageConfigurationResponse**](PutStorageConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceAlreadyExistsException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | ThrottlingException |  -  |
| **485** | LimitExceededException |  -  |
| **486** | ConflictingOperationException |  -  |

<a id="tagResource"></a>
# **tagResource**
> Object tagResource(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Adds tags to an IoT SiteWise resource. If a tag already exists for the resource, this operation updates the tag&#39;s value.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the resource to tag.
    TagResourceRequest tagResourceRequest = new TagResourceRequest(); // TagResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.tagResource(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
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
| **resourceArn** | **String**| The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the resource to tag. | |
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
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ConflictingOperationException |  -  |
| **485** | LimitExceededException |  -  |
| **486** | UnauthorizedException |  -  |
| **487** | TooManyTagsException |  -  |

<a id="untagResource"></a>
# **untagResource**
> Object untagResource(resourceArn, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Removes a tag from an IoT SiteWise resource.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the resource to untag.
    List<String> tagKeys = Arrays.asList(); // List<String> | A list of keys for tags to remove from the resource.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.untagResource(resourceArn, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
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
| **resourceArn** | **String**| The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the resource to untag. | |
| **tagKeys** | [**List&lt;String&gt;**](String.md)| A list of keys for tags to remove from the resource. | |
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
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ConflictingOperationException |  -  |
| **485** | LimitExceededException |  -  |
| **486** | UnauthorizedException |  -  |

<a id="updateAccessPolicy"></a>
# **updateAccessPolicy**
> Object updateAccessPolicy(accessPolicyId, updateAccessPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates an existing access policy that specifies an identity&#39;s access to an IoT SiteWise Monitor portal or project resource.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accessPolicyId = "accessPolicyId_example"; // String | The ID of the access policy.
    UpdateAccessPolicyRequest updateAccessPolicyRequest = new UpdateAccessPolicyRequest(); // UpdateAccessPolicyRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.updateAccessPolicy(accessPolicyId, updateAccessPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateAccessPolicy");
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
| **accessPolicyId** | **String**| The ID of the access policy. | |
| **updateAccessPolicyRequest** | [**UpdateAccessPolicyRequest**](UpdateAccessPolicyRequest.md)|  | |
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
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |

<a id="updateAsset"></a>
# **updateAsset**
> UpdateAssetResponse updateAsset(assetId, updateAssetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates an asset&#39;s name. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-assets-and-models.html\&quot;&gt;Updating assets and models&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String assetId = "assetId_example"; // String | The ID of the asset to update.
    UpdateAssetRequest updateAssetRequest = new UpdateAssetRequest(); // UpdateAssetRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateAssetResponse result = apiInstance.updateAsset(assetId, updateAssetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateAsset");
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
| **assetId** | **String**| The ID of the asset to update. | |
| **updateAssetRequest** | [**UpdateAssetRequest**](UpdateAssetRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateAssetResponse**](UpdateAssetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceAlreadyExistsException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | ThrottlingException |  -  |
| **485** | ConflictingOperationException |  -  |

<a id="updateAssetModel"></a>
# **updateAssetModel**
> UpdateAssetModelResponse updateAssetModel(assetModelId, updateAssetModelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates an asset model and all of the assets that were created from the model. Each asset created from the model inherits the updated asset model&#39;s property and hierarchy definitions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-assets-and-models.html\&quot;&gt;Updating assets and models&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This operation overwrites the existing model with the provided model. To avoid deleting your asset model&#39;s properties or hierarchies, you must include their IDs and definitions in the updated asset model payload. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModel.html\&quot;&gt;DescribeAssetModel&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you remove a property from an asset model, IoT SiteWise deletes all previous data for that property. If you remove a hierarchy definition from an asset model, IoT SiteWise disassociates every asset associated with that hierarchy. You can&#39;t change the type or data type of an existing property.&lt;/p&gt; &lt;/important&gt;

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String assetModelId = "assetModelId_example"; // String | The ID of the asset model to update.
    UpdateAssetModelRequest updateAssetModelRequest = new UpdateAssetModelRequest(); // UpdateAssetModelRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateAssetModelResponse result = apiInstance.updateAssetModel(assetModelId, updateAssetModelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateAssetModel");
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
| **assetModelId** | **String**| The ID of the asset model to update. | |
| **updateAssetModelRequest** | [**UpdateAssetModelRequest**](UpdateAssetModelRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateAssetModelResponse**](UpdateAssetModelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceAlreadyExistsException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | ThrottlingException |  -  |
| **486** | ConflictingOperationException |  -  |

<a id="updateAssetProperty"></a>
# **updateAssetProperty**
> updateAssetProperty(assetId, propertyId, updateAssetPropertyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates an asset property&#39;s alias and notification state.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This operation overwrites the property&#39;s existing alias and notification state. To keep your existing property&#39;s alias or notification state, you must include the existing values in the UpdateAssetProperty request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetProperty.html\&quot;&gt;DescribeAssetProperty&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt;

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String assetId = "assetId_example"; // String | The ID of the asset to be updated.
    String propertyId = "propertyId_example"; // String | The ID of the asset property to be updated.
    UpdateAssetPropertyRequest updateAssetPropertyRequest = new UpdateAssetPropertyRequest(); // UpdateAssetPropertyRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.updateAssetProperty(assetId, propertyId, updateAssetPropertyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateAssetProperty");
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
| **assetId** | **String**| The ID of the asset to be updated. | |
| **propertyId** | **String**| The ID of the asset property to be updated. | |
| **updateAssetPropertyRequest** | [**UpdateAssetPropertyRequest**](UpdateAssetPropertyRequest.md)|  | |
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
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ConflictingOperationException |  -  |

<a id="updateDashboard"></a>
# **updateDashboard**
> Object updateDashboard(dashboardId, updateDashboardRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates an IoT SiteWise Monitor dashboard.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String dashboardId = "dashboardId_example"; // String | The ID of the dashboard to update.
    UpdateDashboardRequest updateDashboardRequest = new UpdateDashboardRequest(); // UpdateDashboardRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.updateDashboard(dashboardId, updateDashboardRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateDashboard");
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
| **dashboardId** | **String**| The ID of the dashboard to update. | |
| **updateDashboardRequest** | [**UpdateDashboardRequest**](UpdateDashboardRequest.md)|  | |
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
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |

<a id="updateGateway"></a>
# **updateGateway**
> updateGateway(gatewayId, updateGatewayRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates a gateway&#39;s name.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String gatewayId = "gatewayId_example"; // String | The ID of the gateway to update.
    UpdateGatewayRequest updateGatewayRequest = new UpdateGatewayRequest(); // UpdateGatewayRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.updateGateway(gatewayId, updateGatewayRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateGateway");
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
| **gatewayId** | **String**| The ID of the gateway to update. | |
| **updateGatewayRequest** | [**UpdateGatewayRequest**](UpdateGatewayRequest.md)|  | |
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
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | ConflictingOperationException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | ThrottlingException |  -  |

<a id="updateGatewayCapabilityConfiguration"></a>
# **updateGatewayCapabilityConfiguration**
> UpdateGatewayCapabilityConfigurationResponse updateGatewayCapabilityConfiguration(gatewayId, updateGatewayCapabilityConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates a gateway capability configuration or defines a new capability configuration. Each gateway capability defines data sources for a gateway. A capability configuration can contain multiple data source configurations. If you define OPC-UA sources for a gateway in the IoT SiteWise console, all of your OPC-UA sources are stored in one capability configuration. To list all capability configurations for a gateway, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGateway.html\&quot;&gt;DescribeGateway&lt;/a&gt;.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String gatewayId = "gatewayId_example"; // String | The ID of the gateway to be updated.
    UpdateGatewayCapabilityConfigurationRequest updateGatewayCapabilityConfigurationRequest = new UpdateGatewayCapabilityConfigurationRequest(); // UpdateGatewayCapabilityConfigurationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateGatewayCapabilityConfigurationResponse result = apiInstance.updateGatewayCapabilityConfiguration(gatewayId, updateGatewayCapabilityConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateGatewayCapabilityConfiguration");
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
| **gatewayId** | **String**| The ID of the gateway to be updated. | |
| **updateGatewayCapabilityConfigurationRequest** | [**UpdateGatewayCapabilityConfigurationRequest**](UpdateGatewayCapabilityConfigurationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateGatewayCapabilityConfigurationResponse**](UpdateGatewayCapabilityConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | ConflictingOperationException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | ThrottlingException |  -  |
| **485** | LimitExceededException |  -  |

<a id="updatePortal"></a>
# **updatePortal**
> UpdatePortalResponse updatePortal(portalId, updatePortalRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates an IoT SiteWise Monitor portal.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String portalId = "portalId_example"; // String | The ID of the portal to update.
    UpdatePortalRequest updatePortalRequest = new UpdatePortalRequest(); // UpdatePortalRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdatePortalResponse result = apiInstance.updatePortal(portalId, updatePortalRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updatePortal");
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
| **portalId** | **String**| The ID of the portal to update. | |
| **updatePortalRequest** | [**UpdatePortalRequest**](UpdatePortalRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdatePortalResponse**](UpdatePortalResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ConflictingOperationException |  -  |

<a id="updateProject"></a>
# **updateProject**
> Object updateProject(projectId, updateProjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates an IoT SiteWise Monitor project.

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
    defaultClient.setBasePath("http://iotsitewise.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectId = "projectId_example"; // String | The ID of the project to update.
    UpdateProjectRequest updateProjectRequest = new UpdateProjectRequest(); // UpdateProjectRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.updateProject(projectId, updateProjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateProject");
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
| **projectId** | **String**| The ID of the project to update. | |
| **updateProjectRequest** | [**UpdateProjectRequest**](UpdateProjectRequest.md)|  | |
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
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | ThrottlingException |  -  |

