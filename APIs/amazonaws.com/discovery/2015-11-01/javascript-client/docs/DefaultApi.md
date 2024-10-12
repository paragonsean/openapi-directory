# AwsApplicationDiscoveryService.DefaultApi

All URIs are relative to *http://discovery.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateConfigurationItemsToApplication**](DefaultApi.md#associateConfigurationItemsToApplication) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.AssociateConfigurationItemsToApplication | 
[**batchDeleteImportData**](DefaultApi.md#batchDeleteImportData) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.BatchDeleteImportData | 
[**createApplication**](DefaultApi.md#createApplication) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.CreateApplication | 
[**createTags**](DefaultApi.md#createTags) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.CreateTags | 
[**deleteApplications**](DefaultApi.md#deleteApplications) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.DeleteApplications | 
[**deleteTags**](DefaultApi.md#deleteTags) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.DeleteTags | 
[**describeAgents**](DefaultApi.md#describeAgents) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.DescribeAgents | 
[**describeConfigurations**](DefaultApi.md#describeConfigurations) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.DescribeConfigurations | 
[**describeContinuousExports**](DefaultApi.md#describeContinuousExports) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.DescribeContinuousExports | 
[**describeExportConfigurations**](DefaultApi.md#describeExportConfigurations) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.DescribeExportConfigurations | 
[**describeExportTasks**](DefaultApi.md#describeExportTasks) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.DescribeExportTasks | 
[**describeImportTasks**](DefaultApi.md#describeImportTasks) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.DescribeImportTasks | 
[**describeTags**](DefaultApi.md#describeTags) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.DescribeTags | 
[**disassociateConfigurationItemsFromApplication**](DefaultApi.md#disassociateConfigurationItemsFromApplication) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.DisassociateConfigurationItemsFromApplication | 
[**exportConfigurations**](DefaultApi.md#exportConfigurations) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.ExportConfigurations | 
[**getDiscoverySummary**](DefaultApi.md#getDiscoverySummary) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.GetDiscoverySummary | 
[**listConfigurations**](DefaultApi.md#listConfigurations) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.ListConfigurations | 
[**listServerNeighbors**](DefaultApi.md#listServerNeighbors) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.ListServerNeighbors | 
[**startContinuousExport**](DefaultApi.md#startContinuousExport) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.StartContinuousExport | 
[**startDataCollectionByAgentIds**](DefaultApi.md#startDataCollectionByAgentIds) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.StartDataCollectionByAgentIds | 
[**startExportTask**](DefaultApi.md#startExportTask) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.StartExportTask | 
[**startImportTask**](DefaultApi.md#startImportTask) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.StartImportTask | 
[**stopContinuousExport**](DefaultApi.md#stopContinuousExport) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.StopContinuousExport | 
[**stopDataCollectionByAgentIds**](DefaultApi.md#stopDataCollectionByAgentIds) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.StopDataCollectionByAgentIds | 
[**updateApplication**](DefaultApi.md#updateApplication) | **POST** /#X-Amz-Target&#x3D;AWSPoseidonService_V2015_11_01.UpdateApplication | 



## associateConfigurationItemsToApplication

> Object associateConfigurationItemsToApplication(xAmzTarget, associateConfigurationItemsToApplicationRequest, opts)



Associates one or more configuration items with an application.

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let associateConfigurationItemsToApplicationRequest = new AwsApplicationDiscoveryService.AssociateConfigurationItemsToApplicationRequest(); // AssociateConfigurationItemsToApplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateConfigurationItemsToApplication(xAmzTarget, associateConfigurationItemsToApplicationRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **associateConfigurationItemsToApplicationRequest** | [**AssociateConfigurationItemsToApplicationRequest**](AssociateConfigurationItemsToApplicationRequest.md)|  | 
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


## batchDeleteImportData

> BatchDeleteImportDataResponse batchDeleteImportData(xAmzTarget, batchDeleteImportDataRequest, opts)



&lt;p&gt;Deletes one or more import tasks, each identified by their import ID. Each import task has a number of records that can identify servers or applications. &lt;/p&gt; &lt;p&gt;Amazon Web Services Application Discovery Service has built-in matching logic that will identify when discovered servers match existing entries that you&#39;ve previously discovered, the information for the already-existing discovered server is updated. When you delete an import task that contains records that were used to match, the information in those matched records that comes from the deleted records will also be deleted.&lt;/p&gt;

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let batchDeleteImportDataRequest = new AwsApplicationDiscoveryService.BatchDeleteImportDataRequest(); // BatchDeleteImportDataRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchDeleteImportData(xAmzTarget, batchDeleteImportDataRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **batchDeleteImportDataRequest** | [**BatchDeleteImportDataRequest**](BatchDeleteImportDataRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchDeleteImportDataResponse**](BatchDeleteImportDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createApplication

> CreateApplicationResponse createApplication(xAmzTarget, createApplicationRequest, opts)



Creates an application with the given name and description.

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createApplicationRequest = new AwsApplicationDiscoveryService.CreateApplicationRequest(); // CreateApplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createApplication(xAmzTarget, createApplicationRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **createApplicationRequest** | [**CreateApplicationRequest**](CreateApplicationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateApplicationResponse**](CreateApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTags

> Object createTags(xAmzTarget, createTagsRequest, opts)



&lt;p&gt;Creates one or more tags for configuration items. Tags are metadata that help you categorize IT assets. This API accepts a list of multiple configuration items.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Do not store sensitive information (like personal data) in tags.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createTagsRequest = new AwsApplicationDiscoveryService.CreateTagsRequest(); // CreateTagsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createTags(xAmzTarget, createTagsRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **createTagsRequest** | [**CreateTagsRequest**](CreateTagsRequest.md)|  | 
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


## deleteApplications

> Object deleteApplications(xAmzTarget, deleteApplicationsRequest, opts)



Deletes a list of applications and their associations with configuration items.

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteApplicationsRequest = new AwsApplicationDiscoveryService.DeleteApplicationsRequest(); // DeleteApplicationsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApplications(xAmzTarget, deleteApplicationsRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **deleteApplicationsRequest** | [**DeleteApplicationsRequest**](DeleteApplicationsRequest.md)|  | 
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


## deleteTags

> Object deleteTags(xAmzTarget, deleteTagsRequest, opts)



Deletes the association between configuration items and one or more tags. This API accepts a list of multiple configuration items.

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteTagsRequest = new AwsApplicationDiscoveryService.DeleteTagsRequest(); // DeleteTagsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteTags(xAmzTarget, deleteTagsRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **deleteTagsRequest** | [**DeleteTagsRequest**](DeleteTagsRequest.md)|  | 
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


## describeAgents

> DescribeAgentsResponse describeAgents(xAmzTarget, describeAgentsRequest, opts)



Lists agents or collectors as specified by ID or other filters. All agents/collectors associated with your user can be listed if you call &lt;code&gt;DescribeAgents&lt;/code&gt; as is without passing any parameters.

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeAgentsRequest = new AwsApplicationDiscoveryService.DescribeAgentsRequest(); // DescribeAgentsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAgents(xAmzTarget, describeAgentsRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **describeAgentsRequest** | [**DescribeAgentsRequest**](DescribeAgentsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAgentsResponse**](DescribeAgentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeConfigurations

> DescribeConfigurationsResponse describeConfigurations(xAmzTarget, describeConfigurationsRequest, opts)



&lt;p&gt;Retrieves attributes for a list of configuration item IDs.&lt;/p&gt; &lt;note&gt; &lt;p&gt;All of the supplied IDs must be for the same asset type from one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;server&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;application&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;process&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;connection&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Output fields are specific to the asset type specified. For example, the output for a &lt;i&gt;server&lt;/i&gt; configuration item includes a list of attributes about the server, such as host name, operating system, number of network cards, etc.&lt;/p&gt; &lt;p&gt;For a complete list of outputs for each asset type, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-api-queries.html#DescribeConfigurations\&quot;&gt;Using the DescribeConfigurations Action&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Application Discovery Service User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeConfigurationsRequest = new AwsApplicationDiscoveryService.DescribeConfigurationsRequest(); // DescribeConfigurationsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeConfigurations(xAmzTarget, describeConfigurationsRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **describeConfigurationsRequest** | [**DescribeConfigurationsRequest**](DescribeConfigurationsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeConfigurationsResponse**](DescribeConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeContinuousExports

> DescribeContinuousExportsResponse describeContinuousExports(xAmzTarget, describeContinuousExportsRequest, opts)



Lists exports as specified by ID. All continuous exports associated with your user can be listed if you call &lt;code&gt;DescribeContinuousExports&lt;/code&gt; as is without passing any parameters.

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeContinuousExportsRequest = new AwsApplicationDiscoveryService.DescribeContinuousExportsRequest(); // DescribeContinuousExportsRequest | 
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
apiInstance.describeContinuousExports(xAmzTarget, describeContinuousExportsRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **describeContinuousExportsRequest** | [**DescribeContinuousExportsRequest**](DescribeContinuousExportsRequest.md)|  | 
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

[**DescribeContinuousExportsResponse**](DescribeContinuousExportsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeExportConfigurations

> DescribeExportConfigurationsResponse describeExportConfigurations(xAmzTarget, describeExportConfigurationsRequest, opts)



 &lt;code&gt;DescribeExportConfigurations&lt;/code&gt; is deprecated. Use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeExportTasks.html\&quot;&gt;DescribeExportTasks&lt;/a&gt;, instead.

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeExportConfigurationsRequest = new AwsApplicationDiscoveryService.DescribeExportConfigurationsRequest(); // DescribeExportConfigurationsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeExportConfigurations(xAmzTarget, describeExportConfigurationsRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **describeExportConfigurationsRequest** | [**DescribeExportConfigurationsRequest**](DescribeExportConfigurationsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeExportConfigurationsResponse**](DescribeExportConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeExportTasks

> DescribeExportTasksResponse describeExportTasks(xAmzTarget, describeExportTasksRequest, opts)



Retrieve status of one or more export tasks. You can retrieve the status of up to 100 export tasks.

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeExportTasksRequest = new AwsApplicationDiscoveryService.DescribeExportTasksRequest(); // DescribeExportTasksRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeExportTasks(xAmzTarget, describeExportTasksRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **describeExportTasksRequest** | [**DescribeExportTasksRequest**](DescribeExportTasksRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeExportTasksResponse**](DescribeExportTasksResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeImportTasks

> DescribeImportTasksResponse describeImportTasks(xAmzTarget, describeImportTasksRequest, opts)



Returns an array of import tasks for your account, including status information, times, IDs, the Amazon S3 Object URL for the import file, and more.

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeImportTasksRequest = new AwsApplicationDiscoveryService.DescribeImportTasksRequest(); // DescribeImportTasksRequest | 
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
apiInstance.describeImportTasks(xAmzTarget, describeImportTasksRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **describeImportTasksRequest** | [**DescribeImportTasksRequest**](DescribeImportTasksRequest.md)|  | 
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

[**DescribeImportTasksResponse**](DescribeImportTasksResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeTags

> DescribeTagsResponse describeTags(xAmzTarget, describeTagsRequest, opts)



&lt;p&gt;Retrieves a list of configuration items that have tags as specified by the key-value pairs, name and value, passed to the optional parameter &lt;code&gt;filters&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;There are three valid tag filter names:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;tagKey&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;tagValue&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;configurationId&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Also, all configuration items associated with your user that have tags can be listed if you call &lt;code&gt;DescribeTags&lt;/code&gt; as is without passing any parameters.&lt;/p&gt;

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeTagsRequest = new AwsApplicationDiscoveryService.DescribeTagsRequest(); // DescribeTagsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeTags(xAmzTarget, describeTagsRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **describeTagsRequest** | [**DescribeTagsRequest**](DescribeTagsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeTagsResponse**](DescribeTagsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disassociateConfigurationItemsFromApplication

> Object disassociateConfigurationItemsFromApplication(xAmzTarget, disassociateConfigurationItemsFromApplicationRequest, opts)



Disassociates one or more configuration items from an application.

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let disassociateConfigurationItemsFromApplicationRequest = new AwsApplicationDiscoveryService.DisassociateConfigurationItemsFromApplicationRequest(); // DisassociateConfigurationItemsFromApplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateConfigurationItemsFromApplication(xAmzTarget, disassociateConfigurationItemsFromApplicationRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **disassociateConfigurationItemsFromApplicationRequest** | [**DisassociateConfigurationItemsFromApplicationRequest**](DisassociateConfigurationItemsFromApplicationRequest.md)|  | 
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


## exportConfigurations

> ExportConfigurationsResponse exportConfigurations(xAmzTarget, opts)



&lt;p&gt;Deprecated. Use &lt;code&gt;StartExportTask&lt;/code&gt; instead.&lt;/p&gt; &lt;p&gt;Exports all discovered configuration data to an Amazon S3 bucket or an application that enables you to view and evaluate the data. Data includes tags and tag associations, processes, connections, servers, and system performance. This API returns an export ID that you can query using the &lt;i&gt;DescribeExportConfigurations&lt;/i&gt; API. The system imposes a limit of two configuration exports in six hours.&lt;/p&gt;

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.exportConfigurations(xAmzTarget, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ExportConfigurationsResponse**](ExportConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDiscoverySummary

> GetDiscoverySummaryResponse getDiscoverySummary(xAmzTarget, body, opts)



&lt;p&gt;Retrieves a short summary of discovered assets.&lt;/p&gt; &lt;p&gt;This API operation takes no request parameters and is called as is at the command prompt as shown in the example.&lt;/p&gt;

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let body = {key: null}; // Object | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDiscoverySummary(xAmzTarget, body, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **body** | **Object**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDiscoverySummaryResponse**](GetDiscoverySummaryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listConfigurations

> ListConfigurationsResponse listConfigurations(xAmzTarget, listConfigurationsRequest, opts)



Retrieves a list of configuration items as specified by the value passed to the required parameter &lt;code&gt;configurationType&lt;/code&gt;. Optional filtering may be applied to refine search results.

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listConfigurationsRequest = new AwsApplicationDiscoveryService.ListConfigurationsRequest(); // ListConfigurationsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listConfigurations(xAmzTarget, listConfigurationsRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **listConfigurationsRequest** | [**ListConfigurationsRequest**](ListConfigurationsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListConfigurationsResponse**](ListConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listServerNeighbors

> ListServerNeighborsResponse listServerNeighbors(xAmzTarget, listServerNeighborsRequest, opts)



Retrieves a list of servers that are one network hop away from a specified server.

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listServerNeighborsRequest = new AwsApplicationDiscoveryService.ListServerNeighborsRequest(); // ListServerNeighborsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listServerNeighbors(xAmzTarget, listServerNeighborsRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **listServerNeighborsRequest** | [**ListServerNeighborsRequest**](ListServerNeighborsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListServerNeighborsResponse**](ListServerNeighborsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startContinuousExport

> StartContinuousExportResponse startContinuousExport(xAmzTarget, body, opts)



Start the continuous flow of agent&#39;s discovered data into Amazon Athena.

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let body = {key: null}; // Object | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startContinuousExport(xAmzTarget, body, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **body** | **Object**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartContinuousExportResponse**](StartContinuousExportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startDataCollectionByAgentIds

> StartDataCollectionByAgentIdsResponse startDataCollectionByAgentIds(xAmzTarget, startDataCollectionByAgentIdsRequest, opts)



Instructs the specified agents to start collecting data.

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startDataCollectionByAgentIdsRequest = new AwsApplicationDiscoveryService.StartDataCollectionByAgentIdsRequest(); // StartDataCollectionByAgentIdsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startDataCollectionByAgentIds(xAmzTarget, startDataCollectionByAgentIdsRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **startDataCollectionByAgentIdsRequest** | [**StartDataCollectionByAgentIdsRequest**](StartDataCollectionByAgentIdsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartDataCollectionByAgentIdsResponse**](StartDataCollectionByAgentIdsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startExportTask

> StartExportTaskResponse startExportTask(xAmzTarget, startExportTaskRequest, opts)



&lt;p&gt;Begins the export of a discovered data report to an Amazon S3 bucket managed by Amazon Web Services.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Exports might provide an estimate of fees and savings based on certain information that you provide. Fee estimates do not include any taxes that might apply. Your actual fees and savings depend on a variety of factors, including your actual usage of Amazon Web Services services, which might vary from the estimates provided in this report.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;If you do not specify &lt;code&gt;preferences&lt;/code&gt; or &lt;code&gt;agentIds&lt;/code&gt; in the filter, a summary of all servers, applications, tags, and performance is generated. This data is an aggregation of all server data collected through on-premises tooling, file import, application grouping and applying tags.&lt;/p&gt; &lt;p&gt;If you specify &lt;code&gt;agentIds&lt;/code&gt; in a filter, the task exports up to 72 hours of detailed data collected by the identified Application Discovery Agent, including network, process, and performance details. A time range for exported agent data may be set by using &lt;code&gt;startTime&lt;/code&gt; and &lt;code&gt;endTime&lt;/code&gt;. Export of detailed agent data is limited to five concurrently running exports. Export of detailed agent data is limited to two exports per day.&lt;/p&gt; &lt;p&gt;If you enable &lt;code&gt;ec2RecommendationsPreferences&lt;/code&gt; in &lt;code&gt;preferences&lt;/code&gt; , an Amazon EC2 instance matching the characteristics of each server in Application Discovery Service is generated. Changing the attributes of the &lt;code&gt;ec2RecommendationsPreferences&lt;/code&gt; changes the criteria of the recommendation.&lt;/p&gt;

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startExportTaskRequest = new AwsApplicationDiscoveryService.StartExportTaskRequest(); // StartExportTaskRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startExportTask(xAmzTarget, startExportTaskRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **startExportTaskRequest** | [**StartExportTaskRequest**](StartExportTaskRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartExportTaskResponse**](StartExportTaskResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startImportTask

> StartImportTaskResponse startImportTask(xAmzTarget, startImportTaskRequest, opts)



&lt;p&gt;Starts an import task, which allows you to import details of your on-premises environment directly into Amazon Web Services Migration Hub without having to use the Amazon Web Services Application Discovery Service (Application Discovery Service) tools such as the Amazon Web Services Application Discovery Service Agentless Collector or Application Discovery Agent. This gives you the option to perform migration assessment and planning directly from your imported data, including the ability to group your devices as applications and track their migration status.&lt;/p&gt; &lt;p&gt;To start an import request, do this:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Download the specially formatted comma separated value (CSV) import template, which you can find here: &lt;a href&#x3D;\&quot;https://s3.us-west-2.amazonaws.com/templates-7cffcf56-bd96-4b1c-b45b-a5b42f282e46/import_template.csv\&quot;&gt;https://s3.us-west-2.amazonaws.com/templates-7cffcf56-bd96-4b1c-b45b-a5b42f282e46/import_template.csv&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Fill out the template with your server and application data.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Upload your import file to an Amazon S3 bucket, and make a note of it&#39;s Object URL. Your import file must be in the CSV format.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the console or the &lt;code&gt;StartImportTask&lt;/code&gt; command with the Amazon Web Services CLI or one of the Amazon Web Services SDKs to import the records from your file.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information, including step-by-step procedures, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-import.html\&quot;&gt;Migration Hub Import&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Application Discovery Service User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;There are limits to the number of import tasks you can create (and delete) in an Amazon Web Services account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/application-discovery/latest/userguide/ads_service_limits.html\&quot;&gt;Amazon Web Services Application Discovery Service Limits&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Application Discovery Service User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startImportTaskRequest = new AwsApplicationDiscoveryService.StartImportTaskRequest(); // StartImportTaskRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startImportTask(xAmzTarget, startImportTaskRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **startImportTaskRequest** | [**StartImportTaskRequest**](StartImportTaskRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartImportTaskResponse**](StartImportTaskResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopContinuousExport

> StopContinuousExportResponse stopContinuousExport(xAmzTarget, stopContinuousExportRequest, opts)



Stop the continuous flow of agent&#39;s discovered data into Amazon Athena.

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let stopContinuousExportRequest = new AwsApplicationDiscoveryService.StopContinuousExportRequest(); // StopContinuousExportRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopContinuousExport(xAmzTarget, stopContinuousExportRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **stopContinuousExportRequest** | [**StopContinuousExportRequest**](StopContinuousExportRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StopContinuousExportResponse**](StopContinuousExportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopDataCollectionByAgentIds

> StopDataCollectionByAgentIdsResponse stopDataCollectionByAgentIds(xAmzTarget, stopDataCollectionByAgentIdsRequest, opts)



Instructs the specified agents to stop collecting data.

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let stopDataCollectionByAgentIdsRequest = new AwsApplicationDiscoveryService.StopDataCollectionByAgentIdsRequest(); // StopDataCollectionByAgentIdsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopDataCollectionByAgentIds(xAmzTarget, stopDataCollectionByAgentIdsRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **stopDataCollectionByAgentIdsRequest** | [**StopDataCollectionByAgentIdsRequest**](StopDataCollectionByAgentIdsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StopDataCollectionByAgentIdsResponse**](StopDataCollectionByAgentIdsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateApplication

> Object updateApplication(xAmzTarget, updateApplicationRequest, opts)



Updates metadata about an application.

### Example

```javascript
import AwsApplicationDiscoveryService from 'aws_application_discovery_service';
let defaultClient = AwsApplicationDiscoveryService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsApplicationDiscoveryService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateApplicationRequest = new AwsApplicationDiscoveryService.UpdateApplicationRequest(); // UpdateApplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateApplication(xAmzTarget, updateApplicationRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **updateApplicationRequest** | [**UpdateApplicationRequest**](UpdateApplicationRequest.md)|  | 
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

