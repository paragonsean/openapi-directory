# AwsIoTSiteWise.DefaultApi

All URIs are relative to *http://iotsitewise.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateAssets**](DefaultApi.md#associateAssets) | **POST** /assets/{assetId}/associate | 
[**associateTimeSeriesToAssetProperty**](DefaultApi.md#associateTimeSeriesToAssetProperty) | **POST** /timeseries/associate/#alias&amp;assetId&amp;propertyId | 
[**batchAssociateProjectAssets**](DefaultApi.md#batchAssociateProjectAssets) | **POST** /projects/{projectId}/assets/associate | 
[**batchDisassociateProjectAssets**](DefaultApi.md#batchDisassociateProjectAssets) | **POST** /projects/{projectId}/assets/disassociate | 
[**batchGetAssetPropertyAggregates**](DefaultApi.md#batchGetAssetPropertyAggregates) | **POST** /properties/batch/aggregates | 
[**batchGetAssetPropertyValue**](DefaultApi.md#batchGetAssetPropertyValue) | **POST** /properties/batch/latest | 
[**batchGetAssetPropertyValueHistory**](DefaultApi.md#batchGetAssetPropertyValueHistory) | **POST** /properties/batch/history | 
[**batchPutAssetPropertyValue**](DefaultApi.md#batchPutAssetPropertyValue) | **POST** /properties | 
[**createAccessPolicy**](DefaultApi.md#createAccessPolicy) | **POST** /access-policies | 
[**createAsset**](DefaultApi.md#createAsset) | **POST** /assets | 
[**createAssetModel**](DefaultApi.md#createAssetModel) | **POST** /asset-models | 
[**createBulkImportJob**](DefaultApi.md#createBulkImportJob) | **POST** /jobs | 
[**createDashboard**](DefaultApi.md#createDashboard) | **POST** /dashboards | 
[**createGateway**](DefaultApi.md#createGateway) | **POST** /20200301/gateways | 
[**createPortal**](DefaultApi.md#createPortal) | **POST** /portals | 
[**createProject**](DefaultApi.md#createProject) | **POST** /projects | 
[**deleteAccessPolicy**](DefaultApi.md#deleteAccessPolicy) | **DELETE** /access-policies/{accessPolicyId} | 
[**deleteAsset**](DefaultApi.md#deleteAsset) | **DELETE** /assets/{assetId} | 
[**deleteAssetModel**](DefaultApi.md#deleteAssetModel) | **DELETE** /asset-models/{assetModelId} | 
[**deleteDashboard**](DefaultApi.md#deleteDashboard) | **DELETE** /dashboards/{dashboardId} | 
[**deleteGateway**](DefaultApi.md#deleteGateway) | **DELETE** /20200301/gateways/{gatewayId} | 
[**deletePortal**](DefaultApi.md#deletePortal) | **DELETE** /portals/{portalId} | 
[**deleteProject**](DefaultApi.md#deleteProject) | **DELETE** /projects/{projectId} | 
[**deleteTimeSeries**](DefaultApi.md#deleteTimeSeries) | **POST** /timeseries/delete/ | 
[**describeAccessPolicy**](DefaultApi.md#describeAccessPolicy) | **GET** /access-policies/{accessPolicyId} | 
[**describeAsset**](DefaultApi.md#describeAsset) | **GET** /assets/{assetId} | 
[**describeAssetModel**](DefaultApi.md#describeAssetModel) | **GET** /asset-models/{assetModelId} | 
[**describeAssetProperty**](DefaultApi.md#describeAssetProperty) | **GET** /assets/{assetId}/properties/{propertyId} | 
[**describeBulkImportJob**](DefaultApi.md#describeBulkImportJob) | **GET** /jobs/{jobId} | 
[**describeDashboard**](DefaultApi.md#describeDashboard) | **GET** /dashboards/{dashboardId} | 
[**describeDefaultEncryptionConfiguration**](DefaultApi.md#describeDefaultEncryptionConfiguration) | **GET** /configuration/account/encryption | 
[**describeGateway**](DefaultApi.md#describeGateway) | **GET** /20200301/gateways/{gatewayId} | 
[**describeGatewayCapabilityConfiguration**](DefaultApi.md#describeGatewayCapabilityConfiguration) | **GET** /20200301/gateways/{gatewayId}/capability/{capabilityNamespace} | 
[**describeLoggingOptions**](DefaultApi.md#describeLoggingOptions) | **GET** /logging | 
[**describePortal**](DefaultApi.md#describePortal) | **GET** /portals/{portalId} | 
[**describeProject**](DefaultApi.md#describeProject) | **GET** /projects/{projectId} | 
[**describeStorageConfiguration**](DefaultApi.md#describeStorageConfiguration) | **GET** /configuration/account/storage | 
[**describeTimeSeries**](DefaultApi.md#describeTimeSeries) | **GET** /timeseries/describe/ | 
[**disassociateAssets**](DefaultApi.md#disassociateAssets) | **POST** /assets/{assetId}/disassociate | 
[**disassociateTimeSeriesFromAssetProperty**](DefaultApi.md#disassociateTimeSeriesFromAssetProperty) | **POST** /timeseries/disassociate/#alias&amp;assetId&amp;propertyId | 
[**getAssetPropertyAggregates**](DefaultApi.md#getAssetPropertyAggregates) | **GET** /properties/aggregates#aggregateTypes&amp;resolution&amp;startDate&amp;endDate | 
[**getAssetPropertyValue**](DefaultApi.md#getAssetPropertyValue) | **GET** /properties/latest | 
[**getAssetPropertyValueHistory**](DefaultApi.md#getAssetPropertyValueHistory) | **GET** /properties/history | 
[**getInterpolatedAssetPropertyValues**](DefaultApi.md#getInterpolatedAssetPropertyValues) | **GET** /properties/interpolated#startTimeInSeconds&amp;endTimeInSeconds&amp;quality&amp;intervalInSeconds&amp;type | 
[**listAccessPolicies**](DefaultApi.md#listAccessPolicies) | **GET** /access-policies | 
[**listAssetModelProperties**](DefaultApi.md#listAssetModelProperties) | **GET** /asset-models/{assetModelId}/properties | 
[**listAssetModels**](DefaultApi.md#listAssetModels) | **GET** /asset-models | 
[**listAssetProperties**](DefaultApi.md#listAssetProperties) | **GET** /assets/{assetId}/properties | 
[**listAssetRelationships**](DefaultApi.md#listAssetRelationships) | **GET** /assets/{assetId}/assetRelationships#traversalType | 
[**listAssets**](DefaultApi.md#listAssets) | **GET** /assets | 
[**listAssociatedAssets**](DefaultApi.md#listAssociatedAssets) | **GET** /assets/{assetId}/hierarchies | 
[**listBulkImportJobs**](DefaultApi.md#listBulkImportJobs) | **GET** /jobs | 
[**listDashboards**](DefaultApi.md#listDashboards) | **GET** /dashboards#projectId | 
[**listGateways**](DefaultApi.md#listGateways) | **GET** /20200301/gateways | 
[**listPortals**](DefaultApi.md#listPortals) | **GET** /portals | 
[**listProjectAssets**](DefaultApi.md#listProjectAssets) | **GET** /projects/{projectId}/assets | 
[**listProjects**](DefaultApi.md#listProjects) | **GET** /projects#portalId | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags#resourceArn | 
[**listTimeSeries**](DefaultApi.md#listTimeSeries) | **GET** /timeseries/ | 
[**putDefaultEncryptionConfiguration**](DefaultApi.md#putDefaultEncryptionConfiguration) | **POST** /configuration/account/encryption | 
[**putLoggingOptions**](DefaultApi.md#putLoggingOptions) | **PUT** /logging | 
[**putStorageConfiguration**](DefaultApi.md#putStorageConfiguration) | **POST** /configuration/account/storage | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags#resourceArn | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags#resourceArn&amp;tagKeys | 
[**updateAccessPolicy**](DefaultApi.md#updateAccessPolicy) | **PUT** /access-policies/{accessPolicyId} | 
[**updateAsset**](DefaultApi.md#updateAsset) | **PUT** /assets/{assetId} | 
[**updateAssetModel**](DefaultApi.md#updateAssetModel) | **PUT** /asset-models/{assetModelId} | 
[**updateAssetProperty**](DefaultApi.md#updateAssetProperty) | **PUT** /assets/{assetId}/properties/{propertyId} | 
[**updateDashboard**](DefaultApi.md#updateDashboard) | **PUT** /dashboards/{dashboardId} | 
[**updateGateway**](DefaultApi.md#updateGateway) | **PUT** /20200301/gateways/{gatewayId} | 
[**updateGatewayCapabilityConfiguration**](DefaultApi.md#updateGatewayCapabilityConfiguration) | **POST** /20200301/gateways/{gatewayId}/capability | 
[**updatePortal**](DefaultApi.md#updatePortal) | **PUT** /portals/{portalId} | 
[**updateProject**](DefaultApi.md#updateProject) | **PUT** /projects/{projectId} | 



## associateAssets

> associateAssets(assetId, associateAssetsRequest, opts)



Associates a child asset with the given parent asset through a hierarchy defined in the parent asset&#39;s model. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/add-associated-assets.html\&quot;&gt;Associating assets&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let assetId = "assetId_example"; // String | The ID of the parent asset.
let associateAssetsRequest = new AwsIoTSiteWise.AssociateAssetsRequest(); // AssociateAssetsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateAssets(assetId, associateAssetsRequest, opts, (error, data, response) => {
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
 **assetId** | **String**| The ID of the parent asset. | 
 **associateAssetsRequest** | [**AssociateAssetsRequest**](AssociateAssetsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associateTimeSeriesToAssetProperty

> associateTimeSeriesToAssetProperty(alias, assetId, propertyId, associateTimeSeriesToAssetPropertyRequest, opts)



Associates a time series (data stream) with an asset property.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let alias = "alias_example"; // String | The alias that identifies the time series.
let assetId = "assetId_example"; // String | The ID of the asset in which the asset property was created.
let propertyId = "propertyId_example"; // String | The ID of the asset property.
let associateTimeSeriesToAssetPropertyRequest = new AwsIoTSiteWise.AssociateTimeSeriesToAssetPropertyRequest(); // AssociateTimeSeriesToAssetPropertyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateTimeSeriesToAssetProperty(alias, assetId, propertyId, associateTimeSeriesToAssetPropertyRequest, opts, (error, data, response) => {
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
 **alias** | **String**| The alias that identifies the time series. | 
 **assetId** | **String**| The ID of the asset in which the asset property was created. | 
 **propertyId** | **String**| The ID of the asset property. | 
 **associateTimeSeriesToAssetPropertyRequest** | [**AssociateTimeSeriesToAssetPropertyRequest**](AssociateTimeSeriesToAssetPropertyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchAssociateProjectAssets

> BatchAssociateProjectAssetsResponse batchAssociateProjectAssets(projectId, batchAssociateProjectAssetsRequest, opts)



Associates a group (batch) of assets with an IoT SiteWise Monitor project.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let projectId = "projectId_example"; // String | The ID of the project to which to associate the assets.
let batchAssociateProjectAssetsRequest = new AwsIoTSiteWise.BatchAssociateProjectAssetsRequest(); // BatchAssociateProjectAssetsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchAssociateProjectAssets(projectId, batchAssociateProjectAssetsRequest, opts, (error, data, response) => {
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
 **projectId** | **String**| The ID of the project to which to associate the assets. | 
 **batchAssociateProjectAssetsRequest** | [**BatchAssociateProjectAssetsRequest**](BatchAssociateProjectAssetsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchAssociateProjectAssetsResponse**](BatchAssociateProjectAssetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchDisassociateProjectAssets

> BatchDisassociateProjectAssetsResponse batchDisassociateProjectAssets(projectId, batchDisassociateProjectAssetsRequest, opts)



Disassociates a group (batch) of assets from an IoT SiteWise Monitor project.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let projectId = "projectId_example"; // String | The ID of the project from which to disassociate the assets.
let batchDisassociateProjectAssetsRequest = new AwsIoTSiteWise.BatchDisassociateProjectAssetsRequest(); // BatchDisassociateProjectAssetsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchDisassociateProjectAssets(projectId, batchDisassociateProjectAssetsRequest, opts, (error, data, response) => {
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
 **projectId** | **String**| The ID of the project from which to disassociate the assets. | 
 **batchDisassociateProjectAssetsRequest** | [**BatchDisassociateProjectAssetsRequest**](BatchDisassociateProjectAssetsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchDisassociateProjectAssetsResponse**](BatchDisassociateProjectAssetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchGetAssetPropertyAggregates

> BatchGetAssetPropertyAggregatesResponse batchGetAssetPropertyAggregates(batchGetAssetPropertyAggregatesRequest, opts)



Gets aggregated values (for example, average, minimum, and maximum) for one or more asset properties. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#aggregates\&quot;&gt;Querying aggregates&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let batchGetAssetPropertyAggregatesRequest = new AwsIoTSiteWise.BatchGetAssetPropertyAggregatesRequest(); // BatchGetAssetPropertyAggregatesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.batchGetAssetPropertyAggregates(batchGetAssetPropertyAggregatesRequest, opts, (error, data, response) => {
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
 **batchGetAssetPropertyAggregatesRequest** | [**BatchGetAssetPropertyAggregatesRequest**](BatchGetAssetPropertyAggregatesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**BatchGetAssetPropertyAggregatesResponse**](BatchGetAssetPropertyAggregatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchGetAssetPropertyValue

> BatchGetAssetPropertyValueResponse batchGetAssetPropertyValue(batchGetAssetPropertyValueRequest, opts)



Gets the current value for one or more asset properties. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#current-values\&quot;&gt;Querying current values&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let batchGetAssetPropertyValueRequest = new AwsIoTSiteWise.BatchGetAssetPropertyValueRequest(); // BatchGetAssetPropertyValueRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.batchGetAssetPropertyValue(batchGetAssetPropertyValueRequest, opts, (error, data, response) => {
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
 **batchGetAssetPropertyValueRequest** | [**BatchGetAssetPropertyValueRequest**](BatchGetAssetPropertyValueRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**BatchGetAssetPropertyValueResponse**](BatchGetAssetPropertyValueResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchGetAssetPropertyValueHistory

> BatchGetAssetPropertyValueHistoryResponse batchGetAssetPropertyValueHistory(batchGetAssetPropertyValueHistoryRequest, opts)



Gets the historical values for one or more asset properties. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#historical-values\&quot;&gt;Querying historical values&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let batchGetAssetPropertyValueHistoryRequest = new AwsIoTSiteWise.BatchGetAssetPropertyValueHistoryRequest(); // BatchGetAssetPropertyValueHistoryRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.batchGetAssetPropertyValueHistory(batchGetAssetPropertyValueHistoryRequest, opts, (error, data, response) => {
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
 **batchGetAssetPropertyValueHistoryRequest** | [**BatchGetAssetPropertyValueHistoryRequest**](BatchGetAssetPropertyValueHistoryRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**BatchGetAssetPropertyValueHistoryResponse**](BatchGetAssetPropertyValueHistoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchPutAssetPropertyValue

> BatchPutAssetPropertyValueResponse batchPutAssetPropertyValue(batchPutAssetPropertyValueRequest, opts)



&lt;p&gt;Sends a list of asset property values to IoT SiteWise. Each value is a timestamp-quality-value (TQV) data point. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ingest-api.html\&quot;&gt;Ingesting data using the API&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To identify an asset property, you must specify one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; of an asset property.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;propertyAlias&lt;/code&gt;, which is a data stream alias (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). To define an asset property&#39;s alias, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\&quot;&gt;UpdateAssetProperty&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;important&gt; &lt;p&gt;With respect to Unix epoch time, IoT SiteWise accepts only TQVs that have a timestamp of no more than 7 days in the past and no more than 10 minutes in the future. IoT SiteWise rejects timestamps outside of the inclusive range of [-7 days, +10 minutes] and returns a &lt;code&gt;TimestampOutOfRangeException&lt;/code&gt; error.&lt;/p&gt; &lt;p&gt;For each asset property, IoT SiteWise overwrites TQVs with duplicate timestamps unless the newer TQV has a different quality. For example, if you store a TQV &lt;code&gt;{T1, GOOD, V1}&lt;/code&gt;, then storing &lt;code&gt;{T1, GOOD, V2}&lt;/code&gt; replaces the existing TQV.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;IoT SiteWise authorizes access to each &lt;code&gt;BatchPutAssetPropertyValue&lt;/code&gt; entry individually. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-batchputassetpropertyvalue-action\&quot;&gt;BatchPutAssetPropertyValue authorization&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let batchPutAssetPropertyValueRequest = new AwsIoTSiteWise.BatchPutAssetPropertyValueRequest(); // BatchPutAssetPropertyValueRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchPutAssetPropertyValue(batchPutAssetPropertyValueRequest, opts, (error, data, response) => {
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
 **batchPutAssetPropertyValueRequest** | [**BatchPutAssetPropertyValueRequest**](BatchPutAssetPropertyValueRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchPutAssetPropertyValueResponse**](BatchPutAssetPropertyValueResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAccessPolicy

> CreateAccessPolicyResponse createAccessPolicy(createAccessPolicyRequest, opts)



Creates an access policy that grants the specified identity (IAM Identity Center user, IAM Identity Center group, or IAM user) access to the specified IoT SiteWise Monitor portal or project resource.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let createAccessPolicyRequest = new AwsIoTSiteWise.CreateAccessPolicyRequest(); // CreateAccessPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAccessPolicy(createAccessPolicyRequest, opts, (error, data, response) => {
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
 **createAccessPolicyRequest** | [**CreateAccessPolicyRequest**](CreateAccessPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAccessPolicyResponse**](CreateAccessPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAsset

> CreateAssetResponse createAsset(createAssetRequest, opts)



Creates an asset from an existing asset model. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-assets.html\&quot;&gt;Creating assets&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let createAssetRequest = new AwsIoTSiteWise.CreateAssetRequest(); // CreateAssetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAsset(createAssetRequest, opts, (error, data, response) => {
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
 **createAssetRequest** | [**CreateAssetRequest**](CreateAssetRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAssetResponse**](CreateAssetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAssetModel

> CreateAssetModelResponse createAssetModel(createAssetModelRequest, opts)



Creates an asset model from specified property and hierarchy definitions. You create assets from asset models. With asset models, you can easily create assets of the same type that have standardized definitions. Each asset created from a model inherits the asset model&#39;s property and hierarchy definitions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/define-models.html\&quot;&gt;Defining asset models&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let createAssetModelRequest = new AwsIoTSiteWise.CreateAssetModelRequest(); // CreateAssetModelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAssetModel(createAssetModelRequest, opts, (error, data, response) => {
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
 **createAssetModelRequest** | [**CreateAssetModelRequest**](CreateAssetModelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAssetModelResponse**](CreateAssetModelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBulkImportJob

> CreateBulkImportJobResponse createBulkImportJob(createBulkImportJobRequest, opts)



&lt;p&gt;Defines a job to ingest data to IoT SiteWise from Amazon S3. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/CreateBulkImportJob.html\&quot;&gt;Create a bulk import job (CLI)&lt;/a&gt; in the &lt;i&gt;Amazon Simple Storage Service User Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;You must enable IoT SiteWise to export data to Amazon S3 before you create a bulk import job. For more information about how to configure storage settings, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PutStorageConfiguration.html\&quot;&gt;PutStorageConfiguration&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let createBulkImportJobRequest = new AwsIoTSiteWise.CreateBulkImportJobRequest(); // CreateBulkImportJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBulkImportJob(createBulkImportJobRequest, opts, (error, data, response) => {
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
 **createBulkImportJobRequest** | [**CreateBulkImportJobRequest**](CreateBulkImportJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateBulkImportJobResponse**](CreateBulkImportJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDashboard

> CreateDashboardResponse createDashboard(createDashboardRequest, opts)



Creates a dashboard in an IoT SiteWise Monitor project.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let createDashboardRequest = new AwsIoTSiteWise.CreateDashboardRequest(); // CreateDashboardRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDashboard(createDashboardRequest, opts, (error, data, response) => {
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
 **createDashboardRequest** | [**CreateDashboardRequest**](CreateDashboardRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateDashboardResponse**](CreateDashboardResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createGateway

> CreateGatewayResponse createGateway(createGatewayRequest, opts)



Creates a gateway, which is a virtual or edge device that delivers industrial data streams from local servers to IoT SiteWise. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateway-connector.html\&quot;&gt;Ingesting data using a gateway&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let createGatewayRequest = new AwsIoTSiteWise.CreateGatewayRequest(); // CreateGatewayRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createGateway(createGatewayRequest, opts, (error, data, response) => {
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
 **createGatewayRequest** | [**CreateGatewayRequest**](CreateGatewayRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateGatewayResponse**](CreateGatewayResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPortal

> CreatePortalResponse createPortal(createPortalRequest, opts)



&lt;p&gt;Creates a portal, which can contain projects and dashboards. IoT SiteWise Monitor uses IAM Identity Center or IAM to authenticate portal users and manage user permissions.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before you can sign in to a new portal, you must add at least one identity to that portal. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/administer-portals.html#portal-change-admins\&quot;&gt;Adding or removing portal administrators&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let createPortalRequest = new AwsIoTSiteWise.CreatePortalRequest(); // CreatePortalRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createPortal(createPortalRequest, opts, (error, data, response) => {
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
 **createPortalRequest** | [**CreatePortalRequest**](CreatePortalRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreatePortalResponse**](CreatePortalResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createProject

> CreateProjectResponse createProject(createProjectRequest, opts)



&lt;p&gt;Creates a project in the specified portal.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Make sure that the project name and description don&#39;t contain confidential information.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let createProjectRequest = new AwsIoTSiteWise.CreateProjectRequest(); // CreateProjectRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createProject(createProjectRequest, opts, (error, data, response) => {
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
 **createProjectRequest** | [**CreateProjectRequest**](CreateProjectRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateProjectResponse**](CreateProjectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAccessPolicy

> Object deleteAccessPolicy(accessPolicyId, opts)



Deletes an access policy that grants the specified identity access to the specified IoT SiteWise Monitor resource. You can use this operation to revoke access to an IoT SiteWise Monitor resource.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let accessPolicyId = "accessPolicyId_example"; // String | The ID of the access policy to be deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
};
apiInstance.deleteAccessPolicy(accessPolicyId, opts, (error, data, response) => {
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
 **accessPolicyId** | **String**| The ID of the access policy to be deleted. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteAsset

> DeleteAssetResponse deleteAsset(assetId, opts)



&lt;p&gt;Deletes an asset. This action can&#39;t be undone. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-assets-and-models.html\&quot;&gt;Deleting assets and models&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t delete an asset that&#39;s associated to another asset. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DisassociateAssets.html\&quot;&gt;DisassociateAssets&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let assetId = "assetId_example"; // String | The ID of the asset to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
};
apiInstance.deleteAsset(assetId, opts, (error, data, response) => {
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
 **assetId** | **String**| The ID of the asset to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. | [optional] 

### Return type

[**DeleteAssetResponse**](DeleteAssetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteAssetModel

> DeleteAssetModelResponse deleteAssetModel(assetModelId, opts)



Deletes an asset model. This action can&#39;t be undone. You must delete all assets created from an asset model before you can delete the model. Also, you can&#39;t delete an asset model if a parent asset model exists that contains a property formula expression that depends on the asset model that you want to delete. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-assets-and-models.html\&quot;&gt;Deleting assets and models&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let assetModelId = "assetModelId_example"; // String | The ID of the asset model to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
};
apiInstance.deleteAssetModel(assetModelId, opts, (error, data, response) => {
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
 **assetModelId** | **String**| The ID of the asset model to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. | [optional] 

### Return type

[**DeleteAssetModelResponse**](DeleteAssetModelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDashboard

> Object deleteDashboard(dashboardId, opts)



Deletes a dashboard from IoT SiteWise Monitor.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let dashboardId = "dashboardId_example"; // String | The ID of the dashboard to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
};
apiInstance.deleteDashboard(dashboardId, opts, (error, data, response) => {
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
 **dashboardId** | **String**| The ID of the dashboard to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteGateway

> deleteGateway(gatewayId, opts)



Deletes a gateway from IoT SiteWise. When you delete a gateway, some of the gateway&#39;s files remain in your gateway&#39;s file system.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let gatewayId = "gatewayId_example"; // String | The ID of the gateway to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteGateway(gatewayId, opts, (error, data, response) => {
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
 **gatewayId** | **String**| The ID of the gateway to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePortal

> DeletePortalResponse deletePortal(portalId, opts)



Deletes a portal from IoT SiteWise Monitor.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let portalId = "portalId_example"; // String | The ID of the portal to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
};
apiInstance.deletePortal(portalId, opts, (error, data, response) => {
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
 **portalId** | **String**| The ID of the portal to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. | [optional] 

### Return type

[**DeletePortalResponse**](DeletePortalResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteProject

> Object deleteProject(projectId, opts)



Deletes a project from IoT SiteWise Monitor.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let projectId = "projectId_example"; // String | The ID of the project.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
};
apiInstance.deleteProject(projectId, opts, (error, data, response) => {
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
 **projectId** | **String**| The ID of the project. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTimeSeries

> deleteTimeSeries(associateTimeSeriesToAssetPropertyRequest, opts)



&lt;p&gt;Deletes a time series (data stream). If you delete a time series that&#39;s associated with an asset property, the asset property still exists, but the time series will no longer be associated with this asset property.&lt;/p&gt; &lt;p&gt;To identify a time series, do one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the time series isn&#39;t associated with an asset property, specify the &lt;code&gt;alias&lt;/code&gt; of the time series.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the time series is associated with an asset property, specify one of the following: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;alias&lt;/code&gt; of the time series.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; that identifies the asset property.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let associateTimeSeriesToAssetPropertyRequest = new AwsIoTSiteWise.AssociateTimeSeriesToAssetPropertyRequest(); // AssociateTimeSeriesToAssetPropertyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'alias': "alias_example", // String | The alias that identifies the time series.
  'assetId': "assetId_example", // String | The ID of the asset in which the asset property was created.
  'propertyId': "propertyId_example" // String | The ID of the asset property.
};
apiInstance.deleteTimeSeries(associateTimeSeriesToAssetPropertyRequest, opts, (error, data, response) => {
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
 **associateTimeSeriesToAssetPropertyRequest** | [**AssociateTimeSeriesToAssetPropertyRequest**](AssociateTimeSeriesToAssetPropertyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **alias** | **String**| The alias that identifies the time series. | [optional] 
 **assetId** | **String**| The ID of the asset in which the asset property was created. | [optional] 
 **propertyId** | **String**| The ID of the asset property. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeAccessPolicy

> DescribeAccessPolicyResponse describeAccessPolicy(accessPolicyId, opts)



Describes an access policy, which specifies an identity&#39;s access to an IoT SiteWise Monitor portal or project.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let accessPolicyId = "accessPolicyId_example"; // String | The ID of the access policy.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAccessPolicy(accessPolicyId, opts, (error, data, response) => {
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
 **accessPolicyId** | **String**| The ID of the access policy. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAccessPolicyResponse**](DescribeAccessPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeAsset

> DescribeAssetResponse describeAsset(assetId, opts)



Retrieves information about an asset.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let assetId = "assetId_example"; // String | The ID of the asset.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'excludeProperties': true // Boolean |  Whether or not to exclude asset properties from the response. 
};
apiInstance.describeAsset(assetId, opts, (error, data, response) => {
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
 **assetId** | **String**| The ID of the asset. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **excludeProperties** | **Boolean**|  Whether or not to exclude asset properties from the response.  | [optional] 

### Return type

[**DescribeAssetResponse**](DescribeAssetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeAssetModel

> DescribeAssetModelResponse describeAssetModel(assetModelId, opts)



Retrieves information about an asset model.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let assetModelId = "assetModelId_example"; // String | The ID of the asset model.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'excludeProperties': true // Boolean |  Whether or not to exclude asset model properties from the response. 
};
apiInstance.describeAssetModel(assetModelId, opts, (error, data, response) => {
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
 **assetModelId** | **String**| The ID of the asset model. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **excludeProperties** | **Boolean**|  Whether or not to exclude asset model properties from the response.  | [optional] 

### Return type

[**DescribeAssetModelResponse**](DescribeAssetModelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeAssetProperty

> DescribeAssetPropertyResponse describeAssetProperty(assetId, propertyId, opts)



&lt;p&gt;Retrieves information about an asset property.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When you call this operation for an attribute property, this response includes the default attribute value that you define in the asset model. If you update the default value in the model, this operation&#39;s response includes the new default value.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation doesn&#39;t return the value of the asset property. To get the value of an asset property, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetAssetPropertyValue.html\&quot;&gt;GetAssetPropertyValue&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let assetId = "assetId_example"; // String | The ID of the asset.
let propertyId = "propertyId_example"; // String | The ID of the asset property.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAssetProperty(assetId, propertyId, opts, (error, data, response) => {
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
 **assetId** | **String**| The ID of the asset. | 
 **propertyId** | **String**| The ID of the asset property. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAssetPropertyResponse**](DescribeAssetPropertyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeBulkImportJob

> DescribeBulkImportJobResponse describeBulkImportJob(jobId, opts)



Retrieves information about a bulk import job request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/DescribeBulkImportJob.html\&quot;&gt;Describe a bulk import job (CLI)&lt;/a&gt; in the &lt;i&gt;Amazon Simple Storage Service User Guide&lt;/i&gt;.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let jobId = "jobId_example"; // String | The ID of the job.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeBulkImportJob(jobId, opts, (error, data, response) => {
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
 **jobId** | **String**| The ID of the job. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeBulkImportJobResponse**](DescribeBulkImportJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeDashboard

> DescribeDashboardResponse describeDashboard(dashboardId, opts)



Retrieves information about a dashboard.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let dashboardId = "dashboardId_example"; // String | The ID of the dashboard.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeDashboard(dashboardId, opts, (error, data, response) => {
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
 **dashboardId** | **String**| The ID of the dashboard. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeDashboardResponse**](DescribeDashboardResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeDefaultEncryptionConfiguration

> DescribeDefaultEncryptionConfigurationResponse describeDefaultEncryptionConfiguration(opts)



Retrieves information about the default encryption configuration for the Amazon Web Services account in the default or specified Region. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html\&quot;&gt;Key management&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeDefaultEncryptionConfiguration(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeDefaultEncryptionConfigurationResponse**](DescribeDefaultEncryptionConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeGateway

> DescribeGatewayResponse describeGateway(gatewayId, opts)



Retrieves information about a gateway.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let gatewayId = "gatewayId_example"; // String | The ID of the gateway device.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeGateway(gatewayId, opts, (error, data, response) => {
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
 **gatewayId** | **String**| The ID of the gateway device. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeGatewayResponse**](DescribeGatewayResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeGatewayCapabilityConfiguration

> DescribeGatewayCapabilityConfigurationResponse describeGatewayCapabilityConfiguration(gatewayId, capabilityNamespace, opts)



Retrieves information about a gateway capability configuration. Each gateway capability defines data sources for a gateway. A capability configuration can contain multiple data source configurations. If you define OPC-UA sources for a gateway in the IoT SiteWise console, all of your OPC-UA sources are stored in one capability configuration. To list all capability configurations for a gateway, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGateway.html\&quot;&gt;DescribeGateway&lt;/a&gt;.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let gatewayId = "gatewayId_example"; // String | The ID of the gateway that defines the capability configuration.
let capabilityNamespace = "capabilityNamespace_example"; // String | The namespace of the capability configuration. For example, if you configure OPC-UA sources from the IoT SiteWise console, your OPC-UA capability configuration has the namespace <code>iotsitewise:opcuacollector:version</code>, where <code>version</code> is a number such as <code>1</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeGatewayCapabilityConfiguration(gatewayId, capabilityNamespace, opts, (error, data, response) => {
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
 **gatewayId** | **String**| The ID of the gateway that defines the capability configuration. | 
 **capabilityNamespace** | **String**| The namespace of the capability configuration. For example, if you configure OPC-UA sources from the IoT SiteWise console, your OPC-UA capability configuration has the namespace &lt;code&gt;iotsitewise:opcuacollector:version&lt;/code&gt;, where &lt;code&gt;version&lt;/code&gt; is a number such as &lt;code&gt;1&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeGatewayCapabilityConfigurationResponse**](DescribeGatewayCapabilityConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeLoggingOptions

> DescribeLoggingOptionsResponse describeLoggingOptions(opts)



Retrieves the current IoT SiteWise logging options.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeLoggingOptions(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeLoggingOptionsResponse**](DescribeLoggingOptionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describePortal

> DescribePortalResponse describePortal(portalId, opts)



Retrieves information about a portal.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let portalId = "portalId_example"; // String | The ID of the portal.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describePortal(portalId, opts, (error, data, response) => {
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
 **portalId** | **String**| The ID of the portal. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribePortalResponse**](DescribePortalResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeProject

> DescribeProjectResponse describeProject(projectId, opts)



Retrieves information about a project.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let projectId = "projectId_example"; // String | The ID of the project.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeProject(projectId, opts, (error, data, response) => {
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
 **projectId** | **String**| The ID of the project. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeProjectResponse**](DescribeProjectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeStorageConfiguration

> DescribeStorageConfigurationResponse describeStorageConfiguration(opts)



Retrieves information about the storage configuration for IoT SiteWise.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeStorageConfiguration(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeStorageConfigurationResponse**](DescribeStorageConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeTimeSeries

> DescribeTimeSeriesResponse describeTimeSeries(opts)



&lt;p&gt;Retrieves information about a time series (data stream).&lt;/p&gt; &lt;p&gt;To identify a time series, do one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the time series isn&#39;t associated with an asset property, specify the &lt;code&gt;alias&lt;/code&gt; of the time series.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the time series is associated with an asset property, specify one of the following: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;alias&lt;/code&gt; of the time series.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; that identifies the asset property.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'alias': "alias_example", // String | The alias that identifies the time series.
  'assetId': "assetId_example", // String | The ID of the asset in which the asset property was created.
  'propertyId': "propertyId_example" // String | The ID of the asset property.
};
apiInstance.describeTimeSeries(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **alias** | **String**| The alias that identifies the time series. | [optional] 
 **assetId** | **String**| The ID of the asset in which the asset property was created. | [optional] 
 **propertyId** | **String**| The ID of the asset property. | [optional] 

### Return type

[**DescribeTimeSeriesResponse**](DescribeTimeSeriesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateAssets

> disassociateAssets(assetId, disassociateAssetsRequest, opts)



Disassociates a child asset from the given parent asset through a hierarchy defined in the parent asset&#39;s model.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let assetId = "assetId_example"; // String | The ID of the parent asset from which to disassociate the child asset.
let disassociateAssetsRequest = new AwsIoTSiteWise.DisassociateAssetsRequest(); // DisassociateAssetsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateAssets(assetId, disassociateAssetsRequest, opts, (error, data, response) => {
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
 **assetId** | **String**| The ID of the parent asset from which to disassociate the child asset. | 
 **disassociateAssetsRequest** | [**DisassociateAssetsRequest**](DisassociateAssetsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disassociateTimeSeriesFromAssetProperty

> disassociateTimeSeriesFromAssetProperty(alias, assetId, propertyId, associateTimeSeriesToAssetPropertyRequest, opts)



Disassociates a time series (data stream) from an asset property.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let alias = "alias_example"; // String | The alias that identifies the time series.
let assetId = "assetId_example"; // String | The ID of the asset in which the asset property was created.
let propertyId = "propertyId_example"; // String | The ID of the asset property.
let associateTimeSeriesToAssetPropertyRequest = new AwsIoTSiteWise.AssociateTimeSeriesToAssetPropertyRequest(); // AssociateTimeSeriesToAssetPropertyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateTimeSeriesFromAssetProperty(alias, assetId, propertyId, associateTimeSeriesToAssetPropertyRequest, opts, (error, data, response) => {
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
 **alias** | **String**| The alias that identifies the time series. | 
 **assetId** | **String**| The ID of the asset in which the asset property was created. | 
 **propertyId** | **String**| The ID of the asset property. | 
 **associateTimeSeriesToAssetPropertyRequest** | [**AssociateTimeSeriesToAssetPropertyRequest**](AssociateTimeSeriesToAssetPropertyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAssetPropertyAggregates

> GetAssetPropertyAggregatesResponse getAssetPropertyAggregates(aggregateTypes, resolution, startDate, endDate, opts)



&lt;p&gt;Gets aggregated values for an asset property. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#aggregates\&quot;&gt;Querying aggregates&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To identify an asset property, you must specify one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; of an asset property.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;propertyAlias&lt;/code&gt;, which is a data stream alias (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). To define an asset property&#39;s alias, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\&quot;&gt;UpdateAssetProperty&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let aggregateTypes = [new AwsIoTSiteWise.AggregateType()]; // [AggregateType] | The data aggregating function.
let resolution = "resolution_example"; // String | The time interval over which to aggregate data.
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.
let endDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'assetId': "assetId_example", // String | The ID of the asset.
  'propertyId': "propertyId_example", // String | The ID of the asset property.
  'propertyAlias': "propertyAlias_example", // String | The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.
  'qualities': [new AwsIoTSiteWise.Quality()], // [Quality] | The quality by which to filter asset data.
  'timeOrdering': "timeOrdering_example", // String | <p>The chronological sorting order of the requested information.</p> <p>Default: <code>ASCENDING</code> </p>
  'nextToken': "nextToken_example", // String | The token to be used for the next set of paginated results.
  'maxResults': 56 // Number | <p>The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.</p> <ul> <li> <p>The size of the result set is equal to 1 MB.</p> </li> <li> <p>The number of data points in the result set is equal to the value of <code>maxResults</code>. The maximum value of <code>maxResults</code> is 250.</p> </li> </ul>
};
apiInstance.getAssetPropertyAggregates(aggregateTypes, resolution, startDate, endDate, opts, (error, data, response) => {
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
 **aggregateTypes** | [**[AggregateType]**](AggregateType.md)| The data aggregating function. | 
 **resolution** | **String**| The time interval over which to aggregate data. | 
 **startDate** | **Date**| The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time. | 
 **endDate** | **Date**| The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **assetId** | **String**| The ID of the asset. | [optional] 
 **propertyId** | **String**| The ID of the asset property. | [optional] 
 **propertyAlias** | **String**| The alias that identifies the property, such as an OPC-UA server data stream path (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\&quot;&gt;Mapping industrial data streams to asset properties&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;. | [optional] 
 **qualities** | [**[Quality]**](Quality.md)| The quality by which to filter asset data. | [optional] 
 **timeOrdering** | **String**| &lt;p&gt;The chronological sorting order of the requested information.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;ASCENDING&lt;/code&gt; &lt;/p&gt; | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The size of the result set is equal to 1 MB.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The number of data points in the result set is equal to the value of &lt;code&gt;maxResults&lt;/code&gt;. The maximum value of &lt;code&gt;maxResults&lt;/code&gt; is 250.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 

### Return type

[**GetAssetPropertyAggregatesResponse**](GetAssetPropertyAggregatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAssetPropertyValue

> GetAssetPropertyValueResponse getAssetPropertyValue(opts)



&lt;p&gt;Gets an asset property&#39;s current value. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#current-values\&quot;&gt;Querying current values&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To identify an asset property, you must specify one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; of an asset property.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;propertyAlias&lt;/code&gt;, which is a data stream alias (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). To define an asset property&#39;s alias, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\&quot;&gt;UpdateAssetProperty&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'assetId': "assetId_example", // String | The ID of the asset.
  'propertyId': "propertyId_example", // String | The ID of the asset property.
  'propertyAlias': "propertyAlias_example" // String | The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.
};
apiInstance.getAssetPropertyValue(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **assetId** | **String**| The ID of the asset. | [optional] 
 **propertyId** | **String**| The ID of the asset property. | [optional] 
 **propertyAlias** | **String**| The alias that identifies the property, such as an OPC-UA server data stream path (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\&quot;&gt;Mapping industrial data streams to asset properties&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;. | [optional] 

### Return type

[**GetAssetPropertyValueResponse**](GetAssetPropertyValueResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAssetPropertyValueHistory

> GetAssetPropertyValueHistoryResponse getAssetPropertyValueHistory(opts)



&lt;p&gt;Gets the history of an asset property&#39;s values. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#historical-values\&quot;&gt;Querying historical values&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To identify an asset property, you must specify one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; of an asset property.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;propertyAlias&lt;/code&gt;, which is a data stream alias (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). To define an asset property&#39;s alias, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\&quot;&gt;UpdateAssetProperty&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'assetId': "assetId_example", // String | The ID of the asset.
  'propertyId': "propertyId_example", // String | The ID of the asset property.
  'propertyAlias': "propertyAlias_example", // String | The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.
  'qualities': [new AwsIoTSiteWise.Quality()], // [Quality] | The quality by which to filter asset data.
  'timeOrdering': "timeOrdering_example", // String | <p>The chronological sorting order of the requested information.</p> <p>Default: <code>ASCENDING</code> </p>
  'nextToken': "nextToken_example", // String | The token to be used for the next set of paginated results.
  'maxResults': 56 // Number | <p>The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.</p> <ul> <li> <p>The size of the result set is equal to 4 MB.</p> </li> <li> <p>The number of data points in the result set is equal to the value of <code>maxResults</code>. The maximum value of <code>maxResults</code> is 20000.</p> </li> </ul>
};
apiInstance.getAssetPropertyValueHistory(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **assetId** | **String**| The ID of the asset. | [optional] 
 **propertyId** | **String**| The ID of the asset property. | [optional] 
 **propertyAlias** | **String**| The alias that identifies the property, such as an OPC-UA server data stream path (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\&quot;&gt;Mapping industrial data streams to asset properties&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;. | [optional] 
 **startDate** | **Date**| The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time. | [optional] 
 **endDate** | **Date**| The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time. | [optional] 
 **qualities** | [**[Quality]**](Quality.md)| The quality by which to filter asset data. | [optional] 
 **timeOrdering** | **String**| &lt;p&gt;The chronological sorting order of the requested information.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;ASCENDING&lt;/code&gt; &lt;/p&gt; | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The size of the result set is equal to 4 MB.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The number of data points in the result set is equal to the value of &lt;code&gt;maxResults&lt;/code&gt;. The maximum value of &lt;code&gt;maxResults&lt;/code&gt; is 20000.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 

### Return type

[**GetAssetPropertyValueHistoryResponse**](GetAssetPropertyValueHistoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInterpolatedAssetPropertyValues

> GetInterpolatedAssetPropertyValuesResponse getInterpolatedAssetPropertyValues(startTimeInSeconds, endTimeInSeconds, quality, intervalInSeconds, type, opts)



&lt;p&gt;Get interpolated values for an asset property for a specified time interval, during a period of time. If your time series is missing data points during the specified time interval, you can use interpolation to estimate the missing data.&lt;/p&gt; &lt;p&gt;For example, you can use this operation to return the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days.&lt;/p&gt; &lt;p&gt;To identify an asset property, you must specify one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; of an asset property.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;propertyAlias&lt;/code&gt;, which is a data stream alias (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). To define an asset property&#39;s alias, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\&quot;&gt;UpdateAssetProperty&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let startTimeInSeconds = 56; // Number | The exclusive start of the range from which to interpolate data, expressed in seconds in Unix epoch time.
let endTimeInSeconds = 56; // Number | The inclusive end of the range from which to interpolate data, expressed in seconds in Unix epoch time.
let quality = "quality_example"; // String | The quality of the asset property value. You can use this parameter as a filter to choose only the asset property values that have a specific quality.
let intervalInSeconds = 56; // Number | The time interval in seconds over which to interpolate data. Each interval starts when the previous one ends.
let type = "type_example"; // String | <p>The interpolation type.</p> <p>Valid values: <code>LINEAR_INTERPOLATION | LOCF_INTERPOLATION</code> </p> <ul> <li> <p> <code>LINEAR_INTERPOLATION</code> – Estimates missing data using <a href=\"https://en.wikipedia.org/wiki/Linear_interpolation\">linear interpolation</a>.</p> <p>For example, you can use this operation to return the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days. If the interpolation starts July 1, 2021, at 9 AM, IoT SiteWise returns the first interpolated value on July 2, 2021, at 9 AM, the second interpolated value on July 3, 2021, at 9 AM, and so on.</p> </li> <li> <p> <code>LOCF_INTERPOLATION</code> – Estimates missing data using last observation carried forward interpolation</p> <p>If no data point is found for an interval, IoT SiteWise returns the last observed data point for the previous interval and carries forward this interpolated value until a new data point is found.</p> <p>For example, you can get the state of an on-off valve every 24 hours over a duration of 7 days. If the interpolation starts July 1, 2021, at 9 AM, IoT SiteWise returns the last observed data point between July 1, 2021, at 9 AM and July 2, 2021, at 9 AM as the first interpolated value. If a data point isn't found after 9 AM on July 2, 2021, IoT SiteWise uses the same interpolated value for the rest of the days.</p> </li> </ul>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'assetId': "assetId_example", // String | The ID of the asset.
  'propertyId': "propertyId_example", // String | The ID of the asset property.
  'propertyAlias': "propertyAlias_example", // String | The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.
  'startTimeOffsetInNanos': 56, // Number | The nanosecond offset converted from <code>startTimeInSeconds</code>.
  'endTimeOffsetInNanos': 56, // Number | The nanosecond offset converted from <code>endTimeInSeconds</code>.
  'nextToken': "nextToken_example", // String | The token to be used for the next set of paginated results.
  'maxResults': 56, // Number | The maximum number of results to return for each paginated request. If not specified, the default value is 10.
  'intervalWindowInSeconds': 56 // Number | <p>The query interval for the window, in seconds. IoT SiteWise computes each interpolated value by using data points from the timestamp of each interval, minus the window to the timestamp of each interval plus the window. If not specified, the window ranges between the start time minus the interval and the end time plus the interval.</p> <note> <ul> <li> <p>If you specify a value for the <code>intervalWindowInSeconds</code> parameter, the value for the <code>type</code> parameter must be <code>LINEAR_INTERPOLATION</code>.</p> </li> <li> <p>If a data point isn't found during the specified query window, IoT SiteWise won't return an interpolated value for the interval. This indicates that there's a gap in the ingested data points.</p> </li> </ul> </note> <p>For example, you can get the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days. If the interpolation starts on July 1, 2021, at 9 AM with a window of 2 hours, IoT SiteWise uses the data points from 7 AM (9 AM minus 2 hours) to 11 AM (9 AM plus 2 hours) on July 2, 2021 to compute the first interpolated value. Next, IoT SiteWise uses the data points from 7 AM (9 AM minus 2 hours) to 11 AM (9 AM plus 2 hours) on July 3, 2021 to compute the second interpolated value, and so on. </p>
};
apiInstance.getInterpolatedAssetPropertyValues(startTimeInSeconds, endTimeInSeconds, quality, intervalInSeconds, type, opts, (error, data, response) => {
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
 **startTimeInSeconds** | **Number**| The exclusive start of the range from which to interpolate data, expressed in seconds in Unix epoch time. | 
 **endTimeInSeconds** | **Number**| The inclusive end of the range from which to interpolate data, expressed in seconds in Unix epoch time. | 
 **quality** | **String**| The quality of the asset property value. You can use this parameter as a filter to choose only the asset property values that have a specific quality. | 
 **intervalInSeconds** | **Number**| The time interval in seconds over which to interpolate data. Each interval starts when the previous one ends. | 
 **type** | **String**| &lt;p&gt;The interpolation type.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;LINEAR_INTERPOLATION | LOCF_INTERPOLATION&lt;/code&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LINEAR_INTERPOLATION&lt;/code&gt; – Estimates missing data using &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/Linear_interpolation\&quot;&gt;linear interpolation&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For example, you can use this operation to return the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days. If the interpolation starts July 1, 2021, at 9 AM, IoT SiteWise returns the first interpolated value on July 2, 2021, at 9 AM, the second interpolated value on July 3, 2021, at 9 AM, and so on.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LOCF_INTERPOLATION&lt;/code&gt; – Estimates missing data using last observation carried forward interpolation&lt;/p&gt; &lt;p&gt;If no data point is found for an interval, IoT SiteWise returns the last observed data point for the previous interval and carries forward this interpolated value until a new data point is found.&lt;/p&gt; &lt;p&gt;For example, you can get the state of an on-off valve every 24 hours over a duration of 7 days. If the interpolation starts July 1, 2021, at 9 AM, IoT SiteWise returns the last observed data point between July 1, 2021, at 9 AM and July 2, 2021, at 9 AM as the first interpolated value. If a data point isn&#39;t found after 9 AM on July 2, 2021, IoT SiteWise uses the same interpolated value for the rest of the days.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **assetId** | **String**| The ID of the asset. | [optional] 
 **propertyId** | **String**| The ID of the asset property. | [optional] 
 **propertyAlias** | **String**| The alias that identifies the property, such as an OPC-UA server data stream path (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\&quot;&gt;Mapping industrial data streams to asset properties&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;. | [optional] 
 **startTimeOffsetInNanos** | **Number**| The nanosecond offset converted from &lt;code&gt;startTimeInSeconds&lt;/code&gt;. | [optional] 
 **endTimeOffsetInNanos** | **Number**| The nanosecond offset converted from &lt;code&gt;endTimeInSeconds&lt;/code&gt;. | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return for each paginated request. If not specified, the default value is 10. | [optional] 
 **intervalWindowInSeconds** | **Number**| &lt;p&gt;The query interval for the window, in seconds. IoT SiteWise computes each interpolated value by using data points from the timestamp of each interval, minus the window to the timestamp of each interval plus the window. If not specified, the window ranges between the start time minus the interval and the end time plus the interval.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you specify a value for the &lt;code&gt;intervalWindowInSeconds&lt;/code&gt; parameter, the value for the &lt;code&gt;type&lt;/code&gt; parameter must be &lt;code&gt;LINEAR_INTERPOLATION&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If a data point isn&#39;t found during the specified query window, IoT SiteWise won&#39;t return an interpolated value for the interval. This indicates that there&#39;s a gap in the ingested data points.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p&gt;For example, you can get the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days. If the interpolation starts on July 1, 2021, at 9 AM with a window of 2 hours, IoT SiteWise uses the data points from 7 AM (9 AM minus 2 hours) to 11 AM (9 AM plus 2 hours) on July 2, 2021 to compute the first interpolated value. Next, IoT SiteWise uses the data points from 7 AM (9 AM minus 2 hours) to 11 AM (9 AM plus 2 hours) on July 3, 2021 to compute the second interpolated value, and so on. &lt;/p&gt; | [optional] 

### Return type

[**GetInterpolatedAssetPropertyValuesResponse**](GetInterpolatedAssetPropertyValuesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAccessPolicies

> ListAccessPoliciesResponse listAccessPolicies(opts)



Retrieves a paginated list of access policies for an identity (an IAM Identity Center user, an IAM Identity Center group, or an IAM user) or an IoT SiteWise Monitor resource (a portal or project).

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'identityType': "identityType_example", // String | The type of identity (IAM Identity Center user, IAM Identity Center group, or IAM user). This parameter is required if you specify <code>identityId</code>.
  'identityId': "identityId_example", // String | The ID of the identity. This parameter is required if you specify <code>USER</code> or <code>GROUP</code> for <code>identityType</code>.
  'resourceType': "resourceType_example", // String | The type of resource (portal or project). This parameter is required if you specify <code>resourceId</code>.
  'resourceId': "resourceId_example", // String | The ID of the resource. This parameter is required if you specify <code>resourceType</code>.
  'iamArn': "iamArn_example", // String | The ARN of the IAM user. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html\">IAM ARNs</a> in the <i>IAM User Guide</i>. This parameter is required if you specify <code>IAM</code> for <code>identityType</code>.
  'nextToken': "nextToken_example", // String | The token to be used for the next set of paginated results.
  'maxResults': 56 // Number | <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
};
apiInstance.listAccessPolicies(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **identityType** | **String**| The type of identity (IAM Identity Center user, IAM Identity Center group, or IAM user). This parameter is required if you specify &lt;code&gt;identityId&lt;/code&gt;. | [optional] 
 **identityId** | **String**| The ID of the identity. This parameter is required if you specify &lt;code&gt;USER&lt;/code&gt; or &lt;code&gt;GROUP&lt;/code&gt; for &lt;code&gt;identityType&lt;/code&gt;. | [optional] 
 **resourceType** | **String**| The type of resource (portal or project). This parameter is required if you specify &lt;code&gt;resourceId&lt;/code&gt;. | [optional] 
 **resourceId** | **String**| The ID of the resource. This parameter is required if you specify &lt;code&gt;resourceType&lt;/code&gt;. | [optional] 
 **iamArn** | **String**| The ARN of the IAM user. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html\&quot;&gt;IAM ARNs&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. This parameter is required if you specify &lt;code&gt;IAM&lt;/code&gt; for &lt;code&gt;identityType&lt;/code&gt;. | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt; | [optional] 

### Return type

[**ListAccessPoliciesResponse**](ListAccessPoliciesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAssetModelProperties

> ListAssetModelPropertiesResponse listAssetModelProperties(assetModelId, opts)



Retrieves a paginated list of properties associated with an asset model. If you update properties associated with the model before you finish listing all the properties, you need to start all over again.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let assetModelId = "assetModelId_example"; // String | The ID of the asset model.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to be used for the next set of paginated results.
  'maxResults': 56, // Number | The maximum number of results to return for each paginated request. If not specified, the default value is 50.
  'filter': "filter_example" // String | <p> Filters the requested list of asset model properties. You can choose one of the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all asset model properties for a given asset model ID. </p> </li> <li> <p> <code>BASE</code> – The list includes only base asset model properties for a given asset model ID. </p> </li> </ul> <p>Default: <code>BASE</code> </p>
};
apiInstance.listAssetModelProperties(assetModelId, opts, (error, data, response) => {
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
 **assetModelId** | **String**| The ID of the asset model. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return for each paginated request. If not specified, the default value is 50. | [optional] 
 **filter** | **String**| &lt;p&gt; Filters the requested list of asset model properties. You can choose one of the following options:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ALL&lt;/code&gt; – The list includes all asset model properties for a given asset model ID. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;BASE&lt;/code&gt; – The list includes only base asset model properties for a given asset model ID. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: &lt;code&gt;BASE&lt;/code&gt; &lt;/p&gt; | [optional] 

### Return type

[**ListAssetModelPropertiesResponse**](ListAssetModelPropertiesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAssetModels

> ListAssetModelsResponse listAssetModels(opts)



Retrieves a paginated list of summaries of all asset models.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to be used for the next set of paginated results.
  'maxResults': 56 // Number | <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
};
apiInstance.listAssetModels(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt; | [optional] 

### Return type

[**ListAssetModelsResponse**](ListAssetModelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAssetProperties

> ListAssetPropertiesResponse listAssetProperties(assetId, opts)



Retrieves a paginated list of properties associated with an asset. If you update properties associated with the model before you finish listing all the properties, you need to start all over again.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let assetId = "assetId_example"; // String | The ID of the asset.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to be used for the next set of paginated results.
  'maxResults': 56, // Number | The maximum number of results to return for each paginated request. If not specified, the default value is 50.
  'filter': "filter_example" // String | <p> Filters the requested list of asset properties. You can choose one of the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all asset properties for a given asset model ID. </p> </li> <li> <p> <code>BASE</code> – The list includes only base asset properties for a given asset model ID. </p> </li> </ul> <p>Default: <code>BASE</code> </p>
};
apiInstance.listAssetProperties(assetId, opts, (error, data, response) => {
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
 **assetId** | **String**| The ID of the asset. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return for each paginated request. If not specified, the default value is 50. | [optional] 
 **filter** | **String**| &lt;p&gt; Filters the requested list of asset properties. You can choose one of the following options:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ALL&lt;/code&gt; – The list includes all asset properties for a given asset model ID. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;BASE&lt;/code&gt; – The list includes only base asset properties for a given asset model ID. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: &lt;code&gt;BASE&lt;/code&gt; &lt;/p&gt; | [optional] 

### Return type

[**ListAssetPropertiesResponse**](ListAssetPropertiesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAssetRelationships

> ListAssetRelationshipsResponse listAssetRelationships(assetId, traversalType, opts)



Retrieves a paginated list of asset relationships for an asset. You can use this operation to identify an asset&#39;s root asset and all associated assets between that asset and its root.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let assetId = "assetId_example"; // String | The ID of the asset.
let traversalType = "traversalType_example"; // String | <p>The type of traversal to use to identify asset relationships. Choose the following option:</p> <ul> <li> <p> <code>PATH_TO_ROOT</code> – Identify the asset's parent assets up to the root asset. The asset that you specify in <code>assetId</code> is the first result in the list of <code>assetRelationshipSummaries</code>, and the root asset is the last result.</p> </li> </ul>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to be used for the next set of paginated results.
  'maxResults': 56 // Number | The maximum number of results to return for each paginated request.
};
apiInstance.listAssetRelationships(assetId, traversalType, opts, (error, data, response) => {
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
 **assetId** | **String**| The ID of the asset. | 
 **traversalType** | **String**| &lt;p&gt;The type of traversal to use to identify asset relationships. Choose the following option:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PATH_TO_ROOT&lt;/code&gt; – Identify the asset&#39;s parent assets up to the root asset. The asset that you specify in &lt;code&gt;assetId&lt;/code&gt; is the first result in the list of &lt;code&gt;assetRelationshipSummaries&lt;/code&gt;, and the root asset is the last result.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return for each paginated request. | [optional] 

### Return type

[**ListAssetRelationshipsResponse**](ListAssetRelationshipsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAssets

> ListAssetsResponse listAssets(opts)



&lt;p&gt;Retrieves a paginated list of asset summaries.&lt;/p&gt; &lt;p&gt;You can use this operation to do the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;List assets based on a specific asset model.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;List top-level assets.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can&#39;t use this operation to list all assets. To retrieve summaries for all of your assets, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssetModels.html\&quot;&gt;ListAssetModels&lt;/a&gt; to get all of your asset model IDs. Then, use ListAssets to get all assets for each asset model.&lt;/p&gt;

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to be used for the next set of paginated results.
  'maxResults': 56, // Number | <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
  'assetModelId': "assetModelId_example", // String | The ID of the asset model by which to filter the list of assets. This parameter is required if you choose <code>ALL</code> for <code>filter</code>.
  'filter': "filter_example" // String | <p>The filter for the requested list of assets. Choose one of the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all assets for a given asset model ID. The <code>assetModelId</code> parameter is required if you filter by <code>ALL</code>.</p> </li> <li> <p> <code>TOP_LEVEL</code> – The list includes only top-level assets in the asset hierarchy tree.</p> </li> </ul> <p>Default: <code>ALL</code> </p>
};
apiInstance.listAssets(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt; | [optional] 
 **assetModelId** | **String**| The ID of the asset model by which to filter the list of assets. This parameter is required if you choose &lt;code&gt;ALL&lt;/code&gt; for &lt;code&gt;filter&lt;/code&gt;. | [optional] 
 **filter** | **String**| &lt;p&gt;The filter for the requested list of assets. Choose one of the following options:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ALL&lt;/code&gt; – The list includes all assets for a given asset model ID. The &lt;code&gt;assetModelId&lt;/code&gt; parameter is required if you filter by &lt;code&gt;ALL&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TOP_LEVEL&lt;/code&gt; – The list includes only top-level assets in the asset hierarchy tree.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: &lt;code&gt;ALL&lt;/code&gt; &lt;/p&gt; | [optional] 

### Return type

[**ListAssetsResponse**](ListAssetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAssociatedAssets

> ListAssociatedAssetsResponse listAssociatedAssets(assetId, opts)



&lt;p&gt;Retrieves a paginated list of associated assets.&lt;/p&gt; &lt;p&gt;You can use this operation to do the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;List child assets associated to a parent asset by a hierarchy that you specify.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;List an asset&#39;s parent asset.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let assetId = "assetId_example"; // String | The ID of the asset to query.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'hierarchyId': "hierarchyId_example", // String | <p>The ID of the hierarchy by which child assets are associated to the asset. To find a hierarchy ID, use the <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAsset.html\">DescribeAsset</a> or <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModel.html\">DescribeAssetModel</a> operations. This parameter is required if you choose <code>CHILD</code> for <code>traversalDirection</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html\">Asset hierarchies</a> in the <i>IoT SiteWise User Guide</i>.</p>
  'traversalDirection': "traversalDirection_example", // String | <p>The direction to list associated assets. Choose one of the following options:</p> <ul> <li> <p> <code>CHILD</code> – The list includes all child assets associated to the asset. The <code>hierarchyId</code> parameter is required if you choose <code>CHILD</code>.</p> </li> <li> <p> <code>PARENT</code> – The list includes the asset's parent asset.</p> </li> </ul> <p>Default: <code>CHILD</code> </p>
  'nextToken': "nextToken_example", // String | The token to be used for the next set of paginated results.
  'maxResults': 56 // Number | <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
};
apiInstance.listAssociatedAssets(assetId, opts, (error, data, response) => {
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
 **assetId** | **String**| The ID of the asset to query. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **hierarchyId** | **String**| &lt;p&gt;The ID of the hierarchy by which child assets are associated to the asset. To find a hierarchy ID, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAsset.html\&quot;&gt;DescribeAsset&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModel.html\&quot;&gt;DescribeAssetModel&lt;/a&gt; operations. This parameter is required if you choose &lt;code&gt;CHILD&lt;/code&gt; for &lt;code&gt;traversalDirection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html\&quot;&gt;Asset hierarchies&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; | [optional] 
 **traversalDirection** | **String**| &lt;p&gt;The direction to list associated assets. Choose one of the following options:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CHILD&lt;/code&gt; – The list includes all child assets associated to the asset. The &lt;code&gt;hierarchyId&lt;/code&gt; parameter is required if you choose &lt;code&gt;CHILD&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PARENT&lt;/code&gt; – The list includes the asset&#39;s parent asset.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: &lt;code&gt;CHILD&lt;/code&gt; &lt;/p&gt; | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt; | [optional] 

### Return type

[**ListAssociatedAssetsResponse**](ListAssociatedAssetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBulkImportJobs

> ListBulkImportJobsResponse listBulkImportJobs(opts)



Retrieves a paginated list of bulk import job requests. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ListBulkImportJobs.html\&quot;&gt;List bulk import jobs (CLI)&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to be used for the next set of paginated results.
  'maxResults': 56, // Number | The maximum number of results to return for each paginated request.
  'filter': "filter_example" // String | You can use a filter to select the bulk import jobs that you want to retrieve.
};
apiInstance.listBulkImportJobs(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return for each paginated request. | [optional] 
 **filter** | **String**| You can use a filter to select the bulk import jobs that you want to retrieve. | [optional] 

### Return type

[**ListBulkImportJobsResponse**](ListBulkImportJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDashboards

> ListDashboardsResponse listDashboards(projectId, opts)



Retrieves a paginated list of dashboards for an IoT SiteWise Monitor project.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let projectId = "projectId_example"; // String | The ID of the project.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to be used for the next set of paginated results.
  'maxResults': 56 // Number | <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
};
apiInstance.listDashboards(projectId, opts, (error, data, response) => {
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
 **projectId** | **String**| The ID of the project. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt; | [optional] 

### Return type

[**ListDashboardsResponse**](ListDashboardsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listGateways

> ListGatewaysResponse listGateways(opts)



Retrieves a paginated list of gateways.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to be used for the next set of paginated results.
  'maxResults': 56 // Number | <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
};
apiInstance.listGateways(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt; | [optional] 

### Return type

[**ListGatewaysResponse**](ListGatewaysResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPortals

> ListPortalsResponse listPortals(opts)



Retrieves a paginated list of IoT SiteWise Monitor portals.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to be used for the next set of paginated results.
  'maxResults': 56 // Number | <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
};
apiInstance.listPortals(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt; | [optional] 

### Return type

[**ListPortalsResponse**](ListPortalsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listProjectAssets

> ListProjectAssetsResponse listProjectAssets(projectId, opts)



Retrieves a paginated list of assets associated with an IoT SiteWise Monitor project.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let projectId = "projectId_example"; // String | The ID of the project.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to be used for the next set of paginated results.
  'maxResults': 56 // Number | <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
};
apiInstance.listProjectAssets(projectId, opts, (error, data, response) => {
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
 **projectId** | **String**| The ID of the project. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt; | [optional] 

### Return type

[**ListProjectAssetsResponse**](ListProjectAssetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listProjects

> ListProjectsResponse listProjects(portalId, opts)



Retrieves a paginated list of projects for an IoT SiteWise Monitor portal.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let portalId = "portalId_example"; // String | The ID of the portal.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to be used for the next set of paginated results.
  'maxResults': 56 // Number | <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
};
apiInstance.listProjects(portalId, opts, (error, data, response) => {
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
 **portalId** | **String**| The ID of the portal. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt; | [optional] 

### Return type

[**ListProjectsResponse**](ListProjectsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Retrieves the list of tags for an IoT SiteWise resource.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTimeSeries

> ListTimeSeriesResponse listTimeSeries(opts)



Retrieves a paginated list of time series (data streams).

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to be used for the next set of paginated results.
  'maxResults': 56, // Number | The maximum number of results to return for each paginated request.
  'assetId': "assetId_example", // String | The ID of the asset in which the asset property was created.
  'aliasPrefix': "aliasPrefix_example", // String | The alias prefix of the time series.
  'timeSeriesType': "timeSeriesType_example" // String | <p>The type of the time series. The time series type can be one of the following values:</p> <ul> <li> <p> <code>ASSOCIATED</code> – The time series is associated with an asset property.</p> </li> <li> <p> <code>DISASSOCIATED</code> – The time series isn't associated with any asset property.</p> </li> </ul>
};
apiInstance.listTimeSeries(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return for each paginated request. | [optional] 
 **assetId** | **String**| The ID of the asset in which the asset property was created. | [optional] 
 **aliasPrefix** | **String**| The alias prefix of the time series. | [optional] 
 **timeSeriesType** | **String**| &lt;p&gt;The type of the time series. The time series type can be one of the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ASSOCIATED&lt;/code&gt; – The time series is associated with an asset property.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DISASSOCIATED&lt;/code&gt; – The time series isn&#39;t associated with any asset property.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 

### Return type

[**ListTimeSeriesResponse**](ListTimeSeriesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putDefaultEncryptionConfiguration

> PutDefaultEncryptionConfigurationResponse putDefaultEncryptionConfiguration(putDefaultEncryptionConfigurationRequest, opts)



Sets the default encryption configuration for the Amazon Web Services account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html\&quot;&gt;Key management&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let putDefaultEncryptionConfigurationRequest = new AwsIoTSiteWise.PutDefaultEncryptionConfigurationRequest(); // PutDefaultEncryptionConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putDefaultEncryptionConfiguration(putDefaultEncryptionConfigurationRequest, opts, (error, data, response) => {
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
 **putDefaultEncryptionConfigurationRequest** | [**PutDefaultEncryptionConfigurationRequest**](PutDefaultEncryptionConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutDefaultEncryptionConfigurationResponse**](PutDefaultEncryptionConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putLoggingOptions

> Object putLoggingOptions(putLoggingOptionsRequest, opts)



Sets logging options for IoT SiteWise.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let putLoggingOptionsRequest = new AwsIoTSiteWise.PutLoggingOptionsRequest(); // PutLoggingOptionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putLoggingOptions(putLoggingOptionsRequest, opts, (error, data, response) => {
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
 **putLoggingOptionsRequest** | [**PutLoggingOptionsRequest**](PutLoggingOptionsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putStorageConfiguration

> PutStorageConfigurationResponse putStorageConfiguration(putStorageConfigurationRequest, opts)



Configures storage settings for IoT SiteWise.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let putStorageConfigurationRequest = new AwsIoTSiteWise.PutStorageConfigurationRequest(); // PutStorageConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putStorageConfiguration(putStorageConfigurationRequest, opts, (error, data, response) => {
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
 **putStorageConfigurationRequest** | [**PutStorageConfigurationRequest**](PutStorageConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutStorageConfigurationResponse**](PutStorageConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



Adds tags to an IoT SiteWise resource. If a tag already exists for the resource, this operation updates the tag&#39;s value.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the resource to tag.
let tagResourceRequest = new AwsIoTSiteWise.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(resourceArn, tagResourceRequest, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the resource to tag. | 
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> Object untagResource(resourceArn, tagKeys, opts)



Removes a tag from an IoT SiteWise resource.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the resource to untag.
let tagKeys = ["null"]; // [String] | A list of keys for tags to remove from the resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(resourceArn, tagKeys, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the resource to untag. | 
 **tagKeys** | [**[String]**](String.md)| A list of keys for tags to remove from the resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAccessPolicy

> Object updateAccessPolicy(accessPolicyId, updateAccessPolicyRequest, opts)



Updates an existing access policy that specifies an identity&#39;s access to an IoT SiteWise Monitor portal or project resource.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let accessPolicyId = "accessPolicyId_example"; // String | The ID of the access policy.
let updateAccessPolicyRequest = new AwsIoTSiteWise.UpdateAccessPolicyRequest(); // UpdateAccessPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAccessPolicy(accessPolicyId, updateAccessPolicyRequest, opts, (error, data, response) => {
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
 **accessPolicyId** | **String**| The ID of the access policy. | 
 **updateAccessPolicyRequest** | [**UpdateAccessPolicyRequest**](UpdateAccessPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAsset

> UpdateAssetResponse updateAsset(assetId, updateAssetRequest, opts)



Updates an asset&#39;s name. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-assets-and-models.html\&quot;&gt;Updating assets and models&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let assetId = "assetId_example"; // String | The ID of the asset to update.
let updateAssetRequest = new AwsIoTSiteWise.UpdateAssetRequest(); // UpdateAssetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAsset(assetId, updateAssetRequest, opts, (error, data, response) => {
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
 **assetId** | **String**| The ID of the asset to update. | 
 **updateAssetRequest** | [**UpdateAssetRequest**](UpdateAssetRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAssetResponse**](UpdateAssetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAssetModel

> UpdateAssetModelResponse updateAssetModel(assetModelId, updateAssetModelRequest, opts)



&lt;p&gt;Updates an asset model and all of the assets that were created from the model. Each asset created from the model inherits the updated asset model&#39;s property and hierarchy definitions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-assets-and-models.html\&quot;&gt;Updating assets and models&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This operation overwrites the existing model with the provided model. To avoid deleting your asset model&#39;s properties or hierarchies, you must include their IDs and definitions in the updated asset model payload. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModel.html\&quot;&gt;DescribeAssetModel&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you remove a property from an asset model, IoT SiteWise deletes all previous data for that property. If you remove a hierarchy definition from an asset model, IoT SiteWise disassociates every asset associated with that hierarchy. You can&#39;t change the type or data type of an existing property.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let assetModelId = "assetModelId_example"; // String | The ID of the asset model to update.
let updateAssetModelRequest = new AwsIoTSiteWise.UpdateAssetModelRequest(); // UpdateAssetModelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAssetModel(assetModelId, updateAssetModelRequest, opts, (error, data, response) => {
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
 **assetModelId** | **String**| The ID of the asset model to update. | 
 **updateAssetModelRequest** | [**UpdateAssetModelRequest**](UpdateAssetModelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAssetModelResponse**](UpdateAssetModelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAssetProperty

> updateAssetProperty(assetId, propertyId, updateAssetPropertyRequest, opts)



&lt;p&gt;Updates an asset property&#39;s alias and notification state.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This operation overwrites the property&#39;s existing alias and notification state. To keep your existing property&#39;s alias or notification state, you must include the existing values in the UpdateAssetProperty request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetProperty.html\&quot;&gt;DescribeAssetProperty&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let assetId = "assetId_example"; // String | The ID of the asset to be updated.
let propertyId = "propertyId_example"; // String | The ID of the asset property to be updated.
let updateAssetPropertyRequest = new AwsIoTSiteWise.UpdateAssetPropertyRequest(); // UpdateAssetPropertyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAssetProperty(assetId, propertyId, updateAssetPropertyRequest, opts, (error, data, response) => {
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
 **assetId** | **String**| The ID of the asset to be updated. | 
 **propertyId** | **String**| The ID of the asset property to be updated. | 
 **updateAssetPropertyRequest** | [**UpdateAssetPropertyRequest**](UpdateAssetPropertyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDashboard

> Object updateDashboard(dashboardId, updateDashboardRequest, opts)



Updates an IoT SiteWise Monitor dashboard.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let dashboardId = "dashboardId_example"; // String | The ID of the dashboard to update.
let updateDashboardRequest = new AwsIoTSiteWise.UpdateDashboardRequest(); // UpdateDashboardRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateDashboard(dashboardId, updateDashboardRequest, opts, (error, data, response) => {
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
 **dashboardId** | **String**| The ID of the dashboard to update. | 
 **updateDashboardRequest** | [**UpdateDashboardRequest**](UpdateDashboardRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateGateway

> updateGateway(gatewayId, updateGatewayRequest, opts)



Updates a gateway&#39;s name.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let gatewayId = "gatewayId_example"; // String | The ID of the gateway to update.
let updateGatewayRequest = new AwsIoTSiteWise.UpdateGatewayRequest(); // UpdateGatewayRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateGateway(gatewayId, updateGatewayRequest, opts, (error, data, response) => {
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
 **gatewayId** | **String**| The ID of the gateway to update. | 
 **updateGatewayRequest** | [**UpdateGatewayRequest**](UpdateGatewayRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateGatewayCapabilityConfiguration

> UpdateGatewayCapabilityConfigurationResponse updateGatewayCapabilityConfiguration(gatewayId, updateGatewayCapabilityConfigurationRequest, opts)



Updates a gateway capability configuration or defines a new capability configuration. Each gateway capability defines data sources for a gateway. A capability configuration can contain multiple data source configurations. If you define OPC-UA sources for a gateway in the IoT SiteWise console, all of your OPC-UA sources are stored in one capability configuration. To list all capability configurations for a gateway, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGateway.html\&quot;&gt;DescribeGateway&lt;/a&gt;.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let gatewayId = "gatewayId_example"; // String | The ID of the gateway to be updated.
let updateGatewayCapabilityConfigurationRequest = new AwsIoTSiteWise.UpdateGatewayCapabilityConfigurationRequest(); // UpdateGatewayCapabilityConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateGatewayCapabilityConfiguration(gatewayId, updateGatewayCapabilityConfigurationRequest, opts, (error, data, response) => {
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
 **gatewayId** | **String**| The ID of the gateway to be updated. | 
 **updateGatewayCapabilityConfigurationRequest** | [**UpdateGatewayCapabilityConfigurationRequest**](UpdateGatewayCapabilityConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateGatewayCapabilityConfigurationResponse**](UpdateGatewayCapabilityConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePortal

> UpdatePortalResponse updatePortal(portalId, updatePortalRequest, opts)



Updates an IoT SiteWise Monitor portal.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let portalId = "portalId_example"; // String | The ID of the portal to update.
let updatePortalRequest = new AwsIoTSiteWise.UpdatePortalRequest(); // UpdatePortalRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updatePortal(portalId, updatePortalRequest, opts, (error, data, response) => {
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
 **portalId** | **String**| The ID of the portal to update. | 
 **updatePortalRequest** | [**UpdatePortalRequest**](UpdatePortalRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdatePortalResponse**](UpdatePortalResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateProject

> Object updateProject(projectId, updateProjectRequest, opts)



Updates an IoT SiteWise Monitor project.

### Example

```javascript
import AwsIoTSiteWise from 'aws_io_t_site_wise';
let defaultClient = AwsIoTSiteWise.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTSiteWise.DefaultApi();
let projectId = "projectId_example"; // String | The ID of the project to update.
let updateProjectRequest = new AwsIoTSiteWise.UpdateProjectRequest(); // UpdateProjectRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateProject(projectId, updateProjectRequest, opts, (error, data, response) => {
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
 **projectId** | **String**| The ID of the project to update. | 
 **updateProjectRequest** | [**UpdateProjectRequest**](UpdateProjectRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

