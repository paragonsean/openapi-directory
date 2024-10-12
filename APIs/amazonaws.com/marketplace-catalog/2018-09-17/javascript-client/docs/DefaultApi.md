# AwsMarketplaceCatalogService.DefaultApi

All URIs are relative to *http://catalog.marketplace.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelChangeSet**](DefaultApi.md#cancelChangeSet) | **PATCH** /CancelChangeSet#catalog&amp;changeSetId | 
[**deleteResourcePolicy**](DefaultApi.md#deleteResourcePolicy) | **DELETE** /DeleteResourcePolicy#resourceArn | 
[**describeChangeSet**](DefaultApi.md#describeChangeSet) | **GET** /DescribeChangeSet#catalog&amp;changeSetId | 
[**describeEntity**](DefaultApi.md#describeEntity) | **GET** /DescribeEntity#catalog&amp;entityId | 
[**getResourcePolicy**](DefaultApi.md#getResourcePolicy) | **GET** /GetResourcePolicy#resourceArn | 
[**listChangeSets**](DefaultApi.md#listChangeSets) | **POST** /ListChangeSets | 
[**listEntities**](DefaultApi.md#listEntities) | **POST** /ListEntities | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /ListTagsForResource | 
[**putResourcePolicy**](DefaultApi.md#putResourcePolicy) | **POST** /PutResourcePolicy | 
[**startChangeSet**](DefaultApi.md#startChangeSet) | **POST** /StartChangeSet | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /TagResource | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /UntagResource | 



## cancelChangeSet

> CancelChangeSetResponse cancelChangeSet(catalog, changeSetId, opts)



Used to cancel an open change request. Must be sent before the status of the request changes to &lt;code&gt;APPLYING&lt;/code&gt;, the final stage of completing your change request. You can describe a change during the 60-day request history retention period for API calls.

### Example

```javascript
import AwsMarketplaceCatalogService from 'aws_marketplace_catalog_service';
let defaultClient = AwsMarketplaceCatalogService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMarketplaceCatalogService.DefaultApi();
let catalog = "catalog_example"; // String | Required. The catalog related to the request. Fixed value: <code>AWSMarketplace</code>.
let changeSetId = "changeSetId_example"; // String | Required. The unique identifier of the <code>StartChangeSet</code> request that you want to cancel.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.cancelChangeSet(catalog, changeSetId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **String**| Required. The catalog related to the request. Fixed value: &lt;code&gt;AWSMarketplace&lt;/code&gt;. | 
 **changeSetId** | **String**| Required. The unique identifier of the &lt;code&gt;StartChangeSet&lt;/code&gt; request that you want to cancel. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CancelChangeSetResponse**](CancelChangeSetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteResourcePolicy

> Object deleteResourcePolicy(resourceArn, opts)



Deletes a resource-based policy on an Entity that is identified by its resource ARN.

### Example

```javascript
import AwsMarketplaceCatalogService from 'aws_marketplace_catalog_service';
let defaultClient = AwsMarketplaceCatalogService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMarketplaceCatalogService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the Entity resource that is associated with the resource policy.
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the Entity resource that is associated with the resource policy. | 
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


## describeChangeSet

> DescribeChangeSetResponse describeChangeSet(catalog, changeSetId, opts)



Provides information about a given change set.

### Example

```javascript
import AwsMarketplaceCatalogService from 'aws_marketplace_catalog_service';
let defaultClient = AwsMarketplaceCatalogService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMarketplaceCatalogService.DefaultApi();
let catalog = "catalog_example"; // String | Required. The catalog related to the request. Fixed value: <code>AWSMarketplace</code> 
let changeSetId = "changeSetId_example"; // String | Required. The unique identifier for the <code>StartChangeSet</code> request that you want to describe the details for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeChangeSet(catalog, changeSetId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **String**| Required. The catalog related to the request. Fixed value: &lt;code&gt;AWSMarketplace&lt;/code&gt;  | 
 **changeSetId** | **String**| Required. The unique identifier for the &lt;code&gt;StartChangeSet&lt;/code&gt; request that you want to describe the details for. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeChangeSetResponse**](DescribeChangeSetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeEntity

> DescribeEntityResponse describeEntity(catalog, entityId, opts)



Returns the metadata and content of the entity.

### Example

```javascript
import AwsMarketplaceCatalogService from 'aws_marketplace_catalog_service';
let defaultClient = AwsMarketplaceCatalogService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMarketplaceCatalogService.DefaultApi();
let catalog = "catalog_example"; // String | Required. The catalog related to the request. Fixed value: <code>AWSMarketplace</code> 
let entityId = "entityId_example"; // String | Required. The unique ID of the entity to describe.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeEntity(catalog, entityId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **String**| Required. The catalog related to the request. Fixed value: &lt;code&gt;AWSMarketplace&lt;/code&gt;  | 
 **entityId** | **String**| Required. The unique ID of the entity to describe. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeEntityResponse**](DescribeEntityResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getResourcePolicy

> GetResourcePolicyResponse getResourcePolicy(resourceArn, opts)



Gets a resource-based policy of an Entity that is identified by its resource ARN.

### Example

```javascript
import AwsMarketplaceCatalogService from 'aws_marketplace_catalog_service';
let defaultClient = AwsMarketplaceCatalogService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMarketplaceCatalogService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the Entity resource that is associated with the resource policy.
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the Entity resource that is associated with the resource policy. | 
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


## listChangeSets

> ListChangeSetsResponse listChangeSets(listChangeSetsRequest, opts)



&lt;p&gt;Returns the list of change sets owned by the account being used to make the call. You can filter this list by providing any combination of &lt;code&gt;entityId&lt;/code&gt;, &lt;code&gt;ChangeSetName&lt;/code&gt;, and status. If you provide more than one filter, the API operation applies a logical AND between the filters.&lt;/p&gt; &lt;p&gt;You can describe a change during the 60-day request history retention period for API calls.&lt;/p&gt;

### Example

```javascript
import AwsMarketplaceCatalogService from 'aws_marketplace_catalog_service';
let defaultClient = AwsMarketplaceCatalogService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMarketplaceCatalogService.DefaultApi();
let listChangeSetsRequest = new AwsMarketplaceCatalogService.ListChangeSetsRequest(); // ListChangeSetsRequest | 
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
apiInstance.listChangeSets(listChangeSetsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listChangeSetsRequest** | [**ListChangeSetsRequest**](ListChangeSetsRequest.md)|  | 
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

[**ListChangeSetsResponse**](ListChangeSetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listEntities

> ListEntitiesResponse listEntities(listEntitiesRequest, opts)



Provides the list of entities of a given type.

### Example

```javascript
import AwsMarketplaceCatalogService from 'aws_marketplace_catalog_service';
let defaultClient = AwsMarketplaceCatalogService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMarketplaceCatalogService.DefaultApi();
let listEntitiesRequest = new AwsMarketplaceCatalogService.ListEntitiesRequest(); // ListEntitiesRequest | 
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
apiInstance.listEntities(listEntitiesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listEntitiesRequest** | [**ListEntitiesRequest**](ListEntitiesRequest.md)|  | 
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

[**ListEntitiesResponse**](ListEntitiesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(listTagsForResourceRequest, opts)



Lists all tags that have been added to a resource (either an &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#catalog-api-entities\&quot;&gt;entity&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets\&quot;&gt;change set&lt;/a&gt;).

### Example

```javascript
import AwsMarketplaceCatalogService from 'aws_marketplace_catalog_service';
let defaultClient = AwsMarketplaceCatalogService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMarketplaceCatalogService.DefaultApi();
let listTagsForResourceRequest = new AwsMarketplaceCatalogService.ListTagsForResourceRequest(); // ListTagsForResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(listTagsForResourceRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listTagsForResourceRequest** | [**ListTagsForResourceRequest**](ListTagsForResourceRequest.md)|  | 
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

- **Content-Type**: application/json
- **Accept**: application/json


## putResourcePolicy

> Object putResourcePolicy(putResourcePolicyRequest, opts)



Attaches a resource-based policy to an Entity. Examples of an entity include: &lt;code&gt;AmiProduct&lt;/code&gt; and &lt;code&gt;ContainerProduct&lt;/code&gt;.

### Example

```javascript
import AwsMarketplaceCatalogService from 'aws_marketplace_catalog_service';
let defaultClient = AwsMarketplaceCatalogService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMarketplaceCatalogService.DefaultApi();
let putResourcePolicyRequest = new AwsMarketplaceCatalogService.PutResourcePolicyRequest(); // PutResourcePolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putResourcePolicy(putResourcePolicyRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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


## startChangeSet

> StartChangeSetResponse startChangeSet(startChangeSetRequest, opts)



&lt;p&gt;Allows you to request changes for your entities. Within a single &lt;code&gt;ChangeSet&lt;/code&gt;, you can&#39;t start the same change type against the same entity multiple times. Additionally, when a &lt;code&gt;ChangeSet&lt;/code&gt; is running, all the entities targeted by the different changes are locked until the change set has completed (either succeeded, cancelled, or failed). If you try to start a change set containing a change against an entity that is already locked, you will receive a &lt;code&gt;ResourceInUseException&lt;/code&gt; error.&lt;/p&gt; &lt;p&gt;For example, you can&#39;t start the &lt;code&gt;ChangeSet&lt;/code&gt; described in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_StartChangeSet.html#API_StartChangeSet_Examples\&quot;&gt;example&lt;/a&gt; later in this topic because it contains two changes to run the same change type (&lt;code&gt;AddRevisions&lt;/code&gt;) against the same entity (&lt;code&gt;entity-id@1&lt;/code&gt;).&lt;/p&gt; &lt;p&gt;For more information about working with change sets, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets\&quot;&gt; Working with change sets&lt;/a&gt;. For information on change types for single-AMI products, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/ami-products.html#working-with-single-AMI-products\&quot;&gt;Working with single-AMI products&lt;/a&gt;. Als, for more information on change types available for container-based products, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/container-products.html#working-with-container-products\&quot;&gt;Working with container products&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsMarketplaceCatalogService from 'aws_marketplace_catalog_service';
let defaultClient = AwsMarketplaceCatalogService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMarketplaceCatalogService.DefaultApi();
let startChangeSetRequest = new AwsMarketplaceCatalogService.StartChangeSetRequest(); // StartChangeSetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startChangeSet(startChangeSetRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startChangeSetRequest** | [**StartChangeSetRequest**](StartChangeSetRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartChangeSetResponse**](StartChangeSetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(tagResourceRequest, opts)



Tags a resource (either an &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#catalog-api-entities\&quot;&gt;entity&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets\&quot;&gt;change set&lt;/a&gt;).

### Example

```javascript
import AwsMarketplaceCatalogService from 'aws_marketplace_catalog_service';
let defaultClient = AwsMarketplaceCatalogService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMarketplaceCatalogService.DefaultApi();
let tagResourceRequest = new AwsMarketplaceCatalogService.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(tagResourceRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

> Object untagResource(untagResourceRequest, opts)



Removes a tag or list of tags from a resource (either an &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#catalog-api-entities\&quot;&gt;entity&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets\&quot;&gt;change set&lt;/a&gt;).

### Example

```javascript
import AwsMarketplaceCatalogService from 'aws_marketplace_catalog_service';
let defaultClient = AwsMarketplaceCatalogService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMarketplaceCatalogService.DefaultApi();
let untagResourceRequest = new AwsMarketplaceCatalogService.UntagResourceRequest(); // UntagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(untagResourceRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

