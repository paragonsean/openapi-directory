# AmazonOpenSearchService.DefaultApi

All URIs are relative to *http://es.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acceptInboundConnection**](DefaultApi.md#acceptInboundConnection) | **PUT** /2021-01-01/opensearch/cc/inboundConnection/{ConnectionId}/accept | 
[**addTags**](DefaultApi.md#addTags) | **POST** /2021-01-01/tags | 
[**associatePackage**](DefaultApi.md#associatePackage) | **POST** /2021-01-01/packages/associate/{PackageID}/{DomainName} | 
[**authorizeVpcEndpointAccess**](DefaultApi.md#authorizeVpcEndpointAccess) | **POST** /2021-01-01/opensearch/domain/{DomainName}/authorizeVpcEndpointAccess | 
[**cancelServiceSoftwareUpdate**](DefaultApi.md#cancelServiceSoftwareUpdate) | **POST** /2021-01-01/opensearch/serviceSoftwareUpdate/cancel | 
[**createDomain**](DefaultApi.md#createDomain) | **POST** /2021-01-01/opensearch/domain | 
[**createOutboundConnection**](DefaultApi.md#createOutboundConnection) | **POST** /2021-01-01/opensearch/cc/outboundConnection | 
[**createPackage**](DefaultApi.md#createPackage) | **POST** /2021-01-01/packages | 
[**createVpcEndpoint**](DefaultApi.md#createVpcEndpoint) | **POST** /2021-01-01/opensearch/vpcEndpoints | 
[**deleteDomain**](DefaultApi.md#deleteDomain) | **DELETE** /2021-01-01/opensearch/domain/{DomainName} | 
[**deleteInboundConnection**](DefaultApi.md#deleteInboundConnection) | **DELETE** /2021-01-01/opensearch/cc/inboundConnection/{ConnectionId} | 
[**deleteOutboundConnection**](DefaultApi.md#deleteOutboundConnection) | **DELETE** /2021-01-01/opensearch/cc/outboundConnection/{ConnectionId} | 
[**deletePackage**](DefaultApi.md#deletePackage) | **DELETE** /2021-01-01/packages/{PackageID} | 
[**deleteVpcEndpoint**](DefaultApi.md#deleteVpcEndpoint) | **DELETE** /2021-01-01/opensearch/vpcEndpoints/{VpcEndpointId} | 
[**describeDomain**](DefaultApi.md#describeDomain) | **GET** /2021-01-01/opensearch/domain/{DomainName} | 
[**describeDomainAutoTunes**](DefaultApi.md#describeDomainAutoTunes) | **GET** /2021-01-01/opensearch/domain/{DomainName}/autoTunes | 
[**describeDomainChangeProgress**](DefaultApi.md#describeDomainChangeProgress) | **GET** /2021-01-01/opensearch/domain/{DomainName}/progress | 
[**describeDomainConfig**](DefaultApi.md#describeDomainConfig) | **GET** /2021-01-01/opensearch/domain/{DomainName}/config | 
[**describeDomainHealth**](DefaultApi.md#describeDomainHealth) | **GET** /2021-01-01/opensearch/domain/{DomainName}/health | 
[**describeDomainNodes**](DefaultApi.md#describeDomainNodes) | **GET** /2021-01-01/opensearch/domain/{DomainName}/nodes | 
[**describeDomains**](DefaultApi.md#describeDomains) | **POST** /2021-01-01/opensearch/domain-info | 
[**describeDryRunProgress**](DefaultApi.md#describeDryRunProgress) | **GET** /2021-01-01/opensearch/domain/{DomainName}/dryRun | 
[**describeInboundConnections**](DefaultApi.md#describeInboundConnections) | **POST** /2021-01-01/opensearch/cc/inboundConnection/search | 
[**describeInstanceTypeLimits**](DefaultApi.md#describeInstanceTypeLimits) | **GET** /2021-01-01/opensearch/instanceTypeLimits/{EngineVersion}/{InstanceType} | 
[**describeOutboundConnections**](DefaultApi.md#describeOutboundConnections) | **POST** /2021-01-01/opensearch/cc/outboundConnection/search | 
[**describePackages**](DefaultApi.md#describePackages) | **POST** /2021-01-01/packages/describe | 
[**describeReservedInstanceOfferings**](DefaultApi.md#describeReservedInstanceOfferings) | **GET** /2021-01-01/opensearch/reservedInstanceOfferings | 
[**describeReservedInstances**](DefaultApi.md#describeReservedInstances) | **GET** /2021-01-01/opensearch/reservedInstances | 
[**describeVpcEndpoints**](DefaultApi.md#describeVpcEndpoints) | **POST** /2021-01-01/opensearch/vpcEndpoints/describe | 
[**dissociatePackage**](DefaultApi.md#dissociatePackage) | **POST** /2021-01-01/packages/dissociate/{PackageID}/{DomainName} | 
[**getCompatibleVersions**](DefaultApi.md#getCompatibleVersions) | **GET** /2021-01-01/opensearch/compatibleVersions | 
[**getPackageVersionHistory**](DefaultApi.md#getPackageVersionHistory) | **GET** /2021-01-01/packages/{PackageID}/history | 
[**getUpgradeHistory**](DefaultApi.md#getUpgradeHistory) | **GET** /2021-01-01/opensearch/upgradeDomain/{DomainName}/history | 
[**getUpgradeStatus**](DefaultApi.md#getUpgradeStatus) | **GET** /2021-01-01/opensearch/upgradeDomain/{DomainName}/status | 
[**listDomainNames**](DefaultApi.md#listDomainNames) | **GET** /2021-01-01/domain | 
[**listDomainsForPackage**](DefaultApi.md#listDomainsForPackage) | **GET** /2021-01-01/packages/{PackageID}/domains | 
[**listInstanceTypeDetails**](DefaultApi.md#listInstanceTypeDetails) | **GET** /2021-01-01/opensearch/instanceTypeDetails/{EngineVersion} | 
[**listPackagesForDomain**](DefaultApi.md#listPackagesForDomain) | **GET** /2021-01-01/domain/{DomainName}/packages | 
[**listScheduledActions**](DefaultApi.md#listScheduledActions) | **GET** /2021-01-01/opensearch/domain/{DomainName}/scheduledActions | 
[**listTags**](DefaultApi.md#listTags) | **GET** /2021-01-01/tags/#arn | 
[**listVersions**](DefaultApi.md#listVersions) | **GET** /2021-01-01/opensearch/versions | 
[**listVpcEndpointAccess**](DefaultApi.md#listVpcEndpointAccess) | **GET** /2021-01-01/opensearch/domain/{DomainName}/listVpcEndpointAccess | 
[**listVpcEndpoints**](DefaultApi.md#listVpcEndpoints) | **GET** /2021-01-01/opensearch/vpcEndpoints | 
[**listVpcEndpointsForDomain**](DefaultApi.md#listVpcEndpointsForDomain) | **GET** /2021-01-01/opensearch/domain/{DomainName}/vpcEndpoints | 
[**purchaseReservedInstanceOffering**](DefaultApi.md#purchaseReservedInstanceOffering) | **POST** /2021-01-01/opensearch/purchaseReservedInstanceOffering | 
[**rejectInboundConnection**](DefaultApi.md#rejectInboundConnection) | **PUT** /2021-01-01/opensearch/cc/inboundConnection/{ConnectionId}/reject | 
[**removeTags**](DefaultApi.md#removeTags) | **POST** /2021-01-01/tags-removal | 
[**revokeVpcEndpointAccess**](DefaultApi.md#revokeVpcEndpointAccess) | **POST** /2021-01-01/opensearch/domain/{DomainName}/revokeVpcEndpointAccess | 
[**startServiceSoftwareUpdate**](DefaultApi.md#startServiceSoftwareUpdate) | **POST** /2021-01-01/opensearch/serviceSoftwareUpdate/start | 
[**updateDomainConfig**](DefaultApi.md#updateDomainConfig) | **POST** /2021-01-01/opensearch/domain/{DomainName}/config | 
[**updatePackage**](DefaultApi.md#updatePackage) | **POST** /2021-01-01/packages/update | 
[**updateScheduledAction**](DefaultApi.md#updateScheduledAction) | **PUT** /2021-01-01/opensearch/domain/{DomainName}/scheduledAction/update | 
[**updateVpcEndpoint**](DefaultApi.md#updateVpcEndpoint) | **POST** /2021-01-01/opensearch/vpcEndpoints/update | 
[**upgradeDomain**](DefaultApi.md#upgradeDomain) | **POST** /2021-01-01/opensearch/upgradeDomain | 



## acceptInboundConnection

> AcceptInboundConnectionResponse acceptInboundConnection(connectionId, opts)



Allows the destination Amazon OpenSearch Service domain owner to accept an inbound cross-cluster search connection request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html\&quot;&gt;Cross-cluster search for Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let connectionId = "connectionId_example"; // String | The ID of the inbound connection to accept.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.acceptInboundConnection(connectionId, opts, (error, data, response) => {
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
 **connectionId** | **String**| The ID of the inbound connection to accept. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AcceptInboundConnectionResponse**](AcceptInboundConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addTags

> addTags(addTagsRequest, opts)



Attaches tags to an existing Amazon OpenSearch Service domain. Tags are a set of case-sensitive key-value pairs. A domain can have up to 10 tags. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-awsresourcetagging.html\&quot;&gt;Tagging Amazon OpenSearch Service domains&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let addTagsRequest = new AmazonOpenSearchService.AddTagsRequest(); // AddTagsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.addTags(addTagsRequest, opts, (error, data, response) => {
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
 **addTagsRequest** | [**AddTagsRequest**](AddTagsRequest.md)|  | 
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


## associatePackage

> AssociatePackageResponse associatePackage(packageID, domainName, opts)



Associates a package with an Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\&quot;&gt;Custom packages for Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let packageID = "packageID_example"; // String | Internal ID of the package to associate with a domain. Use <code>DescribePackages</code> to find this value. 
let domainName = "domainName_example"; // String | Name of the domain to associate the package with.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associatePackage(packageID, domainName, opts, (error, data, response) => {
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
 **packageID** | **String**| Internal ID of the package to associate with a domain. Use &lt;code&gt;DescribePackages&lt;/code&gt; to find this value.  | 
 **domainName** | **String**| Name of the domain to associate the package with. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AssociatePackageResponse**](AssociatePackageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## authorizeVpcEndpointAccess

> AuthorizeVpcEndpointAccessResponse authorizeVpcEndpointAccess(domainName, authorizeVpcEndpointAccessRequest, opts)



Provides access to an Amazon OpenSearch Service domain through the use of an interface VPC endpoint.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the OpenSearch Service domain to provide access to.
let authorizeVpcEndpointAccessRequest = new AmazonOpenSearchService.AuthorizeVpcEndpointAccessRequest(); // AuthorizeVpcEndpointAccessRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.authorizeVpcEndpointAccess(domainName, authorizeVpcEndpointAccessRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The name of the OpenSearch Service domain to provide access to. | 
 **authorizeVpcEndpointAccessRequest** | [**AuthorizeVpcEndpointAccessRequest**](AuthorizeVpcEndpointAccessRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AuthorizeVpcEndpointAccessResponse**](AuthorizeVpcEndpointAccessResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cancelServiceSoftwareUpdate

> CancelServiceSoftwareUpdateResponse cancelServiceSoftwareUpdate(cancelServiceSoftwareUpdateRequest, opts)



Cancels a scheduled service software update for an Amazon OpenSearch Service domain. You can only perform this operation before the &lt;code&gt;AutomatedUpdateDate&lt;/code&gt; and when the domain&#39;s &lt;code&gt;UpdateStatus&lt;/code&gt; is &lt;code&gt;PENDING_UPDATE&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html\&quot;&gt;Service software updates in Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let cancelServiceSoftwareUpdateRequest = new AmazonOpenSearchService.CancelServiceSoftwareUpdateRequest(); // CancelServiceSoftwareUpdateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.cancelServiceSoftwareUpdate(cancelServiceSoftwareUpdateRequest, opts, (error, data, response) => {
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
 **cancelServiceSoftwareUpdateRequest** | [**CancelServiceSoftwareUpdateRequest**](CancelServiceSoftwareUpdateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CancelServiceSoftwareUpdateResponse**](CancelServiceSoftwareUpdateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDomain

> CreateDomainResponse createDomain(createDomainRequest, opts)



Creates an Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html\&quot;&gt;Creating and managing Amazon OpenSearch Service domains&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let createDomainRequest = new AmazonOpenSearchService.CreateDomainRequest(); // CreateDomainRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDomain(createDomainRequest, opts, (error, data, response) => {
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
 **createDomainRequest** | [**CreateDomainRequest**](CreateDomainRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateDomainResponse**](CreateDomainResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOutboundConnection

> CreateOutboundConnectionResponse createOutboundConnection(createOutboundConnectionRequest, opts)



Creates a new cross-cluster search connection from a source Amazon OpenSearch Service domain to a destination domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html\&quot;&gt;Cross-cluster search for Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let createOutboundConnectionRequest = new AmazonOpenSearchService.CreateOutboundConnectionRequest(); // CreateOutboundConnectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createOutboundConnection(createOutboundConnectionRequest, opts, (error, data, response) => {
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
 **createOutboundConnectionRequest** | [**CreateOutboundConnectionRequest**](CreateOutboundConnectionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateOutboundConnectionResponse**](CreateOutboundConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPackage

> CreatePackageResponse createPackage(createPackageRequest, opts)



Creates a package for use with Amazon OpenSearch Service domains. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\&quot;&gt;Custom packages for Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let createPackageRequest = new AmazonOpenSearchService.CreatePackageRequest(); // CreatePackageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createPackage(createPackageRequest, opts, (error, data, response) => {
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
 **createPackageRequest** | [**CreatePackageRequest**](CreatePackageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreatePackageResponse**](CreatePackageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVpcEndpoint

> CreateVpcEndpointResponse createVpcEndpoint(createVpcEndpointRequest, opts)



Creates an Amazon OpenSearch Service-managed VPC endpoint.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let createVpcEndpointRequest = new AmazonOpenSearchService.CreateVpcEndpointRequest(); // CreateVpcEndpointRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createVpcEndpoint(createVpcEndpointRequest, opts, (error, data, response) => {
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
 **createVpcEndpointRequest** | [**CreateVpcEndpointRequest**](CreateVpcEndpointRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateVpcEndpointResponse**](CreateVpcEndpointResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDomain

> DeleteDomainResponse deleteDomain(domainName, opts)



Deletes an Amazon OpenSearch Service domain and all of its data. You can&#39;t recover a domain after you delete it.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the domain you want to permanently delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteDomain(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The name of the domain you want to permanently delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteDomainResponse**](DeleteDomainResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteInboundConnection

> DeleteInboundConnectionResponse deleteInboundConnection(connectionId, opts)



Allows the destination Amazon OpenSearch Service domain owner to delete an existing inbound cross-cluster search connection. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html\&quot;&gt;Cross-cluster search for Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let connectionId = "connectionId_example"; // String | The ID of the inbound connection to permanently delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteInboundConnection(connectionId, opts, (error, data, response) => {
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
 **connectionId** | **String**| The ID of the inbound connection to permanently delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteInboundConnectionResponse**](DeleteInboundConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteOutboundConnection

> DeleteOutboundConnectionResponse deleteOutboundConnection(connectionId, opts)



Allows the source Amazon OpenSearch Service domain owner to delete an existing outbound cross-cluster search connection. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html\&quot;&gt;Cross-cluster search for Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let connectionId = "connectionId_example"; // String | The ID of the outbound connection you want to permanently delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteOutboundConnection(connectionId, opts, (error, data, response) => {
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
 **connectionId** | **String**| The ID of the outbound connection you want to permanently delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteOutboundConnectionResponse**](DeleteOutboundConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePackage

> DeletePackageResponse deletePackage(packageID, opts)



Deletes an Amazon OpenSearch Service package. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\&quot;&gt;Custom packages for Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let packageID = "packageID_example"; // String | The internal ID of the package you want to delete. Use <code>DescribePackages</code> to find this value.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deletePackage(packageID, opts, (error, data, response) => {
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
 **packageID** | **String**| The internal ID of the package you want to delete. Use &lt;code&gt;DescribePackages&lt;/code&gt; to find this value. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeletePackageResponse**](DeletePackageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVpcEndpoint

> DeleteVpcEndpointResponse deleteVpcEndpoint(vpcEndpointId, opts)



Deletes an Amazon OpenSearch Service-managed interface VPC endpoint.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let vpcEndpointId = "vpcEndpointId_example"; // String | The unique identifier of the endpoint.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteVpcEndpoint(vpcEndpointId, opts, (error, data, response) => {
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
 **vpcEndpointId** | **String**| The unique identifier of the endpoint. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteVpcEndpointResponse**](DeleteVpcEndpointResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeDomain

> DescribeDomainResponse describeDomain(domainName, opts)



Describes the domain configuration for the specified Amazon OpenSearch Service domain, including the domain ID, domain service endpoint, and domain ARN.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the domain that you want information about.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeDomain(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The name of the domain that you want information about. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeDomainResponse**](DescribeDomainResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeDomainAutoTunes

> DescribeDomainAutoTunesResponse describeDomainAutoTunes(domainName, describeDomainAutoTunesRequest, opts)



Returns the list of optimizations that Auto-Tune has made to an Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html\&quot;&gt;Auto-Tune for Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let domainName = "domainName_example"; // String | Name of the domain that you want Auto-Tune details about.
let describeDomainAutoTunesRequest = new AmazonOpenSearchService.DescribeDomainAutoTunesRequest(); // DescribeDomainAutoTunesRequest | 
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
apiInstance.describeDomainAutoTunes(domainName, describeDomainAutoTunesRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| Name of the domain that you want Auto-Tune details about. | 
 **describeDomainAutoTunesRequest** | [**DescribeDomainAutoTunesRequest**](DescribeDomainAutoTunesRequest.md)|  | 
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

[**DescribeDomainAutoTunesResponse**](DescribeDomainAutoTunesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeDomainChangeProgress

> DescribeDomainChangeProgressResponse describeDomainChangeProgress(domainName, opts)



Returns information about the current blue/green deployment happening on an Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html\&quot;&gt;Making configuration changes in Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the domain to get progress information for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'changeid': "changeid_example" // String | The specific change ID for which you want to get progress information. If omitted, the request returns information about the most recent configuration change.
};
apiInstance.describeDomainChangeProgress(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The name of the domain to get progress information for. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **changeid** | **String**| The specific change ID for which you want to get progress information. If omitted, the request returns information about the most recent configuration change. | [optional] 

### Return type

[**DescribeDomainChangeProgressResponse**](DescribeDomainChangeProgressResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeDomainConfig

> DescribeDomainConfigResponse describeDomainConfig(domainName, opts)



Returns the configuration of an Amazon OpenSearch Service domain.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let domainName = "domainName_example"; // String | Name of the OpenSearch Service domain configuration that you want to describe.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeDomainConfig(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| Name of the OpenSearch Service domain configuration that you want to describe. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeDomainConfigResponse**](DescribeDomainConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeDomainHealth

> DescribeDomainHealthResponse describeDomainHealth(domainName, opts)



Returns information about domain and node health, the standby Availability Zone, number of nodes per Availability Zone, and shard count per node.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the domain.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeDomainHealth(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The name of the domain. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeDomainHealthResponse**](DescribeDomainHealthResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeDomainNodes

> DescribeDomainNodesResponse describeDomainNodes(domainName, opts)



Returns information about domain and nodes, including data nodes, master nodes, ultrawarm nodes, Availability Zone(s), standby nodes, node configurations, and node states.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the domain.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeDomainNodes(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The name of the domain. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeDomainNodesResponse**](DescribeDomainNodesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeDomains

> DescribeDomainsResponse describeDomains(describeDomainsRequest, opts)



Returns domain configuration information about the specified Amazon OpenSearch Service domains.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let describeDomainsRequest = new AmazonOpenSearchService.DescribeDomainsRequest(); // DescribeDomainsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeDomains(describeDomainsRequest, opts, (error, data, response) => {
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
 **describeDomainsRequest** | [**DescribeDomainsRequest**](DescribeDomainsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeDomainsResponse**](DescribeDomainsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeDryRunProgress

> DescribeDryRunProgressResponse describeDryRunProgress(domainName, opts)



Describes the progress of a pre-update dry run analysis on an Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes#dryrun\&quot;&gt;Determining whether a change will cause a blue/green deployment&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the domain.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'dryRunId': "dryRunId_example", // String | The unique identifier of the dry run.
  'loadDryRunConfig': true // Boolean | Whether to include the configuration of the dry run in the response. The configuration specifies the updates that you're planning to make on the domain.
};
apiInstance.describeDryRunProgress(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The name of the domain. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **dryRunId** | **String**| The unique identifier of the dry run. | [optional] 
 **loadDryRunConfig** | **Boolean**| Whether to include the configuration of the dry run in the response. The configuration specifies the updates that you&#39;re planning to make on the domain. | [optional] 

### Return type

[**DescribeDryRunProgressResponse**](DescribeDryRunProgressResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeInboundConnections

> DescribeInboundConnectionsResponse describeInboundConnections(describeInboundConnectionsRequest, opts)



Lists all the inbound cross-cluster search connections for a destination (remote) Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html\&quot;&gt;Cross-cluster search for Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let describeInboundConnectionsRequest = new AmazonOpenSearchService.DescribeInboundConnectionsRequest(); // DescribeInboundConnectionsRequest | 
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
apiInstance.describeInboundConnections(describeInboundConnectionsRequest, opts, (error, data, response) => {
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
 **describeInboundConnectionsRequest** | [**DescribeInboundConnectionsRequest**](DescribeInboundConnectionsRequest.md)|  | 
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

[**DescribeInboundConnectionsResponse**](DescribeInboundConnectionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeInstanceTypeLimits

> DescribeInstanceTypeLimitsResponse describeInstanceTypeLimits(instanceType, engineVersion, opts)



Describes the instance count, storage, and master node limits for a given OpenSearch or Elasticsearch version and instance type.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let instanceType = "instanceType_example"; // String | The OpenSearch Service instance type for which you need limit information.
let engineVersion = "engineVersion_example"; // String | Version of OpenSearch or Elasticsearch, in the format Elasticsearch_X.Y or OpenSearch_X.Y. Defaults to the latest version of OpenSearch.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'domainName': "domainName_example" // String | The name of the domain. Only specify if you need the limits for an existing domain.
};
apiInstance.describeInstanceTypeLimits(instanceType, engineVersion, opts, (error, data, response) => {
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
 **instanceType** | **String**| The OpenSearch Service instance type for which you need limit information. | 
 **engineVersion** | **String**| Version of OpenSearch or Elasticsearch, in the format Elasticsearch_X.Y or OpenSearch_X.Y. Defaults to the latest version of OpenSearch. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **domainName** | **String**| The name of the domain. Only specify if you need the limits for an existing domain. | [optional] 

### Return type

[**DescribeInstanceTypeLimitsResponse**](DescribeInstanceTypeLimitsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeOutboundConnections

> DescribeOutboundConnectionsResponse describeOutboundConnections(describeOutboundConnectionsRequest, opts)



Lists all the outbound cross-cluster connections for a local (source) Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html\&quot;&gt;Cross-cluster search for Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let describeOutboundConnectionsRequest = new AmazonOpenSearchService.DescribeOutboundConnectionsRequest(); // DescribeOutboundConnectionsRequest | 
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
apiInstance.describeOutboundConnections(describeOutboundConnectionsRequest, opts, (error, data, response) => {
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
 **describeOutboundConnectionsRequest** | [**DescribeOutboundConnectionsRequest**](DescribeOutboundConnectionsRequest.md)|  | 
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

[**DescribeOutboundConnectionsResponse**](DescribeOutboundConnectionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describePackages

> DescribePackagesResponse describePackages(describePackagesRequest, opts)



Describes all packages available to OpenSearch Service. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\&quot;&gt;Custom packages for Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let describePackagesRequest = new AmazonOpenSearchService.DescribePackagesRequest(); // DescribePackagesRequest | 
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
apiInstance.describePackages(describePackagesRequest, opts, (error, data, response) => {
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
 **describePackagesRequest** | [**DescribePackagesRequest**](DescribePackagesRequest.md)|  | 
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

[**DescribePackagesResponse**](DescribePackagesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeReservedInstanceOfferings

> DescribeReservedInstanceOfferingsResponse describeReservedInstanceOfferings(opts)



Describes the available Amazon OpenSearch Service Reserved Instance offerings for a given Region. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ri.html\&quot;&gt;Reserved Instances in Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'offeringId': "offeringId_example", // String | The Reserved Instance identifier filter value. Use this parameter to show only the available instance types that match the specified reservation identifier.
  'maxResults': 56, // Number | An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.
  'nextToken': "nextToken_example", // String | If your initial <code>DescribeReservedInstanceOfferings</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>DescribeReservedInstanceOfferings</code> operations, which returns results in the next page.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.describeReservedInstanceOfferings(opts, (error, data, response) => {
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
 **offeringId** | **String**| The Reserved Instance identifier filter value. Use this parameter to show only the available instance types that match the specified reservation identifier. | [optional] 
 **maxResults** | **Number**| An optional parameter that specifies the maximum number of results to return. You can use &lt;code&gt;nextToken&lt;/code&gt; to get the next page of results. | [optional] 
 **nextToken** | **String**| If your initial &lt;code&gt;DescribeReservedInstanceOfferings&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;DescribeReservedInstanceOfferings&lt;/code&gt; operations, which returns results in the next page. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**DescribeReservedInstanceOfferingsResponse**](DescribeReservedInstanceOfferingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeReservedInstances

> DescribeReservedInstancesResponse describeReservedInstances(opts)



Describes the Amazon OpenSearch Service instances that you have reserved in a given Region. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ri.html\&quot;&gt;Reserved Instances in Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'reservationId': "reservationId_example", // String | The reserved instance identifier filter value. Use this parameter to show only the reservation that matches the specified reserved OpenSearch instance ID.
  'maxResults': 56, // Number | An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.
  'nextToken': "nextToken_example", // String | If your initial <code>DescribeReservedInstances</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>DescribeReservedInstances</code> operations, which returns results in the next page.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.describeReservedInstances(opts, (error, data, response) => {
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
 **reservationId** | **String**| The reserved instance identifier filter value. Use this parameter to show only the reservation that matches the specified reserved OpenSearch instance ID. | [optional] 
 **maxResults** | **Number**| An optional parameter that specifies the maximum number of results to return. You can use &lt;code&gt;nextToken&lt;/code&gt; to get the next page of results. | [optional] 
 **nextToken** | **String**| If your initial &lt;code&gt;DescribeReservedInstances&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;DescribeReservedInstances&lt;/code&gt; operations, which returns results in the next page. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**DescribeReservedInstancesResponse**](DescribeReservedInstancesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeVpcEndpoints

> DescribeVpcEndpointsResponse describeVpcEndpoints(describeVpcEndpointsRequest, opts)



Describes one or more Amazon OpenSearch Service-managed VPC endpoints.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let describeVpcEndpointsRequest = new AmazonOpenSearchService.DescribeVpcEndpointsRequest(); // DescribeVpcEndpointsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeVpcEndpoints(describeVpcEndpointsRequest, opts, (error, data, response) => {
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
 **describeVpcEndpointsRequest** | [**DescribeVpcEndpointsRequest**](DescribeVpcEndpointsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeVpcEndpointsResponse**](DescribeVpcEndpointsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dissociatePackage

> DissociatePackageResponse dissociatePackage(packageID, domainName, opts)



Removes a package from the specified Amazon OpenSearch Service domain. The package can&#39;t be in use with any OpenSearch index for the dissociation to succeed. The package is still available in OpenSearch Service for association later. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\&quot;&gt;Custom packages for Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let packageID = "packageID_example"; // String | Internal ID of the package to dissociate from the domain. Use <code>ListPackagesForDomain</code> to find this value.
let domainName = "domainName_example"; // String | Name of the domain to dissociate the package from.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.dissociatePackage(packageID, domainName, opts, (error, data, response) => {
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
 **packageID** | **String**| Internal ID of the package to dissociate from the domain. Use &lt;code&gt;ListPackagesForDomain&lt;/code&gt; to find this value. | 
 **domainName** | **String**| Name of the domain to dissociate the package from. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DissociatePackageResponse**](DissociatePackageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompatibleVersions

> GetCompatibleVersionsResponse getCompatibleVersions(opts)



Returns a map of OpenSearch or Elasticsearch versions and the versions you can upgrade them to.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'domainName': "domainName_example" // String | The name of an existing domain. Provide this parameter to limit the results to a single domain.
};
apiInstance.getCompatibleVersions(opts, (error, data, response) => {
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
 **domainName** | **String**| The name of an existing domain. Provide this parameter to limit the results to a single domain. | [optional] 

### Return type

[**GetCompatibleVersionsResponse**](GetCompatibleVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPackageVersionHistory

> GetPackageVersionHistoryResponse getPackageVersionHistory(packageID, opts)



Returns a list of Amazon OpenSearch Service package versions, along with their creation time, commit message, and plugin properties (if the package is a zip plugin package). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\&quot;&gt;Custom packages for Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let packageID = "packageID_example"; // String | The unique identifier of the package.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.
  'nextToken': "nextToken_example", // String | If your initial <code>GetPackageVersionHistory</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>GetPackageVersionHistory</code> operations, which returns results in the next page. 
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.getPackageVersionHistory(packageID, opts, (error, data, response) => {
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
 **packageID** | **String**| The unique identifier of the package. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| An optional parameter that specifies the maximum number of results to return. You can use &lt;code&gt;nextToken&lt;/code&gt; to get the next page of results. | [optional] 
 **nextToken** | **String**| If your initial &lt;code&gt;GetPackageVersionHistory&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;GetPackageVersionHistory&lt;/code&gt; operations, which returns results in the next page.  | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**GetPackageVersionHistoryResponse**](GetPackageVersionHistoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUpgradeHistory

> GetUpgradeHistoryResponse getUpgradeHistory(domainName, opts)



Retrieves the complete history of the last 10 upgrades performed on an Amazon OpenSearch Service domain.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of an existing domain.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.
  'nextToken': "nextToken_example", // String | If your initial <code>GetUpgradeHistory</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>GetUpgradeHistory</code> operations, which returns results in the next page.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.getUpgradeHistory(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The name of an existing domain. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| An optional parameter that specifies the maximum number of results to return. You can use &lt;code&gt;nextToken&lt;/code&gt; to get the next page of results. | [optional] 
 **nextToken** | **String**| If your initial &lt;code&gt;GetUpgradeHistory&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;GetUpgradeHistory&lt;/code&gt; operations, which returns results in the next page. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**GetUpgradeHistoryResponse**](GetUpgradeHistoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUpgradeStatus

> GetUpgradeStatusResponse getUpgradeStatus(domainName, opts)



Returns the most recent status of the last upgrade or upgrade eligibility check performed on an Amazon OpenSearch Service domain.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let domainName = "domainName_example"; // String | The domain of the domain to get upgrade status information for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getUpgradeStatus(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The domain of the domain to get upgrade status information for. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetUpgradeStatusResponse**](GetUpgradeStatusResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDomainNames

> ListDomainNamesResponse listDomainNames(opts)



Returns the names of all Amazon OpenSearch Service domains owned by the current user in the active Region.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'engineType': "engineType_example" // String | Filters the output by domain engine type.
};
apiInstance.listDomainNames(opts, (error, data, response) => {
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
 **engineType** | **String**| Filters the output by domain engine type. | [optional] 

### Return type

[**ListDomainNamesResponse**](ListDomainNamesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDomainsForPackage

> ListDomainsForPackageResponse listDomainsForPackage(packageID, opts)



Lists all Amazon OpenSearch Service domains associated with a given package. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\&quot;&gt;Custom packages for Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let packageID = "packageID_example"; // String | The unique identifier of the package for which to list associated domains.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.
  'nextToken': "nextToken_example", // String | If your initial <code>ListDomainsForPackage</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListDomainsForPackage</code> operations, which returns results in the next page.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listDomainsForPackage(packageID, opts, (error, data, response) => {
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
 **packageID** | **String**| The unique identifier of the package for which to list associated domains. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| An optional parameter that specifies the maximum number of results to return. You can use &lt;code&gt;nextToken&lt;/code&gt; to get the next page of results. | [optional] 
 **nextToken** | **String**| If your initial &lt;code&gt;ListDomainsForPackage&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;ListDomainsForPackage&lt;/code&gt; operations, which returns results in the next page. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListDomainsForPackageResponse**](ListDomainsForPackageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listInstanceTypeDetails

> ListInstanceTypeDetailsResponse listInstanceTypeDetails(engineVersion, opts)



Lists all instance types and available features for a given OpenSearch or Elasticsearch version.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let engineVersion = "engineVersion_example"; // String | The version of OpenSearch or Elasticsearch, in the format Elasticsearch_X.Y or OpenSearch_X.Y. Defaults to the latest version of OpenSearch.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'domainName': "domainName_example", // String | The name of the domain.
  'maxResults': 56, // Number | An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.
  'nextToken': "nextToken_example", // String | If your initial <code>ListInstanceTypeDetails</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListInstanceTypeDetails</code> operations, which returns results in the next page.
  'retrieveAZs': true, // Boolean | An optional parameter that specifies the Availability Zones for the domain.
  'instanceType': "instanceType_example", // String | An optional parameter that lists information for a given instance type.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listInstanceTypeDetails(engineVersion, opts, (error, data, response) => {
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
 **engineVersion** | **String**| The version of OpenSearch or Elasticsearch, in the format Elasticsearch_X.Y or OpenSearch_X.Y. Defaults to the latest version of OpenSearch. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **domainName** | **String**| The name of the domain. | [optional] 
 **maxResults** | **Number**| An optional parameter that specifies the maximum number of results to return. You can use &lt;code&gt;nextToken&lt;/code&gt; to get the next page of results. | [optional] 
 **nextToken** | **String**| If your initial &lt;code&gt;ListInstanceTypeDetails&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;ListInstanceTypeDetails&lt;/code&gt; operations, which returns results in the next page. | [optional] 
 **retrieveAZs** | **Boolean**| An optional parameter that specifies the Availability Zones for the domain. | [optional] 
 **instanceType** | **String**| An optional parameter that lists information for a given instance type. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListInstanceTypeDetailsResponse**](ListInstanceTypeDetailsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPackagesForDomain

> ListPackagesForDomainResponse listPackagesForDomain(domainName, opts)



Lists all packages associated with an Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\&quot;&gt;Custom packages for Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the domain for which you want to list associated packages.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.
  'nextToken': "nextToken_example", // String | If your initial <code>ListPackagesForDomain</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListPackagesForDomain</code> operations, which returns results in the next page.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listPackagesForDomain(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The name of the domain for which you want to list associated packages. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| An optional parameter that specifies the maximum number of results to return. You can use &lt;code&gt;nextToken&lt;/code&gt; to get the next page of results. | [optional] 
 **nextToken** | **String**| If your initial &lt;code&gt;ListPackagesForDomain&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;ListPackagesForDomain&lt;/code&gt; operations, which returns results in the next page. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListPackagesForDomainResponse**](ListPackagesForDomainResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listScheduledActions

> ListScheduledActionsResponse listScheduledActions(domainName, opts)



Retrieves a list of configuration changes that are scheduled for a domain. These changes can be &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html\&quot;&gt;service software updates&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html#auto-tune-types\&quot;&gt;blue/green Auto-Tune enhancements&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the domain.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.
  'nextToken': "nextToken_example", // String | If your initial <code>ListScheduledActions</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListScheduledActions</code> operations, which returns results in the next page.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listScheduledActions(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The name of the domain. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| An optional parameter that specifies the maximum number of results to return. You can use &lt;code&gt;nextToken&lt;/code&gt; to get the next page of results. | [optional] 
 **nextToken** | **String**| If your initial &lt;code&gt;ListScheduledActions&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;ListScheduledActions&lt;/code&gt; operations, which returns results in the next page. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListScheduledActionsResponse**](ListScheduledActionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTags

> ListTagsResponse listTags(arn, opts)



Returns all resource tags for an Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-awsresourcetagging.html\&quot;&gt;Tagging Amazon OpenSearch Service domains&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let arn = "arn_example"; // String | Amazon Resource Name (ARN) for the domain to view tags for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTags(arn, opts, (error, data, response) => {
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
 **arn** | **String**| Amazon Resource Name (ARN) for the domain to view tags for. | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## listVersions

> ListVersionsResponse listVersions(opts)



Lists all versions of OpenSearch and Elasticsearch that Amazon OpenSearch Service supports.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.
  'nextToken': "nextToken_example", // String | If your initial <code>ListVersions</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListVersions</code> operations, which returns results in the next page.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listVersions(opts, (error, data, response) => {
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
 **maxResults** | **Number**| An optional parameter that specifies the maximum number of results to return. You can use &lt;code&gt;nextToken&lt;/code&gt; to get the next page of results. | [optional] 
 **nextToken** | **String**| If your initial &lt;code&gt;ListVersions&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;ListVersions&lt;/code&gt; operations, which returns results in the next page. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListVersionsResponse**](ListVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listVpcEndpointAccess

> ListVpcEndpointAccessResponse listVpcEndpointAccess(domainName, opts)



Retrieves information about each Amazon Web Services principal that is allowed to access a given Amazon OpenSearch Service domain through the use of an interface VPC endpoint.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the OpenSearch Service domain to retrieve access information for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | If your initial <code>ListVpcEndpointAccess</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListVpcEndpointAccess</code> operations, which returns results in the next page.
};
apiInstance.listVpcEndpointAccess(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The name of the OpenSearch Service domain to retrieve access information for. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| If your initial &lt;code&gt;ListVpcEndpointAccess&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;ListVpcEndpointAccess&lt;/code&gt; operations, which returns results in the next page. | [optional] 

### Return type

[**ListVpcEndpointAccessResponse**](ListVpcEndpointAccessResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listVpcEndpoints

> ListVpcEndpointsResponse listVpcEndpoints(opts)



Retrieves all Amazon OpenSearch Service-managed VPC endpoints in the current Amazon Web Services account and Region.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | If your initial <code>ListVpcEndpoints</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListVpcEndpoints</code> operations, which returns results in the next page.
};
apiInstance.listVpcEndpoints(opts, (error, data, response) => {
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
 **nextToken** | **String**| If your initial &lt;code&gt;ListVpcEndpoints&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;ListVpcEndpoints&lt;/code&gt; operations, which returns results in the next page. | [optional] 

### Return type

[**ListVpcEndpointsResponse**](ListVpcEndpointsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listVpcEndpointsForDomain

> ListVpcEndpointsForDomainResponse listVpcEndpointsForDomain(domainName, opts)



Retrieves all Amazon OpenSearch Service-managed VPC endpoints associated with a particular domain.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the domain to list associated VPC endpoints for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | If your initial <code>ListEndpointsForDomain</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListEndpointsForDomain</code> operations, which returns results in the next page.
};
apiInstance.listVpcEndpointsForDomain(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The name of the domain to list associated VPC endpoints for. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| If your initial &lt;code&gt;ListEndpointsForDomain&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;ListEndpointsForDomain&lt;/code&gt; operations, which returns results in the next page. | [optional] 

### Return type

[**ListVpcEndpointsForDomainResponse**](ListVpcEndpointsForDomainResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## purchaseReservedInstanceOffering

> PurchaseReservedInstanceOfferingResponse purchaseReservedInstanceOffering(purchaseReservedInstanceOfferingRequest, opts)



Allows you to purchase Amazon OpenSearch Service Reserved Instances.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let purchaseReservedInstanceOfferingRequest = new AmazonOpenSearchService.PurchaseReservedInstanceOfferingRequest(); // PurchaseReservedInstanceOfferingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.purchaseReservedInstanceOffering(purchaseReservedInstanceOfferingRequest, opts, (error, data, response) => {
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
 **purchaseReservedInstanceOfferingRequest** | [**PurchaseReservedInstanceOfferingRequest**](PurchaseReservedInstanceOfferingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PurchaseReservedInstanceOfferingResponse**](PurchaseReservedInstanceOfferingResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## rejectInboundConnection

> RejectInboundConnectionResponse rejectInboundConnection(connectionId, opts)



Allows the remote Amazon OpenSearch Service domain owner to reject an inbound cross-cluster connection request.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let connectionId = "connectionId_example"; // String | The unique identifier of the inbound connection to reject.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.rejectInboundConnection(connectionId, opts, (error, data, response) => {
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
 **connectionId** | **String**| The unique identifier of the inbound connection to reject. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RejectInboundConnectionResponse**](RejectInboundConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeTags

> removeTags(removeTagsRequest, opts)



Removes the specified set of tags from an Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains.html#managedomains-awsresorcetagging\&quot;&gt; Tagging Amazon OpenSearch Service domains&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let removeTagsRequest = new AmazonOpenSearchService.RemoveTagsRequest(); // RemoveTagsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.removeTags(removeTagsRequest, opts, (error, data, response) => {
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
 **removeTagsRequest** | [**RemoveTagsRequest**](RemoveTagsRequest.md)|  | 
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


## revokeVpcEndpointAccess

> Object revokeVpcEndpointAccess(domainName, revokeVpcEndpointAccessRequest, opts)



Revokes access to an Amazon OpenSearch Service domain that was provided through an interface VPC endpoint.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the OpenSearch Service domain.
let revokeVpcEndpointAccessRequest = new AmazonOpenSearchService.RevokeVpcEndpointAccessRequest(); // RevokeVpcEndpointAccessRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.revokeVpcEndpointAccess(domainName, revokeVpcEndpointAccessRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The name of the OpenSearch Service domain. | 
 **revokeVpcEndpointAccessRequest** | [**RevokeVpcEndpointAccessRequest**](RevokeVpcEndpointAccessRequest.md)|  | 
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


## startServiceSoftwareUpdate

> StartServiceSoftwareUpdateResponse startServiceSoftwareUpdate(startServiceSoftwareUpdateRequest, opts)



Schedules a service software update for an Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html\&quot;&gt;Service software updates in Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let startServiceSoftwareUpdateRequest = new AmazonOpenSearchService.StartServiceSoftwareUpdateRequest(); // StartServiceSoftwareUpdateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startServiceSoftwareUpdate(startServiceSoftwareUpdateRequest, opts, (error, data, response) => {
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
 **startServiceSoftwareUpdateRequest** | [**StartServiceSoftwareUpdateRequest**](StartServiceSoftwareUpdateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartServiceSoftwareUpdateResponse**](StartServiceSoftwareUpdateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDomainConfig

> UpdateDomainConfigResponse updateDomainConfig(domainName, updateDomainConfigRequest, opts)



Modifies the cluster configuration of the specified Amazon OpenSearch Service domain.sl

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the domain that you're updating.
let updateDomainConfigRequest = new AmazonOpenSearchService.UpdateDomainConfigRequest(); // UpdateDomainConfigRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateDomainConfig(domainName, updateDomainConfigRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The name of the domain that you&#39;re updating. | 
 **updateDomainConfigRequest** | [**UpdateDomainConfigRequest**](UpdateDomainConfigRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateDomainConfigResponse**](UpdateDomainConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePackage

> UpdatePackageResponse updatePackage(updatePackageRequest, opts)



Updates a package for use with Amazon OpenSearch Service domains. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\&quot;&gt;Custom packages for Amazon OpenSearch Service&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let updatePackageRequest = new AmazonOpenSearchService.UpdatePackageRequest(); // UpdatePackageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updatePackage(updatePackageRequest, opts, (error, data, response) => {
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
 **updatePackageRequest** | [**UpdatePackageRequest**](UpdatePackageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdatePackageResponse**](UpdatePackageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateScheduledAction

> UpdateScheduledActionResponse updateScheduledAction(domainName, updateScheduledActionRequest, opts)



Reschedules a planned domain configuration change for a later time. This change can be a scheduled &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html\&quot;&gt;service software update&lt;/a&gt; or a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html#auto-tune-types\&quot;&gt;blue/green Auto-Tune enhancement&lt;/a&gt;.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the domain to reschedule an action for.
let updateScheduledActionRequest = new AmazonOpenSearchService.UpdateScheduledActionRequest(); // UpdateScheduledActionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateScheduledAction(domainName, updateScheduledActionRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The name of the domain to reschedule an action for. | 
 **updateScheduledActionRequest** | [**UpdateScheduledActionRequest**](UpdateScheduledActionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateScheduledActionResponse**](UpdateScheduledActionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateVpcEndpoint

> UpdateVpcEndpointResponse updateVpcEndpoint(updateVpcEndpointRequest, opts)



Modifies an Amazon OpenSearch Service-managed interface VPC endpoint.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let updateVpcEndpointRequest = new AmazonOpenSearchService.UpdateVpcEndpointRequest(); // UpdateVpcEndpointRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateVpcEndpoint(updateVpcEndpointRequest, opts, (error, data, response) => {
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
 **updateVpcEndpointRequest** | [**UpdateVpcEndpointRequest**](UpdateVpcEndpointRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateVpcEndpointResponse**](UpdateVpcEndpointResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## upgradeDomain

> UpgradeDomainResponse upgradeDomain(upgradeDomainRequest, opts)



Allows you to either upgrade your Amazon OpenSearch Service domain or perform an upgrade eligibility check to a compatible version of OpenSearch or Elasticsearch.

### Example

```javascript
import AmazonOpenSearchService from 'amazon_open_search_service';
let defaultClient = AmazonOpenSearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOpenSearchService.DefaultApi();
let upgradeDomainRequest = new AmazonOpenSearchService.UpgradeDomainRequest(); // UpgradeDomainRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.upgradeDomain(upgradeDomainRequest, opts, (error, data, response) => {
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
 **upgradeDomainRequest** | [**UpgradeDomainRequest**](UpgradeDomainRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpgradeDomainResponse**](UpgradeDomainResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

