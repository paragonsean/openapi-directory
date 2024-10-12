# ManagedStreamingForKafka.DefaultApi

All URIs are relative to *http://kafka.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchAssociateScramSecret**](DefaultApi.md#batchAssociateScramSecret) | **POST** /v1/clusters/{clusterArn}/scram-secrets | 
[**batchDisassociateScramSecret**](DefaultApi.md#batchDisassociateScramSecret) | **PATCH** /v1/clusters/{clusterArn}/scram-secrets | 
[**createCluster**](DefaultApi.md#createCluster) | **POST** /v1/clusters | 
[**createClusterV2**](DefaultApi.md#createClusterV2) | **POST** /api/v2/clusters | 
[**createConfiguration**](DefaultApi.md#createConfiguration) | **POST** /v1/configurations | 
[**createVpcConnection**](DefaultApi.md#createVpcConnection) | **POST** /v1/vpc-connection | 
[**deleteCluster**](DefaultApi.md#deleteCluster) | **DELETE** /v1/clusters/{clusterArn} | 
[**deleteClusterPolicy**](DefaultApi.md#deleteClusterPolicy) | **DELETE** /v1/clusters/{clusterArn}/policy | 
[**deleteConfiguration**](DefaultApi.md#deleteConfiguration) | **DELETE** /v1/configurations/{arn} | 
[**deleteVpcConnection**](DefaultApi.md#deleteVpcConnection) | **DELETE** /v1/vpc-connection/{arn} | 
[**describeCluster**](DefaultApi.md#describeCluster) | **GET** /v1/clusters/{clusterArn} | 
[**describeClusterOperation**](DefaultApi.md#describeClusterOperation) | **GET** /v1/operations/{clusterOperationArn} | 
[**describeClusterOperationV2**](DefaultApi.md#describeClusterOperationV2) | **GET** /api/v2/operations/{clusterOperationArn} | 
[**describeClusterV2**](DefaultApi.md#describeClusterV2) | **GET** /api/v2/clusters/{clusterArn} | 
[**describeConfiguration**](DefaultApi.md#describeConfiguration) | **GET** /v1/configurations/{arn} | 
[**describeConfigurationRevision**](DefaultApi.md#describeConfigurationRevision) | **GET** /v1/configurations/{arn}/revisions/{revision} | 
[**describeVpcConnection**](DefaultApi.md#describeVpcConnection) | **GET** /v1/vpc-connection/{arn} | 
[**getBootstrapBrokers**](DefaultApi.md#getBootstrapBrokers) | **GET** /v1/clusters/{clusterArn}/bootstrap-brokers | 
[**getClusterPolicy**](DefaultApi.md#getClusterPolicy) | **GET** /v1/clusters/{clusterArn}/policy | 
[**getCompatibleKafkaVersions**](DefaultApi.md#getCompatibleKafkaVersions) | **GET** /v1/compatible-kafka-versions | 
[**listClientVpcConnections**](DefaultApi.md#listClientVpcConnections) | **GET** /v1/clusters/{clusterArn}/client-vpc-connections | 
[**listClusterOperations**](DefaultApi.md#listClusterOperations) | **GET** /v1/clusters/{clusterArn}/operations | 
[**listClusterOperationsV2**](DefaultApi.md#listClusterOperationsV2) | **GET** /api/v2/clusters/{clusterArn}/operations | 
[**listClusters**](DefaultApi.md#listClusters) | **GET** /v1/clusters | 
[**listClustersV2**](DefaultApi.md#listClustersV2) | **GET** /api/v2/clusters | 
[**listConfigurationRevisions**](DefaultApi.md#listConfigurationRevisions) | **GET** /v1/configurations/{arn}/revisions | 
[**listConfigurations**](DefaultApi.md#listConfigurations) | **GET** /v1/configurations | 
[**listKafkaVersions**](DefaultApi.md#listKafkaVersions) | **GET** /v1/kafka-versions | 
[**listNodes**](DefaultApi.md#listNodes) | **GET** /v1/clusters/{clusterArn}/nodes | 
[**listScramSecrets**](DefaultApi.md#listScramSecrets) | **GET** /v1/clusters/{clusterArn}/scram-secrets | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /v1/tags/{resourceArn} | 
[**listVpcConnections**](DefaultApi.md#listVpcConnections) | **GET** /v1/vpc-connections | 
[**putClusterPolicy**](DefaultApi.md#putClusterPolicy) | **PUT** /v1/clusters/{clusterArn}/policy | 
[**rebootBroker**](DefaultApi.md#rebootBroker) | **PUT** /v1/clusters/{clusterArn}/reboot-broker | 
[**rejectClientVpcConnection**](DefaultApi.md#rejectClientVpcConnection) | **PUT** /v1/clusters/{clusterArn}/client-vpc-connection | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /v1/tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /v1/tags/{resourceArn}#tagKeys | 
[**updateBrokerCount**](DefaultApi.md#updateBrokerCount) | **PUT** /v1/clusters/{clusterArn}/nodes/count | 
[**updateBrokerStorage**](DefaultApi.md#updateBrokerStorage) | **PUT** /v1/clusters/{clusterArn}/nodes/storage | 
[**updateBrokerType**](DefaultApi.md#updateBrokerType) | **PUT** /v1/clusters/{clusterArn}/nodes/type | 
[**updateClusterConfiguration**](DefaultApi.md#updateClusterConfiguration) | **PUT** /v1/clusters/{clusterArn}/configuration | 
[**updateClusterKafkaVersion**](DefaultApi.md#updateClusterKafkaVersion) | **PUT** /v1/clusters/{clusterArn}/version | 
[**updateConfiguration**](DefaultApi.md#updateConfiguration) | **PUT** /v1/configurations/{arn} | 
[**updateConnectivity**](DefaultApi.md#updateConnectivity) | **PUT** /v1/clusters/{clusterArn}/connectivity | 
[**updateMonitoring**](DefaultApi.md#updateMonitoring) | **PUT** /v1/clusters/{clusterArn}/monitoring | 
[**updateSecurity**](DefaultApi.md#updateSecurity) | **PATCH** /v1/clusters/{clusterArn}/security | 
[**updateStorage**](DefaultApi.md#updateStorage) | **PUT** /v1/clusters/{clusterArn}/storage | 



## batchAssociateScramSecret

> BatchAssociateScramSecretResponse batchAssociateScramSecret(clusterArn, batchAssociateScramSecretRequest, opts)



             &lt;p&gt;Associates one or more Scram Secrets with an Amazon MSK cluster.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) of the cluster to be updated.</p>          
let batchAssociateScramSecretRequest = new ManagedStreamingForKafka.BatchAssociateScramSecretRequest(); // BatchAssociateScramSecretRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchAssociateScramSecret(clusterArn, batchAssociateScramSecretRequest, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster to be updated.&lt;/p&gt;           | 
 **batchAssociateScramSecretRequest** | [**BatchAssociateScramSecretRequest**](BatchAssociateScramSecretRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchAssociateScramSecretResponse**](BatchAssociateScramSecretResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchDisassociateScramSecret

> BatchDisassociateScramSecretResponse batchDisassociateScramSecret(clusterArn, batchAssociateScramSecretRequest, opts)



             &lt;p&gt;Disassociates one or more Scram Secrets from an Amazon MSK cluster.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) of the cluster to be updated.</p>          
let batchAssociateScramSecretRequest = new ManagedStreamingForKafka.BatchAssociateScramSecretRequest(); // BatchAssociateScramSecretRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchDisassociateScramSecret(clusterArn, batchAssociateScramSecretRequest, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster to be updated.&lt;/p&gt;           | 
 **batchAssociateScramSecretRequest** | [**BatchAssociateScramSecretRequest**](BatchAssociateScramSecretRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchDisassociateScramSecretResponse**](BatchDisassociateScramSecretResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createCluster

> CreateClusterResponse createCluster(createClusterRequest, opts)



             &lt;p&gt;Creates a new MSK cluster.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let createClusterRequest = new ManagedStreamingForKafka.CreateClusterRequest(); // CreateClusterRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createCluster(createClusterRequest, opts, (error, data, response) => {
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
 **createClusterRequest** | [**CreateClusterRequest**](CreateClusterRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateClusterResponse**](CreateClusterResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createClusterV2

> CreateClusterV2Response createClusterV2(createClusterV2Request, opts)



             &lt;p&gt;Creates a new MSK cluster.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let createClusterV2Request = new ManagedStreamingForKafka.CreateClusterV2Request(); // CreateClusterV2Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createClusterV2(createClusterV2Request, opts, (error, data, response) => {
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
 **createClusterV2Request** | [**CreateClusterV2Request**](CreateClusterV2Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateClusterV2Response**](CreateClusterV2Response.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createConfiguration

> CreateConfigurationResponse createConfiguration(createConfigurationRequest, opts)



             &lt;p&gt;Creates a new MSK configuration.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let createConfigurationRequest = new ManagedStreamingForKafka.CreateConfigurationRequest(); // CreateConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createConfiguration(createConfigurationRequest, opts, (error, data, response) => {
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
 **createConfigurationRequest** | [**CreateConfigurationRequest**](CreateConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateConfigurationResponse**](CreateConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVpcConnection

> CreateVpcConnectionResponse createVpcConnection(createVpcConnectionRequest, opts)



             &lt;p&gt;Creates a new MSK VPC connection.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let createVpcConnectionRequest = new ManagedStreamingForKafka.CreateVpcConnectionRequest(); // CreateVpcConnectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createVpcConnection(createVpcConnectionRequest, opts, (error, data, response) => {
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
 **createVpcConnectionRequest** | [**CreateVpcConnectionRequest**](CreateVpcConnectionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateVpcConnectionResponse**](CreateVpcConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteCluster

> DeleteClusterResponse deleteCluster(clusterArn, opts)



             &lt;p&gt;Deletes the MSK cluster specified by the Amazon Resource Name (ARN) in the request.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>          
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'currentVersion': "currentVersion_example" // String |              <p>The current version of the MSK cluster.</p>          
};
apiInstance.deleteCluster(clusterArn, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;           | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **currentVersion** | **String**|              &lt;p&gt;The current version of the MSK cluster.&lt;/p&gt;           | [optional] 

### Return type

[**DeleteClusterResponse**](DeleteClusterResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteClusterPolicy

> Object deleteClusterPolicy(clusterArn, opts)



             &lt;p&gt;Deletes the MSK cluster policy specified by the Amazon Resource Name (ARN) in the request.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) of the cluster.</p>          
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteClusterPolicy(clusterArn, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster.&lt;/p&gt;           | 
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


## deleteConfiguration

> DeleteConfigurationResponse deleteConfiguration(arn, opts)



             &lt;p&gt;Deletes an MSK Configuration.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let arn = "arn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration.</p>          
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteConfiguration(arn, opts, (error, data, response) => {
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
 **arn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration.&lt;/p&gt;           | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteConfigurationResponse**](DeleteConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVpcConnection

> DeleteVpcConnectionResponse deleteVpcConnection(arn, opts)



             &lt;p&gt;Deletes a MSK VPC connection.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let arn = "arn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies an MSK VPC connection.</p>          
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteVpcConnection(arn, opts, (error, data, response) => {
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
 **arn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies an MSK VPC connection.&lt;/p&gt;           | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteVpcConnectionResponse**](DeleteVpcConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeCluster

> DescribeClusterResponse describeCluster(clusterArn, opts)



             &lt;p&gt;Returns a description of the MSK cluster whose Amazon Resource Name (ARN) is specified in the request.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>          
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeCluster(clusterArn, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;           | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeClusterResponse**](DescribeClusterResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeClusterOperation

> DescribeClusterOperationResponse describeClusterOperation(clusterOperationArn, opts)



             &lt;p&gt;Returns a description of the cluster operation specified by the ARN.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterOperationArn = "clusterOperationArn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies the MSK cluster operation.</p>          
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeClusterOperation(clusterOperationArn, opts, (error, data, response) => {
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
 **clusterOperationArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the MSK cluster operation.&lt;/p&gt;           | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeClusterOperationResponse**](DescribeClusterOperationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeClusterOperationV2

> DescribeClusterOperationV2Response describeClusterOperationV2(clusterOperationArn, opts)



             &lt;p&gt;Returns a description of the cluster operation specified by the ARN.&lt;/p&gt; 

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterOperationArn = "clusterOperationArn_example"; // String | ARN of the cluster operation to describe.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeClusterOperationV2(clusterOperationArn, opts, (error, data, response) => {
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
 **clusterOperationArn** | **String**| ARN of the cluster operation to describe. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeClusterOperationV2Response**](DescribeClusterOperationV2Response.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeClusterV2

> DescribeClusterV2Response describeClusterV2(clusterArn, opts)



             &lt;p&gt;Returns a description of the MSK cluster whose Amazon Resource Name (ARN) is specified in the request.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>          
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeClusterV2(clusterArn, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;           | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeClusterV2Response**](DescribeClusterV2Response.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeConfiguration

> DescribeConfigurationResponse describeConfiguration(arn, opts)



             &lt;p&gt;Returns a description of this MSK configuration.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let arn = "arn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions.</p>          
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeConfiguration(arn, opts, (error, data, response) => {
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
 **arn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions.&lt;/p&gt;           | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeConfigurationResponse**](DescribeConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeConfigurationRevision

> DescribeConfigurationRevisionResponse describeConfigurationRevision(arn, revision, opts)



             &lt;p&gt;Returns a description of this revision of the configuration.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let arn = "arn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions.</p>          
let revision = 56; // Number |              <p>A string that uniquely identifies a revision of an MSK configuration.</p>          
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeConfigurationRevision(arn, revision, opts, (error, data, response) => {
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
 **arn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions.&lt;/p&gt;           | 
 **revision** | **Number**|              &lt;p&gt;A string that uniquely identifies a revision of an MSK configuration.&lt;/p&gt;           | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeConfigurationRevisionResponse**](DescribeConfigurationRevisionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeVpcConnection

> DescribeVpcConnectionResponse describeVpcConnection(arn, opts)



             &lt;p&gt;Returns a description of this MSK VPC connection.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let arn = "arn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies a MSK VPC connection.</p>    
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeVpcConnection(arn, opts, (error, data, response) => {
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
 **arn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies a MSK VPC connection.&lt;/p&gt;     | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeVpcConnectionResponse**](DescribeVpcConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBootstrapBrokers

> GetBootstrapBrokersResponse getBootstrapBrokers(clusterArn, opts)



             &lt;p&gt;A list of brokers that a client application can use to bootstrap.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>          
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBootstrapBrokers(clusterArn, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;           | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBootstrapBrokersResponse**](GetBootstrapBrokersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClusterPolicy

> GetClusterPolicyResponse getClusterPolicy(clusterArn, opts)



             &lt;p&gt;Get the MSK cluster policy specified by the Amazon Resource Name (ARN) in the request.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) of the cluster.</p>             
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getClusterPolicy(clusterArn, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster.&lt;/p&gt;              | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetClusterPolicyResponse**](GetClusterPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompatibleKafkaVersions

> GetCompatibleKafkaVersionsResponse getCompatibleKafkaVersions(opts)



             &lt;p&gt;Gets the Apache Kafka versions to which you can update the MSK cluster.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clusterArn': "clusterArn_example" // String |              <p>The Amazon Resource Name (ARN) of the cluster check.</p>             
};
apiInstance.getCompatibleKafkaVersions(opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster check.&lt;/p&gt;              | [optional] 

### Return type

[**GetCompatibleKafkaVersionsResponse**](GetCompatibleKafkaVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listClientVpcConnections

> ListClientVpcConnectionsResponse listClientVpcConnections(clusterArn, opts)



             &lt;p&gt;Returns a list of all the VPC connections in this Region.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) of the cluster.</p>          
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number |              <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>          
  'nextToken': "nextToken_example", // String |              <p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.</p>          
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listClientVpcConnections(clusterArn, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster.&lt;/p&gt;           | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**|              &lt;p&gt;The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.&lt;/p&gt;           | [optional] 
 **nextToken** | **String**|              &lt;p&gt;The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.&lt;/p&gt;           | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListClientVpcConnectionsResponse**](ListClientVpcConnectionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listClusterOperations

> ListClusterOperationsResponse listClusterOperations(clusterArn, opts)



             &lt;p&gt;Returns a list of all the operations that have been performed on the specified MSK cluster.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>          
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number |              <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>          
  'nextToken': "nextToken_example", // String |              <p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.</p>          
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listClusterOperations(clusterArn, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;           | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**|              &lt;p&gt;The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.&lt;/p&gt;           | [optional] 
 **nextToken** | **String**|              &lt;p&gt;The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.&lt;/p&gt;           | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListClusterOperationsResponse**](ListClusterOperationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listClusterOperationsV2

> ListClusterOperationsV2Response listClusterOperationsV2(clusterArn, opts)



             &lt;p&gt;Returns a list of all the operations that have been performed on the specified MSK cluster.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String | The arn of the cluster whose operations are being requested.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maxResults of the query.
  'nextToken': "nextToken_example", // String | The nextToken of the query.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listClusterOperationsV2(clusterArn, opts, (error, data, response) => {
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
 **clusterArn** | **String**| The arn of the cluster whose operations are being requested. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maxResults of the query. | [optional] 
 **nextToken** | **String**| The nextToken of the query. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListClusterOperationsV2Response**](ListClusterOperationsV2Response.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listClusters

> ListClustersResponse listClusters(opts)



             &lt;p&gt;Returns a list of all the MSK clusters in the current Region.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clusterNameFilter': "clusterNameFilter_example", // String |              <p>Specify a prefix of the name of the clusters that you want to list. The service lists all the clusters whose names start with this prefix.</p>          
  'maxResults': 56, // Number |              <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>          
  'nextToken': "nextToken_example", // String |              <p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.</p>          
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listClusters(opts, (error, data, response) => {
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
 **clusterNameFilter** | **String**|              &lt;p&gt;Specify a prefix of the name of the clusters that you want to list. The service lists all the clusters whose names start with this prefix.&lt;/p&gt;           | [optional] 
 **maxResults** | **Number**|              &lt;p&gt;The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.&lt;/p&gt;           | [optional] 
 **nextToken** | **String**|              &lt;p&gt;The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.&lt;/p&gt;           | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListClustersResponse**](ListClustersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listClustersV2

> ListClustersV2Response listClustersV2(opts)



             &lt;p&gt;Returns a list of all the MSK clusters in the current Region.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clusterNameFilter': "clusterNameFilter_example", // String |              <p>Specify a prefix of the names of the clusters that you want to list. The service lists all the clusters whose names start with this prefix.</p>          
  'clusterTypeFilter': "clusterTypeFilter_example", // String |              <p>Specify either PROVISIONED or SERVERLESS.</p>          
  'maxResults': 56, // Number |              <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>          
  'nextToken': "nextToken_example", // String |              <p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.</p>          
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listClustersV2(opts, (error, data, response) => {
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
 **clusterNameFilter** | **String**|              &lt;p&gt;Specify a prefix of the names of the clusters that you want to list. The service lists all the clusters whose names start with this prefix.&lt;/p&gt;           | [optional] 
 **clusterTypeFilter** | **String**|              &lt;p&gt;Specify either PROVISIONED or SERVERLESS.&lt;/p&gt;           | [optional] 
 **maxResults** | **Number**|              &lt;p&gt;The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.&lt;/p&gt;           | [optional] 
 **nextToken** | **String**|              &lt;p&gt;The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.&lt;/p&gt;           | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListClustersV2Response**](ListClustersV2Response.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConfigurationRevisions

> ListConfigurationRevisionsResponse listConfigurationRevisions(arn, opts)



             &lt;p&gt;Returns a list of all the MSK configurations in this Region.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let arn = "arn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions.</p>          
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number |              <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>          
  'nextToken': "nextToken_example", // String |              <p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.</p>          
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listConfigurationRevisions(arn, opts, (error, data, response) => {
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
 **arn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions.&lt;/p&gt;           | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**|              &lt;p&gt;The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.&lt;/p&gt;           | [optional] 
 **nextToken** | **String**|              &lt;p&gt;The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.&lt;/p&gt;           | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListConfigurationRevisionsResponse**](ListConfigurationRevisionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConfigurations

> ListConfigurationsResponse listConfigurations(opts)



             &lt;p&gt;Returns a list of all the MSK configurations in this Region.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number |              <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>          
  'nextToken': "nextToken_example", // String |              <p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.</p>          
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listConfigurations(opts, (error, data, response) => {
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
 **maxResults** | **Number**|              &lt;p&gt;The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.&lt;/p&gt;           | [optional] 
 **nextToken** | **String**|              &lt;p&gt;The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.&lt;/p&gt;           | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListConfigurationsResponse**](ListConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listKafkaVersions

> ListKafkaVersionsResponse listKafkaVersions(opts)



             &lt;p&gt;Returns a list of Apache Kafka versions.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number |              <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>
  'nextToken': "nextToken_example", // String |              <p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.</p>
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listKafkaVersions(opts, (error, data, response) => {
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
 **maxResults** | **Number**|              &lt;p&gt;The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.&lt;/p&gt; | [optional] 
 **nextToken** | **String**|              &lt;p&gt;The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.&lt;/p&gt; | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListKafkaVersionsResponse**](ListKafkaVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listNodes

> ListNodesResponse listNodes(clusterArn, opts)



             &lt;p&gt;Returns a list of the broker nodes in the cluster.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>          
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number |              <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>          
  'nextToken': "nextToken_example", // String |              <p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.</p>          
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listNodes(clusterArn, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;           | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**|              &lt;p&gt;The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.&lt;/p&gt;           | [optional] 
 **nextToken** | **String**|              &lt;p&gt;The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.&lt;/p&gt;           | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListNodesResponse**](ListNodesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listScramSecrets

> ListScramSecretsResponse listScramSecrets(clusterArn, opts)



             &lt;p&gt;Returns a list of the Scram Secrets associated with an Amazon MSK cluster.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The arn of the cluster.</p>          
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number |              <p>The maxResults of the query.</p>          
  'nextToken': "nextToken_example", // String |              <p>The nextToken of the query.</p>          
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listScramSecrets(clusterArn, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The arn of the cluster.&lt;/p&gt;           | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**|              &lt;p&gt;The maxResults of the query.&lt;/p&gt;           | [optional] 
 **nextToken** | **String**|              &lt;p&gt;The nextToken of the query.&lt;/p&gt;           | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListScramSecretsResponse**](ListScramSecretsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



             &lt;p&gt;Returns a list of the tags associated with the specified resource.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let resourceArn = "resourceArn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies the resource that's associated with the tags.</p>          
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
 **resourceArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the resource that&#39;s associated with the tags.&lt;/p&gt;           | 
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


## listVpcConnections

> ListVpcConnectionsResponse listVpcConnections(opts)



             &lt;p&gt;Returns a list of all the VPC connections in this Region.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number |              <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>          
  'nextToken': "nextToken_example", // String |              <p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.</p>          
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listVpcConnections(opts, (error, data, response) => {
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
 **maxResults** | **Number**|              &lt;p&gt;The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.&lt;/p&gt;           | [optional] 
 **nextToken** | **String**|              &lt;p&gt;The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.&lt;/p&gt;           | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListVpcConnectionsResponse**](ListVpcConnectionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putClusterPolicy

> PutClusterPolicyResponse putClusterPolicy(clusterArn, putClusterPolicyRequest, opts)



             &lt;p&gt;Creates or updates the MSK cluster policy specified by the cluster Amazon Resource Name (ARN) in the request.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) of the cluster.</p>          
let putClusterPolicyRequest = new ManagedStreamingForKafka.PutClusterPolicyRequest(); // PutClusterPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putClusterPolicy(clusterArn, putClusterPolicyRequest, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster.&lt;/p&gt;           | 
 **putClusterPolicyRequest** | [**PutClusterPolicyRequest**](PutClusterPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutClusterPolicyResponse**](PutClusterPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## rebootBroker

> RebootBrokerResponse rebootBroker(clusterArn, rebootBrokerRequest, opts)



Reboots brokers.

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) of the cluster to be updated.</p>          
let rebootBrokerRequest = new ManagedStreamingForKafka.RebootBrokerRequest(); // RebootBrokerRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.rebootBroker(clusterArn, rebootBrokerRequest, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster to be updated.&lt;/p&gt;           | 
 **rebootBrokerRequest** | [**RebootBrokerRequest**](RebootBrokerRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RebootBrokerResponse**](RebootBrokerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## rejectClientVpcConnection

> Object rejectClientVpcConnection(clusterArn, rejectClientVpcConnectionRequest, opts)



             &lt;p&gt;Returns empty response.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) of the cluster.</p>          
let rejectClientVpcConnectionRequest = new ManagedStreamingForKafka.RejectClientVpcConnectionRequest(); // RejectClientVpcConnectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.rejectClientVpcConnection(clusterArn, rejectClientVpcConnectionRequest, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster.&lt;/p&gt;           | 
 **rejectClientVpcConnectionRequest** | [**RejectClientVpcConnectionRequest**](RejectClientVpcConnectionRequest.md)|  | 
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


## tagResource

> tagResource(resourceArn, tagResourceRequest, opts)



             &lt;p&gt;Adds tags to the specified MSK resource.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let resourceArn = "resourceArn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies the resource that's associated with the tags.</p>          
let tagResourceRequest = new ManagedStreamingForKafka.TagResourceRequest(); // TagResourceRequest | 
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
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the resource that&#39;s associated with the tags.&lt;/p&gt;           | 
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
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


## untagResource

> untagResource(resourceArn, tagKeys, opts)



             &lt;p&gt;Removes the tags associated with the keys that are provided in the query.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let resourceArn = "resourceArn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies the resource that's associated with the tags.</p>          
let tagKeys = ["null"]; // [String] |              <p>Tag keys must be unique for a given cluster. In addition, the following restrictions apply:</p>             <ul>                <li>                   <p>Each tag key must be unique. If you add a tag with a key that's already in                   use, your new tag overwrites the existing key-value pair. </p>                </li>                <li>                   <p>You can't start a tag key with aws: because this prefix is reserved for use                   by  AWS.  AWS creates tags that begin with this prefix on your behalf, but                   you can't edit or delete them.</p>                </li>                <li>                   <p>Tag keys must be between 1 and 128 Unicode characters in length.</p>                </li>                <li>                   <p>Tag keys must consist of the following characters: Unicode letters, digits,                   white space, and the following special characters: _ . / = + -                      @.</p>                </li>             </ul>          
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
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the resource that&#39;s associated with the tags.&lt;/p&gt;           | 
 **tagKeys** | [**[String]**](String.md)|              &lt;p&gt;Tag keys must be unique for a given cluster. In addition, the following restrictions apply:&lt;/p&gt;             &lt;ul&gt;                &lt;li&gt;                   &lt;p&gt;Each tag key must be unique. If you add a tag with a key that&#39;s already in                   use, your new tag overwrites the existing key-value pair. &lt;/p&gt;                &lt;/li&gt;                &lt;li&gt;                   &lt;p&gt;You can&#39;t start a tag key with aws: because this prefix is reserved for use                   by  AWS.  AWS creates tags that begin with this prefix on your behalf, but                   you can&#39;t edit or delete them.&lt;/p&gt;                &lt;/li&gt;                &lt;li&gt;                   &lt;p&gt;Tag keys must be between 1 and 128 Unicode characters in length.&lt;/p&gt;                &lt;/li&gt;                &lt;li&gt;                   &lt;p&gt;Tag keys must consist of the following characters: Unicode letters, digits,                   white space, and the following special characters: _ . / &#x3D; + -                      @.&lt;/p&gt;                &lt;/li&gt;             &lt;/ul&gt;           | 
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


## updateBrokerCount

> UpdateBrokerCountResponse updateBrokerCount(clusterArn, updateBrokerCountRequest, opts)



             &lt;p&gt;Updates the number of broker nodes in the cluster.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>          
let updateBrokerCountRequest = new ManagedStreamingForKafka.UpdateBrokerCountRequest(); // UpdateBrokerCountRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateBrokerCount(clusterArn, updateBrokerCountRequest, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;           | 
 **updateBrokerCountRequest** | [**UpdateBrokerCountRequest**](UpdateBrokerCountRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateBrokerCountResponse**](UpdateBrokerCountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBrokerStorage

> UpdateBrokerStorageResponse updateBrokerStorage(clusterArn, updateBrokerStorageRequest, opts)



             &lt;p&gt;Updates the EBS storage associated with MSK brokers.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>          
let updateBrokerStorageRequest = new ManagedStreamingForKafka.UpdateBrokerStorageRequest(); // UpdateBrokerStorageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateBrokerStorage(clusterArn, updateBrokerStorageRequest, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;           | 
 **updateBrokerStorageRequest** | [**UpdateBrokerStorageRequest**](UpdateBrokerStorageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateBrokerStorageResponse**](UpdateBrokerStorageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBrokerType

> UpdateBrokerTypeResponse updateBrokerType(clusterArn, updateBrokerTypeRequest, opts)



             &lt;p&gt;Updates EC2 instance type.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>          
let updateBrokerTypeRequest = new ManagedStreamingForKafka.UpdateBrokerTypeRequest(); // UpdateBrokerTypeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateBrokerType(clusterArn, updateBrokerTypeRequest, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;           | 
 **updateBrokerTypeRequest** | [**UpdateBrokerTypeRequest**](UpdateBrokerTypeRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateBrokerTypeResponse**](UpdateBrokerTypeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateClusterConfiguration

> UpdateClusterConfigurationResponse updateClusterConfiguration(clusterArn, updateClusterConfigurationRequest, opts)



             &lt;p&gt;Updates the cluster with the configuration that is specified in the request body.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>          
let updateClusterConfigurationRequest = new ManagedStreamingForKafka.UpdateClusterConfigurationRequest(); // UpdateClusterConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateClusterConfiguration(clusterArn, updateClusterConfigurationRequest, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;           | 
 **updateClusterConfigurationRequest** | [**UpdateClusterConfigurationRequest**](UpdateClusterConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateClusterConfigurationResponse**](UpdateClusterConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateClusterKafkaVersion

> UpdateClusterKafkaVersionResponse updateClusterKafkaVersion(clusterArn, updateClusterKafkaVersionRequest, opts)



             &lt;p&gt;Updates the Apache Kafka version for the cluster.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) of the cluster to be updated.</p>             
let updateClusterKafkaVersionRequest = new ManagedStreamingForKafka.UpdateClusterKafkaVersionRequest(); // UpdateClusterKafkaVersionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateClusterKafkaVersion(clusterArn, updateClusterKafkaVersionRequest, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster to be updated.&lt;/p&gt;              | 
 **updateClusterKafkaVersionRequest** | [**UpdateClusterKafkaVersionRequest**](UpdateClusterKafkaVersionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateClusterKafkaVersionResponse**](UpdateClusterKafkaVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateConfiguration

> UpdateConfigurationResponse updateConfiguration(arn, updateConfigurationRequest, opts)



             &lt;p&gt;Updates an MSK configuration.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let arn = "arn_example"; // String |              <p>The Amazon Resource Name (ARN) of the configuration.</p>          
let updateConfigurationRequest = new ManagedStreamingForKafka.UpdateConfigurationRequest(); // UpdateConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateConfiguration(arn, updateConfigurationRequest, opts, (error, data, response) => {
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
 **arn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) of the configuration.&lt;/p&gt;           | 
 **updateConfigurationRequest** | [**UpdateConfigurationRequest**](UpdateConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateConfigurationResponse**](UpdateConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateConnectivity

> UpdateConnectivityResponse updateConnectivity(clusterArn, updateConnectivityRequest, opts)



             &lt;p&gt;Updates the cluster&#39;s connectivity configuration.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) of the configuration.</p>          
let updateConnectivityRequest = new ManagedStreamingForKafka.UpdateConnectivityRequest(); // UpdateConnectivityRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateConnectivity(clusterArn, updateConnectivityRequest, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) of the configuration.&lt;/p&gt;           | 
 **updateConnectivityRequest** | [**UpdateConnectivityRequest**](UpdateConnectivityRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateConnectivityResponse**](UpdateConnectivityResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMonitoring

> UpdateMonitoringResponse updateMonitoring(clusterArn, updateMonitoringRequest, opts)



             &lt;p&gt;Updates the monitoring settings for the cluster. You can use this operation to specify which Apache Kafka metrics you want Amazon MSK to send to Amazon CloudWatch. You can also specify settings for open monitoring with Prometheus.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>          
let updateMonitoringRequest = new ManagedStreamingForKafka.UpdateMonitoringRequest(); // UpdateMonitoringRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateMonitoring(clusterArn, updateMonitoringRequest, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;           | 
 **updateMonitoringRequest** | [**UpdateMonitoringRequest**](UpdateMonitoringRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateMonitoringResponse**](UpdateMonitoringResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSecurity

> UpdateSecurityResponse updateSecurity(clusterArn, updateSecurityRequest, opts)



             &lt;p&gt;Updates the security settings for the cluster. You can use this operation to specify encryption and authentication on existing clusters.&lt;/p&gt;          

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>          
let updateSecurityRequest = new ManagedStreamingForKafka.UpdateSecurityRequest(); // UpdateSecurityRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSecurity(clusterArn, updateSecurityRequest, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;           | 
 **updateSecurityRequest** | [**UpdateSecurityRequest**](UpdateSecurityRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSecurityResponse**](UpdateSecurityResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateStorage

> UpdateStorageResponse updateStorage(clusterArn, updateStorageRequest, opts)



Updates cluster broker volume size (or) sets cluster storage mode to TIERED.

### Example

```javascript
import ManagedStreamingForKafka from 'managed_streaming_for_kafka';
let defaultClient = ManagedStreamingForKafka.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ManagedStreamingForKafka.DefaultApi();
let clusterArn = "clusterArn_example"; // String |              <p>The Amazon Resource Name (ARN) of the cluster to be updated.</p>          
let updateStorageRequest = new ManagedStreamingForKafka.UpdateStorageRequest(); // UpdateStorageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateStorage(clusterArn, updateStorageRequest, opts, (error, data, response) => {
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
 **clusterArn** | **String**|              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster to be updated.&lt;/p&gt;           | 
 **updateStorageRequest** | [**UpdateStorageRequest**](UpdateStorageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateStorageResponse**](UpdateStorageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

