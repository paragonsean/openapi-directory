# AmazonMemoryDb.DefaultApi

All URIs are relative to *http://memory-db.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchUpdateCluster**](DefaultApi.md#batchUpdateCluster) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.BatchUpdateCluster | 
[**copySnapshot**](DefaultApi.md#copySnapshot) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.CopySnapshot | 
[**createACL**](DefaultApi.md#createACL) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.CreateACL | 
[**createCluster**](DefaultApi.md#createCluster) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.CreateCluster | 
[**createParameterGroup**](DefaultApi.md#createParameterGroup) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.CreateParameterGroup | 
[**createSnapshot**](DefaultApi.md#createSnapshot) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.CreateSnapshot | 
[**createSubnetGroup**](DefaultApi.md#createSubnetGroup) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.CreateSubnetGroup | 
[**createUser**](DefaultApi.md#createUser) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.CreateUser | 
[**deleteACL**](DefaultApi.md#deleteACL) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.DeleteACL | 
[**deleteCluster**](DefaultApi.md#deleteCluster) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.DeleteCluster | 
[**deleteParameterGroup**](DefaultApi.md#deleteParameterGroup) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.DeleteParameterGroup | 
[**deleteSnapshot**](DefaultApi.md#deleteSnapshot) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.DeleteSnapshot | 
[**deleteSubnetGroup**](DefaultApi.md#deleteSubnetGroup) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.DeleteSubnetGroup | 
[**deleteUser**](DefaultApi.md#deleteUser) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.DeleteUser | 
[**describeACLs**](DefaultApi.md#describeACLs) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.DescribeACLs | 
[**describeClusters**](DefaultApi.md#describeClusters) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.DescribeClusters | 
[**describeEngineVersions**](DefaultApi.md#describeEngineVersions) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.DescribeEngineVersions | 
[**describeEvents**](DefaultApi.md#describeEvents) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.DescribeEvents | 
[**describeParameterGroups**](DefaultApi.md#describeParameterGroups) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.DescribeParameterGroups | 
[**describeParameters**](DefaultApi.md#describeParameters) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.DescribeParameters | 
[**describeReservedNodes**](DefaultApi.md#describeReservedNodes) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.DescribeReservedNodes | 
[**describeReservedNodesOfferings**](DefaultApi.md#describeReservedNodesOfferings) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.DescribeReservedNodesOfferings | 
[**describeServiceUpdates**](DefaultApi.md#describeServiceUpdates) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.DescribeServiceUpdates | 
[**describeSnapshots**](DefaultApi.md#describeSnapshots) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.DescribeSnapshots | 
[**describeSubnetGroups**](DefaultApi.md#describeSubnetGroups) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.DescribeSubnetGroups | 
[**describeUsers**](DefaultApi.md#describeUsers) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.DescribeUsers | 
[**failoverShard**](DefaultApi.md#failoverShard) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.FailoverShard | 
[**listAllowedNodeTypeUpdates**](DefaultApi.md#listAllowedNodeTypeUpdates) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.ListAllowedNodeTypeUpdates | 
[**listTags**](DefaultApi.md#listTags) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.ListTags | 
[**purchaseReservedNodesOffering**](DefaultApi.md#purchaseReservedNodesOffering) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.PurchaseReservedNodesOffering | 
[**resetParameterGroup**](DefaultApi.md#resetParameterGroup) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.ResetParameterGroup | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.TagResource | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.UntagResource | 
[**updateACL**](DefaultApi.md#updateACL) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.UpdateACL | 
[**updateCluster**](DefaultApi.md#updateCluster) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.UpdateCluster | 
[**updateParameterGroup**](DefaultApi.md#updateParameterGroup) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.UpdateParameterGroup | 
[**updateSubnetGroup**](DefaultApi.md#updateSubnetGroup) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.UpdateSubnetGroup | 
[**updateUser**](DefaultApi.md#updateUser) | **POST** /#X-Amz-Target&#x3D;AmazonMemoryDB.UpdateUser | 



## batchUpdateCluster

> BatchUpdateClusterResponse batchUpdateCluster(xAmzTarget, batchUpdateClusterRequest, opts)



Apply the service update to a list of clusters supplied. For more information on service updates and applying them, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/MemoryDB/latest/devguide/managing-updates.html#applying-updates\&quot;&gt;Applying the service updates&lt;/a&gt;.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let batchUpdateClusterRequest = new AmazonMemoryDb.BatchUpdateClusterRequest(); // BatchUpdateClusterRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchUpdateCluster(xAmzTarget, batchUpdateClusterRequest, opts, (error, data, response) => {
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
 **batchUpdateClusterRequest** | [**BatchUpdateClusterRequest**](BatchUpdateClusterRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchUpdateClusterResponse**](BatchUpdateClusterResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## copySnapshot

> CopySnapshotResponse copySnapshot(xAmzTarget, copySnapshotRequest, opts)



Makes a copy of an existing snapshot.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let copySnapshotRequest = new AmazonMemoryDb.CopySnapshotRequest(); // CopySnapshotRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.copySnapshot(xAmzTarget, copySnapshotRequest, opts, (error, data, response) => {
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
 **copySnapshotRequest** | [**CopySnapshotRequest**](CopySnapshotRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CopySnapshotResponse**](CopySnapshotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createACL

> CreateACLResponse createACL(xAmzTarget, createACLRequest, opts)



Creates an Access Control List. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/MemoryDB/latest/devguide/clusters.acls.html\&quot;&gt;Authenticating users with Access Contol Lists (ACLs)&lt;/a&gt;.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createACLRequest = new AmazonMemoryDb.CreateACLRequest(); // CreateACLRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createACL(xAmzTarget, createACLRequest, opts, (error, data, response) => {
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
 **createACLRequest** | [**CreateACLRequest**](CreateACLRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateACLResponse**](CreateACLResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createCluster

> CreateClusterResponse createCluster(xAmzTarget, createClusterRequest, opts)



Creates a cluster. All nodes in the cluster run the same protocol-compliant engine software.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createClusterRequest = new AmazonMemoryDb.CreateClusterRequest(); // CreateClusterRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createCluster(xAmzTarget, createClusterRequest, opts, (error, data, response) => {
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


## createParameterGroup

> CreateParameterGroupResponse createParameterGroup(xAmzTarget, createParameterGroupRequest, opts)



Creates a new MemoryDB parameter group. A parameter group is a collection of parameters and their values that are applied to all of the nodes in any cluster. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/MemoryDB/latest/devguide/parametergroups.html\&quot;&gt;Configuring engine parameters using parameter groups&lt;/a&gt;. 

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createParameterGroupRequest = new AmazonMemoryDb.CreateParameterGroupRequest(); // CreateParameterGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createParameterGroup(xAmzTarget, createParameterGroupRequest, opts, (error, data, response) => {
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
 **createParameterGroupRequest** | [**CreateParameterGroupRequest**](CreateParameterGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateParameterGroupResponse**](CreateParameterGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSnapshot

> CreateSnapshotResponse createSnapshot(xAmzTarget, createSnapshotRequest, opts)



Creates a copy of an entire cluster at a specific moment in time.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createSnapshotRequest = new AmazonMemoryDb.CreateSnapshotRequest(); // CreateSnapshotRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSnapshot(xAmzTarget, createSnapshotRequest, opts, (error, data, response) => {
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
 **createSnapshotRequest** | [**CreateSnapshotRequest**](CreateSnapshotRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSnapshotResponse**](CreateSnapshotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSubnetGroup

> CreateSubnetGroupResponse createSubnetGroup(xAmzTarget, createSubnetGroupRequest, opts)



Creates a subnet group. A subnet group is a collection of subnets (typically private) that you can designate for your clusters running in an Amazon Virtual Private Cloud (VPC) environment. When you create a cluster in an Amazon VPC, you must specify a subnet group. MemoryDB uses that subnet group to choose a subnet and IP addresses within that subnet to associate with your nodes. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/MemoryDB/latest/devguide/subnetgroups.html\&quot;&gt;Subnets and subnet groups&lt;/a&gt;.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createSubnetGroupRequest = new AmazonMemoryDb.CreateSubnetGroupRequest(); // CreateSubnetGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSubnetGroup(xAmzTarget, createSubnetGroupRequest, opts, (error, data, response) => {
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
 **createSubnetGroupRequest** | [**CreateSubnetGroupRequest**](CreateSubnetGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSubnetGroupResponse**](CreateSubnetGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createUser

> CreateUserResponse createUser(xAmzTarget, createUserRequest, opts)



Creates a MemoryDB user. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/MemoryDB/latest/devguide/clusters.acls.html\&quot;&gt;Authenticating users with Access Contol Lists (ACLs)&lt;/a&gt;.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createUserRequest = new AmazonMemoryDb.CreateUserRequest(); // CreateUserRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createUser(xAmzTarget, createUserRequest, opts, (error, data, response) => {
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
 **createUserRequest** | [**CreateUserRequest**](CreateUserRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteACL

> DeleteACLResponse deleteACL(xAmzTarget, deleteACLRequest, opts)



Deletes an Access Control List. The ACL must first be disassociated from the cluster before it can be deleted. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/MemoryDB/latest/devguide/clusters.acls.html\&quot;&gt;Authenticating users with Access Contol Lists (ACLs)&lt;/a&gt;.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteACLRequest = new AmazonMemoryDb.DeleteACLRequest(); // DeleteACLRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteACL(xAmzTarget, deleteACLRequest, opts, (error, data, response) => {
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
 **deleteACLRequest** | [**DeleteACLRequest**](DeleteACLRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteACLResponse**](DeleteACLResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteCluster

> DeleteClusterResponse deleteCluster(xAmzTarget, deleteClusterRequest, opts)



Deletes a cluster. It also deletes all associated nodes and node endpoints

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteClusterRequest = new AmazonMemoryDb.DeleteClusterRequest(); // DeleteClusterRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteCluster(xAmzTarget, deleteClusterRequest, opts, (error, data, response) => {
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
 **deleteClusterRequest** | [**DeleteClusterRequest**](DeleteClusterRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteClusterResponse**](DeleteClusterResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteParameterGroup

> DeleteParameterGroupResponse deleteParameterGroup(xAmzTarget, deleteParameterGroupRequest, opts)



Deletes the specified parameter group. You cannot delete a parameter group if it is associated with any clusters. You cannot delete the default parameter groups in your account.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteParameterGroupRequest = new AmazonMemoryDb.DeleteParameterGroupRequest(); // DeleteParameterGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteParameterGroup(xAmzTarget, deleteParameterGroupRequest, opts, (error, data, response) => {
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
 **deleteParameterGroupRequest** | [**DeleteParameterGroupRequest**](DeleteParameterGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteParameterGroupResponse**](DeleteParameterGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSnapshot

> DeleteSnapshotResponse deleteSnapshot(xAmzTarget, deleteSnapshotRequest, opts)



Deletes an existing snapshot. When you receive a successful response from this operation, MemoryDB immediately begins deleting the snapshot; you cannot cancel or revert this operation.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteSnapshotRequest = new AmazonMemoryDb.DeleteSnapshotRequest(); // DeleteSnapshotRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSnapshot(xAmzTarget, deleteSnapshotRequest, opts, (error, data, response) => {
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
 **deleteSnapshotRequest** | [**DeleteSnapshotRequest**](DeleteSnapshotRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteSnapshotResponse**](DeleteSnapshotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSubnetGroup

> DeleteSubnetGroupResponse deleteSubnetGroup(xAmzTarget, deleteSubnetGroupRequest, opts)



Deletes a subnet group. You cannot delete a default subnet group or one that is associated with any clusters.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteSubnetGroupRequest = new AmazonMemoryDb.DeleteSubnetGroupRequest(); // DeleteSubnetGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSubnetGroup(xAmzTarget, deleteSubnetGroupRequest, opts, (error, data, response) => {
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
 **deleteSubnetGroupRequest** | [**DeleteSubnetGroupRequest**](DeleteSubnetGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteSubnetGroupResponse**](DeleteSubnetGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteUser

> DeleteUserResponse deleteUser(xAmzTarget, deleteUserRequest, opts)



Deletes a user. The user will be removed from all ACLs and in turn removed from all clusters.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteUserRequest = new AmazonMemoryDb.DeleteUserRequest(); // DeleteUserRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteUser(xAmzTarget, deleteUserRequest, opts, (error, data, response) => {
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
 **deleteUserRequest** | [**DeleteUserRequest**](DeleteUserRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteUserResponse**](DeleteUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeACLs

> DescribeACLsResponse describeACLs(xAmzTarget, describeACLsRequest, opts)



Returns a list of ACLs

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeACLsRequest = new AmazonMemoryDb.DescribeACLsRequest(); // DescribeACLsRequest | 
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
apiInstance.describeACLs(xAmzTarget, describeACLsRequest, opts, (error, data, response) => {
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
 **describeACLsRequest** | [**DescribeACLsRequest**](DescribeACLsRequest.md)|  | 
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

[**DescribeACLsResponse**](DescribeACLsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeClusters

> DescribeClustersResponse describeClusters(xAmzTarget, describeClustersRequest, opts)



Returns information about all provisioned clusters if no cluster identifier is specified, or about a specific cluster if a cluster name is supplied.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeClustersRequest = new AmazonMemoryDb.DescribeClustersRequest(); // DescribeClustersRequest | 
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
apiInstance.describeClusters(xAmzTarget, describeClustersRequest, opts, (error, data, response) => {
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
 **describeClustersRequest** | [**DescribeClustersRequest**](DescribeClustersRequest.md)|  | 
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

[**DescribeClustersResponse**](DescribeClustersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeEngineVersions

> DescribeEngineVersionsResponse describeEngineVersions(xAmzTarget, describeEngineVersionsRequest, opts)



Returns a list of the available Redis engine versions.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeEngineVersionsRequest = new AmazonMemoryDb.DescribeEngineVersionsRequest(); // DescribeEngineVersionsRequest | 
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
apiInstance.describeEngineVersions(xAmzTarget, describeEngineVersionsRequest, opts, (error, data, response) => {
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
 **describeEngineVersionsRequest** | [**DescribeEngineVersionsRequest**](DescribeEngineVersionsRequest.md)|  | 
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

[**DescribeEngineVersionsResponse**](DescribeEngineVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeEvents

> DescribeEventsResponse describeEvents(xAmzTarget, describeEventsRequest, opts)



Returns events related to clusters, security groups, and parameter groups. You can obtain events specific to a particular cluster, security group, or parameter group by providing the name as a parameter. By default, only the events occurring within the last hour are returned; however, you can retrieve up to 14 days&#39; worth of events if necessary.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeEventsRequest = new AmazonMemoryDb.DescribeEventsRequest(); // DescribeEventsRequest | 
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
apiInstance.describeEvents(xAmzTarget, describeEventsRequest, opts, (error, data, response) => {
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
 **describeEventsRequest** | [**DescribeEventsRequest**](DescribeEventsRequest.md)|  | 
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

[**DescribeEventsResponse**](DescribeEventsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeParameterGroups

> DescribeParameterGroupsResponse describeParameterGroups(xAmzTarget, describeParameterGroupsRequest, opts)



Returns a list of parameter group descriptions. If a parameter group name is specified, the list contains only the descriptions for that group.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeParameterGroupsRequest = new AmazonMemoryDb.DescribeParameterGroupsRequest(); // DescribeParameterGroupsRequest | 
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
apiInstance.describeParameterGroups(xAmzTarget, describeParameterGroupsRequest, opts, (error, data, response) => {
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
 **describeParameterGroupsRequest** | [**DescribeParameterGroupsRequest**](DescribeParameterGroupsRequest.md)|  | 
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

[**DescribeParameterGroupsResponse**](DescribeParameterGroupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeParameters

> DescribeParametersResponse describeParameters(xAmzTarget, describeParametersRequest, opts)



Returns the detailed parameter list for a particular parameter group.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeParametersRequest = new AmazonMemoryDb.DescribeParametersRequest(); // DescribeParametersRequest | 
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
apiInstance.describeParameters(xAmzTarget, describeParametersRequest, opts, (error, data, response) => {
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
 **describeParametersRequest** | [**DescribeParametersRequest**](DescribeParametersRequest.md)|  | 
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

[**DescribeParametersResponse**](DescribeParametersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeReservedNodes

> DescribeReservedNodesResponse describeReservedNodes(xAmzTarget, describeReservedNodesRequest, opts)



Returns information about reserved nodes for this account, or about a specified reserved node.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeReservedNodesRequest = new AmazonMemoryDb.DescribeReservedNodesRequest(); // DescribeReservedNodesRequest | 
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
apiInstance.describeReservedNodes(xAmzTarget, describeReservedNodesRequest, opts, (error, data, response) => {
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
 **describeReservedNodesRequest** | [**DescribeReservedNodesRequest**](DescribeReservedNodesRequest.md)|  | 
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

[**DescribeReservedNodesResponse**](DescribeReservedNodesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeReservedNodesOfferings

> DescribeReservedNodesOfferingsResponse describeReservedNodesOfferings(xAmzTarget, describeReservedNodesOfferingsRequest, opts)



Lists available reserved node offerings.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeReservedNodesOfferingsRequest = new AmazonMemoryDb.DescribeReservedNodesOfferingsRequest(); // DescribeReservedNodesOfferingsRequest | 
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
apiInstance.describeReservedNodesOfferings(xAmzTarget, describeReservedNodesOfferingsRequest, opts, (error, data, response) => {
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
 **describeReservedNodesOfferingsRequest** | [**DescribeReservedNodesOfferingsRequest**](DescribeReservedNodesOfferingsRequest.md)|  | 
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

[**DescribeReservedNodesOfferingsResponse**](DescribeReservedNodesOfferingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeServiceUpdates

> DescribeServiceUpdatesResponse describeServiceUpdates(xAmzTarget, describeServiceUpdatesRequest, opts)



Returns details of the service updates

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeServiceUpdatesRequest = new AmazonMemoryDb.DescribeServiceUpdatesRequest(); // DescribeServiceUpdatesRequest | 
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
apiInstance.describeServiceUpdates(xAmzTarget, describeServiceUpdatesRequest, opts, (error, data, response) => {
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
 **describeServiceUpdatesRequest** | [**DescribeServiceUpdatesRequest**](DescribeServiceUpdatesRequest.md)|  | 
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

[**DescribeServiceUpdatesResponse**](DescribeServiceUpdatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeSnapshots

> DescribeSnapshotsResponse describeSnapshots(xAmzTarget, describeSnapshotsRequest, opts)



Returns information about cluster snapshots. By default, DescribeSnapshots lists all of your snapshots; it can optionally describe a single snapshot, or just the snapshots associated with a particular cluster.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeSnapshotsRequest = new AmazonMemoryDb.DescribeSnapshotsRequest(); // DescribeSnapshotsRequest | 
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
apiInstance.describeSnapshots(xAmzTarget, describeSnapshotsRequest, opts, (error, data, response) => {
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
 **describeSnapshotsRequest** | [**DescribeSnapshotsRequest**](DescribeSnapshotsRequest.md)|  | 
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

[**DescribeSnapshotsResponse**](DescribeSnapshotsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeSubnetGroups

> DescribeSubnetGroupsResponse describeSubnetGroups(xAmzTarget, describeSubnetGroupsRequest, opts)



Returns a list of subnet group descriptions. If a subnet group name is specified, the list contains only the description of that group.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeSubnetGroupsRequest = new AmazonMemoryDb.DescribeSubnetGroupsRequest(); // DescribeSubnetGroupsRequest | 
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
apiInstance.describeSubnetGroups(xAmzTarget, describeSubnetGroupsRequest, opts, (error, data, response) => {
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
 **describeSubnetGroupsRequest** | [**DescribeSubnetGroupsRequest**](DescribeSubnetGroupsRequest.md)|  | 
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

[**DescribeSubnetGroupsResponse**](DescribeSubnetGroupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeUsers

> DescribeUsersResponse describeUsers(xAmzTarget, describeUsersRequest, opts)



Returns a list of users.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeUsersRequest = new AmazonMemoryDb.DescribeUsersRequest(); // DescribeUsersRequest | 
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
apiInstance.describeUsers(xAmzTarget, describeUsersRequest, opts, (error, data, response) => {
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
 **describeUsersRequest** | [**DescribeUsersRequest**](DescribeUsersRequest.md)|  | 
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

[**DescribeUsersResponse**](DescribeUsersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## failoverShard

> FailoverShardResponse failoverShard(xAmzTarget, failoverShardRequest, opts)



Used to failover a shard. This API is designed for testing the behavior of your application in case of MemoryDB failover. It is not designed to be used as a production-level tool for initiating a failover to overcome a problem you may have with the cluster. Moreover, in certain conditions such as large scale operational events, Amazon may block this API. 

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let failoverShardRequest = new AmazonMemoryDb.FailoverShardRequest(); // FailoverShardRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.failoverShard(xAmzTarget, failoverShardRequest, opts, (error, data, response) => {
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
 **failoverShardRequest** | [**FailoverShardRequest**](FailoverShardRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**FailoverShardResponse**](FailoverShardResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAllowedNodeTypeUpdates

> ListAllowedNodeTypeUpdatesResponse listAllowedNodeTypeUpdates(xAmzTarget, listAllowedNodeTypeUpdatesRequest, opts)



Lists all available node types that you can scale to from your cluster&#39;s current node type. When you use the UpdateCluster operation to scale your cluster, the value of the NodeType parameter must be one of the node types returned by this operation.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listAllowedNodeTypeUpdatesRequest = new AmazonMemoryDb.ListAllowedNodeTypeUpdatesRequest(); // ListAllowedNodeTypeUpdatesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listAllowedNodeTypeUpdates(xAmzTarget, listAllowedNodeTypeUpdatesRequest, opts, (error, data, response) => {
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
 **listAllowedNodeTypeUpdatesRequest** | [**ListAllowedNodeTypeUpdatesRequest**](ListAllowedNodeTypeUpdatesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListAllowedNodeTypeUpdatesResponse**](ListAllowedNodeTypeUpdatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTags

> ListTagsResponse listTags(xAmzTarget, listTagsRequest, opts)



Lists all tags currently on a named resource. A tag is a key-value pair where the key and value are case-sensitive. You can use tags to categorize and track your MemoryDB resources. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html\&quot;&gt;Tagging your MemoryDB resources&lt;/a&gt; 

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTagsRequest = new AmazonMemoryDb.ListTagsRequest(); // ListTagsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTags(xAmzTarget, listTagsRequest, opts, (error, data, response) => {
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
 **listTagsRequest** | [**ListTagsRequest**](ListTagsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsResponse**](ListTagsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## purchaseReservedNodesOffering

> PurchaseReservedNodesOfferingResponse purchaseReservedNodesOffering(xAmzTarget, purchaseReservedNodesOfferingRequest, opts)



Allows you to purchase a reserved node offering. Reserved nodes are not eligible for cancellation and are non-refundable.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let purchaseReservedNodesOfferingRequest = new AmazonMemoryDb.PurchaseReservedNodesOfferingRequest(); // PurchaseReservedNodesOfferingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.purchaseReservedNodesOffering(xAmzTarget, purchaseReservedNodesOfferingRequest, opts, (error, data, response) => {
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
 **purchaseReservedNodesOfferingRequest** | [**PurchaseReservedNodesOfferingRequest**](PurchaseReservedNodesOfferingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PurchaseReservedNodesOfferingResponse**](PurchaseReservedNodesOfferingResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resetParameterGroup

> ResetParameterGroupResponse resetParameterGroup(xAmzTarget, resetParameterGroupRequest, opts)



Modifies the parameters of a parameter group to the engine or system default value. You can reset specific parameters by submitting a list of parameter names. To reset the entire parameter group, specify the AllParameters and ParameterGroupName parameters.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let resetParameterGroupRequest = new AmazonMemoryDb.ResetParameterGroupRequest(); // ResetParameterGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.resetParameterGroup(xAmzTarget, resetParameterGroupRequest, opts, (error, data, response) => {
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
 **resetParameterGroupRequest** | [**ResetParameterGroupRequest**](ResetParameterGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ResetParameterGroupResponse**](ResetParameterGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> TagResourceResponse tagResource(xAmzTarget, tagResourceRequest, opts)



&lt;p&gt;A tag is a key-value pair where the key and value are case-sensitive. You can use tags to categorize and track all your MemoryDB resources. When you add or remove tags on clusters, those actions will be replicated to all nodes in the cluster. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/MemoryDB/latest/devguide/iam.resourcelevelpermissions.html\&quot;&gt;Resource-level permissions&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For example, you can use cost-allocation tags to your MemoryDB resources, Amazon generates a cost allocation report as a comma-separated value (CSV) file with your usage and costs aggregated by your tags. You can apply tags that represent business categories (such as cost centers, application names, or owners) to organize your costs across multiple services. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/MemoryDB/latest/devguide/tagging.html\&quot;&gt;Using Cost Allocation Tags&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let tagResourceRequest = new AmazonMemoryDb.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(xAmzTarget, tagResourceRequest, opts, (error, data, response) => {
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
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**TagResourceResponse**](TagResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> UntagResourceResponse untagResource(xAmzTarget, untagResourceRequest, opts)



Use this operation to remove tags on a resource

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let untagResourceRequest = new AmazonMemoryDb.UntagResourceRequest(); // UntagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(xAmzTarget, untagResourceRequest, opts, (error, data, response) => {
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
 **untagResourceRequest** | [**UntagResourceRequest**](UntagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UntagResourceResponse**](UntagResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateACL

> UpdateACLResponse updateACL(xAmzTarget, updateACLRequest, opts)



Changes the list of users that belong to the Access Control List.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateACLRequest = new AmazonMemoryDb.UpdateACLRequest(); // UpdateACLRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateACL(xAmzTarget, updateACLRequest, opts, (error, data, response) => {
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
 **updateACLRequest** | [**UpdateACLRequest**](UpdateACLRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateACLResponse**](UpdateACLResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCluster

> UpdateClusterResponse updateCluster(xAmzTarget, updateClusterRequest, opts)



Modifies the settings for a cluster. You can use this operation to change one or more cluster configuration settings by specifying the settings and the new values.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateClusterRequest = new AmazonMemoryDb.UpdateClusterRequest(); // UpdateClusterRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateCluster(xAmzTarget, updateClusterRequest, opts, (error, data, response) => {
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
 **updateClusterRequest** | [**UpdateClusterRequest**](UpdateClusterRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateClusterResponse**](UpdateClusterResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateParameterGroup

> UpdateParameterGroupResponse updateParameterGroup(xAmzTarget, updateParameterGroupRequest, opts)



Updates the parameters of a parameter group. You can modify up to 20 parameters in a single request by submitting a list parameter name and value pairs.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateParameterGroupRequest = new AmazonMemoryDb.UpdateParameterGroupRequest(); // UpdateParameterGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateParameterGroup(xAmzTarget, updateParameterGroupRequest, opts, (error, data, response) => {
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
 **updateParameterGroupRequest** | [**UpdateParameterGroupRequest**](UpdateParameterGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateParameterGroupResponse**](UpdateParameterGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSubnetGroup

> UpdateSubnetGroupResponse updateSubnetGroup(xAmzTarget, updateSubnetGroupRequest, opts)



Updates a subnet group. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/MemoryDB/latest/devguide/ubnetGroups.Modifying.html\&quot;&gt;Updating a subnet group&lt;/a&gt; 

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateSubnetGroupRequest = new AmazonMemoryDb.UpdateSubnetGroupRequest(); // UpdateSubnetGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSubnetGroup(xAmzTarget, updateSubnetGroupRequest, opts, (error, data, response) => {
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
 **updateSubnetGroupRequest** | [**UpdateSubnetGroupRequest**](UpdateSubnetGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSubnetGroupResponse**](UpdateSubnetGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUser

> UpdateUserResponse updateUser(xAmzTarget, updateUserRequest, opts)



Changes user password(s) and/or access string.

### Example

```javascript
import AmazonMemoryDb from 'amazon_memory_db';
let defaultClient = AmazonMemoryDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMemoryDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateUserRequest = new AmazonMemoryDb.UpdateUserRequest(); // UpdateUserRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateUser(xAmzTarget, updateUserRequest, opts, (error, data, response) => {
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
 **updateUserRequest** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateUserResponse**](UpdateUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

