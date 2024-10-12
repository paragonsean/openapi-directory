# AmazonVpcLattice.DefaultApi

All URIs are relative to *http://vpc-lattice.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchUpdateRule**](DefaultApi.md#batchUpdateRule) | **PATCH** /services/{serviceIdentifier}/listeners/{listenerIdentifier}/rules | 
[**createAccessLogSubscription**](DefaultApi.md#createAccessLogSubscription) | **POST** /accesslogsubscriptions | 
[**createListener**](DefaultApi.md#createListener) | **POST** /services/{serviceIdentifier}/listeners | 
[**createRule**](DefaultApi.md#createRule) | **POST** /services/{serviceIdentifier}/listeners/{listenerIdentifier}/rules | 
[**createService**](DefaultApi.md#createService) | **POST** /services | 
[**createServiceNetwork**](DefaultApi.md#createServiceNetwork) | **POST** /servicenetworks | 
[**createServiceNetworkServiceAssociation**](DefaultApi.md#createServiceNetworkServiceAssociation) | **POST** /servicenetworkserviceassociations | 
[**createServiceNetworkVpcAssociation**](DefaultApi.md#createServiceNetworkVpcAssociation) | **POST** /servicenetworkvpcassociations | 
[**createTargetGroup**](DefaultApi.md#createTargetGroup) | **POST** /targetgroups | 
[**deleteAccessLogSubscription**](DefaultApi.md#deleteAccessLogSubscription) | **DELETE** /accesslogsubscriptions/{accessLogSubscriptionIdentifier} | 
[**deleteAuthPolicy**](DefaultApi.md#deleteAuthPolicy) | **DELETE** /authpolicy/{resourceIdentifier} | 
[**deleteListener**](DefaultApi.md#deleteListener) | **DELETE** /services/{serviceIdentifier}/listeners/{listenerIdentifier} | 
[**deleteResourcePolicy**](DefaultApi.md#deleteResourcePolicy) | **DELETE** /resourcepolicy/{resourceArn} | 
[**deleteRule**](DefaultApi.md#deleteRule) | **DELETE** /services/{serviceIdentifier}/listeners/{listenerIdentifier}/rules/{ruleIdentifier} | 
[**deleteService**](DefaultApi.md#deleteService) | **DELETE** /services/{serviceIdentifier} | 
[**deleteServiceNetwork**](DefaultApi.md#deleteServiceNetwork) | **DELETE** /servicenetworks/{serviceNetworkIdentifier} | 
[**deleteServiceNetworkServiceAssociation**](DefaultApi.md#deleteServiceNetworkServiceAssociation) | **DELETE** /servicenetworkserviceassociations/{serviceNetworkServiceAssociationIdentifier} | 
[**deleteServiceNetworkVpcAssociation**](DefaultApi.md#deleteServiceNetworkVpcAssociation) | **DELETE** /servicenetworkvpcassociations/{serviceNetworkVpcAssociationIdentifier} | 
[**deleteTargetGroup**](DefaultApi.md#deleteTargetGroup) | **DELETE** /targetgroups/{targetGroupIdentifier} | 
[**deregisterTargets**](DefaultApi.md#deregisterTargets) | **POST** /targetgroups/{targetGroupIdentifier}/deregistertargets | 
[**getAccessLogSubscription**](DefaultApi.md#getAccessLogSubscription) | **GET** /accesslogsubscriptions/{accessLogSubscriptionIdentifier} | 
[**getAuthPolicy**](DefaultApi.md#getAuthPolicy) | **GET** /authpolicy/{resourceIdentifier} | 
[**getListener**](DefaultApi.md#getListener) | **GET** /services/{serviceIdentifier}/listeners/{listenerIdentifier} | 
[**getResourcePolicy**](DefaultApi.md#getResourcePolicy) | **GET** /resourcepolicy/{resourceArn} | 
[**getRule**](DefaultApi.md#getRule) | **GET** /services/{serviceIdentifier}/listeners/{listenerIdentifier}/rules/{ruleIdentifier} | 
[**getService**](DefaultApi.md#getService) | **GET** /services/{serviceIdentifier} | 
[**getServiceNetwork**](DefaultApi.md#getServiceNetwork) | **GET** /servicenetworks/{serviceNetworkIdentifier} | 
[**getServiceNetworkServiceAssociation**](DefaultApi.md#getServiceNetworkServiceAssociation) | **GET** /servicenetworkserviceassociations/{serviceNetworkServiceAssociationIdentifier} | 
[**getServiceNetworkVpcAssociation**](DefaultApi.md#getServiceNetworkVpcAssociation) | **GET** /servicenetworkvpcassociations/{serviceNetworkVpcAssociationIdentifier} | 
[**getTargetGroup**](DefaultApi.md#getTargetGroup) | **GET** /targetgroups/{targetGroupIdentifier} | 
[**listAccessLogSubscriptions**](DefaultApi.md#listAccessLogSubscriptions) | **GET** /accesslogsubscriptions#resourceIdentifier | 
[**listListeners**](DefaultApi.md#listListeners) | **GET** /services/{serviceIdentifier}/listeners | 
[**listRules**](DefaultApi.md#listRules) | **GET** /services/{serviceIdentifier}/listeners/{listenerIdentifier}/rules | 
[**listServiceNetworkServiceAssociations**](DefaultApi.md#listServiceNetworkServiceAssociations) | **GET** /servicenetworkserviceassociations | 
[**listServiceNetworkVpcAssociations**](DefaultApi.md#listServiceNetworkVpcAssociations) | **GET** /servicenetworkvpcassociations | 
[**listServiceNetworks**](DefaultApi.md#listServiceNetworks) | **GET** /servicenetworks | 
[**listServices**](DefaultApi.md#listServices) | **GET** /services | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**listTargetGroups**](DefaultApi.md#listTargetGroups) | **GET** /targetgroups | 
[**listTargets**](DefaultApi.md#listTargets) | **POST** /targetgroups/{targetGroupIdentifier}/listtargets | 
[**putAuthPolicy**](DefaultApi.md#putAuthPolicy) | **PUT** /authpolicy/{resourceIdentifier} | 
[**putResourcePolicy**](DefaultApi.md#putResourcePolicy) | **PUT** /resourcepolicy/{resourceArn} | 
[**registerTargets**](DefaultApi.md#registerTargets) | **POST** /targetgroups/{targetGroupIdentifier}/registertargets | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updateAccessLogSubscription**](DefaultApi.md#updateAccessLogSubscription) | **PATCH** /accesslogsubscriptions/{accessLogSubscriptionIdentifier} | 
[**updateListener**](DefaultApi.md#updateListener) | **PATCH** /services/{serviceIdentifier}/listeners/{listenerIdentifier} | 
[**updateRule**](DefaultApi.md#updateRule) | **PATCH** /services/{serviceIdentifier}/listeners/{listenerIdentifier}/rules/{ruleIdentifier} | 
[**updateService**](DefaultApi.md#updateService) | **PATCH** /services/{serviceIdentifier} | 
[**updateServiceNetwork**](DefaultApi.md#updateServiceNetwork) | **PATCH** /servicenetworks/{serviceNetworkIdentifier} | 
[**updateServiceNetworkVpcAssociation**](DefaultApi.md#updateServiceNetworkVpcAssociation) | **PATCH** /servicenetworkvpcassociations/{serviceNetworkVpcAssociationIdentifier} | 
[**updateTargetGroup**](DefaultApi.md#updateTargetGroup) | **PATCH** /targetgroups/{targetGroupIdentifier} | 



## batchUpdateRule

> BatchUpdateRuleResponse batchUpdateRule(listenerIdentifier, serviceIdentifier, batchUpdateRuleRequest, opts)



Updates the listener rules in a batch. You can use this operation to change the priority of listener rules. This can be useful when bulk updating or swapping rule priority. 

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let listenerIdentifier = "listenerIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the listener.
let serviceIdentifier = "serviceIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the service.
let batchUpdateRuleRequest = new AmazonVpcLattice.BatchUpdateRuleRequest(); // BatchUpdateRuleRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchUpdateRule(listenerIdentifier, serviceIdentifier, batchUpdateRuleRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listenerIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the listener. | 
 **serviceIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service. | 
 **batchUpdateRuleRequest** | [**BatchUpdateRuleRequest**](BatchUpdateRuleRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchUpdateRuleResponse**](BatchUpdateRuleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAccessLogSubscription

> CreateAccessLogSubscriptionResponse createAccessLogSubscription(createAccessLogSubscriptionRequest, opts)



Enables access logs to be sent to Amazon CloudWatch, Amazon S3, and Amazon Kinesis Data Firehose. The service network owner can use the access logs to audit the services in the network. The service network owner will only see access logs from clients and services that are associated with their service network. Access log entries represent traffic originated from VPCs associated with that network. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-access-logs.html\&quot;&gt;Access logs&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let createAccessLogSubscriptionRequest = new AmazonVpcLattice.CreateAccessLogSubscriptionRequest(); // CreateAccessLogSubscriptionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAccessLogSubscription(createAccessLogSubscriptionRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createAccessLogSubscriptionRequest** | [**CreateAccessLogSubscriptionRequest**](CreateAccessLogSubscriptionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAccessLogSubscriptionResponse**](CreateAccessLogSubscriptionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createListener

> CreateListenerResponse createListener(serviceIdentifier, createListenerRequest, opts)



Creates a listener for a service. Before you start using your Amazon VPC Lattice service, you must add one or more listeners. A listener is a process that checks for connection requests to your services. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html\&quot;&gt;Listeners&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let serviceIdentifier = "serviceIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the service.
let createListenerRequest = new AmazonVpcLattice.CreateListenerRequest(); // CreateListenerRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createListener(serviceIdentifier, createListenerRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service. | 
 **createListenerRequest** | [**CreateListenerRequest**](CreateListenerRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateListenerResponse**](CreateListenerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRule

> CreateRuleResponse createRule(listenerIdentifier, serviceIdentifier, createRuleRequest, opts)



Creates a listener rule. Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules\&quot;&gt;Listener rules&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let listenerIdentifier = "listenerIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the listener.
let serviceIdentifier = "serviceIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the service.
let createRuleRequest = new AmazonVpcLattice.CreateRuleRequest(); // CreateRuleRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRule(listenerIdentifier, serviceIdentifier, createRuleRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listenerIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the listener. | 
 **serviceIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service. | 
 **createRuleRequest** | [**CreateRuleRequest**](CreateRuleRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateRuleResponse**](CreateRuleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createService

> CreateServiceResponse createService(createServiceRequest, opts)



&lt;p&gt;Creates a service. A service is any software application that can run on instances containers, or serverless functions within an account or virtual private cloud (VPC).&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html\&quot;&gt;Services&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let createServiceRequest = new AmazonVpcLattice.CreateServiceRequest(); // CreateServiceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createService(createServiceRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createServiceRequest** | [**CreateServiceRequest**](CreateServiceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateServiceResponse**](CreateServiceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createServiceNetwork

> CreateServiceNetworkResponse createServiceNetwork(createServiceNetworkRequest, opts)



&lt;p&gt;Creates a service network. A service network is a logical boundary for a collection of services. You can associate services and VPCs with a service network.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html\&quot;&gt;Service networks&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let createServiceNetworkRequest = new AmazonVpcLattice.CreateServiceNetworkRequest(); // CreateServiceNetworkRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createServiceNetwork(createServiceNetworkRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createServiceNetworkRequest** | [**CreateServiceNetworkRequest**](CreateServiceNetworkRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateServiceNetworkResponse**](CreateServiceNetworkResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createServiceNetworkServiceAssociation

> CreateServiceNetworkServiceAssociationResponse createServiceNetworkServiceAssociation(createServiceNetworkServiceAssociationRequest, opts)



&lt;p&gt;Associates a service with a service network.&lt;/p&gt; &lt;p&gt;You can&#39;t use this operation if the service and service network are already associated or if there is a disassociation or deletion in progress. If the association fails, you can retry the operation by deleting the association and recreating it.&lt;/p&gt; &lt;p&gt;You cannot associate a service and service network that are shared with a caller. The caller must own either the service or the service network.&lt;/p&gt; &lt;p&gt;As a result of this operation, the association is created in the service network account and the association owner account.&lt;/p&gt;

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let createServiceNetworkServiceAssociationRequest = new AmazonVpcLattice.CreateServiceNetworkServiceAssociationRequest(); // CreateServiceNetworkServiceAssociationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createServiceNetworkServiceAssociation(createServiceNetworkServiceAssociationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createServiceNetworkServiceAssociationRequest** | [**CreateServiceNetworkServiceAssociationRequest**](CreateServiceNetworkServiceAssociationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateServiceNetworkServiceAssociationResponse**](CreateServiceNetworkServiceAssociationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createServiceNetworkVpcAssociation

> CreateServiceNetworkVpcAssociationResponse createServiceNetworkVpcAssociation(createServiceNetworkVpcAssociationRequest, opts)



&lt;p&gt;Associates a VPC with a service network. When you associate a VPC with the service network, it enables all the resources within that VPC to be clients and communicate with other services in the service network. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-vpc-associations\&quot;&gt;Manage VPC associations&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can&#39;t use this operation if there is a disassociation in progress. If the association fails, retry by deleting the association and recreating it.&lt;/p&gt; &lt;p&gt;As a result of this operation, the association gets created in the service network account and the VPC owner account.&lt;/p&gt; &lt;p&gt;If you add a security group to the service network and VPC association, the association must continue to always have at least one security group. You can add or edit security groups at any time. However, to remove all security groups, you must first delete the association and recreate it without security groups.&lt;/p&gt;

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let createServiceNetworkVpcAssociationRequest = new AmazonVpcLattice.CreateServiceNetworkVpcAssociationRequest(); // CreateServiceNetworkVpcAssociationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createServiceNetworkVpcAssociation(createServiceNetworkVpcAssociationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createServiceNetworkVpcAssociationRequest** | [**CreateServiceNetworkVpcAssociationRequest**](CreateServiceNetworkVpcAssociationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateServiceNetworkVpcAssociationResponse**](CreateServiceNetworkVpcAssociationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTargetGroup

> CreateTargetGroupResponse createTargetGroup(createTargetGroupRequest, opts)



&lt;p&gt;Creates a target group. A target group is a collection of targets, or compute resources, that run your application or service. A target group can only be used by a single service.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html\&quot;&gt;Target groups&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let createTargetGroupRequest = new AmazonVpcLattice.CreateTargetGroupRequest(); // CreateTargetGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createTargetGroup(createTargetGroupRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createTargetGroupRequest** | [**CreateTargetGroupRequest**](CreateTargetGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateTargetGroupResponse**](CreateTargetGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAccessLogSubscription

> Object deleteAccessLogSubscription(accessLogSubscriptionIdentifier, opts)



Deletes the specified access log subscription.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let accessLogSubscriptionIdentifier = "accessLogSubscriptionIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the access log subscription.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAccessLogSubscription(accessLogSubscriptionIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessLogSubscriptionIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the access log subscription. | 
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


## deleteAuthPolicy

> Object deleteAuthPolicy(resourceIdentifier, opts)



Deletes the specified auth policy. If an auth is set to &lt;code&gt;AWS_IAM&lt;/code&gt; and the auth policy is deleted, all requests will be denied by default. If you are trying to remove the auth policy completely, you must set the auth_type to &lt;code&gt;NONE&lt;/code&gt;. If auth is enabled on the resource, but no auth policy is set, all requests will be denied.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let resourceIdentifier = "resourceIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAuthPolicy(resourceIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the resource. | 
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


## deleteListener

> Object deleteListener(listenerIdentifier, serviceIdentifier, opts)



Deletes the specified listener.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let listenerIdentifier = "listenerIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the listener.
let serviceIdentifier = "serviceIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the service.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteListener(listenerIdentifier, serviceIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listenerIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the listener. | 
 **serviceIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service. | 
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


## deleteResourcePolicy

> Object deleteResourcePolicy(resourceArn, opts)



Deletes the specified resource policy.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteResourcePolicy(resourceArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource. | 
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


## deleteRule

> Object deleteRule(listenerIdentifier, ruleIdentifier, serviceIdentifier, opts)



&lt;p&gt;Deletes a listener rule. Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions. You can delete additional listener rules, but you cannot delete the default rule.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules\&quot;&gt;Listener rules&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let listenerIdentifier = "listenerIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the listener.
let ruleIdentifier = "ruleIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the rule.
let serviceIdentifier = "serviceIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the service.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRule(listenerIdentifier, ruleIdentifier, serviceIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listenerIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the listener. | 
 **ruleIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the rule. | 
 **serviceIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service. | 
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


## deleteService

> DeleteServiceResponse deleteService(serviceIdentifier, opts)



Deletes a service. A service can&#39;t be deleted if it&#39;s associated with a service network. If you delete a service, all resources related to the service, such as the resource policy, auth policy, listeners, listener rules, and access log subscriptions, are also deleted. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html#delete-service\&quot;&gt;Delete a service&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let serviceIdentifier = "serviceIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the service.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteService(serviceIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteServiceResponse**](DeleteServiceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteServiceNetwork

> Object deleteServiceNetwork(serviceNetworkIdentifier, opts)



Deletes a service network. You can only delete the service network if there is no service or VPC associated with it. If you delete a service network, all resources related to the service network, such as the resource policy, auth policy, and access log subscriptions, are also deleted. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html#delete-service-network\&quot;&gt;Delete a service network&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let serviceNetworkIdentifier = "serviceNetworkIdentifier_example"; // String | The Amazon Resource Name (ARN) or ID of the service network.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteServiceNetwork(serviceNetworkIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceNetworkIdentifier** | **String**| The Amazon Resource Name (ARN) or ID of the service network. | 
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


## deleteServiceNetworkServiceAssociation

> DeleteServiceNetworkServiceAssociationResponse deleteServiceNetworkServiceAssociation(serviceNetworkServiceAssociationIdentifier, opts)



Deletes the association between a specified service and the specific service network. This request will fail if an association is still in progress.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let serviceNetworkServiceAssociationIdentifier = "serviceNetworkServiceAssociationIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the association.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteServiceNetworkServiceAssociation(serviceNetworkServiceAssociationIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceNetworkServiceAssociationIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the association. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteServiceNetworkServiceAssociationResponse**](DeleteServiceNetworkServiceAssociationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteServiceNetworkVpcAssociation

> DeleteServiceNetworkVpcAssociationResponse deleteServiceNetworkVpcAssociation(serviceNetworkVpcAssociationIdentifier, opts)



Disassociates the VPC from the service network. You can&#39;t disassociate the VPC if there is a create or update association in progress.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let serviceNetworkVpcAssociationIdentifier = "serviceNetworkVpcAssociationIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the association.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteServiceNetworkVpcAssociation(serviceNetworkVpcAssociationIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceNetworkVpcAssociationIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the association. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteServiceNetworkVpcAssociationResponse**](DeleteServiceNetworkVpcAssociationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTargetGroup

> DeleteTargetGroupResponse deleteTargetGroup(targetGroupIdentifier, opts)



Deletes a target group. You can&#39;t delete a target group if it is used in a listener rule or if the target group creation is in progress.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let targetGroupIdentifier = "targetGroupIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the target group.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteTargetGroup(targetGroupIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **targetGroupIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the target group. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteTargetGroupResponse**](DeleteTargetGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deregisterTargets

> DeregisterTargetsResponse deregisterTargets(targetGroupIdentifier, deregisterTargetsRequest, opts)



Deregisters the specified targets from the specified target group.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let targetGroupIdentifier = "targetGroupIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the target group.
let deregisterTargetsRequest = new AmazonVpcLattice.DeregisterTargetsRequest(); // DeregisterTargetsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deregisterTargets(targetGroupIdentifier, deregisterTargetsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **targetGroupIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the target group. | 
 **deregisterTargetsRequest** | [**DeregisterTargetsRequest**](DeregisterTargetsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeregisterTargetsResponse**](DeregisterTargetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAccessLogSubscription

> GetAccessLogSubscriptionResponse getAccessLogSubscription(accessLogSubscriptionIdentifier, opts)



Retrieves information about the specified access log subscription.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let accessLogSubscriptionIdentifier = "accessLogSubscriptionIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the access log subscription.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAccessLogSubscription(accessLogSubscriptionIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessLogSubscriptionIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the access log subscription. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAccessLogSubscriptionResponse**](GetAccessLogSubscriptionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAuthPolicy

> GetAuthPolicyResponse getAuthPolicy(resourceIdentifier, opts)



Retrieves information about the auth policy for the specified service or service network.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let resourceIdentifier = "resourceIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the service network or service.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAuthPolicy(resourceIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service network or service. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAuthPolicyResponse**](GetAuthPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getListener

> GetListenerResponse getListener(listenerIdentifier, serviceIdentifier, opts)



Retrieves information about the specified listener for the specified service.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let listenerIdentifier = "listenerIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the listener.
let serviceIdentifier = "serviceIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the service.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getListener(listenerIdentifier, serviceIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listenerIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the listener. | 
 **serviceIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetListenerResponse**](GetListenerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getResourcePolicy

> GetResourcePolicyResponse getResourcePolicy(resourceArn, opts)



Retrieves information about the resource policy. The resource policy is an IAM policy created on behalf of the resource owner when they share a resource.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the service network or service.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getResourcePolicy(resourceArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the service network or service. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetResourcePolicyResponse**](GetResourcePolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRule

> GetRuleResponse getRule(listenerIdentifier, ruleIdentifier, serviceIdentifier, opts)



Retrieves information about listener rules. You can also retrieve information about the default listener rule. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules\&quot;&gt;Listener rules&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let listenerIdentifier = "listenerIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the listener.
let ruleIdentifier = "ruleIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the listener rule.
let serviceIdentifier = "serviceIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the service.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRule(listenerIdentifier, ruleIdentifier, serviceIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listenerIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the listener. | 
 **ruleIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the listener rule. | 
 **serviceIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRuleResponse**](GetRuleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getService

> GetServiceResponse getService(serviceIdentifier, opts)



Retrieves information about the specified service.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let serviceIdentifier = "serviceIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the service.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getService(serviceIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetServiceResponse**](GetServiceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServiceNetwork

> GetServiceNetworkResponse getServiceNetwork(serviceNetworkIdentifier, opts)



Retrieves information about the specified service network.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let serviceNetworkIdentifier = "serviceNetworkIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the service network.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getServiceNetwork(serviceNetworkIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceNetworkIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service network. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetServiceNetworkResponse**](GetServiceNetworkResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServiceNetworkServiceAssociation

> GetServiceNetworkServiceAssociationResponse getServiceNetworkServiceAssociation(serviceNetworkServiceAssociationIdentifier, opts)



Retrieves information about the specified association between a service network and a service.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let serviceNetworkServiceAssociationIdentifier = "serviceNetworkServiceAssociationIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the association.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getServiceNetworkServiceAssociation(serviceNetworkServiceAssociationIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceNetworkServiceAssociationIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the association. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetServiceNetworkServiceAssociationResponse**](GetServiceNetworkServiceAssociationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServiceNetworkVpcAssociation

> GetServiceNetworkVpcAssociationResponse getServiceNetworkVpcAssociation(serviceNetworkVpcAssociationIdentifier, opts)



Retrieves information about the association between a service network and a VPC.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let serviceNetworkVpcAssociationIdentifier = "serviceNetworkVpcAssociationIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the association.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getServiceNetworkVpcAssociation(serviceNetworkVpcAssociationIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceNetworkVpcAssociationIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the association. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetServiceNetworkVpcAssociationResponse**](GetServiceNetworkVpcAssociationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTargetGroup

> GetTargetGroupResponse getTargetGroup(targetGroupIdentifier, opts)



Retrieves information about the specified target group.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let targetGroupIdentifier = "targetGroupIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the target group.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getTargetGroup(targetGroupIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **targetGroupIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the target group. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetTargetGroupResponse**](GetTargetGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAccessLogSubscriptions

> ListAccessLogSubscriptionsResponse listAccessLogSubscriptions(resourceIdentifier, opts)



Lists all access log subscriptions for the specified service network or service.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let resourceIdentifier = "resourceIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the service network or service.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return.
  'nextToken': "nextToken_example" // String | A pagination token for the next page of results.
};
apiInstance.listAccessLogSubscriptions(resourceIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service network or service. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return. | [optional] 
 **nextToken** | **String**| A pagination token for the next page of results. | [optional] 

### Return type

[**ListAccessLogSubscriptionsResponse**](ListAccessLogSubscriptionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listListeners

> ListListenersResponse listListeners(serviceIdentifier, opts)



Lists the listeners for the specified service.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let serviceIdentifier = "serviceIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the service.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return.
  'nextToken': "nextToken_example" // String | A pagination token for the next page of results.
};
apiInstance.listListeners(serviceIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return. | [optional] 
 **nextToken** | **String**| A pagination token for the next page of results. | [optional] 

### Return type

[**ListListenersResponse**](ListListenersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRules

> ListRulesResponse listRules(listenerIdentifier, serviceIdentifier, opts)



Lists the rules for the listener.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let listenerIdentifier = "listenerIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the listener.
let serviceIdentifier = "serviceIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the service.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return.
  'nextToken': "nextToken_example" // String | A pagination token for the next page of results.
};
apiInstance.listRules(listenerIdentifier, serviceIdentifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listenerIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the listener. | 
 **serviceIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return. | [optional] 
 **nextToken** | **String**| A pagination token for the next page of results. | [optional] 

### Return type

[**ListRulesResponse**](ListRulesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listServiceNetworkServiceAssociations

> ListServiceNetworkServiceAssociationsResponse listServiceNetworkServiceAssociations(opts)



&lt;p&gt;Lists the associations between the service network and the service. You can filter the list either by service or service network. You must provide either the service network identifier or the service identifier.&lt;/p&gt; &lt;p&gt;Every association in Amazon VPC Lattice is given a unique Amazon Resource Name (ARN), such as when a service network is associated with a VPC or when a service is associated with a service network. If the association is for a resource that is shared with another account, the association will include the local account ID as the prefix in the ARN for each account the resource is shared with.&lt;/p&gt;

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return.
  'nextToken': "nextToken_example", // String | A pagination token for the next page of results.
  'serviceIdentifier': "serviceIdentifier_example", // String | The ID or Amazon Resource Name (ARN) of the service.
  'serviceNetworkIdentifier': "serviceNetworkIdentifier_example" // String | The ID or Amazon Resource Name (ARN) of the service network.
};
apiInstance.listServiceNetworkServiceAssociations(opts, (error, data, response) => {
  if (error) {
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
 **maxResults** | **Number**| The maximum number of results to return. | [optional] 
 **nextToken** | **String**| A pagination token for the next page of results. | [optional] 
 **serviceIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service. | [optional] 
 **serviceNetworkIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service network. | [optional] 

### Return type

[**ListServiceNetworkServiceAssociationsResponse**](ListServiceNetworkServiceAssociationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listServiceNetworkVpcAssociations

> ListServiceNetworkVpcAssociationsResponse listServiceNetworkVpcAssociations(opts)



Lists the service network and VPC associations. You can filter the list either by VPC or service network. You must provide either the service network identifier or the VPC identifier.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return.
  'nextToken': "nextToken_example", // String | A pagination token for the next page of results.
  'serviceNetworkIdentifier': "serviceNetworkIdentifier_example", // String | The ID or Amazon Resource Name (ARN) of the service network.
  'vpcIdentifier': "vpcIdentifier_example" // String | The ID or Amazon Resource Name (ARN) of the VPC.
};
apiInstance.listServiceNetworkVpcAssociations(opts, (error, data, response) => {
  if (error) {
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
 **maxResults** | **Number**| The maximum number of results to return. | [optional] 
 **nextToken** | **String**| A pagination token for the next page of results. | [optional] 
 **serviceNetworkIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service network. | [optional] 
 **vpcIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the VPC. | [optional] 

### Return type

[**ListServiceNetworkVpcAssociationsResponse**](ListServiceNetworkVpcAssociationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listServiceNetworks

> ListServiceNetworksResponse listServiceNetworks(opts)



Lists the service networks owned by the caller account or shared with the caller account. Also includes the account ID in the ARN to show which account owns the service network.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return.
  'nextToken': "nextToken_example" // String | A pagination token for the next page of results.
};
apiInstance.listServiceNetworks(opts, (error, data, response) => {
  if (error) {
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
 **maxResults** | **Number**| The maximum number of results to return. | [optional] 
 **nextToken** | **String**| A pagination token for the next page of results. | [optional] 

### Return type

[**ListServiceNetworksResponse**](ListServiceNetworksResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listServices

> ListServicesResponse listServices(opts)



Lists the services owned by the caller account or shared with the caller account.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return.
  'nextToken': "nextToken_example" // String | A pagination token for the next page of results.
};
apiInstance.listServices(opts, (error, data, response) => {
  if (error) {
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
 **maxResults** | **Number**| The maximum number of results to return. | [optional] 
 **nextToken** | **String**| A pagination token for the next page of results. | [optional] 

### Return type

[**ListServicesResponse**](ListServicesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Lists the tags for the specified resource.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource.
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource. | 
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


## listTargetGroups

> ListTargetGroupsResponse listTargetGroups(opts)



Lists your target groups. You can narrow your search by using the filters below in your request.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return.
  'nextToken': "nextToken_example", // String | A pagination token for the next page of results.
  'targetGroupType': "targetGroupType_example", // String | The target group type.
  'vpcIdentifier': "vpcIdentifier_example" // String | The ID or Amazon Resource Name (ARN) of the service.
};
apiInstance.listTargetGroups(opts, (error, data, response) => {
  if (error) {
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
 **maxResults** | **Number**| The maximum number of results to return. | [optional] 
 **nextToken** | **String**| A pagination token for the next page of results. | [optional] 
 **targetGroupType** | **String**| The target group type. | [optional] 
 **vpcIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service. | [optional] 

### Return type

[**ListTargetGroupsResponse**](ListTargetGroupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTargets

> ListTargetsResponse listTargets(targetGroupIdentifier, listTargetsRequest, opts)



Lists the targets for the target group. By default, all targets are included. You can use this API to check the health status of targets. You can also ﬁlter the results by target. 

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let targetGroupIdentifier = "targetGroupIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the target group.
let listTargetsRequest = new AmazonVpcLattice.ListTargetsRequest(); // ListTargetsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return.
  'nextToken': "nextToken_example" // String | A pagination token for the next page of results.
};
apiInstance.listTargets(targetGroupIdentifier, listTargetsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **targetGroupIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the target group. | 
 **listTargetsRequest** | [**ListTargetsRequest**](ListTargetsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return. | [optional] 
 **nextToken** | **String**| A pagination token for the next page of results. | [optional] 

### Return type

[**ListTargetsResponse**](ListTargetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putAuthPolicy

> PutAuthPolicyResponse putAuthPolicy(resourceIdentifier, putAuthPolicyRequest, opts)



Creates or updates the auth policy. The policy string in JSON must not contain newlines or blank lines.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let resourceIdentifier = "resourceIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the service network or service for which the policy is created.
let putAuthPolicyRequest = new AmazonVpcLattice.PutAuthPolicyRequest(); // PutAuthPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putAuthPolicy(resourceIdentifier, putAuthPolicyRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service network or service for which the policy is created. | 
 **putAuthPolicyRequest** | [**PutAuthPolicyRequest**](PutAuthPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutAuthPolicyResponse**](PutAuthPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putResourcePolicy

> Object putResourcePolicy(resourceArn, putResourcePolicyRequest, opts)



Attaches a resource-based permission policy to a service or service network. The policy must contain the same actions and condition statements as the Amazon Web Services Resource Access Manager permission for sharing services and service networks.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ID or Amazon Resource Name (ARN) of the service network or service for which the policy is created.
let putResourcePolicyRequest = new AmazonVpcLattice.PutResourcePolicyRequest(); // PutResourcePolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putResourcePolicy(resourceArn, putResourcePolicyRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceArn** | **String**| The ID or Amazon Resource Name (ARN) of the service network or service for which the policy is created. | 
 **putResourcePolicyRequest** | [**PutResourcePolicyRequest**](PutResourcePolicyRequest.md)|  | 
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


## registerTargets

> RegisterTargetsResponse registerTargets(targetGroupIdentifier, registerTargetsRequest, opts)



Registers the targets with the target group. If it&#39;s a Lambda target, you can only have one target in a target group.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let targetGroupIdentifier = "targetGroupIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the target group.
let registerTargetsRequest = new AmazonVpcLattice.RegisterTargetsRequest(); // RegisterTargetsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.registerTargets(targetGroupIdentifier, registerTargetsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **targetGroupIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the target group. | 
 **registerTargetsRequest** | [**RegisterTargetsRequest**](RegisterTargetsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RegisterTargetsResponse**](RegisterTargetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



Adds the specified tags to the specified resource.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource.
let tagResourceRequest = new AmazonVpcLattice.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource. | 
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



Removes the specified tags from the specified resource.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource.
let tagKeys = ["null"]; // [String] | The tag keys of the tags to remove.
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource. | 
 **tagKeys** | [**[String]**](String.md)| The tag keys of the tags to remove. | 
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


## updateAccessLogSubscription

> UpdateAccessLogSubscriptionResponse updateAccessLogSubscription(accessLogSubscriptionIdentifier, updateAccessLogSubscriptionRequest, opts)



Updates the specified access log subscription.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let accessLogSubscriptionIdentifier = "accessLogSubscriptionIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the access log subscription.
let updateAccessLogSubscriptionRequest = new AmazonVpcLattice.UpdateAccessLogSubscriptionRequest(); // UpdateAccessLogSubscriptionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAccessLogSubscription(accessLogSubscriptionIdentifier, updateAccessLogSubscriptionRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessLogSubscriptionIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the access log subscription. | 
 **updateAccessLogSubscriptionRequest** | [**UpdateAccessLogSubscriptionRequest**](UpdateAccessLogSubscriptionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAccessLogSubscriptionResponse**](UpdateAccessLogSubscriptionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateListener

> UpdateListenerResponse updateListener(listenerIdentifier, serviceIdentifier, updateListenerRequest, opts)



Updates the specified listener for the specified service.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let listenerIdentifier = "listenerIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the listener.
let serviceIdentifier = "serviceIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the service.
let updateListenerRequest = new AmazonVpcLattice.UpdateListenerRequest(); // UpdateListenerRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateListener(listenerIdentifier, serviceIdentifier, updateListenerRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listenerIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the listener. | 
 **serviceIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service. | 
 **updateListenerRequest** | [**UpdateListenerRequest**](UpdateListenerRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateListenerResponse**](UpdateListenerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRule

> UpdateRuleResponse updateRule(listenerIdentifier, ruleIdentifier, serviceIdentifier, updateRuleRequest, opts)



Updates a rule for the listener. You can&#39;t modify a default listener rule. To modify a default listener rule, use &lt;code&gt;UpdateListener&lt;/code&gt;.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let listenerIdentifier = "listenerIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the listener.
let ruleIdentifier = "ruleIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the rule.
let serviceIdentifier = "serviceIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the service.
let updateRuleRequest = new AmazonVpcLattice.UpdateRuleRequest(); // UpdateRuleRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRule(listenerIdentifier, ruleIdentifier, serviceIdentifier, updateRuleRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listenerIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the listener. | 
 **ruleIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the rule. | 
 **serviceIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service. | 
 **updateRuleRequest** | [**UpdateRuleRequest**](UpdateRuleRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateRuleResponse**](UpdateRuleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateService

> UpdateServiceResponse updateService(serviceIdentifier, updateServiceRequest, opts)



Updates the specified service.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let serviceIdentifier = "serviceIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the service.
let updateServiceRequest = new AmazonVpcLattice.UpdateServiceRequest(); // UpdateServiceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateService(serviceIdentifier, updateServiceRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service. | 
 **updateServiceRequest** | [**UpdateServiceRequest**](UpdateServiceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateServiceResponse**](UpdateServiceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateServiceNetwork

> UpdateServiceNetworkResponse updateServiceNetwork(serviceNetworkIdentifier, updateServiceNetworkRequest, opts)



Updates the specified service network.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let serviceNetworkIdentifier = "serviceNetworkIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the service network.
let updateServiceNetworkRequest = new AmazonVpcLattice.UpdateServiceNetworkRequest(); // UpdateServiceNetworkRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateServiceNetwork(serviceNetworkIdentifier, updateServiceNetworkRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceNetworkIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the service network. | 
 **updateServiceNetworkRequest** | [**UpdateServiceNetworkRequest**](UpdateServiceNetworkRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateServiceNetworkResponse**](UpdateServiceNetworkResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateServiceNetworkVpcAssociation

> UpdateServiceNetworkVpcAssociationResponse updateServiceNetworkVpcAssociation(serviceNetworkVpcAssociationIdentifier, updateServiceNetworkVpcAssociationRequest, opts)



Updates the service network and VPC association. If you add a security group to the service network and VPC association, the association must continue to always have at least one security group. You can add or edit security groups at any time. However, to remove all security groups, you must first delete the association and recreate it without security groups.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let serviceNetworkVpcAssociationIdentifier = "serviceNetworkVpcAssociationIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the association.
let updateServiceNetworkVpcAssociationRequest = new AmazonVpcLattice.UpdateServiceNetworkVpcAssociationRequest(); // UpdateServiceNetworkVpcAssociationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateServiceNetworkVpcAssociation(serviceNetworkVpcAssociationIdentifier, updateServiceNetworkVpcAssociationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceNetworkVpcAssociationIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the association. | 
 **updateServiceNetworkVpcAssociationRequest** | [**UpdateServiceNetworkVpcAssociationRequest**](UpdateServiceNetworkVpcAssociationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateServiceNetworkVpcAssociationResponse**](UpdateServiceNetworkVpcAssociationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTargetGroup

> UpdateTargetGroupResponse updateTargetGroup(targetGroupIdentifier, updateTargetGroupRequest, opts)



Updates the specified target group.

### Example

```javascript
import AmazonVpcLattice from 'amazon_vpc_lattice';
let defaultClient = AmazonVpcLattice.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVpcLattice.DefaultApi();
let targetGroupIdentifier = "targetGroupIdentifier_example"; // String | The ID or Amazon Resource Name (ARN) of the target group.
let updateTargetGroupRequest = new AmazonVpcLattice.UpdateTargetGroupRequest(); // UpdateTargetGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateTargetGroup(targetGroupIdentifier, updateTargetGroupRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **targetGroupIdentifier** | **String**| The ID or Amazon Resource Name (ARN) of the target group. | 
 **updateTargetGroupRequest** | [**UpdateTargetGroupRequest**](UpdateTargetGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateTargetGroupResponse**](UpdateTargetGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

