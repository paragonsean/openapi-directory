# AwsOpsWorksCm.DefaultApi

All URIs are relative to *http://opsworks-cm.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateNode**](DefaultApi.md#associateNode) | **POST** /#X-Amz-Target&#x3D;OpsWorksCM_V2016_11_01.AssociateNode | 
[**createBackup**](DefaultApi.md#createBackup) | **POST** /#X-Amz-Target&#x3D;OpsWorksCM_V2016_11_01.CreateBackup | 
[**createServer**](DefaultApi.md#createServer) | **POST** /#X-Amz-Target&#x3D;OpsWorksCM_V2016_11_01.CreateServer | 
[**deleteBackup**](DefaultApi.md#deleteBackup) | **POST** /#X-Amz-Target&#x3D;OpsWorksCM_V2016_11_01.DeleteBackup | 
[**deleteServer**](DefaultApi.md#deleteServer) | **POST** /#X-Amz-Target&#x3D;OpsWorksCM_V2016_11_01.DeleteServer | 
[**describeAccountAttributes**](DefaultApi.md#describeAccountAttributes) | **POST** /#X-Amz-Target&#x3D;OpsWorksCM_V2016_11_01.DescribeAccountAttributes | 
[**describeBackups**](DefaultApi.md#describeBackups) | **POST** /#X-Amz-Target&#x3D;OpsWorksCM_V2016_11_01.DescribeBackups | 
[**describeEvents**](DefaultApi.md#describeEvents) | **POST** /#X-Amz-Target&#x3D;OpsWorksCM_V2016_11_01.DescribeEvents | 
[**describeNodeAssociationStatus**](DefaultApi.md#describeNodeAssociationStatus) | **POST** /#X-Amz-Target&#x3D;OpsWorksCM_V2016_11_01.DescribeNodeAssociationStatus | 
[**describeServers**](DefaultApi.md#describeServers) | **POST** /#X-Amz-Target&#x3D;OpsWorksCM_V2016_11_01.DescribeServers | 
[**disassociateNode**](DefaultApi.md#disassociateNode) | **POST** /#X-Amz-Target&#x3D;OpsWorksCM_V2016_11_01.DisassociateNode | 
[**exportServerEngineAttribute**](DefaultApi.md#exportServerEngineAttribute) | **POST** /#X-Amz-Target&#x3D;OpsWorksCM_V2016_11_01.ExportServerEngineAttribute | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;OpsWorksCM_V2016_11_01.ListTagsForResource | 
[**restoreServer**](DefaultApi.md#restoreServer) | **POST** /#X-Amz-Target&#x3D;OpsWorksCM_V2016_11_01.RestoreServer | 
[**startMaintenance**](DefaultApi.md#startMaintenance) | **POST** /#X-Amz-Target&#x3D;OpsWorksCM_V2016_11_01.StartMaintenance | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;OpsWorksCM_V2016_11_01.TagResource | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;OpsWorksCM_V2016_11_01.UntagResource | 
[**updateServer**](DefaultApi.md#updateServer) | **POST** /#X-Amz-Target&#x3D;OpsWorksCM_V2016_11_01.UpdateServer | 
[**updateServerEngineAttributes**](DefaultApi.md#updateServerEngineAttributes) | **POST** /#X-Amz-Target&#x3D;OpsWorksCM_V2016_11_01.UpdateServerEngineAttributes | 



## associateNode

> AssociateNodeResponse associateNode(xAmzTarget, associateNodeRequest, opts)



&lt;p&gt; Associates a new node with the server. For more information about how to disassociate a node, see &lt;a&gt;DisassociateNode&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; On a Chef server: This command is an alternative to &lt;code&gt;knife bootstrap&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; Example (Chef): &lt;code&gt;aws opsworks-cm associate-node --server-name &lt;i&gt;MyServer&lt;/i&gt; --node-name &lt;i&gt;MyManagedNode&lt;/i&gt; --engine-attributes \&quot;Name&#x3D;&lt;i&gt;CHEF_ORGANIZATION&lt;/i&gt;,Value&#x3D;default\&quot; \&quot;Name&#x3D;&lt;i&gt;CHEF_NODE_PUBLIC_KEY&lt;/i&gt;,Value&#x3D;&lt;i&gt;public-key-pem&lt;/i&gt;\&quot;&lt;/code&gt; &lt;/p&gt; &lt;p&gt; On a Puppet server, this command is an alternative to the &lt;code&gt;puppet cert sign&lt;/code&gt; command that signs a Puppet node CSR. &lt;/p&gt; &lt;p&gt; Example (Puppet): &lt;code&gt;aws opsworks-cm associate-node --server-name &lt;i&gt;MyServer&lt;/i&gt; --node-name &lt;i&gt;MyManagedNode&lt;/i&gt; --engine-attributes \&quot;Name&#x3D;&lt;i&gt;PUPPET_NODE_CSR&lt;/i&gt;,Value&#x3D;&lt;i&gt;csr-pem&lt;/i&gt;\&quot;&lt;/code&gt; &lt;/p&gt; &lt;p&gt; A node can can only be associated with servers that are in a &lt;code&gt;HEALTHY&lt;/code&gt; state. Otherwise, an &lt;code&gt;InvalidStateException&lt;/code&gt; is thrown. A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the server does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. The AssociateNode API call can be integrated into Auto Scaling configurations, AWS Cloudformation templates, or the user data of a server&#39;s instance. &lt;/p&gt;

### Example

```javascript
import AwsOpsWorksCm from 'aws_ops_works_cm';
let defaultClient = AwsOpsWorksCm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsOpsWorksCm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let associateNodeRequest = new AwsOpsWorksCm.AssociateNodeRequest(); // AssociateNodeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateNode(xAmzTarget, associateNodeRequest, opts, (error, data, response) => {
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
 **associateNodeRequest** | [**AssociateNodeRequest**](AssociateNodeRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AssociateNodeResponse**](AssociateNodeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBackup

> CreateBackupResponse createBackup(xAmzTarget, createBackupRequest, opts)



&lt;p&gt; Creates an application-level backup of a server. While the server is in the &lt;code&gt;BACKING_UP&lt;/code&gt; state, the server cannot be changed, and no additional backup can be created. &lt;/p&gt; &lt;p&gt; Backups can be created for servers in &lt;code&gt;RUNNING&lt;/code&gt;, &lt;code&gt;HEALTHY&lt;/code&gt;, and &lt;code&gt;UNHEALTHY&lt;/code&gt; states. By default, you can create a maximum of 50 manual backups. &lt;/p&gt; &lt;p&gt; This operation is asynchronous. &lt;/p&gt; &lt;p&gt; A &lt;code&gt;LimitExceededException&lt;/code&gt; is thrown when the maximum number of manual backups is reached. An &lt;code&gt;InvalidStateException&lt;/code&gt; is thrown when the server is not in any of the following states: RUNNING, HEALTHY, or UNHEALTHY. A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the server is not found. A &lt;code&gt;ValidationException&lt;/code&gt; is thrown when parameters of the request are not valid. &lt;/p&gt;

### Example

```javascript
import AwsOpsWorksCm from 'aws_ops_works_cm';
let defaultClient = AwsOpsWorksCm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsOpsWorksCm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createBackupRequest = new AwsOpsWorksCm.CreateBackupRequest(); // CreateBackupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBackup(xAmzTarget, createBackupRequest, opts, (error, data, response) => {
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
 **createBackupRequest** | [**CreateBackupRequest**](CreateBackupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateBackupResponse**](CreateBackupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createServer

> CreateServerResponse createServer(xAmzTarget, createServerRequest, opts)



&lt;p&gt; Creates and immedately starts a new server. The server is ready to use when it is in the &lt;code&gt;HEALTHY&lt;/code&gt; state. By default, you can create a maximum of 10 servers. &lt;/p&gt; &lt;p&gt; This operation is asynchronous. &lt;/p&gt; &lt;p&gt; A &lt;code&gt;LimitExceededException&lt;/code&gt; is thrown when you have created the maximum number of servers (10). A &lt;code&gt;ResourceAlreadyExistsException&lt;/code&gt; is thrown when a server with the same name already exists in the account. A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when you specify a backup ID that is not valid or is for a backup that does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is thrown when parameters of the request are not valid. &lt;/p&gt; &lt;p&gt; If you do not specify a security group by adding the &lt;code&gt;SecurityGroupIds&lt;/code&gt; parameter, AWS OpsWorks creates a new security group. &lt;/p&gt; &lt;p&gt; &lt;i&gt;Chef Automate:&lt;/i&gt; The default security group opens the Chef server to the world on TCP port 443. If a KeyName is present, AWS OpsWorks enables SSH access. SSH is also open to the world on TCP port 22. &lt;/p&gt; &lt;p&gt; &lt;i&gt;Puppet Enterprise:&lt;/i&gt; The default security group opens TCP ports 22, 443, 4433, 8140, 8142, 8143, and 8170. If a KeyName is present, AWS OpsWorks enables SSH access. SSH is also open to the world on TCP port 22. &lt;/p&gt; &lt;p&gt;By default, your server is accessible from any IP address. We recommend that you update your security group rules to allow access from known IP addresses and address ranges only. To edit security group rules, open Security Groups in the navigation pane of the EC2 management console. &lt;/p&gt; &lt;p&gt;To specify your own domain for a server, and provide your own self-signed or CA-signed certificate and private key, specify values for &lt;code&gt;CustomDomain&lt;/code&gt;, &lt;code&gt;CustomCertificate&lt;/code&gt;, and &lt;code&gt;CustomPrivateKey&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AwsOpsWorksCm from 'aws_ops_works_cm';
let defaultClient = AwsOpsWorksCm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsOpsWorksCm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createServerRequest = new AwsOpsWorksCm.CreateServerRequest(); // CreateServerRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createServer(xAmzTarget, createServerRequest, opts, (error, data, response) => {
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
 **createServerRequest** | [**CreateServerRequest**](CreateServerRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateServerResponse**](CreateServerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteBackup

> Object deleteBackup(xAmzTarget, deleteBackupRequest, opts)



&lt;p&gt; Deletes a backup. You can delete both manual and automated backups. This operation is asynchronous. &lt;/p&gt; &lt;p&gt; An &lt;code&gt;InvalidStateException&lt;/code&gt; is thrown when a backup deletion is already in progress. A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the backup does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is thrown when parameters of the request are not valid. &lt;/p&gt;

### Example

```javascript
import AwsOpsWorksCm from 'aws_ops_works_cm';
let defaultClient = AwsOpsWorksCm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsOpsWorksCm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteBackupRequest = new AwsOpsWorksCm.DeleteBackupRequest(); // DeleteBackupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBackup(xAmzTarget, deleteBackupRequest, opts, (error, data, response) => {
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
 **deleteBackupRequest** | [**DeleteBackupRequest**](DeleteBackupRequest.md)|  | 
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


## deleteServer

> Object deleteServer(xAmzTarget, deleteServerRequest, opts)



&lt;p&gt; Deletes the server and the underlying AWS CloudFormation stacks (including the server&#39;s EC2 instance). When you run this command, the server state is updated to &lt;code&gt;DELETING&lt;/code&gt;. After the server is deleted, it is no longer returned by &lt;code&gt;DescribeServer&lt;/code&gt; requests. If the AWS CloudFormation stack cannot be deleted, the server cannot be deleted. &lt;/p&gt; &lt;p&gt; This operation is asynchronous. &lt;/p&gt; &lt;p&gt; An &lt;code&gt;InvalidStateException&lt;/code&gt; is thrown when a server deletion is already in progress. A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the server does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. &lt;/p&gt; &lt;p&gt; &lt;/p&gt;

### Example

```javascript
import AwsOpsWorksCm from 'aws_ops_works_cm';
let defaultClient = AwsOpsWorksCm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsOpsWorksCm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteServerRequest = new AwsOpsWorksCm.DeleteServerRequest(); // DeleteServerRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteServer(xAmzTarget, deleteServerRequest, opts, (error, data, response) => {
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
 **deleteServerRequest** | [**DeleteServerRequest**](DeleteServerRequest.md)|  | 
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


## describeAccountAttributes

> DescribeAccountAttributesResponse describeAccountAttributes(xAmzTarget, body, opts)



&lt;p&gt; Describes your OpsWorks-CM account attributes. &lt;/p&gt; &lt;p&gt; This operation is synchronous. &lt;/p&gt;

### Example

```javascript
import AwsOpsWorksCm from 'aws_ops_works_cm';
let defaultClient = AwsOpsWorksCm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsOpsWorksCm.DefaultApi();
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
apiInstance.describeAccountAttributes(xAmzTarget, body, opts, (error, data, response) => {
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

[**DescribeAccountAttributesResponse**](DescribeAccountAttributesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeBackups

> DescribeBackupsResponse describeBackups(xAmzTarget, describeBackupsRequest, opts)



&lt;p&gt; Describes backups. The results are ordered by time, with newest backups first. If you do not specify a BackupId or ServerName, the command returns all backups. &lt;/p&gt; &lt;p&gt; This operation is synchronous. &lt;/p&gt; &lt;p&gt; A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the backup does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. &lt;/p&gt;

### Example

```javascript
import AwsOpsWorksCm from 'aws_ops_works_cm';
let defaultClient = AwsOpsWorksCm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsOpsWorksCm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeBackupsRequest = new AwsOpsWorksCm.DescribeBackupsRequest(); // DescribeBackupsRequest | 
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
apiInstance.describeBackups(xAmzTarget, describeBackupsRequest, opts, (error, data, response) => {
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
 **describeBackupsRequest** | [**DescribeBackupsRequest**](DescribeBackupsRequest.md)|  | 
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

[**DescribeBackupsResponse**](DescribeBackupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeEvents

> DescribeEventsResponse describeEvents(xAmzTarget, describeEventsRequest, opts)



&lt;p&gt; Describes events for a specified server. Results are ordered by time, with newest events first. &lt;/p&gt; &lt;p&gt; This operation is synchronous. &lt;/p&gt; &lt;p&gt; A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the server does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. &lt;/p&gt;

### Example

```javascript
import AwsOpsWorksCm from 'aws_ops_works_cm';
let defaultClient = AwsOpsWorksCm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsOpsWorksCm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeEventsRequest = new AwsOpsWorksCm.DescribeEventsRequest(); // DescribeEventsRequest | 
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


## describeNodeAssociationStatus

> DescribeNodeAssociationStatusResponse describeNodeAssociationStatus(xAmzTarget, describeNodeAssociationStatusRequest, opts)



&lt;p&gt; Returns the current status of an existing association or disassociation request. &lt;/p&gt; &lt;p&gt; A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when no recent association or disassociation request with the specified token is found, or when the server does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. &lt;/p&gt;

### Example

```javascript
import AwsOpsWorksCm from 'aws_ops_works_cm';
let defaultClient = AwsOpsWorksCm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsOpsWorksCm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeNodeAssociationStatusRequest = new AwsOpsWorksCm.DescribeNodeAssociationStatusRequest(); // DescribeNodeAssociationStatusRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeNodeAssociationStatus(xAmzTarget, describeNodeAssociationStatusRequest, opts, (error, data, response) => {
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
 **describeNodeAssociationStatusRequest** | [**DescribeNodeAssociationStatusRequest**](DescribeNodeAssociationStatusRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeNodeAssociationStatusResponse**](DescribeNodeAssociationStatusResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeServers

> DescribeServersResponse describeServers(xAmzTarget, describeServersRequest, opts)



&lt;p&gt; Lists all configuration management servers that are identified with your account. Only the stored results from Amazon DynamoDB are returned. AWS OpsWorks CM does not query other services. &lt;/p&gt; &lt;p&gt; This operation is synchronous. &lt;/p&gt; &lt;p&gt; A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the server does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. &lt;/p&gt;

### Example

```javascript
import AwsOpsWorksCm from 'aws_ops_works_cm';
let defaultClient = AwsOpsWorksCm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsOpsWorksCm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeServersRequest = new AwsOpsWorksCm.DescribeServersRequest(); // DescribeServersRequest | 
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
apiInstance.describeServers(xAmzTarget, describeServersRequest, opts, (error, data, response) => {
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
 **describeServersRequest** | [**DescribeServersRequest**](DescribeServersRequest.md)|  | 
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

[**DescribeServersResponse**](DescribeServersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disassociateNode

> DisassociateNodeResponse disassociateNode(xAmzTarget, disassociateNodeRequest, opts)



&lt;p&gt; Disassociates a node from an AWS OpsWorks CM server, and removes the node from the server&#39;s managed nodes. After a node is disassociated, the node key pair is no longer valid for accessing the configuration manager&#39;s API. For more information about how to associate a node, see &lt;a&gt;AssociateNode&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;A node can can only be disassociated from a server that is in a &lt;code&gt;HEALTHY&lt;/code&gt; state. Otherwise, an &lt;code&gt;InvalidStateException&lt;/code&gt; is thrown. A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the server does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. &lt;/p&gt;

### Example

```javascript
import AwsOpsWorksCm from 'aws_ops_works_cm';
let defaultClient = AwsOpsWorksCm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsOpsWorksCm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let disassociateNodeRequest = new AwsOpsWorksCm.DisassociateNodeRequest(); // DisassociateNodeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateNode(xAmzTarget, disassociateNodeRequest, opts, (error, data, response) => {
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
 **disassociateNodeRequest** | [**DisassociateNodeRequest**](DisassociateNodeRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DisassociateNodeResponse**](DisassociateNodeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## exportServerEngineAttribute

> ExportServerEngineAttributeResponse exportServerEngineAttribute(xAmzTarget, exportServerEngineAttributeRequest, opts)



&lt;p&gt; Exports a specified server engine attribute as a base64-encoded string. For example, you can export user data that you can use in EC2 to associate nodes with a server. &lt;/p&gt; &lt;p&gt; This operation is synchronous. &lt;/p&gt; &lt;p&gt; A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the server does not exist. An &lt;code&gt;InvalidStateException&lt;/code&gt; is thrown when the server is in any of the following states: CREATING, TERMINATED, FAILED or DELETING. &lt;/p&gt;

### Example

```javascript
import AwsOpsWorksCm from 'aws_ops_works_cm';
let defaultClient = AwsOpsWorksCm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsOpsWorksCm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let exportServerEngineAttributeRequest = new AwsOpsWorksCm.ExportServerEngineAttributeRequest(); // ExportServerEngineAttributeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.exportServerEngineAttribute(xAmzTarget, exportServerEngineAttributeRequest, opts, (error, data, response) => {
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
 **exportServerEngineAttributeRequest** | [**ExportServerEngineAttributeRequest**](ExportServerEngineAttributeRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ExportServerEngineAttributeResponse**](ExportServerEngineAttributeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(xAmzTarget, listTagsForResourceRequest, opts)



Returns a list of tags that are applied to the specified AWS OpsWorks for Chef Automate or AWS OpsWorks for Puppet Enterprise servers or backups.

### Example

```javascript
import AwsOpsWorksCm from 'aws_ops_works_cm';
let defaultClient = AwsOpsWorksCm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsOpsWorksCm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTagsForResourceRequest = new AwsOpsWorksCm.ListTagsForResourceRequest(); // ListTagsForResourceRequest | 
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
apiInstance.listTagsForResource(xAmzTarget, listTagsForResourceRequest, opts, (error, data, response) => {
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
 **listTagsForResourceRequest** | [**ListTagsForResourceRequest**](ListTagsForResourceRequest.md)|  | 
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

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## restoreServer

> RestoreServerResponse restoreServer(xAmzTarget, restoreServerRequest, opts)



&lt;p&gt; Restores a backup to a server that is in a &lt;code&gt;CONNECTION_LOST&lt;/code&gt;, &lt;code&gt;HEALTHY&lt;/code&gt;, &lt;code&gt;RUNNING&lt;/code&gt;, &lt;code&gt;UNHEALTHY&lt;/code&gt;, or &lt;code&gt;TERMINATED&lt;/code&gt; state. When you run RestoreServer, the server&#39;s EC2 instance is deleted, and a new EC2 instance is configured. RestoreServer maintains the existing server endpoint, so configuration management of the server&#39;s client devices (nodes) should continue to work. &lt;/p&gt; &lt;p&gt;Restoring from a backup is performed by creating a new EC2 instance. If restoration is successful, and the server is in a &lt;code&gt;HEALTHY&lt;/code&gt; state, AWS OpsWorks CM switches traffic over to the new instance. After restoration is finished, the old EC2 instance is maintained in a &lt;code&gt;Running&lt;/code&gt; or &lt;code&gt;Stopped&lt;/code&gt; state, but is eventually terminated.&lt;/p&gt; &lt;p&gt; This operation is asynchronous. &lt;/p&gt; &lt;p&gt; An &lt;code&gt;InvalidStateException&lt;/code&gt; is thrown when the server is not in a valid state. A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the server does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. &lt;/p&gt;

### Example

```javascript
import AwsOpsWorksCm from 'aws_ops_works_cm';
let defaultClient = AwsOpsWorksCm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsOpsWorksCm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let restoreServerRequest = new AwsOpsWorksCm.RestoreServerRequest(); // RestoreServerRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.restoreServer(xAmzTarget, restoreServerRequest, opts, (error, data, response) => {
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
 **restoreServerRequest** | [**RestoreServerRequest**](RestoreServerRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RestoreServerResponse**](RestoreServerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startMaintenance

> StartMaintenanceResponse startMaintenance(xAmzTarget, startMaintenanceRequest, opts)



&lt;p&gt; Manually starts server maintenance. This command can be useful if an earlier maintenance attempt failed, and the underlying cause of maintenance failure has been resolved. The server is in an &lt;code&gt;UNDER_MAINTENANCE&lt;/code&gt; state while maintenance is in progress. &lt;/p&gt; &lt;p&gt; Maintenance can only be started on servers in &lt;code&gt;HEALTHY&lt;/code&gt; and &lt;code&gt;UNHEALTHY&lt;/code&gt; states. Otherwise, an &lt;code&gt;InvalidStateException&lt;/code&gt; is thrown. A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the server does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. &lt;/p&gt;

### Example

```javascript
import AwsOpsWorksCm from 'aws_ops_works_cm';
let defaultClient = AwsOpsWorksCm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsOpsWorksCm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startMaintenanceRequest = new AwsOpsWorksCm.StartMaintenanceRequest(); // StartMaintenanceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startMaintenance(xAmzTarget, startMaintenanceRequest, opts, (error, data, response) => {
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
 **startMaintenanceRequest** | [**StartMaintenanceRequest**](StartMaintenanceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartMaintenanceResponse**](StartMaintenanceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(xAmzTarget, tagResourceRequest, opts)



Applies tags to an AWS OpsWorks for Chef Automate or AWS OpsWorks for Puppet Enterprise server, or to server backups.

### Example

```javascript
import AwsOpsWorksCm from 'aws_ops_works_cm';
let defaultClient = AwsOpsWorksCm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsOpsWorksCm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let tagResourceRequest = new AwsOpsWorksCm.TagResourceRequest(); // TagResourceRequest | 
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

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> Object untagResource(xAmzTarget, untagResourceRequest, opts)



Removes specified tags from an AWS OpsWorks-CM server or backup.

### Example

```javascript
import AwsOpsWorksCm from 'aws_ops_works_cm';
let defaultClient = AwsOpsWorksCm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsOpsWorksCm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let untagResourceRequest = new AwsOpsWorksCm.UntagResourceRequest(); // UntagResourceRequest | 
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

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateServer

> UpdateServerResponse updateServer(xAmzTarget, updateServerRequest, opts)



&lt;p&gt; Updates settings for a server. &lt;/p&gt; &lt;p&gt; This operation is synchronous. &lt;/p&gt;

### Example

```javascript
import AwsOpsWorksCm from 'aws_ops_works_cm';
let defaultClient = AwsOpsWorksCm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsOpsWorksCm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateServerRequest = new AwsOpsWorksCm.UpdateServerRequest(); // UpdateServerRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateServer(xAmzTarget, updateServerRequest, opts, (error, data, response) => {
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
 **updateServerRequest** | [**UpdateServerRequest**](UpdateServerRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateServerResponse**](UpdateServerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateServerEngineAttributes

> UpdateServerEngineAttributesResponse updateServerEngineAttributes(xAmzTarget, updateServerEngineAttributesRequest, opts)



&lt;p&gt; Updates engine-specific attributes on a specified server. The server enters the &lt;code&gt;MODIFYING&lt;/code&gt; state when this operation is in progress. Only one update can occur at a time. You can use this command to reset a Chef server&#39;s public key (&lt;code&gt;CHEF_PIVOTAL_KEY&lt;/code&gt;) or a Puppet server&#39;s admin password (&lt;code&gt;PUPPET_ADMIN_PASSWORD&lt;/code&gt;). &lt;/p&gt; &lt;p&gt; This operation is asynchronous. &lt;/p&gt; &lt;p&gt; This operation can only be called for servers in &lt;code&gt;HEALTHY&lt;/code&gt; or &lt;code&gt;UNHEALTHY&lt;/code&gt; states. Otherwise, an &lt;code&gt;InvalidStateException&lt;/code&gt; is raised. A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the server does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. &lt;/p&gt;

### Example

```javascript
import AwsOpsWorksCm from 'aws_ops_works_cm';
let defaultClient = AwsOpsWorksCm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsOpsWorksCm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateServerEngineAttributesRequest = new AwsOpsWorksCm.UpdateServerEngineAttributesRequest(); // UpdateServerEngineAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateServerEngineAttributes(xAmzTarget, updateServerEngineAttributesRequest, opts, (error, data, response) => {
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
 **updateServerEngineAttributesRequest** | [**UpdateServerEngineAttributesRequest**](UpdateServerEngineAttributesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateServerEngineAttributesResponse**](UpdateServerEngineAttributesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

