# AmazonElasticsearchService.DefaultApi

All URIs are relative to *http://es.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acceptInboundCrossClusterSearchConnection**](DefaultApi.md#acceptInboundCrossClusterSearchConnection) | **PUT** /2015-01-01/es/ccs/inboundConnection/{ConnectionId}/accept | 
[**addTags**](DefaultApi.md#addTags) | **POST** /2015-01-01/tags | 
[**associatePackage**](DefaultApi.md#associatePackage) | **POST** /2015-01-01/packages/associate/{PackageID}/{DomainName} | 
[**authorizeVpcEndpointAccess**](DefaultApi.md#authorizeVpcEndpointAccess) | **POST** /2015-01-01/es/domain/{DomainName}/authorizeVpcEndpointAccess | 
[**cancelElasticsearchServiceSoftwareUpdate**](DefaultApi.md#cancelElasticsearchServiceSoftwareUpdate) | **POST** /2015-01-01/es/serviceSoftwareUpdate/cancel | 
[**createElasticsearchDomain**](DefaultApi.md#createElasticsearchDomain) | **POST** /2015-01-01/es/domain | 
[**createOutboundCrossClusterSearchConnection**](DefaultApi.md#createOutboundCrossClusterSearchConnection) | **POST** /2015-01-01/es/ccs/outboundConnection | 
[**createPackage**](DefaultApi.md#createPackage) | **POST** /2015-01-01/packages | 
[**createVpcEndpoint**](DefaultApi.md#createVpcEndpoint) | **POST** /2015-01-01/es/vpcEndpoints | 
[**deleteElasticsearchDomain**](DefaultApi.md#deleteElasticsearchDomain) | **DELETE** /2015-01-01/es/domain/{DomainName} | 
[**deleteElasticsearchServiceRole**](DefaultApi.md#deleteElasticsearchServiceRole) | **DELETE** /2015-01-01/es/role | 
[**deleteInboundCrossClusterSearchConnection**](DefaultApi.md#deleteInboundCrossClusterSearchConnection) | **DELETE** /2015-01-01/es/ccs/inboundConnection/{ConnectionId} | 
[**deleteOutboundCrossClusterSearchConnection**](DefaultApi.md#deleteOutboundCrossClusterSearchConnection) | **DELETE** /2015-01-01/es/ccs/outboundConnection/{ConnectionId} | 
[**deletePackage**](DefaultApi.md#deletePackage) | **DELETE** /2015-01-01/packages/{PackageID} | 
[**deleteVpcEndpoint**](DefaultApi.md#deleteVpcEndpoint) | **DELETE** /2015-01-01/es/vpcEndpoints/{VpcEndpointId} | 
[**describeDomainAutoTunes**](DefaultApi.md#describeDomainAutoTunes) | **GET** /2015-01-01/es/domain/{DomainName}/autoTunes | 
[**describeDomainChangeProgress**](DefaultApi.md#describeDomainChangeProgress) | **GET** /2015-01-01/es/domain/{DomainName}/progress | 
[**describeElasticsearchDomain**](DefaultApi.md#describeElasticsearchDomain) | **GET** /2015-01-01/es/domain/{DomainName} | 
[**describeElasticsearchDomainConfig**](DefaultApi.md#describeElasticsearchDomainConfig) | **GET** /2015-01-01/es/domain/{DomainName}/config | 
[**describeElasticsearchDomains**](DefaultApi.md#describeElasticsearchDomains) | **POST** /2015-01-01/es/domain-info | 
[**describeElasticsearchInstanceTypeLimits**](DefaultApi.md#describeElasticsearchInstanceTypeLimits) | **GET** /2015-01-01/es/instanceTypeLimits/{ElasticsearchVersion}/{InstanceType} | 
[**describeInboundCrossClusterSearchConnections**](DefaultApi.md#describeInboundCrossClusterSearchConnections) | **POST** /2015-01-01/es/ccs/inboundConnection/search | 
[**describeOutboundCrossClusterSearchConnections**](DefaultApi.md#describeOutboundCrossClusterSearchConnections) | **POST** /2015-01-01/es/ccs/outboundConnection/search | 
[**describePackages**](DefaultApi.md#describePackages) | **POST** /2015-01-01/packages/describe | 
[**describeReservedElasticsearchInstanceOfferings**](DefaultApi.md#describeReservedElasticsearchInstanceOfferings) | **GET** /2015-01-01/es/reservedInstanceOfferings | 
[**describeReservedElasticsearchInstances**](DefaultApi.md#describeReservedElasticsearchInstances) | **GET** /2015-01-01/es/reservedInstances | 
[**describeVpcEndpoints**](DefaultApi.md#describeVpcEndpoints) | **POST** /2015-01-01/es/vpcEndpoints/describe | 
[**dissociatePackage**](DefaultApi.md#dissociatePackage) | **POST** /2015-01-01/packages/dissociate/{PackageID}/{DomainName} | 
[**getCompatibleElasticsearchVersions**](DefaultApi.md#getCompatibleElasticsearchVersions) | **GET** /2015-01-01/es/compatibleVersions | 
[**getPackageVersionHistory**](DefaultApi.md#getPackageVersionHistory) | **GET** /2015-01-01/packages/{PackageID}/history | 
[**getUpgradeHistory**](DefaultApi.md#getUpgradeHistory) | **GET** /2015-01-01/es/upgradeDomain/{DomainName}/history | 
[**getUpgradeStatus**](DefaultApi.md#getUpgradeStatus) | **GET** /2015-01-01/es/upgradeDomain/{DomainName}/status | 
[**listDomainNames**](DefaultApi.md#listDomainNames) | **GET** /2015-01-01/domain | 
[**listDomainsForPackage**](DefaultApi.md#listDomainsForPackage) | **GET** /2015-01-01/packages/{PackageID}/domains | 
[**listElasticsearchInstanceTypes**](DefaultApi.md#listElasticsearchInstanceTypes) | **GET** /2015-01-01/es/instanceTypes/{ElasticsearchVersion} | 
[**listElasticsearchVersions**](DefaultApi.md#listElasticsearchVersions) | **GET** /2015-01-01/es/versions | 
[**listPackagesForDomain**](DefaultApi.md#listPackagesForDomain) | **GET** /2015-01-01/domain/{DomainName}/packages | 
[**listTags**](DefaultApi.md#listTags) | **GET** /2015-01-01/tags/#arn | 
[**listVpcEndpointAccess**](DefaultApi.md#listVpcEndpointAccess) | **GET** /2015-01-01/es/domain/{DomainName}/listVpcEndpointAccess | 
[**listVpcEndpoints**](DefaultApi.md#listVpcEndpoints) | **GET** /2015-01-01/es/vpcEndpoints | 
[**listVpcEndpointsForDomain**](DefaultApi.md#listVpcEndpointsForDomain) | **GET** /2015-01-01/es/domain/{DomainName}/vpcEndpoints | 
[**purchaseReservedElasticsearchInstanceOffering**](DefaultApi.md#purchaseReservedElasticsearchInstanceOffering) | **POST** /2015-01-01/es/purchaseReservedInstanceOffering | 
[**rejectInboundCrossClusterSearchConnection**](DefaultApi.md#rejectInboundCrossClusterSearchConnection) | **PUT** /2015-01-01/es/ccs/inboundConnection/{ConnectionId}/reject | 
[**removeTags**](DefaultApi.md#removeTags) | **POST** /2015-01-01/tags-removal | 
[**revokeVpcEndpointAccess**](DefaultApi.md#revokeVpcEndpointAccess) | **POST** /2015-01-01/es/domain/{DomainName}/revokeVpcEndpointAccess | 
[**startElasticsearchServiceSoftwareUpdate**](DefaultApi.md#startElasticsearchServiceSoftwareUpdate) | **POST** /2015-01-01/es/serviceSoftwareUpdate/start | 
[**updateElasticsearchDomainConfig**](DefaultApi.md#updateElasticsearchDomainConfig) | **POST** /2015-01-01/es/domain/{DomainName}/config | 
[**updatePackage**](DefaultApi.md#updatePackage) | **POST** /2015-01-01/packages/update | 
[**updateVpcEndpoint**](DefaultApi.md#updateVpcEndpoint) | **POST** /2015-01-01/es/vpcEndpoints/update | 
[**upgradeElasticsearchDomain**](DefaultApi.md#upgradeElasticsearchDomain) | **POST** /2015-01-01/es/upgradeDomain | 



## acceptInboundCrossClusterSearchConnection

> AcceptInboundCrossClusterSearchConnectionResponse acceptInboundCrossClusterSearchConnection(connectionId, opts)



Allows the destination domain owner to accept an inbound cross-cluster search connection request.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let connectionId = "connectionId_example"; // String | The id of the inbound connection that you want to accept.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.acceptInboundCrossClusterSearchConnection(connectionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectionId** | **String**| The id of the inbound connection that you want to accept. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AcceptInboundCrossClusterSearchConnectionResponse**](AcceptInboundCrossClusterSearchConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addTags

> addTags(addTagsRequest, opts)



Attaches tags to an existing Elasticsearch domain. Tags are a set of case-sensitive key value pairs. An Elasticsearch domain may have up to 10 tags. See &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-awsresorcetagging\&quot; target&#x3D;\&quot;_blank\&quot;&gt; Tagging Amazon Elasticsearch Service Domains for more information.&lt;/a&gt;

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let addTagsRequest = new AmazonElasticsearchService.AddTagsRequest(); // AddTagsRequest | 
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



Associates a package with an Amazon ES domain.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let packageID = "packageID_example"; // String | Internal ID of the package that you want to associate with a domain. Use <code>DescribePackages</code> to find this value.
let domainName = "domainName_example"; // String | Name of the domain that you want to associate the package with.
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
 **packageID** | **String**| Internal ID of the package that you want to associate with a domain. Use &lt;code&gt;DescribePackages&lt;/code&gt; to find this value. | 
 **domainName** | **String**| Name of the domain that you want to associate the package with. | 
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
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the OpenSearch Service domain to provide access to.
let authorizeVpcEndpointAccessRequest = new AmazonElasticsearchService.AuthorizeVpcEndpointAccessRequest(); // AuthorizeVpcEndpointAccessRequest | 
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


## cancelElasticsearchServiceSoftwareUpdate

> CancelElasticsearchServiceSoftwareUpdateResponse cancelElasticsearchServiceSoftwareUpdate(cancelElasticsearchServiceSoftwareUpdateRequest, opts)



Cancels a scheduled service software update for an Amazon ES domain. You can only perform this operation before the &lt;code&gt;AutomatedUpdateDate&lt;/code&gt; and when the &lt;code&gt;UpdateStatus&lt;/code&gt; is in the &lt;code&gt;PENDING_UPDATE&lt;/code&gt; state.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let cancelElasticsearchServiceSoftwareUpdateRequest = new AmazonElasticsearchService.CancelElasticsearchServiceSoftwareUpdateRequest(); // CancelElasticsearchServiceSoftwareUpdateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.cancelElasticsearchServiceSoftwareUpdate(cancelElasticsearchServiceSoftwareUpdateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancelElasticsearchServiceSoftwareUpdateRequest** | [**CancelElasticsearchServiceSoftwareUpdateRequest**](CancelElasticsearchServiceSoftwareUpdateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CancelElasticsearchServiceSoftwareUpdateResponse**](CancelElasticsearchServiceSoftwareUpdateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createElasticsearchDomain

> CreateElasticsearchDomainResponse createElasticsearchDomain(createElasticsearchDomainRequest, opts)



Creates a new Elasticsearch domain. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomains\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Creating Elasticsearch Domains&lt;/a&gt; in the &lt;i&gt;Amazon Elasticsearch Service Developer Guide&lt;/i&gt;.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let createElasticsearchDomainRequest = new AmazonElasticsearchService.CreateElasticsearchDomainRequest(); // CreateElasticsearchDomainRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createElasticsearchDomain(createElasticsearchDomainRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createElasticsearchDomainRequest** | [**CreateElasticsearchDomainRequest**](CreateElasticsearchDomainRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateElasticsearchDomainResponse**](CreateElasticsearchDomainResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOutboundCrossClusterSearchConnection

> CreateOutboundCrossClusterSearchConnectionResponse createOutboundCrossClusterSearchConnection(createOutboundCrossClusterSearchConnectionRequest, opts)



Creates a new cross-cluster search connection from a source domain to a destination domain.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let createOutboundCrossClusterSearchConnectionRequest = new AmazonElasticsearchService.CreateOutboundCrossClusterSearchConnectionRequest(); // CreateOutboundCrossClusterSearchConnectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createOutboundCrossClusterSearchConnection(createOutboundCrossClusterSearchConnectionRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createOutboundCrossClusterSearchConnectionRequest** | [**CreateOutboundCrossClusterSearchConnectionRequest**](CreateOutboundCrossClusterSearchConnectionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateOutboundCrossClusterSearchConnectionResponse**](CreateOutboundCrossClusterSearchConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPackage

> CreatePackageResponse createPackage(createPackageRequest, opts)



Create a package for use with Amazon ES domains.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let createPackageRequest = new AmazonElasticsearchService.CreatePackageRequest(); // CreatePackageRequest | 
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
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let createVpcEndpointRequest = new AmazonElasticsearchService.CreateVpcEndpointRequest(); // CreateVpcEndpointRequest | 
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


## deleteElasticsearchDomain

> DeleteElasticsearchDomainResponse deleteElasticsearchDomain(domainName, opts)



Permanently deletes the specified Elasticsearch domain and all of its data. Once a domain is deleted, it cannot be recovered.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the Elasticsearch domain that you want to permanently delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteElasticsearchDomain(domainName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domainName** | **String**| The name of the Elasticsearch domain that you want to permanently delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteElasticsearchDomainResponse**](DeleteElasticsearchDomainResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteElasticsearchServiceRole

> deleteElasticsearchServiceRole(opts)



Deletes the service-linked role that Elasticsearch Service uses to manage and maintain VPC domains. Role deletion will fail if any existing VPC domains use the role. You must delete any such Elasticsearch domains before deleting the role. See &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-enabling-slr\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Deleting Elasticsearch Service Role&lt;/a&gt; in &lt;i&gt;VPC Endpoints for Amazon Elasticsearch Service Domains&lt;/i&gt;.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteElasticsearchServiceRole(opts, (error, data, response) => {
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


## deleteInboundCrossClusterSearchConnection

> DeleteInboundCrossClusterSearchConnectionResponse deleteInboundCrossClusterSearchConnection(connectionId, opts)



Allows the destination domain owner to delete an existing inbound cross-cluster search connection.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let connectionId = "connectionId_example"; // String | The id of the inbound connection that you want to permanently delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteInboundCrossClusterSearchConnection(connectionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectionId** | **String**| The id of the inbound connection that you want to permanently delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteInboundCrossClusterSearchConnectionResponse**](DeleteInboundCrossClusterSearchConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteOutboundCrossClusterSearchConnection

> DeleteOutboundCrossClusterSearchConnectionResponse deleteOutboundCrossClusterSearchConnection(connectionId, opts)



Allows the source domain owner to delete an existing outbound cross-cluster search connection.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let connectionId = "connectionId_example"; // String | The id of the outbound connection that you want to permanently delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteOutboundCrossClusterSearchConnection(connectionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectionId** | **String**| The id of the outbound connection that you want to permanently delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteOutboundCrossClusterSearchConnectionResponse**](DeleteOutboundCrossClusterSearchConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePackage

> DeletePackageResponse deletePackage(packageID, opts)



Delete the package.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let packageID = "packageID_example"; // String | Internal ID of the package that you want to delete. Use <code>DescribePackages</code> to find this value.
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
 **packageID** | **String**| Internal ID of the package that you want to delete. Use &lt;code&gt;DescribePackages&lt;/code&gt; to find this value. | 
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
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let vpcEndpointId = "vpcEndpointId_example"; // String | The unique identifier of the endpoint to be deleted.
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
 **vpcEndpointId** | **String**| The unique identifier of the endpoint to be deleted. | 
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


## describeDomainAutoTunes

> DescribeDomainAutoTunesResponse describeDomainAutoTunes(domainName, describeDomainAutoTunesRequest, opts)



Provides scheduled Auto-Tune action details for the Elasticsearch domain, such as Auto-Tune action type, description, severity, and scheduled date.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let domainName = "domainName_example"; // String | Specifies the domain name for which you want Auto-Tune action details.
let describeDomainAutoTunesRequest = new AmazonElasticsearchService.DescribeDomainAutoTunesRequest(); // DescribeDomainAutoTunesRequest | 
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
 **domainName** | **String**| Specifies the domain name for which you want Auto-Tune action details. | 
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



Returns information about the current blue/green deployment happening on a domain, including a change ID, status, and progress stages.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let domainName = "domainName_example"; // String | The domain you want to get the progress information about.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'changeid': "changeid_example" // String | The specific change ID for which you want to get progress information. This is an optional parameter. If omitted, the service returns information about the most recent configuration change. 
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
 **domainName** | **String**| The domain you want to get the progress information about. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **changeid** | **String**| The specific change ID for which you want to get progress information. This is an optional parameter. If omitted, the service returns information about the most recent configuration change.  | [optional] 

### Return type

[**DescribeDomainChangeProgressResponse**](DescribeDomainChangeProgressResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeElasticsearchDomain

> DescribeElasticsearchDomainResponse describeElasticsearchDomain(domainName, opts)



Returns domain configuration information about the specified Elasticsearch domain, including the domain ID, domain endpoint, and domain ARN.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the Elasticsearch domain for which you want information.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeElasticsearchDomain(domainName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domainName** | **String**| The name of the Elasticsearch domain for which you want information. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeElasticsearchDomainResponse**](DescribeElasticsearchDomainResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeElasticsearchDomainConfig

> DescribeElasticsearchDomainConfigResponse describeElasticsearchDomainConfig(domainName, opts)



Provides cluster configuration information about the specified Elasticsearch domain, such as the state, creation date, update version, and update date for cluster options.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let domainName = "domainName_example"; // String | The Elasticsearch domain that you want to get information about.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeElasticsearchDomainConfig(domainName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domainName** | **String**| The Elasticsearch domain that you want to get information about. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeElasticsearchDomainConfigResponse**](DescribeElasticsearchDomainConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeElasticsearchDomains

> DescribeElasticsearchDomainsResponse describeElasticsearchDomains(describeElasticsearchDomainsRequest, opts)



Returns domain configuration information about the specified Elasticsearch domains, including the domain ID, domain endpoint, and domain ARN.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let describeElasticsearchDomainsRequest = new AmazonElasticsearchService.DescribeElasticsearchDomainsRequest(); // DescribeElasticsearchDomainsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeElasticsearchDomains(describeElasticsearchDomainsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describeElasticsearchDomainsRequest** | [**DescribeElasticsearchDomainsRequest**](DescribeElasticsearchDomainsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeElasticsearchDomainsResponse**](DescribeElasticsearchDomainsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeElasticsearchInstanceTypeLimits

> DescribeElasticsearchInstanceTypeLimitsResponse describeElasticsearchInstanceTypeLimits(instanceType, elasticsearchVersion, opts)



 Describe Elasticsearch Limits for a given InstanceType and ElasticsearchVersion. When modifying existing Domain, specify the &lt;code&gt; &lt;a&gt;DomainName&lt;/a&gt; &lt;/code&gt; to know what Limits are supported for modifying. 

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let instanceType = "instanceType_example"; // String |  The instance type for an Elasticsearch cluster for which Elasticsearch <code> <a>Limits</a> </code> are needed. 
let elasticsearchVersion = "elasticsearchVersion_example"; // String |  Version of Elasticsearch for which <code> <a>Limits</a> </code> are needed. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'domainName': "domainName_example" // String |  DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for Elasticsearch <code> <a>Limits</a> </code> for existing domain. 
};
apiInstance.describeElasticsearchInstanceTypeLimits(instanceType, elasticsearchVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceType** | **String**|  The instance type for an Elasticsearch cluster for which Elasticsearch &lt;code&gt; &lt;a&gt;Limits&lt;/a&gt; &lt;/code&gt; are needed.  | 
 **elasticsearchVersion** | **String**|  Version of Elasticsearch for which &lt;code&gt; &lt;a&gt;Limits&lt;/a&gt; &lt;/code&gt; are needed.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **domainName** | **String**|  DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for Elasticsearch &lt;code&gt; &lt;a&gt;Limits&lt;/a&gt; &lt;/code&gt; for existing domain.  | [optional] 

### Return type

[**DescribeElasticsearchInstanceTypeLimitsResponse**](DescribeElasticsearchInstanceTypeLimitsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeInboundCrossClusterSearchConnections

> DescribeInboundCrossClusterSearchConnectionsResponse describeInboundCrossClusterSearchConnections(describeInboundCrossClusterSearchConnectionsRequest, opts)



Lists all the inbound cross-cluster search connections for a destination domain.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let describeInboundCrossClusterSearchConnectionsRequest = new AmazonElasticsearchService.DescribeInboundCrossClusterSearchConnectionsRequest(); // DescribeInboundCrossClusterSearchConnectionsRequest | 
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
apiInstance.describeInboundCrossClusterSearchConnections(describeInboundCrossClusterSearchConnectionsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describeInboundCrossClusterSearchConnectionsRequest** | [**DescribeInboundCrossClusterSearchConnectionsRequest**](DescribeInboundCrossClusterSearchConnectionsRequest.md)|  | 
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

[**DescribeInboundCrossClusterSearchConnectionsResponse**](DescribeInboundCrossClusterSearchConnectionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeOutboundCrossClusterSearchConnections

> DescribeOutboundCrossClusterSearchConnectionsResponse describeOutboundCrossClusterSearchConnections(describeOutboundCrossClusterSearchConnectionsRequest, opts)



Lists all the outbound cross-cluster search connections for a source domain.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let describeOutboundCrossClusterSearchConnectionsRequest = new AmazonElasticsearchService.DescribeOutboundCrossClusterSearchConnectionsRequest(); // DescribeOutboundCrossClusterSearchConnectionsRequest | 
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
apiInstance.describeOutboundCrossClusterSearchConnections(describeOutboundCrossClusterSearchConnectionsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describeOutboundCrossClusterSearchConnectionsRequest** | [**DescribeOutboundCrossClusterSearchConnectionsRequest**](DescribeOutboundCrossClusterSearchConnectionsRequest.md)|  | 
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

[**DescribeOutboundCrossClusterSearchConnectionsResponse**](DescribeOutboundCrossClusterSearchConnectionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describePackages

> DescribePackagesResponse describePackages(describePackagesRequest, opts)



Describes all packages available to Amazon ES. Includes options for filtering, limiting the number of results, and pagination.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let describePackagesRequest = new AmazonElasticsearchService.DescribePackagesRequest(); // DescribePackagesRequest | 
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


## describeReservedElasticsearchInstanceOfferings

> DescribeReservedElasticsearchInstanceOfferingsResponse describeReservedElasticsearchInstanceOfferings(opts)



Lists available reserved Elasticsearch instance offerings.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'offeringId': "offeringId_example", // String | The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.
  'maxResults': 56, // Number | Set this value to limit the number of results returned. If not specified, defaults to 100.
  'nextToken': "nextToken_example", // String | NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.describeReservedElasticsearchInstanceOfferings(opts, (error, data, response) => {
  if (error) {
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
 **offeringId** | **String**| The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier. | [optional] 
 **maxResults** | **Number**| Set this value to limit the number of results returned. If not specified, defaults to 100. | [optional] 
 **nextToken** | **String**| NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**DescribeReservedElasticsearchInstanceOfferingsResponse**](DescribeReservedElasticsearchInstanceOfferingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeReservedElasticsearchInstances

> DescribeReservedElasticsearchInstancesResponse describeReservedElasticsearchInstances(opts)



Returns information about reserved Elasticsearch instances for this account.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'reservationId': "reservationId_example", // String | The reserved instance identifier filter value. Use this parameter to show only the reservation that matches the specified reserved Elasticsearch instance ID.
  'maxResults': 56, // Number | Set this value to limit the number of results returned. If not specified, defaults to 100.
  'nextToken': "nextToken_example", // String | NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.describeReservedElasticsearchInstances(opts, (error, data, response) => {
  if (error) {
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
 **reservationId** | **String**| The reserved instance identifier filter value. Use this parameter to show only the reservation that matches the specified reserved Elasticsearch instance ID. | [optional] 
 **maxResults** | **Number**| Set this value to limit the number of results returned. If not specified, defaults to 100. | [optional] 
 **nextToken** | **String**| NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**DescribeReservedElasticsearchInstancesResponse**](DescribeReservedElasticsearchInstancesResponse.md)

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
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let describeVpcEndpointsRequest = new AmazonElasticsearchService.DescribeVpcEndpointsRequest(); // DescribeVpcEndpointsRequest | 
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



Dissociates a package from the Amazon ES domain.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let packageID = "packageID_example"; // String | Internal ID of the package that you want to associate with a domain. Use <code>DescribePackages</code> to find this value.
let domainName = "domainName_example"; // String | Name of the domain that you want to associate the package with.
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
 **packageID** | **String**| Internal ID of the package that you want to associate with a domain. Use &lt;code&gt;DescribePackages&lt;/code&gt; to find this value. | 
 **domainName** | **String**| Name of the domain that you want to associate the package with. | 
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


## getCompatibleElasticsearchVersions

> GetCompatibleElasticsearchVersionsResponse getCompatibleElasticsearchVersions(opts)



 Returns a list of upgrade compatible Elastisearch versions. You can optionally pass a &lt;code&gt; &lt;a&gt;DomainName&lt;/a&gt; &lt;/code&gt; to get all upgrade compatible Elasticsearch versions for that specific domain. 

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'domainName': "domainName_example" // String | 
};
apiInstance.getCompatibleElasticsearchVersions(opts, (error, data, response) => {
  if (error) {
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
 **domainName** | **String**|  | [optional] 

### Return type

[**GetCompatibleElasticsearchVersionsResponse**](GetCompatibleElasticsearchVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPackageVersionHistory

> GetPackageVersionHistoryResponse getPackageVersionHistory(packageID, opts)



Returns a list of versions of the package, along with their creation time and commit message.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let packageID = "packageID_example"; // String | Returns an audit history of versions of the package.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | Limits results to a maximum number of versions.
  'nextToken': "nextToken_example", // String | Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page.
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
 **packageID** | **String**| Returns an audit history of versions of the package. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| Limits results to a maximum number of versions. | [optional] 
 **nextToken** | **String**| Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page. | [optional] 
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



Retrieves the complete history of the last 10 upgrades that were performed on the domain.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let domainName = "domainName_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | 
  'nextToken': "nextToken_example", // String | 
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
 **domainName** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**|  | [optional] 
 **nextToken** | **String**|  | [optional] 
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



Retrieves the latest status of the last upgrade or upgrade eligibility check that was performed on the domain.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let domainName = "domainName_example"; // String | 
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
 **domainName** | **String**|  | 
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



Returns the name of all Elasticsearch domains owned by the current user&#39;s account. 

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'engineType': "engineType_example" // String |  Optional parameter to filter the output by domain engine type. Acceptable values are 'Elasticsearch' and 'OpenSearch'. 
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
 **engineType** | **String**|  Optional parameter to filter the output by domain engine type. Acceptable values are &#39;Elasticsearch&#39; and &#39;OpenSearch&#39;.  | [optional] 

### Return type

[**ListDomainNamesResponse**](ListDomainNamesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDomainsForPackage

> ListDomainsForPackageResponse listDomainsForPackage(packageID, opts)



Lists all Amazon ES domains associated with the package.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let packageID = "packageID_example"; // String | The package for which to list domains.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | Limits results to a maximum number of domains.
  'nextToken': "nextToken_example", // String | Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page.
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
 **packageID** | **String**| The package for which to list domains. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| Limits results to a maximum number of domains. | [optional] 
 **nextToken** | **String**| Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListDomainsForPackageResponse**](ListDomainsForPackageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listElasticsearchInstanceTypes

> ListElasticsearchInstanceTypesResponse listElasticsearchInstanceTypes(elasticsearchVersion, opts)



List all Elasticsearch instance types that are supported for given ElasticsearchVersion

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let elasticsearchVersion = "elasticsearchVersion_example"; // String | Version of Elasticsearch for which list of supported elasticsearch instance types are needed. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'domainName': "domainName_example", // String | DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for list of available Elasticsearch instance types when modifying existing domain. 
  'maxResults': 56, // Number |  Set this value to limit the number of results returned. Value provided must be greater than 30 else it wont be honored. 
  'nextToken': "nextToken_example", // String | NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination. 
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listElasticsearchInstanceTypes(elasticsearchVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **elasticsearchVersion** | **String**| Version of Elasticsearch for which list of supported elasticsearch instance types are needed.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **domainName** | **String**| DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for list of available Elasticsearch instance types when modifying existing domain.  | [optional] 
 **maxResults** | **Number**|  Set this value to limit the number of results returned. Value provided must be greater than 30 else it wont be honored.  | [optional] 
 **nextToken** | **String**| NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination.  | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListElasticsearchInstanceTypesResponse**](ListElasticsearchInstanceTypesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listElasticsearchVersions

> ListElasticsearchVersionsResponse listElasticsearchVersions(opts)



List all supported Elasticsearch versions

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number |  Set this value to limit the number of results returned. Value provided must be greater than 10 else it wont be honored. 
  'nextToken': "nextToken_example", // String | 
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listElasticsearchVersions(opts, (error, data, response) => {
  if (error) {
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
 **maxResults** | **Number**|  Set this value to limit the number of results returned. Value provided must be greater than 10 else it wont be honored.  | [optional] 
 **nextToken** | **String**|  | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListElasticsearchVersionsResponse**](ListElasticsearchVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPackagesForDomain

> ListPackagesForDomainResponse listPackagesForDomain(domainName, opts)



Lists all packages associated with the Amazon ES domain.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the domain for which you want to list associated packages.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | Limits results to a maximum number of packages.
  'nextToken': "nextToken_example", // String | Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page.
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
 **maxResults** | **Number**| Limits results to a maximum number of packages. | [optional] 
 **nextToken** | **String**| Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListPackagesForDomainResponse**](ListPackagesForDomainResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTags

> ListTagsResponse listTags(arn, opts)



Returns all tags for the given Elasticsearch domain.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let arn = "arn_example"; // String |  Specify the <code>ARN</code> for the Elasticsearch domain to which the tags are attached that you want to view.
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
 **arn** | **String**|  Specify the &lt;code&gt;ARN&lt;/code&gt; for the Elasticsearch domain to which the tags are attached that you want to view. | 
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


## listVpcEndpointAccess

> ListVpcEndpointAccessResponse listVpcEndpointAccess(domainName, opts)



Retrieves information about each principal that is allowed to access a given Amazon OpenSearch Service domain through the use of an interface VPC endpoint.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the OpenSearch Service domain to retrieve access information for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | Provides an identifier to allow retrieval of paginated results.
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
 **nextToken** | **String**| Provides an identifier to allow retrieval of paginated results. | [optional] 

### Return type

[**ListVpcEndpointAccessResponse**](ListVpcEndpointAccessResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listVpcEndpoints

> ListVpcEndpointsResponse listVpcEndpoints(opts)



Retrieves all Amazon OpenSearch Service-managed VPC endpoints in the current account and Region.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | Identifier to allow retrieval of paginated results.
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
 **nextToken** | **String**| Identifier to allow retrieval of paginated results. | [optional] 

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
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let domainName = "domainName_example"; // String | Name of the ElasticSearch domain whose VPC endpoints are to be listed.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | Provides an identifier to allow retrieval of paginated results.
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
 **domainName** | **String**| Name of the ElasticSearch domain whose VPC endpoints are to be listed. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| Provides an identifier to allow retrieval of paginated results. | [optional] 

### Return type

[**ListVpcEndpointsForDomainResponse**](ListVpcEndpointsForDomainResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## purchaseReservedElasticsearchInstanceOffering

> PurchaseReservedElasticsearchInstanceOfferingResponse purchaseReservedElasticsearchInstanceOffering(purchaseReservedElasticsearchInstanceOfferingRequest, opts)



Allows you to purchase reserved Elasticsearch instances.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let purchaseReservedElasticsearchInstanceOfferingRequest = new AmazonElasticsearchService.PurchaseReservedElasticsearchInstanceOfferingRequest(); // PurchaseReservedElasticsearchInstanceOfferingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.purchaseReservedElasticsearchInstanceOffering(purchaseReservedElasticsearchInstanceOfferingRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchaseReservedElasticsearchInstanceOfferingRequest** | [**PurchaseReservedElasticsearchInstanceOfferingRequest**](PurchaseReservedElasticsearchInstanceOfferingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PurchaseReservedElasticsearchInstanceOfferingResponse**](PurchaseReservedElasticsearchInstanceOfferingResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## rejectInboundCrossClusterSearchConnection

> RejectInboundCrossClusterSearchConnectionResponse rejectInboundCrossClusterSearchConnection(connectionId, opts)



Allows the destination domain owner to reject an inbound cross-cluster search connection request.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let connectionId = "connectionId_example"; // String | The id of the inbound connection that you want to reject.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.rejectInboundCrossClusterSearchConnection(connectionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectionId** | **String**| The id of the inbound connection that you want to reject. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RejectInboundCrossClusterSearchConnectionResponse**](RejectInboundCrossClusterSearchConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeTags

> removeTags(removeTagsRequest, opts)



Removes the specified set of tags from the specified Elasticsearch domain.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let removeTagsRequest = new AmazonElasticsearchService.RemoveTagsRequest(); // RemoveTagsRequest | 
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
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the OpenSearch Service domain.
let revokeVpcEndpointAccessRequest = new AmazonElasticsearchService.RevokeVpcEndpointAccessRequest(); // RevokeVpcEndpointAccessRequest | 
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


## startElasticsearchServiceSoftwareUpdate

> StartElasticsearchServiceSoftwareUpdateResponse startElasticsearchServiceSoftwareUpdate(cancelElasticsearchServiceSoftwareUpdateRequest, opts)



Schedules a service software update for an Amazon ES domain.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let cancelElasticsearchServiceSoftwareUpdateRequest = new AmazonElasticsearchService.CancelElasticsearchServiceSoftwareUpdateRequest(); // CancelElasticsearchServiceSoftwareUpdateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startElasticsearchServiceSoftwareUpdate(cancelElasticsearchServiceSoftwareUpdateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancelElasticsearchServiceSoftwareUpdateRequest** | [**CancelElasticsearchServiceSoftwareUpdateRequest**](CancelElasticsearchServiceSoftwareUpdateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartElasticsearchServiceSoftwareUpdateResponse**](StartElasticsearchServiceSoftwareUpdateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateElasticsearchDomainConfig

> UpdateElasticsearchDomainConfigResponse updateElasticsearchDomainConfig(domainName, updateElasticsearchDomainConfigRequest, opts)



Modifies the cluster configuration of the specified Elasticsearch domain, setting as setting the instance type and the number of instances. 

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let domainName = "domainName_example"; // String | The name of the Elasticsearch domain that you are updating. 
let updateElasticsearchDomainConfigRequest = new AmazonElasticsearchService.UpdateElasticsearchDomainConfigRequest(); // UpdateElasticsearchDomainConfigRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateElasticsearchDomainConfig(domainName, updateElasticsearchDomainConfigRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domainName** | **String**| The name of the Elasticsearch domain that you are updating.  | 
 **updateElasticsearchDomainConfigRequest** | [**UpdateElasticsearchDomainConfigRequest**](UpdateElasticsearchDomainConfigRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateElasticsearchDomainConfigResponse**](UpdateElasticsearchDomainConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePackage

> UpdatePackageResponse updatePackage(updatePackageRequest, opts)



Updates a package for use with Amazon ES domains.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let updatePackageRequest = new AmazonElasticsearchService.UpdatePackageRequest(); // UpdatePackageRequest | 
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


## updateVpcEndpoint

> UpdateVpcEndpointResponse updateVpcEndpoint(updateVpcEndpointRequest, opts)



Modifies an Amazon OpenSearch Service-managed interface VPC endpoint.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let updateVpcEndpointRequest = new AmazonElasticsearchService.UpdateVpcEndpointRequest(); // UpdateVpcEndpointRequest | 
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


## upgradeElasticsearchDomain

> UpgradeElasticsearchDomainResponse upgradeElasticsearchDomain(upgradeElasticsearchDomainRequest, opts)



Allows you to either upgrade your domain or perform an Upgrade eligibility check to a compatible Elasticsearch version.

### Example

```javascript
import AmazonElasticsearchService from 'amazon_elasticsearch_service';
let defaultClient = AmazonElasticsearchService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticsearchService.DefaultApi();
let upgradeElasticsearchDomainRequest = new AmazonElasticsearchService.UpgradeElasticsearchDomainRequest(); // UpgradeElasticsearchDomainRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.upgradeElasticsearchDomain(upgradeElasticsearchDomainRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upgradeElasticsearchDomainRequest** | [**UpgradeElasticsearchDomainRequest**](UpgradeElasticsearchDomainRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpgradeElasticsearchDomainResponse**](UpgradeElasticsearchDomainResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

