# AmazonCognitoSync.DefaultApi

All URIs are relative to *http://cognito-sync.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkPublish**](DefaultApi.md#bulkPublish) | **POST** /identitypools/{IdentityPoolId}/bulkpublish | 
[**deleteDataset**](DefaultApi.md#deleteDataset) | **DELETE** /identitypools/{IdentityPoolId}/identities/{IdentityId}/datasets/{DatasetName} | 
[**describeDataset**](DefaultApi.md#describeDataset) | **GET** /identitypools/{IdentityPoolId}/identities/{IdentityId}/datasets/{DatasetName} | 
[**describeIdentityPoolUsage**](DefaultApi.md#describeIdentityPoolUsage) | **GET** /identitypools/{IdentityPoolId} | 
[**describeIdentityUsage**](DefaultApi.md#describeIdentityUsage) | **GET** /identitypools/{IdentityPoolId}/identities/{IdentityId} | 
[**getBulkPublishDetails**](DefaultApi.md#getBulkPublishDetails) | **POST** /identitypools/{IdentityPoolId}/getBulkPublishDetails | 
[**getCognitoEvents**](DefaultApi.md#getCognitoEvents) | **GET** /identitypools/{IdentityPoolId}/events | 
[**getIdentityPoolConfiguration**](DefaultApi.md#getIdentityPoolConfiguration) | **GET** /identitypools/{IdentityPoolId}/configuration | 
[**listDatasets**](DefaultApi.md#listDatasets) | **GET** /identitypools/{IdentityPoolId}/identities/{IdentityId}/datasets | 
[**listIdentityPoolUsage**](DefaultApi.md#listIdentityPoolUsage) | **GET** /identitypools | 
[**listRecords**](DefaultApi.md#listRecords) | **GET** /identitypools/{IdentityPoolId}/identities/{IdentityId}/datasets/{DatasetName}/records | 
[**registerDevice**](DefaultApi.md#registerDevice) | **POST** /identitypools/{IdentityPoolId}/identity/{IdentityId}/device | 
[**setCognitoEvents**](DefaultApi.md#setCognitoEvents) | **POST** /identitypools/{IdentityPoolId}/events | 
[**setIdentityPoolConfiguration**](DefaultApi.md#setIdentityPoolConfiguration) | **POST** /identitypools/{IdentityPoolId}/configuration | 
[**subscribeToDataset**](DefaultApi.md#subscribeToDataset) | **POST** /identitypools/{IdentityPoolId}/identities/{IdentityId}/datasets/{DatasetName}/subscriptions/{DeviceId} | 
[**unsubscribeFromDataset**](DefaultApi.md#unsubscribeFromDataset) | **DELETE** /identitypools/{IdentityPoolId}/identities/{IdentityId}/datasets/{DatasetName}/subscriptions/{DeviceId} | 
[**updateRecords**](DefaultApi.md#updateRecords) | **POST** /identitypools/{IdentityPoolId}/identities/{IdentityId}/datasets/{DatasetName} | 



## bulkPublish

> BulkPublishResponse bulkPublish(identityPoolId, opts)



&lt;p&gt;Initiates a bulk publish of all existing datasets for an Identity Pool to the configured stream. Customers are limited to one successful bulk publish per 24 hours. Bulk publish is an asynchronous request, customers can see the status of the request via the GetBulkPublishDetails operation.&lt;/p&gt;&lt;p&gt;This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoSync from 'amazon_cognito_sync';
let defaultClient = AmazonCognitoSync.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoSync.DefaultApi();
let identityPoolId = "identityPoolId_example"; // String | A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.bulkPublish(identityPoolId, opts, (error, data, response) => {
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
 **identityPoolId** | **String**| A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BulkPublishResponse**](BulkPublishResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDataset

> DeleteDatasetResponse deleteDataset(identityPoolId, identityId, datasetName, opts)



&lt;p&gt;Deletes the specific dataset. The dataset will be deleted permanently, and the action can&#39;t be undone. Datasets that this dataset was merged with will no longer report the merge. Any subsequent operation on this dataset will result in a ResourceNotFoundException.&lt;/p&gt; &lt;p&gt;This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoSync from 'amazon_cognito_sync';
let defaultClient = AmazonCognitoSync.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoSync.DefaultApi();
let identityPoolId = "identityPoolId_example"; // String | A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
let identityId = "identityId_example"; // String | A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
let datasetName = "datasetName_example"; // String | A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteDataset(identityPoolId, identityId, datasetName, opts, (error, data, response) => {
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
 **identityPoolId** | **String**| A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region. | 
 **identityId** | **String**| A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region. | 
 **datasetName** | **String**| A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, &#39;_&#39; (underscore), &#39;-&#39; (dash), and &#39;.&#39; (dot). | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteDatasetResponse**](DeleteDatasetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeDataset

> DescribeDatasetResponse describeDataset(identityPoolId, identityId, datasetName, opts)



&lt;p&gt;Gets meta data about a dataset by identity and dataset name. With Amazon Cognito Sync, each identity has access only to its own data. Thus, the credentials used to make this API call need to have access to the identity data.&lt;/p&gt; &lt;p&gt;This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials. You should use Cognito Identity credentials to make this API call.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoSync from 'amazon_cognito_sync';
let defaultClient = AmazonCognitoSync.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoSync.DefaultApi();
let identityPoolId = "identityPoolId_example"; // String | A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
let identityId = "identityId_example"; // String | A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
let datasetName = "datasetName_example"; // String | A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeDataset(identityPoolId, identityId, datasetName, opts, (error, data, response) => {
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
 **identityPoolId** | **String**| A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region. | 
 **identityId** | **String**| A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region. | 
 **datasetName** | **String**| A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, &#39;_&#39; (underscore), &#39;-&#39; (dash), and &#39;.&#39; (dot). | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeDatasetResponse**](DescribeDatasetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeIdentityPoolUsage

> DescribeIdentityPoolUsageResponse describeIdentityPoolUsage(identityPoolId, opts)



&lt;p&gt;Gets usage details (for example, data storage) about a particular identity pool.&lt;/p&gt; &lt;p&gt;This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoSync from 'amazon_cognito_sync';
let defaultClient = AmazonCognitoSync.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoSync.DefaultApi();
let identityPoolId = "identityPoolId_example"; // String | A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeIdentityPoolUsage(identityPoolId, opts, (error, data, response) => {
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
 **identityPoolId** | **String**| A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeIdentityPoolUsageResponse**](DescribeIdentityPoolUsageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeIdentityUsage

> DescribeIdentityUsageResponse describeIdentityUsage(identityPoolId, identityId, opts)



&lt;p&gt;Gets usage information for an identity, including number of datasets and data usage.&lt;/p&gt; &lt;p&gt;This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoSync from 'amazon_cognito_sync';
let defaultClient = AmazonCognitoSync.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoSync.DefaultApi();
let identityPoolId = "identityPoolId_example"; // String | A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
let identityId = "identityId_example"; // String | A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeIdentityUsage(identityPoolId, identityId, opts, (error, data, response) => {
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
 **identityPoolId** | **String**| A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region. | 
 **identityId** | **String**| A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeIdentityUsageResponse**](DescribeIdentityUsageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBulkPublishDetails

> GetBulkPublishDetailsResponse getBulkPublishDetails(identityPoolId, opts)



&lt;p&gt;Get the status of the last BulkPublish operation for an identity pool.&lt;/p&gt;&lt;p&gt;This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoSync from 'amazon_cognito_sync';
let defaultClient = AmazonCognitoSync.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoSync.DefaultApi();
let identityPoolId = "identityPoolId_example"; // String | A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBulkPublishDetails(identityPoolId, opts, (error, data, response) => {
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
 **identityPoolId** | **String**| A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBulkPublishDetailsResponse**](GetBulkPublishDetailsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCognitoEvents

> GetCognitoEventsResponse getCognitoEvents(identityPoolId, opts)



&lt;p&gt;Gets the events and the corresponding Lambda functions associated with an identity pool.&lt;/p&gt;&lt;p&gt;This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoSync from 'amazon_cognito_sync';
let defaultClient = AmazonCognitoSync.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoSync.DefaultApi();
let identityPoolId = "identityPoolId_example"; // String | The Cognito Identity Pool ID for the request
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getCognitoEvents(identityPoolId, opts, (error, data, response) => {
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
 **identityPoolId** | **String**| The Cognito Identity Pool ID for the request | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetCognitoEventsResponse**](GetCognitoEventsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIdentityPoolConfiguration

> GetIdentityPoolConfigurationResponse getIdentityPoolConfiguration(identityPoolId, opts)



&lt;p&gt;Gets the configuration settings of an identity pool.&lt;/p&gt;&lt;p&gt;This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoSync from 'amazon_cognito_sync';
let defaultClient = AmazonCognitoSync.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoSync.DefaultApi();
let identityPoolId = "identityPoolId_example"; // String | A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. This is the ID of the pool for which to return a configuration.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getIdentityPoolConfiguration(identityPoolId, opts, (error, data, response) => {
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
 **identityPoolId** | **String**| A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. This is the ID of the pool for which to return a configuration. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetIdentityPoolConfigurationResponse**](GetIdentityPoolConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDatasets

> ListDatasetsResponse listDatasets(identityPoolId, identityId, opts)



&lt;p&gt;Lists datasets for an identity. With Amazon Cognito Sync, each identity has access only to its own data. Thus, the credentials used to make this API call need to have access to the identity data.&lt;/p&gt; &lt;p&gt;ListDatasets can be called with temporary user credentials provided by Cognito Identity or with developer credentials. You should use the Cognito Identity credentials to make this API call.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoSync from 'amazon_cognito_sync';
let defaultClient = AmazonCognitoSync.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoSync.DefaultApi();
let identityPoolId = "identityPoolId_example"; // String | A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
let identityId = "identityId_example"; // String | A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A pagination token for obtaining the next page of results.
  'maxResults': 56 // Number | The maximum number of results to be returned.
};
apiInstance.listDatasets(identityPoolId, identityId, opts, (error, data, response) => {
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
 **identityPoolId** | **String**| A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region. | 
 **identityId** | **String**| A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| A pagination token for obtaining the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned. | [optional] 

### Return type

[**ListDatasetsResponse**](ListDatasetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listIdentityPoolUsage

> ListIdentityPoolUsageResponse listIdentityPoolUsage(opts)



&lt;p&gt;Gets a list of identity pools registered with Cognito.&lt;/p&gt; &lt;p&gt;ListIdentityPoolUsage can only be called with developer credentials. You cannot make this API call with the temporary user credentials provided by Cognito Identity.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoSync from 'amazon_cognito_sync';
let defaultClient = AmazonCognitoSync.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoSync.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A pagination token for obtaining the next page of results.
  'maxResults': 56 // Number | The maximum number of results to be returned.
};
apiInstance.listIdentityPoolUsage(opts, (error, data, response) => {
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
 **nextToken** | **String**| A pagination token for obtaining the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned. | [optional] 

### Return type

[**ListIdentityPoolUsageResponse**](ListIdentityPoolUsageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRecords

> ListRecordsResponse listRecords(identityPoolId, identityId, datasetName, opts)



&lt;p&gt;Gets paginated records, optionally changed after a particular sync count for a dataset and identity. With Amazon Cognito Sync, each identity has access only to its own data. Thus, the credentials used to make this API call need to have access to the identity data.&lt;/p&gt; &lt;p&gt;ListRecords can be called with temporary user credentials provided by Cognito Identity or with developer credentials. You should use Cognito Identity credentials to make this API call.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoSync from 'amazon_cognito_sync';
let defaultClient = AmazonCognitoSync.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoSync.DefaultApi();
let identityPoolId = "identityPoolId_example"; // String | A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
let identityId = "identityId_example"; // String | A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
let datasetName = "datasetName_example"; // String | A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'lastSyncCount': 56, // Number | The last server sync count for this record.
  'nextToken': "nextToken_example", // String | A pagination token for obtaining the next page of results.
  'maxResults': 56, // Number | The maximum number of results to be returned.
  'syncSessionToken': "syncSessionToken_example" // String | A token containing a session ID, identity ID, and expiration.
};
apiInstance.listRecords(identityPoolId, identityId, datasetName, opts, (error, data, response) => {
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
 **identityPoolId** | **String**| A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region. | 
 **identityId** | **String**| A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region. | 
 **datasetName** | **String**| A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, &#39;_&#39; (underscore), &#39;-&#39; (dash), and &#39;.&#39; (dot). | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **lastSyncCount** | **Number**| The last server sync count for this record. | [optional] 
 **nextToken** | **String**| A pagination token for obtaining the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned. | [optional] 
 **syncSessionToken** | **String**| A token containing a session ID, identity ID, and expiration. | [optional] 

### Return type

[**ListRecordsResponse**](ListRecordsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registerDevice

> RegisterDeviceResponse registerDevice(identityPoolId, identityId, registerDeviceRequest, opts)



&lt;p&gt;Registers a device to receive push sync notifications.&lt;/p&gt;&lt;p&gt;This API can only be called with temporary credentials provided by Cognito Identity. You cannot call this API with developer credentials.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoSync from 'amazon_cognito_sync';
let defaultClient = AmazonCognitoSync.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoSync.DefaultApi();
let identityPoolId = "identityPoolId_example"; // String | A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. Here, the ID of the pool that the identity belongs to.
let identityId = "identityId_example"; // String | The unique ID for this identity.
let registerDeviceRequest = new AmazonCognitoSync.RegisterDeviceRequest(); // RegisterDeviceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.registerDevice(identityPoolId, identityId, registerDeviceRequest, opts, (error, data, response) => {
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
 **identityPoolId** | **String**| A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. Here, the ID of the pool that the identity belongs to. | 
 **identityId** | **String**| The unique ID for this identity. | 
 **registerDeviceRequest** | [**RegisterDeviceRequest**](RegisterDeviceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RegisterDeviceResponse**](RegisterDeviceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setCognitoEvents

> setCognitoEvents(identityPoolId, setCognitoEventsRequest, opts)



&lt;p&gt;Sets the AWS Lambda function for a given event type for an identity pool. This request only updates the key/value pair specified. Other key/values pairs are not updated. To remove a key value pair, pass a empty value for the particular key.&lt;/p&gt;&lt;p&gt;This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoSync from 'amazon_cognito_sync';
let defaultClient = AmazonCognitoSync.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoSync.DefaultApi();
let identityPoolId = "identityPoolId_example"; // String | The Cognito Identity Pool to use when configuring Cognito Events
let setCognitoEventsRequest = new AmazonCognitoSync.SetCognitoEventsRequest(); // SetCognitoEventsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.setCognitoEvents(identityPoolId, setCognitoEventsRequest, opts, (error, data, response) => {
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
 **identityPoolId** | **String**| The Cognito Identity Pool to use when configuring Cognito Events | 
 **setCognitoEventsRequest** | [**SetCognitoEventsRequest**](SetCognitoEventsRequest.md)|  | 
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


## setIdentityPoolConfiguration

> SetIdentityPoolConfigurationResponse setIdentityPoolConfiguration(identityPoolId, setIdentityPoolConfigurationRequest, opts)



&lt;p&gt;Sets the necessary configuration for push sync.&lt;/p&gt;&lt;p&gt;This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoSync from 'amazon_cognito_sync';
let defaultClient = AmazonCognitoSync.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoSync.DefaultApi();
let identityPoolId = "identityPoolId_example"; // String | A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. This is the ID of the pool to modify.
let setIdentityPoolConfigurationRequest = new AmazonCognitoSync.SetIdentityPoolConfigurationRequest(); // SetIdentityPoolConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.setIdentityPoolConfiguration(identityPoolId, setIdentityPoolConfigurationRequest, opts, (error, data, response) => {
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
 **identityPoolId** | **String**| A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. This is the ID of the pool to modify. | 
 **setIdentityPoolConfigurationRequest** | [**SetIdentityPoolConfigurationRequest**](SetIdentityPoolConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SetIdentityPoolConfigurationResponse**](SetIdentityPoolConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## subscribeToDataset

> Object subscribeToDataset(identityPoolId, identityId, datasetName, deviceId, opts)



&lt;p&gt;Subscribes to receive notifications when a dataset is modified by another device.&lt;/p&gt;&lt;p&gt;This API can only be called with temporary credentials provided by Cognito Identity. You cannot call this API with developer credentials.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoSync from 'amazon_cognito_sync';
let defaultClient = AmazonCognitoSync.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoSync.DefaultApi();
let identityPoolId = "identityPoolId_example"; // String | A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The ID of the pool to which the identity belongs.
let identityId = "identityId_example"; // String | Unique ID for this identity.
let datasetName = "datasetName_example"; // String | The name of the dataset to subcribe to.
let deviceId = "deviceId_example"; // String | The unique ID generated for this device by Cognito.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.subscribeToDataset(identityPoolId, identityId, datasetName, deviceId, opts, (error, data, response) => {
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
 **identityPoolId** | **String**| A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The ID of the pool to which the identity belongs. | 
 **identityId** | **String**| Unique ID for this identity. | 
 **datasetName** | **String**| The name of the dataset to subcribe to. | 
 **deviceId** | **String**| The unique ID generated for this device by Cognito. | 
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


## unsubscribeFromDataset

> Object unsubscribeFromDataset(identityPoolId, identityId, datasetName, deviceId, opts)



&lt;p&gt;Unsubscribes from receiving notifications when a dataset is modified by another device.&lt;/p&gt;&lt;p&gt;This API can only be called with temporary credentials provided by Cognito Identity. You cannot call this API with developer credentials.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoSync from 'amazon_cognito_sync';
let defaultClient = AmazonCognitoSync.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoSync.DefaultApi();
let identityPoolId = "identityPoolId_example"; // String | A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The ID of the pool to which this identity belongs.
let identityId = "identityId_example"; // String | Unique ID for this identity.
let datasetName = "datasetName_example"; // String | The name of the dataset from which to unsubcribe.
let deviceId = "deviceId_example"; // String | The unique ID generated for this device by Cognito.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.unsubscribeFromDataset(identityPoolId, identityId, datasetName, deviceId, opts, (error, data, response) => {
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
 **identityPoolId** | **String**| A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The ID of the pool to which this identity belongs. | 
 **identityId** | **String**| Unique ID for this identity. | 
 **datasetName** | **String**| The name of the dataset from which to unsubcribe. | 
 **deviceId** | **String**| The unique ID generated for this device by Cognito. | 
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


## updateRecords

> UpdateRecordsResponse updateRecords(identityPoolId, identityId, datasetName, updateRecordsRequest, opts)



&lt;p&gt;Posts updates to records and adds and deletes records for a dataset and user.&lt;/p&gt; &lt;p&gt;The sync count in the record patch is your last known sync count for that record. The server will reject an UpdateRecords request with a ResourceConflictException if you try to patch a record with a new value but a stale sync count.&lt;/p&gt;&lt;p&gt;For example, if the sync count on the server is 5 for a key called highScore and you try and submit a new highScore with sync count of 4, the request will be rejected. To obtain the current sync count for a record, call ListRecords. On a successful update of the record, the response returns the new sync count for that record. You should present that sync count the next time you try to update that same record. When the record does not exist, specify the sync count as 0.&lt;/p&gt; &lt;p&gt;This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoSync from 'amazon_cognito_sync';
let defaultClient = AmazonCognitoSync.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoSync.DefaultApi();
let identityPoolId = "identityPoolId_example"; // String | A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
let identityId = "identityId_example"; // String | A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
let datasetName = "datasetName_example"; // String | A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).
let updateRecordsRequest = new AmazonCognitoSync.UpdateRecordsRequest(); // UpdateRecordsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientContext': "xAmzClientContext_example" // String | Intended to supply a device ID that will populate the lastModifiedBy field referenced in other methods. The ClientContext field is not yet implemented.
};
apiInstance.updateRecords(identityPoolId, identityId, datasetName, updateRecordsRequest, opts, (error, data, response) => {
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
 **identityPoolId** | **String**| A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region. | 
 **identityId** | **String**| A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region. | 
 **datasetName** | **String**| A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, &#39;_&#39; (underscore), &#39;-&#39; (dash), and &#39;.&#39; (dot). | 
 **updateRecordsRequest** | [**UpdateRecordsRequest**](UpdateRecordsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientContext** | **String**| Intended to supply a device ID that will populate the lastModifiedBy field referenced in other methods. The ClientContext field is not yet implemented. | [optional] 

### Return type

[**UpdateRecordsResponse**](UpdateRecordsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

